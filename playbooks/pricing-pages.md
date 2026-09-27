# Pricing pages — CRO playbook

Surface type 1: the public or in-app plan comparison. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks). Cohort: mostly **new users** evaluating; logged-in "See plans" traffic is existing users.

## Core rule

A pricing page has one job: make the right plan feel obvious for the right buyer. Visitors arrive evaluating whether the price is worth it, so every element should reduce the work of choosing — structure first, visual design last.

## Patterns

### Page structure (proven order)

1. **Headline** — the outcome, not "Compare our plans".
2. **Billing toggle** — monthly / annual, with the saving shown in dollars as well as percent.
3. **Plan cards** — the self-serve choice kept to three or four comparable cards (see *Tier count* below).
4. **One recommended plan**, singled out by emphasis — the only filled CTA, a label, an accent border — not by extra height.
5. **Feature comparison** — collapsed by default, expandable; expanding it is a high-intent signal worth tracking.
6. **Social proof** — next to the CTA, where the hesitating buyer is, not only at the bottom.
7. **FAQ** — the top objections: cancellation, seat minimums, billing, credits.
8. **CTA repeat** — sticky or repeated at the bottom.

### Plan card anatomy

- Plan name, and a **one-line promise** naming who it's for.
- Price with the cadence explicit ("per seat / month, billed annually").
- A **specific CTA** per plan, matched to its intent.
- 3–5 highlights: what makes *this* plan different from the one below.
- "Everything in {lower plan}, plus:" — saves re-reading.
- For seat-based plans, the minimum and bundle steps stated on the card, not discovered at checkout.
- **Free tier clarity:** its limits stated plainly, and "Free forever" vs. "Free trial" never ambiguous — a vague free tier creates churn, not activation.
- **Annual anchor:** when the toggle is on annual, show the monthly price crossed out beside the annual equivalent.

### Billing default

Figma and Canva default to annual; Linear and Airtable show only annual rates; Slack leads with a monthly promotion beside the annual price [Verified — each company's pricing page, checked 2026-09-25]. Annual contracts correlate with lower churn [Reported — ProfitWell research via [Reforge](https://www.reforge.com/blog/brief-churn-benchmarks-for-recurring-revenue-businesses)]. monday already defaults to annual (~18% saving, [monday-context.md](../context/monday-context.md)), so for monday the test is the savings label (dollars vs. percent), not the default.

### Tier count

Fewer comparable choices are easier to decide between — there's no primary study behind a magic number, but three or four self-serve cards is the common practice. **monday has five tiers** (Free, Basic, Standard, Pro, Enterprise — [monday-context.md](../context/monday-context.md)). Canva shows four main cards and treats Free and Enterprise differently from the paid middle [Verified — [Canva pricing](https://www.canva.com/pricing/)]; the analogue for monday is to make Free and Enterprise visually distinct so the real comparison is Basic / Standard / Pro.

### The recommended plan is a commercial decision

Highlight the plan that serves the revenue goal, not a design choice. Canva's "Recommended" badge sits on **Business**, its higher paid plan [Verified — [Canva pricing](https://www.canva.com/pricing/)]. Figma and Linear recommend no plan [Verified — [Figma](https://www.figma.com/pricing/), [Linear](https://linear.app/pricing)].

### CTAs specific to each plan

| Plan | Right CTA | Wrong CTA |
|---|---|---|
| Free | "Get started free" | "Get started" |
| Paid, with trial | "Try {plan} free" / "Start a free trial" | "Get started" |
| Enterprise | "Talk to us", plus a self-serve path for smaller enterprise teams | "Upgrade" |

Cursor's CTAs are tier-specific — "Try Cursor", "Get Pro", "Get Teams", "Contact sales" [Verified — [Cursor pricing](https://cursor.com/pricing)]. Canva uses "Get started" on Free and "Start a free trial" on Pro and Business [Verified]. Linear uses "Get started" on every self-serve plan [Verified] — the same-CTA pattern.

### AI credits on the pricing page

Credits need their own explanation, with task translation at the tier level — not buried in docs ([credit-ui.md](credit-ui.md) owns the translation rule).

- **Publish the rates.** HubSpot publishes included credits per tier (Starter 500, Professional 3,000, Enterprise 5,000) and a rate sheet (50 credits per resolved Customer Agent conversation, 10 per AI workflow action) [Verified — [HubSpot catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog)]. A worked example built from those rates — e.g. 40 resolutions (2,000) + 50 workflow actions (500) — is this playbook's construction, not HubSpot's.
- **Show credits per seat or tier on the page.** Figma's pricing page now lists AI credits per seat type [Verified — [Figma pricing](https://www.figma.com/pricing/)], after confusion around the March 18, 2026 enforcement [Reported — [Vibe Coding Academy](https://www.vibecodingacademy.ai/blog/figma-ai-credits-everything-you-need-to-know)].
- **Translate into real tasks.** Notion publishes per-run cost ranges for Custom Agents in its help center [Verified — [Notion help](https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents)].
- **For monday:** use the context file's official translation (1,000 credits ≈ 50 resume screenings, 5 hours of meeting summaries, hundreds of workflow updates). "1 credit ≈ 1 AI action" is retired — the rate card contradicts it.

### Bundling AI into a higher tier

When AI moves into a higher tier, the page must justify the jump on AI value, not on the other features in the bundle — see [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling).

### Mobile

- The recommended plan first in the stacked cards, not in the middle.
- Tap targets at least 44 × 44 pt [Verified — [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/buttons)].
- The billing toggle works before the cards appear.
- The comparison table becomes an accordion or a horizontal scroll.
- Judge mobile on a real device or a true 375px viewport — a narrow headless-browser window crops the page and fakes overflow.

### Testing order

Structure before visual design: recommended plan → CTA copy per plan → social proof placement → comparison collapsed vs. open → savings label. Don't test button colour until these are settled.

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

**What they ship [Reported — third-party pricing coverage].** Repriced March 2026 to Free / Launch / Growth / Enterprise. Launch lists at $185/mo and Growth at $495/mo, $167 and $446 on annual ("save 10%"). All plans include unlimited seats — you pay for consumption, not people. Two meters on every paid tier: Data Credits (buying third-party data) and Actions (platform work). Plan cards are sliders: small print reads "Starts at $54/mo, expand anytime" on Launch — the headline price is a default position, not a floor. Legacy Starter/Explorer/Pro kept indefinitely for existing customers.

**Flow.** Land on pricing → pick plan → drag slider to credit volume → price updates live → credit calculator for estimation.

**UI.** Plan card = headline price + slider + two meter values. Annual toggle. FAQ below the cards.

**Copy pattern.** Leads with "unlimited users" as the anti-seat-tax promise. Expansion language ("expand anytime") on the card itself, removing fear of picking the wrong tier.

**Why it works.** The slider kills the "which box am I?" paralysis for usage products — the tier sets capabilities (CRM sync, API), the slider sets volume. Unlimited seats removes the internal "who gets a license" negotiation, a common blocker to spreading a PLG product (inference).

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

**Copy pattern.** The pricing promise is the standout copy asset — it pre-empts a common AI-buyer fear: that the vendor will raise prices once the team depends on it (inference).

**Why it works.** Separating AI lets ClickUp keep the $7/$12 headline competitive against Asana/monday while monetizing AI demand. The promise block turns cost volatility into a trust signal.

**Where it breaks.** A Business seat with Everything AI is $40/user/mo — over 3x the advertised $12 — and third-party pages frame this as a hidden cost. All-seats AI billing means a 30-seat workspace pays for 30 AI seats when 5 people use it. Three layers (plan × AI tier × credits) is the most cognitively expensive structure in this set.

**Steal for monday.com.** (1) Steal the *pricing promise* verbatim in structure (not copy) for the AI credits section — monday's credits are new (May 2026) and buyers have no track record to trust. (2) Avoid the three-layer stack: monday's current model (credits bought alongside seats, per [monday-context.md](../context/monday-context.md)) is two layers — keep the page at two.

### Claude — plans defined by usage multipliers

**What they ship [Reported — third-party coverage of Claude's plans].** Individual: Free, Pro $20/mo ($17/mo annual, $200/yr), Max $100 (5x Pro usage) and $200 (20x Pro usage). Team: standard seats (1.25x Pro) and premium seats (6.25x Pro). Usage runs on a rolling five-hour session window plus a weekly limit on paid plans; chat, desktop, and Claude Code draw from one pool. Anthropic doesn't publish a fixed message count because usage depends on message length, attachments, model, and features; the Help Center gives an approximate Pro figure (~45 messages per five hours). Usage-based Enterprise bills at API rates with no per-seat caps.

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
| Seat-tax killer (if applicable) | Name the fear | "Credits are shared across your account" (monday pools credits account-wide; admins can still set per-user limits, so don't promise "no caps") |
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

## Anti-patterns

| Anti-pattern | Why it fails | Who did it |
|---|---|---|
| Credit amounts without task translation | Meaningless without context | Common; monday risk if the retired 1:1 translation returns |
| Seat minimum hidden until checkout | Users feel tricked | Common |
| The same bullets on every plan | The buyer can't tell the plans apart | Common |
| The same CTA on every plan | No signal on intent or recommendation | Linear — "Get started" on every self-serve plan [Verified] |
| Feature table fully expanded above the fold | Adds cognitive load | Common |
| Feature lists start at different heights across plans | The eye can't compare line by line *(design rule)* | Common |
| CTAs at different heights across plans | The buttons stop reading as one choice *(design rule)* | Common |
| Recommended plan singled out only by height | Height reads as "more stuff", not "pick this" *(design rule)* | Common |
| AI bundled into a higher tier with no path for AI-only buyers | Buyers route to alternatives | [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling) |
| A billing-model change explained unclearly | Trust collapse, refunds | [case: cursor-2025-pricing](cases.md#cursor-2025-pricing) |
| Social proof only at the bottom | Misses the buyer hesitating at the CTA | Common |
| "Contact sales" as the only Enterprise path | Loses mid-market teams that would self-serve | Common |
| Comparison table with no locked first column on mobile | Users lose which row they're reading; the table stops being a comparison | Most SaaS products — see [NN/g, mobile tables](https://www.nngroup.com/articles/mobile-tables/) [Verified] |

## monday.com-specific notes

All facts from [context/monday-context.md](../context/monday-context.md).

- **Five tiers**, annual shown by default with an ~18% saving; paid plans start at 3 seats in bundles (3, 5, 10, 15, 20, 25, 30, 40). State the minimum and bundles on the card.
- **Make Free and Enterprise visually distinct** so the comparison is Basic / Standard / Pro.
- **Enterprise** needs "Talk to us" and a self-serve path for smaller enterprise teams.
- **AI credits need their own explanation** on the page, with the official task translation per tier (Basic 1,000 fixed; Standard 2,000–8,000; Pro 3,000–20,000).
- **Cross-sell:** the pricing page is an underused channel for CRM, service and dev awareness.
- **One translation:** the page uses the official "1,000 credits ≈ 50 resume screenings" line, matching the in-product meter (see [credit-ui.md](credit-ui.md)).

## Sources

Checked 2026-09-24 (AI-native set) and 2026-09-25 (everything else).

- Pricing pages: https://www.figma.com/pricing/ · https://www.canva.com/pricing/ · https://www.airtable.com/pricing · https://linear.app/pricing · https://slack.com/pricing · https://cursor.com/pricing
- Churn and annual contracts: https://www.reforge.com/blog/brief-churn-benchmarks-for-recurring-revenue-businesses
- HubSpot: https://legal.hubspot.com/hubspot-product-and-services-catalog · https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing
- Figma credits: https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work · https://www.vibecodingacademy.ai/blog/figma-ai-credits-everything-you-need-to-know
- Notion: https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents · https://www.notion.com/help/2025-pricing-changes
- Apple HIG: https://developer.apple.com/design/human-interface-guidelines/buttons
