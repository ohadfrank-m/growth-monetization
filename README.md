# Growth Monetization Plugin

[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-000?style=flat-square)](https://claude.ai/code)
[![Cursor](https://img.shields.io/badge/Cursor-plugin-000?style=flat-square)](https://cursor.com/docs/plugins)
[![Skills](https://img.shields.io/badge/skills-7-333?style=flat-square)](#the-skills)
[![monday.com](https://img.shields.io/badge/built_for-monday.com-ff3366?style=flat-square)](https://monday.com)

A monetization copilot for growth product squads. Hand the **Monetization Growth PM** a surface and it does the full product work — asks for every missing input up front, sizes the opportunity on monday's own data (Kramer and the BigBrain AI Brains), then competitor research, a journey map of who hits the surface and every step around it, spec, conversion copy, wireframe, an independent CRO review that loops until the fixes land, and one requirements doc design and engineering can build from. Or call any single skill on its own when you only need one piece.

Built for: pricing pages · paywalls · promotions · upgrade flows · credit/consumption UI · trial flows · cancellation and downgrade flows

---

## How it works

![How the plugin works: the Monetization Growth PM checks Kramer and BigBrain are connected, sizes the opportunity, then runs research, journey map, spec, copy, wireframe with the journey board, review and requirements left to right, with a fix loop from review back to spec, copy and wireframe; every skill can also be called on its own](docs/flow.svg)

### Two ways to use it

| You want | Do this | What happens |
|----------|---------|--------------|
| **The full product work** — from an idea (or a live page) to an implementation-ready requirements doc | `/monetization-growth-pm` + describe the surface, or share a screenshot / Figma link | The Growth PM works out how far and how deep to go, asks for anything missing in at most two short rounds before it starts, runs every step without re-prompting, and delivers `05-requirements.md`. You can also stop it early: "spec and copy for…", "wireframe a…" |
| **One piece of the work** — you know exactly what you need | Call the skill directly: `/monetization-opportunity-sizing`, `/monetization-intelligence`, `/monetization-journey-map`, `/monetization-surface-spec`, `/improve-conversion-surfaces-copy`, `/monetization-design-reviewer` | Just that skill. It first checks it has what a top-tier output needs and asks for anything missing in one message (with the data question, when a data MCP is missing), then produces its artifact, ending with a `→ Next step` prompt if you want to keep going |

You never have to use the Growth PM, and you never have to use every skill. Every skill reads what's already in the feature folder and picks up from there.

### How the Growth PM scopes a run

When your prompt is clear about the deliverable ("wireframe a credit depletion surface for Pro"), it skips the scoping question. When it isn't, it asks one message with up to three pick-one questions:

| Question | Options |
|----------|---------|
| **How far should this go?** | New surface: spec + copy · up to a wireframe · all the way to a requirements doc. Existing surface: review + fixed copy + requirements · review only · start fresh · redesign all the way |
| **Start with a benchmark of how competitors run this surface?** | Yes / No — recommended for a new surface; the journey and the spec's flow map are then built from real competitor flows |
| **How thorough should the review be?** *(only when the chain reviews a wireframe it built)* | Standard *(recommended)* · Quick · Thorough — see below |

Then it makes sure every skill in the run has what it needs — surface, cohort, tier, role, trigger, objective metric, constraints, the current design. It infers what's obvious (and says from where) and asks the rest before anything is written: in the same message as the scoping question when it fits, otherwise in one follow-up — never more than two rounds. Mid-run, a skill that hits a gap stops and asks. No artifact ever carries an "Assumptions" section: what you answered goes in its header, and only facts nobody can answer yet (a legal policy, an unpublished price) stay open, each with an owner.

Before announcing a run that sizes, designs or reviews, it checks that monday's internal data is connected — Kramer for counts and baselines, BigBrain for plans, prices and credits. If either is missing, it names the MCP, says what it unlocks (the opportunity size, baselines, verified monday facts), points to [mcp-setup.md](mcp-setup.md), and asks once: **Connect now** (recommended) or **Continue without data**. Continue, and the whole run goes ahead — every number it couldn't measure is marked `[Not measured]` in place, never estimated, and each file opens with one line saying the data tools weren't connected. Research and copy don't need the data at all.

If the surface is live and public (e.g. monday.com/pricing), it captures the page itself instead of asking for a screenshot. On a new surface where research wasn't chosen, the announcement adds one line — `Say "add research" to benchmark competitors first` — so you can still add it without a question up front. A research-only ask ends at the research doc.

### The review loop, and how deep it goes

A review that only lists problems hands dev a wrong wireframe plus a to-do list. So for a new surface, the Growth PM sends every fixable finding back to the skill that owns it — copy lines to the copy skill, layout and states to the wireframe, a wrong trigger or missing state to the spec, a missing step or wrong path to the journey — and a **fresh reviewer that sees only the files** (not the reasoning that produced them) checks the fixes.

| Depth | What happens | Stops when |
|-------|--------------|-----------|
| **Quick** | One review, no loop, and no journey map. One copy pass writes the strings every finding needs; the rest go into the requirements doc as design changes on top of the v1 wireframe, and the fixed wireframe is offered at the end | After the review |
| **Standard** *(default)* | Critical and major findings loop back | Every fixable 🔴/🟠 finding is resolved and the re-review found no new 🔴/🟠 — max 2 passes. Polish (🟡) findings get one copy pass after the loop, then go into the doc |
| **Thorough** | Every fixable finding loops, polish included | Score ≥85/100 and every fixable finding resolved — max 3 passes, earlier if only human-blocked items remain |

Findings that need a human — a price, a policy, an engineering answer — never loop; they go into the requirements doc as Open items with an owner. In a live test, a credit-depletion surface went 67 → 85 → 91 over two Standard passes without a human in the loop.

If the environment can't run an independent reviewer (e.g. a chat session with no subagents), the Growth PM says so up front, labels every score **self-graded**, and never calls a self-graded score "ship it".

### Who does what

In the order they run:

| Skill | Responsible for | Produces | Never does |
|-------|----------------|----------|------------|
| `monetization-growth-pm` | The PM on the job: scopes how far and how deep, asks every missing input up front, checks the data is connected and the monday facts are current, runs every skill below in order, runs the fix loop, keeps the artifact ledger, and writes the final requirements | `05-requirements.md` | Write copy or score designs itself |
| `monetization-opportunity-sizing` | Whether it's worth building: reach × current conversion × addressable lift × ARPA → ARR at stake, low / base / high, every input a Kramer query or BigBrain price shown in the file; the baselines everything after it uses; testability and a go / no-go line | `00-sizing.md` | Guess a number — an unmeasured one is marked `[Not measured]` |
| `monetization-intelligence` | How competitors monetize and how they run each surface: surface benchmarks (e.g. five competitors' cancellation flows, screen by screen), full monetization teardowns, model benchmarks, landscapes, battlecards, change monitoring | `research/{topic}-{YYYY-MM}.md` | Spec or design anything |
| `monetization-journey-map` | Who hits the surface and why — scenarios per persona (IC and admin always a pair), sized with live data — and every step before, on and after it, with each step's state of mind; then a journey board showing the real wireframe on every step | `00-journey.md`, `03-journey.html` | Design screens or write copy — it names the steps and hands off |
| `monetization-surface-spec` | What to build: trigger, cohort, the screen-by-screen flow with its friction points, layout, edge cases — then the low-fi HTML wireframe of every state, and revisions of both when a review sends fixes back | `01-spec.md`, `03-wireframe.html` | Write final copy — it names the reason and hands off |
| `improve-conversion-surfaces-copy` | Every word the user reads: 2–3 options per element, one ★ recommended, grounded in a real reason people buy | `02-copy.md` | Layout, hierarchy, or scoring |
| `monetization-design-reviewer` | Scoring against an 8-dimension CRO rubric, a ranked fix list with a **Fix path** per row, and verifying fixes on re-review | `04-review.md` | Write the fix — it routes it to the skill that owns it |

Copy runs *before* the wireframe, not after the review — so the wireframe you look at, and the review that scores it, both reflect real language, never bracketed placeholder text.

---

## Installation

Claude Code and Cursor install the same repo as a plugin: skills load from `skills/`, and every skill reads [`plugin-rules.md`](plugin-rules.md) — the plugin-wide rules for intake, the Data gate and artifacts — at the start of its run. Neither host loads a root rules file on its own, so there's nothing to copy into your project's rules.

### Claude Code

```bash
/plugin marketplace add ohadfrank-m/growth-monetization
/plugin install growth-monetization@growth-monetization
```

Skills load automatically. Run `/growth-monetization:monetization-growth-pm` for the full flow (type `/growth-monetization` to see all seven), or just describe the job and the matching skill triggers.

Try it locally before installing: `claude --plugin-dir /path/to/growth-monetization`. Update: `/plugin update growth-monetization@growth-monetization`.

### Cursor

The repo carries a Cursor Plugin manifest (`.cursor-plugin/`), so it installs like any Cursor plugin. Pick one:

- **Team marketplace** (Teams and Enterprise — the way to roll it out to a squad). An admin opens Dashboard → Plugins & MCPs → Team Marketplaces → **Add Marketplace** → **Import from Repo**, pastes `https://github.com/ohadfrank-m/growth-monetization`, adds the plugin, and sets access and an installation mode (Default On or Default Off). Turn on **Auto Refresh** so pushes to `main` reach everyone. Each person then finds it under **Customize** in the sidebar.
- **Local** (one person, or trying a branch):

  ```bash
  git clone https://github.com/ohadfrank-m/growth-monetization ~/.cursor/plugins/local/growth-monetization
  ```

  Then run **Developer: Reload Window**. Clone into that folder directly: Cursor skips a symlink that points outside it. On Enterprise, local plugins are off unless an admin enables **Allow Local Plugin Imports** — use the team marketplace instead. Update with `git -C ~/.cursor/plugins/local/growth-monetization pull` and a reload.

Check it under **Customize → Skills** (all seven should be listed), then run `/monetization-growth-pm` in the agent chat. MCP servers for Cursor: [mcp-setup.md](mcp-setup.md#cursor-config-snippet).

### Check the install (either host)

Call `/monetization-opportunity-sizing` with a one-line brief. With Kramer and BigBrain not connected, it should ask its missing inputs and **Connect now / Continue without data** in one round, and write nothing before you answer. If it writes a file straight away or adds an "Assumptions" section, the skill isn't reading `plugin-rules.md` — reinstall or update.

### Claude.ai / Claude Desktop

Not a full install. A skill uploaded on its own loses what sits outside its folder — `plugin-rules.md`, `context/`, `playbooks/`, `templates/`. If you use one there, add `plugin-rules.md` and `context/monday-context.md` to the project knowledge next to it; the skill names any other file it can't find and says what that affects.

---

## MCP connections

### Strongly recommended — monday's internal data

Sizing, the journey map, spec success metrics, reviews of live surfaces and the requirements doc run on monday's own numbers. When one of these isn't connected, the run names it, says what it unlocks, links the setup, and asks once per run: connect now, or continue without data. Continuing, every unmeasured number is marked `[Not measured]` — never guessed — and nothing else is added (no analyst request, no list of pulls).

| MCP | What it's for | Without it | How to connect |
|-----|---------------|-----------|----------------|
| **Kramer** (monday's Snowflake data agent — `data-expert-agent`, `check-query-status`; `run-sql` for re-runs) | Counts, rates and baselines: how many accounts hit a trigger, how many convert today, conversion lag, past experiment lifts. Read-only, aggregates only, every question and source table shown in the artifact | Asked once to connect. Continuing, sizing reads **Not sized — no data**, and every count, rate and baseline is marked `[Not measured]` | monday internal — see [mcp-setup.md](mcp-setup.md#kramer-mcp-monday-internal) |
| **BigBrain AI Brains** (`AI Brain - Payments` and related) | Current plans, prices, AI credit packages, gating and trial terms, checked at run time. `context/monday-context.md` caches the last verified answers | Asked once to connect. Continuing, facts come from the context file marked `[Unverified]` with its `verified-against` date | monday internal — see [mcp-setup.md](mcp-setup.md#bigbrain-ai-brains-monday-internal) |

**Optional:** the **Researchio** plugin. When it's installed, sizing hands the "why" behind a baseline (a segment converting at half the rate of the rest) to its `kramer-pull` → `data-breakdown` pipeline instead of improvising one.

Research (`/monetization-intelligence`) and copy (`/improve-conversion-surfaces-copy`) make no claims about monday's numbers, so they run without these.

### Optional — higher-fidelity research and design input

| MCP | What it unlocks | Without it | How to connect |
|-----|-----------------|-----------|----------------|
| **monday.com** | `monetization-intelligence` can log its research to the Pricing Intelligence board on monday.com (it asks first), so competitive work compounds in one shared place instead of living in local files or Slack threads. Inside a Growth PM chain, logging is offered once at the end, never posted mid-run. | Every artifact is still written to `.monetization/` locally — you log it yourself if you want it on a board. | Add `https://mcp.monday.com/mcp` as a remote MCP server |
| **PricingSaaS** | Structured, current competitor pricing data — live plans, historical change diffs, watchlists, pricing-news feed. This is what makes `monetization-intelligence` fast and precise instead of a slow manual Google-and-guess exercise, and it's the only source with real historical diffs (before/after a pricing change, dated). | Falls back to enrichment-only research — Wayback Machine, changelogs, sentiment, job postings. Still usable, but slower and with no structured change history. | Add `https://mcp.pricingsaas.com` — see [mcp-setup.md](mcp-setup.md) |
| **Figma** | Pull a design directly from a Figma link or frame — layer structure, exact copy text (not read off pixels), and variable bindings, so `monetization-design-reviewer` can catch hardcoded colors/spacing that have drifted from Vibe design tokens and the wireframe can name real tokens instead of "token TBD". | Paste a screenshot instead — full visual review still works, you just lose token-binding checks and have to transcribe copy by eye instead of reading it exactly. | Add `https://mcp.figma.com/mcp` |
| **Slack** | The weekly pricing digest (`monetization-intelligence`) comes formatted as a paste-ready Slack message for the channel your team watches. | Digest is delivered in chat — same content, formatted for pasting. | See your Slack app's MCP setup |
| **Web search** | Enrichment sources for `monetization-intelligence` — Wayback Machine snapshots, product changelogs, earnings-call commentary, sentiment from Reddit/G2/HN. This is what grounds research in evidence beyond whatever PricingSaaS alone returns. | Research is limited to PricingSaaS/monday.com MCP data alone — meaningfully reduced coverage on anything PricingSaaS doesn't track. | Built into Claude Code; in Cursor, keep the agent's web search enabled |

Skills degrade gracefully when an optional MCP is unavailable and tell you what's affected — they never fail silently.

---

## The skills

Listed in the order the Growth PM runs them. Each one also works on its own.

### `/monetization-growth-pm` — the Monetization Growth PM

The full product work in one command. It scopes the job (how far, how deep), asks every missing input up front, checks Kramer and BigBrain are connected, sizes the opportunity, then runs research → journey map → spec → copy → wireframe → journey board → independent review → fix loop, and synthesizes everything into one doc a designer and engineer can start from without opening anything else. After every step it prints a one-line **ledger** of the current version of each artifact, so it's always clear which spec, copy, and wireframe are the latest — even in a chat session with no real files.

**What you get:** `05-requirements.md` — the **build target** (the approved wireframe version), the depth used and passes run, final copy strings (verbatim ★ picks, each next to the line it replaces), what the loop already fixed, remaining design changes, open items (including any suggested playbook updates from the research, so they land in `playbooks/`), a **measurement plan** (one revenue-proximate primary metric, guardrails that block ship, sample size and runtime from real baselines — or marked `[Not measured]` when the run continued without data — a pre-registered ship table — grounded in its `references/experiment-design.md`), and a sorted build order in which every journey scenario gets its own acceptance criterion. Every design change and build step carries **acceptance criteria** a tester can check, every owner is a named person or a role marked "name TBD", and vague words ("intuitive", "fast", "as needed") are quantified or cut. Every row traces back to the review row it came from, and the Growth PM re-checks the reviewer's factual claims before they go in.

In Claude Code the `/` menu namespaces skills by plugin (`/growth-monetization:monetization-growth-pm`); in Cursor they're listed under Customize → Skills and called by name (`/monetization-growth-pm`). This README uses the short names.

---

### `/monetization-opportunity-sizing` — Is it worth building?

Puts a number on the opportunity before anyone designs anything: how many accounts hit the moment, how many convert today, how much of the gap a better surface could close, and what each conversion is worth. **Runs first** in every Growth PM run that designs or reviews a surface, and again (`00-sizing-v2.md`) if research or a fix changes the trigger, cohort or objective it measured.

**Asks for, if your prompt doesn't say:** the surface and its exact trigger, cohort and tiers, the objective metric, the longest test the team will run, and the smallest ARR that would justify the build.

**Needs:** Kramer and BigBrain — without them it asks once to connect. If you continue, a direct call still writes the file, with every number marked `[Not measured]`; inside a Growth PM run it skips the file and puts a short population-and-prices block at the top of the journey (or spec), so the run doesn't carry an empty step. Optional: Researchio for the why behind a baseline.

**What you get:** `00-sizing.md` — reach × current conversion × addressable lift × ARPA → **ARR at stake per year**, in low / base / high cases. Lift comes from monday's own history (past experiments on the same surface type, the gap to the best-converting comparable segment), never a competitor's claim. Every input is a Kramer query or a BigBrain price shown in the file, segmented by tier, billing period and role. Then testability — sample size and runtime for the base-case lift — and one **go / no-go** line: Go — test · Go — ship + holdout · Re-scope · No-go. Its baselines feed the journey's scenario frequencies and the measurement plan in `05-requirements.md`. The file is internal and never leaves `.monetization/`.

---

### `/monetization-intelligence` — How competitors monetize

Not just what competitors charge — how they make money and how they run the surfaces where they ask for it. It covers the whole system (value metric, packaging and tiers, price points and discounting, free/trial model, expansion paths) and benchmarks any specific surface screen by screen — so a spec for an upgrade or cancellation flow starts from how five competitors actually run theirs.

**Asks for, if your prompt doesn't say:** the company or category, the surface type (for a surface benchmark), the monday.com decision the research should inform, the competitor set, quick scan vs deep dive, and whether it may spend PricingSaaS credits.

**Works best with:** PricingSaaS MCP + web search (falls back to web-only enrichment)

| What you ask | What you get |
|-------------|-------------|
| "How do Notion, ClickUp and Asana handle cancellation?" | **Surface benchmark** — each competitor's flow screen by screen (entry, offer, escape, what happens after, win-back and seat-expansion mechanics), patterns to steal and avoid, flow implications for the journey and spec, and what it means for monday.com |
| "Tear down Notion's monetization" | **Monetization teardown** — value metric, packaging, price, free/trial model, expansion paths, where self-serve stops and sales starts, a map of every surface where they charge, and a layer-by-layer comparison with monday.com |
| "How does Notion price?" | Company deep-dive — plans, packaging logic, history, what it means for monday.com |
| "How do AI companies sell credits?" | Model benchmark — credit unit names, package sizes, rollover policies, top-up UX across the category |
| "Map the work management pricing landscape" | Landscape report in `research/` — all players, price bands, model patterns, market-level signals. A hosted HTML version only on your go-ahead (PricingSaaS charges credits for it and the link is public) |
| "What changed in pricing this week?" | Weekly digest — watchlist changes, key moves, signal vs. noise |
| "Tear down Asana's pricing page" | Page teardown — hierarchy, copy psychology, what works and what doesn't |
| "Build a battlecard: monday vs Asana" | Battlecard — plan comparison, objection handling, negotiation intelligence |

Every claim about a competitor's product is evidence-tagged — `[Verified]` from vendor docs or a capture, `[Reported]` from third parties, `[Teardown needed]` when a screen sits behind a login and couldn't be seen (it never describes a screen it hasn't seen). Surface findings end with **suggested playbook updates**, so what's learned moves into the shared `playbooks/` instead of staying in one report.

After a company research or monetization teardown it offers a battlecard. It offers to log each output to the **Pricing Intelligence** board on monday.com — right after a standalone run, or once at the end of a Growth PM chain. Nothing posts without your go-ahead.

---

### `/monetization-journey-map` — Scenarios and journey

Maps the story around a surface before anyone designs it: who hits it, why, and how often, and every step they take — including the ones off the surface, like the admin request, the confirmation email, the invoice and the renewal. **Runs twice**: once before the spec, and again after the wireframe to build the board.

**Asks for, if your prompt doesn't say:** the surface type, the cohorts and tiers in scope, and whether the surface is new or live (a live one is mapped as it is today, from screenshots).

**What you get:**

- `00-journey.md` — scenario cards (problem, persona, trigger, frequency, current result, evidence, impact — adapted from Pragmatic Institute use scenarios), sized with read-only Kramer queries to monday's data, split from `00-sizing.md` (every question and source shown; it marks a frequency `[Not measured]` rather than guess when data isn't available), and a step table across five stages (before → trigger → on-surface → hand-off → after) with each step's channel, state of mind, branches, friction, event and wireframe state id. The spec takes its flow map from it, copy writes to each step, and the reviewer walks every scenario through the design
- `03-journey.html` — the journey board: one lane per scenario, one column per step, the real wireframe state embedded on every in-app step and the real copy on every email or notification card, viewable per scenario by URL hash

---

### `/monetization-surface-spec` — Spec and wireframe

A complete spec and a low-fi HTML wireframe for any monetization surface, from a brief, a Figma link, or a screenshot. **Runs twice per surface** — once for the spec, again after copy exists to build the wireframe around it — and again in revision mode when a review sends fixes back.

**Asks for, if your prompt doesn't say:** surface type, trigger, cohort (new vs existing), tier, the one conversion objective, whether a design already exists — and whether to pull 3 best-in-class examples first.

| # | Surface | Triggered when |
|---|---------|---------------|
| 1 | Pricing page | Plan comparison — public or in-app |
| 2 | Paywall / feature gate | User tries to access a locked feature |
| 3 | Promotion | Discount, limited-time offer, upsell |
| 4 | Tier upgrade trigger | Usage limit hit, seat expansion |
| 5 | Credit / consumption UI | Running low, credit meter, top-up flow |
| 6 | Cancellation flow | User initiates cancel or downgrade |
| 7 | Trial flow | Trial start, mid-trial nudge, expiry |

**What you get:**

- `01-spec.md` — trigger, cohort, the scenarios from the journey map (when one exists), a **flow map** (every screen in the journey, where users arrive from and go next, and the friction point at each touchpoint with its fix — taken from `00-journey.md` when it exists), a **trigger-logic block** (conditions, frequency cap, dismiss and re-show rules, with thresholds cited from the surface's playbook), a pattern decision table, section-by-section layout, copy strategy (the reason and direction — never final copy), success metrics, and every edge case (credit debt, admin-gated purchase, mobile, repeat exposure, enterprise, loading/empty/error states)
- `03-wireframe.html` — one self-contained file built to a fixed **wireframe contract**: every state in a state switcher (and reachable by URL hash, so each can be rendered for review), the real ★ copy, for multi-screen surfaces a left-to-right **flow strip** with a `T{n}` pin on every friction point, pins that tie elements to spec sections and review rows (dashed when blocked on an open item), an annotation panel, neutral colors named for their Vibe token, and a true-375px mobile layout
- `01-spec-v2.md` / `03-wireframe-v2.html` — fix-loop revisions: only the rows the review sent back, each change pinned with its row number
- A wireframe of the fixed version after an existing-design review — built from `05-requirements.md`, with each element pinned to its final-copy, design-change or open-item code

---

### `/improve-conversion-surfaces-copy` — Conversion copy

Every line maps to a real reason people buy, not a feature description. The deliverable is always the same shape: for each element, 2–3 options that differ by angle, one marked **★ Recommended** with a one-line why.

**Asks for, if your prompt doesn't say:** the surface and element(s), the cohort / journey stage, the action the copy must drive, the current copy (when rewriting), and hard constraints — length, and facts that must stay true.

Every option is written to the evidence-backed rules in its `references/copy-craft.md` (CTA labels, numbers and prices, loss vs gain framing, urgency, error states, mobile — each rule sourced to NN/g, Baymard or the original study) and monday's own voice from the Vibe UX Writing Handbook, then checked against `references/copy-guardrails.md` — the language it never writes (confirmshaming, fake urgency, drip pricing, hidden renewal terms, trick wording), grounded in the FTC dark-patterns report, ROSCA, the California ARL, the UK DMCC Act and EU consumer law. A breaching option is rewritten, never shipped with a flag. With a journey map, each element is labelled with its step and written to that step's state of mind, and off-surface steps (the confirmation email, the admin notification) get copy too.

**What you get:**

- `02-copy.md` — the first pass right after the spec (the wireframe is built from these), or a standalone rewrite when you call the skill directly. Real, ship-ready lines either way
- `02-copy-v2.md`, `-v3` — targeted revisions when a review flags lines (inside the fix loop, or once afterwards for polish rows) — never a fresh draft

---

### `/monetization-design-reviewer` — CRO design review

Scores any monetization design, screenshot, Figma frame, live URL, or wireframe against an 8-dimension CRO rubric (value clarity, timing, copy, friction, trust, escape hatch, hierarchy, mobile), weighted by surface type.

**Asks for, if your prompt doesn't say:** the design itself, surface type, cohort, the goal or metric, single screen vs full flow, and whether you want the review only or the full fix-and-requirements chain.

**What you get:** `04-review.md` — weighted score out of 100, projected score if the Critical and Major fixes ship, a ship / don't-ship verdict, **what's working — keep** (so fixes don't break it), one ranked fix list where every row carries a **Fix path** (`copy`, `wireframe`, `spec`, `journey`, `design team`, or `blocked — {owner}`), **one alternative worth testing** (a different pattern for the same goal, with the A/B to run), and one benchmark example. When the spec has a flow map, friction is judged touchpoint by touchpoint. With a journey map, every scenario is walked through the design step by step (a cognitive walkthrough), and a scenario that can't reach its end state is a critical finding. Inside the Growth PM it runs as a fresh subagent so it isn't grading work it wrote; on re-review (`04-review-v2.md`) it verifies each fix and ends with `Exit loop` or `Another pass`. Called directly, it runs the same chain the Growth PM would — intake and the data check once, sizing, then the review, copy rewrites and `05-requirements.md` — unless you say "review only", in which case it scores, offers a low-fi prototype of the fixes, and stops.

Scores aren't intuition: every 5 has checkable criteria behind it (WCAG 2.2 AA target sizes and reflow, NN/g heuristics, Baymard findings, the FTC dark-patterns taxonomy, DSA Art. 25), each dimension maps to the playbooks' anti-pattern rows, and `references/calibration-examples.md` shows what a 1, 3 and 5 look like on real, cited surfaces — including a fully worked score of the FTC-documented Amazon cancel flow. A **dark-pattern gate** caps the verdict at "Not yet" whenever the escape hatch scores ≤2 or a starred criterion fails, so weighting can never average an obstructive flow into "ship after fixes". Every surface type, trial flows and downgrades included, has its own weight column.

---

## Your work persists

Every artifact lands in `.monetization/` in your working directory, numbered by artifact type:

```
.monetization/
├── credit-depletion-ic-pro/        ← new surface, full flow
│   ├── 00-sizing.md                ← ARR at stake, baselines, go / no-go (internal data)
│   ├── 00-journey.md               ← scenarios + every step; the spec's flow map comes from here
│   ├── 01-spec.md                  ← spec (names the reason, hands off)
│   ├── 02-copy.md                  ← copy — the wireframe is built from this
│   ├── 03-wireframe.html           ← wireframe, every state
│   ├── 03-journey.html             ← journey board: each scenario's path, real wireframe on every step
│   ├── 04-review.md                ← independent review, a Fix path on every row
│   ├── 01-spec-v2.md               ← fix loop: only the spec rows the review sent back
│   ├── 02-copy-v2.md, -v3          ← fix loop: only the copy rows sent back, per pass
│   ├── 03-wireframe-v2.html, -v3   ← fix loop: rebuilt; the last approved one is the build target
│   ├── 04-review-v2.md, -v3        ← re-reviews: verify each fix, exit or loop
│   ├── renders/                    ← every wireframe state and the journey board, desktop + true 375px, for the reviewer
│   └── 05-requirements.md          ← what design + eng build from
├── pricing-page/                   ← existing design (no fix loop — it's your live design)
│   ├── input/                      ← screenshots, or captures of the public page
│   ├── 00-sizing.md                ← the live surface's reach, conversion and ARR at stake
│   ├── 04-review.md
│   ├── 02-copy.md
│   ├── 05-requirements.md
│   └── 03-wireframe.html           ← optional: the fixed version, built from 05-requirements.md
└── research/
    ├── cancellation-benchmark-2026-09.md   ← surface benchmark: how competitors run it
    └── notion-monetization-2026-09.md      ← monetization teardown
```

Every file carries the same header block: plugin, skill, feature, cohort, date and status, plus what you confirmed at intake, what was inferred and from where, and where its monday numbers came from (or that they weren't measured). Returning to a feature later, a skill detects what's there and picks up from the next step. Iterations get a version suffix instead of overwriting.

---

## Key principles

**Artifacts over answers.** Every skill produces a real deliverable — a spec, a wireframe, a research report, a requirements doc — not a chat response.

**Full flow or one skill.** The Growth PM runs everything back to back with no re-prompting and ends in one requirements doc. Call a skill on its own and it does just that job, ending with a `→ Next step` prompt.

**Ask, never assume.** Before anything is written — by the Growth PM for the whole run, or by a skill called directly — every gap that would change the output is asked up front, in as few messages as possible (at most two in a full run), and nothing is asked that your prompt already covers. No artifact has an "Assumptions" section.

**Real data, or clearly marked.** Counts, rates and baselines come from Kramer queries shown in the file; prices and credits from BigBrain. Without them, the run pushes you once to connect, and if you continue, every unmeasured number says `[Not measured]` where it sits — never an estimate.

**Reviewed until right, by someone who didn't write it.** For a new surface, a fresh reviewer scores the work, fixes go back to the skill that owns them, and it re-checks at the depth you chose. Dev gets a wireframe that's already corrected, not a list of corrections.

**One source of truth for monday.com facts.** Plans, prices, AI credit packages, gating, and trial terms come from the BigBrain AI Brains, checked at run time. [`context/monday-context.md`](context/monday-context.md) caches the last verified answers with a `verified-against` date, and any mismatch is reported, never silently used.

**Copy is always handed off — and runs before the wireframe.** Only `/improve-conversion-surfaces-copy` writes final copy. The spec names the reason from the 15 reasons people buy; the copy skill writes the lines; the wireframe and the review both use those real lines.

**Scenarios before screens.** On a new surface the journey comes first: who hits it, how often (from real data), and every step before, on and after it. The spec, the copy and the review all read that one file, so an IC and an admin at the same screen get different lines and the reviewer checks both get through.

**Nothing degrades silently.** A missing optional MCP, a missing reference file, or no independent reviewer — the skill says what's affected and takes the best fallback. A missing data MCP gets one push to connect; continuing, nothing unmeasured is passed off as measured.

---

## Repo structure

```
growth-monetization/
├── .claude-plugin/                    ← Claude Code manifest + marketplace
├── .cursor-plugin/                    ← Cursor Plugin manifest + marketplace (same name and version)
├── .github/workflows/checks.yml       ← CI: runs both scripts below on every push and PR
├── plugin-rules.md                    ← plugin-wide rules every skill reads first: intake, data gate, tool names, chain mode, artifacts
├── HANDOFF.md                         ← design decisions and history for the next maintainer
├── docs/
│   └── flow.svg                       ← the "How it works" diagram
├── context/
│   └── monday-context.md              ← monday.com facts cache + pointer to BigBrain (owned, versioned)
├── playbooks/                         ← CRO knowledge, one file per surface type + cases.md — cited by spec + reviewer, never duplicated
├── scripts/
│   ├── check-plugin.py                ← manifests in sync, skill frontmatter, skill lists, links and anchors
│   └── lint-playbooks.py              ← playbook structure, benchmark rows, evidence tags, links and source dates
├── templates/                         ← artifact header + research and spec templates
├── skills/
│   ├── monetization-growth-pm/        ← the Growth PM: scoping, intake, data gate, chain, fix loop, synthesis (+ experiment-design reference)
│   ├── monetization-opportunity-sizing/ ← ARR at stake, baselines, go / no-go (+ sizing-model reference)
│   ├── monetization-intelligence/
│   ├── monetization-journey-map/      ← scenarios, journey steps, scenario sizing, journey board
│   ├── monetization-surface-spec/
│   ├── improve-conversion-surfaces-copy/
│   └── monetization-design-reviewer/
└── mcp-setup.md
```

## Contributing

- **Updating monday.com facts:** verify against BigBrain, edit `context/monday-context.md`, bump `last-updated` and `verified-against`, add a changelog row. Never commit a query result or an internal figure beyond what the context file already caches
- **Updating CRO best-practice knowledge** (a benchmark, a best-in-class example, an anti-pattern): edit the matching file in `playbooks/`. It's cited by both `monetization-surface-spec` and `monetization-design-reviewer` — never copy it into a skill's own `references/`. Tag every claim `[Verified]` / `[Reported]` / `[Teardown needed]` and date your sources, then run `python3 scripts/lint-playbooks.py` before committing. See [playbooks/README.md](playbooks/README.md).
- **Adding a playbook**: it isn't finished until it carries the mandatory AI-native reference set — Clay, Figma, ClickUp, and Claude teardowns in the standard shape, an at-a-glance comparison, a copy bank, and dated sources. See [playbooks/README.md](playbooks/README.md).
- **Changing a skill:** keep `SKILL.md` lean and self-sufficient (its minimum must work even without `references/`); put mechanics specific to that skill in its `references/`; put anything a second skill needs in `playbooks/`. Keep its **Required context** table current.
- **Adding a skill:** add a folder under `skills/`, open its `SKILL.md` with the "Read first" line pointing to `plugin-rules.md` (copy it from any skill), give it a Required context table, add it to the skills table and output-folder tree in `plugin-rules.md`, to the Growth PM's deliverables table in `skills/monetization-growth-pm/SKILL.md`, to `templates/ARTIFACT_HEADER.md`, to `docs/flow.svg`, and to this README (including the skills badge)
- **Before committing:** run `python3 scripts/check-plugin.py` and `python3 scripts/lint-playbooks.py` — CI runs both
- **Releasing:** bump the version in all four manifests (`.claude-plugin/` and `.cursor-plugin/`, plugin and marketplace) and in each changed skill's frontmatter; `check-plugin.py` fails when the manifests disagree

---

## Security

These files are instructions for local AI tools. Review skills before using them in sensitive contexts. Keep your API keys and MCP credentials on trusted machines.

---

## Built by monday.com Growth

Questions or contributions: open an issue or submit a PR.
