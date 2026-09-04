# Skill guide — what to reach for

Load **one** job skill at a time. Use `marvin` only to set intensity (shrug / paranoid / big-brain) or to recall the map.

| Skill | Reach for it when… |
| --- | --- |
| [`bound-the-ask`](skills/bound-the-ask/SKILL.md) | The outcome, scope, or success bar is unclear — or the work is material enough to need a contract first |
| [`pack-light`](skills/pack-light/SKILL.md) | You are designing or adding parts (API, store, queue, dependency, feature shape) |
| [`prove-it`](skills/prove-it/SKILL.md) | You are about to say done, open a PR, or verify a fix |
| [`find-the-fault`](skills/find-the-fault/SKILL.md) | Something is wrong and the cause is unknown |
| [`subtract`](skills/subtract/SKILL.md) | You want fewer parts with the **same** behavior |

Textbook primers (not job skills): [`thinking-tools.md`](thinking-tools.md).

---

## Task → skill

### Specs, product, and framing

| Task | Skill | Notes |
| --- | --- | --- |
| Draft SDD / specs / a contract | **bound-the-ask** | Write MUST / SHOULD / MAY, scope, stop, proof |
| Bound an ambiguous feature ask | **bound-the-ask** | Eigenquestion if several debates block one another |
| Write acceptance criteria / definition of done | **bound-the-ask** | Then **prove-it** when claiming met |
| “Should we even build this?” | **bound-the-ask** → **pack-light** | Contract first; ladder may stop at “drop it” |
| Prioritize / MoSCoW a backlog slice | **bound-the-ask** | One triage line in the contract — not a new skill |
| ADR / architecture options | **pack-light** | After a contract if the decision is material; use option gen |
| Pick a stack, vendor, or new dependency | **pack-light** | Constraints before analogies; safety floor when relevant |
| Stuck on the wrong question | **bound-the-ask** | Eigenquestion step |
| Claim buried in a long memo / PR body | **bound-the-ask** | Governing sentence first (Minto) |

### Design and implementation

| Task | Skill | Notes |
| --- | --- | --- |
| Implement from a clear spec | **pack-light** | Thin end-to-end slice; then **prove-it** |
| Vibe-code a small obvious feature | **pack-light** | Under shrug, skip a written contract when outcome is obvious |
| Add an API, service, queue, cache, or store | **pack-light** | New parts must pay rent |
| “Is this design too much?” | **pack-light** | Stop at first rung that holds |
| Grow surface area / invent a primitive | **pack-light** | Delete-before-add; `Removed / not built` |
| Dynamic design (retries, autoscaling, caches) | **pack-light** | Name stock / loop / intervention |
| Claimed “high-leverage” architecture change | **pack-light** | Classify leverage rank; prefer structural over knobs |
| Greenfield feature with unclear outcome | **bound-the-ask** → **pack-light** | Do not design inside an unbound ask |

### Bugs, incidents, and performance

| Task | Skill | Notes |
| --- | --- | --- |
| Fix this bug / “why is this broken?” | **find-the-fault** | Observe → one hypothesis → one experiment |
| Production incident / outage | **find-the-fault** | Stabilize first (mitigation ≠ root cause); Cynefin stamp if chaotic |
| Regression after a deploy | **find-the-fault** | Last-good commit is Observe data |
| Flaky test | **find-the-fault** | Then **prove-it** when claiming fixed |
| CI failure with unknown cause | **find-the-fault** | If the failure mode is known and you only need proof, **prove-it** |
| Perf problem (CPU, latency, memory) with unknown cause | **find-the-fault** | e.g. “React app uses too much Chrome memory” → measure first |
| Repeating incident pattern (retry storm, cache stampede) | **find-the-fault** | Name opposing loop; structural fix may later use **pack-light** |
| Suspected misconfig / “it works on my machine” | **find-the-fault** | Prefer misconfig before conspiracy |

### Verification and shipping

| Task | Skill | Notes |
| --- | --- | --- |
| Claim done / check your work | **prove-it** | Name evidence type; cheapest decisive proof |
| Open a PR / review bar | **prove-it** | Optional test-matrix row on material PRs |
| What tests should this change get? | **prove-it** | Blast radius × evidence in hand |
| Verify a fix after debugging | **prove-it** | After **find-the-fault** closes cause |
| Red-green for new behavior | **prove-it** | Prefer failing check that names the behavior |
| Characterization before touching legacy | **prove-it** | Pin behavior, then change (or hand to **subtract**) |

### Cleanup, complexity, and debt

| Task | Skill | Notes |
| --- | --- | --- |
| Reduce codebase complexity without altering behavior | **subtract** | Inspection first unless the cut is already named |
| Delete dead code / unused deps | **subtract** | Quiet search ≠ proof of dead |
| Collapse an abstraction / inline a wrapper | **subtract** | One thesis per diff |
| Refactor for clarity (behavior-preserving) | **subtract** | Not a rewrite; not mixed with feature work |
| Dependency diet / replace with platform | **subtract** or **pack-light** | Existing code → **subtract**; choosing what to add → **pack-light** |
| “Raptor” / aggressive simplify | **subtract** | Hard mode only when asked; still behavior-preserving |
| Reduce memory/CPU by removing known bloat | **subtract** | Cause already known; preserve behavior; prove with **prove-it** |
| Reduce memory/CPU but root cause unknown | **find-the-fault** | Do not subtract randomly |

### DevOps, platform, and operations

| Task | Skill | Notes |
| --- | --- | --- |
| Design a deploy / rollback / migration path | **bound-the-ask** → **pack-light** | Irreversibles and stop condition in the contract |
| Add observability / metrics / tracing | **pack-light** | Pays rent only if it kills a real unknown |
| Capacity / scaling / cost design | **pack-light** | Loops + leverage; avoid parameter-only “architecture” |
| Cut infra cost without changing product behavior | **subtract** | Or **find-the-fault** if “why so expensive?” is unknown |
| On-call: stop the bleed | **find-the-fault** | Act to stabilize; label mitigation |
| Post-incident: prevent recurrence | **bound-the-ask** or **pack-light** | Contract the non-goal / change; design the smallest fix |
| Security-sensitive change (auth, data, money) | **bound-the-ask** → **pack-light** → **prove-it** | Safety floor; high blast always needs stronger proof |
| Feature flag / gradual rollout decision | **bound-the-ask** | Scope and blast in the contract; implement with **pack-light** |

---

## Common sequences

Use the next skill only when the previous job is finished.

| Situation | Order |
| --- | --- |
| Ambiguous feature → ship | **bound-the-ask** → **pack-light** → **prove-it** |
| Bug report → merge | **find-the-fault** → **prove-it** |
| “Make it smaller” with unclear goal | **bound-the-ask** → **subtract** (or **pack-light** if behavior may change) |
| Perf mystery → leaner code | **find-the-fault** → **subtract** or **pack-light** → **prove-it** |
| Known safe delete | **subtract** → **prove-it** |

---

## Tie-breakers

1. **Unknown cause?** → `find-the-fault` before anything else.
2. **Unclear outcome or material blast?** → `bound-the-ask` before design.
3. **Same behavior, fewer parts?** → `subtract`. **New or different behavior?** → `pack-light` (after a contract if needed).
4. **About to say done?** → `prove-it`. No other skill substitutes for evidence.
5. **Only need the map or intensity?** → `marvin`.

When two skills seem to fit, pick the one that matches the **immediate** job, finish it, then switch.
