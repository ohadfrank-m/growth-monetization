# Pricing page — spec reference

Surface type 1: public or in-app plan comparison.

## When it appears
- Direct navigation to the pricing page
- In-app "See plans" / "Compare plans" entry points
- Redirect from a paywall or upgrade trigger ("See all Pro features")

## Mandatory spec sections (in addition to the surface-spec template)
- **Plan structure table:** every tier, annual and monthly price, seat minimum, AI credit inclusion. Pull current values from [monday-context.md](../../../context/monday-context.md). Never hardcode prices in the spec without citing the context file's `last-updated` date.
- **Billing toggle:** default state (annual), savings label, what changes on toggle
- **Recommended tier logic:** which tier is highlighted, and why (static vs. personalised by traffic source or account state)
- **Per-tier headline:** one job-to-be-done per tier, not a feature list
- **AI credits presentation:** how credit amounts are shown per tier, with task translation
- **Seat selector:** how seat bundles and the 3-seat minimum are communicated
- **Feature comparison:** collapsed by default; which 5–7 rows stay visible
- **CTA per tier:** each tier has its own label ("Start free", "Try Pro", "Contact sales")
- **Mobile:** how columns collapse (stacked cards vs. swipeable)

## Patterns
See [wireframe-patterns.md](wireframe-patterns.md) — Pricing page, Pattern A and B.

## Anti-patterns specific to pricing pages
- Credit amounts shown without task translation
- Seat minimum hidden until checkout (users feel tricked)
- All tiers with identical "Get started" CTAs
- Feature table fully expanded above the fold

## Copy hook
Primary reason: make money / save time. See [copy-hooks.md](copy-hooks.md#pricing-page-surface-1).
