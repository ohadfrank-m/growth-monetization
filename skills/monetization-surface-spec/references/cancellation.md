# Cancellation flow — spec reference

Surface type 6: user initiates cancel or downgrade.

CRO rationale, benchmarks, and best-in-class examples for this surface live in the shared playbook — read it before drafting: [../../../playbooks/cancellation.md](../../../playbooks/cancellation.md). This file covers only what's specific to *writing the spec*.

## When it appears
- Billing page "Cancel subscription"
- Downgrade attempt to a lower tier
- Seat reduction below current usage

## Mandatory spec sections
- **Entry points:** every place a user can start cancelling
- **Reason capture:** one question, optional, with 5–7 options plus free text
- **Reason-matched save offer:** each reason maps to one response (price → downgrade or discount; not using → pause; missing feature → roadmap or workaround; switching tool → CSM contact)
- **Value surface:** personalised usage summary (boards, automations, AI actions this year)
- **Downgrade path:** what they keep on the lower tier or Free
- **Confirmation:** final step is clear and one click; no loops
- **Post-cancel state:** access end date, data retention, export options
- **Win-back:** what re-activation looks like and when it's offered
- **Enterprise:** route to CSM rather than self-serve cancel

Check local regulations (e.g. click-to-cancel rules) with legal before shipping any change to this flow.

## Copy hook
Primary reason: feel secure. See [copy-hooks.md](copy-hooks.md#cancellation-flow-surface-6).
