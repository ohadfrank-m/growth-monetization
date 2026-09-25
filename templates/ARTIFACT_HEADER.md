# Artifact Header — growth-monetization plugin

Every artifact produced by this plugin opens with this block. Copy it, fill it, never skip it.

```
---
plugin: growth-monetization
skill: {skill-name}
feature / topic: {feature name or research subject}
surface type: {pricing-page | paywall | promotion | upgrade-trigger | credit-ui | trial | cancellation | research | landscape}
cohort: {new-user | existing-user | both | n/a}
author: {name}
date: {YYYY-MM-DD}
status: {draft | review | approved}
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
| `author` | Yes | Person who ran the skill |
| `date` | Yes | ISO date — auto-filled when possible |
| `status` | Yes | Start as `draft`, move to `review` before sharing |
| `reviewer` | Review and requirements artifacts | `inline (self-graded)` whenever no independent subagent ran the review |
| `fix-loop pass` | Fix-loop revisions | Which pass wrote this version |
| `revises` | Any `-vN` file | Which file and which review rows it revises |

Wireframes carry the same fields in their HTML header comment, plus `Built from:` (which spec and copy versions). The requirements doc also carries the final ledger line.

## Output folder convention

All artifacts land in `.monetization/` in the working directory:

```
.monetization/
├── {feature-slug}/
│   ├── 01-spec.md          ← monetization-surface-spec (names the reason, hands off)
│   ├── 02-copy.md          ← improve-conversion-surfaces-copy (real copy — the wireframe is built from this)
│   ├── 03-wireframe.html   ← monetization-surface-spec (built from 02-copy.md, not placeholders)
│   ├── 04-review.md        ← monetization-design-reviewer (scores the real thing; flags → 02-copy-v2.md)
│   └── 05-requirements.md  ← monetization-growth-pm synthesis (final copy, design specs, build order)
└── research/
    └── {topic-slug}-{YYYY-MM}.md
```

**Folder naming:** lowercase, hyphenated, descriptive. `credit-depletion-modal`, `trial-upgrade-nudge`, `notion-pricing-2026`.

**File numbering:** fixed per skill — 01 spec, 02 copy, 03 wireframe, 04 review, 05 requirements. Copy runs before the wireframe, not after the review, so the wireframe and the review both reflect real language. Iterations get a version suffix (`02-copy-v2.md`).

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
