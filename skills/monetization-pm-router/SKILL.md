---
name: monetization-pm-router
description: Start here. The entry point for the growth-monetization plugin — works out which deliverables the user expects (research doc, spec, copy, wireframe, review, requirements), asks one scoping question only when that's unclear, runs the right skills in sequence without re-prompting between steps, and synthesizes the results into one implementation-ready requirements doc. Use when intent is unclear or spans skills, when someone shares a design, screenshot, or Figma link of a monetization surface, or says "monetization copilot", "help me with monetization", "where do I start", "not sure which skill to use", or "I'm working on [any monetization surface or research task]".
version: 0.3.0
---

# Monetization Copilot — Router

Work out which deliverables the user expects, then run the skills that produce them. For multi-skill workflows, run the full sequence without pausing for the user between steps. When the chain includes a design review, finish with the synthesis phase, which produces `05-requirements.md` — the only artifact the router writes itself.

Use this when:
- The request is vague or spans more than one skill ("help me design and research a paywall")
- The user shares an existing design, screenshot, or Figma link
- The user doesn't know which skill applies

---

## Step 1 — Scope the deliverables

Route by what the user wants to **walk away with**, not by which words they used. "Help with our paywall" can end at a competitor doc, a spec, a wireframe, or a requirements doc — each is a different chain.

### Deliverables and who owns them

| Deliverable | Skill | Artifact |
|-------------|-------|----------|
| Research doc | `pricing-intelligence` | `.monetization/research/{topic-slug}-{YYYY-MM}.md` |
| Spec | `monetization-surface-spec` | `01-spec.md` |
| Copy | `improve-conversion-surfaces-copy` | `02-copy.md` |
| Wireframe | `monetization-surface-spec` (re-invoked) | `03-wireframe.html` |
| Review | `monetization-design-reviewer` | `04-review.md` |
| Requirements | router synthesis (below) | `05-requirements.md` |

### New surface or existing?

Decide this first — it sets the order, the pre-marks, what Review needs, and whether the research nudge fires.

- **Existing:** a design is shared, or the prompt describes live behavior ("isn't converting", "users complain", "current", "today", a metric on it)
- **New:** the prompt says new / add / build / "we haven't designed yet", or names a surface monday doesn't have (check "Monetization surfaces inventory" in [context/monday-context.md](../../context/monday-context.md))
- **Can't tell** ("our cancellation flow", "our top-up"): treat as existing if it's in that inventory, new if it isn't. Still unclear → fold it into the scoping question (below)

### Infer from the prompt first

| Signal in the prompt | Deliverable set |
|----------------------|-----------------|
| Shared design, screenshot, or Figma link — no deliverable named ("isn't converting" is a problem, not a deliverable) | Review + Copy + Requirements |
| "just score this", "review only" | Review |
| "wireframe", "mock it up", "show me how it'd look" | Spec + Copy + Wireframe, **plus Review + Requirements by default** — the review catches problems before build. Announce them as defaults; "wireframe only" stops at `03-wireframe.html` |
| "research", "benchmark", "how does X price", "how do companies sell AI credits" — no build ask | Research doc |
| "write copy for", "rewrite this CTA", "the copy feels flat" | Copy |
| "spec" / "brief" / "build" with no mention of a wireframe, or a vague "help with our {surface}" | **Ambiguous — ask the scoping question** |

**Combining signals.** Union the sets of every row that matches — "research how Notion sells credits, then wireframe ours" is Research + the wireframe set. A research ask doesn't settle the wireframe question: "research, then spec ours" still asks, with Q2 recommended Yes. "Just" / "only" caps the set to what's named, plus prerequisites. The fix loop is part of Review, not a separate deliverable — it runs whenever Review runs on a wireframe the chain built.

When the set is clear, don't ask — go to Step 2.

### Scoping question — only when ambiguous

Two pick-one questions in **one** message — it counts as one ask. Deliverables are cumulative (a wireframe needs spec + copy, requirements need a review), so "how far" is one choice, not a set of checkboxes. Use `AskUserQuestion` with both questions in a single call if available; otherwise send them as two numbered lists with "reply e.g. 2 / yes".

**Q1 — "How far should this go?"** (pick one; mark the recommended option by signal)

| New surface | Existing surface |
|-------------|------------------|
| Spec + copy — *recommended for "spec" / "brief" / "build"* | Review + fixed copy + requirements doc — *recommended* |
| Up to a wireframe (spec + copy + wireframe) | Review only |
| All the way to a requirements doc (adds review, fix loop, re-review) | Start fresh — new spec + copy |
| | Redesign all the way — new spec, copy, wireframe, fix loop, requirements |

**Q2 — "Start with a competitor research doc for inspiration?"** Yes / No — recommend Yes only if the prompt names competitors or asks how others do it.

If the surface is existing (or can't tell) and no design was shared: if it's publicly reachable (e.g. monday.com/pricing), don't ask — capture it yourself at 1440px and 375px into `.monetization/{feature-slug}/input/` (see Capturing screens below). If it's behind login, add one line to the same message: "Paste a screenshot or Figma link of the current version." If the user picked a review option and none arrives, that's a real blocker — ask once more; only treat the surface as new if they say it doesn't exist yet.

The answer is taken literally: "Up to a wireframe" stops at `03-wireframe.html`. The two existing-surface redesign options run the **new-surface** order — the current live design becomes an input to the spec (captured per the rule below), not the thing being reviewed. Never more than this one message. Don't explain the skills before asking.

### Prerequisites — add them, don't ask

| Deliverable | Needs | If missing |
|-------------|-------|------------|
| Wireframe | Spec + Copy | Add both |
| Review | Something to review | Surface exists and is public → capture it (see Scoping question). Behind login → ask for a screenshot or Figma link (a real blocker, per chain mode rules). Surface doesn't exist yet → add Spec + Copy + Wireframe |
| Requirements | A Review | Add Review (and its prerequisites) |
| Copy | A reason source — spec, review, or the user's existing surface/brief | Standalone copy works from the user's surface; otherwise add Spec |

Name every added prerequisite and default in the announcement, so the user sees why the chain is longer than what they asked for.

**Order is fixed — drop the steps not in the set, never reorder:**
- **New surface:** research → spec → copy → wireframe → review → fix loop (see below) → synthesis
- **Existing design:** review → copy → synthesis. Copy always rides with Review + Requirements on an existing design — there's no Copy box for it, and synthesis needs the strings. Skip the copy step only if the review flagged no Copy/CRO rows and added no new on-screen elements

**Spec + copy without a wireframe** ends at `02-copy.md` — nothing to review, so no review and no synthesis. Offer the wireframe once, after the copy.

**Wireframe without Review** ends at `03-wireframe.html`. Offer Review + Requirements once, after the wireframe.

---

## Step 2 — Announce and run

```
**Deliverables:** {list}{ — added: {item} ({prerequisite for X / default with wireframe})}
**Sequence:** {skill} → {skill} → …
**Artifacts:** {file list}
**No re-prompting between steps.**
{research nudge — see below}

Starting now →
```

Then immediately begin the first skill. Don't wait for the user to confirm.

**Research nudge.** On a new-surface build (the surface doesn't exist yet) where the scoping question wasn't asked (a Q2 "No" is final) and the prompt names no competitors, add one line above "Starting now": `Say "add research" to benchmark competitors first.` No question, no stop. If the user says it after the spec is written, run `pricing-intelligence`, then revise the spec as `01-spec-v2.md` using the research. If copy already exists and the revised spec changed the reason or direction, revise it as `02-copy-v2.md`; otherwise keep it. Continue the chain from there.

---

## Chain mode rules

A chain is any sequence the router announced before the first skill started. While a chain is running:

- **The router owns sequencing.** Each skill delivers its artifact, then control returns here for the next step. Skills don't decide what runs next.
- **No next-step blocks.** Skills omit their `→ Next step` block — it's a prompt for a human to re-type, and in a chain nobody needs to.
- **No optional offers mid-chain.** Skip "want me to mock this up?" and similar questions. Offer them once, after the final artifact.
- **External writes wait for the end.** Logging to monday.com or posting anywhere is offered once after the final artifact, never done mid-chain.
- **Only stop for a real blocker:** a missing input the skill can't work without (one question, per that skill's intake rules), or a paid PricingSaaS call, which always needs confirmation per the plugin's standing rules. Resume the chain once answered.

---

## Chain presets

The common deliverable sets, pre-assembled. Anything else is built from Step 1's order and prerequisites.

### Review → Fix → Synthesize ← default when a design is shared
> "Here's our trial-expiry pricing modal — it's not converting" / screenshot / Figma link

1. `monetization-design-reviewer` → scored rubric + ranked fix list (`04-review.md`)
2. `improve-conversion-surfaces-copy` → 2–3 options with one ★ recommended for **every** Copy/CRO row in `04-review.md`. File: `02-copy.md` if none exists (review-first pass), otherwise `02-copy-v2.md`
3. **Synthesis** → `05-requirements.md`

Announce before starting:
```
**Deliverables:** review, copy rewrites, requirements
**Sequence:** design review → copy rewrites → requirements synthesis
**Artifacts:** 04-review.md, 02-copy.md, 05-requirements.md
**One requirements doc at the end — no re-prompting between steps.**

Starting now →
```

### Spec → Copy → Wireframe → Review → Synthesize
> "Wireframe a paywall for AI Agents on Free tier" / scoping answer includes Wireframe + Review

1. `monetization-surface-spec` → `01-spec.md` (names the reason and direction, no final copy)
2. `improve-conversion-surfaces-copy` → `02-copy.md` from the spec's reason
3. `monetization-surface-spec` (re-invoked) → `03-wireframe.html` built with the real copy
4. `monetization-design-reviewer` (independent) → `04-review.md`, every row tagged fixable or blocked
5. **Fix loop** → fixable rows go back to the skill that owns them, then an independent re-review (`04-review-v2.md`). Max 2 passes — see Fix loop below
6. **Synthesis** → `05-requirements.md`, describing the approved wireframe version

### Spec → Copy ← spec requested, no wireframe
> Scoping answer: Spec + copy only

1. `monetization-surface-spec` → `01-spec.md`
2. `improve-conversion-surfaces-copy` → `02-copy.md`

Ends here — no review, no synthesis. After the copy, one line: offer `03-wireframe.html`.

### Research → Spec
> "Research how other tools do credit top-ups, then spec ours"

1. `pricing-intelligence` → monetization model benchmarking (sub-workflow B: AI credits), saved to `.monetization/research/{topic-slug}-{YYYY-MM}.md`
2. Continue into whichever build preset the deliverable set calls for (Spec → Copy, or the full wireframe chain). Pass the research artifact path to `monetization-surface-spec` as input — it cites the competitor examples in References and uses "So what for monday.com" to shape the copy direction

### Research → Positioning
> "How does Asana price compared to us? We're about to run a pricing page test"

1. `pricing-intelligence` → company research + pricing page teardown
2. Offer: the Spec chain for a pricing page variant using the findings

Research-only runs end at the research artifact — no synthesis, since there's nothing to implement yet.

---

## Fix loop — between review and synthesis

Runs in the new-surface chain, where the chain built the wireframe and can change it. Not in the existing-design chain: the team's live design isn't the chain's to edit, so its findings go to synthesis as requirements.

The point: the requirements doc should hand dev a wireframe that's already right, not a wrong wireframe plus a list of corrections.

### Independent review — every pass, every chain

Run each review pass — first review, every re-review, and the review in the existing-design chain — in a fresh subagent via the `Agent` tool. Give it only file paths: the artifacts under review, [monetization-design-reviewer/SKILL.md](../monetization-design-reviewer/SKILL.md), its scoring rubric, the surface's playbook, and `monday-context.md`. Not the conversation, not the reasoning that produced the artifacts. The skill that built the design shouldn't be the one that approves it.

The subagent can't see the chain, so the brief must start with a mode line, or the reviewer will pick its standalone branch and run the rest of the chain itself:

```
Mode: router review — {first review | re-review, pass N}. Write {file name} and return the verdict line. Then stop: no handoff, no next-step block, no prototype offer.
```

No subagent tool available → run the review inline and set `reviewer: inline (not independent)` in the review's header.

### Capturing screens for a review

The reviewer can only score what it can see, so the router hands it rendered images — of a live page (captured per the Scoping question rule) or of every state of a chain-built wireframe (`renders/v{N}-{state}.png`, both widths).

- **Desktop:** a 1440px (live page) or 1280px (wireframe) window.
- **Mobile — never trust a narrow window.** Headless Chrome won't render narrower than 500px; a "375px" screenshot is a 500px page cropped, and every cropped edge looks like horizontal overflow. Render mobile inside a 375px-wide iframe in a wider window, so the page gets a true 375px viewport. Tell the reviewer the grey strip beside the iframe is the harness. A live site that refuses to be framed (X-Frame-Options) gets a device-emulated capture (DevTools/Playwright device mode) instead; if neither is available, say so in the brief and have the reviewer mark mobile Pending rather than score a crop.
- **Wireframe states:** the wireframe opens the state named in its URL hash (`03-wireframe.html#critical`), so every state renders without clicking.

### The loop

1. **Route every fixable row to its owner.** The reviewer tags each row's Fix path. File names below are for a first revision — every revision takes the **next free version number for that artifact** (if the research nudge already wrote `01-spec-v2.md`, a spec fix writes `-v3`), and the pass number goes in the file's header (`fix-loop pass: 1`), never in the file name:

   | Fix path | Owner | Writes |
   |----------|-------|--------|
   | `copy` | `improve-conversion-surfaces-copy` (revision pass) | `02-copy-v2.md` |
   | `wireframe` | `monetization-surface-spec` (revision mode) | `03-wireframe-v2.html` |
   | `spec` | `monetization-surface-spec` (revision mode) | `01-spec-v2.md`, then `03-wireframe-v2.html` |
   | `blocked — {owner}` | nobody in the chain | straight to synthesis as an Open item |
   | `design team` | the team's designers (existing-design chain only) | straight to synthesis as a Design change |

   Order within a pass: spec → copy → wireframe, so the wireframe is rebuilt last with the revised copy. If a `spec` fix changed the reason or copy direction, the copy skill revises the affected lines in the same pass even though no row was tagged `copy`. A row can be fixable and partly blocked (build the path now with a marked `{slot}`; the fact comes later) — fix what can be fixed, and the blocked part still becomes an Open item.

2. **Re-review, independently** → `04-review-v2.md`. The reviewer verifies each fixable row (Resolved / Partly / Not resolved / Regressed) and checks the new version for issues the fixes introduced.

3. **Exit when** every fixable row is Resolved and the re-review found no new 🔴 or 🟠. New 🟡 found on re-review don't loop — they go to synthesis as Design changes, so the loop never turns into nitpicking.

4. **Otherwise run a second pass** on what's left (Not resolved, Partly, Regressed, new 🔴/🟠) → next-version artifacts → next review version.

5. **Hard cap: 2 fix passes.** Anything still open after pass 2 goes to synthesis as an Open item with the reviewer's reason. Never a third pass — at that point it needs a human.

6. **Copy for the 🟡 rows, once, after exit.** 🟡 rows skip the loop, but synthesis can't write copy — so a 🟡 row that needs new words would reach dev with no string. After the loop exits, run `improve-conversion-surfaces-copy` once for every 🟡 row (from any review version) whose recommendation needs a string, as a next-version copy file. No re-review: 🟡 is polish. Synthesis then quotes those strings like any other.

**Exit is "all fixable rows resolved", not a score.** Blocked rows hold the score down however many passes run, so a score threshold would loop forever on questions only Product can answer.

---

## Synthesis phase

Runs last in any chain that includes a review. Its reader is the designer and engineer who will build the fix — they should be able to start work from this doc alone, without opening the other artifacts.

### Inputs

Read the **latest version** of each numbered artifact in `.monetization/{feature-slug}/` — a `-v2`/`-v3` supersedes earlier versions for the lines it revises; unrevised lines still come from the earlier version. After a fix loop, the latest wireframe is the **build target** and the latest review holds the final scores. Read [context/monday-context.md](../../context/monday-context.md) for any price, limit, or credit figure. If `05-requirements.md` already exists, write `05-requirements-v2.md`.

### Rules

- **Traceability.** Every row of every review version appears at least once — in Final copy, Design changes, Open items, or Resolved before handoff — with a `Source` reference: `R{review version}.{row}` — `R1.3` = row 3 of `04-review.md`, `R2.1` = row 1 of `04-review-v2.md`. Use this notation everywhere in the doc. A row that needs both a string and a placement (e.g. "add a Free link") appears in both tables with the same Source; a row blocked on a fact also gets an Open item. Nothing gets dropped silently.
- **Copy is verbatim.** Every Final copy string is the ★ recommended option from the copy artifact, word for word. No paraphrasing, no new lines written here.
- **Specs are exact but not invented.** Name Vibe components and tokens only if they were confirmed from Figma variables or the Vibe MCP. Otherwise, specify relative to what's already on screen ("same text style as the plan feature rows, directly above the Pro CTA") and add "token TBD — confirm in Figma" rather than guessing a token name.
- **No invented numbers.** Credit-to-task conversions, prices, and limits come from `monday-context.md`. If the figure isn't there, the copy keeps a marked slot (`≈ {N} AI actions`) and an Open item names who supplies N.
- **No unverified claims.** Any factual promise in a Final copy string — a cancellation or refund policy, data retention after expiry, a guarantee — that isn't stated in `monday-context.md` gets an Open item naming who confirms it (Billing, Product) and is listed as a ship blocker. Copy that reads well but promises something untrue is worse than the line it replaced.
- **Check the reviewer's factual claims before they land.** An independent reviewer can still misread the input. For every row that asserts a fact — especially "contradicts monday-context.md", a price, a limit, or something "missing" from the design — re-derive it from the input (screenshot, Figma, artifact) and the context file. If it doesn't hold, keep the row for traceability but say so in its Open item ("R1.13 reading likely wrong: {why}") and never propose a context-file change built on it.
- **No direction-only rows.** "Improve", "consider", "strengthen", "make more X" are not requirements. If two people acting on a row would build different things, rewrite it.

### `05-requirements.md` format

Open with the header block from [templates/ARTIFACT_HEADER.md](../../templates/ARTIFACT_HEADER.md) (`skill: monetization-pm-router`, `status: review`).

```markdown
# Requirements: {surface name}

**Surface:** {type} · **Cohort:** {new / existing} · **Current score:** {X}/100 · **Projected score:** {Y}/100 if 🔴 + 🟠 ship
{**Build target:** latest 03-wireframe version — omit when no wireframe was built} · **Built from:** {every artifact version read}

## Final copy

| Element | Final string | Replaces | Reason it activates | Source |
|---------|-------------|----------|---------------------|--------|
| Headline | "..." | "Your Pro trial has ended" | Fear of losing capability | R1.1 |

## Design changes

| # | Priority | Component | Change | Spec | Source |
|---|----------|-----------|--------|------|--------|
| D1 | 🔴 | Pro CTA | ... | {placement, size, style, state behavior — tokens only if confirmed} | R1.5 |

## Resolved before handoff

Fix-loop chains only — rows already fixed in the build target, so dev knows they're done, not missing.

| Source | What was wrong | Fixed in |
|--------|----------------|----------|
| R1.4 | Differentiator overclaimed for some templates | 02-copy-v2.md, 03-wireframe-v2.html |

## Open items

Anything the review couldn't assess or that needs an input before build — pending mobile screenshot, unconfirmed close button, a missing data source.

| # | Owner | What's needed | Blocks | Source |
|---|-------|---------------|--------|--------|
| O1 | Design | 375px screenshot to confirm CTA stays above fold | D1 on mobile | R1.9 |

## Build order

| # | Priority | Owner | Task | Covers | Effort |
|---|----------|-------|------|--------|--------|
| 1 | 🔴 | Eng | ... | Final copy rows 1–2, D1 | S |
```

**Current and projected score:** copy both from the latest review version — the reviewer owns the rubric and computes it. It's a rubric projection, not a conversion forecast; don't restate it as a lift estimate.

### Self-check before delivering

1. Every row of every review version appears at least once, with its Source reference.
2. Every Final copy string matches the ★ recommended option verbatim.
3. No Vibe token or component name appears that wasn't confirmed — unconfirmed ones say "TBD".
4. No price, limit, or credit figure appears that isn't in `monday-context.md`.
5. Every factual promise in the copy (policy, retention, guarantee) not in `monday-context.md` has an Open item and is listed as a ship blocker.
6. Every reviewer row asserting a fact or contradiction was re-derived from the input; any that didn't hold says so in its Open item.
7. No row is direction-only.
8. Build order is sorted 🔴 → 🟠 → 🟡, and by effort (S → M → L) within each severity.

After delivering, one line only — existing-design chains: offer to build a wireframe of the fixed version via `monetization-surface-spec`, using the Final copy and Design changes as input. Fix-loop chains: no offer; the build target is already the fixed wireframe.

---

## Output from the router

**Single skill** (the deliverable set maps to one skill, e.g. Research doc only, Copy only, Review only):
```
**Routing to:** {skill-name}
**Why:** {one sentence}
**What you'll get:** {artifact names and what they contain}

Starting now →
```

**Chain:** use the Step 2 announcement block.

Either way, begin the first skill immediately.
