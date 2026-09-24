# Paywalls & feature gates — CRO playbook

Surface type 2. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

## Core principle
A paywall is a value conversation, not a wall. The best paywalls feel like a natural offer, not an interruption. Users should leave thinking "that makes sense" not "I got blocked."

## Paywall trigger types

| Trigger | Context | Key design constraint |
|---------|---------|----------------------|
| Feature gate | User clicks locked feature | Must show the feature value *before* the ask |
| Usage cap | User hits limit (seats, items, actions) | Show progress toward limit proactively — not just at 100% |
| Trial expiry | Trial period ending | Personalize with what they built/used during trial |
| Time-based nudge | N days of free use | Lowest urgency — must be dismissible, never recurring |
| Aha moment upsell | After key activation milestone | Highest intent — convert here |

## Paywall screen components (ranked by importance)

1. **Headline** — benefit-led, not feature-led. "Get unlimited automations" > "Upgrade to Pro"
2. **Feature preview** — screenshot, animation, or description of what they're unlocking. Never skip this.
3. **Differentiator line** — one sentence on why this feature exists / what pain it solves
4. **Price anchoring** — show monthly equivalent even if billed annually. Show savings vs monthly.
5. **Primary CTA** — specific: "Unlock Automations", "Start Pro — $X/mo"
6. **Secondary path** — downgrade, continue free, or "remind me later" — must be visible
7. **Social proof** (optional but lifts) — "Used by 50,000+ teams"

## Modal vs. full-page vs. inline

| Format | When to use | Conversion notes |
|--------|------------|-----------------|
| Modal | Feature gate, usage cap | High intent context — converts well if triggered correctly |
| Full page | Trial expiry, plan comparison | More deliberate — use when user has time to decide |
| Inline nudge | Low-urgency upsell, approaching limit | Non-blocking — lower CVR but lower annoyance |
| Tooltip / hover | Discovery of locked features | Awareness, not conversion — don't over-optimize here |

## Copy patterns that work

**Headline formulas:**
- "Unlock [Feature] to [Outcome]"
- "You're one step away from [Benefit]"
- "[Feature] is a Pro feature — here's why teams love it"
- "You've hit your free limit — here's what's next"

**CTA formulas:**
- "Unlock [Feature Name]" (most specific, highest CVR)
- "Start [Plan] — $X/month" (price-transparent, builds trust)
- "Continue with Pro" (trial-to-paid context)

**Avoid:**
- "Upgrade now" — zero benefit signal
- "Go Premium" — meaningless without context
- "Subscribe" — transactional, cold

## Timing rules

- **Do not show** during onboarding (first session, before activation)
- **Do not show** mid-task if the task doesn't require the locked feature
- **Wait 24–48h** after a dismiss before showing again
- **Session cap:** max 1 paywall per session (excluding feature gates triggered by user intent)
- **Best moment:** immediately after the user has completed something meaningful (just created their first board, just ran their first automation, etc.)

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Gate with no feature preview | User can't tell what they'd gain |
| Pushing a higher tier than needed to unlock the feature | Friction, feels like a bait-and-switch |
| Generic "This feature requires Pro" with no outcome named | Functional, not motivating |

## Benchmarks

*Directional only — these figures pre-date the evidence-tag standard and carry no source. Don't cite them as fact in a review; the sourced material is in the AI-native reference set below.*

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Paywall → upgrade CTR | <3% | 5–10% | 15%+ |
| Trial expiry paywall CVR | <10% | 15–25% | 30%+ |
| Feature gate CTR (high intent) | <8% | 12–18% | 25%+ |

## Best-in-class examples

*Pre-dates the evidence-tag standard — the patterns are sound, but any figures here are unsourced. Tagged teardowns are in the AI-native reference set below.*

**Notion** — Feature gate paywalls show a live preview of the blocked content blurred behind the modal. User can see exactly what they're missing. CVR benchmark: ~18–22% on database-related gates.

**Figma** — Trial expiry screen uses "Here's what you built" personalization with actual file thumbnails. Anchors loss aversion to real work, not abstract features.

**Linear** — Usage cap modals show a progress bar with team context ("Your team has created 95/100 issues this month"). Social proof of team usage increases urgency without guilt.

**Loom** — "You've watched this 3x" re-engagement paywall on high-value content. Intent signal used to time the ask.

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

**Where it breaks.** A 200-row cap is hit during evaluation for most real lists, so some users meet the gate before the aha moment.

**Steal for monday.com.** Gate at the "operationalize" step: let the user run the agent and see the output on the board, then gate scheduling/recurring runs or cross-board automation. Show the output before the ask — this is the monday version of "show the value first."

### Figma — seat gate with instant temporary access

**What they ship [Verified].** Actions that need a higher seat trigger a seat request (or instant access if the admin enabled auto-approve). With manual approval, requesters get a one-time 3-day temporary access for each paid seat type while the admin reviews. For AI: Starter and View seats have a 150-credit daily cap on top of the monthly one; when credits run out, paid AI features are disabled until reset, free AI features stay available.

**Flow.** User clicks a gated action → request modal (reason field) → immediate 3-day access → admin gets email + in-app notification → approve/decline.

**UI.** Request modal is in-context; admin sees the request in the dashboard with origin, reason, current seat, time, and cost.

**Why it works.** The 3-day temporary access turns a *blocking* paywall into a *non-blocking* one. The user keeps working, the admin decides with the user's real usage already happening — and removing access after 3 days is loss aversion working on the admin.

**Where it breaks.** Temporary access is one-time per seat type; if declined, the user can't retry temporarily — the second wall is harder than the first.

**Steal for monday.com.** For IC-hits-Pro-feature gates on multi-seat accounts: "Try it now — we've let your admin know" with a short grace window. Converts the IC's intent into admin-facing evidence instead of a dead end.

### ClickUp — sample credits, then pause

**What they ship [Verified].** Free Forever gets 500 AI Super Credits per workspace; paid plans without an AI add-on get 1,000 credits per user. Neither resets. Once consumed, automatic AI features (Super Agents, AI Fields, AI Cards) pause until the workspace buys an AI add-on or credit pack.

**Flow.** User turns on an AI Field → it works on real tasks → credits deplete → field stops auto-filling → gate.

**UI [Teardown needed].** Capture the paused-AI-field state and its CTA.

**Why it works.** One-time credits are a trial that lives inside real work. The value is proven on the user's own tasks before the ask.

**Where it breaks.** "Pause" on an *automatic* feature is silent by nature — the field just stops filling. If the paused state isn't loud at the point of use, the user discovers it as broken data, not a paywall.

**Steal for monday.com.** Sample credits for AI Blocks on existing (pre-May-2026) accounts is the right structure — but the paused state needs an inline marker on every affected column ("AI paused — out of credits · Get more"), not only a banner.

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
| Usage wall headline | When you can continue | "You're out of credits for this cycle — they refill on [date]" |
| Three-exit CTA set | Match the user state | "Top up 2,000 credits" · "Move to a bigger package" · "Notify my admin" |

### Sources (checked 2026-09-24)

- Clay: https://salesmotion.io/blog/clay-pricing · https://www.landbase.com/blog/clay-pricing
- Figma: https://help.figma.com/hc/en-us/articles/360040453433-Make-a-seat-request · https://forum.figma.com/ask-the-community-7/free-figma-design-seat-account-to-edit-projects-for-how-many-days-38477 · https://www.vibecodingacademy.ai/blog/figma-ai-credits-everything-you-need-to-know
- ClickUp: https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits
- Claude: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work · https://www.ai-toolbox.co/claude-management-and-productivity/claude-usage-limits-2026

## monday.com-specific notes

- AI Agents paywall: must show a preview of what the agent would *do* — not just that it exists. Show the output.
- Credit gates: "You've used X of Y AI credits" is not a paywall headline — it's a metric. Lead with what stops working when credits run out.
- Agentic flows: if a paywall interrupts an agent mid-task, the experience is broken. Design for non-blocking upgrade paths in agent contexts — inline banner, not full-screen modal.
- Existing users hitting credit walls: these users have no urgency lever (time-unlimited balance). The hook must be capability, not scarcity.
