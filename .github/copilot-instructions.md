# GitHub Copilot Instructions

This repository packages the `apple-like-ui` skill.

- Treat `SKILL.md` as the canonical skill entrypoint.
- Read `references/apple-hig-synthesis.md` before making Apple-like UI design decisions.
- Use `references/apple-hig-source-index.md` for source lookup when component or platform details matter.
- Use `scripts/collect_apple_hig.py` only when refreshing the Apple HIG corpus.
- Keep `SKILL.md` exactly 236 lines unless the user explicitly asks to change it.
- Push only files needed for the portable skill and agent compatibility.
- Do not include raw corpus output, generated caches, screenshots, `.omx/`, or local machine state.
