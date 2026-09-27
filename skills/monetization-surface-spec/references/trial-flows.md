# Trial flow — spec reference

Surface type 7: trial start, mid-trial nudge, trial expiry.

Current trial terms (length, tier, credits, card requirement, extension): [monday-context.md](../../../context/monday-context.md#trial).

CRO rationale, benchmarks, the **trial phases** (owned there), trigger rules, anti-patterns and best-in-class examples live in the shared playbook. Read it before drafting: [../../../playbooks/trial-flows.md](../../../playbooks/trial-flows.md). This file covers only what a trial *spec* must contain.

Feature gates met during a trial are [paywalls.md](paywalls.md). Credit meters and depletion are [credit-ui.md](credit-ui.md). Tier and seat limits are [upgrade-triggers.md](upgrade-triggers.md).

## When this surface appears

States map onto the playbook's three phases: Setup, Proof, Decision.

- **Trial start (day 0):** the account lands in its trial. The paid-only layer being unlocked is named
- **Phase 1, milestone not reached:** non-blocking setup prompts pointed at the milestone
- **Milestone reached:** a one-time confirmation that names the next paid capability it unlocks
- **Stalled:** no return for {N} days, so re-engagement points at the milestone, not at pricing
- **Phase 2, behaviour prompt:** an event-driven prompt tied to what the user is doing (second teammate invited, automation built)
- **Trial credit threshold:** the trial's credit balance crosses a credit-ui threshold
- **Two meters:** the trial is limited by days and credits, and the one running out first drives the state
- **Phase 3, countdown:** the final window, with the personalised "what you built" list and the plan choice
- **Expiry decision:** trial over. The plan decision screen shows every option, including the no-cost one
- **Post-expiry:** paid plan applied, Free chosen, or account inactive, plus what invited members see when they sign in
- **IC in a team trial:** a non-admin reaches the milestone or a Phase 3 moment, and gets the admin path
- **Converted mid-trial:** every trial surface turns off immediately
- **Add-on product trial on a paid account:** a product trial inside an account that already pays (context file: it ends automatically, with no cancel option)

## Mandatory spec sections for trials

All sections in the surface spec template apply. Additionally, always address:

### Milestone and phases
- **Activation milestone:** the one aha action this trial drives, picked from the context file's aha signals (first automation, first AI action, first teammate invited), with the reason for the pick. A narrower milestone is a proposal that needs the data owner's sign-off
- **Phase map:** a table `State · Phase · Window · Trigger · Surface · Blocking?`, with windows cited from the playbook's phase table, not re-chosen without a reason
- **Trigger logic:** calendar-based, behaviour-based, or both, and what suppresses each nudge (already activated, already converted, not an admin)

### Meters
- **Meter display:** days left, credits left (with the task translation per credit-ui), or both. With two meters, name which ends first as primary and the other as one secondary line
- **Trial credit amount:** the amount comes from the context file. If it isn't published, it's a `{trial_credits}` slot and an open item, never a number. Internal-only trials are never stated in external-facing copy (context file)

### Proof and decision
- **Personalised proof:** what the user has built so far, pulled from their account (boards, automations, AI runs, teammates), with the query or event behind each count
- **Loss list at expiry:** the specific Pro features they'll lose, ranked by their own usage. If the milestone wasn't reached, the screen leads with what's left to try, not a loss list they don't have
- **Explicit downgrade option:** what they keep on Free or a lower plan, with what it keeps and what stops
- **Plan options on the decision screen:** each tier with its price on or beside the CTA, the seat bundle for the team's current size, and the cadence
- **Blocking level:** never block in Phase 1. Only the expiry decision may block, and it always has the no-cost option on screen

### Policy and roles
- **Extension logic:** monday trials can't be extended (context file). A spec that proposes an extension flags it as a policy change with an owner, not as existing behaviour
- **IC vs admin:** the IC path ("tell {admin} you want to keep this"), and the admin's decision screen showing the team's activity, not only the admin's own
- **Post-expiry state:** what the account and its invited members see after expiry for each outcome, per the context file's post-trial default

Anti-patterns to check the spec against: [playbooks/trial-flows.md → Anti-patterns](../../../playbooks/trial-flows.md).

## Trigger logic spec

```
Trigger conditions (phases and windows owned by playbooks/trial-flows.md — Three phases; cite, don't restate):
- Trial start: account created → {trial_tier} trial for {trial_length} (monday-context.md#trial)
- Phase 1 prompt: day ∈ {phase_1_window} AND {milestone} not reached
- Milestone reached: first {milestone} event → one-time confirmation + next paid capability
- Stalled: no session for {stall_days} → re-engagement toward {milestone} (email/in-app per spec)
- Phase 2 prompt: behaviour event {event} ∈ {phase_2_window} AND user activated
- Trial credit threshold: thresholds owned by playbooks/credit-ui.md (Thresholds); in a trial, lead
  with what the credits did
- Two meters: the meter forecast to end first drives Phase 3 — a balance ending on day {N} gets its
  own Phase 3 moment (playbooks/credit-ui.md, trials that gate on time and credits)
- Phase 3: now ≥ trial end − {phase_3_window}, OR credits forecast to end sooner
- Expiry: trial end reached → decision screen on the next visit
- Suppress: any paid plan active → all trial surfaces off immediately; {milestone} reached → no
  Phase 1 prompts; admin-only asks never shown to ICs

Frequency cap:
- Phase 1 banner: once per session; a dismiss holds for {phase_1_dismiss}
- Phase 2 prompts: at most one per session, event-driven
- Phase 3 countdown: persistent header element, never a modal before expiry
- Expiry decision screen: every visit until a choice is made — functional, not capped

Dismiss behaviour:
- Phase 1 / 2: dismissible, never blocking
- Phase 3: the banner is dismissible; the countdown stays in the header
- Expiry: can't be dismissed without a choice, but a no-cost choice is always on screen

Re-show rules:
- Milestone reached → Phase 1 never returns
- After the expiry choice: no trial surfaces; a Free account gets its own upgrade triggers and gates,
  not trial nudges
```

## Choosing a pattern

Patterns: [wireframe-patterns.md](wireframe-patterns.md) → Trial flow.

| Situation | Pattern | Rule |
|---|---|---|
| Phase 1, milestone not reached | **B** — activation nudge | Non-blocking banner pointed at the milestone. No price, no plan ask |
| Phase 2, behaviour prompt | **B**, in-context variant | Tied to the event, in the feature area |
| Phase 3 countdown | **B** + header countdown | Personalised "what you built", price shown, still non-blocking |
| Expiry decision, milestone reached | **A** — expiry modal | Personalised loss list, price on the CTA, no-cost option explicit |
| Expiry decision, milestone not reached | **A**, "not yet" variant | Leads with what's left to try and the no-cost option, not a loss list |
| Trial credit threshold or depletion | credit-ui patterns | [credit-ui.md](credit-ui.md) owns the meter. The trial spec only sets copy direction |
| IC in a team trial | Same pattern | Primary CTA becomes the admin path. Proof shows the team's activity |

## Edge cases specific to trials

In addition to every case in [spec-checklist.md](spec-checklist.md):

- **IC vs admin:** the IC who activates often isn't the buyer. Spec the IC's path and what the admin sees about the team's usage.
- **Converted mid-trial:** suppression is immediate, across devices and email. No "trial ends in 2 days" after payment.
- **Annual vs monthly at conversion:** the decision screen's toggle default and price lines follow the pricing page spec. Trial copy never quotes a price the page doesn't.
- **Seat count at conversion:** the team's active members decide the bundle shown. If they exceed the Free cap, say what happens to extra members on Free.
- **Two meters:** never two equal countdowns. The one ending first is primary.
- **Multiple asks in one session:** a Phase 3 prompt yields to a functional state (depletion, at-limit gate), per spec-checklist.md. A Pro trial sees no Pro gates.
- **Add-on product trial on a paid account:** no cancel option and no charge at the end (context file). The expiry state says what the product returns to.
- **Invited members after expiry:** what a member sees when the account goes inactive or drops to Free.
- **Agentic runs at expiry:** in-flight agent runs at trial end or credit depletion must not promise "your work is saved" while state preservation isn't native (context file).
- **Deep link during a trial:** a link to a Pro feature works during the trial. After expiry, it lands on the decision screen or the Free gate, never an error.
- **Localized pricing on the decision screen:** follows the pricing page's currency rule.
- **Re-trial attempts:** the same user or domain starting a new trial. Spec the rule or mark it an open item. Never assume a policy.
- **Mobile:** the Phase 3 header collapses to "{days_left} days left", and the expiry decision screen fits 375px with the no-cost option visible without scrolling.

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Trial flow, Pattern A (expiry) and Pattern B (activation nudge).

## Copy hook
Primary reason: alleviate fear / escape loss. See [copy-hooks.md](copy-hooks.md#trial-flow-surface-7). Always hand copy finalisation to `improve-conversion-surfaces-copy`.

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Copy (write before the wireframe): `.monetization/{feature-slug}/02-copy.md`
- Wireframe (built from that copy): `.monetization/{feature-slug}/03-wireframe.html`
- The wireframe shows the phases as a flow strip (start → Phase 1 → milestone → Phase 3 → expiry → post-expiry), with the "not yet" expiry variant and the IC variant as states, each with real copy. The personalised proof lines and the no-cost option label are the strings most often left as placeholders

## Next step

After the spec:
```
---
→ Next step: improve-conversion-surfaces-copy — write the phase prompts, proof lines, loss list and decision-screen copy from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

After the wireframe (built once copy exists):
```
---
→ Next step: monetization-design-reviewer — score the trial flow spec, copy, and wireframe together (Trial Flow rubric column)
→ Prompt: "Review .monetization/{feature-slug}/"
```
