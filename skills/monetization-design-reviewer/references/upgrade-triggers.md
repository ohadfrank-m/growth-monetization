# Upgrade Triggers — Tier & Consumption CRO Reference

## Two Types of Upgrade Triggers

| Type | Mechanism | User State |
|------|-----------|-----------|
| **Tier upgrade** | User hits plan-level limit (seats, features, automations) | Frustrated or blocked |
| **Consumption / credit upgrade** | User is depleting a usage quota (AI credits, API calls, storage) | Anxious or mid-task |

These are *very different emotional states* and require different design approaches.

---

## Tier Upgrade Triggers

### When to Show
- User attempts to add a seat beyond plan limit
- User tries to enable a feature locked to higher tier
- Admin views usage dashboard and sees team at capacity
- Usage is consistently at 80–90% of plan limits (proactive nudge before the wall)

### Design Principles for Tier Gates
1. **Contextualize the limit** — "Your team has used 9 of 10 seats" is better than "You've reached your limit"
2. **Show the delta** — What does the next tier unlock? Make it specific, not a full plan comparison.
3. **Route to the right person** — In B2B, the user hitting the limit is often not the buyer. Provide a "notify admin" path alongside the upgrade CTA.
4. **Don't block the current task** — If the user was doing something, let them finish it (or save state) before presenting the upgrade.

### Tier Upgrade Screen Structure
```
[Context: what they hit]
"Your team is at 10/10 seats"

[Upgrade delta — what they get next]
"Pro includes up to 25 seats, plus:"
• [1-2 most relevant features for this team]

[Social proof if available]
"Teams like [similar company type] move to Pro when they reach this point"

[Primary CTA]  [Notify admin]
[Maybe later — dismiss]
```

### Proactive vs Reactive Triggers
- **Reactive** (at 100%): necessary but lowest-satisfaction moment. User is already blocked.
- **Proactive** (at 70–80%): higher satisfaction, higher CVR. User isn't frustrated yet.
- **Recommendation**: Show a non-blocking nudge at 75%, a more prominent prompt at 90%, full gate at 100%.

---

## Consumption / Credit Upgrade Triggers

### The Credit Psychology Problem
Credits create a different anxiety than seat limits. Users fear *running out mid-task* more than they fear hitting a hard cap. Design for the anxiety state, not the depleted state.

### Credit UI Patterns

**Usage indicator (persistent, ambient):**
- Always-visible credit counter in the UI (not just in settings)
- Color shift: green → yellow → orange → red as credits deplete
- Tooltip on hover: "At this rate, you'll run out in ~3 days"

**Proactive nudge (at 30–40% remaining):**
- Non-blocking banner or sidebar card
- Framing: "You're getting great value from AI — here's how to keep the momentum"
- Show what credits are being used on (makes the value tangible)

**Urgent nudge (at 10–15% remaining):**
- More prominent, persistent (but still dismissible)
- Specific: "You have ~X AI actions left. After that, [specific thing] stops working."
- Include preview of what buying credits unlocks

**Depleted state:**
- Most sensitive moment — user is blocked
- Never just show an error. Show: what stopped, why, how to fix it immediately.
- Provide a one-click "get more credits" path with pre-filled quantity

### Credit Upgrade Screen Structure
```
[What stopped / what's at risk]
"You've used all your AI credits for this billing period"

[What they were getting]
"This month you: ran 47 automations, summarized 23 docs, built 3 AI workflows"
(value recap — anchors the purchase)

[Options — simple]
[Buy 500 credits — $X]  [Buy 2,000 credits — $Y (best value)]
OR
[Upgrade to Pro — includes X credits/month]

[Secondary: when credits reset if applicable]
"Your credits reset on June 1 — or get more now"
```

### Credit Pricing Presentation
- Show per-credit price at each tier to enable comparison
- Highlight the "best value" option (volume pricing) — anchors toward higher purchase
- If upgrading to a plan includes credits, show the effective credit cost vs buying standalone
- Avoid presenting credits purely as a number without context ("500 credits" means nothing without "≈ 500 AI actions")

---

## Benchmarks

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Tier gate → upgrade CVR | <5% | 8–15% | 20%+ |
| Proactive nudge (75%) → upgrade CVR | <3% | 5–10% | 15%+ |
| Credit depletion → purchase CVR | <10% | 15–25% | 30%+ |
| Credit warning (30% left) → purchase CVR | <5% | 8–12% | 18%+ |

---

## Best-in-Class Examples

**Notion AI credits** — Running low banner in the editor sidebar. Doesn't interrupt writing. Shows "X AI responses remaining this month." One-click "Get more" button. Non-blocking, contextual.

**OpenAI API usage** — Dashboard shows credit burn rate with projection ("at this rate, runs out in X days"). Rate-based forecasting dramatically increases proactive top-up behavior.

**GitHub Copilot** (Business) — Seat limit hit triggers email to org admin AND in-product notification to the blocked user with a "request access" flow. Separates the user-facing experience from the buyer-facing action.

**Zapier** (task limits) — Zap-level usage bar visible on every automation. Turns invisible usage into a tangible, always-present signal. Normalizes awareness of limits before they're hit.

---

## monday.com Specific Notes

- **AI credits are new** (May 2026 launch) — users have no prior mental model. First-ever credit depletion experience must be educational, not just transactional.
- **New users (14-day trial):** Have urgency lever (time). Credit UI should reinforce "you're getting value now — don't let it stop." 
- **Existing users (credit balance, no time limit):** No urgency lever. Must create desire, not FOMO. Show value received, not scarcity.
- **Agent mid-task interruption:** If a Sidekick agent runs out of credits mid-task, this is a critical experience. Must: save task state, explain what happened, provide immediate path to resume. Never just fail silently.
- **Admin vs. end user:** In B2B, end users hit credit walls but admins hold the credit wallet. Design must include a "notify your admin" path that generates an actionable admin notification, not just a dead end.

---

## Credit Metering, Top-Ups & Forecasting — UI Mechanics

This section covers the surfaces monday's monetization teams build now: the always-on meter, burn-rate forecasting, top-up flows, credit-to-task translation, and dual-gated trials. The credit *psychology* is above; this is the *mechanics*.

### The always-on credit meter
The persistent meter is the single most important credit surface — it sets the mental model before any upgrade moment.

- **Placement:** visible in the primary workspace chrome, not buried in settings. If a user has to hunt for their balance, every downstream depletion feels like a surprise.
- **Always translate:** never show a bare number. "820 credits" alone is meaningless. Pair with task translation: "820 credits ≈ ~160 agent actions." The translation is the product's job, not the user's math.
- **State progression:** green → yellow → orange → red as balance depletes. The color shift is the ambient early warning; it should change *before* any modal fires.
- **Hover/tap detail:** reveal burn context — "You've used 340 credits this week, mostly on document summaries."
- **Score impact:** a meter that shows a number with no translation is an automatic Value-clarity ≤2.

### Burn-rate forecasting
Forecasting is what converts passive awareness into proactive top-up. It is the highest-leverage credit UI pattern.

- **Show the projection, not just the balance:** "At your current rate, you'll run out in ~4 days." Rate-based framing drives top-ups far more than a static remaining count.
- **Accuracy matters more than precision:** a forecast that's visibly wrong destroys trust worse than no forecast. Use a conservative range ("~3–5 days") over a false-precise single number if the data is noisy.
- **Tie the forecast to a moment:** "…which means you'll run out before your Friday report." Anchoring the projection to a known deadline sharply increases action.

### Credit-to-task translation (a live monday workstream)
This is the difference between a meter users understand and one they resent.

- Every credit-denominated surface — meter, depletion, top-up, pricing page, trial — must express credits in tasks the user recognizes.
- Translation must be **honest and stable:** if "1 agent action ≈ 5 credits" on the pricing page but the meter implies a different rate, trust breaks. One rate, everywhere.
- Prefer the user's own recent actions as the unit ("≈ 40 more document summaries at your usage") over abstract catalog actions.

### Top-up flow
The purchase moment when a user chooses to add credits rather than upgrade a plan.

- **Default the recommended quantity:** pre-select the "best value" tier — most users anchor to the default. Don't present a blank quantity field.
- **Show per-credit price at each tier** so volume value is legible; label the volume tier "best value" explicitly.
- **Show the plan-upgrade alternative alongside:** "Or upgrade to Pro — includes X credits/month at a lower effective rate." A pure top-up path hides the often-better subscription option.
- **One-click, no re-entry:** payment on file should mean top-up is a single confirm. Re-entering card details at the depletion moment is a conversion killer.
- **Confirm what they just bought in tasks:** "Added 2,000 credits ≈ ~400 agent actions." Close the loop in the same unit.

### Dual-gated trial display (monday-specific)
The 1,500-credit dual-gated trial structure gates on both time and credits. The UI must make **both** gates legible without creating double anxiety.

- Show the binding constraint — whichever runs out first. If credits will deplete before the trial clock, lead with credits; if time is shorter, lead with days.
- Don't show two racing countdowns with equal weight; that reads as a trap. One primary constraint, one secondary line.
- On the tighter gate, pair with the value recap and the clear post-trial path (buy credits / pick a plan).

### Agentic mid-task depletion (critical experience)
If a Sidekick agent exhausts credits mid-task, this is the highest-stakes credit moment.

- **Never fail silently.** Save task state, explain what happened in one line, and offer an immediate resume path.
- **Non-blocking where possible:** an inline "you're out of credits — top up to let the agent finish" beats a full-screen error that discards the in-progress work.
- **Preserve the artifact:** whatever the agent produced up to the depletion point must survive. Losing partial work turns a top-up moment into a churn moment.

### Metering-specific benchmarks

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Forecast-shown → proactive top-up CVR | <5% | 8–14% | 20%+ |
| Top-up flow completion (payment on file) | <40% | 55–70% | 80%+ |
| Meter comprehension (users who can state what a credit buys) | <30% | 50–65% | 80%+ |
| Mid-task depletion → resume (vs. abandon) | <30% | 45–60% | 75%+ |

### Best-in-class metering references

**OpenAI API dashboard** — burn-rate projection ("at this rate, runs out in X days") is the model for forecasting. Rate framing drives top-ups better than raw balance.

**Anthropic / Claude usage** — plain-language remaining-usage framing tied to the current session, not abstract token counts.

**Vercel** — usage dashboard with per-resource meters and clear overage pricing shown *before* the overage happens; no surprise bills.

**Linear (cycle capacity)** — turns invisible consumption into an always-present, low-anxiety signal, normalizing awareness before any limit is hit.
