# Contract — thinking-tools-expansion-review

## Outcome
A recommendations report that maps the 12 tools in `agentic-se-thinking-tools.md` onto Marvin’s current skills and says what to fold, strengthen, or leave out — with no skill/code changes in this turn.

## Actor
Human maintainer of Marvin, deciding whether to expand skills or deepen existing ones.

## Acceptance
- MUST inventory current plugin skills (purpose, triggers, artifacts).
- MUST map each of the 12 proposed tools to: already covered / strengthen existing / new skill / drop or fold.
- MUST respect Marvin’s “load one skill” routing and the proposed hard cap ≤15.
- MUST produce a chat report only; no skill implementation this turn.
- SHOULD call out overlap with `thinking-tools.md` and doctrine sources.
- MAY rank a short “do next” list if expansion is approved later.

## Scope
- In: overview of current skills; read of `agentic-se-thinking-tools.md`; recommendations report.
- Out (advisory turn): editing `SKILL.md` files; adding skills; changing `AGENTS.md`; rewriting `thinking-tools.md`.
- Follow-up (approved): update `thinking-tools.md` to twelve; fold eigenquestions / feedback-loops / leverage-points into existing job skills; no new top-level skills.

## Irreversible
None this turn (advisory only).

## Assumptions (labeled)
- Assumed: Marvin stays a small job-skill router (5 work skills + `marvin`), not a catalog of named frameworks as top-level skills.
- Assumed: `thinking-tools.md` remains the textbook layer; skills stay agent-operable recipes.

## Stop condition
Report delivered covering all 12 tools with a clear keep/fold/strengthen/drop call per tool.

## Cheapest proof
Reader can check: every current skill named; every tool in the v2 list has one recommendation row.

## Risks
- Report recommends minting many new top-level skills → violates “load one” and ≤15 → mitigated by prefer-fold default.
- Report understates gaps that agents actually miss in practice → mitigated by naming concrete algorithm holes, not just name overlap.
