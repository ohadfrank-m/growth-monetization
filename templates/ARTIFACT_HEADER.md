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

## Output folder convention

All artifacts land in `.monetization/` in the working directory:

```
.monetization/
├── {feature-slug}/
│   ├── 01-spec.md
│   ├── 02-wireframe.html
│   ├── 03-review.md
│   └── 04-copy.md
└── research/
    └── {topic-slug}-{YYYY-MM}.md
```

**Folder naming:** lowercase, hyphenated, descriptive. `credit-depletion-modal`, `trial-upgrade-nudge`, `notion-pricing-2026`.

**File numbering:** fixed per skill — 01 spec, 02 wireframe, 03 review, 04 copy. Iterations get a version suffix (`01-spec-v2.md`).

## Next step block (required at end of every artifact)

```
---
→ Next step: {skill-name} — {one sentence: what it does and why it follows from this artifact}
→ Prompt: "{copy-pasteable prompt the user can send to trigger the next skill}"
```

Example:
```
---
→ Next step: monetization-design-reviewer — score the wireframe against the CRO rubric before it goes to design
→ Prompt: "Review the wireframe in .monetization/credit-depletion-modal/02-wireframe.html"
```
