# Pricing pages — CRO playbook

Surface type 1. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

## What makes a pricing page convert

### The job
A pricing page has one job: make the right plan feel obvious for the right user. Confusion kills conversion. Every element should reduce cognitive load, not add to it.

### Page structure (proven order)
1. **Headline** — outcome-focused, not feature-focused ("Everything your team needs to move faster" not "Compare our plans")
2. **Toggle** — Monthly / Annual with savings callout (show $ saved, not just %)
3. **Plan cards** — 3–4 max. More than 4 creates paralysis.
4. **Recommended plan highlight** — one card visually elevated (border, badge, background)
5. **Feature comparison** — collapsed by default, expandable. Full table below fold is fine.
6. **Social proof** — logos + one strong quote near CTA
7. **FAQ** — address top 3 objections (cancellation, seat limits, billing)
8. **CTA repeat** — sticky or repeated at bottom

## Plan card anatomy

**Must-haves:**
- Plan name (short, memorable)
- One-line value prop per plan (not a list of features — a promise)
- Price with billing cadence explicit ("per seat / month, billed annually")
- Primary CTA — specific ("Start free", "Start Pro trial", not just "Get started")
- 3–5 bullet highlights (what makes *this* plan different from the one below it)
- "Everything in [lower plan], plus:" — reduces re-reading

**Common failures:**
- All plans have the same bullets → user can't differentiate
- Price shown without context → anchor with crossed-out monthly price
- CTA identical across all plans → no signal on what's recommended
- "Contact sales" as only Enterprise CTA without a self-serve option → loses mid-market

## Pricing presentation patterns

### Anchoring
- Show the most expensive plan first (left-to-right reading) or make it visible — it anchors perception
- Cross out monthly price on annual toggle
- "Most popular" badge on the plan you want to sell

### Freemium / free tier
- If you have a free tier, make its limits clear — vague free tiers create churn, not activation
- "Free forever" vs "Free trial" must be unambiguous

### Per-seat vs. flat vs. usage
- Per-seat: show "starting at X users" with a calculator if possible
- Usage-based: show example usage tiers ("~500 AI actions/month")
- Hybrid: simplify — don't show both dimensions simultaneously unless unavoidable

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Credit amounts shown without task translation | Meaningless without context |
| Seat minimum hidden until checkout | Users feel tricked |
| All tiers with identical "Get started" CTAs | No signal on what's recommended |
| Feature table fully expanded above the fold | Adds cognitive load instead of reducing it |
| Feature lists start at different heights across plans | The eye can't compare plans line by line; plans look broken. Fix the title/price block height so every list starts at the same line *(design rule)* |
| CTAs sit at different heights across plans | The buttons stop reading as one choice. Pin each CTA to the same line regardless of content above *(design rule)* |
| Recommended plan singled out only by being taller | Height reads as "more stuff", not "pick this". Use emphasis — the only filled CTA, a label, an accent border *(design rule)* |

## Benchmarks (B2B SaaS)

*Directional only — these figures pre-date the evidence-tag standard and carry no source. Don't cite them as fact in a review; the sourced material is in the AI-native reference set below.*

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Pricing page → trial start | <3% | 5–8% | 10%+ |
| Annual toggle usage | <20% | 30–40% | 50%+ |
| Time on page before CTA click | >3 min | 1–2 min | <60s |

## Best-in-class examples

*Pre-dates the evidence-tag standard — the patterns are sound, but any figures here are unsourced. Tagged teardowns are in the AI-native reference set below.*

**Linear** — Extreme clarity. 3 plans, one recommended, feature list that actually differentiates. No fluff.

**Notion** — Annual toggle with $ savings shown. "Most popular" on Plus. Free tier limits explicit.

**Loom** — Uses "you've already recorded X videos" personalization on pricing page for logged-in users. Context-aware pricing pages convert 30–40% better than static.

**Intercom** — Anchoring via add-ons. Base price looks reasonable; upsells are modular. Reduces sticker shock.

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Each teardown follows the same shape: what they ship → flow → UI → copy → why it works → where it breaks → what monday.com should steal. Evidence tags: **[Verified]** = vendor docs/pricing page, **[Reported]** = third-party source, **[Teardown needed]** = capture a live screenshot before citing in a review.

### At a glance

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Pricing axis | Usage only (two meters), unlimited seats | Seat type × plan, AI credits per seat | Seat plan + separate AI seat layer + AI credits | Plan tier defined by usage multiplier |
| AI unit on the page | Data Credits + Actions | AI credits per seat / month | AI Super Credits per user / month | "Nx Pro" usage, no fixed count |
| Plan count (self-serve) | 3 (Free, Launch, Growth) | 3 + seat types | 4 plans × 2 AI tiers | 4 individual (Free, Pro, Max 5x, Max 20x) |
| Strongest move | Slider plans — tier is a starting point, not a box | Plan separated from seat — buyers price people, not packages | Public pricing promise on AI cost changes | Relative multipliers make a fuzzy unit comparable |
| Biggest risk | Two currencies; per-enrichment cost lives in-app, not on page | Credits per person, no rollover, not shareable | Stacked layers — real price ~3x the headline | No absolute number — users can't predict capacity |

### Clay — usage-only, two meters, slider plans

**What they ship [Verified/Reported].** Repriced March 2026 to Free / Launch / Growth / Enterprise. Launch lists at $185/mo and Growth at $495/mo, $167 and $446 on annual ("save 10%"). All plans include unlimited seats — you pay for consumption, not people. Two meters on every paid tier: Data Credits (buying third-party data) and Actions (platform work). Plan cards are sliders: small print reads "Starts at $54/mo, expand anytime" on Launch — the headline price is a default position, not a floor. Legacy Starter/Explorer/Pro kept indefinitely for existing customers.

**Flow.** Land on pricing → pick plan → drag slider to credit volume → price updates live → credit calculator for estimation.

**UI.** Plan card = headline price + slider + two meter values. Annual toggle. FAQ below the cards.

**Copy pattern.** Leads with "unlimited users" as the anti-seat-tax promise. Expansion language ("expand anytime") on the card itself, removing fear of picking the wrong tier.

**Why it works.** The slider kills the "which box am I?" paralysis for usage products — the tier sets capabilities (CRM sync, API), the slider sets volume. Unlimited seats removes the internal "who gets a license" negotiation, which is the #1 PLG spread blocker.

**Where it breaks.** Two currencies that deplete independently is the most-cited confusion in third-party coverage. The per-enrichment credit cost is published inside the app rather than on the pricing page, so buyers can't compute cost-per-lead before signup. The page states prices two ways (card vs. FAQ) — a legibility tax. Third-party "real cost" articles now outrank Clay for its own pricing queries.

**Steal for monday.com.** (1) Separate *capability tier* from *credit volume* visually — monday's credit packages per tier (see [monday-context.md](../context/monday-context.md)) are a natural slider. (2) Put a "what does 1,000 credits do" table on the page itself — never force the user into the product to learn unit costs. (3) Show one price format per page.

### Figma — plan ≠ seat, AI credits per seat

**What they ship [Verified].** The pricing page separates plan from seat. Professional: Full seat $20/mo ($16 annual), Dev $15/$12, Collab $5/$3, View free. AI credits are included with every seat on every plan and belong to the individual; they reset monthly, don't roll over, and can't be shared. Professional Full seat = 3,000 credits/mo; Starter = 500. Admin-level add-on: a shared credit pool subscription (from $120/mo for +5,000 credits, launched March 11, 2026, repackaged with more credits for the same price on Aug 25, 2026) plus pay-as-you-go up to a spending limit. The Help Center publishes approximate per-task costs (~30+, ~75+, ~100+ credits for escalating Figma Make tasks).

**Flow.** Choose plan → configure seat mix → see AI credit allowance per seat type → admins buy pooled top-ups separately.

**UI.** Plan cards + seat-type price grid. AI credits live in seat descriptions and a Help Center deep-dive.

**Copy pattern.** Task-shaped credit examples ("make this design interactive ≈ 75+ credits") rather than abstract token talk.

**Why it works.** Buyers price the *team composition* they have (designers, devs, reviewers) instead of forcing everyone into one plan. Viewers free = unlimited spread. Publishing task examples is the honest version of credit translation.

**Where it breaks.** Per-person, non-shareable, non-rolling credits create a "use it or lose it" feeling for light users and a wall for heavy users — the March 18, 2026 enforcement generated sustained forum backlash ("ran out after four hours"). Model choice swings cost up to ~8x for the same click (reported: 2 vs. 16 credits for image generation), which the pricing page can't express.

**Steal for monday.com.** (1) Publish task-level credit examples on the pricing page (agent run, notetaker hour, AI Block on 100 items). (2) Pool credits at the account level — Figma's shared admin pool is their fix for the per-seat problem; monday already sells credits alongside seats, so present the account balance as the unit. (3) If model choice changes cost, say so at the point of choice, not on the pricing page.

### ClickUp — three stacked layers + a pricing promise

**What they ship [Verified/Reported].** Workspace plans: Free Forever, Unlimited $7, Business $12, Enterprise custom (annual). AI is sold separately on its own pricing page: Brain AI $9/user/mo (1,500 AI Super Credits per user/mo) and Everything AI $28/user/mo (5,000 credits). Extra credits $10 per 10,000. The whole workspace must be on the same plan, and the AI add-on is billed on every paid member, not only AI users. The Brain pricing page carries an explicit promise: savings on AI costs get passed on, sudden provider cost spikes get subsidized, and any increases will be gradual and transparent.

**Flow.** Pick workspace plan → separately land on Brain pricing → pick AI tier → credits metered on top.

**UI.** Two pricing pages. AI page leads with tier cards and the pricing-promise block.

**Copy pattern.** The pricing promise is the standout copy asset — it pre-empts the #1 AI-buyer fear (the vendor will raise prices once we depend on it).

**Why it works.** Separating AI lets ClickUp keep the $7/$12 headline competitive against Asana/monday while monetizing AI demand. The promise block turns cost volatility into a trust signal.

**Where it breaks.** A Business seat with Everything AI is $40/user/mo — over 3x the advertised $12 — and third-party pages frame this as a hidden cost. All-seats AI billing means a 30-seat workspace pays for 30 AI seats when 5 people use it. Three layers (plan × AI tier × credits) is the most cognitively expensive structure in this set.

**Steal for monday.com.** (1) Steal the *pricing promise* verbatim in structure (not copy) for the AI credits section — monday's credits are new (May 2026) and buyers have no track record to trust. (2) Avoid the three-layer stack: monday's current model (credits bought alongside seats, per [monday-context.md](../context/monday-context.md)) is two layers — keep the page at two.

### Claude — plans defined by usage multipliers

**What they ship [Verified].** Individual: Free, Pro $20/mo ($17/mo annual, $200/yr), Max $100 (5x Pro usage) and $200 (20x Pro usage). Team: standard seats (1.25x Pro) and premium seats (6.25x Pro). Usage runs on a rolling five-hour session window plus a weekly limit on paid plans; chat, desktop, and Claude Code draw from one pool. Anthropic doesn't publish a fixed message count because usage depends on message length, attachments, model, and features; the Help Center gives an approximate Pro figure (~45 messages per five hours). Usage-based Enterprise bills at API rates with no per-seat caps.

**Flow.** Individual vs. Team & Enterprise tabs → monthly/annual toggle → plan cards → FAQ explains the session/weekly mechanics.

**UI.** Minimal cards. Max is one card with a 5x/20x choice rather than two separate cards — keeps the grid at three visible columns.

**Copy pattern.** Each tier is described relative to the one below ("5x more usage than Pro"). No feature laundry list on Max — the only differentiator is capacity, and the copy says so.

**Why it works.** When the base unit is inherently fuzzy (a "message" varies 100x in cost), a relative multiplier is the only honest comparison. The ladder (1x → 5x → 20x) makes the upgrade decision a single question: "Do I hit my limit?"

**Where it breaks.** No absolute number means users can't predict whether Pro covers their week until they've hit the wall — capacity discovery happens through failure. Stacked session + weekly limits need a FAQ to explain.

**Steal for monday.com.** (1) For AI tiers, describe the step-up in capacity multiples *and* tasks ("2x the agent runs of Standard"). (2) Collapse near-identical tiers into one card with a capacity selector (like Max 5x/20x) to keep the grid at 3–4 columns. (3) Publish the approximate anchor (Anthropic's ~45 messages) — one honest number beats none.

### Copy bank — AI pricing pages (adapt, then run through `improve-conversion-surfaces-copy`)

| Element | Pattern | Example for monday.com |
|---|---|---|
| Credit section headline | Outcome + unit translation | "AI credits, measured in work done" |
| Credit explainer line | Task anchor, not a number | "3,000 credits ≈ [X] agent runs or [Y] hours of meeting notes" |
| Seat-tax killer (if applicable) | Name the fear | "Credits are shared across your account — no per-person caps" |
| Expansion reassurance | Put it on the card | "Start at 3,000 credits. Add more anytime." |
| Pricing promise | Pre-empt lock-in fear | "If our AI costs go down, your price goes down. If they go up, we'll tell you first." (requires legal + finance sign-off) |
| Tier differentiator (capacity-only tier) | Relative multiple | "Everything in Pro, with 2x the monthly credits" |

### Anti-patterns surfaced by this set

| Anti-pattern | Seen at | Fix |
|---|---|---|
| Unit cost only discoverable in-product | Clay | Publish a task-cost table on the page |
| Two meters that deplete independently | Clay | One currency on the page; handle internal splits server-side |
| Credits that can't be shared or rolled | Figma | Account-level pool, rollover cap |
| AI billed on every seat regardless of use | ClickUp | Bill AI at account level or allow per-seat opt-in |
| Headline price that's ~1/3 of real cost | ClickUp | Show "with AI" price on the card |
| No absolute capacity number | Claude | Publish an approximate anchor |

### Sources (checked 2026-09-24)

- Clay: https://www.cleanlist.ai/blog/2026-03-12-clay-pricing-changes-2026 · https://www.joinvalley.co/blog/clay-pricing-and-credits-explained-2026 · https://salesmotion.io/blog/clay-pricing · https://www.docket.io/resources/research/clay-pricing
- Figma: https://www.pagedog.app/blog/figma-pricing · https://www.figma.com/blog/updates-to-ai-credits-in-figma/ · https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work · https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ · https://www.appshot.app/posts/2026-07-09-figma-ai-credits-explained/
- ClickUp: https://clickup.com/brain/pricing · https://www.rock.so/blog/clickup-pricing · https://agiled.app/blog/clickup-pricing
- Claude: https://www.ai-toolbox.co/claude-management-and-productivity/claude-usage-limits-2026 · https://krater.ai/blog/claude-usage-limits · https://claudelimit.com/claude-pro-limits/

## monday.com-specific notes

- Enterprise tier should always have a clear "talk to us" path but *also* a self-serve option for smaller enterprise teams
- The AI credit model needs its own section on the pricing page — credits as a dimension confuse users if not explained with examples
- CRM cross-sell opportunity: pricing page is an underused channel for multi-product awareness
