# Spec checklist — anti-patterns and edge cases

Stable rules applied to every surface spec. Strategy data (prices, tiers, credit packages) lives in [../../../context/monday-context.md](../../../context/monday-context.md); this file holds the rules that don't change when pricing does.

---

## Anti-patterns — flag in every spec

| Anti-pattern | Why it fails | Spec this instead |
|-------------|-------------|-------------------|
| Bare credit number ("500 credits") | Meaningless without context | Always add a task translation from the context file's official line ("≈ 25 resume screenings"), never 1 credit = 1 action |
| Hard stop mid-agent-task | State lost, user churns | Save state, pause the task, offer a resume path |
| Full-screen blocking modal in an agentic flow | Breaks momentum | Inline nudge at the warning threshold |
| "Upgrade" as the only CTA | Names the cost, not the benefit | Benefit-led CTA ("Keep building", "Unlock AI Agents") |
| No escape hatch | Dark pattern, regulatory risk | Always include dismiss or "Not now" |
| Same prompt repeated after dismiss | Annoyance, unsubscribe risk | Frequency cap per the surface's playbook (e.g. [paywalls.md → Timing and frequency](../../../playbooks/paywalls.md#timing-and-frequency--owned-here)); never re-show on a timer regardless of behaviour |
| Price with no anchor | Loss of perceived value | Anchor against a higher tier or the monthly price |
| Guilt-trip copy ("Don't abandon your team") | Brand damage, no lift evidence | Lead with what they gain |
| IC dead-end when they can't purchase | IC churns, admin never hears | Always include a "Notify admin" path |
| Asking before value is delivered | Conversion drops pre-aha | Show proof of value before the ask |
| Hardcoded colours, type, or spacing | Design-system drift | Reference Vibe tokens by name |

---

## Flow map — check before and after drafting

- Multi-screen surface: a flow map row for every screen, in order, with where the user arrives from and goes next (including abandon).
- Every screen names a friction point and its reduction — or "none" with a reason.
- Single-screen surface: the screen before and after, and the friction at the hand-off.
- With a `00-journey.md`: every on-surface and hand-off J step appears in the flow map by J#; every scenario in User context; every on-surface J step's wireframe state id listed as a state; any new step marked `J{n}+` with its reason.

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

**Multiple monetization asks in one session.** When more than one surface could fire, show one at a time, in this order: a functional state the user is in (depletion, an at-limit gate on the action they just tried, the trial expiry decision) → an intent gate the user clicked → a lifecycle prompt (trial phases) → a promotion. A lower-priority ask waits for the next session. It never stacks on screen with a higher one.

**Deep links.** If the surface can be reached by URL (email, shared board, campaign link, support macro), spec what the link opens for each state: eligible, ineligible, expired, wrong role, logged out. An invalid link falls back to the default state with a one-line reason, never an error page.

**Localized pricing and currency.** Any price on the surface is in the currency the account is billed in (in-app), or the region currency the context file publishes (public). A currency or tax treatment the context file doesn't list is an open item. Never convert a USD price for display.

**Loading, empty, and error states.** Monetization surfaces fail at the worst moment. Spec each that applies: purchase pending (what shows between click and confirmation), payment failed (inline, with a retry and the reason when known — never a generic error), credits or plan not yet applied (what the user sees until it lands), and the empty state (no usage yet, no plan history).
