# Wireframe patterns and best-in-class examples

Reference for structural patterns when building wireframes. Pull inspiration here before building — these patterns represent battle-tested approaches from leading SaaS tools.

---

## How to use this file

1. Identify the surface type
2. Find the relevant section below
3. Pick the pattern that best fits the brief
4. Reference it in the spec's References section (one sentence on why it applies)
5. Adapt — don't copy directly, apply the structural insight to the monday.com context

---

## Wireframe principles (apply to all surfaces)

**Hierarchy:** The single most important element gets the most visual weight. One hero action, everything else secondary.

**Escape hatch:** Always present, never hidden. Users who can't dismiss trust the product less.

**Task continuity:** If the surface interrupts a task, the surface must reference that task. Users forgive interruption when it's contextual.

**Mobile-first consideration:** Design for the narrowest case first. State which elements stack or collapse.

**Progress indicators:** When a flow has more than one step, show progress. Never strand users in an unknown-length flow.

---

## Pricing page (surface 1)

### Pattern A: Three-column plan comparison (most common)
```
[Header: "Choose your plan" — value-led, not feature-led]

[Toggle: Monthly / Annual — annual pre-selected, show savings]

[Column 1: Free]    [Column 2: Pro — HIGHLIGHTED]    [Column 3: Enterprise]
[Price]             [Price + "Most popular"]           ["Custom pricing"]
[Key feature 1]     [Key feature 1 ✓]                 [Key feature 1 ✓]
[—]                 [Key feature 2 ✓]                 [Key feature 2 ✓]
[CTA: "Get free"]   [CTA: "Start Pro"]                [CTA: "Contact sales"]

[Feature comparison table — collapsed by default, expandable]
```

**Why it works:** Visual attention lands on the highlighted tier. Annual toggle creates immediate anchoring. Comparison table collapsed keeps the page light but accessible.

**Apply when:** Full pricing page, multiple tiers to compare.

### Pattern B: Inline upgrade banner (minimal disruption)
```
[Current plan pill: "Pro plan"]
[Banner: "{Feature} is available on Business — [Upgrade] [Learn more]"]
```

**Apply when:** Upsell within the product, not a dedicated pricing page.

---

## Paywall / feature gate (surface 2)

### Pattern A: Feature preview + gate (Notion style)
```
[Blurred/dimmed feature preview behind modal]
[Modal overlay:]
  [Feature name + icon]
  [1-sentence what it does — outcome, not mechanism]
  [3 bullet proof points — concrete use cases]
  [CTA: "Unlock {feature name}"]  [Secondary: "See all Pro features"]
  [Small: "Already on Pro? Sign in"]
```

**Why it works:** User sees the feature before the ask. Preview anchors the value of the CTA.

### Pattern B: Contextual inline gate (Linear style)
```
[Feature area — partially shown]
[Inline banner at top of feature area:]
  [Lock icon] "{Feature} is a Pro feature — [Start Pro trial] or [See what's included]"
[Rest of feature area: grayed out, not removed]
```

**Why it works:** Not blocking. User can still see other things. Gate is contextual, not a full interrupt.

**Apply when:** Feature lives in a workspace the user already uses. Full modal is too disruptive.

---

## Tier upgrade trigger (surface 4)

### Pattern A: Usage limit reached — inline
```
[Usage bar: ████████░░ 8/10 automations]
[Inline notification below bar:]
  "You've used 8 of your 10 monthly automations."
  "Upgrade to Pro for unlimited automations."
  [CTA: "Upgrade to Pro"]  [Link: "See what Pro includes"]
```

**Why it works:** Usage bar makes the limit visible and concrete. Limit + consequence + action in one view.

### Pattern B: Seat expansion modal
```
[Modal:]
  [Headline: "Add more team members"]
  [Current: "You have {N} seats — {N} are used"]
  [Seat selector: [−] 3 [+] additional seats]
  [Price: "+$X/month — billed {monthly/annually}"]
  [CTA: "Add seats"]  [Dismiss: "Not now"]
```

**Apply when:** User tries to invite someone when at seat limit. Offer the expansion in the moment.

---

## Credit / consumption UI (surface 5)

### Pattern A: Persistent credit meter (sidebar)
```
[Sidebar section:]
  [Icon] AI Credits
  [Progress bar: ██████░░░░ 60%]
  [Label: "600 credits remaining — ≈ 600 AI actions"]
  [Small: "Resets {date}" or "Top up anytime"]
  [Link: "Top up"]
```

**States:**
- Healthy (>50%): bar blue/green, no urgency
- Warning (20-50%): bar amber, "Running low"
- Critical (<20%): bar red, "Top up soon"
- Depleted (0%): bar empty, "Out of credits — [Top up to continue]"

### Pattern B: Depletion inline banner (mid-task)
```
[Inline banner in agent run interface:]
[⚠️] "Your AI agent has paused — you're out of credits"
[Subtext: "{Agent name} stopped at step {N}. Top up to continue where you left off."]
[CTA: "Top up credits — {package size} for ${price}"]  [Secondary: "Notify admin"]
[Small: "Your work is saved"]
```

**Critical elements:** Names the agent, names the step, reassures state is saved, single top-up CTA with price visible, admin path.

### Pattern C: Top-up modal
```
[Modal:]
  [Headline: "Top up AI credits"]
  [Current balance: "0 credits remaining"]
  [Package options:]
    ○ 500 credits — $X/mo  (≈ 500 AI actions)
    ● 2,000 credits — $X/mo  (≈ 2,000 AI actions)  [BEST VALUE badge]
    ○ 5,000 credits — $X/mo  (≈ 5,000 AI actions)
  [Selected package summary: "2,000 credits for $X — billed monthly, cancel anytime"]
  [CTA: "Top up and resume"]  [Dismiss: "Notify my admin instead"]
```

**Critical elements:** Three package options (anchors mid-tier choice), task translation on every option, "resume" in the CTA, admin path as secondary.

---

## Trial flow (surface 7)

### Pattern A: Trial expiry modal (day 7)
```
[Modal:]
  [Headline: "Your trial ends in 2 days"]
  [Subheadline: "Keep everything you've set up"]
  [3 items they built — personalised if possible:]
    ✓ {N} automations created
    ✓ {N} team members added
    ✓ {N} AI agent runs completed
  [Plan comparison: Free (what they lose) vs Pro (what they keep)]
  [CTA: "Continue with Pro — ${price}/month"]
  [Secondary: "Switch to Free plan — I'll lose these features"]
```

**Why it works:** Personalised loss list anchors the value they'll lose. Secondary CTA makes downgrade explicit — users don't feel trapped.

### Pattern B: Mid-trial activation nudge (day 3)
```
[Non-blocking banner at top of workspace:]
"You have {N} days left in your Pro trial — [Set up your first AI agent →]"
[Dismiss ×]
```

**Apply when:** User hasn't activated key feature yet. Drive aha moment before asking for payment.

---

## Wireframe delivery format

Always deliver wireframes as single-file HTML:
- Low-fi — grey boxes, placeholder text, clear labels
- All states shown (if multi-state surface): use tabs or stacked sections
- Annotated: small labels explaining each element's purpose
- Mobile note at top: "Mobile: {what stacks or collapses}"

File: `.monetization/{feature-slug}/03-wireframe.html` — built after `02-copy.md` exists, using its recommended copy in place of any placeholder text below

Reference the pattern used in the wireframe's opening comment:
```html
<!-- Pattern: {pattern name} — adapted for monday.com credit depletion, existing-user cohort -->
```
