---
name: find-the-fault
description: Debug with observation, one hypothesis, and one experiment at a time. Use for bugs, incidents, regressions, flaky tests, or when the user says why is this broken, find the fault, root cause, or debug. Do not use for greenfield design or behavior-preserving cleanup.
license: MIT
metadata:
  collection: dont-panic
  version: "1.0"
---

> One hypothesis. One experiment. Then look again.

## Intensity

- **lite** — short observe → one experiment; log in chat.
- **full** — write a debug log for non-trivial faults; ≤3 cycles then escalate.
- **ultra** — formal log always; after ~10 minutes of guessing go formal; no parallel shotgun patches.

## Algorithm

1. **Observe** — facts only. Repro steps, logs, traces, last-good commit, what changed. No patching yet. Ask what data is being ignored.
2. If the situation is on fire (data loss, total outage), stabilize first. Label that **mitigation**, not root cause.
3. When the fault is ambiguous and blast radius is high, stamp situation kind + forbidden next move (example: chaotic → do not write architecture; stabilize).
4. Invent **one** hypothesis consistent with the observations.
5. Make a **prediction** the hypothesis requires.
6. Run **one** experiment that would kill the hypothesis if false. Collecting more data counts. Not twelve changes in parallel.
7. Record: hypothesis / prediction / experiment / observation / conclusion.
8. Match → refine. Miss → replace the hypothesis. Do not silently mutate the hypothesis to fit.
9. Loop ≤3 cycles, then escalate with what is known and what is blocked.
10. Split compound faults into separate trees of causes vs separate trees of fixes — do not mix "why" and "how" in one list. Stop a branch when the leaf is a check you can run.
11. When you claim a fix, load `prove-it`. Containment without root cause stays labeled mitigation.

## Artifact

Prefer chat table under lite. Otherwise in the target project:

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
- Declaring root cause because the patch "seems to help"
