# Tier upgrade triggers — CRO playbook

Surface type 4: plan-level limits — seats, features, automations. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

Credit / consumption limits are a different emotional state and have their own playbook: [credit-ui.md](credit-ui.md). Don't conflate the two — a seat cap is a blocked-and-frustrated moment; a credit meter is an anxious, mid-task moment.

## When to show

- User attempts to add a seat beyond plan limit
- User tries to enable a feature locked to a higher tier
- Admin views usage dashboard and sees team at capacity
- Usage is consistently at 80–90% of plan limits (proactive nudge before the wall)

## Design principles

1. **Contextualize the limit** — "Your team has used 9 of 10 seats" is better than "You've reached your limit"
2. **Show the delta** — What does the next tier unlock? Make it specific, not a full plan comparison.
3. **Route to the right person** — In B2B, the user hitting the limit is often not the buyer. Provide a "notify admin" path alongside the upgrade CTA.
4. **Don't block the current task** — If the user was doing something, let them finish it (or save state) before presenting the upgrade.

## Screen structure

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

## Proactive vs. reactive triggers

- **Reactive** (at 100%): necessary but lowest-satisfaction moment. User is already blocked.
- **Proactive** (at 70–80%): higher satisfaction, higher CVR. User isn't frustrated yet.
- **Recommendation**: show a non-blocking nudge at 75%, a more prominent prompt at 90%, full gate at 100%.

## Wireframe patterns

**Pattern A — usage limit reached (inline):**
```
[Usage bar: ████████░░ 8/10 automations]
[Inline notification below bar:]
  "You've used 8 of your 10 monthly automations."
  "Upgrade to Pro for unlimited automations."
  [CTA: "Upgrade to Pro"]  [Link: "See what Pro includes"]
```
Why it works: usage bar makes the limit visible and concrete. Limit + consequence + action in one view.

**Pattern B — seat expansion modal:**
```
[Modal:]
  [Headline: "Add more team members"]
  [Current: "You have {N} seats — {N} are used"]
  [Seat selector: [−] 3 [+] additional seats]
  [Price: "+$X/month — billed {monthly/annually}"]
  [CTA: "Add seats"]  [Dismiss: "Not now"]
```
Apply when: user tries to invite someone when at seat limit. Offer the expansion in the moment.

## Benchmarks

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Tier gate → upgrade CVR | <5% | 8–15% | 20%+ |
| Proactive nudge (75%) → upgrade CVR | <3% | 5–10% | 15%+ |

## Best-in-class examples

**GitHub Copilot (Business)** — Seat limit hit triggers email to org admin AND in-product notification to the blocked user with a "request access" flow. Separates the user-facing experience from the buyer-facing action.

**Zapier** (task limits) — Zap-level usage bar visible on every automation. Turns invisible usage into a tangible, always-present signal. Normalizes awareness of limits before they're hit.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| "You've hit your limit" with no number or consequence | Frustration with no path forward |
| Upgrade CTA with no view of what the next tier changes | Friction, zero motivation |
| Surprise hard stop with no warning threshold | User feels ambushed, not informed |

## monday.com-specific notes

- Automation cap (250/mo on Standard) is the highest-volume tier-upgrade trigger today — proactive nudge at 75% ("188/250 automations used") outperforms the reactive hard-stop message.
- Seat expansion: always show the bundle price delta (bundles of 3/5/10/15/20/25/30/40), never a per-seat price that implies granular add-one purchasing.
- Route ICs who hit a seat or feature cap to "notify admin" — they cannot self-purchase.
