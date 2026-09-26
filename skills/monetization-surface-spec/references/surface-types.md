# Surface type reference index

Quick-reference for all 7 monetization surface types — enough to identify which type applies and where to go next. The mandatory spec sections, anti-patterns, and CRO rationale for each type live in that type's own reference file (and, for CRO rationale specifically, the shared [playbook](../../../playbooks/)) — this index doesn't restate them.

Detailed patterns and wireframes: [wireframe-patterns.md](wireframe-patterns.md)
Copy angles: [copy-hooks.md](copy-hooks.md)
monday.com specific context: [monday-context.md](../../../context/monday-context.md)

---

## 1. Pricing page
**When:** Public or in-app plan comparison
**Cohort:** Both (new and existing)
**Primary conversion:** Plan selection / upgrade initiation
**Key constraint:** Value clarity — each tier must name a job-to-be-done, not a feature list
**Reference:** [pricing-pages.md](pricing-pages.md) · Playbook: [pricing-pages.md](../../../playbooks/pricing-pages.md)

## 2. Paywall / feature gate
**When:** User tries to access a locked feature
**Cohort:** New users (trial) or existing users blocked by tier
**Primary conversion:** Tier upgrade or trial-to-paid
**Key constraint:** Show value before the ask — never gate without a preview
**Reference:** [paywalls.md](paywalls.md) · Playbook: [paywalls.md](../../../playbooks/paywalls.md)

## 3. Promotion
**When:** Discount, limited-time offer, upsell banner/modal
**Cohort:** Both (different angles)
**Primary conversion:** Upgrade during the promotional window
**Key constraint:** Urgency must be real — fake countdowns destroy trust
**Reference:** [promotions.md](promotions.md) · Playbook: [promotions.md](../../../playbooks/promotions.md)

## 4. Tier upgrade trigger
**When:** Usage limit hit, seat expansion needed, plan upgrade nudge at specific moment
**Cohort:** Existing users
**Primary conversion:** Plan upgrade or seat expansion
**Key constraint:** Name the specific limit and consequence — "you've hit a limit" without context converts poorly
**Reference:** [upgrade-triggers.md](upgrade-triggers.md) · Playbook: [upgrade-triggers.md](../../../playbooks/upgrade-triggers.md)

## 5. Credit / consumption UI
**When:** Running low on credits, credit meter, metering dashboard, top-up flow
**Cohort:** Existing users
**Primary conversion:** Credit top-up
**Key constraint:** Task continuity — never let the user lose work without a resume path
**Reference:** [credit-ui.md](credit-ui.md) · Playbook: [credit-ui.md](../../../playbooks/credit-ui.md)

## 6. Cancellation flow
**When:** User initiates cancel or downgrade
**Cohort:** Existing users (retention)
**Primary conversion:** Retain user at current or lower tier (downgrade > cancel)
**Key constraint:** Don't trap — friction is legal risk and brand damage; acknowledge the choice
**Reference:** [cancellation.md](cancellation.md) · Playbook: [cancellation.md](../../../playbooks/cancellation.md)

## 7. Trial flow
**When:** Trial start (onboarding), mid-trial nudge, trial expiry
**Cohort:** New users
**Primary conversion:** Trial to paid (full upgrade or self-serve)
**Key constraint:** Show aha moment before asking for payment — ask too early = conversion tanks
**Reference:** [trial-flows.md](trial-flows.md) · Playbook: [../../../playbooks/trial-flows.md](../../../playbooks/trial-flows.md) · Reviewer scores it against the Trial Flow rubric column.
