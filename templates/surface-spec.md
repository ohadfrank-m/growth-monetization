# Surface Spec Template

Used by: `monetization-surface-spec`
Applies to: all 7 monetization surface types

---

## Anatomy

Every spec artifact follows this structure. The spec is the contract between PM and design. It must be specific enough that two designers produce the same surface from it.

---

```markdown
---
plugin: growth-monetization
skill: monetization-surface-spec
feature / topic: {surface name} — {tier or context}
surface type: {pricing-page | paywall | promotion | upgrade-trigger | credit-ui | trial | cancellation}
cohort: {new-user | existing-user | both}
author: {name}
date: {YYYY-MM-DD}
status: draft
---

# {Surface name}
e.g. "Credit Depletion Modal — Pro Tier" / "Feature Gate — AI Agents, Free Users"

## Brief [required]
2–3 sentences: what this surface is, when it appears, and the single job it must do.

## User context [required]
- **Who sees this:** {user type, tier, what they were doing when it appeared}
- **Cohort:** {new-user (urgency lever applies) | existing-user (capability lever applies)}
- **Trigger:** {exact condition — e.g. "credit balance drops below 50", "user clicks locked feature", "trial day 7"}
- **Competing intent:** {what the user was trying to do — preserve this or they churn}

## Primary objective [required]
One sentence. The single conversion outcome this surface must drive.
e.g. "Drive immediate credit top-up for Pro users mid-task, without breaking task momentum."

## Hook — reason to act [required]
Name the primary reason from the 15 reasons people buy (see `improve-conversion-surfaces-copy`).
e.g. "Escape pain / guilt — user risks losing work they've already done"

This maps directly to the headline and CTA copy strategy. Hand copy writing to `improve-conversion-surfaces-copy`.

## Surface structure [required]

### Sections (top to bottom)
List every section of the surface in visual order:

| # | Section | Content | Notes |
|---|---------|---------|-------|
| 1 | {e.g. Header} | {what it says / shows} | {constraints, e.g. "max 8 words"} |
| 2 | {e.g. Value proof} | {e.g. "3 tasks it has already completed"} | {personalised if possible} |
| 3 | {e.g. Primary CTA} | {label + action} | {benefit-led, not "Upgrade"} |
| 4 | {e.g. Secondary action} | {e.g. "Notify admin" or "Remind me later"} | {always include escape hatch} |

### Component notes
- **Trigger timing:** {when it appears, frequency cap, dismiss behaviour}
- **Blocking vs non-blocking:** {full-screen modal | inline nudge | banner | toast}
- **State preservation:** {if mid-task: does it save state? how does user resume?}
- **Dismiss logic:** {what happens if dismissed — repeat after X days / session / never}

## Copy strategy [required]
Do not write final copy here. Specify the persuasion angle and hand off.

- **Headline angle:** {reason + what outcome it promises}
- **CTA label direction:** {benefit-led — e.g. "Keep building" not "Upgrade"}
- **Tone:** {urgency | capability | reassurance}
- **What to avoid:** {guilt-trip patterns, bare credit numbers, feature-speak}

→ Copy writing: run `improve-conversion-surfaces-copy` with this section as input.

## Success metrics [required]

| Metric | Definition | Target |
|--------|-----------|--------|
| Primary | {e.g. Credit top-up conversion rate} | {e.g. +X% vs current baseline} |
| Secondary | {e.g. Task resume rate after dismiss} | |
| Guardrail | {e.g. Support tickets re: credit confusion} | {no increase} |

## Edge cases [required]
Address each that applies:

- **Credit debt:** what happens if user goes below 0 mid-task?
- **Admin-gated purchase:** user wants to top up but isn't the admin — what's the path?
- **Mobile:** does this surface work on mobile? any layout changes needed?
- **Repeat exposure:** what if the user has already seen this 3× this week?
- **Enterprise accounts:** does this surface behave differently for enterprise users?

## monday.com design constraints [required]
- Use Vibe design system tokens — flag any hardcoded values in review
- Use tier colour tokens from Vibe — verify current tokens rather than assuming colours
- AI agent flows: non-blocking preferred, always preserve task state
- Notify admin path required for IC-facing surfaces where purchase is admin-gated

## Wireframe [built in a later pass — not part of this document]
Not built yet. `improve-conversion-surfaces-copy` writes the real headline/CTA copy from the Copy strategy section above first — the wireframe is built from that real copy, not from placeholder text. Once `02-copy.md` exists, re-invoke `monetization-surface-spec` to build it: low-fi HTML, sections, hierarchy, CTA placement using the ★ Recommended copy, escape hatch. Not pixel-perfect.
Output as: `.monetization/{feature-slug}/03-wireframe.html`

## References [conditional]
Include benchmark examples only when they directly informed a structural decision:
- {Company}: {URL} — {one sentence on what it does well and why it applies here}

---
→ Next step: improve-conversion-surfaces-copy — write the actual headline/CTA copy from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

---

## Formatting rules

- The brief drives everything — if it's vague, ask one question before proceeding
- Surface structure table is non-negotiable — no prose descriptions of layout
- Copy strategy names the reason and hands off — never writes final copy
- Edge cases are addressed even when the answer is "not applicable, because..." — no silent omissions
- Wireframe is always HTML, always low-fi, always delivered as a file — and always built *after* copy exists, never before
