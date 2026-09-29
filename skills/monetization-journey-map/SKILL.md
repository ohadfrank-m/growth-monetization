---
name: monetization-journey-map
description: This skill should be used when the user wants to "map the user journey", "map the flow", "journey map for a cancellation / upgrade / trial / top-up flow", "what are the use cases", "use scenarios", "who hits this and why", "a day in the life", "map every step of the upgrade flow", "show the design on each step", or when a monetization surface is being built and the scenarios and end-to-end steps haven't been defined yet. Produces 00-journey.md (scenarios + every step before, on and after the surface) and, once a wireframe exists, 03-journey.html (a journey board with the real wireframe state on each step).
version: 0.2.2
---

# Monetization Journey Map

**Read first:** [plugin-rules.md](../../plugin-rules.md) — the plugin-wide rules (intake, Data gate, tool names, artifact standards). Hosts don't load it automatically: read it before doing anything else in this run, unless it's already in this conversation.

A monetization surface is one moment in a longer story. The user arrived from somewhere, wants something, and has a life after the screen — a resumed task, an invoice, a renewal, a win-back email. This skill maps that story **before** the spec: who hits the surface and why (scenarios), and every step they take (the journey). Every later skill reads it — the spec takes its flow map from it, the copy skill writes to each step's state of mind, the reviewer walks each scenario through the design.

It runs twice, like `monetization-surface-spec`:

| Pass | When | Writes |
|---|---|---|
| **1 — Map** | Before the spec (or on its own) | `.monetization/{feature-slug}/00-journey.md` |
| **2 — Board** | After `03-wireframe.html` exists | `.monetization/{feature-slug}/03-journey.html` |

The board is built after the wireframe on purpose: it embeds the real wireframe states, with real copy, instead of sketching screens with placeholder text (the plugin's copy-before-wireframe rule).

---

## Required context

Every run follows the plugin's intake protocol ([plugin-rules.md](../../plugin-rules.md), "Intake — ask, never assume"): check this table, infer what's obvious from a named source, ask every real gap in one message, then run. Inside a Growth PM chain, the Growth PM asked these up front; stop and ask only for a gap it didn't cover. Never write a gap down as an assumption.

| Field | Why it changes the output | Infer from |
|---|---|---|
| Surface type | Picks the stage skeleton | The prompt ("cancellation flow" → type 6); the 7 types in [monetization-surface-spec](../monetization-surface-spec/SKILL.md) |
| Cohort(s) | Which personas and scenarios exist | Surface type and [monday-context.md → User cohorts](../../context/monday-context.md#user-cohorts) |
| Tier and billing context | Changes branches (annual vs monthly, invoice-billed, Enterprise) | The prompt; default: every self-serve paid tier the surface applies to |
| New or existing surface | New: design the journey. Existing: map today's live journey first | Prompt, and the surfaces inventory in `monday-context.md` |
| Live design (existing only) | The current steps and their real friction | Screenshots in `input/`, a Figma link, or a public URL |

---

## Pass 1 — Map (`00-journey.md`)

Read first: the latest `00-sizing` version when it exists (reach, conversion and the role split are already queried there — split them by scenario rather than re-asking) — or, in a chain that continued without Kramer, write the sizing skill's Population and prices block at the top of this file ([monetization-opportunity-sizing](../monetization-opportunity-sizing/SKILL.md#without-kramer-inside-a-growth-pm-chain--no-file)) — [monday-context.md](../../context/monday-context.md), the surface's playbook in [playbooks/](../../playbooks/), and any research artifact the chain produced (a surface benchmark's "Flow implications for the spec" is the strongest input for the steps).

### Step 1 — Scenarios

Write the scenarios per [references/scenario-cards.md](references/scenario-cards.md): at least 3, always including the IC / admin pair: the person who hits the surface and the admin who can act on it (buy, cancel, change the plan) are usually different people. Each is a problem card (name · persona · trigger · frequency · current result · evidence · impact) plus a short first-person "day in the life". Stay on the problem — the screens come later.

### Step 2 — Evidence

Size every scenario with real data per [references/evidence-queries.md](references/evidence-queries.md) — aggregate counts from the Kramer data tools (read-only). Show every question asked and its source. This step runs the plugin's Data gate ([plugin-rules.md](../../plugin-rules.md), "Data gate — connect the data, or continue without it"): with no `data-expert-agent` tool, push the user to connect it and ask once (Connect now / Continue without data — in a Growth PM chain, its Step 1c answer holds). Continuing without data, every frequency is marked `[Not measured]`, and a query that fails twice is marked the same way. Never an estimate.

### Step 3 — The journey

Map every step per [references/journey-structure.md](references/journey-structure.md): the five stages (before → trigger → on-surface → hand-off → after), one row per step, every branch (success, abandon, error, IC path), the channel (in-app, email, admin notification, invoice), each step's state of mind and reason to act, friction and its reduction, the event that measures it, and — for on-surface steps — the **wireframe state id** the spec must use. Start from the stage skeleton for the surface type, then cut or add steps from the scenarios.

### Step 4 — Coverage check

Trace every scenario through the step table, start to finish. Each must reach an end state (converted, stayed, left cleanly, handed to admin or sales). A scenario that dead-ends is a gap: add the step, or name it as an Open item. Then list the edge cases the frequencies make primary — the spec treats those as main paths, not footnotes.

### Output format

Open with the header block from [templates/ARTIFACT_HEADER.md](../../templates/ARTIFACT_HEADER.md) (`skill: monetization-journey-map`), then:

```markdown
# Journey: {surface name}

{> Data tools weren't connected ({Kramer | BigBrain | Kramer, BigBrain}) — figures marked [Not measured] weren't measured. — only when the run continued without data}

**Surface:** {type} · **Cohorts:** {…} · **Tiers:** {…} · **Mode:** {new | live journey mapped from {source}}
**Data:** {live — {tool}, {date range}, run {YYYY-MM-DD} | not measured — Kramer not connected} · internal data, don't share outside monday

## Scenarios
{one problem card + day in the life per scenario — S1, S2, …}

## Scenario sizing
| Scenario | Frequency | Evidence | Query | Source |

## Journey
| J# | Stage | Step | Channel | Scenarios | User goal | State of mind · reason | System state | Branches | Friction → reduction | Event | Wireframe state |

## Scenario coverage
| Scenario | Path (J#s) | End state | Gap |

## Primary edge cases
{the edge cases the frequencies promote to main paths, for the spec}

## Open items
| # | Owner | What's needed | Blocks |
```

Standalone, end with:
```
---
→ Next step: monetization-surface-spec — spec the on-surface steps (J{a}–J{b}), taking the flow map from this journey
→ Prompt: "Spec .monetization/{feature-slug}/ from 00-journey.md"
```
Inside a Growth PM chain, omit it (chain mode rules in [monetization-growth-pm](../monetization-growth-pm/SKILL.md#chain-mode-rules)).

---

## Pass 2 — Board (`03-journey.html`)

Triggered once `03-wireframe.html` exists. If it doesn't, stop and hand off to `monetization-surface-spec` — the board embeds real states, so there's nothing to embed yet.

Build the board per the **board contract** in [references/journey-board.md](references/journey-board.md): one lane per scenario, one column per journey step, the real wireframe state embedded on every on-surface step (`03-wireframe.html#{state}`), low-fi cards with the real copy for off-surface steps (email, admin notification, invoice), friction pins, and a true 375px layout.

**Versions follow the wireframe.** The board embeds the latest wireframe version from the ledger. When the fix loop writes `03-wireframe-v{N}.html`, rebuild the board as `03-journey-v{N}.html` against it — same N, so the reviewer always walks the design it's scoring.

Every step with a wireframe state id must have that state to embed. A J step whose wireframe state id doesn't exist in the wireframe is a defect: embed an empty frame labelled "missing state {id}" and list it, so the reviewer sees the gap rather than a silently skipped step.

Standalone, end with:
```
---
→ Next step: monetization-design-reviewer — walk each scenario through the board and score the design
→ Prompt: "Review .monetization/{feature-slug}/"
```

---

## Existing-design mode — the live journey

When the surface is live and a design or public URL is available, pass 1 maps **today's** journey first: the steps as they actually are, from the screenshots in `input/` (or captures of a public page), with the friction each step really has. Mark every step `live`. A redesign then writes its proposed journey as a second table in the same file, and the coverage check compares both — which scenarios the live journey fails and the new one fixes. There's no board in this mode unless a new wireframe is built.

---

## Rules

- **Problem first, screens second.** Scenarios name the persona's problem in their words. Nothing in the Scenarios section names a UI element.
- **No invented numbers.** Frequencies and counts come from a query shown in the file, or are marked `[Not measured]` when the user continued without data or a query failed twice (Data gate). Never an estimate, never an unmarked `{slot}`. monday prices, limits and credit amounts come from BigBrain (in a Growth PM chain, its Step 1c answers), or from `monday-context.md` marked `[Unverified — …]` without it — never from memory.
- **No vague words.** The banned list in the Growth PM's synthesis rules applies here ([monetization-growth-pm → Synthesis phase → Rules](../monetization-growth-pm/SKILL.md#rules)).
- **Every scenario ends somewhere.** No scenario may stop mid-table without an end state or an Open item.
- **The journey owns the steps; the spec owns the screens.** Don't write layouts, trigger thresholds or copy here — name the step, the state of mind and the reason, and hand off.
- **Aggregate data only.** Never pull or write user-level records, emails or names. The file is internal.

## References

- Scenario cards and personas: [references/scenario-cards.md](references/scenario-cards.md)
- Journey stages, step table and per-surface skeletons: [references/journey-structure.md](references/journey-structure.md)
- Sizing scenarios with live data: [references/evidence-queries.md](references/evidence-queries.md)
- Board contract: [references/journey-board.md](references/journey-board.md)
- CRO why per surface (read, cite, never copy): [../../playbooks/](../../playbooks/)
- monday facts: [../../context/monday-context.md](../../context/monday-context.md)
