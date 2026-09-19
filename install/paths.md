# Install paths

Canonical skill instructions live under `skills/`; generated local references make each folder independently installable. Host adapters are thin: plugin manifests point at that tree, or discovery folders symlink into it.

Identical skill bytes. No per-host forks inside `SKILL.md`.

## Host matrix

| Host | How to install | Discovery / adapter | Map |
| --- | --- | --- | --- |
| **Grok Build** | `grok plugin marketplace add tony-sappe/marvin` then `grok plugin install marvin --trust` — or `grok plugin install tony-sappe/marvin --trust` | `.grok-plugin/marketplace.json` (plugin `source` is the git URL) + root `plugin.json` → `skills/` | Merge `install/AGENTS.snippet.md` into the target project's `AGENTS.md` |
| **Codex** | `codex plugin marketplace add tony-sappe/marvin` then `codex plugin add marvin@marvin` — or marketplace-add a local checkout path | `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json` → `skills/` | Same snippet |
| **Claude Code** | `/plugin marketplace add tony-sappe/marvin` then `/plugin install marvin@marvin` — or `claude --plugin-dir /path/to/marvin` | `.claude-plugin/plugin.json` (+ `marketplace.json`) → `skills/` | Same snippet |
| **GitHub CLI** | `gh skill install tony-sappe/marvin --all` | Discovers `skills/*/SKILL.md` via [agentskills.io](https://agentskills.io) / `gh skill` | Same snippet |
| **Cursor** | Open this repo, or use the canonical-folder link/copy commands in [Install](README.md#cursor--windsurf) | `.cursor/skills/<name>` → `skills/<name>` (also discovers `.agents/skills/`) | Same snippet |
| **Windsurf** | Open this repo, or use the canonical-folder link/copy commands in [Install](README.md#cursor--windsurf) | `.windsurf/skills/<name>` → `skills/<name>` | Same snippet |
| **Generic / no plugin** | Link canonical skill folders by absolute path or copy complete `skills/*` folders using [Install](README.md#cursor--windsurf) | Prefer `.agents/skills/` when the host scans it | Same snippet |

## Adapter layout (this repo)

```text
plugin.json                     # Grok plugin identity (repo root)
skills/<name>/SKILL.md          # canonical skill
skills/<name>/references/       # local templates + generated shared guidance
.agents/skills/<name>           # symlink → ../../skills/<name>
.cursor/skills/<name>           # symlink → ../../skills/<name>
.windsurf/skills/<name>         # symlink → ../../skills/<name>
.claude-plugin/plugin.json      # Claude Code plugin identity
.codex-plugin/plugin.json       # Codex plugin identity
.grok-plugin/marketplace.json   # Grok marketplace entry
.agents/plugins/marketplace.json
```

## Verify without installing a host

```bash
./scripts/validate.sh
```

Install the Python/PyYAML development requirements first; see [validation setup](README.md#validate-no-host-clis-required). The validator checks manifests, frontmatter, declared paths, local references, adapters, and the no-hooks policy. Structural PASS is not host-runtime proof.

## Notes

- **Windows:** git symlinks need symlink privilege or Developer Mode. If links arrive as plain text files, use the PowerShell canonical-folder copy procedure in [Install](README.md#cursor--windsurf). Never copy the relative adapter links into another project.
- **Always-on rules:** Marvin does not ship `.cursor/rules` / `.windsurf/rules` copies. Skills load on demand; use the `AGENTS.md` snippet when you want a short always-on map.
