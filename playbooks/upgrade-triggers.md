# Tier upgrade triggers — CRO playbook

Surface type 4: plan-level limits — seats, features, automations, integrations. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks). Cohort: **existing users** — they're customers who outgrew a limit, so the lever is capability, never urgency.

Credit / consumption limits are a different emotional state and have their own playbook: [credit-ui.md](credit-ui.md). A seat cap is a blocked-and-frustrated moment; a credit meter is an anxious, mid-task moment. Don't conflate them.

## Core rule

Propose the upgrade when the user is actively running into the ceiling — the invite that won't send, the automation that won't run — and tie it to what they were trying to do, not to a usage percentage. At that moment the upgrade reads as the answer to their problem, not a sales nudge. Warn before the wall, so the wall is never a surprise.

## Benchmarks

| Metric | Number | Tag | Applies to | Source | Checked |
|---|---|---|---|---|---|
| S&M spend per $1 of new ARR: expansion vs. new logo | $1.00 vs. $2.00 (medians, 2024 data) | [Verified] | B2B SaaS | [Benchmarkit 2025 SaaS Performance Metrics](https://www.benchmarkit.ai/2025benchmarks) | 2026-09-27 |
| Expansion ARR as a share of total new ARR (median, 2024 data) | 40%, up 5 points YoY; 58% at $50–100M ARR, 67% above $100M | [Verified] | B2B SaaS | [Benchmarkit 2025](https://www.benchmarkit.ai/2025benchmarks) | 2026-09-27 |
| Net revenue retention (median, 2024 data) | 101% | [Verified] | B2B SaaS | [Benchmarkit 2025](https://www.benchmarkit.ai/2025benchmarks) | 2026-09-27 |
| Free-trial conversion when product-qualified leads (PQLs) are used (600+ SaaS companies, Feb 2025 survey) | 25% average; 30% at $1K–5K ACV; 39% at $5K–10K ACV — vs 9% overall free-to-paid | [Verified] | B2B SaaS | [ProductLed PLG Benchmarks 2025](https://productled.com/blog/product-led-growth-benchmarks) | 2026-09-27 |

How to read these:
- **Expansion is almost half of new ARR at the median, and most of it at scale.** Each $1 costs half as much to sell as new-logo ARR. That's the economic case for investing in the seat and limit prompts in this playbook. It isn't a conversion rate for any one prompt.
- **NRR at 101% means the median company barely expands net of churn.** Expansion triggers are where the gap between median and good companies sits (inference).
- **The PQL figure measures a sales-assisted motion,** where usage signals route an account to a person. It isn't a self-serve upgrade prompt. For monday it supports the "admin at capacity" trigger and routing high-usage accounts to sales. It says nothing about the conversion of an in-product banner.
- **No sourced benchmark was found for "limit prompt → upgrade" conversion.** Figures like "contextual triggers convert at 4.2% vs 1.3%" or "usage limits convert 1.5–2x feature limits" circulate on agency blogs with no dataset or method. Don't cite them.

## Patterns

### Threshold ladder — owned here

For tier and seat limits, this playbook owns the thresholds; other playbooks cite it. Credit thresholds are owned by [credit-ui.md](credit-ui.md).

| Usage | Surface | Behaviour |
|---|---|---|
| 80% | Non-blocking inline nudge in the feature area | Calm, dismissible, shows the count and the next tier's number |
| 90% | More prominent prompt (banner, persistent) | Still dismissible; adds when they'll hit it if a pace is known |
| 100% | The gate | Blocks the action that exceeds the limit — never the work already done — with the upgrade and "Notify admin" paths |

This is a convention, not an evidence-backed optimum: it matches Airtable's alerts [Verified] and monday's own credit alerts at 80% and 100% ([monday-context.md](../context/monday-context.md)). A/B test the ladder before treating it as tuned.

### The trigger must match a business outcome

The strongest triggers are tied to something the user is trying to do.

- **Slack — history, not storage.** Free workspaces see the most recent 90 days of messages and files, and since August 2024 data older than a year is deleted — upgrading doesn't bring it back [Verified — [Slack help](https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack)]. The trigger is "you can't find the decision from November", a lost-knowledge outcome, and the deletion turns "hidden" into "gone".
- **Linear — the issue cap.** Free allows 250 issues and 2 teams; above 250, new issues can't be created [Verified — [Linear docs](https://linear.app/docs/billing-and-plans)]. Only non-archived issues count; archiving is automatic after an inactivity window that teams can shorten [Verified — [Linear docs](https://linear.app/docs/delete-archive-issues)]. Third-party reviews say most teams hit the cap within weeks of active use [Reported — [checkthat.ai](https://checkthat.ai/brands/linear/pricing)].
- **Notion — growth-event triggers.** A Free workspace with 2+ members gets 1,000 blocks, with a 3-day grace period once it's hit; 10 guests; 7 days of page history [Verified — [Notion help](https://www.notion.com/help/understanding-block-usage), [pricing](https://www.notion.com/pricing)]. These limits are a pricing decision too, but they fire on a growth event — a second member joining — which makes the ask feel earned. The grace period softens the wall without removing it.
- **Contrast — a packaging-driven gate.** When a limit moves because of a packaging change rather than the user's growth, the same prompt reads as a penalty. See [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling).
- **ChatGPT — soft degradation before the block.** When Plus users hit the model limit, chats switch to a lighter model until the limit resets, with a notice [Reported — OpenAI help-center text seen only via search; direct fetch blocked]. The user feels the difference before being asked to pay. Third parties also report it reads as "the model got worse" [Reported — [customgpt.ai](https://customgpt.ai/chatgpt-plus-limits-2026/)] — and silent degradation conflicts with monday's rule that agent flows keep task state ([monday-context.md](../context/monday-context.md)). Use it for interactive features only, and always say it happened.

### Seat expansion — the highest-frequency trigger

When a user tries to invite a teammate at the seat limit, offer the seats right there — not a pricing-page re-evaluation.

**Show:** seats used vs. total; how many they need (inferred from the invite); the price delta **for the next bundle** — monday sells seats in bundles of 3/5/10/15/20/25/30/40 ([monday-context.md](../context/monday-context.md)); one "Add seats" action.
**Contrast — seat right-sizing.** Slack's Fair Billing Policy marks members inactive after 28 days and credits the prorated unused time automatically [Verified — [Slack help](https://slack.com/help/articles/218915077-Slacks-Fair-Billing-Policy)]. Paying only for active seats removes the fear that makes admins hold invites back.
**Don't show:** a full pricing page; "Upgrade to Pro" to someone already on Pro; a wall with no immediate path.

### Seat-expansion modal

```
[Headline: "Add more team members"]
[Current: "You have {N} seats — {N} are used"]
[Bundle selector: next bundle {N} seats]
[Price: "+${X}/month — billed {cadence}"]
[CTA: "Add seats"]  [IC: "Notify admin"]  [Dismiss: "Not now"]
```

Apply when a user invites someone at the seat limit — offer the expansion in the moment.

### Admin at capacity

The admin viewing usage and seeing the team at capacity is a trigger too — the only one where the person who sees it can buy. Show the same bar and the next-tier number there, with the purchase one click away.

### The usage bar

```
[Usage bar: ████████░░ 200/250 automations this month]
"You've used 200 of your 250 monthly automations."
"Pro includes 25,000 a month."
[CTA: "Get more automations"]  [Link: "See what Pro includes"]  [Notify admin]
```

Required: a visual bar; the exact count ("200/250", not "most"); what happens at the limit; what the next tier gives, **as a specific number** — never "unlimited" unless it is (monday's Pro automations are 25,000/month, Enterprise 250,000 — [monday-context.md](../context/monday-context.md)); the price in the CTA on the admin path.

### IC vs. admin — always both paths

The IC who hits the limit usually can't buy. The context file lists admin alerts only for credits (80% and 100%) — for tier and seat limits there's no automatic admin notification, so the IC path is a button they press.

| Scenario | IC path | Admin path |
|---|---|---|
| At seat limit | "Your team is at 10/10 seats" + **Notify admin** | Seat selector with the bundle price delta, one confirm |
| At feature limit | What the feature does, the tier that has it + **Notify admin** | Direct upgrade with the relevant plan difference |
| At usage limit | "You've used 200/250" + **Notify admin** | Usage bar, upgrade CTA with price |

### Screen structure

```
[Context: what they hit]            "Your team is at 10/10 seats"
[Upgrade delta: what they get next] "{next tier} includes up to {N} seats, plus:" • 1–2 features relevant to this team
[Social proof, if available]        "Teams like yours move to {tier} at this point"
[Primary CTA]  [Notify admin]
[Maybe later — dismiss]
```

Don't block the current task: let the user finish what they were doing, or save it, before the upgrade ask.

## Company teardowns

### Airtable — the email-only warning (counter-example)

**What they ship [Verified].** Automation-run warnings go by email to workspace owners at 80%, 90% and 100%; usage lives in the account overview. At the limit, automations stop until the monthly reset or an upgrade. A third-party teardown notes there's no in-app warning next to the automation itself [Reported — [noloco.io](https://noloco.io/blog/airtable-automation-limit)].
**Where it breaks.** The person who built the automation never sees the warning, and the workflow stops silently.
**Steal for monday.com.** Do the opposite: an in-product meter where the builder works, plus the IC's "Notify admin" — the admin email alone isn't enough.

### Cursor — visibility and spend limits

See [case: cursor-2025-pricing](cases.md#cursor-2025-pricing) for the June 2025 backlash. For this surface: the usage dashboard and spend limits already existed; the July 2025 fix added visibility of approaching limits [Verified — [Cursor blog](https://cursor.com/blog/june-2025-pricing)]. On Teams, spend limits can be admin-only, and at the limit **on-demand usage stops** until raised or reset — included usage continues [Verified — [Cursor help](https://cursor.com/help/account-and-billing/spend-limits)].
**Steal for monday.com.** Let the admin set the ceiling, and say exactly what stops at it.

### Directional, unsourced

These pre-date the evidence standard and haven't been re-verified — patterns only, not citable as fact:
- **GitHub Copilot (Business):** a seat-limit hit emails the org admin and shows the blocked user a "request access" flow.
- **Zapier:** a usage bar on every automation turns invisible usage into an always-present signal.

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture before citing in a review.

### At a glance — who hits the limit vs. who pays

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Limit type that triggers upgrade | Capability (CRM, API) + volume | Seat type | Plan (workspace-wide) + automation runs | Usage tier / seat tier |
| IC → admin path | N/A (unlimited seats) | Best-in-class request flow | Weak — upgrade applies to whole workspace | Owner-set spend limits per seat tier / member |
| Proration | — | Yes, credit for unused seat time | Yes | Yes, upgrades immediate and prorated |
| Signature move | Docs steer top-up buyers to tier upgrade | One-time 3-day temporary access + request reason | — | Seat tiers (1.25x / 6.25x) inside one team plan |

### Figma — the reference implementation for IC → admin upgrades

**What they ship [Verified].**
- **Request moment:** users request a seat when they attempt an action their seat doesn't allow. With manual approval, they get a **one-time** 3-day temporary access per paid seat type (Full / Dev / Collab) while the admin reviews [Reported — the 3-day passage was seen only in a help-center search snippet and a Figma staff forum reply, 2026-09-26; re-read the article before citing as fact]; it applies on Professional as well as Organization and Enterprise. Access ends at denial or expiry.
- **Admin side:** the request shows where it was sent from, the request reason, current seat, and time; admins get email and in-app notifications, and the requester hears the decision either way. (An explicit cost line on the request card wasn't found in the docs on 2026-09-25.)
- **Policy control:** per seat type — manual approval, manual unless a paid seat is already free (default), or auto-approve, with digest emails listing new paid seats.
- **Billing:** approved seats are prorated; unused time on a prior paid seat is credited.

**Why it works.** Every step removes a reason for the admin to say no: the reason is attached, the user is already productive, and the default policy fills idle seats first.

**Where it breaks.** Temporary access is one-time per seat type — a declined user loses the grace path for good. Some admins ask to turn it off [Reported — [Figma forum](https://forum.figma.com/suggest-a-feature-11/temporary-3-day-access-when-requesting-an-upgrade-please-turn-this-off-39239)]. Accidental seat upgrades are a known refund-request category [Reported].

**Steal for monday.com.**
1. Request modal with a required one-line reason — it's the admin's approval argument.
2. Admin request card: requester, limit hit, where, reason, and the price delta in the seat *bundle*.
3. Default policy "auto-approve if a paid seat is idle" — a zero-cost yes.
4. Digest email for auto-approved upgrades.

### ClickUp — the counter-example on workspace-wide upgrades

**What they ship [Reported/Verified].** Every member of a workspace must be on the same plan, so one person needing a Business feature moves everyone to Business pricing; the AI add-on is billed per paid member. Free guests can auto-convert to paid members, and third parties report sudden bill jumps from it [Reported — [eesel.ai](https://www.eesel.ai/blog/clickup-pricing)]. Free Forever has unlimited members and tasks but tight storage and automation caps [Verified — [ClickUp pricing](https://clickup.com/pricing); Reported — [eesel.ai](https://www.eesel.ai/blog/clickup-pricing)], so volume, not seats, carries the free-tier trigger.

**Where it breaks.** The upgrade becomes a budget decision for the whole workspace, so ICs rarely trigger it, and surprise seat conversions erode admin trust.

**Steal for monday.com.** The automation-runs meter is the right proactive trigger. Never convert a guest or viewer to paid without an explicit admin action — show "Invite as member (+1 seat in your bundle)" vs. "Invite as guest (free)" at invite time.

### Clay — no seat triggers, so capability does the work

**What they ship [Verified].** Unlimited seats on every plan, so upgrades are driven by capability (CRM sync and API on Growth) and credit volume. Clay's docs state one-time top-ups carry a 30% premium and that upgrading the Data Credit tier is more cost-effective for regular needs.

**Why it works.** The docs do the upsell: the top-up is always available (no hard wall) but priced to make the tier upgrade rational for anyone who tops up twice.

**Steal for monday.com.** After the second top-up in a billing period, show the math: "You've topped up twice this month. The next package costs less than what you've spent." A trigger on the pattern, not the moment.

### Claude — seat tiers and spend controls inside one team

**What they ship [Verified].** Team plans have standard seats (1.25x Pro usage) and premium seats (6.25x Pro). Owners can enable usage credits and set monthly spend limits for the organization, by seat tier, or per member; the member list shows month-to-date spend. Individual Pro → Max upgrades apply immediately with prorated billing.

**Why it works.** Mixed seat tiers solve "only 3 of 20 people are heavy users" without upgrading the whole team. The MTD spend column is the admin's trigger: a member consistently paying overage is a premium-seat candidate.

**Steal for monday.com.** An admin view that flags heavy AI users on overage: "3 members used more than {N} credits in top-ups this month — a larger package would save ${X}." A trigger built from observed spend, shown to the payer.

## Anti-patterns

| Anti-pattern | Why it fails | Who did it |
|---|---|---|
| Warning only by email to the owner | The builder never sees it; workflows stop silently | Airtable automation limits [Verified] |
| "You've hit your limit" with no number or consequence | Frustration with no path forward | Common |
| Surprise hard stop with no warning threshold | The user feels ambushed, not informed | Common |
| Upgrade CTA with no view of what the next tier changes | Friction, zero motivation | Common |
| Vague or false upgrade benefit ("more", "unlimited" when it isn't) | "More" gives nothing to weigh; a false "unlimited" is a broken promise | Common — and a risk for monday, whose automation tiers are finite |
| A limit moved by a packaging change, framed like a growth trigger | Reads as a penalty, not an earned upgrade | [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling) |
| Workspace-wide upgrade for one person's need | ICs stop triggering upgrades; surprise bills | ClickUp [Reported/Verified] |
| Silent degradation in an agent flow | The task quietly gets worse or stops; state is lost | Risk flagged by ChatGPT's fallback [Reported] |
| Full pricing page at seat expansion | The user needs seats, not a plan re-evaluation | Common |
| Guest auto-converted to paid without admin action | Bill shock, broken trust | ClickUp [Reported] |
| Decline or close control under 24×24 CSS px, or below the fold on mobile | The "no" path fails WCAG 2.2 AA and reads as obstruction | Most SaaS products — floor per [WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [Verified] |

## Copy bank — upgrade triggers

Patterns to hand to `improve-conversion-surfaces-copy` — not final copy.

| Moment | Pattern | Example for monday.com |
|---|---|---|
| IC request modal | Ask for the reason | "Tell {admin} why you need Pro — we'll include it in the request" |
| Admin request card | Who, what, cost | "{name} hit the automation limit on '{board}' · Needs Pro · +${X}/mo in your {N}-seat bundle" |
| Proactive volume nudge | Number + consequence | "200 of 250 automations used — at this pace you'll hit the limit on {date}" |
| Next-tier delta | A specific number | "Pro includes 25,000 automations a month" |
| Top-up → package nudge | Show the math | "Two top-ups this month cost ${X}. The next package is ${Y} and includes more." |
| Guest vs. member at invite | Make the cost explicit | "Invite as guest (free, view only)" / "Invite as member (uses 1 seat)" |

## monday.com-specific notes

All facts from [context/monday-context.md](../context/monday-context.md).

- **The automation and integration caps** (250/mo each on Standard; 25,000 on Pro; 250,000 on Enterprise) are the highest-volume tier-upgrade triggers. Free and Basic have no automations, so their trigger is the feature gate, not a meter.
- **Thresholds:** 80% nudge ("200/250"), 90% prompt, 100% gate — per the ladder above.
- **Seat expansion:** always the bundle price delta, never a per-seat price that implies add-one purchasing.
- **ICs can't self-purchase.** Every tier or seat surface an IC sees has "Notify admin"; there's no automatic admin alert for tier limits today.
- **Cohort:** existing users — capability framing ("unlock X to do Y"), inline in the feature area, not a full-screen modal.

## Sources

Checked 2026-09-24 (AI-native set) and 2026-09-25 (everything else).

- Benchmarkit: https://www.benchmarkit.ai/2025benchmarks
- Airtable: https://support.airtable.com/docs/managing-airtable-automations · https://noloco.io/blog/airtable-automation-limit
- Slack: https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack · https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces
- Linear: https://linear.app/pricing · https://linear.app/docs/billing-and-plans · https://linear.app/docs/delete-archive-issues · https://checkthat.ai/brands/linear/pricing
- Notion: https://www.notion.com/help/understanding-block-usage · https://www.notion.com/pricing
- ChatGPT: https://help.openai.com/en/articles/11909943-gpt-5-in-chatgpt · https://customgpt.ai/chatgpt-plus-limits-2026/
- Cursor: https://cursor.com/blog/june-2025-pricing · https://cursor.com/help/account-and-billing/spend-limits · https://forum.cursor.com/t/team-admins-now-can-control-spend-alerts-and-limits/145259
- Figma: https://help.figma.com/hc/en-us/articles/1500003870721-Approve-or-decline-seat-upgrade-requests · https://help.figma.com/hc/en-us/articles/4414038570007-Set-approval-settings-for-new-seats · https://help.figma.com/hc/en-us/articles/15506350302615-Get-notified-when-people-upgrade-to-a-paid-seat · https://help.figma.com/hc/en-us/articles/360041061034-Manage-billing-on-the-Professional-plan · https://help.figma.com/hc/en-us/articles/360040453433-Make-a-seat-request · https://forum.figma.com/suggest-a-feature-11/temporary-3-day-access-when-requesting-an-upgrade-please-turn-this-off-39239
- ClickUp: https://clickup.com/pricing · https://quackback.io/blog/clickup-pricing · https://www.eesel.ai/blog/clickup-pricing · https://get-alfred.ai/blog/clickup-pricing
- Clay: https://university.clay.com/docs/actions-data-credits
- Claude: https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans · https://www.ai-toolbox.co/claude-management-and-productivity/claude-usage-limits-2026
- ProductLed: https://productled.com/blog/product-led-growth-benchmarks
- Slack Fair Billing Policy (2026-09-27): https://slack.com/help/articles/218915077-Slacks-Fair-Billing-Policy
