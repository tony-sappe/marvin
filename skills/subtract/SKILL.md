---
name: subtract
description: Reduce an existing system while preserving behavior. Use when asked to refactor, simplify, delete dead code, collapse an abstraction, drop a dependency, clean a repo, cut tech debt, or when the user says subtract, simplify, or raptor. Do not use for greenfield design unless existing code is the thing being simplified.
license: MIT
metadata:
  collection: dont-panic
  version: "1.0"
---

> Same behavior. Fewer parts.

## Prime directive

Behavior-preserving unless the user explicitly changes behavior.

One thesis per diff. A thesis is one sentence. "Clean up a bunch of stuff" is not a thesis.

If you find a bug while subtracting, do not silently fix it. Call it out. Preserve it and note it, or make the fix a separate labeled change.

## Intensity

- **lite** — inspection or one surgical cut; stop early.
- **full** — choose a mode; walk the ladder; prove the change.
- **ultra** — aggressive deletion and collapse still behavior-preserving; ranked delete-list first unless the user already named the cut.

## Modes — choose one before editing

1. **Inspection** — findings only. No file edits.
2. **Plan** — staged slices, each reviewable in minutes.
3. **Surgical** — one narrow safe cut, then verify.
4. **Subtract hard** — aggressive deletion and collapse. Still behavior-preserving. Not a rewrite.

Default: inspection if the user has not named a cut. Surgical if they pointed at one thing. Plan if the area is broad. Hard mode only when asked for aggressive simplification or under **ultra** with an explicit go-ahead.

## Ladder

1. Understand current behavior — inputs, outputs, side effects, persistence, callers, tests, routes, jobs, config. Quiet local search is not proof of dead. Understand a part before removing it.
2. Smallest useful cut.
3. Preserve behavior first — run or name the safety net before editing.
4. Delete before adding.
5. Collapse before abstracting. Inline single-use wrappers. Replace interface + one implementation with the implementation.
6. Move invariants closer to the source (types, schema, DB constraints, framework validation).
7. Simplify state — derive, don't duplicate. One source of truth.
8. Dependency diet — stdlib / platform / already installed. Classify keep / replace-with-platform / inline / remove / defer. Search imports, dynamic loads, config, build, tests, generated code before "unused."
9. Prove the change — focused tests, typecheck, build, or a specific manual path. Prefer `prove-it` for the gate.
10. Stop. Leftover opportunities become notes, not drive-by edits.

## Smells

See `references/smells.md`. Name the category in the answer; load the list when hunting.

## Safety

Same floor as `smallest-trusted`. Load `../../references/safety-floor.md` when relevant.

## Communication

Inspection leads with a ranked delete-list: what to remove, why, risk, proof needed.

Surgical/hard modes lead with the thesis, the diff summary, and the proof that behavior held.

## Anti-patterns

- Big-bang rewrite
- Repo-wide format mixed into a logic diff
- Renames for taste
- A new framework to remove duplication
- Adding DI or interfaces "for testability" when a simpler test works
- Combining unrelated refactors
