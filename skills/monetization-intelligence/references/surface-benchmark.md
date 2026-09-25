# Surface benchmark workflow

How do competitors run a specific monetization surface — end to end, screen by screen? This is the research a spec or a review of that surface should start from.

Covers all seven surface types: pricing page · paywall / feature gate · promotion · tier upgrade trigger (seats, limits) · credit / consumption UI (meter, depletion, top-up) · cancellation / downgrade · trial (start, mid-trial, expiry).

## When to run

- "How do Notion, ClickUp and Asana handle cancellation?" / "benchmark upgrade flows" / "best-in-class credit top-up" / "how does X's paywall work"
- As the first step of a Growth PM chain building a new surface (the Growth PM passes the surface type)
- Before reviewing a monday.com surface, when the reviewer needs a sourced benchmark the playbook doesn't have

For a pricing page, run [pricing-page-teardown.md](pricing-page-teardown.md) per competitor instead — it already covers that surface in depth — then summarize across them with Step 5 below. For trial *structure* (length, card required, free-tier limits), pull from [freemium-trial-tracker.md](freemium-trial-tracker.md) and add the flow capture here.

---

## Step 1: Fix the surface and the set

- **Surface type** — one of the seven. If the prompt names a flow that spans two (e.g. "upgrade after the trial ends"), benchmark the flow as one surface and say which types it spans.
- **Competitor set: 5–8 companies.** Default: the work-management and PLG set that monday.com competes with, plus every company the prompt names, plus at least one AI-native company from the playbook's reference set (Clay, Figma, ClickUp, Claude) — they monetize AI in different ways and most monday surfaces now involve credits.
- **Cohort** — which user the surface serves (new / existing, IC / admin). It decides which state of the competitor's flow matters.

## Step 2: Read the playbook first

Open `playbooks/{surface}.md` (see [playbooks/README.md](../../../playbooks/README.md) for the file per surface). Note what it already covers per company. This run should **add** to it — new companies, fresher captures, gaps marked `[Teardown needed]` — not repeat it.

## Step 3: Capture each competitor's flow

For each company, find the flow, in this order of evidence strength:

1. **Vendor documentation** — help-center articles that describe the flow ("how to cancel", "what happens when you run out of credits", "start a trial") → `[Verified]`
2. **A capture you made** of any public step — pricing pages, public checkout entry, signup/trial start, public docs pages. Screenshot or fetch it; cite the URL and date → `[Verified]`
3. **Third-party write-ups** — teardown articles, UX case studies, walkthrough videos, community threads describing the flow → `[Reported]`, and say so inline
4. **Nothing seen** — the flow is behind a login or a paid account you don't have → `[Teardown needed]`. Say what's missing ("the save-offer screen after clicking Cancel on a paid workspace"). **Never describe a screen you haven't seen**, and never infer UI from a pricing page.

Search patterns:

```
WebSearch(query="{Company} how to cancel subscription help center")
WebSearch(query="{Company} {surface} flow teardown")
WebSearch(query="{Company} what happens when you run out of credits")
WebSearch(query="{Company} {surface} screenshots walkthrough 2026")
WebFetch(url="{help-center article}", prompt="List each step of the flow in order, what the user sees and can do at each step, and any offer or alternative presented.")
```

Capture per company — and leave a field out rather than guess it:

| Field | What to record |
|-------|---------------|
| Entry point | Where and how the surface appears (click, limit hit, date, notification) |
| Screens in order | One line per screen: what it shows, what the user can do |
| Headline + CTA copy | Only if seen in a cited source; otherwise paraphrase and say so |
| Offer mechanics | Cancellation: pause, downgrade, discount, survey, win-back. Paywall: preview, trial path, lowest tier that unlocks. Top-up: package sizes, auto top-up, rollover. Trial: length, card required, what's gated, expiry behaviour. Upgrade: seat/limit messaging, admin approval path |
| Escape hatch | How the user declines or leaves, and how visible it is |
| After | Confirmation, resume path, data retention, win-back emails |
| Main friction | The one step most likely to cause drop-off or resentment, and why |
| Evidence | Tag + source URL + date checked, per field where they differ |

## Step 4: Write each company in the playbook shape

Use the same shape the playbooks use, so a finding can move into a playbook without rewriting:

**What they ship → Flow → UI → Copy pattern → Why it works → Where it breaks → Steal for monday.com**

Keep each company to one short block. "Why it works" and "Where it breaks" are judgments — tie each to a named principle from the playbook or to evidence (a vendor statement, user complaints), not to taste.

## Step 5: Synthesize across the set

- **At-a-glance table** — one row per company, one column per step of the flow (entry · screens · offer · escape · after). This is the table a spec's flow map is built from.
- **Patterns to steal** — 3–5, each naming which companies do it and why it fits monday.com.
- **Patterns to avoid** — each naming the company, what breaks, and the evidence.
- **Flow implications for the spec** — the screens monday's version needs, in order, with the friction point each competitor pattern suggests at that step. `monetization-surface-spec` reads this directly into its flow map.
- **Coverage** — how many companies were `[Verified]` vs `[Reported]` vs `[Teardown needed]`, and the specific screens someone with account access should capture.

## Step 6: So what for monday.com

Read [context/monday-context.md](../../../context/monday-context.md) first — the surface inventory, cohorts, tiers, and credit behaviour.

- **Adopt / adapt / avoid** — for each pattern, one line on whether monday should take it as-is, change it (and how), or skip it.
- **Gap vs. monday today** — what monday's current version of this surface does or lacks, from the surface inventory.
- **Experiment to consider** — one hypothesis, the metric, the tier and cohort.
- **Threat signal** — a competitor pattern that makes monday's current surface look worse by comparison.

## Step 7: Suggested playbook updates

Durable knowledge belongs in `playbooks/{surface}.md`, owned once and cited by the spec and reviewer skills. End the report with the exact additions — new company teardowns, corrected facts, new anti-patterns — each tagged and sourced, and marked **new** or **replaces {what}**. Check every one against what the playbook already says; don't propose a duplicate. The playbook owner applies them; this skill doesn't edit the playbook itself.

---

## Output file

`.monetization/research/{surface}-benchmark-{YYYY-MM}.md` — e.g. `cancellation-benchmark-2026-09.md`. Same name standalone or in a Growth PM chain; it follows the plugin's `{topic-slug}-{YYYY-MM}.md` convention with `{surface}-benchmark` as the topic.

Use the research artifact template: [../../../templates/research-output.md](../../../templates/research-output.md). The template's company-research sections (plan structure, historical changes) are replaced by Steps 4–7 here.

## Next step (standalone)

```
---
→ Next step: monetization-surface-spec — spec monday's version of this surface from the benchmark
→ Prompt: "Spec a {surface} for {tier / cohort} using .monetization/research/{file}"
```
