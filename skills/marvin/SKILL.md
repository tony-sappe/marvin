---
name: marvin
description: Set Marvin intensity and remind the skill map. Use when the user says marvin, Marvin, Don't Panic, shrug, paranoid, big-brain, lite, full, ultra, or asks how to use this collection. Do not use as a substitute for bound-the-ask, pack-light, prove-it, find-the-fault, or subtract on the actual work.
license: MIT
metadata:
  collection: marvin
  version: "1.1.1"
---

> Pack the towel. Set the dial. Then do the job.

## Intensity

Default **paranoid** for the session until changed.

| Level | Behavior |
| --- | --- |
| **shrug** | Smallest path. Soft challenges in one line. Written contract optional when the outcome is obvious. Prefer shipping over ceremony. |
| **paranoid** | Matching skill algorithm + safety floor. Ask when the answer changes outcome, cost, or blast radius. |
| **big-brain** | Hard gates on material work. Failure-first pass before design. Aggressive subtraction bias. Refuse "done" without decisive evidence. |

Switch: user says `marvin shrug|paranoid|big-brain`, `/marvin shrug|paranoid|big-brain`, or equivalent. No argument → report the current level in one line, then the map.

Aliases (same ladder): `lite` → shrug, `full` → paranoid, `ultra` → big-brain.

Persist for this conversation only (no hooks). State the level once when it changes. Do not re-preach it every turn.

## Map

Load **one** job skill:

1. **bound-the-ask** — ambiguous or material work; write/confirm the contract when unclear.
2. **pack-light** — design shape and new parts; ladder; stop early.
3. **prove-it** — done, PR, verify; name evidence types.
4. **find-the-fault** — bugs and incidents; one hypothesis, one experiment.
5. **subtract** — refactor and delete; behavior-preserving.

Vibe coding is allowed. Obvious one-file outcomes may go straight to `pack-light` under shrug/paranoid.

## Output

```
intensity: <shrug|paranoid|big-brain>
next: <skill or "say what you want to build">
```

Lead with that. No lore dump.
