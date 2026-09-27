# Cancellation flow — spec reference

Surface type 6: user initiates cancel, downgrade, seat reduction, or credit-package reduction.

CRO rationale, benchmarks, the reason → offer starting map, **legal context**, and best-in-class examples live in the shared playbook. Read it before drafting: [../../../playbooks/cancellation.md](../../../playbooks/cancellation.md). monday's live cancellation mechanics, notice window, refund rules and effective dates: [monday-context.md](../../../context/monday-context.md) (plan-change rules: an open item until the file carries them). If that section is missing, those rules are open items. This file covers only what's specific to *writing the spec*.

Check local regulations (click-to-cancel and similar rules) with legal before shipping any change to this flow. The spec carries the playbook's "reviewed by legal" line.

## When this surface appears

**Entry and routing**
- **Cancel intent:** "Cancel" from billing (the product's menu, account settings) or a support deep link
- **Downgrade intent:** a lower tier chosen from billing or the pricing page
- **Reduction intent:** fewer seats, or a smaller credit package
- **Non-admin intent:** a viewer who can't cancel goes to request-to-admin, not the flow
- **Sales-assisted account:** Enterprise, invoice-billed, or account-managed, routed to the account team with the date and contact
- **High-value route (optional):** accounts above {high_value_threshold} are offered a person before the automated flow, skippable

**The flow**
- **Reason:** one question
- **Matched offer:** one offer matched to the reason, with "continue to cancel" on the same screen
- **Offer accepted:** confirmation of what changed, when, and how to undo
- **Downgrade confirmation:** what you keep, what you lose, and when, with the loss list built from the account's own usage
- **Final confirmation:** end date, notice rule, data, export, the way back
- **Error:** the cancel or change didn't save. Show the reason and a retry, never a silent success

**After**
- **Cancelled, before end date:** in-app banner with the end date and "Reactivate"
- **Access ended:** landing state (lower plan, Free, or inactive account), data status, export
- **Win-back:** the email sequence plus the in-app state on return
- **Refund path:** a new customer inside the refund window, where access may end immediately. The consequence is stated before confirm

## Mandatory spec sections for cancellation

All sections in the surface spec template apply. Additionally, always address:

### Entry and routing
- **Entry points:** every place a user can start cancelling, downgrading or reducing, as a table: `Entry point · Intent · Who can use it · Routed to`
- **Eligibility and routing:** role (admin vs not), billing channel, plan, health/MRR route, refund eligibility, each mapped to where it sends the user
- **Notice window:** if the account's contract requires notice before term end (context file), show the renewal date and the notice deadline on the first screen, before any offer. Never let an offer imply that cancelling will stop a renewal that's already locked in

### Reason and offer
- **Reason capture:** one question. Option count and framing per the playbook's step 2, plus "Other" with optional free text. State whether the reason is required, and justify it if it is (monday's live flow requires one today, per the context file)
- **Reason → offer map:** a table in the spec, one row per reason offered: `Reason · Offer (or "none") · Eligibility · What executes on accept · Undo`. Start from the playbook's map. A reason with no fitting offer gets "none" and goes straight to confirm
- **Value recap:** a personalised usage summary (boards, automations, agent runs, AI credits used this cycle) with real counts in slots. Never guilt copy
- **Offer mechanics:** for each offer, what changes on accept (pause length, target plan, target seat bundle, target credit package, discount duration) and when it takes effect, per the context file's effective-date rules

### Downgrade path — mandatory, even in a cancel-only brief
- **Target options:** every lower tier, the next seat bundle down that fits active seats, the smaller credit package, and Free, with the ones monday doesn't support self-serve marked as such
- **Loss list:** from this account's usage, ranked: `Item · Used how much · What happens (read-only / switched off, not deleted / removed) · When`. Omit what the account has never used
- **Keep list:** what stays, listed first when the lower plan is solid
- **Irreversible loss:** anything deleted or not restorable on re-upgrade is stated in the flow, before confirm, with the export action beside it
- **Preconditions:** e.g. seat reductions need active seats at or below the target first (context file). Spec the screen that explains the precondition and links to the fix
- **Effective date and price:** the date the change takes effect, the new price from that date, and the cadence

### Confirmation
- **Final screen:** exact date access ends or the change applies, "you won't be charged again" (or the next charge if a downgrade), the data retention rule, the export action, and the way back ("reactivate before {end_date}")
- **One click, no loops:** exactly one confirmation. No second "Are you sure?"
- **Receipt:** confirmation email content (end date, retention, reactivation link) and the in-app notice

### Post-cancel and win-back — mandatory
- **Pre-end-date state:** in-app banner (who sees it: admins only, or all members), "Reactivate" in one click, and what members see
- **End-of-access state:** where the account lands (lower plan, Free, trial window, inactive), what members see when they sign in, and how data can still be exported
- **Win-back sequence:** the triggers and timing ({winback_schedule}), the content order (what's new → your data is still here → a time-limited return offer, per the playbook's step 5), the stop conditions (reactivated, unsubscribed, deleted), and the stacking rule with [promotions.md](promotions.md)
- **Return path:** a returning admin reactivates with their previous configuration. Spec what's restored and what isn't

### Governance
- **Compliance:** "continue to cancel" (or the jurisdiction's equivalent) is visible on every screen, on the same screen as any offer. Consumer-only rules are flagged per the playbook's legal table
- **Measurement:** save rate by reason, offer acceptance, 30/90-day retention of saved accounts, downgrade-vs-cancel mix, and a holdout ({holdout_pct}) that sees no offer

## Trigger logic spec

```
Trigger conditions:
- Entry: user selects cancel, downgrade, reduce seats or reduce credit package at {entry_points}
- Route before the flow:
  - Viewer isn't an admin → request-to-admin screen (no cancel flow)
  - {billing_channel} = invoice | Enterprise | account-managed → account-team path, date + contact
  - Account ≥ {high_value_threshold} (health or MRR) → offer a person first; skippable
  - Refund-eligible (context file) → state the access consequence before confirm
- Offer selection: exactly one offer, from the spec's reason → offer map; no reason given → no offer
- Suppress an offer when: the same offer was accepted within {offer_cooldown}; the pause limit is
  reached ({max_pauses} per {pause_period}); the account is past the notice deadline and the offer
  would read as preventing a renewal it can't prevent

Frequency cap:
- The flow: none — user-initiated, shown in full every time
- Offers: one per session; a declined offer isn't shown again in the same flow
- Post-cancel banner: persistent until the end date; dismissible per session

Dismiss behaviour:
- Back / close at any step: nothing changes; no exit-intent interstitial
- "Continue to cancel": visible on every screen, on the same screen as the offer, equal in weight to
  the accept action's secondary link
- Offer accepted: confirmation of exactly what changed and when, with an undo

Re-show rules:
- Re-entry after abandoning: restarts at the reason step; the previous reason is pre-selected if
  captured within {reason_memory}
- Win-back: per {winback_schedule} after access ends, plus the in-app state on return; stops on
  reactivation, unsubscribe or data deletion
- Pending cancellation: the Reactivate path stays live until {end_date}; no save offer is pushed
  after confirm
```

## Choosing a pattern

Patterns: [wireframe-patterns.md](wireframe-patterns.md) → Cancellation.

| Situation | Pattern | Rule |
|---|---|---|
| Cancel intent (self-serve admin) | **A** — reason → one offer → confirm | Three steps with a step indicator and "continue to cancel" on each |
| Downgrade to a lower tier, seat reduction, or credit-package reduction | **B** — downgrade confirmation with loss list | Keep / lose / when, irreversible loss before confirm |
| A "right-size" offer accepted inside A | **A** hands off to **B** | The accepted offer lands on B's confirmation, not a new flow |
| Non-admin or sales-assisted account | Routing screen (no pattern) | One screen: who can do this, how to reach them, the relevant date |
| Post-cancel | **A**'s after-state (banner) | Persistent until the end date, with Reactivate |

## Edge cases specific to cancellation

In addition to every case in [spec-checklist.md](spec-checklist.md):

- **IC vs admin:** only admins can cancel ([monday-context.md](../../../context/monday-context.md)). For multi-seat accounts, the IC gets a "request to cancel" that notifies the admin. Never a dead end, never a cancel.
- **Annual vs monthly:** end dates, notice deadlines and refund eligibility differ by cadence. Show the rule for this account, not a generic one.
- **Mid-cycle:** downgrades and reductions take effect at renewal (context file). Show "until {date} you keep {current_plan}". If a right-size offer is an *upgrade* in disguise (e.g. annual at a lower rate), show its proration.
- **Notice window already passed:** the flow still cancels future renewal, but states the term the account is committed to, before confirm.
- **Multi-product accounts:** each product cancels separately, and closing the account needs every product cancelled (context file). Spec which product the flow acts on and what happens to the others.
- **Credit-only shed:** when the reason is AI cost or AI non-use, the offer reduces the credit package and keeps the seats. Say what AI capabilities stop and which free AI features keep working (context file).
- **Scheduled downgrade then over-limit:** an account that schedules a seat downgrade and then exceeds the target before renewal. State the consequence on the confirmation screen (context file: the account stays on the current plan until renewal and can auto-upgrade).
- **Agents and automations running at end of access:** spec what happens to in-flight runs on the end date and what the owner is told beforehand.
- **Refund-eligible new customer:** a refund can end access immediately (context file). Put the export action on the same screen as confirm.
- **Paid via app store:** if the subscription was bought through a platform store, route to that store's cancel path and say so.
- **Deep links:** a "cancel" link from email or support opens the flow at step 1 for admins, and the routing screen for everyone else. The link never bypasses the notice or data lines.
- **Localized legal variants:** where a jurisdiction requires a specific cancel control or confirmation page (playbook legal table), the spec lists the variant and how the region is detected.
- **Mobile:** every step fits one screen at 375px, "continue to cancel" stays above the fold, and the loss list collapses to its top {N} items plus "see all".

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Cancellation, Pattern A (reason → one matched offer → confirm) and Pattern B (downgrade confirmation with loss list).

## Copy hook
Primary reason: feel secure. See [copy-hooks.md](copy-hooks.md#cancellation-flow-surface-6). Always hand copy finalisation to `improve-conversion-surfaces-copy`.

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Copy (write before the wireframe): `.monetization/{feature-slug}/02-copy.md`
- Wireframe (built from that copy): `.monetization/{feature-slug}/03-wireframe.html`
- The wireframe shows the flow strip (intent → reason → offer → confirm → post-cancel), with the downgrade confirmation and the routing screen as states, each with real copy. The notice line, the loss list and the "continue to cancel" label are the strings that can't ship as placeholders

## Next step

After the spec:
```
---
→ Next step: improve-conversion-surfaces-copy — write the reason, offer, loss-list, confirmation and win-back copy from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

After the wireframe (built once copy exists):
```
---
→ Next step: monetization-design-reviewer — score the cancellation spec, copy, and wireframe together
→ Prompt: "Review .monetization/{feature-slug}/"
```
