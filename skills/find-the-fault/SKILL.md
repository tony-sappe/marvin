---
name: find-the-fault
description: Debug with observation, one hypothesis, and one experiment at a time. Use for bugs, incidents, regressions, flaky tests, or when the user says why is this broken, find the fault, root cause, or debug. Do not use for greenfield design or behavior-preserving cleanup, or when the user says skip marvin, no marvin, without marvin, marvin off, or skip find-the-fault.
license: MIT
metadata:
  collection: marvin
  version: "1.4.0"
---

> One hypothesis. One experiment. Then look again.

## Intensity

If intensity is **off**, or the user said skip marvin, no marvin, without marvin, or skip find-the-fault, do not follow this skill this turn. Do the ask. Nothing from this collection.

- **sigh** — short observe → one experiment; log in chat.
- **paranoid** — write a debug log for non-trivial faults; ≤3 cycles then escalate.

## Algorithm

1. **Observe** — facts only. Repro steps, logs, traces, last-good commit, what changed. No patching yet. Ask what data is being ignored.
2. If the situation is on fire (data loss, total outage), stabilize first. Label that **mitigation**, not root cause.
3. If the failing case or change set is large, **reduce it** while the failure predicate stays true: bisect history, or shrink input/config. Record the minimized reproducer and confirm it still matches the original symptom. Primer: `../../thinking-tools.md#fault-isolation`.
4. When the fault is ambiguous and blast radius is high, stamp situation kind + forbidden next move (example: chaotic → do not write architecture; stabilize).
5. Invent **one** hypothesis consistent with the observations. You may list ≤5 ranked candidates with discriminators, but run only one experiment.
6. Make a **prediction** the hypothesis requires.
7. Run **one** experiment that would kill the hypothesis if false. Collecting more data counts. Not twelve changes in parallel.
8. Record: hypothesis / prediction / experiment / observation / conclusion.
9. Match → refine. Miss → replace the hypothesis. Do not silently mutate the hypothesis to fit.
10. Loop ≤3 cycles, then escalate with what is known and what is blocked.
11. Split compound faults into separate trees of causes vs separate trees of fixes — do not mix "why" and "how" in one list. Every leaf must be a check you can run (query, probe, failing test) — not a theme.
12. When the same failure pattern repeats (retries, cache stampede, autoscaling thrash), name stock / flow / polarity / delay / opposing loop and the structural intervention. Primer: `../../thinking-tools.md#feedback-loops`.
13. When you claim a fix, load `prove-it`. Containment without root cause stays labeled mitigation.

## Artifact

Prefer chat table under sigh. Otherwise in the target project:

- `specs/debug-<slug>.md` (create `specs/` if needed)
- or `docs/specs/debug-<slug>.md` if that tree is what the user uses

Template: `references/debug-log-template.md`.

## Communication

Lead with the current cycle row and the next experiment. Not a narrative of every dead end unless asked.

## Anti-patterns

- Skipping Observe
- Panic-patching the first suspicious line
- Renaming flailing as a process
- Twelve experiments in parallel
- Patching the full artifact instead of reducing the reproducer
- Declaring root cause because the patch "seems to help"
