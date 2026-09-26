# Trial flow — spec reference

Surface type 7: trial start, mid-trial nudge, trial expiry.

Current trial terms (length, tier, credits, card requirement): [monday-context.md](../../../context/monday-context.md#trial).

CRO rationale, benchmarks, trial phases, trigger rules and best-in-class examples live in the shared playbook — read it before drafting: [../../../playbooks/trial-flows.md](../../../playbooks/trial-flows.md). This file covers only what a trial *spec* must contain.

## When it appears
- **Day 0–1:** onboarding and activation prompts
- **Mid-trial:** nudges tied to activation milestones, not just calendar days
- **Final days:** expiry warnings
- **Expiry:** plan decision screen

## Mandatory spec sections
- **Activation milestone:** the aha action this surface drives (first automation, first AI agent run, first teammate invited)
- **Trigger logic:** calendar-based, behaviour-based, or both; what suppresses the nudge (already activated, already converted)
- **Personalised proof:** what the user has built so far, pulled from their account
- **Loss list at expiry:** the specific Pro features they'll lose, ranked by their own usage
- **Explicit downgrade option:** what they keep on Free
- **Blocking level:** never block on day 0–1; expiry screen may be blocking with a clear Free option
- **Extension logic:** monday trials can't be extended today (context file). A spec that proposes an extension flags it as a policy change with an owner, not as existing behaviour.

## Patterns
See [wireframe-patterns.md](wireframe-patterns.md) — Trial flow, Pattern A (expiry) and Pattern B (activation nudge).

## Anti-patterns specific to trials
- Asking for payment before the aha moment
- Expiry screen with no Free option
- Generic "Your trial is ending" with no personalised loss list
- Nudging users who have already converted

## Copy hook
Primary reason: alleviate fear / escape loss. See [copy-hooks.md](copy-hooks.md#trial-flow-surface-7).
