# Promotions — CRO playbook

Surface type 3: discounts, limited-time offers, annual upsells, bundles and cross-sells, seasonal pricing, referral and milestone rewards. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks). Cohort: both — the offer and its framing differ for new and existing users.

## Core rule

Only use urgency when the deadline is real, and anchor every offer to the genuine regular price. Promotions train users: run them too often or too deep and the cohort learns to wait. The goal is urgency without dependency — an offer that feels like a reward for a specific moment, not a standing discount.

## Patterns

### Anchoring — always

Show the genuine regular price next to the offer: `~~${list}/mo~~ ${offer}/mo — save {N}%`, plus the annual saving in dollars and the offer's real end date. The anchor must be the price the product actually sells at — an inflated "was" price is a legal risk as well as a trust one (see *Legal context*).

### Urgency — only real deadlines

Real urgency: an actual campaign end date; an actual quantity limit; a lifecycle moment ("for your first renewal only"); a usage milestone. A countdown that restarts on refresh is the textbook fake — the UK regulator uses it as its example of a banned practice (see *Legal context*).

Figma announced its AI-credit enforcement on December 9, 2025 — about 14 weeks ahead — put the credit add-on on sale on March 11, 2026, and enforced limits on March 18, 2026 [Verified — [Figma blog](https://www.figma.com/blog/updates-to-ai-credits-in-figma/)]: the fix was available a week before the pain. Forum complaints about the limits show the lead time didn't remove the friction [Reported — [Figma forum](https://forum.figma.com/share-your-feedback-26/figma-make-ai-credit-limits-not-feasible-51713/index2.html)].

### Targeting — who sees the offer matters more than the offer

| Segment | Best offer type |
|---|---|
| New user, before the aha moment | Extend the trial — reduce friction, not price |
| New user, after the aha moment | A first-renewal discount with a real deadline |
| Existing loyal user | A reward tied to a milestone, not a discount |
| Existing at-risk user | Downgrade or pause before any discount ([cancellation.md](cancellation.md)) |
| Lapsed, win-back | A return offer plus what's new since they left |

Don't show a promotion during onboarding, or to users who already converted without it.

### A price change is a promotion problem

When prices rise or AI moves into a tier, the cohort below decides whether it reads as "more value" or "a penalty".

- **Slack, 2025:** announced June 17, 2025 — Business+ went from $12.50 to $15 per user/month (annual) at each customer's first renewal after August 17, 2025, and the standalone AI add-on was retired; Slack framed it as reflecting "the significant value added through new advanced AI capabilities and premium Salesforce integrations" [Verified — [Slack](https://slack.com/blog/news/june-2025-pricing-and-packaging-announcement)]. For most existing Business+ customers it was a 20% increase; those who had also paid for the AI add-on paid less overall.
- **Salesforce, 2025:** an average 6% list increase effective August 1, 2025 on Enterprise and Unlimited editions of Sales, Service, Field Service and select Industries clouds; no changes for Foundations, Starter or Pro [Verified — [Salesforce](https://www.salesforce.com/news/stories/pricing-update-2025/)]. Sparing the smaller plans likely protects the price-sensitive growth cohort (inference).
- **Notion, 2025:** see [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling) — existing add-on subscribers were grandfathered, which is the promotional lever that softens a forced migration.

### Stacking — define it every time

Every promotion spec answers: Does it combine with the annual discount? With nonprofit, education or startup pricing? Does a user who had a prior promotion see this one? When two run at once, which wins? Linear's program discounts show why this matters — 100% for full-time students, 75% for university staff and nonprofits, and up to 6 months of Business free through startup partners [Verified — [Linear docs](https://linear.app/docs/billing-and-plans)].

### Measurement — redemption rate is the wrong metric

Redemption counts who took the offer, not whether the offer caused the purchase.

1. **Holdout:** a share of the eligible audience sees no offer; compare conversion against it.
2. **Incrementality:** the lift over the holdout, not the absolute redemption rate.
3. **Retention of the discounted cohort** at 90 and 180 days — track it; a discount that converts people who churn later isn't a win.
4. **Test the minimum effective discount.** In one consumer cancel-flow test, 40% off performed almost identically to 50% [Verified — [TouchNote / Chargebee](https://www.chargebee.com/customers/touchnote/)]; that was an A/B of offer variants, not a holdout.

### Copy patterns

- **Discount headlines:** "Get {plan} for {N}% less — until {date}" · "Your {N}-day offer: {plan} at ${X}/mo" · "You've earned a discount" (milestone-triggered) · "{feature} just got better — upgrade at a special rate".
- **Urgency without manipulation:** the exact expiry ("Offer ends {date} at midnight"); session-bound offers ("available while you're here"); avoid vague pressure like "Act now before it's too late".
- **Personal beats generic:** an offer triggered by the user's own moment — "you've been on the free plan for 30 days", a usage milestone, a return visit — reads as a reward; a site-wide banner reads as a sale.

These are patterns for `improve-conversion-surfaces-copy`, not final copy.

### Formats

| Format | Best for | Note |
|---|---|---|
| Full-screen modal | A high-value offer (annual upgrade, a big discount) | Highest attention, highest annoyance — use sparingly |
| Top-of-app banner | A persistent, dismissible reminder | Awareness more than conversion |
| In-context card | Triggered at a relevant moment (feature use, approaching a limit) | Best signal-to-noise |
| Email + in-app | Coordinated campaigns | Email builds awareness, in-app closes |
| Add-on at purchase | Cross-sell while the user is already buying | The easiest upsell moment |

One offer, one CTA; if several plans appear, pre-select the recommended one.

### Annual plan upsell

The monthly → annual move is the core B2B promotion.

- **When:** at plan selection (the toggle, with the saving highlighted); after the first month on monthly ("you've done {X} — lock in the year"); at the renewal reminder.
- **How:** the monthly equivalent billed annually, the dollars saved vs. staying monthly, one click with the payment method on file. A cancellation or refund guarantee reduces commitment anxiety — only if one actually exists.

## Legal context — guidance, not legal advice

**Reviewed by legal: not yet.** These rules protect **consumers**; monday's team buyers are mostly B2B, which falls under separate misleading-marketing law (e.g. the UK Business Protection from Misleading Marketing Regulations 2008, EU Directive 2006/114/EC — not verified here; flag for legal).

| Rule | What it says | Source |
|---|---|---|
| UK — DMCC Act 2024 s.226 | Bans misleading actions, including false or misleading price information relevant to a purchase decision | [s.226](https://www.legislation.gov.uk/ukpga/2024/13/section/226) [Verified] |
| UK — DMCC Act Sch. 20 para 7 | Bans falsely stating a product is available only for a limited time; the CMA's guidance gives restarting countdown timers as an example | [Sch. 20](https://www.legislation.gov.uk/ukpga/2024/13/schedule/20), [CMA207](https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices) [Verified] |
| EU — Price Indication Directive Art. 6a | A price reduction must be measured against the lowest price in the prior 30 days — for **goods**; SaaS reference prices fall under the UCPD's misleading-action rules instead | [Reported] — [HSF Kramer on CJEU C-330/23](https://www.hsfkramer.com/notes/ip/2024-posts/cjeu-confirms-that-price-reduction-claims-must-be-based-on-lowest-price-in-last-30-days); EUR-Lex not read |

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

**What they ship [Reported — press and deal-site coverage].** March 13–27, 2026: usage limits doubled outside weekday peak hours (8 AM–2 PM ET) for Free, Pro, Max, and Team; applied automatically with no action needed; the bonus didn't count against weekly limits; Enterprise excluded. Framed publicly as a thank-you to users. An earlier holiday doubling ran Dec 25–31, 2025 for paid plans. Annual Pro ($17/mo) is the only standing discount; the Help Center says Support can't issue one-off discounts or coupons. Model-launch credit grants are also reported **[Reported]**.

**Why it works.** The promotion shifts load to off-peak capacity (cheap to give) while generating goodwill (valuable to receive). Automatic enrollment means 100% reach with zero friction. Stated end date = real scarcity, no countdown gimmicks.

**Where it breaks.** Third-party coverage reports that claiming a model-launch credit quietly enabled usage credits for some Pro users, who were then billed past plan limits instead of rate-limited; enrollment behavior was changed after backlash **[Reported]**. Lesson: a promotion must never change a billing setting as a side effect.

**Steal for monday.com.** (1) Off-peak or weekend credit multipliers for agent runs — cheap capacity, real goodwill, and it teaches scheduling. (2) No-coupon policy for self-serve keeps list price credible. (3) Hard rule for every credit promo spec: claiming it changes no billing setting, and the spec must say so.

### Copy bank — AI promotions

| Promo | Pattern | Example for monday.com |
|---|---|---|
| Capacity promo | Specific window + automatic | "Double credits on weekend agent runs, [date]–[date]. Nothing to turn on." |
| Annual as balance | Today's balance, not savings | "Go annual — get all {N} credits today" (only if annual credits arrive upfront — not stated in the context file) |
| Beta disclosure | Cost stated upfront | "Free while in beta. After launch, about [X] credits per run." |
| One-time grant | Tie to first action | "Your first {N} AI credits are on us — try them on this board" (only if a grant exists) |
| Thank-you framing | Reason + end date | "A thank-you for being early: extra credits through [date]" |

### Sources (checked 2026-09-24)

- Clay: https://www.landbase.com/blog/clay-pricing · https://www.clay.com/blog/introducing-clay-pricing-3-0-the-most-flexible-credit-system-on-the-market · https://astragtm.io/guides/clay-pricing-2026
- Figma: https://www.figma.com/blog/updates-to-ai-credits-in-figma/ · https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ
- ClickUp: https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits · https://agiled.app/blog/clickup-pricing
- Claude: https://www.engadget.com/ai/anthropic-is-doubling-claudes-usage-limits-during-off-peak-hours-for-the-next-two-weeks-163645928.html · https://slickdeals.net/f/19306695-anthropic-claude-code-usage-promotion-2x-usage-outside-8-am-2-pm-et-5-11-am-pt · https://blog.nachonacho.com/best/claude-promo-codes/ · https://ccforeveryone.com/guides/claude-code-limits-and-pricing

## Anti-patterns

| Anti-pattern | Why it fails | Who did it |
|---|---|---|
| A countdown that restarts on reload | Trust collapses when noticed; banned for consumers in the UK | The CMA's own example [Verified] |
| "Last chance" with no real deadline | A dark pattern and a legal risk for consumer offers | Common |
| A discount without the genuine original price | No anchor, no perceived value | Common |
| An inflated "was" price | Misleading pricing; legal risk | Common |
| The same discount every time the user visits pricing | Trains users to wait | Common |
| A discount shown to loyal users who'd renew anyway | Trains the high-value cohort to expect discounts | Common |
| An offer during onboarding | Before the aha moment the user hasn't felt the value | Common |
| The maximum discount by default | Lost margin if a smaller one works as well | TouchNote found 40% ≈ 50% (one consumer case) [Verified] |
| Measuring redemption instead of incrementality | Can't prove the offer caused anything | Common |
| No stacking rules | Users get two discounts, or the wrong one | Common |
| A usage-model change explained unclearly | Trust collapse, refunds | [case: cursor-2025-pricing](cases.md#cursor-2025-pricing) |

## monday.com-specific notes

- **AI credits as the reward:** "{N} bonus AI credits with the annual upgrade" is more tangible than "2 months free". Credit packages and prices per [monday-context.md](../context/monday-context.md).
- **Cross-product promotions** (e.g. a CRM add-on for existing Pro users) lead with the job to be done, not the price.
- **AI launch windows:** a time-bound, milestone-anchored offer for existing users to move up and unlock more AI — with a real end date.
- **Annual is already the default** on monday's pricing page (~18% saving) — promotions work on the monthly → annual move at renewal and inside the product.
- **Consumer vs. B2B:** monday sells to both; for consumer buyers, the UK and EU rules above apply. Legal review before shipping any price-anchored or time-limited offer.

## Sources

Checked 2026-09-24 (AI-native set) and 2026-09-25 (everything else).

- Figma: https://www.figma.com/blog/updates-to-ai-credits-in-figma/ · https://forum.figma.com/share-your-feedback-26/figma-make-ai-credit-limits-not-feasible-51713/index2.html
- Slack: https://slack.com/blog/news/june-2025-pricing-and-packaging-announcement · https://slack.com/help/articles/39264531104275-Updates-to-feature-availability-and-pricing-for-Slack-plans
- Salesforce: https://www.salesforce.com/news/stories/pricing-update-2025/
- Linear: https://linear.app/docs/billing-and-plans
- TouchNote (Chargebee): https://www.chargebee.com/customers/touchnote/
- UK: https://www.legislation.gov.uk/ukpga/2024/13/section/226 · https://www.legislation.gov.uk/ukpga/2024/13/schedule/20 · https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices
- EU: https://www.hsfkramer.com/notes/ip/2024-posts/cjeu-confirms-that-price-reduction-claims-must-be-based-on-lowest-price-in-last-30-days
