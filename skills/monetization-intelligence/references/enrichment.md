# Enrichment methods

Supplementary research techniques that add context beyond PricingSaaS data. Call these from any workflow to deepen the analysis. All methods use `WebSearch`, `WebFetch` or Bash `curl` — zero credit cost.

**WebFetch failure handling:** If any `WebFetch` call fails (timeout, domain blocked, 4xx/5xx), skip that source silently and continue with the remaining sources. Never block or stall a workflow on a single failed fetch. Document which sources returned useful data in the output.

---

## 1. Wayback Machine — pricing page history

Use when: you need to see how a company's pricing page looked at a specific point in time, or want to reconstruct changes that predate PricingSaaS tracking.

**Access, as tested 2026-09-27 in Claude Code:**

| Endpoint | Via WebFetch | Via Bash `curl` | Use for |
|---|---|---|---|
| `https://archive.org/wayback/available?url={domain}/pricing&timestamp={YYYYMMDD}` | Works | Works | Nearest snapshot to a date. Can return `{}` even when captures exist — never read an empty result as "no history" |
| `https://web.archive.org/cdx/search/cdx?url={domain}/pricing&output=json&fl=timestamp,statuscode&filter=statuscode:200&from={YYYY}&limit=50` | **Blocked** (WebFetch refuses web.archive.org) | Works; rate-limited (HTTP 429 after a burst) | Listing every capture in a window; frequency analysis |
| `https://web.archive.org/web/{timestamp}/{domain}/pricing` | **Blocked** | Works | Reading a snapshot |
| `archive.ph` / `archive.today` | **Blocked** | Timed out | Not usable here — skip |

Rules:
- Pace curl calls ~1 per second, and send a browser User-Agent. On a 429, wait and retry once, then skip.
- Strip scripts and tags from a fetched snapshot before diffing, and diff plan names, `$` values, feature bullets and CTAs.
- In environments without Bash (claude.ai chat), only the Availability API is reachable. Report Wayback coverage as partial.
- No Google Cache fallback: Google retired the `cache:` operator in 2024 ([Search Engine Journal](https://www.searchenginejournal.com/google-removes-cache-search-operator-documentation/528022/), checked 2026-09-27). If Wayback has nothing, fall back to PricingSaaS diff text + the live page + community posts (Method 6 Source 3).

```bash
# List 2026 captures (curl, not WebFetch)
curl -s -A "Mozilla/5.0" "https://web.archive.org/cdx/search/cdx?url={domain}/pricing&output=json&fl=timestamp,statuscode&filter=statuscode:200&from=2026&collapse=timestamp:8"
# Read one capture
curl -s -A "Mozilla/5.0" "https://web.archive.org/web/{timestamp}/https://{domain}/pricing" -o /tmp/{slug}-{timestamp}.html
```

### Compare two snapshots

Fetch both timestamps, then diff the text content to identify:
- Plan names that appeared or disappeared
- Price values that changed
- Feature descriptions that were rewritten
- CTAs or trial offers that changed

### Output format

```
## {Company} — pricing page history ({date range})

### Snapshot: {Date A}
{Key pricing elements: plans, prices, notable features/CTAs}

### Snapshot: {Date B}
{Key pricing elements}

### What changed
- {Specific element}: {before} → {after}
- {Specific element}: {before} → {after}

[View snapshot A on Wayback Machine]({url_A})
[View snapshot B on Wayback Machine]({url_B})
```

---

## 2. Job postings as leading indicator

Use when: monitoring a company for signals of upcoming pricing changes, or trying to understand their monetization direction.

### What to look for

Heuristic (unsourced — directional only): companies often hire for pricing-related roles a few months (roughly 3–6) before major pricing changes. Treat it as a reason to look closer, never as a prediction. Key signals:

| Job title | What it signals |
|-----------|----------------|
| Pricing Analyst / Manager | Pricing review underway |
| Head of Monetization | Revenue model rethink |
| Revenue Operations | GTM motion shift, often tied to pricing |
| Growth PM / Monetization PM | PLG pricing experiment incoming |
| Enterprise Sales | Moving upmarket → pricing tier expansion |

### Search queries

```
WebSearch(query='"{Company}" "pricing" OR "monetization" job posting 2025 OR 2026')
WebSearch(query='site:linkedin.com/jobs "{Company}" pricing OR monetization OR "revenue operations"')
WebSearch(query='site:greenhouse.io OR site:lever.co OR site:ashbyhq.com "{Company}" pricing')
```

### Public job-board APIs (no login, JSON)

Faster and more complete than LinkedIn search. Try the company's slug on each; a 404 means they don't use that ATS.

```
WebFetch(url="https://boards-api.greenhouse.io/v1/boards/{slug}/jobs")        # asana, smartsheet, wrike, figma, airtable
WebFetch(url="https://api.ashbyhq.com/posting-api/job-board/{slug}")         # notion, clickup
WebFetch(url="https://api.lever.co/v0/postings/{slug}?mode=json")
```

Filter titles for `pricing|monetiz|packaging|billing|growth PM|revenue strategy`, then **triage by hand**. Keyword hits are noisy: on 2026-09-27 Asana's board matched "Head of Technical Revenue Accounting" and "Senior Global Billings Lead", which are finance roles, not pricing ones. Atlassian and HubSpot boards weren't found on these APIs; use their careers sites or search.

Caveats: a posting signals intent, not a decision. Postings get reposted and backfilled, so record the posting date and treat one role as weak signal, a cluster as a signal. LinkedIn job pages are login-walled for fetching; use `site:linkedin.com/jobs` search results only, tagged `[Reported]`.

### Output

Note the role, posting date, and what it signals about timing and direction. A cluster of monetization/RevOps hires in Q4 2025 at a company that then restructured pricing in Q1 2026 is a pattern worth documenting.

---

## 3. Product changelog mining

Use when: tracking packaging changes that haven't yet appeared on the pricing page. Changelogs often announce new features being added to specific tiers before the pricing page is updated.

### How to find changelogs

```
WebSearch(query='"{Company}" changelog OR "what\'s new" OR "release notes" 2026')
WebFetch(url="{company changelog URL}")
```

Known changelog URLs (checked 2026-09-27; 200 unless noted):

| Company | URL |
|---|---|
| Notion | https://www.notion.com/releases |
| Asana | https://asana.com/whats-new |
| ClickUp | https://feedback.clickup.com/changelog (`clickup.com/changelog` returns 403) |
| Airtable | https://www.airtable.com/whatsnew (`/whats-new` returns 404) |
| Atlassian | https://confluence.atlassian.com/cloud/blog |
| Smartsheet | https://www.smartsheet.com/content-center/product-news/release-notes |
| Figma | https://www.figma.com/release-notes/ |
| HubSpot | https://www.hubspot.com/new |
| Linear | https://linear.app/changelog |

For anyone else, try `{domain}/changelog`, `/releases`, `/whats-new`, `changelog.{domain}`, `feedback.{domain}/changelog`, then search. A vendor changelog is `[Verified]` for what it announces and when; it isn't evidence that the pricing page has changed.

Fetch the changelog and scan for:
- Feature gating language ("now available on Business and above")
- New add-ons or limits
- Trial or freemium changes
- Deprecations that might indicate packaging consolidation

### Output

List changelog entries relevant to pricing/packaging with dates and a note on whether the pricing page has been updated to reflect it yet (if not, that's a gap worth flagging).

---

## 4. Earnings call and investor report mining

Use when: researching a public company's pricing strategy rationale or anticipating future changes.

Public companies (HubSpot, Salesforce, Docusign, etc.) disclose pricing strategy in earnings calls and annual reports. This is the highest-quality signal for *why* changes happened and *what's coming*.

### Public competitors and where their disclosures live

| Company | Ticker | SEC CIK | Annual / quarterly forms | IR site |
|---|---|---|---|---|
| Asana | ASAN | 0001477720 | 10-K / 10-Q | https://investors.asana.com (403 to fetchers) |
| Atlassian | TEAM | 0001650372 | 10-K / 10-Q (US domestic filer) | https://investors.atlassian.com |
| HubSpot | HUBS | 0001404655 | 10-K / 10-Q | https://ir.hubspot.com (403 to fetchers) |
| Freshworks | FRSH | 0001544522 | 10-K / 10-Q | https://ir.freshworks.com |
| Salesforce | CRM | 0001108524 | 10-K / 10-Q | https://investor.salesforce.com |
| monday.com (self-reference) | MNDY | 0001845338 | **20-F / 6-K** (foreign private issuer — no 10-K/10-Q) | https://ir.monday.com |

CIKs and form types verified against `data.sec.gov/submissions` on 2026-09-27. **Smartsheet** has been private since 22 Jan 2025 (Blackstone/Vista), so it has no new filings or earnings calls ([Vista](https://www.vistaequitypartners.com/news/blackstone-and-vista-equity-partners-complete-acquisition-of-smartsheet/)). ClickUp, Notion, Airtable, Wrike and Canva are private.

### How to pull them

```
# Filing index (works in WebFetch)
WebFetch(url="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={CIK}&type=10-K&count=10")
# Full-text search across filings — use ciks=, not entityName= (entityName returned 0 hits in testing)
WebFetch(url="https://efts.sec.gov/LATEST/search-index?q=%22{phrase}%22&forms=10-K,10-Q,20-F,6-K&ciks={CIK}")
# Transcripts: company IR (often JS-rendered — the fetch may return only navigation), then fool.com
WebSearch(query='"{Company}" Q{N} {FY} earnings call transcript site:fool.com')
```

`data.sec.gov` and `www.sec.gov/files/*` require a User-Agent with a contact address when called with curl. Seeking Alpha returns 403 — don't rely on it.

### What each source is good for

| Source | Good for | Caveats |
|---|---|---|
| 10-K / 20-F (Business + Risk Factors + MD&A) | Stated pricing model, packaging moves, NRR/dollar-based net retention definitions, customer-count thresholds (e.g. ">$100K ARR customers") | Annual and lawyered; "pricing" language is generic — quote the specific sentence |
| 10-Q / 6-K | Quarter-level metric shifts, new pricing called out as a driver | 6-K is a wrapper — the press release or shareholder letter is the attachment |
| Earnings call transcript | *Why* a change happened, migration timelines, analyst pushback on price | Management framing; tag `[Verified]` for what was said, never for whether it's true |
| Shareholder letter / investor day deck | Monetization strategy, AI pricing direction, seat vs usage mix | Forward-looking statements — label as intent |

Filings and calls are primary sources for *what the company said*. Pair them with the pricing page for *what it actually charges*.

### What to extract

- Management commentary on pricing rationale ("we're seeing strong demand at the new price point...")
- Analyst pushback questions about pricing pressure or churn
- ARPU or NRR metrics disclosed alongside pricing changes
- Forward-looking pricing signals ("we expect to complete the migration to new pricing by Q2...")

### Output

```
## {Company} — earnings pricing mentions ({quarter})

**Source:** [{Earnings call title}]({url})

**Key quotes:**
> "{exact quote from management}" — {speaker title}, {date}

**Strategic signal:** {1-2 sentence interpretation of what this means for pricing direction}
```

---

## 5. Cross-company pattern synthesis

Use when: a company makes a pricing move and you want to understand whether it's an isolated decision or part of a broader market pattern.

### Approach

After identifying a specific change type (e.g., "Clay switched to dual-metric pricing"), search for other companies that made the same type of move:

```
WebSearch(query='SaaS "dual metric pricing" OR "usage + seat pricing" 2024 OR 2025 OR 2026')
WebSearch(query='B2B SaaS pricing restructure "actions and credits" OR "seats and usage" 2025')
search_pricing_knowledge(query="{change type} pricing strategy examples")
search_pricing_knowledge(query="{company category} pricing model trends")
```

Then cross-reference with `search_companies_advanced` in PricingSaaS to find companies with similar pricing attributes:

```
search_companies_advanced(has_license=true, price_min={range_floor}, price_max={range_ceiling})
```

### Output

```
## Market pattern: {Change type}

**Companies that made a similar move:**
| Company | When | What they did | Outcome (if known) |
|---------|------|---------------|-------------------|
| {Company A} | {Date} | {Description} | {Revenue impact, churn signal, etc.} |

**Pattern assessment:** {Is this an isolated move or a market-wide trend? What does the prevalence tell you about where the category is heading?}

**Implication for {original company}:** {What can be inferred about likely success or risk of their move given what others experienced?}
```

---

---

## 6. Credit-zero fallback — reconstructing pricing history without paid diffs

Use when: `get_status()` returns 0 credits and paid PricingSaaS tools (`get_company_history`, `get_diff_highlight`, `fetch_diffs`) cannot be called. This method reconstructs the same information from zero-cost sources. Run automatically — no user prompt needed.

### When to activate

Triggers whenever `get_status()` shows 0 remaining credits AND `discovery_only` has identified periods with high-signal change types: `Price Increased`, `Price Decreased`, `Plan Added`, `Plan Removed`, `Plan Renamed`, `Discount Removed`, `Discount Added`.

Skip periods that contain only `Feature Added` or `Feature Changed` — those rarely need diff reconstruction.

### Period-to-date mapping

Convert PricingSaaS period strings to snapshot target dates:

| Period format | Before snapshot date | After snapshot date |
|---------------|---------------------|---------------------|
| `{YYYY}Q1` | `{YYYY-1}1231` | `{YYYY}0401` |
| `{YYYY}Q2` | `{YYYY}0331` | `{YYYY}0701` |
| `{YYYY}Q3` | `{YYYY}0630` | `{YYYY}1001` |
| `{YYYY}Q4` | `{YYYY}0930` | `{YYYY+1}0101` |
| `{YYYY}M{MM}` | first day of prior month | first day of next month |
| `{YYYY}W{WW}` | 3 days before week start | 3 days after week end |

### Source waterfall (run all in parallel per high-signal period)

#### Source 1: Wayback Machine snapshots (highest fidelity)

```
# Find available snapshots bracketing the change:
WebFetch(url="https://archive.org/wayback/available?url={domain}/pricing&timestamp={before_YYYYMMDD}")
WebFetch(url="https://archive.org/wayback/available?url={domain}/pricing&timestamp={after_YYYYMMDD}")

# Fetch the actual pages using closest.url from each response (Bash, not WebFetch):
curl -s -A "Mozilla/5.0" "{closest.url_before}"
curl -s -A "Mozilla/5.0" "{closest.url_after}"
```

Diff the fetched pages — scan for plan names, `$` price values, feature bullets per tier, and CTA text changes.

**Note:** `closest.url` is a `web.archive.org` URL, which WebFetch can't reach — fetch it with Bash `curl` (Method 1 access table). The Availability API can return `{}` even when captures exist; list captures with CDX over curl before concluding there are none.

#### Source 2: Third-party price trackers

```
WebFetch(url="https://www.saaspricepulse.com/tools/{company-name}")
WebFetch(url="https://getpulsesignal.com/pricing/{company-name}")
WebSearch(query='"{Company}" pricing history site:saaspricepulse.com OR site:getpulsesignal.com')
```

These sites often cache old plan names and prices alongside current ones — especially useful after a rename-and-raise.

#### Source 3: Community disclosure (customers post price increase emails/screenshots)

```
WebSearch(query='"{Company}" price increase {year} site:reddit.com OR site:news.ycombinator.com')
WebSearch(query='"{Company}" pricing change {year} "per user" OR "per month" OR "per seat"')
WebSearch(query='"{Company}" new pricing {month_range} {year} announcement OR email OR notification')
```

Reddit and HN threads frequently contain exact before/after prices quoted by customers who received the increase notification.

#### Source 4: Official announcement (changelog / blog)

```
WebFetch(url="{domain}/changelog")
WebFetch(url="{domain}/blog")
WebSearch(query='"{Company}" pricing {year} changelog OR "pricing update" OR "new plans" OR "pricing change"')
```

#### Source 5: (retired) Google Cache
Google removed the `cache:` operator in 2024. Don't call it.

#### Source 6: Vendr marketplace

```
WebFetch(url="https://www.vendr.com/marketplace/{company-name}")
```

Vendr sometimes documents historical pricing in their negotiation sections.

### Output format

Label reconstructed diffs clearly so they are not confused with PricingSaaS-sourced data:

```markdown
#### {Period} — reconstructed diff (credit-free)

*PricingSaaS flagged {N} change(s): {change types}. Reconstructed from: {sources used}.*

| Element | Before | After | Source |
|---------|--------|-------|--------|
| {Plan name / price / feature} | {old value} | {new value} | Wayback / SaasPricePulse / Reddit / etc. |

[View before snapshot]({wayback_url_before})   [View after snapshot]({wayback_url_after})
[Unlock full diff on PricingSaaS](https://pulse.pricingsaas.com/companies/{slug}/diffs/{period}) *(requires {N} credit — resets {reset_date})*
```

If no source returned useful data, always note explicitly:
> "Reconstruction attempted for {period} ({change types}) — Wayback Machine had no snapshots, no community posts found, third-party trackers showed current pricing only. Unlock with {N} credit when available."

Never silently omit a period. Always document what was attempted.

---

## 7. Reviews and community — what's reachable and how to tag it

| Source | Direct fetch (2026-09-27) | Use | Tag | Caveats |
|---|---|---|---|---|
| G2 | 403 (WebFetch and curl) | `WebSearch(... site:g2.com)` snippets | `[Reported]` | Snippets only; review dates often missing; vendor-incentivised reviews |
| Capterra | `/p/{id}/{name}/reviews/` returns 404 — URL pattern changed | Search only | `[Reported]` | Same as G2 |
| TrustRadius | 403 | Search only | `[Reported]` | Enterprise-skewed reviewers |
| Reddit | WebFetch refuses reddit.com; JSON endpoint 403 | `WebSearch(... site:reddit.com)` | `[Reported]` | Anecdotal; check the thread date |
| Hacker News | `https://hn.algolia.com/api/v1/search?query={q}&tags=story&numericFilters=created_at_i>{unix}` works | Direct API | `[Reported]` | Dev-heavy audience |
| Vendr | `https://www.vendr.com/marketplace/{company}` works (e.g. Asana median contract value shown) | Deal economics | `[Reported]` | Vendr's own sample; method not published |
| SaaS Price Pulse / PulseSignal | `saaspricepulse.com/tools/{company}`, `getpulsesignal.com/pricing/{company}` work | Cached old prices, change dates | `[Reported]` | Scraped; verify against Wayback before citing a price |

A fact seen only in a search snippet is `[Reported]`, even when the snippet is from the vendor's help center (playbooks/README.md tag edge cases).

---

## When to call these methods

| Trigger | Method |
|---------|--------|
| "How did their pricing page look before?" | Wayback Machine (Method 1) |
| "Are they planning a pricing change?" | Job postings (Method 2) |
| "Did they add anything to a plan recently?" | Changelog mining (Method 3) |
| "Why did they raise prices?" (public co) | Earnings call (Method 4) |
| "Is this a trend or a one-off?" | Cross-company pattern synthesis (Method 5) |
| Credits = 0 and history has price-related changes | Credit-zero fallback (Method 6) — run automatically, no prompt |
| After any significant change detected via monitoring | All of the above, in parallel |
