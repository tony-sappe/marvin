<p align="center">
  <img src="./assets/marvin-dont-panic.jpg" width="720" alt="Marvin — He isn't paranoid.">
</p>

<h1 align="center">Marvin</h1>

<p align="center">
  <em>Don't Panic! Marvin is here... unfortunately....</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-6-F5C518?style=flat-square&labelColor=111111" alt="6 skills">
  <img src="https://img.shields.io/badge/hosts-Grok%20%7C%20Codex%20%7C%20Claude%20%7C%20Cursor%20%2B-111111?style=flat-square" alt="Works across coding agents">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license"></a>
</p>

<p align="center">
  <a href="skills/marvin/SKILL.md">[marvin]</a>
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
  <sub>Quick router</sub><br>
  <a href="skill-guide.md">[Which skill for this task?]</a>
</p>

<p align="center">
  <sub>Thinking guide</sub><br>
  <a href="thinking-tools.md#cynefin">[Cynefin]</a>
  &middot;
  <a href="thinking-tools.md#eigenquestions">[Eigenquestions]</a>
  &middot;
  <a href="thinking-tools.md#first-principles">[First principles]</a>
  &middot;
  <a href="thinking-tools.md#abstraction-laddering">[Abstraction laddering]</a>
  <br>
  <a href="thinking-tools.md#inversion">[Inversion]</a>
  &middot;
  <a href="thinking-tools.md#zwicky-box">[Zwicky box]</a>
  &middot;
  <a href="thinking-tools.md#minto-pyramid">[Minto Pyramid]</a>
  &middot;
  <a href="thinking-tools.md#test-bar">[Test bar]</a>
  <br>
  <a href="thinking-tools.md#ooda">[OODA]</a>
  &middot;
  <a href="thinking-tools.md#feedback-loops">[Feedback loops]</a>
  &middot;
  <a href="thinking-tools.md#leverage-points">[Leverage points]</a>
  &middot;
  <a href="thinking-tools.md#issue-trees">[Issue trees]</a>
</p>

---

<p align="center">
  <strong>Bound the ask. Pack light. Prove it. Find the fault. Subtract.</strong><br>
  <sub>A small Agent Skills collection that bounds the scope, travels light, and refuses &ldquo;done&rdquo; without proof.</sub>
</p>

## Install

Works as a plugin on **Grok Build**, **Codex**, and **Claude Code**. Other agents discover skills from this repo (Cursor, Windsurf, OpenClaw, Hermes, and anything that scans `.agents/skills/`).

Commands and host matrix: [`install/README.md`](install/README.md) · [`install/paths.md`](install/paths.md)

```bash
# Grok Build
grok plugin marketplace add tony-sappe/marvin
grok plugin install marvin --trust

# Codex — then install Marvin from /plugins
codex plugin marketplace add tony-sappe/marvin

# Agent Skills via GitHub CLI
gh skill install tony-sappe/marvin --all
```

Claude Code: `/plugin marketplace add tony-sappe/marvin` then `/plugin install marvin@marvin`.

Local checkout, AGENTS.md snippet, and non-plugin hosts: see [`install/`](install/).

Start a **new session** (or reload) after install so the skills appear.

## Usage

After install, say the job in plain language (kebab ids also work: `bound-the-ask`, `pack-light`, …):

- **bound the ask** — ambiguous or multi-file work before coding
- **pack light** — design / new parts / YAGNI
- **prove it** — before calling something done or opening a PR
- **find the fault** — bugs, regressions, flaky tests
- **subtract** — delete or simplify without changing behavior

Examples:

```text
Bound the ask for adding SSO to this app.
Pack light for this design.
Prove it before you open the PR.
Find the fault — checkout fails on Safari only.
Subtract the unused auth helpers.
```

### Intensity

```text
marvin shrug       # soft challenges, vibe-coding friendly
marvin paranoid    # default
marvin big-brain   # hard gates, failure-first, subtract hard
```

## Skills
Full instructions live in [`skills/`](skills/) (`SKILL.md` per skill).

| Skill | Job |
| --- | --- |
| `marvin` | Intensity dial + route map |
| `bound-the-ask` | Bounded contract before material work |
| `pack-light` | Smallest complete system you can trust |
| `prove-it` | Named evidence before "done" |
| `find-the-fault` | Observe → one hypothesis → one experiment |
| `subtract` | Behavior-preserving simplification |

Artifacts in the target project go under `specs/` (or `docs/specs/` when that tree already exists or the user asks for it).


## Contributing

```bash
./scripts/validate.sh
```

After editing skill bodies or OpenClaw blurbs:

```bash
./scripts/build-openclaw-skills.sh
```

## ...and Thanks for All the Fish!

<a href="https://ponytail.dev">[ponytail]</a> · <a href="https://github.com/obra/superpowers">[superpowers]</a> · <a href="https://github.com/bmad-code-org/BMAD-METHOD">[BMAD Method]</a> · <a href="https://github.com/sudoconnor/first-principles-engineering">[first-principles-engineering]</a>

〔[MIT](LICENSE)〕
