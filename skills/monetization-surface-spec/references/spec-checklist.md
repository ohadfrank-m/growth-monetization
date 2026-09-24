# Spec checklist — anti-patterns and edge cases

Stable rules applied to every surface spec. Strategy data (prices, tiers, credit packages) lives in [../../../context/monday-context.md](../../../context/monday-context.md); this file holds the rules that don't change when pricing does.

---

## Anti-patterns — flag in every spec

| Anti-pattern | Why it fails | Spec this instead |
|-------------|-------------|-------------------|
| Bare credit number ("500 credits") | Meaningless without context | Always add a task translation ("≈ 500 AI actions") |
| Hard stop mid-agent-task | State lost, user churns | Save state, pause the task, offer a resume path |
| Full-screen blocking modal in an agentic flow | Breaks momentum | Inline nudge at the warning threshold |
| "Upgrade" as the only CTA | Names the cost, not the benefit | Benefit-led CTA ("Keep building", "Unlock AI Agents") |
| No escape hatch | Dark pattern, regulatory risk | Always include dismiss or "Not now" |
| Same prompt repeated after dismiss | Annoyance, unsubscribe risk | Frequency cap: max once per session, once per week |
| Price with no anchor | Loss of perceived value | Anchor against a higher tier or the monthly price |
| Guilt-trip copy ("Don't abandon your team") | Brand damage, no lift evidence | Lead with what they gain |
| IC dead-end when they can't purchase | IC churns, admin never hears | Always include a "Notify admin" path |
| Asking before value is delivered | Conversion drops pre-aha | Show proof of value before the ask |
| Hardcoded colours, type, or spacing | Design-system drift | Reference Vibe tokens by name |

---

## Edge cases — address every one

Mark non-applicable cases `N/A` with a one-line reason. Never skip silently.

**Credit debt.** Can the balance go below 0 mid-task? Spec the error state and the recovery path.

**Admin-gated purchase.** If the viewer isn't an admin, what's their path? Spec the "Notify admin" action and what the admin receives (content, channel, CTA).

**Mobile.** Does the surface work below 375px? List what stacks, collapses, or is hidden. If it isn't designed for mobile, say so.

**Repeat exposure.** What happens on the 3rd dismissal this week? Spec the frequency cap and what changes on repeat views.

**Enterprise accounts.** Enterprise users usually don't self-serve. Route to their CSM instead of self-serve purchase.

**Seats vs. credits.** If both limits can trigger, spec which takes priority.

**Billing cadence.** Does the surface behave differently for monthly vs. annual customers (e.g. mid-cycle top-up proration)?
