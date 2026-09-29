---
name: monetization-opportunity-sizing
description: This skill should be used when the user wants to "size this opportunity", "how much ARR is at stake", "is this worth building", "how many accounts hit this", "what's the baseline conversion", "sample size for this test", "go / no-go on this surface", or before any monetization surface is designed and nobody has put a number on it yet. Produces 00-sizing.md — reach × current conversion × addressable lift × ARPA → ARR at stake, in low / base / high cases, every input from a Kramer query or a BigBrain answer shown in the file (or marked not measured when you continue without them), plus testability and a go / no-go line. Runs first in every Growth PM chain that designs or reviews a surface.
version: 0.1.0
---

# Monetization Opportunity Sizing

Before anyone designs a surface, put a number on it: how many accounts hit the moment, how many convert today, how much of the gap a better surface could close, and what each conversion is worth. The answer decides whether the build is worth it, and its baselines are the ones the journey, the spec's success metrics and the measurement plan all use. No other skill re-queries them.

**The model:** reach × current conversion × addressable lift × ARPA → **ARR at stake per year**, for a low, base and high case. Mechanics, definitions and the query set: [references/sizing-model.md](references/sizing-model.md).

Writes `.monetization/{feature-slug}/00-sizing.md`. It runs before `00-journey.md` — same number, since both are pre-design, and sizing comes first.

---

## Required context

Every run follows the plugin's intake protocol ([CLAUDE.md](../../CLAUDE.md), "Intake — ask, never assume"): check this table, infer what's obvious from a named source, ask every real gap in one message, then run. Inside a Growth PM chain, the Growth PM asked these up front; stop and ask only for a gap it didn't cover. Never write a gap down as an assumption.

| Field | Why it changes the output | Infer from |
|---|---|---|
| Surface and trigger | The trigger *is* the population: "credit balance hits 100%" and "hits 80%" are different reach | The prompt; the surfaces inventory in [monday-context.md](../../context/monday-context.md). Never a threshold you'd have to pick |
| Cohort and tier(s) | Which accounts are counted | Surface type; the prompt |
| Objective metric | Defines "conversion" — upgrade, top-up, save, trial-to-paid | The prompt; the surface's primary in [experiment-design.md](../monetization-growth-pm/references/experiment-design.md) §3 |
| Longest test the team will run | Decides whether a test can read the base-case lift | The prompt only. Ask; recommended answer: 6 weeks |
| Smallest ARR that justifies the build | The go / no-go bar | The prompt only — never inferred. If the user has none, the verdict covers testability only and the bar becomes an Open item for Product |

---

## Data gate

This skill is all data, so connecting both sources matters most here. It runs the plugin's Data gate ([CLAUDE.md](../../CLAUDE.md), "Data gate — connect the data, or continue without it") before writing anything, for both sources it needs:

| Source | Search the tools for | Used for | Missing |
|---|---|---|---|
| Kramer MCP | `data-expert-agent`, `kramer` (e.g. `kramer-mcp-v1`) | Reach, conversion, conversion lag, the ceiling segment, past experiment lifts, converter plan mix and seats | Every input and the whole model are `[Not measured]`; verdict `Not sized — no data` |
| BigBrain AI Brains | `AI Brain`, `ai-brain`, `bigbrain` (e.g. `AI Brain - Payments`) | List prices per seat and per credit package for the plan the conversion lands on | Prices from `monday-context.md`, marked `[Unverified — …]` |

With either missing, push to connect: print the gate's connect block — the missing MCP, what it unlocks here (the opportunity size, the baselines, verified prices), the link to [mcp-setup.md](../../mcp-setup.md) — and ask with the question tool ([CLAUDE.md](../../CLAUDE.md) → Tool names): **Connect now (recommended)** · **Continue without data**. Inside a Growth PM chain, the Growth PM already asked (Step 1c); follow its answer and don't ask again.

**Continuing without Kramer** still writes `00-sizing.md`, just not a sized one: the one-line notice at the top (CLAUDE.md, Data gate), the population definition, the model with every input and result marked `[Not measured]`, prices (from BigBrain, or `[Unverified — …]`), and the verdict **Not sized — no data**. Nothing in it is estimated. No query list, analyst request or data Open item — the marks are the only trace.

A query that fails or times out is retried once in the same session; a second failure marks that input `[Not measured — query failed]`, is told to the user, and the run continues. Never an unmarked `{slot}`, never an estimate.

---

## Workflow

### Step 1 — Define the population

Turn the trigger into one query definition: the event, the unit (account), the tiers, the window (last 90 full days; 12 months when seasonal — renewals, promotions). Ask `data-expert-agent` for reach with that definition, then check what its answer counts (accounts vs users, which table, which filter). When the definition differs from the trigger, ask a follow-up in the same session rather than using it ([evidence-queries.md](../monetization-journey-map/references/evidence-queries.md) → Rules).

### Step 2 — Pull the inputs

Run the query set in [references/sizing-model.md](references/sizing-model.md#the-query-set) in one `data-expert-agent` session (pass the `sessionId` forward): reach by tier, billing period and role; current conversion to the objective within the window; the conversion lag (which sets the window); the best comparable segment's conversion (the internal ceiling); lifts from past monday experiments on this surface type; and the plan / package mix and median seats of accounts that converted.

Start the queries together and poll each `jobId` every ≥5 s — they're independent.

### Step 3 — Prices from BigBrain

Ask the Payments brain for the current list price of each plan or credit package in the converter mix, per seat and billing period. Compare each answer with [monday-context.md](../../context/monday-context.md). A mismatch is reported, never silently used: use the BigBrain answer with its source tag, list the difference under **Context drift** in the file, and tell the user in one line (the plugin's source-of-truth rules in [CLAUDE.md](../../CLAUDE.md)).

### Step 4 — Model the cases

Compute ARPA and the three cases per [references/sizing-model.md](references/sizing-model.md#the-model). Every cell traces to a row in Inputs. The lift cases come from monday's own history (past experiments, the ceiling segment), never from a competitor claim or a playbook benchmark.

### Step 5 — Testability

With the baseline and weekly reach, compute the sample per arm and the runtime for the base-case lift ([experiment-design.md](../monetization-growth-pm/references/experiment-design.md) §5), and the smallest lift the traffic can detect within the longest test the team will run. This is what the measurement plan inherits.

### Step 6 — Verdict

One line, from the table in [references/sizing-model.md](references/sizing-model.md#go--no-go): **Go — test**, **Go — ship + holdout**, **Re-scope**, **No-go**, or **Not sized — no data**, with the base-case ARR against the bar and the runtime against the longest test.

**In a Growth PM chain:** on a Go or Not sized — no data, continue without pausing (the user already chose to continue without data at the gate). On Re-scope or No-go, stop and ask once with the question tool: continue as scoped / re-scope ({the specific re-scope the table names}) / stop — recommended answer first. It changes everything downstream, so it's a real blocker, not an optional offer.

---

## Why a number is what it is — Researchio (optional)

A baseline says *what*. When the file needs the *why* — a segment converting at half the rest, a conversion drop after a date — and the Researchio plugin is installed (its skills `kramer-pull` and `data-breakdown` are available), hand the question to its pipeline instead of improvising a breakdown here: `kramer-pull` → `data-breakdown`, passing the Kramer `sessionId` so it starts from the same context. Reuse it; don't duplicate it.

Researchio writes its session to a monday board, so it's an external write: standalone, ask before starting it; inside a Growth PM chain, offer it once after the final artifact (chain mode rules). Link its Research Summary doc from the file's **Why** section when it exists. Without Researchio, the Segments table is the breakdown and the file says so in one line.

---

## Output format

Open with the header block from [templates/ARTIFACT_HEADER.md](../../templates/ARTIFACT_HEADER.md) (`skill: monetization-opportunity-sizing`), then:

```markdown
# Sizing: {surface name}

**Surface:** {type} · **Trigger:** {exact condition} · **Cohort:** {…} · **Tiers:** {…} · **Objective:** {metric}
**Data:** {live — {tool}, {date range}, run {YYYY-MM-DD} · session {sessionId} | not measured — Kramer not connected} · internal data, don't share outside monday
**Prices:** {brain name}, asked {YYYY-MM-DD} | unverified — monday-context.md, verified-against {date}

**Verdict:** {Go — test | Go — ship + holdout | Re-scope | No-go | Not sized — no data} — base case {ARR}/yr vs bar {ARR}/yr · runtime {W} weeks vs {max} weeks

## Inputs
| Input | Value | What it counts | Query | Source |
|---|---|---|---|---|
| Reach R | … | … | "…" | [Data — {model}, {range}, run {date}] |
| … every input in sizing-model.md → The query set, plus each price from BigBrain [Brain — {name}, {date}] |

## Model
| Case | Lift ℓ | From | Extra conversions / yr | ARR at stake / yr |
|---|---|---|---|---|
| Low | … | … | … | … |
| Base | … | … | … | … |
| High | … | … | … | … |

## Segments
| Segment (tier · billing · role) | Reach / yr | Conversion | Share of base-case ARR |

## Testability
| Baseline p₁ | Base lift δ | n per arm | Eligible / week | Runtime | Longest test | Reads? |

## Feeds
- **Journey:** reach split by tier and role → scenario frequencies
- **Spec + measurement plan:** p₁, weekly eligible, window N, MDE

## Why
{Researchio doc link, or "no breakdown beyond Segments — Researchio not installed"}

## Context drift
{each BigBrain answer that differs from monday-context.md, with both values — omit the section when none}

## Open items
| # | Owner | What's needed | Blocks |
```

Standalone, end with:
```
---
→ Next step: monetization-journey-map — map who hits the surface and every step around it, sized from this file
→ Prompt: "Map the journey for .monetization/{feature-slug}/ from 00-sizing.md"
```
Inside a Growth PM chain, omit it (chain mode rules in [monetization-growth-pm](../monetization-growth-pm/SKILL.md#chain-mode-rules)).

---

## Rules

- **Every number shows its source or its mark.** A Kramer question with its model, range and run date, a BigBrain answer with the brain's name and date, or a `[Not measured]` / `[Unverified — …]` mark. A number with none of these doesn't go in.
- **No estimates.** A missing input is marked `[Not measured]` in its cell, and nothing computed from it is filled in (Data gate).
- **Aggregates only.** Counts, shares and rates by segment. Never user-level rows, account names, emails or IDs.
- **Small segments.** Fewer than 50 accounts in the window → report "<50" and don't compute a rate from it.
- **No figures in the repo.** Results live only in `.monetization/`, never in this plugin's files, examples or commit messages.
- **Internal.** The file's header says so; no figure from it goes into external-facing copy without Data's sign-off.
- **Lift comes from monday's own history.** Past experiments and the ceiling segment — never a competitor's claimed lift.

## References

- Model, query set, lift cases, verdict table: [references/sizing-model.md](references/sizing-model.md)
- Query rules and tool mechanics (shared with the journey map): [../monetization-journey-map/references/evidence-queries.md](../monetization-journey-map/references/evidence-queries.md)
- Sample size and runtime: [../monetization-growth-pm/references/experiment-design.md](../monetization-growth-pm/references/experiment-design.md) §5
- monday facts and the BigBrain pointer model: [../../context/monday-context.md](../../context/monday-context.md)
