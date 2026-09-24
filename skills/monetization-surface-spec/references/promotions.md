# Promotion — spec reference

Surface type 3: discount, limited-time offer, upsell banner or modal.

## When it appears
- Campaign windows (seasonal, launch, end of quarter)
- Lifecycle moments (trial expiry, pre-renewal, lapsed account)
- Targeted offers by segment or behaviour

## Mandatory spec sections
- **Offer:** discount amount, what it applies to (seats, credits, first N months), and the anchor price
- **Eligibility:** exact audience rules (tier, tenure, region, prior offer exposure)
- **Expiry:** real deadline and how it's displayed; what happens after it passes
- **Stacking rules:** does it combine with other discounts, nonprofit pricing, annual savings?
- **Placement:** banner, modal, email, pricing page badge
- **Dismiss and frequency cap**
- **Measurement:** holdout group, incrementality metric (not just redemption rate)

## Anti-patterns specific to promotions
- Fake countdown timers or deadlines that reset
- Discount with no anchor to the original price
- Offer shown to users who already converted without it
- No holdout, so lift can't be measured

## Copy hook
Primary reason: save money; secondary: alleviate fear of missing out. See [copy-hooks.md](copy-hooks.md#promotion-surface-3).
