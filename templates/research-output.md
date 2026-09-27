# Research Output Template

Used by: `monetization-intelligence`
Applies to: company research, surface benchmarks, monetization teardowns, landscape scans, model benchmarking, battlecards, pricing-page teardowns

---

## Anatomy

Every research artifact follows this structure. Sections marked **[required]** are always present. Sections marked **[conditional]** are included only when the data exists — never padded with "no signal found."

---

```markdown
---
plugin: growth-monetization
skill: monetization-intelligence
feature / topic: {Company or topic} — {workflow type}
surface type: research
author: {name}
date: {YYYY-MM-DD}
status: draft
---

# {Company} — {Workflow title}
e.g. "Notion — Pricing Analysis" / "AI Credits Landscape — 2026" / "Asana vs monday.com — Battlecard"

## Exec summary [required]
Three bullets. Each one sentence. Never longer.

- **What we found:** {The single most important fact}
- **What it signals:** {Strategic implication — what this tells us about the company or market}
- **Recommended action:** {One specific thing monday.com should do or test as a result}

## Overview [required]
One sentence: what the company sells, what segment it targets, pricing model.

## Plan structure [required for company research]

| Plan | Monthly | Annual | Model | Notes |
|------|---------|--------|-------|-------|
| {Plan A} | ${x}/mo | ${x}/mo | per user / flat / usage | |

Source: [PricingSaaS]({pricingsaas link})

## Pricing model analysis [required for company research]
- **Value metric:** what they charge for and why it makes sense (or doesn't)
- **Tier differentiation:** what actually changes between tiers
- **Packaging logic:** how they gate features and what it signals about their target buyer
- **Freemium / trial:** conversion mechanism if applicable

## Historical changes [conditional]
Only include if history was pulled. Summarise each change period:

### {Period} — {N} changes
- {Change type}: {what changed, before → after}
- [View diff →]({pricingsaas diff URL})

## Enrichment findings [conditional]
Include only sub-sections where meaningful data was found.

### Wayback Machine
{Earliest and latest snapshots, what changed between them. Link both URLs.}

### Product changelog
{Entries referencing pricing, plans, or packaging. Link entries.}

### Earnings calls
{Management commentary on pricing rationale. Cite quarter + source.}

### Job postings
{Open monetization/pricing roles and their implication as a forward signal.}

### Sentiment
{What customers say on Reddit, G2, HN. Cite sources.}

## Strategic read [required]
2–3 sentences: what the pricing signals about positioning, growth motion (PLG vs SLG), and expansion strategy. Flag anything unusual.

## Landscape patterns [required for landscape scans — omit for single-company research]

| Pattern | Description | Companies |
|---------|-------------|-----------|
| {e.g. Usage-based shift} | {What's happening and why} | {List} |

## So what for monday.com [required]
Always present. Address each relevant point:

- **Pricing headroom:** Does this competitor suggest monday.com has room to raise, or is it pressure in the other direction?
- **Positioning implication:** Does their packaging change how monday.com should frame itself in deals?
- **Experiment to consider:** Name a specific hypothesis, the metric to watch, and the tier it affects.
- **Threat signal:** Anything in their pricing trajectory that creates risk for monday.com?

## Suggested playbook updates [required when the research covers a surface]
Exact additions for `playbooks/{surface}.md` — each tagged `[Verified]` / `[Reported]` / `[Teardown needed]`, sourced and dated, marked **new** or **replaces {what}**, and checked against what the playbook already says. The playbook owner applies them.

## What to do next [required]
2–4 tailored follow-up offers. Use specific names and findings from this research — not generic options.

---
→ Next step: {skill-name} — {one sentence}
→ Prompt: "{copy-pasteable prompt}"
```

---

## Formatting rules

- Tables over prose for plan structures and landscape comparisons
- Every company name links to `https://pricingsaas.com/companies/{slug}` on first mention
- Cite all enrichment sources with URLs — never present web findings as PricingSaaS data
- Omit empty sections entirely — no "N/A" or "no data found" rows
- Exec summary is always 3 bullets, always the first thing after the header
