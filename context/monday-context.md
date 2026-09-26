---
file: monday-context.md
purpose: Living source of truth for monday.com monetization strategy — plans, pricing, AI credits, feature gating, user cohorts, design system, and squad context. Read by every skill in this plugin.
owner: Growth Monetization PM (currently: Ohad Frankfurt)
last-updated: 2026-09-26
data-sources: monday.com/pricing, support.monday.com, monday.com/blog/ai-agents/monday-ai-credits
update-triggers: See "When to update this file" section below
future: Designed to eventually connect to internal AI Brain sources (monetization, AI credits). Until then: manual updates by owner.
---

# monday.com — Monetization Context

This file is the single source of truth for monday.com product and pricing context used by all skills in this plugin. When anything changes — a price, a tier, a credit structure, a new surface — update this file first.

---

## When to update this file

Update immediately when any of the following change:

- Plan prices (monthly or annual)
- AI credit inclusions, package sizes, or per-credit pricing
- What features are gated to which tier
- Trial length, structure, or credit card requirement
- A new monetization surface ships or is sunset
- The squad's primary conversion focus shifts
- A significant A/B test result changes the default surface behaviour

**How to update:** Edit this file directly in the repo. Add a changelog entry at the bottom. Bump `last-updated` in the frontmatter.

**How to verify:** Run `monetization-intelligence` against monday.com itself — the skill can research monday.com's own public pricing page and flag gaps between this file and what's live.

---

## Tier structure

Five tiers. Free is the only one with no seat minimum. All paid plans require minimum 3 seats and sell in bundles (3, 5, 10, 15, 20, 25, 30, 40 — custom quote above 40).

| Tier | Target segment | Annual price | Monthly price | Min seats |
|------|---------------|-------------|--------------|-----------|
| **Free** | Individuals, 2-person teams | $0 | $0 | 2 max |
| **Basic** | Small teams, simple tracking | $9/seat/mo | $12/seat/mo | 3 |
| **Standard** | Growing teams, core PM workflows | $12/seat/mo | $14/seat/mo | 3 |
| **Pro** | Advanced teams, automation-heavy | $19/seat/mo | $24/seat/mo | 3 |
| **Enterprise** | Large orgs, security/compliance needs | Custom | Custom | 3+ |

Annual billing saves ~18% vs monthly. Annual is the default shown on the pricing page.

**Primary upgrade pressure:**
- Free → Pro: the main PLG conversion path; most upgrade surfaces target this
- Standard → Pro: the expansion path for teams who grew into automation limits
- Pro → Enterprise: sales-assisted, not self-serve

---

## AI credits — current model (as of May 6, 2026)

AI credits are the consumption unit for all monday AI capabilities. They are **purchased alongside seats** — not a free inclusion, not a separate add-on. This model applies to customers who joined on or after May 6, 2026.

### What AI credits power

- **AI Notetaker** — meeting transcription and summaries
- **AI Blocks** — board column automations: categorise, summarise, extract, translate, sentiment, generate text (Pro and Enterprise only)
- **monday Agents** — autonomous AI agents running multi-step tasks
- **monday Vibe** — AI-powered app building
- **AI Workflows** — automated AI steps in workflow recipes
- **monday Sidekick** — conversational AI assistant (Standard and above)

Some capabilities are **free and do not consume credits**: check the AI Feature Catalog at support.monday.com for the current list — it changes as the platform evolves.

### Credit inclusions and packages by tier

| Tier | Minimum credits/mo | Available packages | Annual per-credit price | Monthly per-credit price |
|------|------------------|-------------------|------------------------|--------------------------|
| **Free** | 0 | None | — | — |
| **Basic** | 1,000 | 1,000 only (no upgrade buckets) | $0.01 | $0.0125 |
| **Standard** | 2,000 | 2,000 / 4,000 / 8,000 | $0.01 | $0.0125 |
| **Pro** | 3,000 | 3,000 / 4,000 / 8,000 / 20,000 | $0.01 | $0.0125 |
| **Enterprise** | Custom | Contact sales | Custom | Custom |

**Package pricing (annual billing):**

| Package | Standard | Pro |
|---------|----------|-----|
| 2,000 credits/mo | $20/mo ($240/yr) | — |
| 3,000 credits/mo | — | $30/mo ($360/yr) |
| 4,000 credits/mo | $40/mo ($480/yr) | $40/mo ($480/yr) |
| 8,000 credits/mo | $80/mo ($960/yr) | $80/mo ($960/yr) |
| 20,000 credits/mo | — | $200/mo ($2,400/yr) |

**Key constraint:** Basic users get 1,000 credits but cannot upgrade to a larger bucket — they are stuck at 1,000. Only Standard and Pro can scale credit purchases.

### Credit consumption rates

Rates per the AI Feature Catalog ([support.monday.com](https://support.monday.com/hc/en-us/articles/24047211522194-AI-Feature-Catalog), checked 2026-09-26):

| Capability | Credits |
|---|---|
| AI blocks | 8 per action. All actions on the same item within 24h count once; subitems count separately |
| AI Notetaker | 120 per meeting hour |
| Sidekick | ~10–30 / 30–80 / 80–150 / 150+ per message, by complexity |
| Agents | ~10–50 / 50–150 / 150–250 / 250+ per task (a run can include several tasks) |
| Vibe build | ~10–20 (Flash) / ~30–50 (Sonnet, default) / ~50–500 (Opus) per message |
| AI workflows | Varies per run |
| Smart Call (CRM) | 5 per connected minute |

- **Plain-language translation — use this in UI:** "1,000 credits can cover roughly 50 resume screenings, 5 hours of meeting summaries, and hundreds of automated workflow updates" (official pricing-page line). The meeting figure is conservative against the 120/hr rate (≈8 hours).
- **Do not use "1 credit ≈ 1 AI action".** The rate card contradicts it: one AI block action is 8 credits. (Earlier versions of this file recommended it.)
- A typical 3-person team uses ~800–1,200 credits/month

### Cadence and rollover

- Credits are a **monthly allotment tied to the account's billing cycle**, not the calendar month. Annual-billed plans still show "AI credits / month" on the pricing page, so the allotment is monthly. Explicit written rule: **not published — confirm internally**.
- **Unused credits do not roll over** — official only for Notetaker ("rollover hours are not included"). The general rule, and whether mid-cycle top-ups expire at reset: **not published — confirm internally**.

### Top-ups

- Admins buy more via Administration > AI governance > Credits Usage > **Buy more credits**, by moving up to the next bucket without changing seat count. Pricing page: "Need more? Add credits anytime."
- **No auto top-up by default.**
- One-time credit packs, pay-as-you-go / overage billing, and auto top-up: **not published — confirm internally**. Until confirmed, a top-up surface sells the next bucket, not a one-time pack.

### Credit depletion behaviour

- **Notification at 80% and 100%:** admins are the named recipients. Whether ICs are notified: **not published — confirm internally**.
- **Grace period at 100%:** "some of your AI capabilities will continue running for a short period after the limit is reached" (official). Grace length and which capabilities get it: **not published — confirm internally**.
- **After the grace period:** paid AI capabilities pause until credits are added or the next billing cycle resets.
- **Free AI features keep working** (Formula Builder, Updates assistant, Docs assistant, prompt-to-board, AI templates, MCP, etc. — see the AI Feature Catalog).
- **State preservation:** platform does not natively save agentic task state on depletion — this is a UX gap the squad should address in surface design

### Pooling, admin and IC controls

- **One account-level pool** shared by all users and capabilities.
- **Admin limits:** account-wide, per capability (each labelled Hard or Soft), and per user or department via User limit policies (AI governance > Usage limits). Enterprise adds role- and workspace-level AI permissions.
- **Admin:** purchases credits, monitors usage via AI governance section in Administration
- **IC (individual contributor):** consumes credits, sees depletion, cannot self-purchase
- Every credit depletion surface must include a "notify admin" path for ICs

Sources: [AI Credits](https://support.monday.com/hc/en-us/articles/29544502265746-AI-Credits) · [Pricing model for monday AI portfolio](https://support.monday.com/hc/en-us/articles/35277848309394-The-pricing-model-for-monday-AI-portfolio) · [AI Models and Credits](https://support.monday.com/hc/en-us/articles/36207944364434-AI-Models-and-Credits-understanding-and-optimizing-consumption) · [AI Permissions and Governance](https://support.monday.com/hc/en-us/articles/30934592475410-AI-Permissions-and-Governance) · [AI Notetaker](https://support.monday.com/hc/en-us/articles/28017211500434-monday-com-AI-Notetaker) · [Smart Call AI credits](https://support.monday.com/hc/en-us/articles/38017810762770-monday-Smart-Call-AI-credits) · [monday.com/pricing](https://monday.com/pricing). Checked 2026-09-26.

---

## Feature gating by tier

Key features relevant to monetization surfaces. This is not exhaustive — verify against monday.com/pricing for the full current list.

| Feature | Free | Basic | Standard | Pro | Enterprise |
|---------|------|-------|----------|-----|------------|
| Seats | 2 max | 3+ | 3+ | 3+ | 3+ |
| Boards | 3 | Unlimited | Unlimited | Unlimited | Unlimited |
| Items | 1,000 total | Unlimited | Unlimited | Unlimited | Unlimited |
| Storage | 500MB | 5GB | 20GB | 100GB | 1TB |
| Activity log | 1 week | — | 6 months | 1 year | 5 years |
| Automations | None | None | 250/mo | 25,000/mo | 250,000/mo |
| Integrations | None | None | 250/mo | 25,000/mo | 250,000/mo |
| Timeline / Gantt / Calendar | None | None | ✓ | ✓ | ✓ |
| Guest access | None | None | 4 guests = 1 seat | Unlimited guests | Unlimited guests |
| Dashboards | None | 1 board | 5 boards | 20 boards | 50 boards |
| Time tracking | None | None | None | ✓ | ✓ |
| Private boards | None | None | None | ✓ | ✓ |
| AI credits | None | 1,000 (fixed) | 2,000–8,000 | 3,000–20,000 | Custom |
| AI Blocks | None | None | None | ✓ | ✓ |
| AI Sidekick Lite | None | None | ✓ (5 msg/user/day)¹ | ✓ (5 msg/user/day)¹ | — |
| AI Sidekick Plus | None | None | Add-on | Add-on | ✓ (100 msg/user/day) |
| SSO | None | None | None | ✓ | ✓ |
| SAML 2.0 | None | None | None | None | ✓ |
| HIPAA compliance | None | None | None | None | ✓ (with BAA) |
| Dedicated CSM | None | None | None | None | ✓ |
| Uptime SLA | None | None | None | None | 99.9% |

¹ Possibly stale: current docs meter Sidekick per message in credits (see Credit consumption rates). Confirm with the file owner before citing.

---

## Trial

- **Length:** 14 days
- **Trial tier:** Pro plan (users experience the full Pro feature set)
- **Extension:** trial can't be extended (official — [free trial article](https://support.monday.com/hc/en-us/articles/360010594079-All-about-the-monday-com-free-trial))
- **AI credits in trial:** credit amount for a new 14-day trial is **not published — confirm internally**. Plan-type articles still show a one-time 6,000-credit grant (12,000 Enterprise) in legacy "add-on" wording; third-party sources describe it as the May–July 2026 migration grant, not a trial allowance.
- **NT time-and-credits trial:** the No-Touch 1,500-credit dual-gated trial (ends at day limit or credit limit, whichever comes first) has **no public documentation — confirm internally**. Treat as internal-only: never state it in external-facing copy.
- **Credit card required:** No — trial starts without payment details
- **Conversion trigger:** Trial expiry or manual upgrade during trial
- **Post-trial default:** User must choose a plan; no auto-downgrade to Free without user action

---

## User cohorts

Always identify which cohort a surface addresses — the hook and trigger logic differ fundamentally.

### New users / trial cohort
- In their 14-day Pro trial
- Haven't paid yet; haven't necessarily hit the aha moment
- **Urgency lever:** applies — trial has a defined end date
- **Copy angle:** loss framing ("keep what you've built"), time pressure ("3 days left")
- **Risk:** asking before aha moment tanks conversion — show proof of value first
- **Aha moment signals:** first automation created, first AI action completed, first team member invited

### Existing users — credit depletion cohort
- Paying customer on Standard or Pro who has consumed their monthly credits
- Know the product; have established workflows at risk
- **Urgency lever:** does not apply — they're a customer, not a prospect
- **Copy angle:** capability framing ("your agent has paused", "top up to resume")
- **Risk:** blocking or alarming them mid-task damages trust and drives churn

### Existing users — tier limit cohort
- Paying customer who has hit a plan limit (automation cap, seat cap, feature gate)
- Knows the product; experiencing specific friction
- **Copy angle:** capability gap ("unlock X to do Y"), not urgency
- **Appropriate surfaces:** inline nudge within the feature area, not full-screen modal

### B2B PLG split (applies to all existing user cohorts)
- **IC (individual contributor):** experiences the friction, wants to keep working, cannot purchase
- **Admin:** makes the purchase decision, may be unaware the IC hit a limit
- Every surface that blocks an IC must include a **"Notify admin"** path
- Copy speaks to the IC's experience; the secondary action handles the buyer

---

## Monetization surfaces inventory

Active surfaces as of last update. Update this list when surfaces ship, change, or are sunset.

| Surface | Trigger | Tier targeted | Cohort | Status |
|---------|---------|--------------|--------|--------|
| Pricing page | Direct navigation or in-app "See plans" | All | New users | Live |
| Trial expiry modal | Day 14 of trial | Free→Pro | New user | Live |
| Feature gate | User clicks locked feature | Free, Basic | New + existing | Live |
| Credit depletion | 80% / 100% credit usage | Standard, Pro | Existing | Live (notification only — no dedicated depletion UX as of last update) |
| Seat expansion | Team invite at seat limit | All paid | Existing | Live |
| Automation limit nudge | 250 automation cap hit on Standard | Standard | Existing | Live |

**Gaps to address (design opportunities):**
- No dedicated credit depletion surface — only admin email notifications at 80%/100%. No IC-facing in-product UX. High priority.
- No mid-trial activation nudge — trial users who haven't hit the aha moment get no in-product prompt before expiry.

---

## Design system — Vibe

All monday.com UI uses the Vibe design system. Apply these constraints in every spec and review.

- **Token binding required:** All colours, typography, and spacing must reference Vibe tokens — never hardcoded hex/px values
- **Flag hardcoded values** as a design system issue in every spec and review
- **Tier colour associations** (check Vibe docs for current values):
  - Free: neutral grey
  - Basic: blue
  - Standard: teal/green
  - Pro: purple / gradient
  - Enterprise: dark / premium
- **AI colour:** AI features use a distinct accent — verify current token in Vibe docs before speccing
- **Component library:** use existing Vibe components before designing custom ones

---

## Squad context

- **Squad:** Growth Monetization
- **Primary metric:** Free→Pro conversion rate (self-serve)
- **Secondary metrics:** Standard→Pro expansion, credit top-up conversion, trial activation rate
- **Current focus (as of last update):** AI credit monetization surfaces — the credit depletion UX gap is the top design priority
- **Key constraint:** Agentic task flows must not be blocked without state preservation — this is a product and UX requirement, not just a design preference

---

## Changelog

| Date | What changed | Updated by |
|------|-------------|-----------|
| 2026-09-26 | Credit rates from the AI Feature Catalog; dropped "1 credit ≈ 1 AI action"; added cadence/rollover, top-ups, pooling and admin limits, grace period, trial extension and NT trial status; flagged Sidekick Lite row | Claude (growth-monetization plugin) |
| 2026-09-24 | Initial version created from public pricing research | Claude (growth-monetization plugin) |

*Add new entries at the top of this table when updating.*
