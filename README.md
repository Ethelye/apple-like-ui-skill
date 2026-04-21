# Apple-like UI Skill

`apple-like-ui` is an AI coding-agent skill for designing, implementing, and auditing Apple Human Interface Guidelines-inspired interfaces.

It includes:

- `SKILL.md` - the canonical Codex skill entrypoint.
- `references/apple-hig-synthesis.md` - distilled Apple HIG guidance from the downloaded corpus.
- `references/apple-hig-source-index.md` - source map of the collected official Apple HIG pages.
- `scripts/collect_apple_hig.py` - optional Python script to refresh the source corpus from Apple Developer JSON endpoints.
- Agent compatibility files for Codex, Cursor, Claude Code, Gemini CLI, GitHub Copilot, and Aider.

## Install With Skillfish

Skillfish installs skills to all detected AI coding agents on your system.

One-off install:

```bash
npx skillfish add Ethelye/apple-like-ui-skill apple-like-ui
```

If you installed Skillfish globally:

```bash
skillfish add Ethelye/apple-like-ui-skill apple-like-ui
```

Restart your AI coding agent after installation, then invoke the skill with:

```text
Use $apple-like-ui to redesign this screen with Apple-like UI polish.
```

## Manual Codex Install

Use this only if you do not want to use Skillfish.

### Windows PowerShell

```powershell
$skillDir = "$env:USERPROFILE\.codex\skills\apple-like-ui"
git clone https://github.com/Ethelye/apple-like-ui-skill.git $skillDir
```

### macOS Or Linux

```bash
git clone https://github.com/Ethelye/apple-like-ui-skill.git ~/.codex/skills/apple-like-ui
```

## Update

With Skillfish:

```bash
skillfish update
```

Manual Codex update:

### Windows PowerShell

```powershell
git -C "$env:USERPROFILE\.codex\skills\apple-like-ui" pull
```

### macOS Or Linux

```bash
git -C ~/.codex/skills/apple-like-ui pull
```

## Use With Other AI Coding Agents

Skillfish handles supported agents automatically. If you are wiring the repo manually:

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
