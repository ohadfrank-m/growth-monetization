# Copy hooks per surface type

Use this file to identify the correct persuasion angle for each surface type. The spec names the reason and copy direction — final copy is always written by `improve-conversion-surfaces-copy`.

The 15 reasons people buy (source: `improve-conversion-surfaces-copy` skill):
1. To avoid effort | 2. To feel happier | 3. To save time | 4. To be comfortable
5. To escape pain or guilt | 6. To make money | 7. To save money | 8. To get recognition
9. To be healthier | 10. To feel secure | 11. To alleviate fear | 12. To feel special
13. To increase status | 14. To feel loved | 15. To get knowledge

---

## Surface type → primary reason → hook direction

### Pricing page (surface 1)
**Cohort:** Both (new and existing)
**Primary reason:** Make money (6) + Save time (3)
**Secondary reason:** Feel special / status (12, 13) for higher tiers

**Hook direction:**
- Lead with outcome, not feature: "Ship automations in minutes" not "Unlimited automations"
- Tier differentiation: each tier headline should name a distinct job-to-be-done
- Enterprise: lead with security and control (reason 10: feel secure)
- AI features: lead with what agents do for the team, not credit counts

**What to avoid:** Feature lists, spec sheets, "unlimited everything" without context

---

### Paywall / feature gate (surface 2)
**Cohort:** New users (urgency) or Existing users (capability)
**Primary reason:** Escape pain/guilt (5) — they're blocked; alleviate fear (11) — they might miss out

**Hook direction (new user at gate):**
- Show the value of the locked feature immediately before the ask
- Lead with what they can do: "Automate this — upgrade to Pro"
- Not: "This feature requires Pro" (functional, not motivating)

**Hook direction (existing user at gate):**
- Lead with capability: "Your team is using this — you're missing out"
- Or efficiency: "This would save you {time estimate}"
- Not: urgency or time pressure — they're not in a trial

**What to avoid:** Showing paywall before feature preview, blocking without showing proof of value

---

### Promotion (surface 3)
**Cohort:** Both (new and existing, different angles)
**Primary reason:** Save money (7) + alleviate fear of missing out (11)

**Hook direction:**
- Lead with the saving, anchor against the regular price
- Add urgency only if it's real (actual deadline, not fake countdown)
- For existing users: frame as loyalty reward ("As a Pro user, here's something exclusive")
- For new users: frame as reduced risk ("Try Pro for less — see if it's worth it")

**What to avoid:** Fake urgency, discounts with no expiry, discounts without anchoring the original price

---

### Tier upgrade trigger (surface 4)
**Cohort:** Existing users (capability lever — no urgency lever)
**Primary reason:** Save time (3) + make money (6) + avoid effort (1)

**Hook direction:**
- Name the specific limit they hit: "You've reached your {N}-seat limit"
- Connect the limit to the outcome they can't have: "Add more team members to {task}"
- CTA names the capability gained, not the plan upgrade: "Add seats" not "Upgrade to Pro"

**For usage limit triggers:**
- Show how close to limit: "8/10 automations used this month"
- Show what happens at 10/10: specific, not vague
- Show the step up: exactly what they get if they upgrade

**What to avoid:** "You've hit your limit" with no next step, upgrade CTA without showing what changes

---

### Credit / consumption UI (surface 5)
**Cohort:** Existing users
**Primary reason:** Escape pain/guilt (5) — task is stopped; avoid effort (1) — they want to keep working

**Hook direction (warning state — task still running):**
- Proactive, not alarming: "Your AI agents are running low — top up to keep them going"
- Show the task that's at risk: "Your [recipe name] agent will pause in ~{N} actions"
- CTA: "Top up now" or "Keep [task] running"

**Hook direction (depletion state — task stopped):**
- Name the task that stopped: "Your [agent name] has paused"
- Clear path to resume: "Top up to continue where you left off"
- CTA: "Top up and resume"

**What to avoid:** Bare credit numbers, blocking without resume path, IC dead-end without admin path

---

### Cancellation flow (surface 6)
**Cohort:** Existing users (retention play)
**Primary reason:** Feel secure (10) + avoid effort (1) — cancelling is effort too

**Hook direction:**
- Acknowledge the decision, don't guilt-trip
- Surface the value they've used: "You've automated {N} tasks this year with monday"
- Offer alternatives to cancelling: pause, downgrade, CSM call
- If they continue to cancel: make it frictionless — don't trap them (dark pattern, legal risk)

**What to avoid:** Guilt-trip copy, hiding the cancel button, fake "are you sure?" loops, no downgrade option

---

### Trial flow (surface 7)
**Cohort:** New users
**Primary reason:** Alleviate fear (11) + escape pain/guilt (5) — they're risking losing what they built

**Hook direction (mid-trial upgrade nudge):**
- Show what they've built so far: "You've set up {N} automations — keep them after trial"
- Lead with the loss: "Keep everything you've built"
- CTA: "Keep my setup" not "Upgrade to Pro"

**Hook direction (trial expiry):**
- Lead with the specific thing they'll lose: not "your trial is ending" but "your {workflow} will stop"
- Show the single most used feature as the anchor for the loss
- CTA: "Continue with Pro" or "Keep [most used feature] running"

**Hook direction (day 1 / activation nudge):**
- Lead with the outcome: "Set up your first AI agent in 5 minutes"
- No pressure, no urgency — they just signed up
- CTA: "Get started" or "Try AI Agents"

**What to avoid:** Trial expiry without naming what's lost, countdown timers before value is established, upgrade ask before aha moment

---

## How to use this in a spec

In the spec's Copy strategy section:

```markdown
## Copy strategy

- **Primary reason:** {Reason from list above, e.g. "Escape pain / guilt (5)"}
- **Hook:** {One sentence describing the direction, e.g. "Lead with the task that stopped, not the credit count"}
- **Headline direction:** {e.g. "Your [agent name] has paused — you're out of AI credits"}
- **CTA direction:** {e.g. "Top up and resume — not 'Buy credits' or 'Upgrade'"}
- **Tone:** {urgency | capability | reassurance | acknowledgment}
- **What to avoid:** {Specific patterns to flag — from surface type guidance above}

→ Copy writing: hand off to `improve-conversion-surfaces-copy` with this section as input.
→ Prompt: "Write copy for a {surface type} for {cohort} users. Primary reason: {reason}. Direction: {headline direction}. Avoid: {patterns}."
```
