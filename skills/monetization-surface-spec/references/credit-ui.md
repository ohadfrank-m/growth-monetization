# Credit / consumption UI — spec reference

Surface type 5: running low on credits, credit meter, metering dashboard, top-up flow.

The highest-priority surface type for monday.com given the AI Agents launch. CRO rationale, benchmarks, best-in-class examples, and monday-specific mechanics (meter design, forecasting, top-up flow, agentic depletion, dual-gated trial) live in the shared playbook — read it before drafting, not just for the anti-pattern list: [../../../playbooks/credit-ui.md](../../../playbooks/credit-ui.md). This file covers only what's specific to *writing the spec*.

## When this surface appears

- **Warning state:** credit balance drops below warning threshold (e.g., 20% or 50 credits remaining)
- **Depletion state:** credit balance reaches 0 mid-session or mid-task
- **Depletion mid-task:** balance hits 0 while an AI agent is actively running — highest-risk moment
- **Credit meter (persistent):** visible in dashboard or sidebar at all times when credits are < 100% or < threshold
- **Top-up flow:** user initiates a credit purchase (self-serve or admin)
- **Post-top-up confirmation:** credits added, task can resume

## Mandatory spec sections for credit UI

All sections in the surface spec template apply. Additionally, always address:

### Credit meter design (for persistent meter)
- **Location:** where in the UI does the meter live? (sidebar, header, dashboard widget, contextual to AI features)
- **Display at full:** meter visible or hidden when credits are plentiful?
- **Warning threshold:** at what % or absolute number does the meter change state?
- **Meter states:** define all: healthy / warning / critical / depleted
- **Translation display:** how the number maps to task equivalents at each state

### Depletion flow (for depletion modal)
- **Blocking vs. non-blocking:** inline nudge vs. modal — justify the choice
- **Task state:** is the in-progress task paused or failed? Spec the state preservation logic
- **Resume path:** after top-up, how does the user resume exactly where they were?
- **Admin path:** if user is IC, what does "notify admin" send and to whom?

### Top-up flow
- **Package options:** what sizes/amounts are available? (pull from benchmark if available)
- **Confirmation step:** what does the user see before purchase? (price, what they get, renewal terms)
- **Post-purchase state:** credits appear immediately? Delay? UI feedback?
- **Receipt / confirmation:** email? In-app notification?

## Trigger logic spec

For every credit UI surface, specify the full trigger logic:

```
Trigger conditions:
- Warning state: credit balance ≤ {threshold} OR {N} days remaining
- Critical state: credit balance ≤ {threshold}
- Depletion: balance = 0 OR agent step fails due to insufficient credits

Frequency cap:
- Warning banner: show max once per session, re-show if balance drops further
- Depletion modal: always show (not capped — it's a functional state, not a promotional one)
- Top-up success confirmation: always show once after purchase

Dismiss behaviour:
- Warning banner: dismissible; re-appears next session if balance still in warning range
- Depletion modal: not dismissible until action taken (top-up or notify admin)
```

## Copy hook

Full copy framework: [copy-hooks.md](copy-hooks.md#credit--consumption-ui-surface-5). Always hand copy finalisation to `improve-conversion-surfaces-copy`.

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Copy (write before the wireframe): `.monetization/{feature-slug}/02-copy.md`
- Wireframe (built from that copy): `.monetization/{feature-slug}/03-wireframe.html`
- Include all meter states in wireframe (healthy, warning, critical, depleted), each with its real copy — the meter's task-translation text and the depletion banner's line are exactly the kind of copy that shouldn't ship as a placeholder

## Next step

After the spec:
```
---
→ Next step: improve-conversion-surfaces-copy — write the actual meter/depletion/top-up copy from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

After the wireframe (built once copy exists):
```
---
→ Next step: monetization-design-reviewer — score the credit UI spec, copy, and wireframe together
→ Prompt: "Review .monetization/{feature-slug}/"
```
