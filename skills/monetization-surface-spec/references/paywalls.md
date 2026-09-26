# Paywall / feature gate — spec reference

Surface type 2: user tries to access a locked feature.

CRO rationale, benchmarks, timing and frequency rules, and best-in-class examples for this surface live in the shared playbook — read it before drafting: [../../../playbooks/paywalls.md](../../../playbooks/paywalls.md). This file covers only what's specific to *writing the spec*.

## When it appears
- Click on a locked feature, view, or column type
- Attempt to exceed a feature-level entitlement (e.g. private boards on Standard)
- Deep link into a feature the account's tier doesn't include

## Mandatory spec sections
- **Gate trigger:** exact feature and entry point(s)
- **Preview:** what the user sees of the feature before the ask (blurred, sample data, short demo)
- **Value proof:** 3 concrete use cases or a personalised example from their workspace
- **Target tier:** the lowest tier that unlocks the feature (don't push Pro if Standard unlocks it)
- **Trial path:** can the user start a Pro trial from here instead of paying?
- **Blocking level:** modal vs. inline banner, with justification
- **IC vs. admin:** "Notify admin" path for users who can't purchase
- **Dismiss and frequency cap**

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Paywall, Pattern A (preview + gate) and Pattern B (inline gate).

## Copy hook
New users: alleviate fear of missing out. Existing users: capability gain. See [copy-hooks.md](copy-hooks.md#paywall--feature-gate-surface-2).
