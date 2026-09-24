# Playbooks — shared CRO knowledge

One file per monetization surface type. This is the single owned source for the *why* — CRO principles, benchmarks, best-in-class examples, anti-patterns, and monday.com-specific application — for that surface.

## Why this folder exists

Two skills need the same CRO knowledge for the same surface type: `monetization-surface-spec` needs it to write a spec that's grounded in what actually converts, and `monetization-design-reviewer` needs it to score a design against real benchmarks. Before this folder existed, each skill kept its own copy under its own `references/` folder. They drifted — most visibly on credit/consumption UI, where both skills had independently written a full deep-dive with different benchmarks and different best-in-class examples for the same surface.

This follows the same principle as [`context/monday-context.md`](../context/monday-context.md): one owned file, cited by every skill that needs it, never re-derived or copied into a skill-local reference.

## What lives here vs. what stays in a skill's own `references/`

| Here (`playbooks/`) | Skill-local `references/` |
|---|---|
| Why a pattern works, benchmarks, best-in-class examples, anti-patterns | The mandatory fields a spec must contain, or the rubric anchors/weights used to score |
| Shared across ≥2 skills | Genuinely specific to one skill's job |

If you're adding CRO knowledge (a benchmark, a new best-in-class example, an anti-pattern) — add it here, then cite it from any skill reference that needs it. Don't paste it into a skill folder.

## Files

- [pricing-pages.md](pricing-pages.md) — surface type 1
- [paywalls.md](paywalls.md) — surface type 2
- [promotions.md](promotions.md) — surface type 3
- [upgrade-triggers.md](upgrade-triggers.md) — surface type 4 (tier/seat limits — not credits)
- [credit-ui.md](credit-ui.md) — surface type 5 (credit/consumption — including metering, forecasting, top-up)
- [cancellation.md](cancellation.md) — surface type 6

Trial flow (surface type 7) has no playbook file yet — today it's owned solely by `monetization-surface-spec/references/trial-flows.md` with no counterpart in `monetization-design-reviewer` (that skill has no trial-flow surface type at all — see the open taxonomy gap noted in each skill's SKILL.md). Move it here if and when a second skill needs the same knowledge.

## Owner

Same owner as `monday-context.md` (Growth Monetization PM). Update in place; no changelog required — these are best-practice references, not versioned facts.
