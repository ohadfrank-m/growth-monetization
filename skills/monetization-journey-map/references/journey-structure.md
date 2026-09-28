# Journey structure — stages, steps, skeletons

## Five stages

Every monetization journey runs through the same five stages. Most designs only cover the third one. The journey map covers all five, because that's where the handoffs break.

| Stage | What it covers | Why it matters |
|---|---|---|
| **Before** | What the user was doing, and what they built or used that sets up the moment | Sets the state of mind and the "competing intent" the surface must not destroy |
| **Trigger** | The event that brings the surface up: a click, a limit, a date, a balance | The trigger decides timing, and timing decides most of the outcome |
| **On-surface** | Every screen and state of the surface itself | This is what the spec and wireframe design |
| **Hand-off** | Checkout, payment, the admin request, the sales handoff, the confirmation | Where IC → admin and self-serve → sales journeys most often stall |
| **After** | Resume the task, the email, the invoice, the next renewal, win-back | Decides whether the conversion sticks and whether the next surface is trusted |

## The step table

One row per step, in order. Branches are rows too (`J4a`, `J4b`).

| Column | What goes in it |
|---|---|
| **J#** | `J1`, `J2`, …; branches `J4a`, `J4b`. The spec and the review cite these ids |
| **Stage** | before · trigger · on-surface · hand-off · after |
| **Step** | What happens, as an action: "Admin opens Billing → Cancel product" |
| **Channel** | in-app · email · admin notification · invoice / billing page · sales / CSM · external (app store, card statement) |
| **Scenarios** | Which scenarios pass through it (S1, S3) |
| **User goal** | What the persona is trying to get done at this step, in their words |
| **State of mind · reason** | How they feel (in a hurry, anxious about cost, annoyed, curious) and the one reason from the 15 reasons people buy that moves them here ([sources.md](../../improve-conversion-surfaces-copy/references/sources.md)). The copy skill writes to this |
| **System state** | What the product knows and does: balance, plan, role, trial day, what's saved |
| **Branches** | Each exit: success → J#, abandon → J#, error → J#, IC path → J# |
| **Friction → reduction** | Where they'll hesitate or drop, and the design choice that reduces it. "none — {why}" is allowed |
| **Event** | The analytics event or metric that proves the step happened (`cancel_flow_reason_submitted`). "{event TBD}" + Open item if unknown |
| **Wireframe state** | Every step rendered in the product — on-surface, and any hand-off or after step that has a screen (a `scheduled` confirmation, a banner until the end date, an access-ended screen): the state id the spec and wireframe must use (`reason`, `offer-pause`). It becomes `03-wireframe.html#{id}` and is what the board embeds |

## Stage skeletons per surface type

Start from the skeleton, then add or cut steps from the scenarios. Each skeleton's on-surface steps follow the surface's playbook, cited for the why. The thresholds and phase windows stay owned there.

**1 · Pricing page** ([playbook](../../../playbooks/pricing-pages.md)): before (in-app work, or an ad/search visit) → trigger (clicks "See plans", a gate's "See all features", or a campaign link) → on-surface (plan comparison, billing toggle, seat choice) → hand-off (plan summary → payment, or "Talk to sales") → after (plan applied, back to origin, confirmation email, first invoice).

**2 · Paywall / feature gate** ([playbook](../../../playbooks/paywalls.md)): before (working in a board or agent setup) → trigger (clicks the locked feature, or opens a deep link) → on-surface (preview → value proof → paths: upgrade, trial or notify admin) → hand-off (plan summary or trial start; for an IC, the admin request → admin decision) → after (the feature unlocks in place and the action resumes; the IC learns the decision).

**3 · Promotion** ([playbook](../../../playbooks/promotions.md)): before (eligibility builds: tenure, usage, renewal date) → trigger (campaign window, or a lifecycle moment) → on-surface (banner or modal → offer detail) → hand-off (discount applied at plan summary) → after (discount on the invoice, notice before it ends, price returns to list, and whether the discounted cohort retains).

**4 · Tier upgrade trigger** ([playbook](../../../playbooks/upgrade-triggers.md), which owns the thresholds): before (usage climbs) → trigger (approach warning, then the limit) → on-surface (limit state → next-tier value → bundle or tier choice) → hand-off (admin purchase, or IC → admin request → decision) → after (limit lifted, work resumes, pro-rated charge, next invoice).

**5 · Credit / consumption UI** ([playbook](../../../playbooks/credit-ui.md), which owns the thresholds): before (agents and AI features running) → trigger (warning → critical → depleted, or a pre-spend estimate) → on-surface (meter → depletion state → package choice) → hand-off (top-up purchase, or IC → admin request) → after (credits land, the paused run resumes where it stopped, receipt, and the next cycle's reset).

**6 · Cancellation / downgrade** ([playbook](../../../playbooks/cancellation.md)): before (usage drops, or a budget review) → trigger (admin opens cancel or downgrade) → on-surface (intent → reason → one reason-matched offer → confirmation, with a downgrade branch) → hand-off (cancel or downgrade scheduled for its effective date) → after (confirmation email, access until the end date, data retention window, reactivation, win-back).

**7 · Trial flow** ([playbook](../../../playbooks/trial-flows.md), which owns the phases): before (signup, with or without enrichment) → trigger (trial start) → on-surface (setup phase → proof phase → decision phase → expiry decision) → hand-off (plan choice → payment, or continue on Free) → after (converted workspace, or a lapsed trial with data kept, then re-engagement).

## Quality bar

- Every step rendered in the product has a wireframe state id, and no two steps share one unless they are genuinely the same screen.
- Every step that changes billing (buy, top up, cancel, downgrade) has an IC branch: only admins can act on it, and the person who reaches the step often can't.
- Every "after" stage names at least one non-app channel (email, invoice, admin notification). That's where trust is kept or lost.
- Abandon is a branch on every on-surface step. Where does the user land, and what state is saved?
