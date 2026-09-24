# Brief intake protocol

Run this when input is a natural language brief or just a surface name. Extract required fields before writing the spec. Infer where obvious; ask only when genuinely ambiguous.

---

## Required fields

| Field | How to extract | Ask if missing |
|-------|---------------|---------------|
| Surface type | Match to the 7 types in SKILL.md | Yes — "Is this a paywall, upgrade trigger, credit UI, trial flow, pricing page, promotion, or cancellation flow?" |
| Trigger condition | "when does this appear?" | Yes — be specific: "exact condition that shows this surface, e.g. 'credit balance < 50' or 'user clicks locked feature'" |
| User cohort | new-user or existing-user | Infer from surface type where obvious (trial = new, credit depletion = existing) |
| Tier context | which tier(s) | Infer from surface type; ask if ambiguous |
| Primary objective | single conversion outcome | Ask if not stated — "What's the one thing this surface must make the user do?" |

## Infer without asking

These can usually be inferred from surface type + tier:
- **Cohort:** trial flows → new-user; credit depletion → existing-user; feature gate → depends on trigger
- **Tier:** "for Free users" → Free tier; "when they run out of credits" → all paid tiers
- **Urgency level:** trial expiry → high urgency; credit warning at 20% → medium; feature gate → depends

## Ask at most one question per gap

Never ask all missing fields at once. Ask the most important gap first, then infer the rest if possible.

---

## Intake output — brief summary block

Before writing the spec, confirm the brief with the user in a single block:

```markdown
**Brief confirmed:**
- Surface: {type}
- Trigger: {exact condition}
- Cohort: {new-user | existing-user | both}
- Tier: {tier(s)}
- Objective: {one sentence}
- Key constraint: {any constraints mentioned — timing, design system, scope}

Proceeding to spec. [Or: "One thing before I proceed: {single question}"]
```

This prevents a full spec being written from misunderstood input.

---

## From existing design input

When input is a Figma link, screenshot, or existing partial spec:

1. Pull design context (Figma MCP or screenshot analysis)
2. Identify surface type from visual
3. Extract existing spec fields from what's visible — note gaps
4. Confirm the brief block, marking gaps explicitly:

```markdown
**Brief extracted from design:**
- Surface: {type — identified from visual}
- Trigger: ⚠️ Not visible in design — please confirm
- Cohort: {inferred from copy/context}
- Tier: {inferred from visual or ask}
- Objective: {inferred from primary CTA}
- Gaps: {list anything that couldn't be extracted}
```

Then write the spec, filling gaps with the best inference and flagging each.
