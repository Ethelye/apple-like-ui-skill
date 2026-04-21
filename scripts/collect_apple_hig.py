#!/usr/bin/env python3
"""Collect Apple Human Interface Guidelines pages from official JSON endpoints."""

from __future__ import annotations

import argparse
import json
import re
import time
from collections import deque
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests


BASE_URL = "https://developer.apple.com"
DATA_PREFIX = f"{BASE_URL}/tutorials/data"
HIG_PREFIX = "/design/human-interface-guidelines"
DOC_PREFIX = "doc://com.apple.HIG/design/Human-Interface-Guidelines"
USER_AGENT = "Mozilla/5.0 (compatible; Codex HIG collector; +https://developer.apple.com/)"


def slugify(path: str) -> str:
    slug = normalize_path(path).strip("/").replace("/", "__")
    return slug or "index"


def normalize_path(path: str) -> str:
    clean = path.split("#", 1)[0].strip()
    if clean.startswith(BASE_URL):
        clean = urlparse(clean).path
    clean = clean.rstrip("/")
    return clean or HIG_PREFIX


def endpoint_for_path(path: str) -> str:
    clean = normalize_path(path).strip("/")
    return f"{DATA_PREFIX}/{clean}.json"


def public_url(path: str) -> str:
    return f"{BASE_URL}{path}"


def path_from_doc_identifier(identifier: str) -> str | None:
    if not identifier.startswith(DOC_PREFIX):
        return None
    suffix = identifier[len(DOC_PREFIX) :]
    suffix = suffix.split("#", 1)[0].strip("/")
    if suffix:
        return f"{HIG_PREFIX}/{suffix.lower()}"
    return HIG_PREFIX


def path_from_reference(identifier: str) -> str | None:
    if identifier.startswith(DOC_PREFIX):
        return path_from_doc_identifier(identifier)
    if identifier.startswith("http"):
        parsed = urlparse(identifier)
        if parsed.netloc.endswith("developer.apple.com") and parsed.path.startswith(HIG_PREFIX):
            return normalize_path(parsed.path)
    return None


def walk_values(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_values(child)


def inline_text(items: list[dict[str, Any]], refs: dict[str, Any]) -> str:
    parts: list[str] = []
    for item in items:
        item_type = item.get("type")
        if item_type == "text":
            parts.append(item.get("text", ""))
        elif item_type in {"strong", "emphasis"}:
            parts.append(inline_text(item.get("inlineContent", []), refs))
        elif item_type == "codeVoice":
            parts.append(f"`{item.get('code', '')}`")
        elif item_type == "reference":
            title = item.get("overridingTitle")
            if not title:
                ref = refs.get(item.get("identifier", ""), {})
                title = ref.get("title") or ref.get("url") or item.get("identifier", "")
            parts.append(str(title))
        elif item_type == "image":
            caption = ""
            metadata = item.get("metadata") or {}
            abstract = metadata.get("abstract") or []
            if abstract:
                caption = inline_text(abstract, refs)
            if caption:
                parts.append(f"[Image: {caption}]")
        elif "inlineContent" in item:
            parts.append(inline_text(item.get("inlineContent", []), refs))
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def block_text(block: Any, refs: dict[str, Any], level_offset: int = 0) -> list[str]:
    lines: list[str] = []
    if isinstance(block, list):
        for child in block:
            lines.extend(block_text(child, refs, level_offset))
        return lines
    if not isinstance(block, dict):
        return lines

    block_type = block.get("type")
    if block_type == "heading":
        level = int(block.get("level", 2)) + level_offset
        level = min(max(level, 1), 6)
        text = block.get("text", "").strip()
        if text:
            lines.append(f"{'#' * level} {text}")
    elif block_type == "paragraph":
        text = inline_text(block.get("inlineContent", []), refs)
        if text:
            lines.append(text)
    elif block_type in {"unorderedList", "orderedList"}:
        marker_ordered = block_type == "orderedList"
        for idx, item in enumerate(block.get("items", []), start=1):
            item_lines = block_text(item, refs, level_offset)
            if item_lines:
                marker = f"{idx}." if marker_ordered else "-"
                lines.append(f"{marker} {item_lines[0]}")
                for continuation in item_lines[1:]:
                    lines.append(f"  {continuation}")
    elif block_type == "listItem":
        lines.extend(block_text(block.get("content", []), refs, level_offset))
    elif block_type == "row":
        for column in block.get("columns", []):
            lines.extend(block_text(column.get("content", []), refs, level_offset))
    elif block_type == "table":
        rows = block.get("rows", [])
        if rows:
            lines.append("Table:")
            for row in rows[:20]:
                cells: list[str] = []
                for cell in row:
                    cell_text = " ".join(block_text(cell, refs, level_offset))
                    if cell_text:
                        cells.append(cell_text)
                if cells:
                    lines.append("- " + " | ".join(cells))
            if len(rows) > 20:
                lines.append(f"- ... {len(rows) - 20} more rows in raw JSON")
    elif block_type == "links":
        for identifier in block.get("items", []):
            ref = refs.get(identifier, {})
            title = ref.get("title") or identifier
            url = ref.get("url")
            lines.append(f"- {title}" + (f" ({url})" if url else ""))
    elif "content" in block:
        lines.extend(block_text(block.get("content", []), refs, level_offset))
    elif "inlineContent" in block:
        text = inline_text(block.get("inlineContent", []), refs)
        if text:
            lines.append(text)
    return lines


def extract_markdown(data: dict[str, Any], path: str) -> str:
    refs = data.get("references", {})
    metadata = data.get("metadata", {})
    title = metadata.get("title") or path.rsplit("/", 1)[-1].replace("-", " ").title()
    role = metadata.get("role", data.get("kind", ""))
    abstract = inline_text(data.get("abstract", []), refs)

    lines = [
        f"# {title}",
        "",
        f"- Source: {public_url(path)}",
        f"- Role: {role}",
    ]
    if abstract:
        lines.extend(["", abstract])

    content_sections = data.get("primaryContentSections") or data.get("sections") or []
    for section in content_sections:
        section_lines = block_text(section.get("content", section), refs)
        if section_lines:
            lines.extend(["", *section_lines])

    topic_sections = data.get("topicSections") or []
    if topic_sections:
        lines.extend(["", "## Linked HIG pages"])
        seen: set[str] = set()
        for topic in topic_sections:
            for identifier in topic.get("identifiers", []):
                ref = refs.get(identifier, {})
                child_path = path_from_reference(identifier) or ref.get("url")
                title = ref.get("title") or identifier
                key = child_path or identifier
                if key in seen:
                    continue
                seen.add(key)
                lines.append(f"- {title}" + (f" ({child_path})" if child_path else ""))

    return "\n".join(lines).rstrip() + "\n"


def discover_hig_paths(data: dict[str, Any]) -> set[str]:
    found: set[str] = set()
    refs = data.get("references", {})

    for node in walk_values(data):
        identifier = node.get("identifier")
        if isinstance(identifier, str):
            path = path_from_reference(identifier)
            if path:
                found.add(path)
        url = node.get("url")
        if isinstance(url, str) and url.startswith(HIG_PREFIX):
            found.add(normalize_path(url))

    for identifier, ref in refs.items():
        path = path_from_reference(identifier)
        if path:
            found.add(path)
        if isinstance(ref, dict):
            url = ref.get("url")
            if isinstance(url, str) and url.startswith(HIG_PREFIX):
                found.add(normalize_path(url))

    return found


def fetch_json(session: requests.Session, path: str) -> dict[str, Any] | None:
    url = endpoint_for_path(path)
    response = session.get(url, timeout=45)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


def collect(out_dir: Path, start_path: str, delay: float, max_pages: int) -> None:
    raw_dir = out_dir / "raw"
    markdown_dir = out_dir / "markdown"
    raw_dir.mkdir(parents=True, exist_ok=True)
    markdown_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json,text/html;q=0.9"})

    queue: deque[str] = deque([start_path.rstrip("/")])
    seen: set[str] = set()
    index: list[dict[str, Any]] = []
    misses: list[str] = []

    while queue and len(seen) < max_pages:
        path = normalize_path(queue.popleft())
        if path in seen:
            continue
        seen.add(path)

        print(f"Fetching {path}")
        data = fetch_json(session, path)
        if data is None:
            misses.append(path)
            continue

        slug = slugify(path)
        (raw_dir / f"{slug}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        (markdown_dir / f"{slug}.md").write_text(extract_markdown(data, path), encoding="utf-8")

        metadata = data.get("metadata", {})
        index.append(
            {
                "title": metadata.get("title"),
                "role": metadata.get("role", data.get("kind")),
                "path": path,
                "url": public_url(path),
                "raw": str((raw_dir / f"{slug}.json").relative_to(out_dir)).replace("\\", "/"),
                "markdown": str((markdown_dir / f"{slug}.md").relative_to(out_dir)).replace("\\", "/"),
            }
        )

        for child in sorted(discover_hig_paths(data)):
            if child.startswith(HIG_PREFIX) and child not in seen:
                queue.append(child)

        if delay:
            time.sleep(delay)

    index.sort(key=lambda item: item["path"])
    (out_dir / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / "misses.json").write_text(json.dumps(sorted(misses), indent=2), encoding="utf-8")

    by_section: dict[str, list[dict[str, str]]] = {}
    for item in index:
        suffix = item["path"][len(HIG_PREFIX) :].strip("/")
        section = suffix.split("/", 1)[0] if suffix else "overview"
        by_section.setdefault(section, []).append({"title": item["title"], "url": item["url"]})

    summary_lines = [
        "# Apple HIG Corpus Index",
        "",
        f"- Pages collected: {len(index)}",
        f"- Misses: {len(misses)}",
        f"- Start: {public_url(start_path)}",
        "",
    ]
    for section, items in sorted(by_section.items()):
        summary_lines.append(f"## {section}")
        for item in items:
            summary_lines.append(f"- {item['title']}: {item['url']}")
        summary_lines.append("")
    (out_dir / "INDEX.md").write_text("\n".join(summary_lines).rstrip() + "\n", encoding="utf-8")

    print(f"Collected {len(index)} pages into {out_dir}")
    if misses:
        print(f"Skipped {len(misses)} missing paths; see misses.json")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("apple_hig_corpus"), help="Output directory")
    parser.add_argument("--start", default=HIG_PREFIX, help="HIG path to start crawling")
    parser.add_argument("--delay", type=float, default=0.08, help="Delay between requests")
    parser.add_argument("--max-pages", type=int, default=300, help="Safety limit")
    args = parser.parse_args()

    collect(args.out, normalize_path(args.start), args.delay, args.max_pages)


if __name__ == "__main__":
    main()
