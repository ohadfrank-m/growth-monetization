---
name: monetization-surface-spec
description: This skill should be used when the user wants to "spec out a paywall", "wireframe a credit depletion modal", "design brief for an upgrade flow", "create a spec for a pricing page", "build a trial expiry screen", "spec a cancellation flow", "what should a credit meter look like", "create an upgrade trigger for [feature]", "write a design brief for a monetization surface", "I need a spec for [any of: paywall, feature gate, upgrade prompt, credit top-up, trial flow, cancellation screen, pricing page]". Produces a structured spec artifact and low-fi HTML wireframe. Connects to Figma MCP when a design already exists.
version: 0.1.0
---

# Monetization Surface Spec

Produce a complete spec artifact and low-fi HTML wireframe for any monetization surface. The spec is the contract between PM and design — specific enough that two designers produce the same surface from it.

This skill covers both modes:
- **From brief:** "I need a paywall for AI Agents on Free tier" → generates full spec + wireframe
- **From existing design:** "Here's our current credit modal, turn it into a proper spec" → reverse-engineers spec from design, identifies gaps

---

## Input handling

Accept any of the following as input:

- **Natural language brief** — "I need a spec for..." → run [brief-intake.md](references/brief-intake.md) to extract the required fields, then proceed
- **Figma link** — use Figma MCP to pull design context before speccing (see Figma ingestion below)
- **Screenshot or image** — analyze the existing design, then spec it
- **Existing partial spec** — fill the gaps and produce the wireframe
- **Benchmark output** — from `pricing-intelligence`, translate findings directly into a surface spec

When input is minimal (just a surface name), run the brief intake before proceeding — don't produce a spec from vague input.

---

## Surface types

Identify the surface type first. It determines which reference file and which spec sections are mandatory.

| # | Surface | When it appears | Reference | Playbook (CRO rationale, benchmarks, examples) |
|---|---------|----------------|-----------|-----------|
| 1 | **Pricing page** | Public or in-app plan comparison | [pricing-pages.md](references/pricing-pages.md) | [pricing-pages.md](../../playbooks/pricing-pages.md) |
| 2 | **Paywall / feature gate** | User tries to access a locked feature | [paywalls.md](references/paywalls.md) | [paywalls.md](../../playbooks/paywalls.md) |
| 3 | **Promotion** | Discount, limited-time offer, upsell banner/modal | [promotions.md](references/promotions.md) | [promotions.md](../../playbooks/promotions.md) |
| 4 | **Tier upgrade trigger** | Usage limit hit, seat expansion, plan upgrade nudge | [upgrade-triggers.md](references/upgrade-triggers.md) | [upgrade-triggers.md](../../playbooks/upgrade-triggers.md) |
| 5 | **Credit / consumption UI** | Running low on credits, credit meter, top-up flow | [credit-ui.md](references/credit-ui.md) | [credit-ui.md](../../playbooks/credit-ui.md) |
| 6 | **Cancellation flow** | User initiates cancel or downgrade | [cancellation.md](references/cancellation.md) | [cancellation.md](../../playbooks/cancellation.md) |
| 7 | **Trial flow** | Trial start, mid-trial nudge, trial expiry | [trial-flows.md](references/trial-flows.md) | none yet — see [surface-types.md](references/surface-types.md) |

If the surface type is ambiguous, ask — one question.

The reference file per type covers what to put *in the spec*. The playbook covers *why* — read it before drafting; don't skip to the reference file alone.

---

## Figma ingestion (when design exists)

When given a Figma link, pull design context before writing the spec:

1. `get_design_context` or `get_metadata` — frame structure, layers, component instances
2. `get_screenshot` — visual hierarchy and mobile readiness assessment
3. `get_variable_defs` — check Vibe token binding; flag any hardcoded values

Read copy directly from layer text. If the MCP can't reach the frame, ask for a screenshot — one request.

---

## Workflow

### Step 1: Brief intake

If input is a brief or surface name, extract these fields before proceeding. Ask only what's missing — don't re-ask what's already provided.

Required fields:
- **Surface type** — from the 7 types above
- **Trigger condition** — exact condition that shows this surface (e.g., "credit balance < 50", "user clicks locked feature", "trial day 7")
- **User cohort** — new-user (urgency lever) or existing-user (capability lever)
- **Tier context** — which tier(s) this applies to
- **Primary objective** — the single conversion outcome

For missing fields: infer from context where obvious (a "credit depletion modal" is surface type 5, existing-user cohort). Ask only when genuinely ambiguous.

Full intake protocol: [brief-intake.md](references/brief-intake.md)

### Step 2: Load surface type reference

Read the reference file for the identified surface type. It contains:
- Mandatory spec sections for this surface
- Best-in-class patterns
- Anti-patterns to flag
- monday.com specific considerations

### Step 3: Research (optional but recommended)

For each major surface, offer to pull benchmark patterns before speccing:

> "Want me to pull 3 best-in-class examples of this surface type from pricingsaas.com and similar tools before I write the spec? Takes 2 minutes and usually surfaces a pattern worth stealing."

If yes, run web research using [wireframe-patterns.md](references/wireframe-patterns.md) as a guide. Results feed directly into the References section of the spec.

### Step 4: Write the spec

Check the anti-patterns in [spec-checklist.md](references/spec-checklist.md) before and after drafting.

Use the surface spec template: [../../templates/surface-spec.md](../../templates/surface-spec.md)

Apply monday.com context from [monday-context.md](../../context/monday-context.md) throughout — don't wait to be asked.

**Copy strategy section:** Name the primary reason from the 15 reasons people buy, name the copy direction, and explicitly hand off to `improve-conversion-surfaces-copy`. Never write final copy in the spec.

**Edge cases:** Address every edge case in [spec-checklist.md](references/spec-checklist.md) — credit debt, admin-gated purchase, mobile, repeat exposure, enterprise. Mark non-applicable ones as N/A with one-line rationale — no silent omissions.

### Step 5: Build the wireframe

Produce a low-fi HTML wireframe that shows:
- Visual hierarchy of sections (top to bottom)
- CTA placement and label direction
- Escape hatch (always present)
- Mobile consideration (note if layout changes at mobile breakpoint)

Keep it low-fi — this communicates structure and hierarchy, not final design. Use Vibe color tokens as references, not hardcoded hex values.

Output: `.monetization/{feature-slug}/02-wireframe.html`

Build the wireframe by default. Skip it only if the user asks for the spec doc alone.

### Step 6: Deliver

Write the spec to: `.monetization/{feature-slug}/01-spec.md`
Write the wireframe to: `.monetization/{feature-slug}/02-wireframe.html`

Always end with the next step block:
```
---
→ Next step: monetization-design-reviewer — score the spec and wireframe before it goes to design
→ Prompt: "Review the spec and wireframe in .monetization/{feature-slug}/"
```

---

## Output standards

- Use the artifact template: [../../templates/surface-spec.md](../../templates/surface-spec.md)
- Header block on every file
- Surface structure table is non-negotiable — no prose layout descriptions
- Copy strategy names the reason, states the direction, hands off — never writes final copy
- Edge cases addressed even when N/A
- Wireframe always delivered as `.html` file, never inline

---

## monday.com context

Read [context/monday-context.md](../../context/monday-context.md) before every spec for current tiers, prices, AI credit packages, feature gating, trial terms, and cohorts. Never quote a price or limit from memory; cite the context file.

---

## Additional references

- Brief intake protocol: [brief-intake.md](references/brief-intake.md)
- Surface-type specific guidance (what goes in the spec): in `references/` per surface type
- CRO rationale, benchmarks, and best-in-class examples per surface type (shared with `monetization-design-reviewer` — owned once, cited here, never duplicated): [../../playbooks/](../../playbooks/)
- Wireframe patterns and best-in-class examples: [wireframe-patterns.md](references/wireframe-patterns.md)
- Copy hooks per surface type: [copy-hooks.md](references/copy-hooks.md)
- Anti-patterns and edge cases: [spec-checklist.md](references/spec-checklist.md)
- monday.com strategy and pricing data: [context/monday-context.md](../../context/monday-context.md)
- Surface-type quick index: [surface-types.md](references/surface-types.md)
