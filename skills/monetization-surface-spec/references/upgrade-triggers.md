# Tier upgrade trigger — spec reference

Surface type 4: usage limit hit, seat expansion, plan upgrade nudge.

CRO rationale, benchmarks, and best-in-class examples for this surface live in the shared playbook — read it before drafting: [../../../playbooks/upgrade-triggers.md](../../../playbooks/upgrade-triggers.md). This file covers only what's specific to *writing the spec*. If the trigger is a credit/consumption limit rather than a tier/seat limit, use [credit-ui.md](credit-ui.md) instead.

## When it appears
- Automation or integration cap reached (e.g. Standard's monthly action limit)
- Seat bundle full when inviting a teammate
- Storage, dashboard, or board-count limit reached
- Proactive nudge at a usage threshold (e.g. 80% of the automation cap)

Current limits per tier: [monday-context.md](../../../context/monday-context.md#feature-gating-by-tier).

## Mandatory spec sections
- **Limit and threshold:** which limit, at what % the nudge fires, what happens at 100%
- **Usage context:** how current usage is shown (bar, count, trend)
- **What changes at the next tier:** the specific new limit, not "more features"
- **Behaviour at the limit:** hard stop, soft limit, or grace period
- **Seat bundles:** how the next bundle size and price delta are shown
- **IC vs. admin:** "Notify admin" path
- **Dismiss and frequency cap**

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Tier upgrade trigger, Pattern A (usage limit) and Pattern B (seat expansion).

## Copy hook
Primary reason: save time / avoid effort. See [copy-hooks.md](copy-hooks.md#tier-upgrade-trigger-surface-4).
