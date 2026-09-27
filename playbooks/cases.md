# Case library — stories that span surfaces

Some stories teach something on several surfaces at once. Each is told **once** here, with its evidence, and cited from the playbooks as `[case: {id}]`. The citing playbook adds only the lesson for its own surface. Evidence tags per [README.md](README.md). Checked 2026-09-27.

---

## notion-2025-ai-bundling

**Notion moves full AI into Business, May 2025.**

**What happened.**
- **May 13, 2025, new customers.** Notion AI was bundled into Business and Enterprise and stopped being sold as an add-on to new Free and Plus customers [Verified — [Notion release](https://www.notion.com/releases/2025-05-13)]. Free and Plus now get a limited AI trial [Verified — [pricing](https://www.notion.com/pricing)].
- **Prices.** Business rose from $15 to $20 per member per month (annual). The AI add-on had been $8 annual / $10 monthly, so Plus + AI went from $18 to $20 on annual billing [Reported — [Notion help, 2025 pricing changes](https://www.notion.com/help/2025-pricing-changes), [usecarly](https://www.usecarly.com/blog/notion-ai-pricing-change/)].
- **Existing customers.** The change applied at their next renewal on or after August 13, 2025, about three months' notice, and existing AI add-on subscribers were grandfathered [Reported].
- **What the jump bundles.** Business includes SAML SSO and advanced admin controls; audit log is Enterprise-only [Verified — [pricing](https://www.notion.com/pricing)].
- **Downgrading.** When a workspace downgrades, Custom Agents are "switched off, but not deleted" [Verified — [Notion help](https://www.notion.com/help/plan-downgrade)].
- **How users reacted.** Community advice was summarised by a review site as "stay on Plus and use ChatGPT's free tier for AI" [Reported — [aitooldiscovery](https://www.aitooldiscovery.com/guides/notion-ai-reddit)]. That is a paraphrase, not a quote.

**The mechanism.** A gate moved by a packaging decision, not by the user's growth. A buyer who wanted only AI had to take a tier of features they didn't need, and Business teams without AI paid more for the same product.

| Playbook | Lesson there |
|---|---|
| [paywalls.md](paywalls.md) | A gate at the wrong granularity: the minimum purchase should match the value wanted |
| [upgrade-triggers.md](upgrade-triggers.md) | Limits moved by packaging read as a penalty; limits tied to growth events feel earned |
| [pricing-pages.md](pricing-pages.md) | When AI moves up a tier, the page must justify the jump on AI value alone |
| [promotions.md](promotions.md) | Grandfathering is the promotional lever that softens a forced migration |
| [cancellation.md](cancellation.md) | "Switched off, not deleted" is the honest promise for AI features at downgrade |

---

## cursor-2025-pricing

**Cursor's usage-model change and apology, June–July 2025.**

**What happened.**
- **June 16, 2025.** Cursor replaced Pro's 500 fast requests with $20 of frontier-model usage per month at API prices. The list price didn't change.
- **The misunderstanding.** "Unlimited" applied only to Auto mode, and users ran into unexpected charges.
- **July 4, 2025.** Cursor apologised ("not communicated clearly… we take full responsibility") and refunded unexpected usage from June 16 to July 4 [Verified — [Cursor blog](https://cursor.com/blog/june-2025-pricing); [TechCrunch](https://techcrunch.com/2025/07/07/cursor-apologizes-for-unclear-pricing-changes-that-upset-users/)].
- **What was new.** The usage dashboard and spend limits already existed. The fix added visibility of approaching limits.
- **Carry-over.** Included usage doesn't roll over [Verified — [Cursor help](https://cursor.com/help/models-and-usage/usage-limits)].

**The mechanism.** It wasn't a price increase. It was a change to what the price bought, explained in words ("unlimited") the mechanics didn't back up. Opacity cost more trust than the money involved.

| Playbook | Lesson there |
|---|---|
| [credit-ui.md](credit-ui.md) | Never let a word like "unlimited" do work the metering doesn't support |
| [upgrade-triggers.md](upgrade-triggers.md) | Let the admin set the ceiling, and say exactly what stops at it |
| [pricing-pages.md](pricing-pages.md) | A billing-model change needs its own explanation on the page |
| [promotions.md](promotions.md) | A change to what the price buys is a price change in the customer's eyes |

---

## ftc-cancellation-enforcement

**US enforcement against obstructed cancellation: Amazon and Adobe.**

**What happened.**
- **Amazon, Sept 25, 2025.** A $2.5B settlement with the FTC: a $1B civil penalty, which the FTC calls the largest ever in a case involving an FTC rule violation, plus $1.5B in refunds to about 35M consumers [Verified — [FTC](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon)]. The FTC's 2023 complaint says Amazon used the term "Iliad" for the Prime cancel process [Verified — [FTC, June 2023](https://www.ftc.gov/news-events/news/press-releases/2023/06/ftc-takes-action-against-amazon-enrolling-consumers-amazon-prime-without-consent-sabotaging-their)]. The settlement contains no admission.
- **Adobe, March 13, 2026.** A $150M stipulated order with DOJ: a $75M civil penalty plus $75M in free services, with requirements to disclose early-termination fees, remind users before trials convert, and make cancellation easy [Verified — [DOJ](https://www.justice.gov/opa/pr/adobe-agrees-150-million-settlement-and-injunction-resolve-alleged-violations-restore-online)].
- **What Adobe was alleged to have done.** Buried an early-termination fee of 50% of the remaining payments on "annual, paid monthly" plans, and made cancellation take many pages and agent transfers [Verified — [FTC, June 2024](https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling); allegations]. One employee described the fee as "a bit like heroin for Adobe"; Adobe says that employee was not an executive [Reported — [The Register](https://www.theregister.com/2024/07/25/adobe_subscription_cancel_fees_ftc/)].
- **The rule.** The FTC's Click-to-Cancel rule was vacated by the 8th Circuit on July 8, 2025 [Reported — [Sidley](https://www.sidley.com/en/insights/newsupdates/2025/07/us-ftc-click-to-cancel-rule-struck-down)]. Enforcement continues case by case under existing law.

**The mechanism.** Every screen that exists only to create friction, and every fee hidden at signup, is now a quantified legal and reputational liability, not just bad UX. These are consumer cases; monday's B2B team plans are largely outside these rules, but its consumer buyers are not.

| Playbook | Lesson there |
|---|---|
| [cancellation.md](cancellation.md) | Cancel reachable in plain steps; offers shown alongside the way out; fees disclosed at signup |
| [promotions.md](promotions.md) | Terms that surprise at cancellation, such as early-termination fees, are an enforcement target |

---

## hubspot-2025-credits-ratchet

**HubSpot Credits: pause by default, auto-upgrade once you've bought more, 2025–2026.**

**What happened.**
- **Credits per edition.** Seat-based HubSpot subscriptions include monthly credits: Starter 500, Professional 3,000, Enterprise 5,000. Rates are published per action: 50 credits per resolved Customer Agent conversation, 100 per Prospecting Agent lead recommendation, 10 per workflow AI action [Verified — [HubSpot catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog)].
- **Buying more.** Capacity packs cost $10 per 1,000 credits a month for the rest of the term, or pay-as-you-go at $0.010 per credit [Verified — [HubSpot catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog)].
- **June 2, 2025.** Breeze Customer Agent opened to all Pro and Enterprise customers across Hubs, paid through credits [Verified — [HubSpot news](https://www.hubspot.com/company-news/customer-agent-expansion)]. Existing Service Hub customers moved to credit billing for it on August 4, 2025 [Reported — HubSpot IR release seen via search; the page returned 403].
- **The two defaults.** Without a capacity pack, credit features "pause until your next reset date". Once a pack has been bought, the default flips: at the limit, the account "will automatically be upgraded to include a higher HubSpot Credits capacity pack", and packs can only be reduced "at the end of your contractual commitment term". Pay-as-you-go overage is the opt-in alternative. Unused credits don't roll over. Alerts fire at 75%, 85%, 90% and 100% [Verified — [HubSpot KB](https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing)].
- **April 14, 2026.** Customer Agent moved to $0.50 per resolved conversation (from $1.00 per conversation), and Prospecting Agent to $1.00 per recommended lead (from a recurring monthly charge) [Verified — [HubSpot news](https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete)].
- **Customer reaction** to the auto-upgrade default wasn't captured from a readable source [Teardown needed].

**The mechanism.** A ratchet. A single spike month after the first top-up moves the account to a higher pack for the rest of the contract. The account is upgraded without the admin making an upgrade decision, and it can't be reversed until renewal. The pause-by-default path for accounts that never bought extra is the safe version of the same wall.

| Playbook | Lesson there |
|---|---|
| [credit-ui.md](credit-ui.md) | Default behaviour at the limit is a design decision: pause, overage, or auto-upgrade. Say which on the meter, and never let buying once silently change it |
| [upgrade-triggers.md](upgrade-triggers.md) | An automatic upgrade is a trigger with no decision in it; the payer should opt in, with the cost for the rest of the term shown |
| [pricing-pages.md](pricing-pages.md) | Publishing the rate sheet and outcome-based units makes credits comparable; the auto-upgrade default belongs on the page too |
| [cancellation.md](cancellation.md) | Reductions allowed "only at the end of the term" are a notice window by another name; a right-size offer must be available when the customer asks |

---

## atlassian-2025-rovo-bundle-then-meter

**Atlassian bundles Rovo into paid Cloud plans (2025), then meters it with default-on overage (2026).**

**What happened.**
- **April 9, 2025.** Rovo became "available at no additional upfront cost" to organisations with active Standard, Premium and Enterprise Cloud subscriptions [Verified — [Atlassian support](https://support.atlassian.com/rovo/kb/understand-rovo-billing-and-managing-costs-in-atlassian-cloud/)]. Premium and Enterprise were enabled from April to July 2025 and Standard later in 2025 [Reported — Atlassian support text seen via search].
- **The allowance.** Credits per user per month, pooled across the org: Jira and Confluence get 25 (Standard), 70 (Premium) and 150 (Enterprise); Service and Teamwork Collections get 250, 700 and 1,500. Allowances refresh monthly and don't roll over. Search, definitions and summaries are free; chat and agents consume credits by complexity [Verified — [Rovo credits](https://support.atlassian.com/rovo/docs/rovo-usage-limits/), [Rovo plans](https://www.atlassian.com/licensing/rovo)].
- **December 3, 2026.** Extra-usage billing takes effect at $0.01 per credit ($10 per 1,000). **Extra usage is on by default**, with admin-set spending caps. With it off, billable interactions "pause until the credit allowance resets". Admins are alerted at 80% and 100% [Verified — [Rovo credits](https://support.atlassian.com/rovo/docs/rovo-usage-limits/)]. The change was announced around September 1, 2026 [Reported — third-party coverage, e.g. [SPK](https://www.spkaa.com/blog/atlassian-is-changing-how-you-pay-for-usage-what-you-need-to-know)].

**The mechanism.** Bundle first, meter later. Including Rovo in every paid plan removed the add-on purchase decision and drove adoption. The meter then arrived with the allowance set by tier and overage switched on. With overage on by default, the first depletion shows up as a bill, not a wall, unless an admin set a cap. Keeping search and summaries free protects the everyday habit, and the metering falls on the agentic work.

| Playbook | Lesson there |
|---|---|
| [paywalls.md](paywalls.md) | Free for the habit (search, summaries), metered for the agentic job: the gate falls on the expensive work, not the everyday feature |
| [credit-ui.md](credit-ui.md) | Default-on overage needs a visible cap and a clear line between free and metered actions, or the first overage feels like a surprise charge |
| [upgrade-triggers.md](upgrade-triggers.md) | An allowance that grows with the tier (25 → 70 → 150) makes the next tier an AI-capacity argument |
| [pricing-pages.md](pricing-pages.md) | State the per-user allowance by tier, and that it pools at the org level |
| [promotions.md](promotions.md) | "Included at no extra cost" followed by metering is a takeaway: announce the metered terms with lead time, and say from launch that metering will come |

---

## asana-2025-ai-studio-credits

**Asana AI Studio: pooled credits on every paid plan, then a large first paid step, 2025.**

**What happened.**
- **Included.** AI Studio Basic is included on Starter, Advanced, Enterprise and Enterprise+, with credits **per billing account per month**, not per seat: 50K (Starter), 75K (Advanced), 200K (Enterprise and Enterprise+) [Verified — [Asana pricing](https://asana.com/pricing)].
- **August 11, 2025.** AI Studio Plus, previously sales-only, opened to direct purchase. It starts at $1,620 a year, follows the base plan's billing cadence, and scales "up to 1M credits"; Basic credits stack with Plus credits [Verified — [Asana staff announcement](https://forum.asana.com/t/introducing-ai-studio-plus-for-direct-purchase/1085642)].
- **Package shapes.** Plus includes 100,000 credits that reset monthly, with extra in 100,000 increments, or 1.2M credits valid for the annual term. Pro is 20M credits a year [Reported — Asana help-center text seen via search; the page didn't render].
- **Reaction.** In an October 2025 community thread, a customer on Advanced calculated AI Studio's cost against their usage and called it expensive next to Asana's free AI features. No Asana staff reply appears in the thread [Reported — [Asana forum](https://forum.asana.com/t/price-of-ai-studio-plus-seems-a-little-expensive/1102187)].

**The mechanism.** Pooled, account-level credits remove the seat tax: AI cost doesn't scale with headcount. But the included allowance is followed by a big fixed step. A team slightly over Basic faces a $1,620-a-year minimum purchase, so going over the free allowance feels like a cliff, not a top-up.

| Playbook | Lesson there |
|---|---|
| [credit-ui.md](credit-ui.md) | Pooled account credits are the right unit; the first paid step must be sized close to the overage, or depletion becomes a budget decision |
| [upgrade-triggers.md](upgrade-triggers.md) | A large jump between included and paid capacity turns a usage trigger into a procurement conversation; offer a small step first |
| [pricing-pages.md](pricing-pages.md) | Moving from "contact sales" to a listed price removes friction; the included allowance per plan belongs on the plan card |
| [paywalls.md](paywalls.md) | Including a base AI allowance on every paid plan is sample-then-scale; the gate is the step size, not access |
