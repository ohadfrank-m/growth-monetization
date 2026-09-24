# Cancellation & downgrade — CRO playbook

Surface type 6. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

## The goal
Save customers worth saving. Let go of those who aren't a fit. Never manipulate. Always learn.

A good cancel flow recovers 25–35% of at-risk customers — not through dark patterns, but by matching the right offer to the real reason.

## Cancel flow architecture

```
Cancel intent → Exit survey → Dynamic save offer → Confirmation → Post-cancel
```

Every step is optional to the user. Never trap.

## Step 1: cancel intent interception

The moment the user clicks "Cancel subscription" is the highest-intent retention moment in the entire product lifecycle. Most products waste it with a generic "Are you sure?"

**Better intercept patterns:**
- **Value recap card**: "Before you go — here's what your team accomplished this month: [personalized stats]"
- **Pause offer**: "Need a break? Pause your account for up to 3 months" — shown before the survey for high-engagement users
- **Direct routing**: For accounts flagged as at-risk by health score, route to CS before the cancel flow

**What not to do:**
- Immediate confirmation dialog with no save attempt
- "Are you sure you want to leave your team behind?" — guilt, not value
- Multi-step confirmation maze designed to confuse (FTC Click-to-Cancel rule violation risk)

## Step 2: exit survey

**One question. 5–8 options. Optional free text.**

| Reason | Save offer to show |
|--------|-------------------|
| Too expensive | Discount (20–30% for 2–3 months) OR downgrade offer |
| Not using it enough | Pause (1–3 months) OR free onboarding session |
| Missing a feature | Roadmap preview + workaround OR direct feature feedback |
| Switching to competitor | Competitive comparison + targeted discount |
| Technical issues / bugs | Immediate CS escalation — don't offer discount, fix the problem |
| Temporary / seasonal | Pause — this is exactly the use case for it |
| Business closed / changed | No save offer. Acknowledge gracefully. Ask for feedback. |
| Other | Free text, surface to product team |

**Survey copy principles:**
- Frame as "Help us improve" not "Why are you abandoning us?"
- No negative options ("I hate the product") — keep it neutral and diagnostic
- Make it feel fast — "Takes 30 seconds"

## Step 3: dynamic save offer

Match the offer to the reason. A discount won't save someone who isn't using the product.

**Discount offer:** 20–30% off for 2–3 months is the sweet spot. Show the dollar amount saved, not just the percentage. Time-limit the offer. Avoid 50%+ discounts — trains cancellation behavior.

**Pause offer:** 1–3 months max (longer pauses rarely reactivate). Keep data, settings, and integrations intact. Auto-reactivation with 7-day advance notice email. 60–80% of pausers return to active status.

**Downgrade offer:** Frame as "right-size your plan" not "downgrade". Show explicitly what they *keep* (more important than what they lose). Make the path back up visible immediately.

**Feature/roadmap offer:** Show the specific feature they're missing + ETA if available. "Here's the workaround teams use today" reduces churn while feature ships. Offer to notify them when it launches.

**High-value account offer:** For top 20% by MRR, route to live CS chat or scheduled call. Personal email from account manager > automated offer. Response rate 3–5x higher than automated flows for this segment.

## Step 4: cancellation confirmation

If they still want to cancel after all of the above — make it clean.

**Must include:** clear statement of when access ends (exact date, not "at end of billing period"); what happens to their data (retention period, export option); reactivation path ("You can come back anytime — your data will be waiting"); one final low-friction offer if not already shown.

**Must not include:** hidden confirmation steps; auto-checked boxes that re-subscribe them; confusing language about what "cancellation" means.

## Step 5: post-cancel experience

**Immediately after cancel:** confirmation email with access end date and data retention info; easy "I changed my mind" reactivation link (active for 48–72h); clear reactivation path in the app (don't hide the "reactivate" button).

**Win-back sequence (7 / 30 / 90 days):** Day 7 — "We've made some improvements — here's what's new". Day 30 — "Your data is still here — come back anytime". Day 90 — special reactivation offer (time-limited).

## Downgrade experience (separate from cancel)

Downgrade is often treated as a mini-cancel. It shouldn't be. A user who downgrades and stays is worth more than one who churns.

**Downgrade flow design:**
1. Show what they're losing — specific features, not plan names
2. Show what they're keeping — lead with this if the lower plan is still solid
3. Offer a delay — "Stay on Pro for 30 more days while you evaluate" (especially good if renewal is near)
4. Confirm the specific date — "Your plan changes on [date], not immediately"
5. No guilt — "Totally fine — here's what to expect"

**Loss framing:** Loss aversion is real but must be used ethically. "You'll lose access to: [list of features currently in use]" — personalized to actual usage. "You've never used [feature]" — omit from the loss list (don't manufacture fear). Show data loss risk separately and prominently if applicable (exports, integrations).

## Benchmarks

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Cancel flow save rate | <10% | 25–35% | 40%+ |
| Pause offer acceptance | <10% | 15–25% | 30%+ |
| Discount offer acceptance | <10% | 20–30% | 35%+ |
| Post-cancel reactivation (90 days) | <5% | 10–15% | 20%+ |
| Downgrade → upgrade within 90 days | <5% | 12–18% | 25%+ |

## Best-in-class examples

**Duolingo** — Cancel flow shows personalized streak data ("You've learned for 47 days straight — here's what you'd lose"). Loss aversion anchored to real behavior, not abstract features.

**Spotify** — Pause offer shown before exit survey for users who haven't opened the app in 30+ days. Matches the inactivity signal to the right offer.

**HubSpot** — For high-value accounts, cancel click routes to a "let's talk" flow with live CS availability shown. 3x higher save rate vs automated discount offers for this segment.

**Notion** — Downgrade confirmation shows feature-by-feature "what you keep / what you lose" with actual data from the user's workspace (e.g., "You have 3 databases that require Pro — here's what happens to them").

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Hidden or buried cancel button | Dark pattern, erodes trust |
| More than one "Are you sure?" step | Confirmation maze — regulatory risk (FTC Click-to-Cancel) |
| Guilt-trip copy | Brand damage, no lift evidence |
| Offering the same discount regardless of reason | A discount won't save someone who isn't using the product |
| No downgrade option — only "stay" or "cancel" | Forces churn that a right-sized plan could have prevented |

## monday.com-specific notes

- AI Agents context: if a user is canceling because agents didn't deliver value, a discount won't help. The save offer should be a re-onboarding session with a CS specialist.
- Credit-based model: cancellation after credit depletion is a specific pattern — user exhausted their allocation and didn't see enough value to buy more. The save offer here is a free credit top-up + guided value moment, not a plan discount.
- Admin vs. end user: in B2B, the person clicking cancel may not be the economic buyer. Design must route "request to cancel" to admin review for multi-seat accounts.
- Regulatory: monday.com operates globally. FTC Click-to-Cancel (US), EU consumer directives, and Israeli consumer protection laws all mandate accessible cancellation. Legal review required before shipping any cancel flow changes.
