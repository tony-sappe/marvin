<p align="center">
  <img src="./assets/dont-panic-hero.jpg" width="720" alt="Don't Panic — towel optional, skills required">
</p>

<h1 align="center">Don't Panic!</h1>

<p align="center">
  <em>Searching for the Question while navigating the improbability of AI!</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-6-F5C518?style=flat-square&labelColor=111111" alt="6 skills">
  <img src="https://img.shields.io/badge/hosts-Grok%20%7C%20Codex%20%7C%20Claude%20%7C%20Cursor%20%2B-111111?style=flat-square" alt="Works across coding agents">
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license">
</p>

<p align="center">
  <a href="skills/dont-panic/SKILL.md">[dont-panic]</a>
  &middot;
  <a href="skills/bound-the-ask/SKILL.md">[bound-the-ask]</a>
  &middot;
  <a href="skills/pack-light/SKILL.md">[pack-light]</a>
  &middot;
  <a href="skills/prove-it/SKILL.md">[prove-it]</a>
  &middot;
  <a href="skills/find-the-fault/SKILL.md">[find-the-fault]</a>
  &middot;
  <a href="skills/subtract/SKILL.md">[subtract]</a>
</p>


<p align="center">
  <sub>Thinking tools leveraged by Don't Panic!</sub><br>
  <a href="thinking-tools.md#issue-trees">[Issue trees]</a>
  &middot;
  <a href="thinking-tools.md#inversion">[Inversion]</a>
  &middot;
  <a href="thinking-tools.md#abstraction-laddering">[Abstraction laddering]</a>
  &middot;
  <a href="thinking-tools.md#first-principles">[First principles]</a>
  &middot;
  <a href="thinking-tools.md#cynefin">[Cynefin]</a>
  <br>
  <a href="thinking-tools.md#ooda">[OODA]</a>
  &middot;
  <a href="thinking-tools.md#zwicky-box">[Zwicky box]</a>
  &middot;
  <a href="thinking-tools.md#minto-pyramid">[Minto Pyramid]</a>
  &middot;
  <a href="thinking-tools.md#test-bar">[Test bar]</a>
</p>

---

<p align="center">
  <strong>Bound the ask. Pack light. Prove it. Find the fault. Subtract.</strong><br>
  <sub>Portable Agent Skills — one <code>skills/</code> tree, thin host adapters, identical bytes.</sub>
</p>

## Install

Plugin hosts: **Grok Build**, **Codex**, **Claude Code**.  
Discovery adapters in-repo: **Cursor**, **Windsurf**, **OpenClaw**, plus `.agents/skills/`.  
**Hermes:** copy or symlink `skills/*` into `~/.hermes/skills/` (or open this repo).

Full matrix: [`install/paths.md`](install/paths.md) · human notes: [`install/README.md`](install/README.md)

### Grok Build

```bash
grok plugin marketplace add tony-sappe/dont-panic
grok plugin install dont-panic --trust
```

Local checkout:

```bash
grok plugin install /path/to/dont-panic --trust
```

Enable if needed: `/plugins` → Space on `dont-panic`, or in `~/.grok/config.toml`:

```toml
[plugins]
enabled = ["dont-panic"]
```

### Codex

```bash
codex plugin marketplace add tony-sappe/dont-panic
```

Then install **Don't Panic** from `/plugins` (CLI or app). For a local checkout, add this repo as a marketplace source and install `dont-panic`.

### Claude Code

```text
/plugin marketplace add tony-sappe/dont-panic
/plugin install dont-panic@dont-panic
```

Or: `claude --plugin-dir /path/to/dont-panic`.

### Cursor / Windsurf / OpenClaw

Open this checkout (adapters already present), or copy/symlink the matching `.<host>/skills/` tree into your project. Details in [`install/paths.md`](install/paths.md).

### AGENTS.md map

Merge [`install/AGENTS.snippet.md`](install/AGENTS.snippet.md) into the target project's `AGENTS.md` (prepend preferred).

### Intensity

```text
dont-panic lite    # soft challenges, vibe-coding friendly
dont-panic full    # default
dont-panic ultra   # hard gates, failure-first, subtract hard
```

## Skills

| Skill | Job |
| --- | --- |
| `dont-panic` | Intensity dial + route map |
| `bound-the-ask` | Bounded contract before material work |
| `pack-light` | Pack light — smallest complete system you can trust |
| `prove-it` | Named evidence before "done" |
| `find-the-fault` | Observe → one hypothesis → one experiment |
| `subtract` | Behavior-preserving simplification |

Artifacts in the target project go under `specs/` (created if missing), or `docs/specs/` when that tree already exists or the user asks for it.

## Contributing

```bash
./scripts/validate.sh
```

After editing skill bodies or OpenClaw blurbs:

```bash
./scripts/build-openclaw-skills.sh
```

## Thanks
Noteworthy projects inspiring this project:
<a href="https://ponytail.dev">[ponytail]</a> &middot; <a href="https://github.com/obra/superpowers">[superpowers]</a> &middot; <a href="https://github.com/bmad-code-org/BMAD-METHOD">[BMAD Method]</a> &middot; <a href="https://github.com/sudoconnor/first-principles-engineering">[first-principles-engineering]</a>