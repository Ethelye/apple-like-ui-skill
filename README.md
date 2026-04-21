# Apple-like UI Skill

`apple-like-ui` is an AI coding-agent skill for designing, implementing, and auditing Apple Human Interface Guidelines-inspired interfaces.

It includes:

- `SKILL.md` - the canonical Codex skill entrypoint.
- `references/apple-hig-synthesis.md` - distilled Apple HIG guidance from the downloaded corpus.
- `references/apple-hig-source-index.md` - source map of the collected official Apple HIG pages.
- `scripts/collect_apple_hig.py` - optional Python script to refresh the source corpus from Apple Developer JSON endpoints.
- Agent compatibility files for Codex, Cursor, Claude Code, Gemini CLI, GitHub Copilot, and Aider.

## Install For Codex

Close any active Codex session that should pick up the new skill, then clone the repo into your Codex skills folder.

### Windows PowerShell

```powershell
$skillDir = "$env:USERPROFILE\.codex\skills\apple-like-ui"
git clone https://github.com/Ethelye/skillfish.git $skillDir
```

### macOS Or Linux

```bash
git clone https://github.com/Ethelye/skillfish.git ~/.codex/skills/apple-like-ui
```

Start a new Codex session and invoke it with:

```text
Use $apple-like-ui to redesign this screen with Apple-like UI polish.
```

## Update

### Windows PowerShell

```powershell
git -C "$env:USERPROFILE\.codex\skills\apple-like-ui" pull
```

### macOS Or Linux

```bash
git -C ~/.codex/skills/apple-like-ui pull
```

## Use With Other AI Coding Agents

Open or clone this repository in the agent's workspace.

- Codex and Cursor-style agents: read `AGENTS.md`.
- Claude Code: reads `CLAUDE.md`, which imports `AGENTS.md`.
- Gemini CLI: reads `GEMINI.md`, which imports `AGENTS.md`.
- GitHub Copilot: reads `.github/copilot-instructions.md` where supported.
- Aider: use `.aider.conf.yml` or read `CONVENTIONS.md`.

For best results, ask the agent to read `SKILL.md` and `references/apple-hig-synthesis.md` before making UI changes.

## Refresh The Apple HIG Corpus

The skill already includes distilled guidance. Refresh only when you need updated Apple HIG source material.

```bash
python scripts/collect_apple_hig.py --out apple_hig_corpus
```

Do not commit the generated `apple_hig_corpus/` output unless you intentionally want to publish the raw corpus.

## Notes

- Keep `SKILL.md` as the canonical source of behavior.
- Keep compatibility files small so they do not drift from `SKILL.md`.
- Do not use this skill to clone Apple apps, trademarks, product imagery, or proprietary Apple UI assets.
