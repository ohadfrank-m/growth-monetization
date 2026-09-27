# Trend research workflow

Map the pricing landscape of a SaaS category or industry: who's in the space, how they price, what models dominate, and where the market is moving.

## Step 1: Discover companies in the space

**If given a category or industry**, run 2–3 keyword variations in parallel to maximize coverage (goal: 10–30 companies):

```
search_companies(query="{primary category term}")
search_companies(query="{alternate phrasing}")
search_companies(query="{industry + 'software' or 'platform'}")
```

Then use attribute filters to catch what text search missed:

```
search_companies_advanced(
  has_license=true,
  price_min={estimated floor},
  price_max={estimated ceiling}
)
```

**If given a seed company** ("who competes with X"):

```
get_company_details(slug="{seed slug}")  # extract category, price range, attributes
```

Then find peers using extracted attributes:

```
search_companies(query="{seed's product description keywords}")
search_companies_advanced(
  has_freemium={match seed},
  price_min={seed price * 0.3},
  price_max={seed price * 5}
)
```

Deduplicate all results across searches.

## Step 2: Pull pricing details

Fetch details for all discovered companies in batches of 5–6 (run in parallel):

```
get_company_details(slug="{slug}")  # repeat for each company
```

From each response, extract:
- Plan names and prices (monthly + annual)
- Pricing metric (per user, per seat, flat, usage-based)
- Freemium / trial availability
- Add-ons
- Employee count
- logo_url

## Step 3: Pull recent market moves

```
get_pricing_news()
```

Filter results to companies in this category. Note any that changed pricing recently — this is signal for where the market is heading.

## Step 4: Pull strategy frameworks (optional but recommended)

```
search_pricing_knowledge(query="{category} pricing strategy")
search_pricing_knowledge(query="{category} packaging best practices")
```

Run in parallel. Use findings to contextualize patterns in step 5.

## Step 5: Enrich with supplementary sources

Run these in parallel with Step 4 to add depth. See [enrichment.md](enrichment.md) for full instructions.

### Wayback Machine — detect legacy pricing patterns

For the 3–5 most relevant companies in the landscape, pull Wayback Machine snapshots to see how their pricing page has evolved over the past 12–24 months.

Follow [enrichment.md](enrichment.md) Method 1 (Wayback). WebFetch can't reach `web.archive.org`: use the Availability API through WebFetch, and CDX or snapshot fetches through Bash `curl`, at most ~1 request per second.

Use the earliest and latest snapshots to characterize the trajectory (e.g., "moved from flat to per-seat", "added enterprise tier", "removed freemium").

### Job postings as leading indicator

For any company that appears to be in transition (recent price changes, new plan structures), check for open monetization/pricing roles:

```
WebSearch(query='"{Company}" pricing OR monetization OR "revenue operations" job 2026')
```

Cluster findings: companies actively hiring for pricing roles are likely to restructure soon — note this as a forward-looking signal in the report.

### Cross-company pattern synthesis

After collecting data, use `search_pricing_knowledge` to benchmark detected patterns against established frameworks:

```
search_pricing_knowledge(query="{dominant model in this category} pricing")
search_pricing_knowledge(query="{unusual pattern observed} SaaS pricing")
```

Then look for market-wide signals in PricingSaaS:

```
get_pricing_news()  # already called in Step 3 — filter to companies in this category
```

Flag any cluster of companies making the same type of move in the same quarter as a market-level signal (e.g., "5 of 12 companies added usage-based components since Q3 2025").

## Step 6: Fill coverage gaps

After pulling details, identify well-known competitors not found in PricingSaaS. For each:

```
# Search for their pricing page
WebSearch(query="{Company Name} pricing page URL")

# If a public pricing page exists, submit it
add_page(url="{pricing page URL}")
```

Run web searches in parallel (batches of 4–6). Note submitted companies in the report — their data will be available in ~15 minutes. Skip companies with no public pricing page (enterprise "contact us" only).

## Step 7: Structure the landscape

Group companies by market layer — use price bands, feature depth, and employee count as signals:

**Tier examples:**
- SMB / self-serve: typically lower price points, self-service signup, per-seat or flat
- Mid-market: broader feature sets, higher per-seat prices, often hybrid PLG+SLG
- Enterprise: custom pricing or high-end tiers, SSO/security features, annual contracts

**Identify pricing model patterns:**
- What model dominates? (per user, flat, usage-based)
- Who is an outlier and why?
- Where do prices cluster? (e.g., $10–20/user, $50–100/user, $200+ enterprise)
- Who has freemium in a mostly paid market, or vice versa?
- Who is moving to AI-based pricing or usage-based in a per-seat market?

## Step 8: Write the landscape report

**Default output — markdown, always.** Write the report to `.monetization/research/{category-slug}-landscape-{YYYY-MM}.md` using [../../../templates/research-output.md](../../../templates/research-output.md) and the structure below. This is the deliverable; the next skill reads it from there.

**Optional HTML (only on the user's go-ahead).** PricingSaaS hosts a branded template (`https://share.pricingsaas.com/templates/pulse-market-scan-v1.html`, `{{TOKEN}}` placeholders). `upload_report` publishes the filled file to a **public** `share.pricingsaas.com` URL, and PricingSaaS says credits are consumed on report delivery. So before calling it, state the credit cost, say the link will be public, and wait for a yes (CLAUDE.md standing rules). Otherwise skip the HTML. **If the template fetch fails** (the old `raw.githubusercontent.com/pricingsaas/pricingsaas-claude-skills/...` URL has returned 404 since at least 2026-09-27), **use the inline structure below and deliver markdown only.** Never block the workflow on the template.

### Inline report structure (use when the template is unavailable, or by default)

1. **Header block** — [templates/ARTIFACT_HEADER.md](../../../templates/ARTIFACT_HEADER.md)
2. **Exec summary** — 3 bullets: what we found · what it signals · recommended action for monday.com
3. **Stats line** — `{N} companies · {M} pricing models · entry paid ${min}–${max}/seat/mo · {K} with freemium · {J} with a free trial`
4. **Market layers** — one table per layer (SMB self-serve · mid-market · enterprise):
   `Company · Entry paid plan · Monthly · Annual · Value metric · Free/trial · Self-serve ceiling · Source (tag, URL, checked)`
5. **Pricing patterns** — 3–5 findings, each: pattern · which companies · evidence tag · why it matters
6. **Price comparison** — table sorted by entry paid price, annual per seat per month. Bar chart only in the optional HTML
7. **Recent market moves** — from `get_pricing_news()` + changelogs, dated, one line each
8. **Forward-looking signals** — hiring (enrichment Method 2), filings and earnings calls (Method 4), Wayback trajectory (Method 1)
9. **So what for monday.com** — pricing headroom · positioning · experiment · threat signal, against [context/monday-context.md](../../../context/monday-context.md)
10. **Coverage and sources** — each company: data from PricingSaaS / vendor page / third party, with URL and checked date; companies submitted via `add_page` listed as "pending"

## Step 9: Deliver conversational summary

Structure the response as:

```
**{Category} pricing landscape**
Full report: `.monetization/research/{category-slug}-landscape-{YYYY-MM}.md` {+ the share URL only if the user approved the HTML upload}

---

{Category overview — how many companies, how the landscape breaks down}

**Market layers**
{For each tier: companies, price range, dominant model}

**Key patterns**
- {Pattern 1}
- {Pattern 2}
- {Pattern 3}

**Recent market moves** (from get_pricing_news)
{Any notable changes in this category}

**Forward-looking signals**
{Job postings analysis: which companies are hiring for pricing/monetization roles and what it suggests}
{Wayback Machine findings: any notable trajectory observations from historical snapshots}

---

Full report: `.monetization/research/{category-slug}-landscape-{YYYY-MM}.md` {+ the share URL only if the user approved the HTML upload}
```

Include `https://pricingsaas.com/companies/{slug}` links for every company named in the summary.

After delivering the summary, offer once:
> "Want me to check what customers are saying about pricing in this space — Reddit, G2, HN sentiment across the top players?"

If yes, run [sentiment-research.md](sentiment-research.md) for the top 3–5 most significant companies in the landscape.

## Step 10: Log to monday

After delivering the output, offer once to log it to the Pricing Intelligence board, and log on a yes, per [monday-logging.md](monday-logging.md). Skip inside a Growth PM chain. For landscape scans, create one item representing the scan (not one per company).

- Item name: `{Category} — Landscape`
- Change Type: `Landscape Scan`
- Summary: 1–2 sentences on the dominant pricing model and key market pattern
- PricingSaaS link: leave blank (landscape scans have no single company diff URL)
- Workflow: `trend-research`

## Step 11: Recommend next steps

After the summary, offer 3 tailored follow-ups using specific company names and findings:

1. **Company deep-dive** — "Want a full breakdown of how {top competitor} structures their pricing? I can pull their plan details, packaging logic, history, and Wayback Machine page evolution."
2. **Monitor the market** — "Want to track when any of these {N} companies changes pricing? I can add them all to your watchlist now."
3. **Sentiment sweep** — "Want to check what customers and operators are saying about pricing in this space across Reddit, G2, and HN?"
