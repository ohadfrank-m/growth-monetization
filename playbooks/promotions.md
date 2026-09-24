# Promotions — CRO playbook

Surface type 3. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

## What counts as a promotion
- Discount modals (% off, $ off)
- Limited-time upgrade offers
- Annual plan upsell banners
- Bundle / cross-sell offers
- Black Friday / seasonal pricing
- Referral reward redemption screens
- "You've unlocked X" reward moments

## Core tension in promotions
Promotions train users. Run them too often or too deep and you teach the cohort to wait for discounts. The goal is *urgency without dependency*.

**The rule:** Promotions should feel like a lucky moment, not an expected tactic. If users know the discount is always there, it loses all lift.

## Promotion design principles

### 1. Real scarcity over fake scarcity
- Countdown timers work — but only if the offer genuinely expires
- "Limited time" with no end date = dark pattern = trust erosion
- Seat-based scarcity ("Only 3 slots left at this price") works best when true

### 2. Anchor the savings
- Show the full price crossed out: ~~$24/mo~~ → **$16/mo**
- Show annual savings as a dollar amount: "Save $96/year"
- Show both monthly equivalent AND annual total — let the user do the math they prefer

### 3. Make the offer feel personal
- "We noticed you've been on the free plan for 30 days — here's a one-time offer" converts better than a generic banner
- Trigger-based promotions (usage milestone, return visit, feature exploration) outperform time-based by 2–3x

### 4. One offer, one CTA
- Promotion modals with multiple options convert worse than single-offer modals
- If you need to offer multiple plans, default-select the recommended one

## Promotion formats

| Format | Best for | CVR notes |
|--------|---------|-----------|
| Full-screen modal | High-value offer (annual upgrade, big discount) | Highest CVR but highest annoyance — use sparingly |
| Banner (top of app) | Persistent but dismissible reminder | Low CVR per impression, good for awareness |
| In-context card | Triggered at relevant moment (feature use, limit approach) | Best signal-to-noise ratio |
| Email + in-app | Coordinated campaigns (Black Friday, trial expiry) | Email drives awareness, in-app closes |
| Upgrade confirmation add-on | Cross-sell at point of purchase | Easiest upsell moment — user already in buying mode |

## Copy patterns

**Discount headline formulas:**
- "Get [Plan] for [X]% less — today only"
- "Your [N]-day offer: [Plan] at $X/mo"
- "You've earned a discount" (milestone-triggered)
- "[Specific feature] just got better — upgrade at a special rate"

**Urgency without manipulation:**
- Show exact expiry: "Offer expires May 26 at midnight"
- Use session-bound offers: "This offer is available while you're here"
- Avoid: "Act now before it's too late" — vague and distrusted

## Annual plan upsell (specific pattern)
This is the highest-ROI promotion in B2B SaaS. Targets: monthly → annual conversion.

Best trigger points:
1. At plan selection (toggle with savings highlighted)
2. 30 days after monthly plan start ("You've saved X hours — lock in savings for the year")
3. At renewal reminder (pre-charge email + in-app)

Best offer structure:
- Show monthly equivalent price billed annually
- Show $ saved vs staying monthly
- Offer a 14-day cancellation guarantee to reduce commitment anxiety
- One-click toggle — don't make them re-enter payment

Benchmark: Monthly → Annual conversion rate of 25–40% with well-timed in-app prompt.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Countdown timer that resets on page reload | Destroys trust permanently when users notice |
| Discount available every time user visits pricing | Trains cancellation behavior |
| Offer shown during onboarding | Pre-aha moment — user hasn't felt value yet |
| "Last chance" with no actual deadline | Classic dark pattern, legally risky in some jurisdictions |
| Discount without showing original price | No anchoring = no perceived value |
| Offer shown to users who already converted without it | Wastes the slot, signals sloppy targeting |
| No holdout group | Lift can't be measured |

## Benchmarks

*Directional only — these figures pre-date the evidence-tag standard and carry no source. Don't cite them as fact in a review; the sourced material is in the AI-native reference set below.*

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Discount modal → upgrade CVR | <5% | 8–15% | 20%+ |
| Annual upsell acceptance (in-app) | <10% | 20–30% | 35%+ |
| Banner CTR | <0.5% | 1–2% | 3%+ |

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture before citing in a review.

The pattern across all four: **AI companies promote with capacity, not discounts.** None of them leans on coupon codes. They give more of the unit (credits, usage) or better unit economics, which protects list price and teaches the user the value of the unit at the same time.

### At a glance

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Primary promo lever | Annual (10%) + credits front-loaded | More credits, same price | Sample credits + annual/program discounts | Time-boxed capacity doubling |
| Uses coupons? | No | No | Occasionally (partner/seasonal, reported) | No — Support states it can't issue one-off discounts |
| Signature move | Repricing framed as "data costs dropped 50–90%" | Add-on launched a week *before* enforcement | 1,000 one-time AI credits on paid plans | 2x off-peak, automatic, no opt-in |
| Risk | Grandfathering creates two customer classes | "More credits" can read as a correction | Seasonal discounts train waiting | Promo that touches billing settings (see Claude below) |

### Clay — repricing as the promotion

**What they ship [Verified/Reported].** Annual billing saves ~10% and delivers credits upfront. The March 2026 repricing was positioned around data costs dropping 50–90% across most providers — a value promotion baked into list price. Legacy plans grandfathered indefinitely. Clay published the reasoning for an earlier pricing generation as a public memo. Third-party buyer guides advise negotiating for more credits rather than a lower subscription price.

**Why it works.** A price-change moment is a promotion moment if you lead with "you get more." Front-loading annual credits makes annual feel like a bigger balance today, not only a saving over twelve months.

**Where it breaks.** Indefinite grandfathering leaves a permanent two-class base that every future pricing test has to work around.

**Steal for monday.com.** Annual offer framed as balance: "Go annual — get the full year's credits today." Enterprise discount policy: give credits, not percentage points.

### Figma — promote the fix before the pain

**What they ship [Verified].** Announced AI credit enforcement months ahead (Dec 2025 post), launched the paid shared-credit add-on on March 11, 2026, a week before enforcing seat limits on March 18. On Aug 25, 2026 the add-on was repackaged with more credits for the same price. New AI features (Weave tools, the agent in Figma Design) ran as free open beta before general availability, when they begin consuming credits.

**Why it works.** The add-on arrives *before* the limit bites, so the first depletion moment has a purchase path ready. Free beta builds habit before metering; "more for the same" is a promotion that never needs to be unwound.

**Where it breaks.** Free beta → metered GA is a takeaway. If the GA date and cost aren't announced with the beta, the transition reads as bait-and-switch (Figma's help article commits to publishing the date once known).

**Steal for monday.com.** For every new AI capability: free beta with the GA credit cost stated on day one ("Free during beta. At launch: ~X credits per run"). Launch paid top-ups before any new limit is enforced.

### ClickUp — sampling as the promotion

**What they ship [Verified/Reported].** Paid plans without an AI add-on get 1,000 one-time AI credits per user; Free gets 500 per workspace. A 50% nonprofit discount on Unlimited and Business. Third-party sources report periodic 20–30% annual-upgrade discounts around quarter-end and Black Friday **[Reported — unverified, don't cite as fact]**.

**Why it works.** One-time credits are a promotion the user experiences as product value, not as a deal — and they're gone once used, so no discount dependency.

**Where it breaks.** Seasonal annual discounts (if real) train buyers to wait for Q4.

**Steal for monday.com.** Existing-customer AI launch promo = one-time credit grant tied to the first AI Block or agent setup, not a price cut. It measures itself: grant → first run → depletion → purchase.

### Claude — time-boxed capacity doubling

**What they ship [Verified].** March 13–27, 2026: usage limits doubled outside weekday peak hours (8 AM–2 PM ET) for Free, Pro, Max, and Team; applied automatically with no action needed; the bonus didn't count against weekly limits; Enterprise excluded. Framed publicly as a thank-you to users. An earlier holiday doubling ran Dec 25–31, 2025 for paid plans. Annual Pro ($17/mo) is the only standing discount; the Help Center says Support can't issue one-off discounts or coupons. Model-launch credit grants are also reported **[Reported]**.

**Why it works.** The promotion shifts load to off-peak capacity (cheap to give) while generating goodwill (valuable to receive). Automatic enrollment means 100% reach with zero friction. Stated end date = real scarcity, no countdown gimmicks.

**Where it breaks.** Third-party coverage reports that claiming a model-launch credit quietly enabled usage credits for some Pro users, who were then billed past plan limits instead of rate-limited; enrollment behavior was changed after backlash **[Reported]**. Lesson: a promotion must never change a billing setting as a side effect.

**Steal for monday.com.** (1) Off-peak or weekend credit multipliers for agent runs — cheap capacity, real goodwill, and it teaches scheduling. (2) No-coupon policy for self-serve keeps list price credible. (3) Hard rule for every credit promo spec: claiming it changes no billing setting, and the spec must say so.

### Copy bank — AI promotions

| Promo | Pattern | Example for monday.com |
|---|---|---|
| Capacity promo | Specific window + automatic | "Double credits on weekend agent runs, [date]–[date]. Nothing to turn on." |
| Annual as balance | Today's balance, not savings | "Go annual — get all 36,000 credits today" (use real package from context file) |
| Beta disclosure | Cost stated upfront | "Free while in beta. After launch, about [X] credits per run." |
| One-time grant | Tie to first action | "Your first 500 AI credits are on us — try them on this board" |
| Thank-you framing | Reason + end date | "A thank-you for being early: extra credits through [date]" |

### Sources (checked 2026-09-24)

- Clay: https://www.landbase.com/blog/clay-pricing · https://www.clay.com/blog/introducing-clay-pricing-3-0-the-most-flexible-credit-system-on-the-market · https://astragtm.io/guides/clay-pricing-2026
- Figma: https://www.figma.com/blog/updates-to-ai-credits-in-figma/ · https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ
- ClickUp: https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits · https://agiled.app/blog/clickup-pricing
- Claude: https://www.engadget.com/ai/anthropic-is-doubling-claudes-usage-limits-during-off-peak-hours-for-the-next-two-weeks-163645928.html · https://slickdeals.net/f/19306695-anthropic-claude-code-usage-promotion-2x-usage-outside-8-am-2-pm-et-5-11-am-pt · https://blog.nachonacho.com/best/claude-promo-codes/ · https://ccforeveryone.com/guides/claude-code-limits-and-pricing

## monday.com-specific notes

- AI credits as a promotion vehicle: "Get 500 bonus AI credits free with annual upgrade" is more tangible than "2 months free"
- Cross-product promotions (e.g., CRM add-on at discount for existing Pro users) are high-leverage but require clear value framing — don't lead with price, lead with the job-to-be-done
- For the AI Agents launch window: consider a launch-window promotion for existing users to upgrade and unlock Sidekick — time-bound and milestone-anchored
