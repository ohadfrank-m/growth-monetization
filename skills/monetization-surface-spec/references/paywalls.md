# Paywall / feature gate — spec reference

Surface type 2: user tries to access a locked feature.

CRO rationale, benchmarks, best-in-class examples, and the **gate timing and frequency rules** (owned there) live in the shared playbook. Read it before drafting: [../../../playbooks/paywalls.md](../../../playbooks/paywalls.md). Which tier unlocks what: [monday-context.md](../../../context/monday-context.md#feature-gating-by-tier). This file covers only what's specific to *writing the spec*.

Not this surface: a tier or seat *limit* (a count running out) is [upgrade-triggers.md](upgrade-triggers.md). A credit balance running out is [credit-ui.md](credit-ui.md).

## When this surface appears

- **Intent gate, admin, trial available:** clicks a locked feature, view, column type or action. The account can start a trial of the target tier
- **Intent gate, admin, no trial:** same click, but the trial is used or not offered, so the paths are upgrade or not now
- **Intent gate, IC:** same click, from a viewer who can't purchase
- **Request pending:** the IC already asked the admin and clicks the feature again
- **Compact gate:** repeat clicks past the dismiss count set in the playbook's timing rules
- **Deep-link gate:** arrives by URL (shared link, email, template) at a feature the tier doesn't include
- **Sample-then-lock:** a use-based allowance: the warning before the lock, then the locked state
- **Preview running:** the user tries the feature on their own data before the ask (only if the spec uses a live preview)
- **Downgraded content:** the account built something on a feature it no longer has, after a downgrade or trial end. The gate covers existing content
- **Sales-assisted unlock:** the feature is Enterprise-only, so the unlock goes through sales
- **Post-unlock:** upgrade or trial started, and the user is back at the exact entry point with the feature on
- **Admin decision:** the request notification and the approve/decline screen (if in scope)

## Mandatory spec sections for paywalls

All sections in the surface spec template apply. Additionally, always address:

### Gate definition
- **Entry-point inventory:** a table, one row per entry point: `Entry point · Surface · Gated action · Target tier · Blocking level`
- **Target tier:** the lowest tier that unlocks the feature, per the context file. Don't push Pro if Standard unlocks it
- **Locked vs still working:** the exact action that's gated (create, save, schedule, run, export, share) and what the user can keep doing. Gate the last mile, not the first step, where the feature allows it
- **Blocking level:** modal vs. inline banner, with justification. Agent and automation contexts are non-blocking

### Value before the ask
- **Preview:** what the user sees (blurred, sample data, their own data, short demo) and where the preview data comes from
- **Preview cost:** whether the preview consumes AI credits. Free has none ([monday-context.md](../../../context/monday-context.md)), so an AI preview for Free users must not need them
- **Value proof:** 3 concrete use cases, or a personalised example from the user's workspace

### Paths
- **Trial path:** the eligibility rule, the trial tier, and what the current screen does when the trial starts (the feature unlocks in place)
- **IC vs. admin:** "Notify admin", pre-filled with the feature, where it was hit, and an optional reason. Spec what the admin receives (channel, content, CTA), what the IC sees after sending, and how the IC learns the decision
- **Price on the admin path:** plan, seats and cadence on or beside the CTA, or a link to the plan summary
- **Post-unlock return:** the exact landing: same board/view, feature active, the attempted action resumed or one click away

### Rules
- **Dismiss and frequency cap:** see the trigger block below
- **Existing content after downgrade:** read-only, hidden, or switched off (not deleted), and how the gate explains which
- **Measurement:** gate view → CTA → trial start or upgrade → feature used within {N} days; IC request → admin decision → unlock

## Trigger logic spec

```
Trigger conditions:
- Intent gate: user attempts {gated_action} on {feature} AND account tier < {target_tier}
- Deep-link gate: route resolves to {feature} AND tier < {target_tier} → render the gate over the
  feature's shell (never a 404 or a silent redirect to home)
- Sample-then-lock warning: {uses_left} ≤ {warn_at}; if the allowance is a tier limit, its
  thresholds are owned by playbooks/upgrade-triggers.md (Threshold ladder)
- Downgraded content: user opens content built on {feature} after the tier fell below {target_tier}
- Suppress: account already on {target_tier} or trialling it (re-check entitlement before render);
  first session before activation; mid-task when the task doesn't need {feature}

Frequency cap (values owned by playbooks/paywalls.md — Timing and frequency):
- Intent-triggered gate: every click — the user asked; switch to the compact variant after
  {compact_after} dismissals in {compact_window}
- Unprompted gate (product-initiated): {per_session_cap} per session; not again within
  {post_dismiss_window} of a dismiss
- Request pending: the requester never sees the full gate again for {feature}; show the pending state

Dismiss behaviour:
- "Not now" returns to the prior screen unchanged; the locked entry point stays marked
  (glyph, not colour alone)
- IC request sent: inline confirmation; the entry point shows "Requested" until the admin decides

Re-show rules:
- Intent gate: on the next click, full or compact per the cap
- Unprompted gate: not before {post_dismiss_window}; never on a timer independent of behaviour
- Admin declined: the IC sees the decision once; the entry point returns to the default IC gate
```

## Choosing a pattern

Patterns: [wireframe-patterns.md](wireframe-patterns.md) → Paywall / feature gate.

| Situation | Pattern | Rule |
|---|---|---|
| Feature has its own surface (a view type, agent setup, AI column) and can be previewed | **A** — preview + gate | Default for an intent gate on a feature the user hasn't used |
| Feature sits inside a workspace the user is working in, or the gate fires while an agent or automation is running (setting up an agent is Pattern A) | **B** — inline gate | Non-blocking by rule in agent contexts |
| Repeat clicks past the compact threshold | **B**, compact variant | Preview collapsed, CTA kept |
| Architecturally separate feature, no preview possible, explicit intent | **A** without the preview (hard gate) | The spec must justify it. Rare in PLG ([playbook: two gate models](../../../playbooks/paywalls.md)) |
| Downgraded content | **B** on the content itself | Says read-only vs switched off, and names the way back |
| IC viewer | Same pattern as the admin | Primary CTA becomes "Notify admin". The price stays visible |

## Edge cases specific to paywalls

In addition to every case in [spec-checklist.md](spec-checklist.md):

- **IC vs admin, multi-admin:** name who receives the request (all admins, billing admin, workspace owner) and what happens if two ICs request the same feature.
- **Trial state:** an account in a Pro trial sees no Pro gates. If it hits an Enterprise-only feature, it gets the sales path, and the gate never offers a trial the account can't start.
- **Annual vs monthly:** the price on the CTA uses the account's cadence. A mid-cycle upgrade's proration appears in the plan summary, per [monday-context.md](../../../context/monday-context.md) (plan-change rules: an open item until the file carries them).
- **Multiple gates in one session:** follow the cross-surface rule in spec-checklist.md. On this surface, a second *different* locked feature still shows the full gate, because the dismiss count is per feature.
- **Deep link from higher-tier content:** a shared board or template built on a feature the viewer's tier lacks opens with the content visible and the gate on the gated action, not a blank page.
- **Stale entitlement:** the user upgraded in another tab or device. The gate re-checks entitlement before rendering and on focus.
- **Guest or viewer:** if the unlock is a user-type change (viewer → member) rather than a tier, route to [upgrade-triggers.md](upgrade-triggers.md) seat logic.
- **Credit-gated AI on a tier that includes it:** that's a balance problem, not a gate. Use [credit-ui.md](credit-ui.md).
- **Localized price on the CTA:** billing currency per spec-checklist.md. Otherwise, link to the plan summary instead of showing a number.
- **Sales-assisted accounts:** the CTA goes to the account team with the feature pre-filled. No self-serve checkout.
- **Mobile:** the modal becomes a full-height sheet, the preview is reduced to a static image, and the CTA stays sticky. Nothing is gated on mobile that's open on web.

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Paywall, Pattern A (preview + gate) and Pattern B (inline gate).

## Copy hook
New users: alleviate fear of missing out. Existing users: capability gain. See [copy-hooks.md](copy-hooks.md#paywall--feature-gate-surface-2). Always hand copy finalisation to `improve-conversion-surfaces-copy`.

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Copy (write before the wireframe): `.monetization/{feature-slug}/02-copy.md`
- Wireframe (built from that copy): `.monetization/{feature-slug}/03-wireframe.html`
- States in the wireframe: at minimum admin with trial, admin without trial, IC, request pending, compact, and post-unlock, each with real copy. The IC's request confirmation and the pending label are the lines most often left as placeholders

## Next step

After the spec:
```
---
→ Next step: improve-conversion-surfaces-copy — write the gate headline, value proof, CTA and IC-request copy from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

After the wireframe (built once copy exists):
```
---
→ Next step: monetization-design-reviewer — score the paywall spec, copy, and wireframe together
→ Prompt: "Review .monetization/{feature-slug}/"
```
