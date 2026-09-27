# Trial flows — CRO playbook

Surface type 7: trial start, mid-trial nudge, trial expiry. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against the Trial Flow rubric column). This file **owns trial phases**. Feature gates met during a trial are [paywalls.md](paywalls.md); credit meters and depletion are [credit-ui.md](credit-ui.md); tier and seat limits are [upgrade-triggers.md](upgrade-triggers.md).

## Core rule

A trial exists to get the user to one activation milestone before the clock or the balance runs out. Everything else follows from that milestone: define it first, point every nudge at it, and never ask for money before it has happened. At expiry, show what the user built and exactly what changes. The work stays; the paid capability stops.

## Benchmarks

| Metric | Number | Tag | Applies to | Source | Checked |
|---|---|---|---|---|---|
| Free-to-paid, free trial, **no card** (50th / 75th percentile, within 6 months) | 4–6% / 10–15% | [Verified] | B2B SaaS | [ChartMogul × Kyle Poyar, SaaS Conversion Report 2026](https://chartmogul.com/reports/saas-conversion-report/) | 2026-09-27 |
| Free-to-paid, free trial, **card required** (50th / 75th) | 25–35% / 50–60% | [Verified] | B2B SaaS | [ChartMogul 2026](https://chartmogul.com/reports/saas-conversion-report/) | 2026-09-27 |
| Most common trial length | 14 days (62% of products; 7 and 30 days 14% each) | [Verified] | B2B SaaS | [ChartMogul 2026](https://chartmogul.com/reports/saas-conversion-report/) | 2026-09-27 |
| Trial-to-paid, opt-in (no card) vs opt-out (card), organic | 18.2% vs 48.8% | [Verified] | mixed | [First Page Sage, Sept 2025](https://firstpagesage.com/seo-blog/saas-free-trial-conversion-rate-benchmarks/) | 2026-09-27 |
| Activation rate, SaaS (median / average; each company defines activation) | 30% / 36% | [Verified] | mixed | [Lenny's Newsletter activation survey, 2022](https://www.lennysnewsletter.com/p/what-is-a-good-activation-rate) | 2026-09-27 |
| Time to value, best-in-class (90th percentile) | 0.2 days | [Verified] | mixed | [Pendo Product Benchmarks](https://www.pendo.io/product-benchmarks/) | 2026-09-27 |
| Trial-to-paid by length (median): ≤4d / 5–9d / 17–32d | 25.5% / 37.4% / 42.5% | [Verified] | mobile app | [RevenueCat State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps) | 2026-09-27 |
| Trial-to-paid by length, monthly plans: ≤4d / 5–9d / 10–16d / 17–32d | 39.6% / 45.9% / 46.6% / 43.7% | [Verified] | mobile app | [RevenueCat, free-trial length](https://www.revenuecat.com/blog/growth/free-trial-length) | 2026-09-27 |
| Free-to-paid, reverse trial (50th / 75th percentile) | 4–6% / 8–12% | [Verified] | B2B SaaS | [ChartMogul 2026](https://chartmogul.com/reports/saas-conversion-report/) | 2026-09-27 |
| Spread of self-serve conversion, top 20% vs bottom 20% of products | ~10x | [Verified] | B2B SaaS | [Growth Unhinged, 2026 free-to-paid report](https://www.growthunhinged.com/p/free-to-paid-conversion-report) | 2026-09-27 |
| Activation rate, product-led vs sales-led (547 SaaS companies, Userpilot customers, 2024) | 34.6% vs 41.6% | [Verified] | B2B SaaS | [Userpilot Product Metrics Benchmark Report 2024](https://userpilot.com/blog/product-metrics-benchmark-report/) | 2026-09-27 |
| Onboarding checklist completion rate (average) | 19.2% | [Verified] | B2B SaaS | [Userpilot 2024](https://userpilot.com/blog/product-metrics-benchmark-report/) | 2026-09-27 |
| Time to value, product-led vs sales-led (average) | 1 day 12 h vs 1 day 11 h | [Verified] | B2B SaaS | [Userpilot 2024](https://userpilot.com/blog/product-metrics-benchmark-report/) | 2026-09-27 |

How to read these:
- **The two no-card figures differ ~3x** (ChartMogul median 4–6% vs First Page Sage 18.2%) because they measure different things: a self-reported survey of 200 B2B products over a 6-month window vs one agency's client book (86 companies, 71% B2B) measured trial-to-paid. Cite both; never average them or quote one alone.
- **monday's trial is no-card**, so the no-card rows are the comparison, not the card-required ones (inference from [monday-context.md](../context/monday-context.md#trial)).
- **Mobile rows are directional only.** The two RevenueCat cuts disagree on whether longer trials win; neither can set monday's B2B trial length.
- **Activation, three sources, three definitions.** Lenny's SaaS median (30%), Userpilot's PLG average (34.6%) and Pendo's time to value are each measured against every company's own milestone. They bound what "normal" looks like; none sets monday's target. Userpilot's sample is its own customer base, which is self-selected.
- **A checklist is not the milestone.** Average checklist completion is 19.2%, so four in five users never finish one. Phase 1 should point at one action, not a list (inference from the number).
- **Dropped as unsourced:** "OpenView 2025" 14.7% (OpenView closed in Dec 2023), ChurnZero 52% day-7–14 disengagement, Gainsight 2.7x for 3+ features, Totango 61% email-only, Pulseahead "4x behavioural triggers" and "~1% by day 14". None traces to an openable report with a method.

## Patterns

### Define the activation milestone first

One action, observable in product data, that the trial is built to reach. monday's aha signals are **first automation created, first AI action completed, first team member invited** ([monday-context.md](../context/monday-context.md#user-cohorts)). A spec picks one as the trial's primary milestone and says why. A narrower milestone, such as "first agent run that completes a task end-to-end", is a proposal and needs the data owner to confirm it correlates with conversion.

Activation is company-defined (the Lenny survey's median is 30% under each company's own definition), so a benchmark can't tell you what monday's milestone should be. Only monday's own trial-to-paid data can.

### Three phases — owned here

| Phase | Window (14-day trial) | Goal | Surface | Never |
|---|---|---|---|---|
| **1. Setup** | Day 0–3 | Reach the milestone | Non-blocking banner, checklist, templates on the user's own use case | An upgrade ask or a modal |
| **2. Proof** | Day 4–11 | Convert activated users; re-engage stalled ones | Behaviour-triggered inline prompts tied to what the user is doing | A calendar-only drip that ignores what the user did |
| **3. Decision** | Final 48–72h and expiry | Make the choice concrete | Countdown, personalised "what you built" list, plan decision screen | A generic "your trial is ending" with no specifics |

The window boundaries are a convention, not a tested optimum. A/B test them before treating them as tuned.

### Triggers: behaviour first, calendar as the backstop

Fire on what the user did, then use the calendar only for the countdown. Behaviour triggers worth speccing:

- **Milestone reached** → confirm it, then name the next Pro capability it unlocks
- **No return for {N} days** after signup → re-engagement pointed at the milestone, not at pricing
- **Trial credit balance crosses a threshold** → credit-meter rules in [credit-ui.md](credit-ui.md); in a trial, lead with what the credits did
- **Second teammate invited** → collaboration signal; show what the team keeps on a paid plan
- **Locked feature attempted** → gate rules in [paywalls.md](paywalls.md)

Suppression matters as much as firing. Never nudge a user who has already converted, and never send a Phase 1 prompt to a user who has already reached the milestone.

No sourced study quantifies the gap between behaviour and calendar triggers (the widely quoted "4x" traces only to a vendor blog). The case for behaviour triggers is mechanical: the prompt meets the user at the moment the value is visible.

### What the trial meters

Days are one meter, not the only one. The AI-native set below shows four:

| Meter | Example | Risk |
|---|---|---|
| Calendar | Clay 14 days | Expires before a slow evaluator activates |
| Credit balance | Clay trial credits; monday's NT dual-gated trial (internal) | Runs out before the milestone on a heavy first day |
| Per-feature uses | ClickUp "Trial" allowances | Many meters, walls with no warning |
| Seat / intent grace | Figma 3-day seat access | Admin resents a grant they didn't approve |

**When a trial has two meters** (days *and* credits), the surface must show both and say which runs out first. A balance that ends a trial on day 3 needs its own Phase 3 moment, not a day-14 modal.

### Trial limits never undercut the plan after it

A trial limit tighter than the free or lower plan the user lands on means the evaluator hits the wall sooner in the trial than after it ends. Clay's trial caps tables at 50 rows; its Free plan allows 200 [Verified — [Clay FAQ](https://www.clay.com/faq/what-do-i-get-in-the-free-trial), [Clay pricing](https://www.clay.com/pricing)].

### Expiry: data stays, capability stops — and the lower option is visible

- **Keep the work.** ClickUp keeps trial data but blocks editing with the paid features [Verified]; Figma locks files over the Starter limit rather than deleting them [Verified]. "Nothing is deleted" is the promise that makes a downgrade survivable.
- **List what changes, item by item**, from the user's own account: boards, automations, AI runs, teammates. A personalised list beats a generic feature list. This is a recommended pattern for monday; no competitor publicly documents one (the "Notion expiry modal" often cited for it has no source).
- **Show the lower option explicitly**, with what it keeps and what it loses. A decision screen with only "Upgrade" reads as a trap.
- **Put the price on the upgrade CTA** or directly beside it, so the decision doesn't need another click.

### Extensions

Canva limits its trial to once per account and once per payment method [Verified — [Canva help](https://www.canva.com/help/upgrade-to-canva-pro-or-business/)]. That rule is about stopping people gaming the trial, not about extensions. There is no sourced evidence on whether extensions help conversion. **monday trials can't be extended** ([monday-context.md](../context/monday-context.md#trial)), so any extension design is a policy proposal with an owner, not a surface tweak.

### Card required vs no card

The benchmark split is large (ChartMogul median 25–35% with a card vs 4–6% without), but a card-required trial filters who starts, so the rates aren't a like-for-like lift. A card-required trial also converts automatically, which brings disclosure and pre-conversion reminder duties. Adobe's 2026 order requires reminders before trials convert [Verified — [case: ftc-cancellation-enforcement](cases.md#ftc-cancellation-enforcement)]. monday's trial needs no card, so nothing converts silently. That keeps the trial trustworthy, but it also means the decision screen does all the converting.

### IC vs admin in a team trial

In a team trial, the person who activates is often not the buyer. Figma starts short seat access at the moment of intent and routes the decision to the admin [Reported — help-center snippet and staff forum reply]. For monday: the IC who reaches the milestone needs a "Notify admin" path, and the admin's decision screen should show the team's activity, not only the admin's own.

## Company teardowns

### Canva — generous length, AI held back

**What they ship [Verified].** A 30-day Pro/Business trial, once per account and once per payment method. It can start without payment details in some flows; if it does, it ends automatically with no charge. **Trials get the same AI allowance as Canva Free**; the larger AI allowance needs a paid plan [Verified — [Canva help](https://www.canva.com/help/upgrade-to-canva-pro-or-business/), [pricing](https://www.canva.com/pricing/)].

**Flow.** Start trial → full Pro features for design → AI at Free levels → day 30: pay or revert.

**UI [Teardown needed].** Day-0 onboarding prompt and the expiry screen aren't captured; don't quote their copy.

**Why it works.** A long window suits a product people use in bursts. The once-per-account rule stops people re-trialling.

**Where it breaks.** Holding AI back means the trial can't prove the AI value it sells (inference).

**Steal for monday.com.** The opposite lesson on AI. monday's trial is Pro, and AI is the paid-only layer that's hardest to picture, so the trial should let the user *run* AI on their own boards, not preview it. The trial credit amount isn't published (see monday notes).

### Linear — forever-free plus a 30-day paid trial

**What they ship [Verified].** Free forever: 250 issues and 2 teams. Over 250 issues "you will no longer be able to create new issues." Separately, a 30-day trial of Business features ("try Asks and other Business features for 30 days") [Verified — [pricing](https://linear.app/pricing), [billing docs](https://linear.app/docs/billing-and-plans), [Linear Asks](https://linear.app/integrations/linear-asks)]. Linear Agent and the agent platform are on Free [Verified].

**Flow.** Free workspace → hit the capacity cap *or* start a Business trial for a specific capability.

**Why it works.** Two conversion paths: the capacity cap catches teams that grow, and the trial catches teams that want a specific capability.

**Where it breaks.** The capacity cap moves slowly. A third-party blog says teams outgrow Free in about six months [Reported — [Lifestack](https://lifestack.ai/blog/linear-pricing), opinion].

**Steal for monday.com.** Scope a trial to a capability ("try AI agents for {N} days") as well as to a plan, for users already on a lower plan (proposal).

### Notion — trial that converts by default only if a card is on file

**What they ship [Verified].** A 30-day Business trial. With a card on file, the plan auto-renews; without one, the user is "prompted to confirm your upgrade" at the end. Cancelling returns the workspace to Free (Plus users return to Plus). The Business trial includes Notion AI [Verified — [Notion help](https://www.notion.com/help/paid-plan-trials)].

**Why it works.** The user chooses at the end, which matches the moment they've seen the value.

**Where it breaks.** Notion's AI moved into Business in May 2025, so the trial now carries a bigger upgrade than a user who wanted only AI might want [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling). For trials: when AI sits only in the top tier, the trial has to prove that tier's full price, not just the AI.

**Steal for monday.com.** monday's no-card trial works like Notion's no-card path: a confirm-your-plan moment. Make that screen personal and specific.

### Cursor — a Pro trial behind a model gate

**What they ship.** The free Hobby plan has limited Agent requests; frontier models are a paid feature [Verified — [pricing](https://cursor.com/pricing)]. New Hobby users get a Pro trial, reported as 1–2 weeks [Reported — [nxcode](https://www.nxcode.io/resources/news/is-cursor-ai-free-plans-limits-worth-upgrading-2026)]. The trigger UI isn't documented [Teardown needed].

**Why it works.** The paid difference is a capability the user can feel (a better model), not a quota.

**Steal for monday.com.** In a trial, name the Pro-only AI capability the user is running, so expiry means losing something concrete.

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party or search snippet, **[Teardown needed]** capture a live screenshot before citing in a review. None of the four documents its trial copy in a readable source, so there's no Copy pattern step until a teardown.

### At a glance — how each one runs a trial

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Trial offer | 14 days, Growth-plan features [Verified] | No paid-plan trial; free-forever Starter + 3-day seat access on request [Verified / Reported] | Plan trials [Verified], reported 14 days [Reported]; per-feature "Trial" allowances [Verified] | No Pro/Max trial; Free plan + 7-day referral guest pass [Reported] |
| Card required | Not stated; third parties say no [Reported] | No (Starter) | Not stated for trials; needed to upgrade [Verified] | Yes, for the guest pass [Reported] |
| Credits in trial | 1,000 data credits (docs) vs 2,000 credits + 10,000 actions (FAQ) [Verified — contradictory] | Starter: 500 AI credits/mo, 150/day cap [Verified] | One-time: 500 AI credits per Free workspace; 1,000 per user on paid plans without the AI add-on [Verified] | Free: smaller models only; no Claude Code or top models [Verified] |
| Metered by | Calendar + rows + credits | Files + seats + daily AI cap | Uses per feature (never reset) + one-time credits | Usage limits with timed reset |
| At expiry | Drops to Free; credits expire except 100 [Verified]; data kept [Reported] | No expiry. Downgrade: 3-file limit, excess files locked [Verified] | Data kept; can't edit with the trial's paid features [Verified] | Guest pass renews to paid Pro unless cancelled [Reported] |

### Clay — the constrained sandbox trial

**What they ship [Verified].** A 14-day trial of Growth-plan features (webhooks, CRM integrations, sequencers, HTTP API); phone enrichment excluded. The allowance differs between Clay's own pages: 1,000 data credits (plans doc) vs 2,000 credits, 10,000 actions and tables capped at 50 rows (FAQ). Trial credits expire at the end; only 100 roll over. Each teammate can open their own trial account. Free: 100 data credits, 500 actions a month, 200 rows per table, no CRM or API.

**Flow.** Sign up → trial starts → build a table (≤50 rows) → enrich and push to CRM/API → day 14: credits expire (100 kept), plan drops to Free, CRM/API gated again.

**UI [Teardown needed].** Days-remaining indicator, 50-row limit state, day-14 notice.

**Why it works.** The trial unlocks exactly what Free gates, the "operationalize" layer, so the user tries the paid step itself. The row cap stops a new user spending the whole allowance on one table.

**Where it breaks.** The trial is stricter than Free on rows (50 vs 200). Two pages give two allowances, so the offer is hard to understand. Unused credits vanish at the moment they'd be a reason to stay (inference).

**Steal for monday.com.** Aim the trial at the paid-only layer: AI running on the user's own boards. Never make a trial limit tighter than the plan that follows it.

### Figma — no trial clock; free forever plus a 3-day grace

**What they ship.** No trial of any paid plan [Verified — [pricing FAQ](https://www.figma.com/pricing-faq/), absence]. Starter full seats get 500 AI credits a month with a 150-credit daily cap [Verified — [Figma help](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits)]. The trial-like mechanic is temporary seat access: request a paid seat, use it for up to 3 days while the admin reviews, one-time per seat type [Reported — help-center snippet and a Figma staff forum reply]. Downgrading to Starter limits the team to 3 files per product and one folder; excess files lock and Sites unpublish [Verified — [Figma help](https://help.figma.com/hc/en-us/articles/360046216313-Upgrade-or-downgrade-your-plan)].

**Flow.** Starter → hit a paid action → seat request → 3 days of access → approved, or access reverts.

**UI [Teardown needed].** Request modal with the 3-day notice, expiry state, Starter file lock.

**Why it works.** The trial is scoped to one person, one seat type, one intent, and starts at the moment of intent, not at signup.

**Where it breaks.** Admins complain about unapproved edits, users who think temporary access means approval, and no org-level off switch [Reported — [Figma forum](https://forum.figma.com/suggest-a-feature-11/temporary-3-day-access-when-requesting-an-upgrade-please-turn-this-off-39239)].

**Steal for monday.com.** An intent-triggered mini-trial for an IC on a multi-seat account: short access now, the admin notified. Give admins the off switch Figma didn't, and tell the IC on screen that the access is temporary (proposal).

### ClickUp — trial by feature, not by calendar

**What they ship [Verified].** Plan trials, with status on the Billing plan card. At expiry, "you won't lose access to your data" but can't edit or add with the trial's paid features. The pricing grid marks many features "Trial" on lower tiers; those allowances never reset, and at the limit data stays read-only with an upgrade prompt. AI is trialled separately: Brain use caps (Free 25 per workspace) and one-time AI credits (500 per Free workspace); "once trial credits are consumed, automatic AI features pause". Only owners or admins upgrade; a card is required [Verified — [upgrade](https://help.clickup.com/hc/en-us/articles/6303314345623-Upgrade-your-plan), [pricing intro](https://help.clickup.com/hc/en-us/articles/10129535087383-Intro-to-pricing), [Brain limits](https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits)].

**Flow.** Free workspace → use a "Trial" feature → hit its cap → upgrade prompt, data read-only. In parallel: AI on a one-time balance → balance used → automatic AI pauses.

**UI [Teardown needed].** Plan-trial banner, per-feature limit prompt, paused-AI state.

**Why it works.** Each feature carries its own trial, so the prompt fires on the feature in use: behavioural timing without a behavioural engine. "Data kept, editing blocked" makes expiry a visible loss, not a deletion.

**Where it breaks.** Dozens of never-resetting allowances are hard to explain; a user can burn one while exploring and meet a wall weeks later without warning [Reported — [ClickUp feedback](https://feedback.clickup.com/feature-requests/p/limited-uses-warning)]. Plan, feature and AI trials run on three separate meters (inference).

**Steal for monday.com.** Keep the expiry rule (data stays, paid editing stops) and show item by item what becomes read-only. Don't copy the per-feature allowances into a 14-day trial: one clock, one balance.

### Claude — the free tier is the trial

**What they ship.** No Pro or Max trial [Verified — [Pro plan article](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan), absence]. "Try Claude" puts users on a $0 Free plan with chat, search, files, artifacts and connectors; Claude Code and the top models are paid [Verified — [pricing](https://claude.com/pricing)]. Usage walls show the reset time and offer wait / upgrade / usage credits ([paywalls.md](paywalls.md)). The only time-boxed offer is a referral guest pass: 7 days of Pro for someone who has never paid, card required, renews to paid unless cancelled [Reported — [GrowSurf](https://growsurf.com/blog/anthropic-claude-referral-program/)].

**Flow.** Free → usage wall or Pro-only capability → upgrade. Or: guest pass → card → 7 days of Pro → renews.

**UI [Teardown needed].** Guest-pass claim and day-7 renewal screens.

**Why it works.** A free tier with a timed reset trials the core job daily, with no clock to expire. The paid difference is capability, so the upgrade reason is concrete. Passes flow through existing heavy users, who pre-qualify the recipient (inference).

**Where it breaks.** The only Pro trial needs a card and auto-renews: an opt-out trial that carries the consumer-protection duties in [cancellation.md](cancellation.md). The paid-only capabilities can't be tried without paying or an invite.

**Steal for monday.com.** Treat trial AI credits as a sample of the capability, not just a quota: let the user run the Pro-only AI jobs on their own boards.

### Sources (checked 2026-09-26)

- Clay: https://www.clay.com/pricing · https://university.clay.com/docs/plans-and-billing · https://www.clay.com/faq/what-do-i-get-in-the-free-trial · https://www.clay.com/faq/do-credits-roll-over
- Figma: https://www.figma.com/pricing-faq/ · https://help.figma.com/hc/en-us/articles/360046216313-Upgrade-or-downgrade-your-plan · https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits · https://forum.figma.com/suggest-a-feature-11/temporary-3-day-access-when-requesting-an-upgrade-please-turn-this-off-39239
- ClickUp: https://help.clickup.com/hc/en-us/articles/6303314345623-Upgrade-your-plan · https://help.clickup.com/hc/en-us/articles/10129535087383-Intro-to-pricing · https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits · https://feedback.clickup.com/feature-requests/p/limited-uses-warning
- Claude: https://claude.com/pricing · https://support.claude.com/en/articles/8325606-what-is-the-pro-plan · https://growsurf.com/blog/anthropic-claude-referral-program/

## Anti-patterns

| Anti-pattern | Why it fails | Who did it |
|---|---|---|
| Upgrade ask before the activation milestone | The user can't yet judge what they'd pay for | Common |
| Trial limit tighter than the plan after it | The evaluator hits the wall sooner in the trial than after | Clay: 50 rows in trial vs 200 on Free [Verified] |
| Two official pages giving different trial allowances | The offer can't be understood or supported | Clay: 1,000 vs 2,000 credits [Verified] |
| Credit balance ends the trial before the milestone | The trial fails before value is shown | Risk for any credit-metered trial, including monday's NT dual-gated trial (inference) |
| Calendar-only nudges that ignore behaviour | Nudges activated and stalled users alike | Common |
| Generic "Your trial is ending" | No personal loss, no reason to act | Common |
| No visible lower option at expiry | Reads as a trap | Common |
| Upgrade CTA with no price | Adds a click at the decision moment | Common |
| Temporary access with no admin off switch | The payer resents a grant they didn't approve | Figma [Reported — forum] |
| Many never-resetting per-feature allowances | A wall with no warning, weeks after exploring | ClickUp [Verified mechanics; complaint Reported] |
| AI held back to Free levels in the trial | The trial can't prove the AI it sells | Canva [Verified mechanics; the effect is inference] |

## Copy bank

Patterns only, for `improve-conversion-surfaces-copy`. Slots in `{braces}` — never fill them with invented monday numbers; trial terms come from [monday-context.md](../context/monday-context.md#trial).

| Moment | Pattern | Seen at | Example shape for monday.com |
|---|---|---|---|
| Trial start | Name the paid-only layer being unlocked, not "all features" | Clay | "Your {trial_length}-day Pro trial includes AI agents on your boards" |
| Phase 1 | Outcome-led, zero pressure, points at the milestone | — | "Set up your first automation — it takes {N} minutes" |
| Mid-trial, feature-anchored | Tie the prompt to the feature in use | ClickUp | "You've built {N} automations — they keep running on Pro after {trial_end_date}" |
| Mid-trial, IC on a team | Access now + admin loop | Figma | "You can use {feature} now — we've asked {admin_name} to keep it on" |
| Credit balance in trial | What the credits did, then what's left | Claude, ClickUp | "AI completed {N} tasks this trial · {credits_left} credits left until {trial_end_date}" |
| Two meters | Say which ends first | — | "{days_left} days or {credits_left} credits left — whichever comes first" |
| Expiry decision | Data stays; list what becomes read-only | ClickUp, Figma | "Everything you built stays. Choose a plan to keep editing {board_count} boards and running {automation_count} automations" |
| Expiry, credits | Say what happens to unused credits | Clay | "Unused trial credits end on {trial_end_date} — {plan} includes {plan_credits}/month" |
| Lower option | Name the cost honestly | — | "Continue on {lower_plan} — {what_stops}" |

## monday.com-specific notes

All facts from [context/monday-context.md](../context/monday-context.md).

- **Terms:** 14-day Pro trial, no card, can't be extended. Converts by trial expiry or a manual upgrade during the trial. At expiry the user must choose a plan; there's no auto-downgrade to Free without user action.
- **Trial credit amount isn't published.** Spec it as an open item with a slot (`{trial_credits}`), never a number. The 6,000-credit figure on plan-type articles is a legacy migration grant, not a trial allowance.
- **The NT 1,500-credit dual-gated trial** (ends at the day limit or the credit limit, whichever comes first) is internal-only: design for both meters, but never state it in external-facing copy until it's confirmed and published.
- **Aha signals:** first automation created, first AI action completed, first team member invited. Pick one as the primary milestone per spec.
- **Surfaces today:** a trial expiry modal at day 14 is live. **There's no mid-trial activation nudge**; that's the named gap. Phase 2 is the opportunity.
- **Credit translation in trial copy:** the official line (1,000 credits ≈ 50 resume screenings, 5 hours of meeting summaries), never "1 credit ≈ 1 AI action".
- **Agentic tasks:** state isn't preserved natively on depletion. A trial balance that runs out mid-run must not promise "your work is saved".
- **Cohort:** new users. Time pressure and loss framing ("keep what you've built") apply here, unlike the existing-user cohorts.
- **Primary metric:** Free→Pro conversion; trial activation rate is a secondary squad metric.

## Sources

Checked 2026-09-26 unless noted.

- Benchmarks: https://chartmogul.com/reports/saas-conversion-report/ · https://firstpagesage.com/seo-blog/saas-free-trial-conversion-rate-benchmarks/ · https://www.lennysnewsletter.com/p/what-is-a-good-activation-rate · https://www.pendo.io/product-benchmarks/ · https://www.revenuecat.com/state-of-subscription-apps · https://www.revenuecat.com/blog/growth/free-trial-length
- Canva (2026-09-25): https://www.canva.com/help/upgrade-to-canva-pro-or-business/ · https://www.canva.com/pricing/
- Linear (2026-09-25): https://linear.app/pricing · https://linear.app/docs/billing-and-plans · https://linear.app/integrations/linear-asks · https://lifestack.ai/blog/linear-pricing
- Notion (2026-09-25): https://www.notion.com/help/paid-plan-trials
- Cursor (2026-09-25): https://cursor.com/pricing · https://www.nxcode.io/resources/news/is-cursor-ai-free-plans-limits-worth-upgrading-2026
- AI-native set: see its Sources block above
- monday: [context/monday-context.md](../context/monday-context.md) · https://support.monday.com/hc/en-us/articles/360010594079-All-about-the-monday-com-free-trial
- Benchmarks added 2026-09-27: https://userpilot.com/blog/product-metrics-benchmark-report/ · https://www.growthunhinged.com/p/free-to-paid-conversion-report
