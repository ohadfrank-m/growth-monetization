# Pricing page — spec reference

Surface type 1: public (marketing site) or in-app plan comparison, plus the plan summary it hands off to.

CRO rationale, benchmarks, and best-in-class examples for this surface live in the shared playbook. Read it before drafting: [../../../playbooks/pricing-pages.md](../../../playbooks/pricing-pages.md). Current plans, prices, seat bundles and credit packages: [monday-context.md](../../../context/monday-context.md). This file covers only what's specific to *writing the spec*.

A pricing-page spec covers both contexts unless the brief scopes it to one. The public page and the in-app page share plan data, but they differ in who's looking, what that person already owns, and whether they can pay.

## When this surface appears

**Public (marketing site, logged out)**
- **Default:** direct or organic navigation, no account context
- **Campaign / deep link:** arrives with parameters (plan, billing cadence, seats, promo) from an ad, email or partner link
- **Localized:** the visitor's region implies a non-USD currency or a tax-inclusive price display
- **Known visitor:** a logged-in session is present on the marketing domain. The spec decides whether the page switches to in-app behaviour or stays generic

**In-app (logged in)**
- **Admin on Free or in trial:** "See plans" / "Upgrade" from billing, a gate, or a trial surface
- **Admin on a paid plan:** current plan marked. Higher tiers are upgrades; lower tiers route to the downgrade flow
- **IC (non-admin):** sees the plans but can't buy. Every purchase CTA becomes a request to the admin
- **From a gate or trigger:** arrives carrying the feature or limit that sent them ("See all Pro features")
- **Sales-assisted account:** Enterprise, invoice-billed, or managed by an account team. Self-serve purchase is replaced by the account-team path

**Hand-off**
- **Plan summary:** the confirmation step after a plan is chosen: plan, seats, cadence, discounts, proration, tax, total today, next bill
- **Post-purchase:** plan applied, and the user returns to where they came from
- **Price data unavailable:** prices fail to load, or the account's price can't be resolved

## Mandatory spec sections for pricing pages

All sections in the surface spec template apply. Additionally, always address:

### Context and state detection
- **Context matrix:** a table of every state above that's in scope × what renders (headline, recommended tier, CTA per tier, current-plan marker). A state that's out of scope is listed as N/A with a reason
- **Account-state inputs:** the signals that choose the in-app state (role, current tier, trial status, billing channel, credit model), and what renders while they load

### Plan data
- **Plan structure table:** every tier, annual and monthly price, seat minimum and bundles, AI credit inclusion. Pull current values from [monday-context.md](../../../context/monday-context.md) and cite its `last-updated` date. Never hardcode a price without that date
- **Billing toggle:** default state (per the context file), savings label (dollars, percent, or both), and what changes on toggle (seat price, credit price, billed-total line)
- **Price format:** per seat per month, with the cadence stated. For annual, also the billed total. Use one format per page
- **Seat selector:** how the minimum and the bundle steps are communicated. The price shown is the bundle total, never a per-seat add-on (bundle rule: [upgrade-triggers playbook](../../../playbooks/upgrade-triggers.md))
- **AI credits presentation:** credits per tier, with the context file's official task translation (translation rule owned by [credit-ui playbook](../../../playbooks/credit-ui.md)). State whether packages above the minimum appear as a selector or as an "add more anytime" line
- **Currency and tax:** which currencies the page renders, where each currency's price comes from, and whether tax is included or added on top. A currency the context file doesn't publish is an open item. Never convert a USD price for display

### Choice architecture
- **Recommended tier logic:** which tier is highlighted and why: static, or personalised by traffic source or account state. Name the rule and its inputs
- **Per-tier headline:** one job-to-be-done per tier, not a feature list
- **CTA per tier:** each tier's label and destination in each state (public / admin / IC / current plan)
- **Current-plan marker (in-app):** how the current tier is shown, and what its CTA does (manage, add seats, nothing)
- **Free and Enterprise treatment:** visually distinct from the paid comparison. Enterprise gets "Talk to us" plus a self-serve path if one exists
- **Feature comparison:** collapsed by default. List which 5–7 rows stay visible, and how the row that sent a gate user here is highlighted

### Hand-off
- **Plan summary:** what the confirmation step shows before any charge: plan, seats, cadence, list price, discount lines, proration credit, tax, total today, next bill date and amount. Mid-cycle rules come from [monday-context.md](../../../context/monday-context.md) (plan-change rules: an open item until the file carries them). Mark them open items if that section is missing
- **Downgrade path:** choosing a lower tier in-app routes to the downgrade flow ([cancellation.md](cancellation.md)), never to checkout
- **Return path:** where each successful purchase lands: the origin screen, with the feature that sent the user there now unlocked
- **Mobile:** how columns collapse (stacked cards or swipeable), which card comes first, and what happens to the toggle and the comparison table

## Trigger logic spec

A pricing page is navigation-initiated, so its trigger logic is render logic plus the rules for the nudges that point to it:

```
Render conditions:
- Public: billing default per monday-context.md; recommended tier = {recommended_tier} ({static | rule: inputs})
- Deep link: honour {plan}, {billing}, {seats}, {promo}; an invalid, expired or ineligible
  parameter falls back to the default render — never an error page
- In-app admin: {current_tier} marked current; tiers above → upgrade CTA; tiers below → downgrade flow
- In-app IC: every purchase CTA → "Ask admin"; request already pending → pending state, no duplicate
- From a gate/trigger: carry {source_feature}; pre-highlight the lowest tier that unlocks it;
  the recommended badge doesn't move
- Sales-assisted ({billing_channel} = invoice | Enterprise | account-managed): self-serve CTAs
  replaced by the account-team path

Frequency cap:
- The page itself: none — the user asked for it
- In-app "See plans" nudges that link here: the unprompted-paywall cap owned by
  playbooks/paywalls.md (Timing and frequency)
- Promo badge or strike-through on a tier: only while the offer is live and the viewer is eligible
  (promotions.md)

Dismiss behaviour:
- In-app overlay or page: close/back returns to the exact origin (board, view, item), nothing changed
- Plan summary: back returns to the page with the selection kept; abandoning charges nothing

Re-show rules:
- None from this surface. An abandoned-checkout follow-up is a separate promotion or lifecycle spec
```

## Choosing a pattern

Patterns: [wireframe-patterns.md](wireframe-patterns.md) → Pricing page.

| Situation | Pattern | Rule |
|---|---|---|
| Public page, or in-app "See plans" comparing tiers | **A** — plan comparison | The default. With five tiers, the comparison cards are the paid middle; Free and Enterprise are treated distinctly ([playbook: tier count](../../../playbooks/pricing-pages.md)) |
| In-product upsell of one tier for one feature | **B** — inline banner | Only if the ask is a single tier. If the user was *blocked*, the surface is a paywall or upgrade trigger, so use that reference |
| After a plan is chosen | **Plan summary** — Promotion, Pattern B layout | Every discount, proration and next-bill line lives on one screen |
| IC viewer | Same pattern as the admin | Swap purchase CTAs for "Ask admin". Never hide prices |

## Edge cases specific to pricing pages

In addition to every case in [spec-checklist.md](spec-checklist.md):

- **IC vs admin:** the IC sees prices (hiding them blocks the IC's case to the admin) but no purchase CTA. Spec the request payload: tier, reason, source feature.
- **Annual vs monthly, mid-cycle:** a monthly admin switching to annual, or upgrading mid-term, sees the proration credit and the new billing-cycle start in the plan summary. A downgrade chosen from the page is scheduled, not immediate, and the screen shows its effective date.
- **Legacy credit model:** the current AI-credit model applies to customers who joined on or after its start date ([monday-context.md](../../../context/monday-context.md)). Spec what the in-app page shows older accounts, or list it as an open item.
- **Localized pricing / currency:** in-app, the page's currency matches the currency the account is billed in. Public visitors see a regional currency only if the context file publishes it. Spec the fallback.
- **Tax display:** tax-inclusive regions need a different price line. Spec it per region, or mark it open.
- **Seat minimum and Free cap:** a 1–2 person team sees Free as the fit. A team one seat past a bundle sees the next bundle's price, not a per-seat price.
- **Multi-product accounts:** which product's plans the page shows when the account has more than one, and whether a cross-product entry appears.
- **Sales-assisted:** invoice-billed accounts can't self-serve plan changes (plan-changes section of the context file). Every CTA goes to the account team.
- **Deep link vs account state:** when a parameter conflicts with the account (e.g. `plan=standard` for a Pro admin), render with Pro marked current. Never pre-select a downgrade.
- **Promotion live:** show a strike-through only with the genuine anchor, and declare stacking with the annual saving ([promotions.md](promotions.md)).
- **Trial user in-app:** show the trial days left. Lower-tier cards must not contradict the trial's expiry messaging ([trial-flows.md](trial-flows.md) owns it).
- **Price-load failure:** never render $0 or a blank price. Show a retry state with purchase CTAs disabled.

## Wireframe pattern
See [wireframe-patterns.md](wireframe-patterns.md) — Pricing page, Pattern A (plan comparison) and Pattern B (inline banner). The plan summary uses Promotion, Pattern B.

## Copy hook
Primary reason: make money / save time. Enterprise: feel secure. See [copy-hooks.md](copy-hooks.md#pricing-page-surface-1). Always hand copy finalisation to `improve-conversion-surfaces-copy`.

## Output files

- Spec: `.monetization/{feature-slug}/01-spec.md`
- Copy (write before the wireframe): `.monetization/{feature-slug}/02-copy.md`
- Wireframe (built from that copy): `.monetization/{feature-slug}/03-wireframe.html`
- The wireframe's state switcher covers every in-scope row of the context matrix: at minimum public default, in-app admin with the current plan marked, in-app IC, and the plan summary, each with real copy. Per-tier headlines and CTA labels are the strings most likely to ship as placeholders

## Next step

After the spec:
```
---
→ Next step: improve-conversion-surfaces-copy — write the per-tier headlines, CTA labels and plan-summary lines from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

After the wireframe (built once copy exists):
```
---
→ Next step: monetization-design-reviewer — score the pricing page spec, copy, and wireframe together
→ Prompt: "Review .monetization/{feature-slug}/"
```
