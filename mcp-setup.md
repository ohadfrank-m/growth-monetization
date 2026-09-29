# MCP setup

Two MCPs are **strongly recommended**: Kramer and BigBrain, monday's internal data. Sizing, the journey map, spec success metrics, reviews of live surfaces and the requirements doc check for them before writing anything. When either is missing, the run names it, says what it unlocks, links this page, and asks once: **Connect now** (recommended) or **Continue without data**. Continuing, every number it couldn't measure is marked `[Not measured]` (a fact it couldn't verify, `[Unverified]`) — never estimated. Research and copy run without them. Every other MCP is optional: a skill degrades gracefully without it and tells you what's affected.

| MCP | Required? | Used by |
|-----|----------|---------|
| Kramer (monday internal) | **Strongly recommended** | Growth PM, `monetization-opportunity-sizing`, `monetization-journey-map`, `monetization-surface-spec` (success metrics), `monetization-design-reviewer` (live surfaces), synthesis |
| BigBrain AI Brains (monday internal) | **Strongly recommended** | Growth PM (fact check), `monetization-opportunity-sizing` (prices), spec, reviewer, synthesis |
| Researchio plugin | Optional | `monetization-opportunity-sizing` — the why behind a baseline |
| monday.com | Recommended | `monetization-intelligence` — logging research to the Pricing Intelligence board (it asks first) |
| PricingSaaS | Recommended | `monetization-intelligence` |
| Figma | Optional | `monetization-surface-spec`, `monetization-design-reviewer` |
| Slack | Optional | `monetization-intelligence` weekly digest |
| Web search | Built in (needed for enrichment) | All skills — enrichment and surface benchmarks |

---

## monday.com

**URL:** `https://mcp.monday.com/mcp`

- **Claude.ai / Claude Desktop:** Settings → Connectors → add monday.com
- **Claude Code:** `claude mcp add --transport http monday https://mcp.monday.com/mcp`
- **Cursor:** add to `~/.cursor/mcp.json` (see snippet below)

Used to log research outputs to a **Pricing Intelligence** board — the skill offers after each output and logs on a yes (the board is created on first use; you'll be asked which workspace). Without it, artifacts are saved locally only.

---

## PricingSaaS

**URL:** `https://mcp.pricingsaas.com` · Account and API key: [pricingsaas.com](https://pricingsaas.com)

- **Claude.ai / Claude Desktop:** Settings → Connectors → add custom connector with the URL above
- **Claude Code:** `claude mcp add --transport http pricingsaas https://mcp.pricingsaas.com`
- **Cursor:** see snippet below

Some tools cost PricingSaaS credits. The skill always states the cost and waits for your confirmation. Without this MCP, `monetization-intelligence` runs in enrichment-only mode (Wayback Machine, changelogs, web, community sources).

**Verify:** ask Claude to run `get_status()` — it should return your account and credit balance.

---

## Figma

**URL:** `https://mcp.figma.com/mcp`

- **Claude.ai / Claude Desktop:** Settings → Connectors → add Figma
- **Claude Code:** `claude mcp add --transport http figma https://mcp.figma.com/mcp`

Used when you paste a Figma link into a spec or review. Without it, share a screenshot instead.

---

## Slack

**URL:** `https://mcp.slack.com/mcp`

Used only for the weekly pricing digest, which the skill formats as a paste-ready Slack message. Without it, the digest is delivered in chat.

---

## Kramer MCP (monday internal)

**Strongly recommended** — it's what turns sizing, baselines and scenario frequencies into real numbers. monday's Snowflake data agent. It exposes `data-expert-agent` (ask a business question in plain language; it picks the tables and curated metric definitions, runs the SQL and returns a sourced answer) and `check-query-status` (poll the returned job id). Some setups also expose `run-sql` for re-running SQL you already have. Tool names vary by environment — the skills find them by searching for `data-expert-agent` or `kramer` (e.g. `kramer-mcp-v1`).

- **Connect:** through monday's internal MCP setup — ask Data/BI for access. The Snowflake role is read-only.
- **What the plugin asks it:** aggregates only (counts, shares, rates by segment), never user-level rows. Every question, source table, date range and run date is written into the artifact.
- **Without it:** the run asks once — connect now, or continue without data. Continuing, every count, rate and baseline is marked `[Not measured]` and the file opens with one line saying the data tools weren't connected. A query that fails or times out is retried once, then marked `[Not measured — query failed]` — never estimated.

**Verify:** ask Claude to run `data-expert-agent` with "How many active paying accounts do we have?" — it should return a job id, then a sourced answer via `check-query-status`. The answer stays in your session; don't paste it into the repo.

---

## BigBrain AI Brains (monday internal)

**Strongly recommended** for any run that states a monday price, limit, credit amount, gate or trial term. monday's internal question-answering brains: `AI Brain - Payments` owns plans, prices, AI credits and billing; related `AI Brain - …` MCPs cover other product and monetization knowledge. The skills find them by searching for `AI Brain`, `ai-brain` or `bigbrain`.

- **Connect:** through monday's internal MCP setup (the AI Brain MCPs listed in your org's MCP catalog).
- **What the plugin asks it:** each fact an artifact cites, at run time. [context/monday-context.md](context/monday-context.md) is the cache: when a brain's answer differs from it, the artifact uses the brain's answer, lists both, and tells you — never silently.
- **Without it:** the run asks once — connect now, or continue without data. Continuing, facts are cited from the context file marked `[Unverified — monday-context.md, verified-against {date}]`. Copy and research called on their own cite the context file with its `verified-against` date; inside a Growth PM run they use the run's BigBrain answers.

**Verify:** ask Claude to ask `AI Brain - Payments` "What is the current annual list price per seat of the Pro plan?" — it should return a sourced answer. Compare it with the Tier structure table in the context file.

---

## Researchio plugin (optional)

A separate plugin whose research pipeline runs on Kramer. When its skills `kramer-pull` and `data-breakdown` are available, `monetization-opportunity-sizing` hands it the *why* behind a baseline (a segment converting at half the rate of the rest) instead of improvising a breakdown. Researchio writes its session to a monday board, so the plugin asks before starting it (or offers it at the end of a Growth PM run). Without it, the sizing file's Segments table is the breakdown.

---

## Web search

Built into Claude.ai, Claude Desktop, and Claude Code. In Cursor, make sure web search is enabled for the agent.

---

## Cursor config snippet

```json
{
  "mcpServers": {
    "monday": { "url": "https://mcp.monday.com/mcp" },
    "pricingsaas": { "command": "npx", "args": ["-y", "mcp-remote", "https://mcp.pricingsaas.com"] },
    "figma": { "url": "https://mcp.figma.com/mcp" }
  }
}
```
