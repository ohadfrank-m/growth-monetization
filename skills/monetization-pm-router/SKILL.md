---
name: monetization-pm-router
description: "**Start here.** Routes to the right monetization skill and orchestrates multi-skill chains through to a final requirements doc. Use when intent is unclear, when you say 'monetization copilot' or 'help me with monetization', or whenever you share a design for review. This is the entry point — it reads what you need, runs the right skills in sequence without asking you to re-prompt between steps, and synthesizes everything into one requirements doc at the end."
version: 0.1.0
---

# Monetization Copilot — Router

Read the user's intent and route to the correct skill. For multi-skill workflows, run the full sequence without pausing for the user between steps. After all skills complete, synthesize their outputs into a single requirements doc (`05-requirements.md`). This is the only artifact the router produces directly.

Use this when:
- The request is vague or spans more than one skill ("help me design and research a paywall")
- The user doesn't know which skill applies
- A task requires multiple skills run in sequence

---

## Routing table

| What the user says | Route to | What it does |
|-------------------|---------|-------------|
| "research how X prices", "competitive pricing", "how do companies sell AI credits", "benchmark our model" | `pricing-intelligence` | Competitor research, landscape scans, model benchmarking |
| "review this design", "critique this paywall", "score this upgrade modal" | `monetization-design-reviewer` | CRO rubric score + prioritised improvement list |
| "spec out a surface", "wireframe a paywall", "design brief for a trial flow", "I need a spec for..." | `monetization-surface-spec` | Full spec + low-fi wireframe |
| "write copy for this CTA", "rewrite this upgrade prompt", "the copy feels flat" | `improve-conversion-surfaces-copy` | Benefit-led copy rewrite with 2–3 options |
| Multi-step / unclear | Continue below → |

---

## Multi-skill workflow patterns

When a request spans multiple skills, announce the full sequence upfront, then run every step without pausing for the user between them. The user gets one set of artifacts at the end — not one artifact per prompt. The synthesis step (below) always runs last when there are two or more skills in the chain.

---

### Review → Fix → Synthesize (from existing design) ← most common pattern
> "Here's our current upgrade modal — it's not converting well" / user shares a screenshot or Figma link

This is the default pattern when an existing design is shared. Run all steps without interruption.

Sequence:
1. `monetization-design-reviewer` → score the design, produce ranked fix list (`04-review.md`)
2. `improve-conversion-surfaces-copy` → for every Copy/CRO row flagged in `04-review.md`, write 2–3 options with one recommended (`02-copy.md` or `02-copy-v2.md`)
3. **Synthesis** → router reads `04-review.md` + copy artifact, produces `05-requirements.md` (see Synthesis phase below)

Announce before starting:
```
**Sequence:** design-reviewer → copy revisions → synthesis
**Artifacts:** 04-review.md, 02-copy-v2.md, 05-requirements.md
**You'll get one requirements doc at the end — no re-prompting needed between steps.**

Starting now →
```

---

### Research → Spec
> "I want to design a credit top-up flow — can you research how other tools do it and then spec ours?"

Sequence:
1. `pricing-intelligence` → monetization model benchmarking (sub-workflow B: AI credits)
2. `monetization-surface-spec` → credit UI spec, using benchmark findings as input

Announce: "I'll start with the benchmark research. Once that's done, I'll use the findings to spec the surface — you'll end up with both a competitive picture and a ready-to-use spec."

---

### Spec → Copy → Wireframe → Review → Synthesize
> "I need to build a paywall for AI Agents on Free tier, get it reviewed, and write the copy"

Sequence:
1. `monetization-surface-spec` → paywall spec (`01-spec.md`) — names the reason and direction, doesn't write final copy
2. `improve-conversion-surfaces-copy` → the actual headline/CTA copy from that reason (`02-copy.md`)
3. `monetization-surface-spec` (re-invoked) → wireframe built with the real copy, not placeholders (`03-wireframe.html`)
4. `monetization-design-reviewer` → CRO score of the real thing (`04-review.md`)
5. **Synthesis** → `05-requirements.md`

---

### Research → Positioning
> "How does Asana price compared to us? We're about to run a pricing page test"

Sequence:
1. `pricing-intelligence` → company research (Asana) + pricing page teardown
2. Offer: `monetization-surface-spec` → spec a pricing page variant using competitive findings

---

## Synthesis phase

Run this after all other skills in the chain have completed. Read every artifact in `.monetization/{feature-slug}/` and produce `05-requirements.md`. This is the deliverable the team actually ships from.

The document must be implementation-ready. "Strengthen the CTA" is not a requirement. "CTA button label: 'Keep Pro features' (★ recommended from 02-copy-v2.md)" is. If two people acting on a row would produce different results, rewrite it until they wouldn't.

### `05-requirements.md` format

```markdown
# Requirements: {Surface Name}

**Surface:** {surface-type} | **Cohort:** {new/existing} | **Score before:** {X/100} | **Date:** {YYYY-MM-DD}
**Sources:** {list the artifacts read — e.g. 04-review.md + 02-copy-v2.md}

---

## Final copy

Strings are ★ recommended options from the copy artifact. Ready to implement as-is.

| Element | Final string | Reason |
|---------|-------------|--------|
| Headline | "..." | {which of the 15 reasons it activates} |
| CTA — primary | "..." | ... |
| CTA — secondary | "..." | ... |
| Trust signal | "..." | ... |
| [any other surface-specific copy elements] | "..." | ... |

---

## Design changes

One row = one shippable instruction. No vague directions.

| # | Priority | Component | Change | Specification |
|---|----------|-----------|--------|---------------|
| 1 | 🔴 | {component name} | {what changes} | {exact spec: text, font, color token, position, size, component name if Vibe} |

---

## Action items

Sorted by priority then effort. Each item is scoped for one sprint.

| # | Priority | Owner | Action | Effort |
|---|----------|-------|--------|--------|
| 1 | 🔴 | {Eng/Design/Copy/PM} | {verb + specific thing} | S/M/L |

---

**Estimated impact:** {one sentence — what moving the 🔴 items is worth, in terms of the score or conversion}
```

### Synthesis self-check before delivering

1. Every copy string in the Final copy table came from the ★ recommended option in the copy artifact — not a paraphrase or a new invention.
2. Every design change row contains a specification specific enough that a designer could implement it without asking a follow-up question.
3. Every action item names an owner type (Eng / Design / Copy / PM) and is scoped to one sprint.
4. No row says anything like "improve X", "consider Y", or "make it more Z" — these are not requirements.
5. The action items table is sorted: 🔴 first, then within severity by effort (S before M before L).
6. Every unresolved item from the review (pending mobile, pending close button) has an action item with Owner = "Design" and action "Confirm [X] — pending {what was blocked} from 04-review.md".

---

## When intent is still unclear

Ask one question — the answer will route unambiguously:

> "Are you trying to (a) research a competitor or industry, (b) spec or wireframe a surface, (c) review an existing design, or (d) write copy for a surface?"

Don't ask more than one. Don't explain the skills before asking.

---

## Output from the router

**Single-skill routing:**
```
**Routing to:** {skill-name}
**Why:** {one sentence}
**What you'll get:** {artifact names and what they contain}

Starting now →
```

**Multi-skill chain (two or more skills + synthesis):**
```
**Sequence:** {skill 1} → {skill 2} → synthesis
**Artifacts:** {list — e.g. "04-review.md, 02-copy-v2.md, 05-requirements.md"}
**You'll get one requirements doc at the end — no re-prompting needed between steps.**

Starting now →
```

Then immediately begin the first skill. Don't wait for the user to confirm the routing. After each skill delivers its artifact, continue to the next step without pausing. The synthesis step runs last and produces `05-requirements.md`.
