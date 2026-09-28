# Artifact Header — growth-monetization plugin

Every artifact produced by this plugin opens with this block. Copy it, fill it, never skip it.

```
---
plugin: growth-monetization
skill: {skill-name}
feature / topic: {feature name or research subject}
surface type: {pricing-page | paywall | promotion | upgrade-trigger | credit-ui | trial | cancellation | research | landscape}
data: {live — {tool}, {date range}, run {YYYY-MM-DD} | not measured — {Kramer | BigBrain} not connected | n/a — no monday numbers}   # internal-data artifacts: sizing, journey, spec, review, requirements
verified against: {brain name}, {YYYY-MM-DD}                 # monday facts cited from BigBrain
cohort: {new-user | existing-user | both | n/a}
author: {name}
date: {YYYY-MM-DD}
status: {draft | review | approved}
confirmed with user: {field: value; …}                      # inputs the user answered at intake
inferred: {field — from {source}; …}                        # inputs inferred from a named source
# optional — add when they apply:
reviewer: {independent (subagent) | inline (self-graded)}   # review + requirements artifacts
fix-loop pass: {1 | 2 | 3}                                  # revisions written by the fix loop
revises: {file} for {review rows}                           # any -v2/-v3 file
---
```

## Field definitions

| Field | Required | Notes |
|-------|----------|-------|
| `skill` | Yes | Exact skill name as in plugin.json |
| `feature / topic` | Yes | e.g. "Credit depletion modal — Pro tier" or "Notion pricing research" |
| `surface type` | Yes for design artifacts | From the 7 surface types in monetization-surface-spec |
| `cohort` | Yes for design artifacts | Which user type this surface addresses |
| `data` | Yes for sizing, journey, spec, review, requirements | The data tool, range and run date behind every monday number — or `not measured` when the user chose to continue without data. Then the body opens with the one-line notice from CLAUDE.md's Data gate, and every unmeasured figure carries a `[Not measured]` mark — nothing else: no analyst request or query list. Artifacts with data are internal |
| `verified against` | Yes when the artifact cites a monday price, limit, credit amount, gate or trial term | The BigBrain brain and date. Without BigBrain (copy, research, or a run that continued without it) write `monday-context.md, verified-against {date} — unverified` |
| `author` | Yes | Person who ran the skill |
| `date` | Yes | ISO date — auto-filled when possible |
| `status` | Yes | Start as `draft`, move to `review` before sharing |
| `confirmed with user` | Yes, when intake asked anything | The answers from intake (the Growth PM's Step 1b, or the skill's own). This replaces any `Assumptions` section — an artifact never has one |
| `inferred` | Yes, when anything was inferred | Each inferred field with the source it came from. A field with no source to point to wasn't inferred; it's a gap to ask |
| `reviewer` | Review and requirements artifacts | `inline (self-graded)` whenever no independent subagent ran the review |
| `fix-loop pass` | Fix-loop revisions | Which pass wrote this version |
| `revises` | Any `-vN` file | Which file and which review rows it revises |

Wireframes carry the same fields in their HTML header comment, plus `Built from:` (which spec and copy versions). The requirements doc also carries the final ledger line.

## Output folder convention

All artifacts land in `.monetization/` in the working directory:

```
.monetization/
├── {feature-slug}/
│   ├── 00-sizing.md        ← monetization-opportunity-sizing (ARR at stake, baselines, go / no-go — internal)
│   ├── 00-journey.md       ← monetization-journey-map (scenarios + every step; the spec's flow map comes from here)
│   ├── 01-spec.md          ← monetization-surface-spec (names the reason, hands off)
│   ├── 02-copy.md          ← improve-conversion-surfaces-copy (real copy — the wireframe is built from this)
│   ├── 03-wireframe.html   ← monetization-surface-spec (built from 02-copy.md, not placeholders)
│   ├── 03-journey.html     ← monetization-journey-map (board: the real wireframe state on each journey step)
│   ├── 04-review.md        ← monetization-design-reviewer (scores the real thing; flags → 02-copy-v2.md)
│   └── 05-requirements.md  ← monetization-growth-pm synthesis (final copy, design specs, build order)
└── research/
    └── {topic-slug}-{YYYY-MM}.md
```

**Folder naming:** lowercase, hyphenated, descriptive. `credit-depletion-modal`, `trial-upgrade-nudge`, `notion-pricing-2026`.

**File numbering:** fixed per skill — 00 sizing and journey (sizing first), 01 spec, 02 copy, 03 wireframe and journey board, 04 review, 05 requirements. Copy runs before the wireframe, not after the review, so the wireframe and the review both reflect real language. Iterations get a version suffix (`02-copy-v2.md`).

## Next step block (standalone runs only — omitted inside a Growth PM chain)

```
---
→ Next step: {skill-name} — {one sentence: what it does and why it follows from this artifact}
→ Prompt: "{copy-pasteable prompt the user can send to trigger the next skill}"
```

Example:
```
---
→ Next step: monetization-design-reviewer — score the spec, copy, and wireframe together
→ Prompt: "Review .monetization/credit-depletion-modal/"
```
