# Ladder — stop at the first rung that holds

1. **Drop it.** Speculative work is not in the contract. Never drop a stated MUST without confirmation.
2. **Reframe the job.** Different mechanism, same outcome. Confirm before changing behavior, contracts, persistence, or acceptance.
3. **Platform.** Language stdlib, framework primitive, OS, database, browser, cloud provider. Native platform controls beat packages.
4. **This repo.** Extend the smallest proven seam. Keep its source of truth.
5. **Collapse or derive.** Merge duplicate flows. Derive state when the authority is available and derivation is cheap and stable. Do not store what you can compute.
6. **Add a part that pays rent.** Current need, why rungs 1–5 lose, owner, failure mode, removal trigger. Reject flexibility justified only by a hypothetical future.

## Worked example — one webhook

Need: "Add a webhook so billing pings us on payout." Climb the rungs:

1. **Drop it.** Stated MUST from the contract — cannot drop without confirmation.
2. **Reframe.** Polling the billing API on a cron would meet the outcome, but adds a worker and a cron surface. Net larger.
3. **Platform.** The cloud provider has a native webhook receiver with retries, signature verification, and an HTTPS endpoint. Use it instead of a new service.
4. **This repo.** Route the receiver to the smallest proven seam that already owns billing state. Keep that seam as the source of truth.
5. **Collapse or derive.** Payout status is derivable from the existing ledger authority — do not store a second copy.
6. **Add a part that pays rent.** Not reached: rung 3 held.

Result: one platform endpoint plus one function on the existing seam. No new service, no queue, no new table.

## Unit of account

Lifecycle surface area, not lines:

code, files, dependencies, services, processes, network hops, queues, caches, stores, public APIs, config knobs, owners, build/release/migration/rollback paths, failure modes.

Complexity pushed onto operators, another team, or "we'll automate it later" still counts.

## Pay rent

A new dependency, service, queue, cache, table, worker, cron, retry path, config surface, public API, network boundary, or build step is expensive. Allow it when it reduces greater whole-system risk now. A single-use wrapper for taste does not pay rent.

## Option generation (material architecture only)

When several real designs compete, name 3–5 independent axes, give each ≥3 values, drop pairwise incompatibilities, keep 3–5 survivors, then pick the smallest survivor that still holds. Do not score before the space exists. Skip this for ordinary CRUD.
