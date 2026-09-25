# Monetization model benchmarking workflow

Answer strategic questions about how SaaS companies structure pricing models — not just what they charge, but how they package, gate, and monetise AI features, usage, and seats. Benchmark monday.com's model against industry patterns.

Typical triggers:
- "How do AI companies sell credits?"
- "Usage-based vs seat-based — what do PLG tools do?"
- "How should we structure our credit packages?"
- "What's the industry norm for free trial length?"
- "How do other tools gate AI features?"
- "Benchmark our monetisation model"

---

## Step 1: Clarify the benchmarking question

If the question is broad ("how should we price AI?"), ask one clarifying question to identify the specific dimension:

> "Are you asking about: (a) the pricing metric — what unit to charge for, (b) the packaging structure — how to bundle features into tiers, (c) credit/consumption economics — how to size and price credit packages, or (d) a specific competitor's approach?"

Then route to the relevant sub-workflow below.

---

## Sub-workflow A: Pricing metric benchmarking

**Question type:** "Should we charge per seat, per usage, or flat?"

### Step A1: Pull relevant companies by model type

```
search_companies_advanced(pricing_model="per_user")
search_companies_advanced(pricing_model="usage_based")
search_companies_advanced(pricing_model="flat")
```

Run in parallel. Filter to the user's specified category or closest relevant category.

### Step A2: Get strategy context

```
search_pricing_knowledge(query="usage-based pricing SaaS 2025 2026")
search_pricing_knowledge(query="seat-based vs usage-based PLG")
search_pricing_knowledge(query="hybrid pricing model AI SaaS")
```

### Step A3: Web research

```
WebSearch(query="SaaS pricing metric trends 2026 seat-based usage-based")
WebSearch(query="{category} pricing model benchmark 2026")
WebSearch(query="PLG AI pricing per credit vs per seat")
```

### Step A4: Output — Pricing Metric Benchmark

```markdown
## Pricing metric landscape — {category}

### Model distribution

| Model | Companies using it | Example companies | Typical range |
|-------|--------------------|-------------------|---------------|
| Per seat | {N} | {list} | ${x}–${x}/seat/mo |
| Usage-based | {N} | {list} | ${x}/unit or credit |
| Flat / workspace | {N} | {list} | ${x}/mo |
| Hybrid | {N} | {list} | base + usage |

### Trend signal
{Which model is gaining share and why — cite evidence}

### Fit analysis for monday.com
- **Current model:** {seat-based with AI credit overlay}
- **Market direction:** {what the data shows}
- **Recommendation:** {specific, actionable — e.g. "Maintain seat-based as the anchor; AI credits as the expansion lever is the dominant 2026 pattern in B2B work tools"}
```

---

## Sub-workflow B: AI credit / consumption model benchmarking

**Question type:** "How do AI companies sell credits?" / "How do we structure credit packages?"

This is the highest-priority sub-workflow for monday.com given the AI Agents launch.

### Step B1: Identify AI-credit-using SaaS companies

```
search_companies(query="AI credits")
search_companies(query="AI agents usage")
search_companies(query="AI automation credits")
WebSearch(query="SaaS AI credit pricing model 2026 examples")
WebSearch(query="how AI companies sell credits usage-based 2026")
```

### Step B2: Pull details for each identified company

```
get_company_details(slug="{slug}")  # for each company found
```

Extract specifically: credit/usage pricing structure, package sizes, rollover policy, top-up mechanics, overage handling.

### Step B3: Supplementary research

```
WebSearch(query="Notion AI credits pricing how it works")
WebSearch(query="HubSpot AI credits model 2026")
WebSearch(query="Salesforce Einstein credits pricing structure")
WebSearch(query="Intercom Fin AI credit usage pricing")
WebSearch(query="Zapier AI credit model vs automation steps")
WebSearch(query='"AI credits" OR "AI actions" pricing model SaaS 2026')
```

For each company found, extract:
- **Credit unit name** (credits, actions, runs, tokens, compute units)
- **Credit-to-task translation** (how clearly they communicate what 1 credit does)
- **Package structure** (included in plan vs. add-on, package sizes, pricing)
- **Rollover policy** (monthly reset, accumulate, expire)
- **Overage handling** (hard stop, auto top-up, soft limit with warning)
- **Admin vs IC controls** (who can buy more, who sees the meter)

### Step B4: Output — AI Credit Model Benchmark

```markdown
## AI credit model benchmark — {date}

### How leading SaaS tools sell AI credits

| Company | Credit unit | Included in plan | Top-up available | Rollover | Overage |
|---------|-------------|-----------------|-----------------|---------|---------|
| {Company} | {name} | {plan + amount} | {yes/no, price} | {yes/no} | {stop/auto/warn} |

### Credit communication patterns
How clearly does each company translate credits to outcomes?

| Company | Translation clarity | Example |
|---------|-------------------|---------|
| {Company} | Clear / Vague / None | "1 credit = 1 AI action" |

**Industry finding:** {what the data shows about how companies communicate credit value}

### Package sizing patterns
- Common included credit amounts: {ranges}
- Common top-up package sizes: {ranges and prices}
- Dominant overage approach: {hard stop | auto-charge | warning}

### Key design patterns

**Pattern 1: Credits-in-plan (Intercom model)**
{Description — what companies do this, how it works, why}

**Pattern 2: Credits-as-add-on (Salesforce model)**
{Description}

**Pattern 3: Hybrid (base plan + credit overlay)**
{Description — this is closest to monday.com's current approach}

### So what for monday.com

- **Credit unit name:** {recommendation — does "AI credits" land well vs competitors?}
- **Included amount:** {what industry norms suggest for the Pro tier}
- **Top-up package sizing:** {recommended range based on benchmarks}
- **Rollover:** {what users expect based on competitive norms}
- **Overage UX:** {recommendation — hard stop risks agentic task failure; auto-charge risks trust issues; warning is safest but requires good credit meter UI}
- **Credit-to-task translation:** {how monday.com should communicate this — specific wording direction}
- **Admin vs IC controls:** {recommendation}
```

---

## Sub-workflow C: Trial and freemium model benchmarking

**Question type:** "What's the industry norm for trial length?" / "Should we offer freemium?"

### Step C1: Pull freemium data across category

```
search_companies_advanced(has_freemium=true)
search_companies_advanced(has_free_trial=true)
```

Filter to the relevant category.

### Step C2: Web research

```
WebSearch(query="{category} free trial length benchmark 2026")
WebSearch(query="PLG SaaS freemium vs free trial conversion 2026")
WebSearch(query="{category} freemium limits AI features gating")
```

### Step C3: Output — Trial / Freemium Benchmark

```markdown
## Trial and freemium benchmark — {category}

### Market overview

| Approach | % of market | Examples | Typical length/limits |
|----------|------------|---------|----------------------|
| Freemium | {N}% | {list} | {limits} |
| Free trial | {N}% | {list} | {length, credit card required?} |
| Demo-only | {N}% | {list} | — |
| None | {N}% | {list} | — |

### Trial conversion patterns
{What the data shows about typical trial-to-paid conversion triggers and timelines}

### AI feature gating in freemium
{How companies gate AI features on free tier — included, limited, or fully gated}

### So what for monday.com
- **Trial length:** {recommendation vs. norms}
- **AI credits in trial:** {recommendation — how much to include to drive aha moment}
- **Trial conversion trigger:** {what to show/prompt at what point}
```

---

## Sub-workflow D: Feature gating and packaging benchmarking

**Question type:** "How do competitors gate AI features across tiers?" / "What should be in Basic vs Pro?"

### Step D1: Pull tier details for relevant companies

```
get_company_details(slug="{slug}")  # for each competitor
```

Focus on: what's gated at each tier, especially AI/automation features.

### Step D2: Web research

```
WebSearch(query="{competitor} pricing tier breakdown AI features 2026")
WebSearch(query="{category} feature gating strategy per tier")
```

### Step D3: Output — Feature Gating Benchmark

```markdown
## Feature gating benchmark — AI features, {category}

### AI feature availability by tier

| Company | Free | Basic/Starter | Mid | Pro/Business | Enterprise |
|---------|------|--------------|-----|-------------|------------|
| {Company} | {credits/none/limited} | | | | |

### Gating patterns

**Pattern: AI included at mid-tier** — {companies, what's included}
**Pattern: AI gated to top tier only** — {companies}
**Pattern: AI credits as add-on** — {companies}

### So what for monday.com
- **Current gating:** {where AI sits today}
- **Competitive position:** {how it compares}
- **Recommendation:** {specific tier/feature recommendation with rationale}
```

---

## Output file

Write the benchmark output to:
`.monetization/research/{topic-slug}-{YYYY-MM}.md` — same convention as every research artifact, so the Growth PM and the spec skill find it

Use the research output template: [../../../templates/research-output.md](../../../templates/research-output.md)

## Log to monday

Follow [monday-logging.md](monday-logging.md):
- Item name: `{Topic} — Model Benchmark`
- Change Type: `Model Benchmark`
- Workflow: `monetization-model-benchmarking`

## Next step

After delivering the benchmark, always offer:

> "Want me to translate these findings into a recommendation for how monday.com should structure [specific aspect]? I can produce a 1-pager spec you can take to leadership."

If yes, hand off to `monetization-surface-spec` for the pricing page or `improve-conversion-surfaces-copy` for the copy angle.

```
---
→ Next step: monetization-surface-spec — translate benchmark findings into a surface spec or pricing page structure
→ Prompt: "Based on the benchmark, spec out [surface] for [tier/cohort]"
```
