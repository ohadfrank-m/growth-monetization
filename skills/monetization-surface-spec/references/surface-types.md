# Surface type reference index

Quick-reference for all 7 monetization surface types. Each entry names mandatory spec sections, the primary user cohort, and the key design constraint.

Detailed patterns and wireframes: [wireframe-patterns.md](wireframe-patterns.md)
Copy angles: [copy-hooks.md](copy-hooks.md)
monday.com specific context: [monday-context.md](../../../context/monday-context.md)

---

## 1. Pricing page

**When:** Public or in-app plan comparison
**Cohort:** Both (new and existing)
**Primary conversion:** Plan selection / upgrade initiation
**Key constraint:** Value clarity — each tier must name a job-to-be-done, not a feature list

**Mandatory spec sections:**
- Plan structure table (all tiers)
- Annual/monthly toggle behaviour
- Highlighted / recommended tier logic
- Feature comparison (collapsed by default)
- AI credits/usage shown per tier (if applicable)
- CTA per tier (not all "Upgrade")
- Mobile: how the column layout collapses

**Critical anti-pattern:** Showing credits as bare numbers ("500 AI credits/month") — always add task translation.

---

## 2. Paywall / feature gate

**When:** User tries to access a locked feature
**Cohort:** New users (trial) or existing users blocked by tier
**Primary conversion:** Tier upgrade or trial-to-paid
**Key constraint:** Show value before the ask — never gate without a preview

**Mandatory spec sections:**
- Feature preview (what the user sees behind/before the gate)
- Gate trigger (exact condition)
- Value proof (3 concrete use cases or social proof)
- Primary CTA (benefit-led, names the feature or outcome)
- Secondary action (learn more, see plan details)
- Dismiss logic and frequency cap

**Critical anti-pattern:** Full blocking modal with no feature preview.

---

## 3. Promotion

**When:** Discount, limited-time offer, upsell banner/modal
**Cohort:** Both (different angles)
**Primary conversion:** Upgrade during the promotional window
**Key constraint:** Urgency must be real — fake countdowns destroy trust

**Mandatory spec sections:**
- Discount amount + anchor (what it's normally priced at)
- Expiry (date or time remaining — must be accurate)
- Eligibility (who sees this? new users, lapsed, specific tier?)
- Dismiss and frequency cap
- Post-promo state (what happens after the offer expires)

**Critical anti-pattern:** Discount shown with no expiry or fake urgency countdown.

---

## 4. Tier upgrade trigger

**When:** Usage limit hit, seat expansion needed, plan upgrade nudge at specific moment
**Cohort:** Existing users
**Primary conversion:** Plan upgrade or seat expansion
**Key constraint:** Name the specific limit and consequence — "you've hit a limit" without context converts poorly

**Mandatory spec sections:**
- Trigger condition (exact limit, exact moment)
- Current usage context (usage bar, seats used, etc.)
- What changes at the next tier (specific, not "more features")
- CTA naming the capability gained, not the plan
- Dismiss and frequency cap

**Critical anti-pattern:** Generic "you've hit your limit" without showing what the limit was or what changes.

---

## 5. Credit / consumption UI

**When:** Running low on credits, credit meter, metering dashboard, top-up flow
**Cohort:** Existing users
**Primary conversion:** Credit top-up
**Key constraint:** Task continuity — never let the user lose work without a resume path

See full reference: [credit-ui.md](credit-ui.md)

---

## 6. Cancellation flow

**When:** User initiates cancel or downgrade
**Cohort:** Existing users (retention)
**Primary conversion:** Retain user at current or lower tier (downgrade > cancel)
**Key constraint:** Don't trap — friction is legal risk and brand damage; acknowledge the choice

**Mandatory spec sections:**
- Value surface (what they've done/built — personalised if possible)
- Alternatives to cancelling (pause, downgrade, CSM contact for Enterprise)
- Cancellation confirmation (if they continue: frictionless, no dark patterns)
- Post-cancellation state (what happens to their data and access)
- Win-back path (optional: what re-activation looks like)

**Critical anti-pattern:** Hiding the cancel button, guilt-trip copy, no downgrade option offered.

---

## 7. Trial flow

**When:** Trial start (onboarding), mid-trial nudge, trial expiry
**Cohort:** New users
**Primary conversion:** Trial to paid (full upgrade or self-serve)
**Key constraint:** Show aha moment before asking for payment — ask too early = conversion tanks

**Mandatory spec sections (vary by trigger):**

*Trial start / activation nudge:*
- Activation action to drive (what's the aha moment?)
- Trigger timing (when does this nudge fire?)
- Non-blocking vs. blocking (day 1: never block)

*Mid-trial nudge:*
- Usage context (what they've done so far)
- Feature gap (what they haven't tried that would unlock value)
- Progress toward aha moment

*Trial expiry:*
- Personalised loss list (what they built — automations, team members, etc.)
- Explicit downgrade option (what they keep on Free)
- CTA: "Continue with Pro" vs "Switch to Free"
- Expiry timing options (extend if usage is high but no upgrade?)

**Critical anti-pattern:** Asking for payment before aha moment, no explicit downgrade option at expiry.
