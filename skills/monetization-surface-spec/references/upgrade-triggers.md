# Tier upgrade trigger — spec reference

Surface type 4: usage limit hit, seat expansion, plan upgrade nudge.

CRO rationale, benchmarks, best-in-class examples, and the **tier and seat threshold ladder** (owned there) live in the shared playbook. Read it before drafting: [../../../playbooks/upgrade-triggers.md](../../../playbooks/upgrade-triggers.md). Current limits per tier: [monday-context.md](../../../context/monday-context.md#feature-gating-by-tier). This file covers only what's specific to *writing the spec*.

If the trigger is a credit/consumption limit rather than a tier or seat limit, use [credit-ui.md](credit-ui.md) instead. If the user tried a feature the tier doesn't have at all, use [paywalls.md](paywalls.md).

## When this surface appears

- **Approaching the limit:** usage crosses the nudge rung of the ladder (e.g. automations or integrations this month)
- **Near the limit:** usage crosses the prompt rung, optionally with a pace forecast
- **At the limit:** the action that would exceed the limit is attempted (run, create, connect, upload). That action is gated
- **Seat limit at invite, admin:** the invite would exceed paid seats, so the seat expansion modal opens with the next bundle
- **Seat limit at invite, IC:** same invite from someone who can't buy, so the notify-admin path opens
- **Seat overage:** active seats already exceed paid seats (added outside the invite flow). The admin sees the overage state and the platform's auto-upgrade timeline ([monday-context.md](../../../context/monday-context.md) (plan-change rules: an open item until the file carries them))
- **Admin at capacity:** an admin opens billing or usage while the team is at or near a limit, which is the only state where the viewer can buy
- **Request pending:** the IC already notified the admin
- **Post-upgrade:** limit raised; the blocked action resumes (invite sent, automation re-enabled)
- **Cycle reset:** a monthly cap resets, and the rungs clear

## Mandatory spec sections for upgrade triggers

All sections in the surface spec template apply. Additionally, always address:

### Limit definition
- **Limit and rungs:** which limit, which rungs of the playbook's ladder the surface uses (cited, not re-chosen without a reason), and what happens at 100%
- **Behaviour at the limit:** hard stop, soft limit, or grace period, taken from the context file. If the context file doesn't state it, it's an open item
- **Blocked vs still working:** exactly what stops (new runs, new items, new invites) and what continues (existing boards, runs already in progress)
- **Usage context:** how current usage is shown (bar, exact count, trend) and where. The builder sees it in the feature area, not only in billing

### Upgrade delta
- **What changes at the next tier:** the specific new limit as a number from the context file, never "more" or "unlimited" unless it is
- **Seat bundles:** the next bundle size and the bundle price delta, with the cadence stated. Never a per-seat price that implies add-one purchasing
- **Invite alternatives:** guest or viewer instead of a member, where the tier allows, with the cost of each option explicit
- **Price and timing on the admin path:** the price delta on or beside the CTA, and whether the upgrade applies now (with proration) or at renewal, per the context file's plan-changes section

### Paths
- **IC vs. admin:** "Notify admin", pre-filled with limit, count, where it was hit, and an optional reason. Spec what the admin receives. The context file lists admin alerts only for credits and seat overage, so for other tier limits the IC button is the only signal
- **Resume path:** after the upgrade, how the blocked action completes (auto-retry, or one click, with the draft kept)
- **Pace forecast (optional):** the rule for "at this pace you'll hit it on {date}" and the minimum history it needs
- **Dismiss and frequency cap:** see the trigger block below

## Trigger logic spec

```
Trigger conditions (rungs owned by playbooks/upgrade-triggers.md — Threshold ladder; cite, don't restate):
- Nudge: usage ≥ {nudge_rung} of {limit} in the current {period}
- Prompt: usage ≥ {prompt_rung} of {limit}; add the pace line only with ≥ {min_history} of data
- Gate: the action that would exceed {limit} is attempted → block that action only, never work
  already done or runs already in progress
- Seat limit at invite: invite would take active seats above {paid_seats} → seat modal (admin) or
  notify-admin (IC); guest/viewer option where the tier allows
- Seat overage: active seats > {paid_seats} → admin overage state with the platform's countdown
  (context file, plan-changes section)
- Admin at capacity: admin views billing/usage with usage ≥ {nudge_rung}
- Suppress: tier already covers the request (re-check before render); request pending for this
  limit; sales-assisted account (route to the account team)

Frequency cap:
- Nudge: once per {period} per user; returns only when usage crosses the next rung
- Prompt: persistent in the feature area until dismissed; the dismiss holds until the next rung or
  the next cycle
- Gate: every attempt — functional, not promotional
- Seat modal: every invite attempt at the limit

Dismiss behaviour:
- Nudge / prompt: dismissible; stored per user, per rung, per cycle
- Gate: always exits — "Not now" returns to the task with the blocked action preserved (invite
  draft kept, automation saved but not running)

Re-show rules:
- Cycle reset (monthly caps): all rungs clear with the counter
- After upgrade: every rung and gate for that limit disappears immediately; the blocked action resumes
- Admin declined an IC request: the IC sees the decision once; the gate returns to the IC default
```

## Choosing a pattern

Patterns: [wireframe-patterns.md](wireframe-patterns.md) → Tier upgrade trigger.

| Situation | Pattern | Rule |
|---|---|---|
| A metered monthly cap (automations, integrations) at the nudge, prompt or gate rung | **A** — usage limit, inline | In the feature area, where the builder works. Bar + exact count + next-tier number |
| Invite at the seat limit | **B** — seat expansion modal | Bundle-based: next bundle and bundle price delta. Guest/viewer alternative shown where allowed |
| Seat overage (seats already over) | **B**, admin overage variant | Countdown and options (reduce seats, change user type, accept the next bundle) |
| Admin viewing usage at capacity | **A** in the billing/usage view | Purchase one click away. The only state with price in the primary CTA |
| IC in any of the above | Same pattern | Primary CTA becomes "Notify admin". The count and next-tier number stay visible |

## Edge cases specific to upgrade triggers

In addition to every case in [spec-checklist.md](spec-checklist.md):

- **IC vs admin:** the IC hits the limit and the admin buys. Spec both screens and the admin's notification.
- **Annual vs monthly:** the bundle price delta uses the account's cadence. Say whether the change is immediate with a proration credit or scheduled, per the context file's plan-changes section.
- **Mid-cycle proration:** the plan summary shows the unused-balance credit and the new cycle start. Never quote a delta without saying when the charge happens.
- **Scheduled downgrade pending:** an account with a downgrade scheduled for renewal that now hits the *new* plan's limit. Spec what the trigger shows (the scheduled plan, not the current one).
- **Multiple limits at once:** seats vs automations vs credits. Follow spec-checklist.md's priority rule, and name which limit the copy leads with.
- **Pace near cycle end:** don't forecast a limit hit after the counter resets.
- **Deactivated users:** the context file says deactivating users doesn't reduce paid seats. A "free up a seat" path must say what it does and doesn't change on the bill.
- **Guests and viewers:** name which user types count toward seats on each tier (context file) before offering a guest as the alternative.
- **Multi-product accounts:** the limit belongs to one product. The trigger names that product and upgrades only that product.
- **Sales-assisted accounts:** no self-serve delta. Route to the account team with the limit and count attached.
- **Mobile:** the usage bar collapses to "{used}/{limit}", and the seat modal becomes a full-height sheet with the bundle choice kept.

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Tier upgrade trigger, Pattern A (usage limit) and Pattern B (seat expansion).

## Copy hook
Primary reason: save time / avoid effort. See [copy-hooks.md](copy-hooks.md#tier-upgrade-trigger-surface-4). Always hand copy finalisation to `improve-conversion-surfaces-copy`.

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Copy (write before the wireframe): `.monetization/{feature-slug}/02-copy.md`
- Wireframe (built from that copy): `.monetization/{feature-slug}/03-wireframe.html`
- States in the wireframe: nudge, prompt, gate, IC gate, request pending and post-upgrade (plus the seat modal and overage when seats are in scope), each with real copy. The next-tier number line and the bundle price line are the strings most often left as placeholders

## Next step

After the spec:
```
---
→ Next step: improve-conversion-surfaces-copy — write the limit, next-tier delta, seat-bundle and notify-admin copy from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

After the wireframe (built once copy exists):
```
---
→ Next step: monetization-design-reviewer — score the upgrade trigger spec, copy, and wireframe together
→ Prompt: "Review .monetization/{feature-slug}/"
```
