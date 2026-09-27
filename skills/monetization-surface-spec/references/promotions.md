# Promotion — spec reference

Surface type 3: discount, limited-time offer, annual upsell, capacity or credit bonus, upsell banner or modal.

CRO rationale, benchmarks, legal context, and best-in-class examples for this surface live in the shared playbook. Read it before drafting: [../../../playbooks/promotions.md](../../../playbooks/promotions.md). Anchor prices come from [monday-context.md](../../../context/monday-context.md). This file covers only what's specific to *writing the spec*.

Not this surface: a retention offer inside the cancel flow is owned by [cancellation.md](cancellation.md). This file only sets how the two stack.

## When this surface appears

- **Offer live, eligible, not yet seen:** campaign window, lifecycle moment (first renewal, lapsed account), or a behaviour-targeted offer
- **Offer live, seen and dismissed:** the offer still applies on the pricing page and plan summary until expiry
- **Final window:** the last {final_window} before the real end date
- **Applied at plan summary / checkout:** auto-applied (targeting or link) or entered as a code
- **Code entry:** valid, invalid, expired, not eligible, or already used, each a distinct state
- **Arrived from a campaign link or email:** eligibility re-checked on arrival
- **Offer expired:** the user arrives from an old link, or a cached banner reopens
- **Ineligible viewer:** sees the regular price. The spec decides whether the page says anything about the offer
- **Redeemed:** discount active on the subscription. The account shows what it pays now and when that ends
- **Discount ending:** notice before the price returns to list
- **Holdout:** eligible, but in the control group, so the viewer gets the regular experience

## Mandatory spec sections for promotions

All sections in the surface spec template apply. Additionally, always address:

### Offer terms
- **Offer:** type (percent off, amount off, extra credits or capacity, trial change), amount, what it applies to (seats, credits, first N months, a product), the cadences it covers (monthly, annual, both), and the **anchor price** from the context file with its `last-updated` date
- **Duration:** first invoice only, N months, the full term, or ongoing. State what the user pays afterwards and from which date. For N-month offers on annual plans, say how the offer applies to an annual invoice
- **Expiry:** the real deadline, as date, time and timezone, from one source of truth that every placement reads. Spec what happens when it passes (banner removed, links fall back, code invalid)
- **Stacking and precedence:** with the annual saving, nonprofit / education / startup programs, prior promotions, and cancel-flow retention offers. Which one wins when two apply

### Audience
- **Eligibility:** exact rules: tier, tenure, region, role, activation state, prior exposure, prior redemption
- **Exclusions:** pre-activation users, users who converted without an offer, already-discounted accounts, sales-assisted accounts, and any region flagged by legal
- **Holdout:** share of the eligible audience that sees nothing: {holdout_pct}, and how it's assigned (per account, not per user)

### Delivery
- **Placements:** banner, modal, in-context card, email + in-app, pricing-page badge, plan-summary line. Give each its own state list
- **Redemption mechanics:** auto-applied or by code. For codes: case-insensitive, per-account limit, restrictions (first purchase only, minimum spend, expiry, total redemption cap), and what each rejection says
- **Admin vs IC:** only admins can redeem. Spec the IC variant ("share with admin") or suppress the offer for ICs
- **Billing side effects:** the spec states that redeeming changes no billing setting other than the discounted price ([playbook](../../../playbooks/promotions.md), Claude teardown)
- **Post-redemption display:** where the discount shows afterwards (billing page, invoice line), and the end-of-discount notice with its timing

### Governance
- **Legal review:** any consumer-facing anchor or time limit gets the playbook's legal-review line before shipping
- **Measurement:** holdout comparison, the incrementality metric, and retention of the discounted cohort. Redemption rate alone isn't a success metric ([playbook: Measurement](../../../playbooks/promotions.md))

## Trigger logic spec

```
Trigger conditions:
- Offer live: now ∈ [{start_datetime}, {end_datetime}] ({timezone}) AND viewer matches
  {eligibility_rule} AND account not in holdout
- Eligibility is re-checked at checkout: a banner seen while eligible never guarantees a price that
  has since expired, and an ineligible banner view never blocks a valid checkout
- Final window: now ≥ {end_datetime} − {final_window}; show the fixed end date/time — a countdown
  only if it counts to that fixed, server-side deadline and never restarts
- Suppress: first session / pre-activation; account converted without an offer; account holding a
  non-stacking discount; any functional block on screen (depletion, at-limit gate, expiry decision) —
  see spec-checklist.md, multiple asks in one session

Frequency cap:
- Banner: {banner_max_views} per {period} until dismissed
- Modal: at most once per campaign per user
- Pricing-page badge / strike-through / plan-summary line: every view while live and eligible —
  it's price information, not a nudge
- Email + in-app: never both on the same day for the same offer unless the spec says why

Dismiss behaviour:
- Banner dismiss: holds for the whole campaign, stored on the user (not the browser), all devices
- Modal dismiss: the offer stays available on the pricing page and plan summary until expiry

Re-show rules:
- At most one re-show in the final window if dismissed and not redeemed — spec it, or write "none"
- After expiry: never; old links land on the regular price with one line naming the end date
- A new campaign resets the caps only if its eligibility allows repeat exposure
```

## Choosing a pattern

Patterns: [wireframe-patterns.md](wireframe-patterns.md) → Promotion.

| Situation | Pattern | Rule |
|---|---|---|
| In-product awareness, persistent but dismissible | **A** — banner | One offer, one CTA, real anchor and end date |
| High-value, one-time offer (monthly → annual, launch window) | **A** — modal variant | Once per campaign, never over an active task |
| Offer tied to a moment (approaching a limit, feature use) | **A** — in-context card | The moment's own reference owns the trigger. This file owns the terms |
| User already choosing a plan, or arriving with a code or link | **B** — applied at plan summary | Discount line, anchor, total today and post-promo price in one view |
| Cancel-flow retention offer | Not this reference | [cancellation.md](cancellation.md). This file only defines stacking |

## Edge cases specific to promotions

In addition to every case in [spec-checklist.md](spec-checklist.md):

- **IC vs admin:** an IC who sees a campaign email or banner can't redeem. Spec the share path, or don't target ICs.
- **Annual vs monthly:** say which cadences qualify, how a percent applies on each, and whether switching cadence mid-promotion keeps, drops or recalculates the discount.
- **Mid-cycle plan change:** if the promotion applies to an upgrade, state whether the discount also applies to the proration charge or only to future invoices, and show that line in the plan summary.
- **Several offers eligible at once:** a precedence rule (highest value, most specific, or newest) plus what the loser shows. Never two discount lines unless the stacking rule allows it.
- **Localized pricing / currency:** amount-off offers need a value per currency. Percent-off offers need a local anchor from the context file. Anything missing is an open item.
- **Time zones:** the end is one instant, shown in the viewer's local time with the timezone named.
- **Deep links:** expired, ineligible, already-used or shared codes each land on the regular price with a one-line reason. Never an error page, and never a silent full price.
- **Payment failure at checkout:** the promotion isn't consumed, and the retry keeps it.
- **Cancel or refund after redemption:** what happens to the discount on reactivation, and whether a win-back offer can stack on it.
- **List price changes mid-campaign:** the anchor and the offer price update together, from the context file.
- **Sales-assisted accounts:** excluded, or routed to the account team with the offer named.
- **Mobile:** the banner collapses to one line plus CTA, and the strike-through and end date stay legible at 375px.

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Promotion, Pattern A (in-app banner/modal with anchor and end date) and Pattern B (discount applied at plan summary).

## Copy hook
Primary reason: save money. Secondary: alleviate fear of missing out. See [copy-hooks.md](copy-hooks.md#promotion-surface-3). Always hand copy finalisation to `improve-conversion-surfaces-copy`.

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Copy (write before the wireframe): `.monetization/{feature-slug}/02-copy.md`
- Wireframe (built from that copy): `.monetization/{feature-slug}/03-wireframe.html`
- States in the wireframe: offer live, final window, applied at plan summary, code rejected, expired-link fallback and redeemed, each with real copy. The terms line and the post-promo price line are the strings most often left as placeholders

## Next step

After the spec:
```
---
→ Next step: improve-conversion-surfaces-copy — write the offer line, terms line, end-date line and plan-summary lines from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

After the wireframe (built once copy exists):
```
---
→ Next step: monetization-design-reviewer — score the promotion spec, copy, and wireframe together
→ Prompt: "Review .monetization/{feature-slug}/"
```
