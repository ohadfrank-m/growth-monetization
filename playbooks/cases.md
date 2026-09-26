# Case library — stories that span surfaces

Some stories teach something on several surfaces at once. Each is told **once** here, with its evidence, and cited from the playbooks as `[case: {id}]`. The citing playbook adds only the lesson for its own surface. Evidence tags per [README.md](README.md). Checked 2026-09-25.

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
