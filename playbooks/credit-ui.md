# Credit / consumption UI — CRO playbook

Surface type 5: credit meter, low-balance warnings, depletion, top-up, and the admin side of all of these. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks). This file owns the credit thresholds; tier and seat limits are [upgrade-triggers.md](upgrade-triggers.md).

The context file names credit depletion UX the squad's top design priority ([monday-context.md](../context/monday-context.md)). It's the surface with the most novel problems in this plugin — most companies don't have a settled pattern yet.

## Core rule

Resolve the complexity for the user before they spend. Credits fail when the user can't tell what a credit buys, can't see how much is left, or learns the cost only after it's spent. Translate every number into work, warn before the wall, and when the wall comes, save the work and name what stopped.

Context: Growth Unhinged, using PricingSaaS data, counts 79 of the PricingSaaS 500 index with a credit model at the end of 2025, up from 35 a year earlier, and calls credits the defining pricing innovation of 2025 [Reported — [Growth Unhinged](https://www.growthunhinged.com/p/2025-state-of-saas-pricing-changes)].

Credits create a different anxiety than seat limits: users fear running out *mid-task* more than hitting a cap. Design for the anxious state, not only the depleted one.

## Patterns

### Thresholds — owned here

| State | Balance | Surface | Behaviour |
|---|---|---|---|
| Healthy | more than 20% left | Meter only | The number and its translation; no urgency copy |
| Warning | 20% left (80% used) | Non-blocking inline banner in the feature in use | "Running low" — proactive, dismissible |
| Critical | 5% left (95% used) | Persistent banner | Says what stops next and when it refills |
| Depleted | 0 | Inline in the feature, never a blocking modal in an agent flow | Names what stopped, saves the work, offers the paths |

These match monday's admin alerts at 80% and 100% ([monday-context.md](../context/monday-context.md)). They're a convention, not a tested optimum — A/B test before treating them as tuned. States must differ without colour too (pattern, glyph, border weight), so they read for colour-blind users and in low-fi wireframes.

### Task translation is mandatory

"500 credits" is meaningless; "≈ 25 resume screenings" is a reason to buy. Every credit number — meter, banner, depletion, top-up, pricing page — carries a task translation.

- **monday's translation:** the official line — 1,000 credits ≈ 50 resume screenings, 5 hours of meeting summaries, or hundreds of automated workflow updates. Never "1 credit ≈ 1 AI action": one AI block action is 8 credits, Notetaker 120 per meeting hour ([monday-context.md](../context/monday-context.md)). When usage data exists, prefer the user's own recent actions as the unit ("≈ 40 more summaries at your pace").
- **One rate everywhere.** If the pricing page and the meter imply different rates, trust breaks.
- **Who does it well.** HubSpot publishes a credit rate sheet — 50 credits per resolved Customer Agent conversation, 10 per workflow AI action, 100 per recommended lead — and per-tier included credits (Starter 500, Pro 3,000, Enterprise 5,000) [Verified — [HubSpot catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog)]. Notion publishes per-run cost ranges for Custom Agents (e.g. Q&A agents ~$0.03–$0.11 a run, daily briefs ~$0.10–$0.30) and shows each run's usage in an admin dashboard [Verified — [Notion help](https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents)]. Figma publishes a per-feature cost table in its Help Center [Verified — [Figma help](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work)], though a third party argues people don't find it before they need it [Reported — [UiChemy](https://uichemy.com/blog/figma-ai-credits/)].
- **Outcome pricing is translation built in.** HubSpot moved Customer Agent to $0.50 per resolved conversation and Prospecting Agent to $1.00 per recommended lead on April 14, 2026 [Verified — [HubSpot](https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete)]: the unit is the result.

### The always-on meter

- **Placement:** in the primary workspace chrome, not buried in settings. If users hunt for their balance, every depletion feels like a surprise.
- **Content:** balance + translation + refill date (`{reset date}` — the context file doesn't state the cadence).
- **Hover / tap detail:** what's been used and on what ("380 credits this week, mostly on summaries").
- **Mark what costs credits.** HubSpot marks credit-consuming features with an icon in the UI [Verified — [HubSpot KB](https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing)].
- **Scoring note:** a meter with a number and no translation is value clarity ≤2 on the design-reviewer rubric.

### Show the cost before the spend

The strongest credit pattern: a cost estimate before a run, not a receipt after it — Clay's pre-run estimate is the reference (AI-native set below). Lovable shows credits used only after or during a run, in a menu under each response, with no upfront estimate [Verified — [Lovable docs](https://docs.lovable.dev/introduction/credits-and-usage)] — honest, but the user can't decide before spending.

### Burn-rate forecasting

Rate-based framing ("at this pace you'll run out around {date}") turns awareness into proactive action. Tie the forecast to a moment the user cares about when one is known — "…before your Friday report" — so the date means something. Accuracy beats precision: a conservative range ("~3–5 days") over a false-precise day when data is noisy. Show it only with enough history (the spec default is ≥7 days).

### Depletion — what the moment needs

1. **Name what stopped**, not the balance: "{agent} has paused" beats "You're out of credits".
2. **Keep the work.** Lovable pauses a mid-task message when credits run out; the user can resume with new credits or ask it to wrap up [Verified — [Lovable docs](https://docs.lovable.dev/introduction/credits-and-usage)]. Cursor notifies the user and offers on-demand usage or an upgrade when included usage runs out [Verified — [Cursor help](https://cursor.com/help/models-and-usage/usage-limits)]. monday's platform doesn't natively save agentic task state today ([monday-context.md](../context/monday-context.md)) — "your work is saved" may only be said once it's true.
3. **Offer the right path for who's looking.** The admin gets the purchase; the IC gets "Notify admin" — ICs can't buy.
4. **Say when it's back:** the refill date makes waiting a real choice (Claude's pattern, AI-native set below).
5. **Resume path after credits land** — explicit, or automatic.

### Admin controls

HubSpot lets Super Admins and Billing Admins set account, feature and action-level limits; at a limit, features pause until the next cycle, and by default usage pauses when included credits run out — overage is opt-in [Verified — [HubSpot KB](https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing)]. Cursor's team spend limits stop on-demand usage at the cap [Verified — [Cursor help](https://cursor.com/help/account-and-billing/spend-limits)]. Caps remove the fear that makes admins switch AI off pre-emptively. monday already ships caps: admins can set limits account-wide, per capability (Hard or Soft) and per user or department ([monday-context.md](../context/monday-context.md)). The surface gap is making those limits visible to the IC who hits one — say which limit stopped them and who set it.

### Top-up and package choice

- **Three options** anchor a middle choice; pre-select the recommended one rather than a blank quantity.
- **Show the plan alternative alongside** — a bigger monthly package can beat repeated top-ups (Clay's docs make this explicit — see [upgrade-triggers.md](upgrade-triggers.md)).
- **One-click for the admin** with payment on file; confirm what was bought in tasks.
- **Rollover is a differentiator.** HubSpot, Figma and Cursor credits don't roll over [Verified — [HubSpot KB](https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing), [Figma help](https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work), [Cursor help](https://cursor.com/help/models-and-usage/usage-limits)]. Lovable's paid monthly credits roll over (2-month expiry); top-ups last 12 months; daily credits don't roll over [Verified — [Lovable docs](https://docs.lovable.dev/introduction/credits-and-usage)].
- **For monday:** packages are monthly buckets bought with seats — Standard 2,000 / 4,000 / 8,000, Pro 3,000 / 4,000 / 8,000 / 20,000, at $0.01 per credit annual or $0.0125 monthly, flat; Basic is fixed at 1,000 ([monday-context.md](../context/monday-context.md)). Top-up today means moving to the next bucket ("Add credits anytime"); one-time packs, overage and auto top-up aren't published, and unused credits don't roll over (official for Notetaker; the general rule is still to confirm) — spec those as open items, never as facts. Illustrative prices use slots (`{N} credits — ${price}`).

### Top-up modal (admin)

```
[Headline: "Add AI credits"]
[Current balance: "{credits} credits left"]
[Package options — three, recommended pre-selected:]
  ○ {N} credits — ${X}/mo   (≈ {translation})
  ● {N} credits — ${X}/mo   (≈ {translation})  [Recommended]
  ○ {N} credits — ${X}/mo   (≈ {translation})
[Summary: "{N} credits for ${X} — billed {cadence}"]
[CTA: "Add credits and resume"]   [Secondary for an IC: "Notify my admin instead"]
```

Three options anchor a middle choice; task translation on every option; "resume" in the CTA; the admin path as the secondary. For monday, show the per-credit price only where it differs — monday's is flat ($0.01 annual, $0.0125 monthly, [monday-context.md](../context/monday-context.md)), so the per-package total is what varies.

### Agent-run depletion banner

```
[Inline, in the agent run view:]
"{agent} has paused — your team is out of AI credits"
"It finished {N} of {M} steps. {what's kept}"
[Admin: "Add credits"]  [IC: "Notify admin"]  [Stop run and keep results]
```

### Agentic depletion — the critical experience

1. Never fail silently: tell the user immediately, with a resume path.
2. Preserve state before any UI, once the platform can.
3. A non-blocking warning during active runs, before the wall: "{agent} will pause in about {N} steps."
4. Never block at the warning threshold — the wall is only for real depletion.

### When a trial gates on time and credits

If a trial limits both days and credits, show the constraint that will bind first as primary, the other as one secondary line — two equal countdowns read as a trap. Pair the tighter gate with a value recap and the post-trial path. (A no-touch trial that limits both time and credits is being worked on, but it isn't in [monday-context.md](../context/monday-context.md) yet — add it there, with its numbers, before a spec relies on it.)

## Company teardowns

### Credit models — a map

Growth Unhinged's 2×2 sorts credit models by whether credits track value or cost, and whether the model favours the vendor or the customer [Reported — [Growth Unhinged](https://www.growthunhinged.com/p/2025-state-of-saas-pricing-changes)]:

| Quadrant | Companies in the source | Pattern (source's description) |
|---|---|---|
| Value-based, vendor-friendly | HubSpot, Adobe Firefly | Price AI around outcomes; tightly control usage to protect margins |
| Value-based, customer-friendly | Lovable, Replit | Framed around what you can build; Lovable pools credits and rolls them over; Replit rolls over on Pro only |
| Cost-based, vendor-friendly | Cursor | Tightly governed through caps, add-ons and admin controls |
| Cost-based, customer-friendly | Clay, PostHog | "Transparent but unforgiving"; limited rollover (Clay up to 2× the monthly allocation; PostHog 50% of unused prepaid credits on an equal-or-higher renewal) |

monday isn't in the source. On the context file's facts — credits bought as monthly buckets alongside seats, packages scaled by tier — it sits closest to the value-based, vendor-friendly quadrant; that placement is this playbook's inference.

### Cursor — opacity costs more than price

See [case: cursor-2025-pricing](cases.md#cursor-2025-pricing). For this surface: on June 16, 2025, Cursor replaced 500 requests with $20 of included usage at API prices; "unlimited" applied only to Auto mode, users hit unexpected charges, and on July 4, 2025 Cursor apologised and refunded [Verified — [Cursor blog](https://cursor.com/blog/june-2025-pricing)]. Included usage doesn't roll over.
**Steal for monday.com.** Never let a word like "unlimited" do work the mechanics don't back up.

### Linear — AI in the seat, compute metered

Most Linear AI features are included in the seat price. On June 11, 2026, Linear launched opt-in, prepaid, workspace-level AI credits for Coding Sessions and Agent Loops [Verified — [Linear docs](https://linear.app/docs/ai-credits), [changelog](https://linear.app/changelog/2026-06-11-coding-sessions)], after saying high-volume compute "may move to usage-based pricing beyond a certain threshold" [Verified — [changelog, Mar 2026](https://linear.app/changelog/2026-03-24-introducing-linear-agent)].
**Steal for monday.com.** A generous baseline inside the plan, and metering only for the heavy agentic workloads above it.

### Other launches worth knowing

- **Salesforce Flex Credits** (May 15, 2025): 20 Flex Credits = $0.10 per Agentforce action; packs of 100,000 for $500 [Verified — [Salesforce](https://www.salesforce.com/news/press-releases/2025/05/15/agentforce-flexible-pricing-news/)].
- **Airtable AI credit packs** replaced per-seat AI charges on June 24, 2025: 10,000 credits for $20/mo up to 400,000 for $800/mo [Verified — [Airtable help](https://support.airtable.com/articles/3378106230-airtable-ai-billing)].
- **Notion Custom Agents:** paid Notion Credits from May 4, 2026, $10 per 1,000, Business and Enterprise only [Verified — [Notion help](https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents)].

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook — and the most important one for this surface. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture before citing in a review.

### At a glance — the credit UI stack, pattern by pattern

| Pattern | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Pre-action cost estimate | **Best-in-class** — total, per-column, rows affected | Published per-task ranges in Help Center | — | — |
| Big-spend warning | Yes — warns when a run uses a large share of monthly budget | — | — | — |
| Persistent meter | Credit dashboard (time-series balance) | User + admin usage views, CSV export on Org/Ent | [Teardown needed] | Settings → Usage: session + weekly bars with reset times |
| Warning before wall | Via budget warning | [Teardown needed] | [Teardown needed] | "Approaching 5-hour limit" |
| Depletion behavior | Auto top-up keeps runs going | Paid AI off until reset; free AI stays on; daily cap on Starter/View | Automatic AI features pause | Blocking message + reset time |
| Continue-past-limit | Auto top-ups (admin, card on file) | Shared pool + PAYG to a spend limit | Credit packs ($10 / 10k) | Usage credits at API rates, monthly cap, auto-reload, alerts |
| Rollover | Up to 2x monthly allocation | None | None (trial credits don't reset) | Usage credits generally don't expire |
| Admin controls | Auto top-up threshold + amount | Pool purchase; custom individual limits (added after enforcement) | Workspace-level | Spend caps: org / seat tier / member, MTD spend column |

### Clay — cost transparency before the spend

**What they ship [Verified].**
- **Pre-run estimate:** when a column run would trigger downstream columns, Clay shows total estimated credits, a per-column breakdown, and the number of rows affected. It applies to manual runs *and* automated ones (scheduled imports, auto-update).
- **Variable pricing honesty:** variable-cost models show a per-row estimate marked with a tilde (~); final cost is set after the run.
- **Budget warning:** a warning fires before a run that would use a significant portion of the workspace's monthly credit budget.
- **History:** Overview tab charts credit balance as a time series so you can see when credits were spent; CSV export on all views.
- **Auto top-ups:** admins on paid self-serve plans set a trigger threshold (at least 15% of plan credits) and an amount (min 250 credits); charged to the card on file so a run in progress keeps going instead of stopping.
- **Rollover:** unused credits roll over up to 2x the monthly allocation. One-time top-ups carry a 30% premium.

**Why it works.** Clay moves the anxiety from *after* the spend to *before* it. The user commits to a known cost for a known number of rows — the same mental model as a checkout. Auto top-up solves mid-run depletion structurally.

**Where it breaks.** Failed lookups still consume credits (paying for three providers that return nothing) — the most-cited trust complaint in third-party coverage. Estimates are non-binding for variable models.

**Steal for monday.com.** This is the pattern for agents and AI Blocks:
- Before an AI Block runs on a column: "~[X] credits · [N] items · ≈[Y]% of this month's balance" with Run / Run on 10 items first.
- Before scheduling a recurring agent: "~[X] credits per run · [Z] runs/month ≈ [total]."
- Big-run warning above a threshold (e.g., >20% of remaining balance).
- Auto top-up for admins, framed as "keep agents running."
- Decide explicitly whether failed/empty AI outputs consume credits — and say so in the estimate.

### Figma — per-person allowance, graceful degradation, pooled rescue

**What they ship [Verified].** Credits belong to individual seats, reset monthly, no rollover, not shareable. Starter and View seats also have a 150-credit daily cap. When credits run out, paid AI features are disabled until the next reset while free features stay available, and an admin-purchased shared pool acts as a buffer (subscription at a better rate + pay-as-you-go up to a spend limit). Users and admins can track usage; Organization and Enterprise admins get CSV export and history, and Enterprise an AI Usage API. Per-user caps weren't available at enforcement (March 18, 2026); admins can now set custom individual limits **[Verified — [Figma help](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits), 2026-09-25]**. Allocations per month: Full seats 500 (Starter) / 3,000 (Professional) / 3,500 (Organization) / 4,250 (Enterprise); Dev, Collab and View seats 500 on every plan; View and Starter also a 150-credit daily cap; a per-feature cost table is published in the Help Center **[Verified]**.

**Why it works.** Free AI features staying live means depletion degrades the product rather than breaking it. The shared pool is the right fix for per-seat limits: the heavy user draws from the account, not from a colleague.

**Where it breaks.** At enforcement (Mar 18, 2026) users reported running out within hours of real Figma Make work; the forum thread is a case study in launching limits on a feature people had used unmetered. Model selection changes cost up to ~8x for the same action **[Reported]**, and the meter can't warn about that unless cost is shown at model choice.

**Steal for monday.com.** (1) Classify every AI capability as credit-consuming vs. free (monday already keeps an AI Feature Catalog — per [monday-context.md](../context/monday-context.md)) and keep the free ones live at zero balance. (2) If a cheaper model/mode exists, show the credit delta at the selector. (3) Never enforce a new limit without a comms ramp and a ready purchase path (Figma had one week between add-on launch and enforcement — take more).

### ClickUp — credits under a seat subscription

**What they ship [Verified].** AI Super Credits power automatic AI features (Super Agents, Autopilot Agents, AI Fields, AI Cards). Allowances: Brain 1,500 per user/mo, Everything AI 5,000 per user/mo; Free 500 per workspace and paid-without-AI 1,000 per user, both one-time. When trial credits run out, automatic features pause until an add-on or credit pack is bought. Extra credits $10 per 10,000. Subject to a fair-use policy.

**Why it works.** Splitting "chat/writing = unlimited in the seat" from "automatic agents = metered" is a clear mental model: humans typing are flat-rate, machines running are metered.

**Where it breaks.** Automatic features fail quietly — a paused AI Field looks like missing data. Seat price + credits stack makes the bill hard to predict (the top theme in third-party reviews).

**Steal for monday.com.** Adopt the "interactive = included, autonomous = metered" split in how credit UI *explains* consumption, even if pricing differs. For any autonomous feature, the paused state is designed first: inline marker on every affected item, a board-level banner, and an owner notification.

### Claude — the two-window meter and the pay-to-continue exit

**What they ship [Verified].**
- **Meter:** Settings → Usage shows progress for the five-hour session and the weekly limit, each with its reset time.
- **Progression:** "Approaching 5-hour limit" warning → blocking message stating when usage is available again.
- **Continue path:** paid plans can turn on usage credits — billed separately at API rates, under a monthly spending cap you set (or unlimited), with auto-reload below a threshold and alerts when approaching limits. Real-time consumption and month-to-date spend are shown in Settings → Usage.
- **Team:** owners set limits org-wide, by seat tier, or per member; a member who hits their cap is paused until reset.
- **Education:** Help Center explains what burns usage (long threads, higher effort, attachments) and what doesn't (reused project content is cached).

**Why it works.** The reset time turns depletion into a wait-or-pay decision instead of a dead end. Spending caps make pay-as-you-go safe to enable. Teaching users *why* usage burns reduces "the limits are unfair" sentiment.

**Where it breaks.** Two stacked windows are harder to reason about than one balance. Third-party reports say a promotional credit claim enabled usage credits by default for some users, who were then charged past plan limits **[Reported]** — continue-past-limit billing must always be an explicit opt-in.

**Steal for monday.com.** (1) Show the *refill date* on every depletion surface. (2) Top-up with a monthly cap as the default admin setting. (3) A "why did this cost so much?" explainer on the usage page, per capability. (4) Overage is always opt-in; the admin sees a confirmation of the cap they set.

### Copy bank — credit UI

| Moment | Pattern | Example for monday.com |
|---|---|---|
| Pre-run estimate | Cost + scope + share of balance | "~450 credits · 300 items · about 15% of your remaining balance" |
| Big-run warning | Name the share | "This run uses about half of what's left this month. Try it on 10 items first?" |
| Persistent meter | Balance + translation + refill | "{credits} credits left ≈ {n} {usage unit} · refills {reset date}" |
| Forecast | Rate + deadline | "At this pace you'll run out around [date], before your cycle refills" |
| Depleted (interactive) | What stopped + resume | "Sidekick needs more credits to answer — top up or wait until [date]" |
| Depleted (autonomous) | Where it stopped | "AI stopped updating 'Sentiment' on 120 items · Top up to resume" |
| Overage opt-in | Cap is the headline | "Keep agents running past your balance — up to $[cap]/month. You'll get an alert at 80%." |

### Sources (checked 2026-09-24)

- Clay: https://university.clay.com/docs/credit-usage · https://university.clay.com/docs/actions-data-credits · https://www.clay.com/blog/introducing-clay-pricing-3-0-the-most-flexible-credit-system-on-the-market · https://www.cleanlist.ai/blog/2026-03-12-clay-pricing-changes-2026
- Figma: https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work · https://www.vibecodingacademy.ai/blog/figma-ai-credits-everything-you-need-to-know · https://forum.figma.com/share-your-feedback-26/figma-make-ai-credit-limits-not-feasible-51713/index4.html · https://www.appshot.app/posts/2026-07-09-figma-ai-credits-explained/
- ClickUp: https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits · https://www.rock.so/blog/clickup-pricing
- Claude: https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans · https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans · https://www.ai-toolbox.co/claude-management-and-productivity/claude-usage-limits-2026 · https://ccforeveryone.com/guides/claude-code-limits-and-pricing

## Anti-patterns

| Anti-pattern | Why it fails | Who did it |
|---|---|---|
| Bare credit number, no task translation | The user can't evaluate the purchase | Common; monday risk if anyone reverts to the retired 1:1 translation |
| Opaque mechanics ("unlimited" that isn't) | Trust collapses faster than any price increase | Cursor, June 2025 [Verified] |
| Cost shown only after the spend | The user can't decide before spending | Lovable — no upfront estimate [Verified] |
| Credit docs that exist but can't be found at the moment of need | Confusion and third-party explainers | Figma, per a third party [Reported] |
| Depletion that names the balance, not what stopped | The loss isn't connected to the work | Common |
| Hard stop mid-agent-task, work lost | The top-up moment becomes a churn moment | Common in agentic tools |
| Full-screen blocking modal in an agentic flow | Breaks momentum | Common |
| No IC → admin path | The IC is stuck; the admin never learns | Common in B2B |
| No resume path after purchase | The user has credits and doesn't know how to continue | Common |
| Credit expiry not communicated | A surprise at month end | Common |
| Silent downgrade to a lighter model in an agent flow | The task quietly gets worse | Risk flagged by ChatGPT's fallback [Verified] |

## monday.com-specific notes

All facts from [context/monday-context.md](../context/monday-context.md).

- **AI credits are new** (the current model applies to customers who joined on or after May 6, 2026) — users have no mental model yet. The first depletion experience must teach, not just sell.
- **Packages** are monthly buckets bought alongside seats: Standard 2,000 / 4,000 / 8,000; Pro 3,000 / 4,000 / 8,000 / 20,000; $0.01 per credit annual, $0.0125 monthly, no volume discount. Basic is fixed at 1,000; Free has 0.
- **At 100%** a short, unquantified grace period runs, then paid AI capabilities pause until credits are added or the billing cycle resets; free AI features keep working. No auto top-up; admins get alerts at 80% and 100% (whether ICs do is unconfirmed). ICs see depletion but can't buy — every surface needs "Notify admin".
- **One account-level pool** with admin limits (account, per capability Hard/Soft, per user or department). A user can be stopped by their own limit while the account still has credits — the copy must say which.
- **State preservation** isn't native for agentic tasks today — a known gap. Don't promise "your work is saved" until it is.
- **Cadence:** a monthly allotment tied to the billing cycle, not the calendar month. Per-feature rates are in the context file's rate table.
- **Still unpublished:** general rollover rule, one-time packs / overage / auto top-up, grace length. Spec them as open items.
- **New users** (14-day Pro trial; trial credit amount unpublished) have a time lever: "you're getting value — don't let it stop". **Existing users** have none: show value received, not scarcity.

## Sources

Checked 2026-09-24 (AI-native set) and 2026-09-25 (everything else).

- Growth Unhinged / PricingSaaS: https://www.growthunhinged.com/p/2025-state-of-saas-pricing-changes · https://newsletter.pricingsaas.com/p/how-to-use-credit-models-12-examples
- HubSpot: https://legal.hubspot.com/hubspot-product-and-services-catalog · https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing · https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete · https://www.hubspot.com/products/artificial-intelligence/credits
- Notion: https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents
- Figma: https://www.figma.com/blog/updates-to-ai-credits-in-figma/ · https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work · https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits · https://uichemy.com/blog/figma-ai-credits/
- Lovable: https://docs.lovable.dev/introduction/credits-and-usage
- Cursor: https://cursor.com/blog/june-2025-pricing · https://cursor.com/help/models-and-usage/usage-limits · https://cursor.com/help/account-and-billing/spend-limits · https://cursor.com/docs/account/pricing
- Linear: https://linear.app/docs/ai-credits · https://linear.app/changelog/2026-06-11-coding-sessions · https://linear.app/changelog/2026-03-24-introducing-linear-agent
- Salesforce: https://www.salesforce.com/news/press-releases/2025/05/15/agentforce-flexible-pricing-news/
- Airtable: https://support.airtable.com/articles/3378106230-airtable-ai-billing
- Replit / PostHog / Clay: https://www.lowcode.agency/blog/replit-pricing-explained · https://posthog.com/docs/billing/pre-paid-plans · https://university.clay.com/docs/credit-usage
