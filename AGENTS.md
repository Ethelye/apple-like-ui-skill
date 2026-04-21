# AI Agent Instructions

This repository packages the `apple-like-ui` design skill for AI coding agents.

## Canonical Guidance

- Treat `SKILL.md` as the canonical skill entrypoint.
- Read `references/apple-hig-synthesis.md` before making Apple-like UI design decisions.
- Use `references/apple-hig-source-index.md` when you need the source map for the downloaded Apple HIG corpus.
- Use `scripts/collect_apple_hig.py` only to refresh the Apple HIG corpus from official Apple JSON endpoints.

## Operating Rules

- Preserve the existing skill structure: `SKILL.md`, `agents/`, `references/`, and `scripts/`.
- Keep `SKILL.md` exactly 236 lines unless the user explicitly asks to change the line count.
- Do not add raw downloaded corpus files, generated caches, screenshots, or extra documentation unless needed for the user's request.
- Avoid copying Apple documentation verbatim into generated code, app copy, or responses.
- Do not clone Apple apps, Apple trademarks, Apple product imagery, or proprietary Apple UI assets.

## UI Work

- Translate Apple HIG principles into the target product instead of applying a generic skin.
- Prioritize content, hierarchy, typography, semantic color, accessibility, adaptive layout, familiar controls, and restrained motion.
- Verify light/dark behavior, responsive layout, focus states, keyboard access, screen-reader labels, and reduced-motion behavior when UI changes are made.

## Publishing

- Push only files needed for the portable skill and compatibility instructions.
- Do not push temporary workspace folders, `apple_hig_corpus/`, `.omx/`, `__pycache__/`, or local auth/config files.
