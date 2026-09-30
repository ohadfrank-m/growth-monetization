---
name: monetization-experiment-analyzer
description: Post-ship experiment results analysis. Reads a completed A/B test on a monetization surface, runs SRM and trust checks first, then calculates lift and statistical significance, checks guardrails, sizes ARR impact on real monday data, and delivers a ship / kill / iterate verdict with a full audit trail. Call this after an experiment has run its minimum runtime. It is standalone — not part of the Growth PM design chain.
version: 0.1.0
---

# Monetization Experiment Analyzer

**Read first:** [plugin-rules.md](../../plugin-rules.md) — the plugin-wide rules (intake, Data gate, tool names, artifact standards). Hosts don't load it automatically: read it before doing anything else in this run, unless it's already in this conversation.

You read the results of a shipped A/B experiment on a monetization surface and produce a single artifact, `06-results.md`, that a PM or engineering lead can use to make and defend a ship / kill / iterate decision.

This skill is **standalone only** — it's called after an experiment ships, not inside the Growth PM design chain. The sizing skill (`monetization-opportunity-sizing`) designed the experiment; this skill reads what actually happened.

---

## Required context

| Input | Where | Required? |
|-------|-------|-----------|
| Experiment name or ID | Prompt | Required |
| What was tested (surface, variant description) | Prompt / `00-sizing.md` | Required |
| Primary metric (conversion, trial start rate, upgrade rate…) | Prompt / `00-sizing.md` | Required |
| Guardrail metrics (e.g. D7 retention, support contacts, revenue per user) | Prompt / `00-sizing.md` | Required — cannot assess safety without them |
| Pre-experiment baseline for primary metric | `00-sizing.md` or Kramer | Required |
| Control and variant sample sizes | Kramer or prompt | Required |
| Control and variant event counts (primary metric) | Kramer or prompt | Required |
| Pre-planned MDE and α (significance threshold) | `00-sizing.md` or prompt | If missing, assume α=0.05 two-tailed and note it |
| Experiment start and end dates | Prompt or Kramer | Required |
| Account plan / tier split (for ARR sizing) | BigBrain | Recommended — mark `[Not measured]` if unavailable |
| `00-sizing.md` from the design phase | `.monetization/{feature-slug}/` | Strongly recommended — aligns baselines |

Run intake the same way every skill does: check the table, infer what's obvious with its source, ask every real gap in one message (at most 4 questions). If nothing is missing, ask nothing.

---

## Data gate

This skill makes quantitative claims about monday's own data. Apply the Data gate from `plugin-rules.md`:

- **Kramer MCP** — primary source for experiment counts, sample sizes, and baseline rates. Query `data-expert-agent` / `kramer` tools.
- **BigBrain** — plan and price data for ARR impact sizing. Search for `bigbrain`, `plans`, `prices` tools.

If either MCP is missing, name it, say what it unlocks (Kramer: experiment counts; BigBrain: ARR impact), link [mcp-setup.md](../../mcp-setup.md), and ask once: **Connect now** or **Continue without data**. Continue: every number sourced from the missing MCP is marked `[Not measured]` and the artifact opens with one line flagging what's missing.

---

## Step 1 — Load the design-phase context

Before querying anything, read:

1. `.monetization/{feature-slug}/00-sizing.md` — the pre-experiment baseline, MDE, planned α, and the original go/no-go threshold.
2. Any previously written `06-results.md` — if one exists, this is a re-read (e.g. extended runtime); note any changes from the prior read.

If `00-sizing.md` is missing, note it in the artifact header and continue with user-supplied baselines.

---

## Step 2 — Pull experiment data from Kramer

Query Kramer for:

1. **Assignment counts** — control and variant user/account counts, by day, for the full experiment window.
2. **Primary metric events** — conversions (or trials, upgrades, etc.) per arm.
3. **Guardrail metric events** — every guardrail metric the prompt or `00-sizing.md` named.
4. **Day-by-day breakdown** — needed for the Twyman's law check and novelty-effect scan.

Show each query and its result in the artifact. An unmeasured number is marked `[Not measured]` — never estimated.

---

## Step 3 — Trust checks (run before reading any metric)

Run all trust checks before reporting any result. A failed trust check changes what you can conclude; report it prominently.

### 3a — Sample ratio mismatch (SRM)

Expected ratio: the pre-planned split (default 50/50 unless stated otherwise).

Chi-square test:

```
χ² = Σ (observed − expected)² / expected
```

- If χ² < 3.84 (p > 0.05): SRM absent — proceed.
- If χ² ≥ 3.84 (p ≤ 0.05): **SRM detected** — stop reading results. The assignment mechanism is broken. Report what you see, state the likely cause categories (bot traffic, logging gaps, mid-experiment changes), and recommend: fix and re-run, or run a diagnostic query to identify the break point.

### 3b — Runtime check

Confirm the experiment ran for at least:
- The minimum runtime from `00-sizing.md`, **and**
- At least 2 complete calendar weeks (to cover day-of-week cycles per §7 of `experiment-design.md`).

If it ran fewer than 14 days, flag it — the result may not be stable.

### 3c — Twyman's law scan

A result that looks too good to be true usually is. If the observed lift is more than 2× the pre-planned MDE, flag it and check:
- Was the experiment assignment stable day-over-day?
- Is there a logging or attribution change that coincides with the start date?
- Does the day-by-day breakdown show a step-change rather than a gradual pattern?

State what you find. A suspicious result doesn't kill the analysis, but it must be disclosed.

---

## Step 4 — Primary metric: two-proportion z-test

Only run this step if Step 3 passed (no SRM, runtime met).

```
p̂_c = events_c / n_c
p̂_v = events_v / n_v
p̂   = (events_c + events_v) / (n_c + n_v)

z = (p̂_v − p̂_c) / √(p̂ × (1 − p̂) × (1/n_c + 1/n_v))
```

Two-tailed p-value from z. Apply the significance threshold α from `00-sizing.md` (default 0.05).

Report:
- Observed rates for control and variant
- Absolute lift (pp) and relative lift (%)
- 95% confidence interval: `(p̂_v − p̂_c) ± 1.96 × SE`
- z-statistic and p-value
- Significance verdict: significant / not significant at α

Show the arithmetic. Don't round intermediate values.

---

## Step 5 — Guardrail checks

For each guardrail metric: run the same two-proportion z-test (Step 4). A guardrail breach is defined as a statistically significant negative movement (p < 0.05) in any guardrail metric.

**A guardrail breach is an unconditional ship block.** Even if the primary metric is positive and significant, a breached guardrail means: do not ship. State this clearly.

For each guardrail:
- Observed rates and absolute change
- z and p-value
- Status: **Clear** / **Breached** / **Directionally negative (not significant)**

If no guardrail data is available from Kramer, mark each guardrail `[Not measured]` and note that safety cannot be assessed — this is a ship-blocker until measured.

---

## Step 6 — ARR impact sizing

If the primary metric is significant and no guardrail is breached, size the ARR impact.

Pull from BigBrain:
- Affected account count (by plan and tier for the experiment cohort)
- ARPA by plan tier

```
ARR impact = affected_accounts × (observed_lift_pp / 100) × conversion_to_revenue_rate × ARPA
```

Where `conversion_to_revenue_rate` is the fraction of the primary metric event that translates to new ARR (e.g. for trial starts: trial-to-paid rate from `00-sizing.md`). Show the formula and every input. Mark `[Not measured]` for any BigBrain input that's missing.

Report low / base / high:
- Low: lower bound of the 95% CI for lift × low ARPA estimate
- Base: observed lift × median ARPA
- High: upper bound of CI × high ARPA estimate

---

## Step 7 — Verdict: §8 decision table

Apply the decision table from `skills/monetization-growth-pm/references/experiment-design.md §8`:

| Condition | Verdict |
|-----------|---------|
| SRM detected | **No verdict** — fix assignment, re-run |
| Guardrail breached | **Kill / redesign** — unconditional; primary result is irrelevant |
| Primary: significant positive, guardrails clear | **Ship** — state ARR impact and monitoring plan |
| Primary: not significant, guardrails clear | **Kill or extend** — if n is below target, extend; otherwise kill |
| Primary: significant negative | **Kill** — do not ship |
| Decaying effect (day-by-day shows diminishing lift) | **Investigate** — novelty effect likely; recommend holdout or longer runtime |

State the verdict in one sentence at the top of the artifact, before any supporting detail.

---

## Artifact: `06-results.md`

Write this file to `.monetization/{feature-slug}/06-results.md`.

```
# Experiment results: {experiment-name}

**Verdict: {SHIP | KILL | KILL / REDESIGN | NO VERDICT — RE-RUN | INVESTIGATE}**
{one sentence stating why}

{artifact header — confirmed with user / inferred / open items — see plugin-rules.md}

---

## Trust checks

### SRM
{χ² value, expected vs observed counts, pass/fail}

### Runtime
{actual days vs minimum, pass/warn}

### Twyman's law
{flag or clear}

---

## Primary metric: {metric name}

| | Control | Variant |
|-|---------|---------|
| Sample size | {n_c} | {n_v} |
| Events | {e_c} | {e_v} |
| Rate | {p̂_c} | {p̂_v} |

Absolute lift: {+/− X.Xpp}
Relative lift: {+/− X%}
95% CI: [{lower}, {upper}]
z = {z}, p = {p}
**{Significant / Not significant} at α={α}**

---

## Guardrail checks

| Metric | Control | Variant | Change | p-value | Status |
|--------|---------|---------|--------|---------|--------|
| {guardrail 1} | | | | | {Clear/Breached/Directionally negative} |

---

## ARR impact

{only if ship verdict}

Low: ${X}M / Base: ${X}M / High: ${X}M ARR

Inputs: {accounts}, {ARPA by tier}, {lift used}

---

## Recommendation

{1–3 sentences: verdict rationale, any monitoring plan for a ship, or redesign direction for a kill}
```

End with a `→ Next step` block:

```
→ Next step
Ship: merge the variant, monitor {guardrail metrics} for 2 weeks post-launch.
Kill: archive `06-results.md`; if redesigning, run `/monetization-opportunity-sizing` with updated assumptions.
Iterate: identify which guardrail or SRM issue to fix before re-running.
```
