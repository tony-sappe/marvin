# Ladder — stop at the first rung that holds

1. **Drop it.** Speculative work is not in the contract. Never drop a stated MUST without confirmation.
2. **Reframe the job.** Different mechanism, same outcome. Confirm before changing behavior, contracts, persistence, or acceptance.
3. **Platform.** Language stdlib, framework primitive, OS, database, browser, cloud provider. Native platform controls beat packages.
4. **This repo.** Extend the smallest proven seam. Keep its source of truth.
5. **Collapse or derive.** Merge duplicate flows. Derive state when the authority is available and derivation is cheap and stable. Do not store what you can compute.
6. **Add a part that pays rent.** Current need, why rungs 1–5 lose, owner, failure mode, removal trigger. Reject flexibility justified only by a hypothetical future.

## Unit of account

Lifecycle surface area, not lines:

code, files, dependencies, services, processes, network hops, queues, caches, stores, public APIs, config knobs, owners, build/release/migration/rollback paths, failure modes.

Complexity pushed onto operators, another team, or "we'll automate it later" still counts.

## Pay rent

A new dependency, service, queue, cache, table, worker, cron, retry path, config surface, public API, network boundary, or build step is expensive. Allow it when it reduces greater whole-system risk now. A single-use wrapper for taste does not pay rent.

## Option generation (material architecture only)

When several real designs compete, name 3–5 independent axes, give each ≥3 values, drop pairwise incompatibilities, keep 3–5 survivors, then pick the smallest survivor that still holds. Do not score before the space exists. Skip this for ordinary CRUD.
