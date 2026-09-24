# Credit / Consumption UI — spec reference

Surface type 5: Running low on credits, credit meter, metering dashboard, top-up flow.

The highest-priority surface type for monday.com given the AI Agents launch. Most of the novel UX problems in this plugin live here.

---

## When this surface appears

- **Warning state:** credit balance drops below warning threshold (e.g., 20% or 50 credits remaining)
- **Depletion state:** credit balance reaches 0 mid-session or mid-task
- **Depletion mid-task:** balance hits 0 while an AI agent is actively running — highest-risk moment
- **Credit meter (persistent):** visible in dashboard or sidebar at all times when credits are < 100% or < threshold
- **Top-up flow:** user initiates a credit purchase (self-serve or admin)
- **Post-top-up confirmation:** credits added, task can resume

---

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

---

## Best-in-class patterns

### Pattern 1: Contextual inline warning (Notion AI)
Notion shows AI credit depletion as an inline banner within the document being edited — not a modal. The banner explains what stopped and offers a one-click top-up. Task is paused, not lost.

**Why it works:** Non-blocking, contextual, preserves task state, single action to resolve.

**Apply for monday.com:** Inline warning within the agent run interface. Banner shows: remaining credits → task translation → single top-up CTA → secondary "notify admin".

### Pattern 2: Progressive warning states (HubSpot)
HubSpot AI shows three states: healthy (no meter visible), warning (meter appears at 20%), critical (meter turns red + pulse animation). Each state has progressively stronger messaging.

**Why it works:** Users aren't surprised by depletion. Warning state gives them time to act before the task is affected.

**Apply for monday.com:** Three-state meter in AI agent sidebar. Healthy state hidden. Warning state appears at 20% remaining. Critical at <10 credits.

### Pattern 3: Task-first messaging (Intercom Fin)
Intercom's credit depletion message leads with the task, not the credits: "Your AI conversation agent has paused — you've run out of AI credits" not "You have 0 credits."

**Why it works:** Users understand what stopped in terms they care about.

**Apply for monday.com:** Always name the stopped task in the depletion message, not just the credit balance.

---

## Anti-patterns to always flag for credit UI

| Anti-pattern | Specific failure | Fix |
|-------------|-----------------|-----|
| Bare credit number | "500 credits" with no task translation | Always add "≈ 500 AI actions" |
| Hard stop mid-agent-task | Task fails, state lost | Save state, pause task, offer resume |
| Full-screen blocking modal in agentic flow | Breaks flow, scary UX | Inline banner at warning threshold |
| No IC→admin path | IC dead-ends, admin never knows | "Notify admin" button always present |
| Post-purchase no resume path | User has credits, doesn't know how to continue | Auto-resume or explicit "Resume task" CTA |
| Credit expiry not communicated | Surprise at month end | Show expiry prominently if credits don't roll over |

---

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

---

## Copy hooks for credit UI

Full copy framework: [copy-hooks.md](copy-hooks.md)

**Primary reason for credit UI:** Escape pain / guilt (work is stopped, in-progress tasks are at risk)
**Secondary reason:** To make money / save time (top up = get the thing done, fast)

**Headline direction (warning state):**
- Lead with what's at risk: "Your AI agents are running low on fuel"
- Not: "You have 47 credits remaining"

**Headline direction (depletion state):**
- Lead with the task that stopped: "Your [agent name] has paused — you're out of AI credits"
- Not: "You've reached your credit limit"

**CTA direction:**
- "Top up and resume" (connects top-up to the outcome)
- "Keep [agent name] running"
- Not: "Buy credits" or "Upgrade"

Always hand copy finalisation to `improve-conversion-surfaces-copy`.

---

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Wireframe: `.monetization/{feature-slug}/02-wireframe.html`
- Include all meter states in wireframe (healthy, warning, critical, depleted)

## Next step

```
---
→ Next step: monetization-design-reviewer — score the credit UI spec and wireframe before design
→ Prompt: "Review the credit UI spec in .monetization/{feature-slug}/"
```
