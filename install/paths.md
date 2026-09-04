# Install paths

Skill bytes live once under `skills/`. Host adapters are thin: plugin manifests point at that tree, or discovery folders symlink into it.

Identical skill bytes. No per-host forks inside `SKILL.md`.

## Host matrix

| Host | How to install | Discovery / adapter | Map |
| --- | --- | --- | --- |
| **Grok Build** | `grok plugin marketplace add tony-sappe/dont-panic` then `grok plugin install dont-panic --trust` — or `grok plugin install <path-or-url> --trust` | `.grok-plugin/marketplace.json` + root `plugin.json` → `skills/` | Merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` |
| **Codex** | `codex plugin marketplace add tony-sappe/dont-panic` then install `dont-panic` — or local-path install | `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json` → `skills/` | Same snippet |
| **Claude Code** | `/plugin marketplace add tony-sappe/dont-panic` then `/plugin install dont-panic@dont-panic` — or `claude --plugin-dir /path/to/dont-panic` | `.claude-plugin/plugin.json` (+ `marketplace.json`) → `skills/` | Same snippet |
| **GitHub CLI** | `gh skill install tony-sappe/dont-panic --all` (optional `--pin vX.Y.Z`) | Discovers `skills/*/SKILL.md` via [agentskills.io](https://agentskills.io) / `gh skill` | Same snippet |
| **Cursor** | Open this repo, or copy/symlink adapters into the target project | `.cursor/skills/<name>` → `skills/<name>` (also discovers `.agents/skills/`) | Same snippet |
| **Windsurf** | Open this repo, or copy/symlink adapters into the target project | `.windsurf/skills/<name>` → `skills/<name>` (also discovers `.agents/skills/`) | Same snippet |
| **OpenClaw** | Point the workspace at this repo, or copy `.openclaw/skills/` | `.openclaw/skills/<name>/SKILL.md` generated from `skills/` with short `description` (<160 chars); body identical; local `references/` symlinked | Same snippet |
| **Hermes Agent** | Copy or symlink `skills/*` into `~/.hermes/skills/` (or a category under it), or open this repo (project `skills/` is discovered) | Canonical `skills/` (no extra Hermes plugin in v1) | Same snippet |
| **Generic / no plugin** | Symlink or copy `skills/*` into the host's skills root | Prefer `.agents/skills/` when the host scans it | Same snippet |

## Adapter layout (this repo)

```text
skills/<name>/SKILL.md          # canonical
.agents/skills/<name>           # symlink → ../../skills/<name>
.cursor/skills/<name>           # symlink → ../../skills/<name>
.windsurf/skills/<name>         # symlink → ../../skills/<name>
.openclaw/skills/<name>/SKILL.md  # generated (short description); body from skills/
.claude-plugin/plugin.json      # Claude Code plugin identity
.codex-plugin/plugin.json       # Codex plugin identity
.grok-plugin/marketplace.json   # Grok marketplace entry
.agents/plugins/marketplace.json
```

## Verify without installing a host

```bash
./scripts/validate.sh
```

That checks canonical skills, required manifests, symlink adapters, and that OpenClaw copies match `./scripts/build-openclaw-skills.sh` output.

## Notes

- **OpenClaw / ClawHub:** short descriptions are generated only under `.openclaw/skills/`. Canonical `skills/` keep the long routing text for other hosts. After editing a skill body or an OpenClaw blurb, run `./scripts/build-openclaw-skills.sh`.
- **Windows:** git symlinks need symlink privilege or Developer Mode. If links arrive as plain text files, recreate them or copy `skills/<name>` into each host folder instead.
- **Always-on rules:** Don't Panic does not ship `.cursor/rules` / `.windsurf/rules` copies. Skills load on demand; use the `AGENTS.md` snippet when you want a short always-on map.
