---
name: monetization-intelligence
description: Competitive monetization intelligence — how other companies make money and how they run every monetization surface, not just what they charge. Covers the whole system (value metric, packaging and tiers, price points, discounting, free/trial model, expansion paths, where the product asks for money) and benchmarks how competitors run a specific surface — upgrade flow, cancellation flow, paywall, trial, credit top-up, pricing page. Use when the user wants to "research how X prices", "how do competitors handle cancellation", "benchmark upgrade flows", "how does X's paywall work", "how do others run trial expiry", "monetization strategy of X", "how does X make money", "X's packaging", "competitive pricing landscape", "how do AI companies sell credits", "benchmark our pricing model", "monitor pricing changes", "tear down X's pricing page", "pricing battlecard for X", "what do customers think about X's pricing", "weekly pricing digest", "has X changed their free trial", "what do people actually pay for X", or "pricing intelligence". Works best with the PricingSaaS MCP and falls back to web-only enrichment without it. Standalone runs offer to log to the Pricing Intelligence board on monday.com.
version: 0.3.0
---

# Monetization Intelligence

How competitors make money — and how they run the surfaces where they ask for it. Price is one input; the job is the whole monetization system: the value metric, packaging and tiers, price points and discounting, the free/trial model, expansion paths, and every surface — pricing page, paywall, upgrade flow, trial, credit top-up, cancellation. A spec for a cancellation flow should be able to start from "here's how five competitors run theirs", not from a blank page.

Powered by the PricingSaaS MCP for plans and change history, public product documentation and captures for surfaces, and enrichment sources (Wayback, changelogs, community) for everything else.

## Routing

Identify intent and route to the correct reference file. When intent is ambiguous, put the routing question in the intake message (see Required context) rather than a separate round trip: "Are you researching a specific company, benchmarking how competitors run a surface (upgrade, cancellation, paywall, trial, top-up), mapping a market, benchmarking a pricing model, tracking changes, building a battlecard, or something else?"

| Intent | Trigger signals | Reference |
|--------|----------------|-----------|
| **Surface benchmark** | "how do competitors / X handle [cancellation, upgrade flow, paywall, trial, trial expiry, credit top-up, seat limit, downgrade]", "benchmark upgrade flows", "best-in-class [surface]", "how does X's paywall work" | [surface-benchmark.md](references/surface-benchmark.md) |
| **Monetization teardown** | "monetization strategy of X", "how does X make money", "X's packaging", "how does X expand accounts", "tear down X's monetization", "full teardown of X" | [monetization-teardown.md](references/monetization-teardown.md) |
| Single company pricing deep-dive | company name + "price", "plans", "tiers", "pricing history" | [company-research.md](references/company-research.md) |
| Category / industry landscape | "industry", "category", "landscape", "trends", "market", "who competes" | [trend-research.md](references/trend-research.md) |
| **Monetization model benchmarking** | "how do AI companies sell credits", "usage-based vs seat-based", "how should we structure our pricing model", "credit economics", "benchmark our model", "how do PLG tools charge for AI" | [monetization-model-benchmarking.md](references/monetization-model-benchmarking.md) |
| Track pricing changes | "monitor", "watchlist", "what changed", "pricing news", "updates" | [monitoring.md](references/monitoring.md) |
| Category watchlist setup | "track the {category} space", "add all {category} competitors", "set up watchlist" | [category-watchlist.md](references/category-watchlist.md) |
| Sentiment / market reaction | "what do people think", "sentiment", "customer reactions", "controversy" | [sentiment-research.md](references/sentiment-research.md) |
| Pricing page teardown | "tear down X's pricing page", "analyze pricing page", "pricing psychology", "how does X present pricing" — only when the pricing page is named | [pricing-page-teardown.md](references/pricing-page-teardown.md) |
| Competitive battlecard | "battlecard", "losing deals to X", "pricing objections", "vs X pricing" | [battlecard-generator.md](references/battlecard-generator.md) |
| Weekly digest | "weekly digest", "what changed this week", "pricing brief", "run my digest" | [weekly-digest.md](references/weekly-digest.md) |
| A/B test detection | "testing their pricing page", "A/B testing pricing", "pricing page experiments" | [ab-test-detection.md](references/ab-test-detection.md) |
| Freemium / trial tracker | "changed their free tier", "trial change", "free plan limits", "did X remove freemium" | [freemium-trial-tracker.md](references/freemium-trial-tracker.md) |
| Negotiation intelligence | "what do people actually pay", "typical discount", "how to negotiate X" | [negotiation-intelligence.md](references/negotiation-intelligence.md) |

Enrichment methods (Wayback Machine, changelog mining, earnings calls, job postings, sentiment) are embedded in the core workflows and called automatically when relevant. Full documentation: [enrichment.md](references/enrichment.md)

---

## Required context

Standalone runs follow the plugin's intake protocol ([CLAUDE.md](../../CLAUDE.md), "Intake — standalone runs"): check this table, infer what's obvious, ask every real gap in one message, then run. Inside a Growth PM chain, skip it.

| Field | Why it changes the output | Infer from |
|-------|--------------------------|-----------|
| Company or category | Decides the workflow and the companies pulled | Named in the prompt |
| Surface type (surface benchmark) | Decides what gets captured per competitor — offers and save paths for cancellation, preview and trial path for a paywall, packages for a top-up | "cancellation", "upgrade flow", "paywall"… — ask only if the prompt names none |
| The monday.com decision it informs | Shapes "So what for monday.com" — a pricing-page test, a paywall spec and a packaging change need different takeaways | "we're about to…", the surface or team mentioned |
| Competitor set (landscape / benchmark runs) | Who's in the table; the wrong set makes the benchmark useless | Category default: the **Work management** bundle in [category-watchlist.md](references/category-watchlist.md) + the prompt's names |
| Depth | Quick scan (current plans, 1 page) vs deep dive (history, enrichment, sentiment) | "quick", "overview" vs "deep dive", "full" |
| OK to spend PricingSaaS credits | Full history and diffs cost credits | Never inferred — ask whenever a paid call would help (standing rule) |

---

## Prerequisites: PricingSaaS MCP

**Claude / Claude Code:**
Add `https://mcp.pricingsaas.com` as a remote MCP server in your environment settings. Setup instructions: `https://pulse.pricingsaas.com/mcp` (sign-in required).

**Cursor:** Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "pricingsaas": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.pricingsaas.com"]
    }
  }
}
```

Verify connectivity before any workflow: `get_status()`. If it fails entirely (not just 0 credits), offer to run enrichment-only research using Wayback Machine and web sources — this covers most workflows without live MCP data.

---

## MCP tool reference

| Tool | Cost | Purpose |
|------|------|---------|
| `get_status()` | Free | Check account and connection status |
| `search_companies(query)` | Free | Find companies by name or keyword |
| `search_companies_advanced(filters)` | Free | Attribute-based discovery |
| `get_company_details(slug)` | Free | Full pricing breakdown |
| `get_company_history(slug, discovery_only=true)` | Free | Preview available history periods |
| `get_company_history(slug)` | **1 credit/diff** | Full pricing change history |
| `get_diff_highlight(slug, period, query)` | **1 credit** | Visual before/after screenshot |
| `add_to_watchlist(slugs=[...])` | Free | Add companies to monitoring |
| `remove_from_watchlist(slugs=[...])` | Free (unverified — MCP unreachable 2026-09-27) | Remove companies from monitoring |
| `get_watchlist()` | Free | List monitored companies |
| `get_pricing_news()` | Free | Recent changes across tracked companies |
| `fetch_diffs(scope, period, period_type)` | **2 credits** | Detailed change data |
| `search_pricing_knowledge(query)` | Free | Pricing strategy frameworks |
| `add_page(url)` | Free | Submit a pricing page for tracking |
| `upload_report(filename, file_path)` | **Credits on delivery (per PricingSaaS); publishes a public URL** | Hosted HTML report — only on the user's go-ahead (see trend-research Step 8) |

**Credit rule:** Always state cost and get explicit user confirmation before any paid tool call.

**Credit-zero fallback:** When `get_status()` returns 0 credits, do not skip history. Automatically run the credit-zero fallback in [enrichment.md](references/enrichment.md) — reconstruct from Wayback Machine, community posts, and changelogs. Label all reconstructed output clearly.

---

## Output standards

- Use the research artifact template: [../../templates/research-output.md](../../templates/research-output.md)
- Include header block on every artifact
- Lead with exec summary (3 bullets) — always the first thing after the header
- Every company name links on first mention — to `https://pricingsaas.com/companies/{slug}` (public profile) when the slug is confirmed through the MCP, otherwise to the source page actually used. Diff links use `https://pulse.pricingsaas.com/companies/{slug}/diffs/{period}` (login required). Never guess a slug. The old pattern with `/pulse/` after the main domain returns 404
- Every standalone artifact ends with a **→ Next step** block (omitted in a Growth PM chain)
- Every competitor research includes a **So what for monday.com** section: pricing headroom, positioning implication, experiment to consider, threat signal — and, for surface work, which pattern to adopt, adapt, or avoid on monday's version of the surface
- **Evidence tags on every claim about a competitor's product or UI**, per [playbooks/README.md](../../playbooks/README.md): `[Verified]` (vendor docs or a capture you made), `[Reported]` (third-party), `[Teardown needed]` (behind a login or not captured). Never describe a screen you haven't seen
- **Durable findings go to the playbooks, not just the report.** When research produces a benchmark, example, or anti-pattern for a surface type, end with **Suggested playbook updates**: the exact addition for `playbooks/{surface}.md`, tagged and sourced, checked against what's already there so nothing is duplicated
- Offer to log the output to monday.com once it's delivered — posting to a shared board needs the user's go-ahead: [monday-logging.md](references/monday-logging.md)

---

## monday.com context

When research involves monday.com or its competitors, read [context/monday-context.md](../../context/monday-context.md) for current plans and prices before writing the "So what for monday.com" section. Compare against the context file, not memory.

After every company research or monetization teardown, offer a pricing battlecard before closing.

---

## In a Growth PM chain

When `monetization-growth-pm` runs this skill as the first step of a chain, the Growth PM's [chain mode rules](../monetization-growth-pm/SKILL.md) apply. For this skill that means:

- Save the artifact to `.monetization/research/{topic-slug}-{YYYY-MM}.md` — the next skill reads it from there
- Omit the `→ Next step` block and skip the battlecard offer
- Don't log to monday.com mid-chain — posting to an external board needs the user's go-ahead. The Growth PM offers logging once, after the final artifact
- Paid PricingSaaS calls still need confirmation before running
