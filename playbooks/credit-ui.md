# Credit / consumption UI — CRO playbook

Surface type 5: running low on credits, credit meter, metering dashboard, top-up flow. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

The highest-priority surface type for monday.com given the AI Agents launch, and the one with the most novel UX problems in this plugin — most companies don't yet have a settled pattern for this.

This file was previously forked across two skills with different benchmarks and different best-in-class examples for the same surface. It's merged here as the single source; don't re-fork it.

## The credit psychology problem

Credits create a different anxiety than seat limits. Users fear *running out mid-task* more than they fear hitting a hard cap. Design for the anxiety state, not the depleted state. Tier upgrade triggers (a blocked-and-frustrated moment — see [upgrade-triggers.md](upgrade-triggers.md)) and credit depletion (an anxious, mid-task moment) require different design approaches even though both are "usage limits."

## When this surface appears

- **Warning state:** credit balance drops below warning threshold (e.g., 20% or 50 credits remaining)
- **Depletion state:** credit balance reaches 0 mid-session or mid-task
- **Depletion mid-task:** balance hits 0 while an AI agent is actively running — highest-risk moment
- **Credit meter (persistent):** visible in dashboard or sidebar at all times when credits are < 100% or < threshold
- **Top-up flow:** user initiates a credit purchase (self-serve or admin)
- **Post-top-up confirmation:** credits added, task can resume

## The always-on credit meter

The persistent meter is the single most important credit surface — it sets the mental model before any upgrade moment.

- **Placement:** visible in the primary workspace chrome, not buried in settings. If a user has to hunt for their balance, every downstream depletion feels like a surprise.
- **Always translate:** never show a bare number. "820 credits" alone is meaningless. Pair with task translation: "820 credits ≈ ~160 agent actions." The translation is the product's job, not the user's math.
- **State progression:** healthy → warning → critical → depleted (color shift green → yellow → orange → red). The color shift is the ambient early warning; it should change *before* any modal fires.
- **Hover/tap detail:** reveal burn context — "You've used 340 credits this week, mostly on document summaries."
- **Scoring note:** a meter that shows a number with no translation is an automatic value-clarity ≤2 on the design-reviewer rubric.

## Burn-rate forecasting

Forecasting is what converts passive awareness into proactive top-up. It's the highest-leverage credit UI pattern.

- **Show the projection, not just the balance:** "At your current rate, you'll run out in ~4 days." Rate-based framing drives top-ups far more than a static remaining count.
- **Accuracy matters more than precision:** a forecast that's visibly wrong destroys trust worse than no forecast. Use a conservative range ("~3–5 days") over a false-precise single number if the data is noisy.
- **Tie the forecast to a moment:** "…which means you'll run out before your Friday report." Anchoring the projection to a known deadline sharply increases action.

## Credit-to-task translation

The difference between a meter users understand and one they resent.

- Every credit-denominated surface — meter, depletion, top-up, pricing page, trial — must express credits in tasks the user recognizes.
- Translation must be **honest and stable:** if "1 agent action ≈ 5 credits" on the pricing page but the meter implies a different rate, trust breaks. One rate, everywhere.
- Prefer the user's own recent actions as the unit ("≈ 40 more document summaries at your usage") over abstract catalog actions.

## Warning → depletion progression

**Proactive nudge (30–40% remaining):** non-blocking banner or sidebar card. Framing: "You're getting great value from AI — here's how to keep the momentum." Show what credits are being used on — makes the value tangible.

**Urgent nudge (10–15% remaining):** more prominent, persistent, but still dismissible. Specific: "You have ~X AI actions left. After that, [specific thing] stops working." Include a preview of what buying credits unlocks.

**Depleted state:** the most sensitive moment — user is blocked. Never just show an error. Show what stopped, why, and how to fix it immediately. Provide a one-click "get more credits" path with pre-filled quantity.

Best-in-class pattern for the warning state — **Notion AI**: running-low banner lives in the editor sidebar, doesn't interrupt writing. Shows "X AI responses remaining this month." One-click "Get more" button. Non-blocking, contextual.

Best-in-class pattern for progressive states — **HubSpot AI**: three states — healthy (no meter visible), warning (meter appears at 20%), critical (meter turns red + pulse animation), each with progressively stronger messaging. Users aren't surprised by depletion; the warning state gives them time to act.

Best-in-class pattern for depletion messaging — **Intercom Fin**: leads with the task, not the credits — "Your AI conversation agent has paused — you've run out of AI credits", not "You have 0 credits." Users understand what stopped in terms they care about.

## Top-up flow

The purchase moment when a user chooses to add credits rather than upgrade a plan.

- **Default the recommended quantity:** pre-select the "best value" tier — most users anchor to the default. Don't present a blank quantity field.
- **Show per-credit price at each tier** so volume value is legible; label the volume tier "best value" explicitly.
- **Show the plan-upgrade alternative alongside:** "Or upgrade to Pro — includes X credits/month at a lower effective rate." A pure top-up path hides the often-better subscription option.
- **One-click, no re-entry:** payment on file should mean top-up is a single confirm. Re-entering card details at the depletion moment is a conversion killer.
- **Confirm what they just bought in tasks:** "Added 2,000 credits ≈ ~400 agent actions." Close the loop in the same unit.

```
[Modal:]
  [Headline: "Top up AI credits"]
  [Current balance: "0 credits remaining"]
  [Package options:]
    ○ 500 credits — $X/mo  (≈ 500 AI actions)
    ● 2,000 credits — $X/mo  (≈ 2,000 AI actions)  [BEST VALUE badge]
    ○ 5,000 credits — $X/mo  (≈ 5,000 AI actions)
  [Selected package summary: "2,000 credits for $X — billed monthly, cancel anytime"]
  [CTA: "Top up and resume"]  [Dismiss: "Notify my admin instead"]
```
Critical elements: three package options (anchors mid-tier choice), task translation on every option, "resume" in the CTA, admin path as secondary.

## Agentic mid-task depletion (critical experience)

If an agent exhausts credits mid-task, this is the highest-stakes credit moment in the product.

- **Never fail silently.** Save task state, explain what happened in one line, and offer an immediate resume path.
- **Non-blocking where possible:** an inline "you're out of credits — top up to let the agent finish" beats a full-screen error that discards the in-progress work.
- **Preserve the artifact.** Whatever the agent produced up to the depletion point must survive. Losing partial work turns a top-up moment into a churn moment.
- **Post-purchase resume:** auto-resume or an explicit "Resume task" CTA — a user who has credits but doesn't know how to continue is a support ticket waiting to happen.

```
[Inline banner in agent run interface:]
[⚠️] "Your AI agent has paused — you're out of credits"
[Subtext: "{Agent name} stopped at step {N}. Top up to continue where you left off."]
[CTA: "Top up credits — {package size} for ${price}"]  [Secondary: "Notify admin"]
[Small: "Your work is saved"]
```

## Dual-gated trial display (monday-specific)

The 1,500-credit dual-gated trial structure gates on both time and credits. The UI must make **both** gates legible without creating double anxiety.

- Show the binding constraint — whichever runs out first. If credits will deplete before the trial clock, lead with credits; if time is shorter, lead with days.
- Don't show two racing countdowns with equal weight — that reads as a trap. One primary constraint, one secondary line.
- On the tighter gate, pair with the value recap and the clear post-trial path (buy credits / pick a plan).

## Benchmarks

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Credit depletion → purchase CVR | <10% | 15–25% | 30%+ |
| Credit warning (30% left) → purchase CVR | <5% | 8–12% | 18%+ |
| Forecast-shown → proactive top-up CVR | <5% | 8–14% | 20%+ |
| Top-up flow completion (payment on file) | <40% | 55–70% | 80%+ |
| Meter comprehension (users who can state what a credit buys) | <30% | 50–65% | 80%+ |
| Mid-task depletion → resume (vs. abandon) | <30% | 45–60% | 75%+ |

## Best-in-class metering references

**OpenAI API dashboard** — burn-rate projection ("at this rate, runs out in X days") is the model for forecasting. Rate framing drives top-ups better than raw balance.

**Anthropic / Claude usage** — plain-language remaining-usage framing tied to the current session, not abstract token counts.

**Vercel** — usage dashboard with per-resource meters and clear overage pricing shown *before* the overage happens; no surprise bills.

**Linear (cycle capacity)** — turns invisible consumption into an always-present, low-anxiety signal, normalizing awareness before any limit is hit.

## Credit pricing presentation

- Show per-credit price at each tier to enable comparison.
- Highlight the "best value" option (volume pricing) — anchors toward higher purchase.
- If upgrading to a plan includes credits, show the effective credit cost vs. buying standalone.
- Avoid presenting credits purely as a number without context — "500 credits" means nothing without "≈ 500 AI actions."

## Anti-patterns

| Anti-pattern | Specific failure | Fix |
|-------------|-----------------|-----|
| Bare credit number | "500 credits" with no task translation | Always add "≈ 500 AI actions" |
| Hard stop mid-agent-task | Task fails, state lost | Save state, pause task, offer resume |
| Full-screen blocking modal in agentic flow | Breaks flow, scary UX | Inline banner at warning threshold |
| No IC → admin path | IC dead-ends, admin never knows | "Notify admin" button always present |
| Post-purchase no resume path | User has credits, doesn't know how to continue | Auto-resume or explicit "Resume task" CTA |
| Credit expiry not communicated | Surprise at month end | Show expiry prominently if credits don't roll over |

## monday.com-specific notes

- AI credits are new (May 2026 launch) — users have no prior mental model. The first-ever credit depletion experience must be educational, not just transactional.
- New users (14-day trial) have an urgency lever (time). Credit UI should reinforce "you're getting value now — don't let it stop."
- Existing users (credit balance, no time limit) have no urgency lever. Must create desire, not FOMO — show value received, not scarcity.
- Agent mid-task interruption: if a Sidekick agent runs out of credits mid-task, this is a critical experience. Must save task state, explain what happened, and provide an immediate path to resume. Never just fail silently.
- Admin vs. end user: in B2B, end users hit credit walls but admins hold the credit wallet. Every credit-facing surface needs a "notify your admin" path that generates an actionable admin notification, not a dead end.
