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
| Existing design | a live version turns greenfield into redesign | Ask only if the surface is in the context file's surface inventory and nothing was shared |

## Infer without asking

These can usually be inferred from surface type + tier:
- **Cohort:** trial flows → new-user; credit depletion → existing-user; feature gate → depends on trigger
- **Tier:** "for Free users" → Free tier; "when they run out of credits" → all paid tiers
- **Urgency level:** trial expiry → high urgency; credit warning at 20% → medium; feature gate → depends

## Ask every real gap in one message

After inferring what you can, put every remaining gap in **one** message — the question tool (`AskUserQuestion` in Claude Code, `AskQuestion` in Cursor; CLAUDE.md → Tool names), at most 4 questions, recommended answer first (the plugin's intake protocol in [CLAUDE.md](../../../CLAUDE.md), "Intake — ask, never assume"). One round trip, not one per field. If a field wouldn't change the spec, don't ask it.

An inference needs a source you can point to (the surface type, the prompt's words, the context file). A field you'd have to guess is a gap: ask it. The spec never carries an `Assumptions` section or a "confirm or correct" list.

---

## Intake output — brief summary block

Before writing the spec, print the brief as one block. It's a statement, not a question — if nothing's missing, proceed in the same turn:

```markdown
**Brief confirmed:**
- Surface: {type}
- Trigger: {exact condition}
- Cohort: {new-user | existing-user | both}
- Tier: {tier(s)}
- Objective: {one sentence}
- Key constraint: {any constraints mentioned — timing, design system, scope}

Proceeding to spec. [Or, if gaps remain: the one intake message with every open question]
```

This prevents a full spec being written from misunderstood input.

**In a Growth PM chain:** the Growth PM's up-front intake already answered these fields. Print the brief block from its answers and proceed in the same turn — don't wait for a confirmation. Only stop if a required field is still missing and can't be inferred from a named source: that's a real blocker, one question, and the chain resumes once it's answered.

In the spec's header, fields the user answered go in `confirmed with user:` and fields inferred go in `inferred:` with their source ([ARTIFACT_HEADER.md](../../../templates/ARTIFACT_HEADER.md)).

---

## From existing design input

When input is a Figma link, screenshot, or existing partial spec:

1. Pull design context (Figma MCP or screenshot analysis)
2. Identify surface type from visual
3. Extract existing spec fields from what's visible — note gaps
4. Print the brief block with what the design shows, each field with its source:

```markdown
**Brief extracted from design:**
- Surface: {type — identified from visual}
- Cohort: {value — from {copy on screen / context}}
- Tier: {value — from {visual}}
- Objective: {value — from primary CTA}
```

5. Ask every field the design couldn't show (the trigger is the usual one — it's rarely visible) in one question-tool message, recommended answer first. Write the spec only once they're answered. Never write the spec with a gap filled by a guess and flagged for later.
