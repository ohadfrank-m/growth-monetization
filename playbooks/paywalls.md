# Paywalls & feature gates — CRO playbook

Surface type 2: the user tries to use a locked feature. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks). Tier and seat *limits* are [upgrade-triggers.md](upgrade-triggers.md); credit depletion is [credit-ui.md](credit-ui.md).

## Core rule

Show the value before the ask. A gate the user meets before seeing what the feature does is a wall; a gate after a preview is a moment of informed desire. In B2B, the person who hits the gate often can't pay — so every gate has a path to the person who can.

## Benchmarks

| Metric | Number | Tag | Applies to | Source | Checked |
|---|---|---|---|---|---|
| Day-35 download-to-paid, hard paywall vs. freemium | 12.11% vs. 2.18% (~75K apps) | [Verified] | mobile app | [RevenueCat State of Subscription Apps 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) | 2026-09-25 |

The one sourced paywall dataset is mobile subscription apps, not B2B SaaS — a direction for monday, never a target.

## Patterns

### Two gate models

- **Hard gate** (blocking modal): only when the feature is architecturally separate, can't be previewed, and intent is already explicit. Rare in B2B PLG.
- **Soft gate** (inline, contextual, non-blocking): monday's default. The gate appears after the user has seen or sampled what's being locked.

### Where the gate sits

| Trigger | Context | Key design constraint |
|---|---|---|
| Feature gate | User clicks a locked feature | Show the feature's value *before* the ask |
| Use-based limit | Free user samples a feature N times, then it locks | Warn before the lock — a silent lock reads as broken |
| Export / operationalize | User built something and tries to use it outside the product | The highest-intent moment: the value is already proven |
| Aha-moment upsell | Right after an activation milestone | Convert here |
| Time-based nudge | N days of free use | Lowest urgency — dismissible, never recurring |

### Screen components (by importance)

1. **Headline** — the outcome, not the plan. "Automate this every Monday" beats "Upgrade to Pro". Name only what the tier actually includes — a specific number beats "unlimited" unless it truly is.
2. **Feature preview** — screenshot, animation, sample output, or what the agent would *do* on the user's own data. Never skip it.
3. **Differentiator line** — one sentence on the pain this feature removes.
4. **Price anchoring** — the monthly equivalent even when billed annually; savings vs. monthly.
5. **Primary CTA** — specific: "Unlock {feature}", "Start {plan} — ${X}/mo".
6. **Secondary path** — continue free, compare plans, or "Not now" — always visible.
7. **Social proof** (optional) — close to the CTA.

### Preview and loss-anchor patterns

- **Blurred preview:** the locked content shown blurred behind the gate, so the user sees exactly what they'd unlock.
- **"Here's what you built":** at trial expiry or a limit, show the user's own work (files, boards, runs) as the loss anchor — real work, not abstract features.

### Copy patterns

**Headline formulas:** "Unlock {feature} to {outcome}" · "You're one step away from {benefit}" · "{feature} is a {plan} feature — here's what it does for your team" · "You've hit your free limit — here's what's next".
**CTA formulas:** "Unlock {feature}" (most specific) · "Start {plan} — ${X}/month" (price-transparent) · "Continue with {plan}" (trial-to-paid).
**Avoid:** "Upgrade now" (no benefit) · "Go Premium" (meaningless without context) · "Subscribe" (transactional, cold).

These are patterns for `improve-conversion-surfaces-copy`, not final copy.

### Format

| Format | When to use | Note |
|---|---|---|
| Modal | Feature gate or use-based limit the user triggered | High intent — works if the timing is right |
| Full page | Trial expiry, plan comparison | Deliberate decisions |
| Inline nudge | Low-urgency upsell, approaching a limit | Lower conversion, lower annoyance |
| Tooltip / hover | Discovery of locked features | Awareness, not conversion |

### Timing and frequency — owned here

- **Intent-triggered gates** (the user clicked the locked feature) show every time they click — the user asked. After 3 dismissals in 7 days, switch to a compact variant (preview collapsed, CTA kept).
- **Unprompted paywalls** (nudges the product initiates): at most one per session, and not again within 48 hours of a dismiss. Never re-show automatically on a timer regardless of behaviour.
- **Don't show** during onboarding (first session, before activation), or mid-task when the task doesn't need the locked feature.
- **Best moment:** right after the user completes something meaningful — the first board, the first automation run, the first agent result.

### IC vs. admin — the B2B decision

The IC who meets the gate usually can't buy; the admin who can buy never sees it. Required on every monday gate:

1. **Admin:** "Unlock {feature}" or "Start trial".
2. **IC:** "Notify admin" / "Ask {admin}" — pre-filled with the feature and what the IC was doing.
3. **The admin's notification** carries enough context to decide: who, what, where, why.

Figma's seat request is the reference implementation — see the AI-native set below. (Slack is often cited for an "ask your admin" upgrade flow, but its help center documents the opposite default: any member can upgrade a free workspace unless owners restrict it [Verified — [Slack help](https://slack.com/help/articles/360002044828-Manage-who-can-upgrade-a-free-workspace)]. Don't cite it for this.)

## Company teardowns

### Canva — the distributed crown

**What they ship [Verified — [Canva Apps SDK](https://www.canva.dev/docs/apps/design-guidelines/premium-apps/), [Canva help](https://www.canva.com/help/premium-elements/)].** A yellow crown marks premium templates, elements and features for free users. Premium **features** open the upgrade dialog right after the click. Premium **elements** can be placed in a design with a watermark; the user pays at removal or download — buy the element, buy all at download, or upgrade.

**Why it works (inference).** The paywall is spread across the product, and the element pattern is preview-first at its purest: the user sees the premium element in their own design before paying.

**Where it breaks.** A third-party reviewer describes free users scanning every result for the crown and choosing by availability rather than fit [Reported — [review](https://brendacadman.com/is-canva-pro-worth-it/)]. That's the friction cost of the pattern.

**Steal for monday.com.** Let a free user place the premium thing — the agent, the AI column — and see it work on their board, and gate the save, the schedule, or the export.

### Linear — capacity, not features

**What they ship [Verified — [Linear pricing](https://linear.app/pricing), [docs](https://linear.app/docs/billing-and-plans)].** Free includes the core product and Linear Agent; it gates mainly on scale — 250 issues, 2 teams, 10MB uploads — plus some Business-only intelligence and integrations. Above 250 issues, new issues can't be created. Only non-archived issues count, so auto-archiving frees capacity.

**Why it works (inference).** By the time the cap hits, the team depends on the product: the cost of not upgrading is losing something they already use.

**Steal for monday.com.** Gate on volume the team generates by using the product, and warn before the wall ([upgrade-triggers.md](upgrade-triggers.md) owns the thresholds).

### Notion — a gate at the wrong granularity

See [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling). For this surface: since May 2025, new Plus customers get only trial-level AI and full AI needs Business ($20/member/mo), which also bundles SAML SSO and admin controls [Verified — [pricing](https://www.notion.com/pricing); date Reported]. A user who wanted AI alone had to buy a tier of features they didn't need.

**Steal for monday.com.** The minimum purchase should match the value wanted. monday's Standard and Pro admins can buy a larger monthly credit package without changing tier — Basic is capped at 1,000 credits and Free has none ([monday-context.md](../context/monday-context.md)) — so a credit gate can offer "more credits" before "a new plan".

### Cursor — the frontier-model gate

**What they ship.** Frontier models are listed under Pro; the free Hobby plan has limited agent requests [Verified — [Cursor pricing](https://cursor.com/pricing)]. Free users meet the gate when they pick a frontier model or run out of Hobby limits [Reported — [nxcode](https://www.nxcode.io/resources/news/is-cursor-ai-free-plans-limits-worth-upgrading-2026)]. The prompt wording hasn't been captured [Teardown needed].

**Steal for monday.com.** Gate at the moment of intent — the user reaching for the capability — not on a schedule.

### ChatGPT — the capability difference as the gate

Free users run a lighter default model and see the stronger one as a Plus benefit [Reported — [MacRumors](https://www.macrumors.com/2026/08/06/chatgpt-free-unlimited-text-chats/); OpenAI pages blocked direct fetch]. Model names change monthly — re-verify before quoting. Exact gate wording not captured [Teardown needed].

### ClickUp — sample, then lock

ClickUp's free plan uses use-based limits: users can try features such as Gantt a set number of times before they lock [Verified — [ClickUp help](https://help.clickup.com/hc/en-us/articles/10129535087383-Intro-to-pricing)]. The reported pain point is the lock arriving with little warning [Reported — [ClickUp feedback board](https://feedback.clickup.com/feature-requests/p/limited-uses-warning)]. The AI-credit version of the same pattern is in the AI-native set below.

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture a live screenshot before citing in a review.

### At a glance — how each one gates AI value

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Gate type | Capability gate (CRM sync, API, phone) + volume | Seat gate + AI credit depletion | Sample-then-gate (one-time AI credits) | Usage gate with timed reset |
| What happens at the wall | Upgrade tier or top up | Seat request → admin; AI: paid features off until reset, free features stay on | Automatic AI features pause until add-on or credit pack | Blocking message with reset time + upgrade + usage credits |
| Exit options offered | 2 (upgrade, top-up) | 2–3 (request, wait, admin buys pool) | 2 (add-on, credit pack) | 3 (wait, upgrade, pay-as-you-go) |
| Degrades gracefully? | Partly | Yes — free AI features stay live | No — automatic features pause | Yes — nothing deleted, nothing charged |

### Clay — capability gates at the moment of export

**What they ship [Reported].** Free: 100 Data Credits + 500 Actions/mo, 200-row cap per table, no phone enrichment. CRM sync and API sit on Growth. 14-day Pro-level trial with 1,000 credits.

**Flow.** Build a table on Free → enrichment works → the gate appears when the user tries to *move* the value out (CRM push, API, bigger table).

**UI [Teardown needed].** Capture the CRM-sync gate and the 200-row limit state.

**Why it works.** Clay gates the *last mile*, not the first. Users experience the core value (enriched rows) on Free, then hit the wall when trying to operationalize it — the highest-intent moment.

**Where it breaks.** A tight row cap can be hit during evaluation, so some users may meet the gate before the aha moment (inference).

**Steal for monday.com.** Gate at the "operationalize" step: let the user run the agent and see the output on the board, then gate scheduling/recurring runs or cross-board automation. Show the output before the ask — this is the monday version of "show the value first."

### Figma — seat gate with instant temporary access

**What they ship [Verified].** Actions that need a higher seat trigger a seat request (or instant access if the admin enabled auto-approve). With manual approval, requesters get a one-time 3-day temporary access for each paid seat type while the admin reviews. For AI: Starter and View seats have a 150-credit daily cap on top of the monthly one; when credits run out, paid AI features are disabled until reset, free AI features stay available.

**Flow.** User clicks a gated action → request modal (reason field) → immediate 3-day access → admin gets email + in-app notification → approve/decline.

**UI.** Request modal is in-context; admin sees the request in the dashboard with origin, reason, current seat and time.

**Why it works.** The 3-day temporary access turns a *blocking* paywall into a *non-blocking* one. The user keeps working, the admin decides with the user's real usage already happening — and removing access after 3 days is loss aversion working on the admin.

**Where it breaks.** Temporary access is one-time per seat type; if declined, the user can't retry temporarily — the second wall is harder than the first.

**Steal for monday.com.** For IC-hits-Pro-feature gates on multi-seat accounts: "Try it now — we've let your admin know" with a short grace window. Converts the IC's intent into admin-facing evidence instead of a dead end.

### ClickUp — sample credits, then pause

**What they ship [Verified].** Free Forever gets 500 AI Super Credits per workspace; paid plans without an AI add-on get 1,000 credits per user. Neither resets. Once consumed, automatic AI features (Super Agents, AI Fields, AI Cards) pause until the workspace buys an AI add-on or credit pack.

**Flow.** User turns on an AI Field → it works on real tasks → credits deplete → field stops auto-filling → gate.

**UI [Teardown needed].** Capture the paused-AI-field state and its CTA.

**Why it works.** One-time credits are a trial that lives inside real work. The value is proven on the user's own tasks before the ask.

**Where it breaks.** "Pause" on an *automatic* feature is silent by nature — the field just stops filling. If the paused state isn't loud at the point of use, the user discovers it as broken data, not a paywall.

**Steal for monday.com.** One-time sample credits for AI Blocks would be the right structure, if monday offers them — but the paused state needs an inline marker on every affected column ("AI paused — out of credits · Get more"), not only a banner.

### Claude — the three-exit usage wall

**What they ship [Verified].** Warning first ("Approaching 5-hour limit"), then a blocking message with the time Claude can be used again. Exits: wait for the reset, upgrade (Free→Pro, Pro→Max 5x, Max 5x→20x — applies immediately, prorated), or continue on usage credits at API rates under a monthly cap. Free excludes Claude Code and the top models.

**Flow.** Warning → wall → choose: wait / upgrade / pay-as-you-go.

**UI.** Inline in the chat composer area — no full-screen modal. The reset time is the headline fact.

**Copy pattern.** Leads with *when you can continue*, then the paths. No guilt, no "unlock more."

**Why it works.** Showing the reset time makes waiting a legitimate choice, which makes paying feel voluntary. Three options match three user states: light user (wait), habitual heavy user (upgrade), occasional spike (usage credits).

**Where it breaks.** Weekly limit and session limit stack; a user with session headroom can still be blocked by the weekly cap, and the wall has to explain which one hit.

**Steal for monday.com.** Every credit/usage wall offers three exits mapped to user states: wait (if a reset exists), top-up (spike), upgrade package (habit). Lead with the task consequence and the resume path — never with the credit number.

### Copy bank — AI paywalls

| Moment | Pattern | Example for monday.com |
|---|---|---|
| Feature gate headline | Outcome, not plan | "Let this agent run every morning" (gate on scheduling) |
| Sample-credit depletion | What stopped, where | "AI stopped filling 'Summary' on 42 items — you've used your trial credits" |
| IC on multi-seat account | Keep working + admin loop | "Keep using it for now — we've asked [Admin name] to add it" |
| Usage wall headline | When you can continue | "You're out of credits for this cycle — they refill {reset date}" |
| Three-exit CTA set | Match the user state | "Add {N} credits" (admin) · "Move to a bigger package" (admin) · "Notify my admin" (IC) |

### Sources (checked 2026-09-24)

- Clay: https://salesmotion.io/blog/clay-pricing · https://www.landbase.com/blog/clay-pricing
- Figma: https://help.figma.com/hc/en-us/articles/360040453433-Make-a-seat-request · https://forum.figma.com/ask-the-community-7/free-figma-design-seat-account-to-edit-projects-for-how-many-days-38477 · https://www.vibecodingacademy.ai/blog/figma-ai-credits-everything-you-need-to-know
- ClickUp: https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits
- Claude: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work · https://www.ai-toolbox.co/claude-management-and-productivity/claude-usage-limits-2026

## Anti-patterns

| Anti-pattern | Why it fails | Who did it |
|---|---|---|
| Gate with no preview | The user can't tell what they'd gain | Common |
| Lock after N uses with no warning | Feels broken, not like an offer | ClickUp use-based limits [Reported] |
| Gate forces a whole bundled tier for one feature | Users route to alternatives instead of upgrading | [case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling) |
| Pushing a higher tier than the feature needs | Friction; feels like bait-and-switch | Common |
| No IC path ("Notify admin") | The IC is stuck; the admin never learns | Common in B2B |
| Hard-blocking modal mid-workflow | Destroys momentum | Common |
| Generic "This feature requires Pro" with no outcome | Functional, not motivating | Common |
| Promising "unlimited" when the tier is capped | A broken promise at the moment of purchase | Risk for monday — Pro automations are 25,000/mo, not unlimited |

## monday.com-specific notes

All facts from [context/monday-context.md](../context/monday-context.md).

- **AI Agents paywall:** show a preview of what the agent would *do* on the user's own board — the output — not just that it exists. Free has 0 AI credits, so the preview must not consume any.
- **Credit gates:** "You've used X of Y AI credits" is a metric, not a headline. Lead with what stops working.
- **Agentic flows:** a paywall that interrupts an agent mid-task breaks the experience. Use inline, non-blocking paths in agent contexts, and preserve task state.
- **Existing users at a credit wall** have no urgency lever (no deadline) — the hook is capability, not scarcity.
- **ICs can't self-purchase** — every gate an IC sees has "Notify admin".
- **Tier facts for gate copy:** Pro automations 25,000/mo, Enterprise 250,000/mo; Free and Basic have none; Basic credits are fixed at 1,000.

## Sources

Checked 2026-09-24 (AI-native set) and 2026-09-25 (everything else).

- RevenueCat: https://www.revenuecat.com/state-of-subscription-apps-2025
- Canva: https://www.canva.dev/docs/apps/design-guidelines/premium-apps/ · https://www.canva.com/help/premium-elements/ · https://brendacadman.com/is-canva-pro-worth-it/
- Linear: https://linear.app/pricing · https://linear.app/docs/billing-and-plans
- Notion: https://www.notion.com/pricing · https://www.usecarly.com/blog/notion-ai-pricing-change/
- Cursor: https://cursor.com/pricing · https://www.nxcode.io/resources/news/is-cursor-ai-free-plans-limits-worth-upgrading-2026
- ChatGPT: https://www.macrumors.com/2026/08/06/chatgpt-free-unlimited-text-chats/
- ClickUp: https://help.clickup.com/hc/en-us/articles/10129535087383-Intro-to-pricing · https://feedback.clickup.com/feature-requests/p/limited-uses-warning
- Slack: https://slack.com/help/articles/360002044828-Manage-who-can-upgrade-a-free-workspace
- Figma: https://help.figma.com/hc/en-us/articles/1500003870721-Approve-or-decline-seat-upgrade-requests · https://help.figma.com/hc/en-us/articles/4414038570007-Set-approval-settings-for-new-seats · https://forum.figma.com/suggest-a-feature-11/temporary-3-day-access-when-requesting-an-upgrade-please-turn-this-off-39239
