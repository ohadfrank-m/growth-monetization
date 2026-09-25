---
name: monetization-pm-router
description: Start here. The entry point for the growth-monetization plugin — reads intent, runs the right skills in sequence without re-prompting between steps, and synthesizes the results into one implementation-ready requirements doc. Use when intent is unclear or spans skills, when someone shares a design, screenshot, or Figma link of a monetization surface, or says "monetization copilot", "help me with monetization", "where do I start", "not sure which skill to use", or "I'm working on [any monetization surface or research task]".
version: 0.2.0
---

# Monetization Copilot — Router

Read the user's intent and route to the correct skill. For multi-skill workflows, run the full sequence without pausing for the user between steps. When the chain includes a design review, finish with the synthesis phase, which produces `05-requirements.md` — the only artifact the router writes itself.

Use this when:
- The request is vague or spans more than one skill ("help me design and research a paywall")
- The user shares an existing design, screenshot, or Figma link
- The user doesn't know which skill applies

---

## Routing table

| What the user says | Route to | What it does |
|-------------------|---------|-------------|
| "research how X prices", "competitive pricing", "how do companies sell AI credits", "benchmark our model" | `pricing-intelligence` | Competitor research, landscape scans, model benchmarking |
| "review this design", "critique this paywall", "score this upgrade modal", or any shared screenshot / Figma link | **Review → Fix → Synthesize chain** (below) | Review + copy rewrites + one `05-requirements.md` |
| "just score this", "review only" | `monetization-design-reviewer` alone | `04-review.md` only — no chain |
| "spec out a surface", "wireframe a paywall", "design brief for a trial flow", "I need a spec for..." | **Spec → Copy → Wireframe → Review → Synthesize chain** (below) | Spec, copy, wireframe, review, requirements |
| "write copy for this CTA", "rewrite this upgrade prompt", "the copy feels flat" | `improve-conversion-surfaces-copy` | Benefit-led copy rewrite with 2–3 options |
| Multi-step / unclear | Continue below → |

---

## Chain mode rules

A chain is any sequence the router announced before the first skill started. While a chain is running:

- **The router owns sequencing.** Each skill delivers its artifact, then control returns here for the next step. Skills don't decide what runs next.
- **No next-step blocks.** Skills omit their `→ Next step` block — it's a prompt for a human to re-type, and in a chain nobody needs to.
- **No optional offers mid-chain.** Skip "want me to mock this up?" and similar questions. Offer them once, after the final artifact.
- **Only stop for a real blocker:** a missing input the skill can't work without (one question, per that skill's intake rules), or a paid PricingSaaS call, which always needs confirmation per the plugin's standing rules. Resume the chain once answered.

---

## Chain patterns

### Review → Fix → Synthesize ← default when a design is shared
> "Here's our trial-expiry pricing modal — it's not converting" / screenshot / Figma link

1. `monetization-design-reviewer` → scored rubric + ranked fix list (`04-review.md`)
2. `improve-conversion-surfaces-copy` → 2–3 options with one ★ recommended for **every** Copy/CRO row in `04-review.md`. File: `02-copy.md` if none exists (review-first pass), otherwise `02-copy-v2.md`
3. **Synthesis** → `05-requirements.md`

Announce before starting:
```
**Sequence:** design review → copy rewrites → requirements synthesis
**Artifacts:** 04-review.md, 02-copy.md, 05-requirements.md
**One requirements doc at the end — no re-prompting between steps.**

Starting now →
```

### Spec → Copy → Wireframe → Review → Synthesize
> "I need to build a paywall for AI Agents on Free tier"

1. `monetization-surface-spec` → `01-spec.md` (names the reason and direction, no final copy)
2. `improve-conversion-surfaces-copy` → `02-copy.md` from the spec's reason
3. `monetization-surface-spec` (re-invoked) → `03-wireframe.html` built with the real copy
4. `monetization-design-reviewer` → `04-review.md`
5. If the review flagged Copy/CRO rows: `improve-conversion-surfaces-copy` → `02-copy-v2.md` (revise flagged lines only)
6. **Synthesis** → `05-requirements.md`

### Research → Spec
> "Research how other tools do credit top-ups, then spec ours"

1. `pricing-intelligence` → monetization model benchmarking (sub-workflow B: AI credits)
2. Continue into the Spec chain above, using the benchmark as input to step 1

### Research → Positioning
> "How does Asana price compared to us? We're about to run a pricing page test"

1. `pricing-intelligence` → company research + pricing page teardown
2. Offer: the Spec chain for a pricing page variant using the findings

Research-only runs end at the research artifact — no synthesis, since there's nothing to implement yet.

---

## Synthesis phase

Runs last in any chain that includes a review. Its reader is the designer and engineer who will build the fix — they should be able to start work from this doc alone, without opening the other artifacts.

### Inputs

Read the **latest version** of each numbered artifact in `.monetization/{feature-slug}/` — `02-copy-v2.md` supersedes `02-copy.md` for the lines it revises; unrevised lines still come from `02-copy.md`. Read [context/monday-context.md](../../context/monday-context.md) for any price, limit, or credit figure. If `05-requirements.md` already exists, write `05-requirements-v2.md`.

### Rules

- **Traceability.** Every row in `04-review.md` appears at least once — in Final copy, Design changes, or Open items — with a `Source` reference (`R3` = review row 3). A row that needs both a string and a placement (e.g. "add a Free link") appears in both tables with the same Source; a row blocked on a fact also gets an Open item. Nothing gets dropped silently.
- **Copy is verbatim.** Every Final copy string is the ★ recommended option from the copy artifact, word for word. No paraphrasing, no new lines written here.
- **Specs are exact but not invented.** Name Vibe components and tokens only if they were confirmed from Figma variables or the Vibe MCP. Otherwise, specify relative to what's already on screen ("same text style as the plan feature rows, directly above the Pro CTA") and add "token TBD — confirm in Figma" rather than guessing a token name.
- **No invented numbers.** Credit-to-task conversions, prices, and limits come from `monday-context.md`. If the figure isn't there, the copy keeps a marked slot (`≈ {N} AI actions`) and an Open item names who supplies N.
- **No unverified claims.** Any factual promise in a Final copy string — a cancellation or refund policy, data retention after expiry, a guarantee — that isn't stated in `monday-context.md` gets an Open item naming who confirms it (Billing, Product) and is listed as a ship blocker. Copy that reads well but promises something untrue is worse than the line it replaced.
- **No direction-only rows.** "Improve", "consider", "strengthen", "make more X" are not requirements. If two people acting on a row would build different things, rewrite it.

### `05-requirements.md` format

Open with the header block from [templates/ARTIFACT_HEADER.md](../../templates/ARTIFACT_HEADER.md) (`skill: monetization-pm-router`, `status: review`).

```markdown
# Requirements: {surface name}

**Surface:** {type} · **Cohort:** {new / existing} · **Current score:** {X}/100 · **Projected score:** {Y}/100 if 🔴 + 🟠 ship
**Built from:** 04-review.md, 02-copy.md{, 02-copy-v2.md}

## Final copy

| Element | Final string | Replaces | Reason it activates | Source |
|---------|-------------|----------|---------------------|--------|
| Headline | "..." | "Your Pro trial has ended" | Fear of losing capability | R#1 |

## Design changes

| # | Priority | Component | Change | Spec | Source |
|---|----------|-----------|--------|------|--------|
| D1 | 🔴 | Pro CTA | ... | {placement, size, style, state behavior — tokens only if confirmed} | R#5 |

## Open items

Anything the review couldn't assess or that needs an input before build — pending mobile screenshot, unconfirmed close button, a missing data source.

| # | Owner | What's needed | Blocks | Source |
|---|-------|---------------|--------|--------|
| O1 | Design | 375px screenshot to confirm CTA stays above fold | D1 on mobile | R#9 |

## Build order

| # | Priority | Owner | Task | Covers | Effort |
|---|----------|-------|------|--------|--------|
| 1 | 🔴 | Eng | ... | Final copy rows 1–2, D1 | S |
```

**Projected score:** copy it from `04-review.md` — the reviewer owns the rubric and computes it. It's a rubric projection, not a conversion forecast; don't restate it as a lift estimate.

### Self-check before delivering

1. Every `04-review.md` row appears at least once, with its Source reference.
2. Every Final copy string matches the ★ recommended option verbatim.
3. No Vibe token or component name appears that wasn't confirmed — unconfirmed ones say "TBD".
4. No price, limit, or credit figure appears that isn't in `monday-context.md`.
5. Every factual promise in the copy (policy, retention, guarantee) not in `monday-context.md` has an Open item and is listed as a ship blocker.
6. No row is direction-only.
7. Build order is sorted 🔴 → 🟠 → 🟡, and by effort (S → M → L) within each severity.

After delivering, one line only: offer to build `03-wireframe.html` of the fixed version via `monetization-surface-spec`, using the Final copy and Design changes as input.

---

## When intent is still unclear

Ask one question — the answer will route unambiguously:

> "Are you trying to (a) research a competitor or industry, (b) spec or wireframe a surface, (c) review an existing design, or (d) write copy for a surface?"

Don't ask more than one. Don't explain the skills before asking.

---

## Output from the router

**Single skill:**
```
**Routing to:** {skill-name}
**Why:** {one sentence}
**What you'll get:** {artifact names and what they contain}

Starting now →
```

**Chain:** use the announcement block from the matching chain pattern above.

Then immediately begin the first skill. Don't wait for the user to confirm the routing.
