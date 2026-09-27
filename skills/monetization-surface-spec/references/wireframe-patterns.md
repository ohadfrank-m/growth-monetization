# Wireframe patterns and best-in-class examples

Reference for structural patterns when building wireframes. The **wireframe contract** in [../SKILL.md](../SKILL.md) (states by URL hash, flow strip, pin conventions, mobile rules) takes precedence over anything here; this file adds per-surface layouts and the annotation-panel markup. Pull inspiration here before building — these patterns represent battle-tested approaches from leading SaaS tools.

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

## Promotion (surface 3)

### Pattern A: In-app promo banner or modal (real anchor, real end date)
```
[Banner, top of workspace — or a modal for a high-value offer, once per campaign:]
  [Offer line: "{plan} for {N}% less — until {end_date}"]
  [Anchor: ~~${list_price}/seat/mo~~  ${offer_price}/seat/mo · billed {cadence}]
  [Terms: "For {duration} on {what it applies to}. Then ${list_price}/seat/mo."]
  [Ends: "Offer ends {end_date}, {end_time} {timezone}" — a fixed date; no timer that restarts]
  [CTA: "{benefit-led action}"]   [Link: "Offer terms"]   [Dismiss ×]
  [IC variant: CTA → "Share with {admin}"; prices stay visible]
```

**States:**
- Live: offer line, anchor, terms, end date
- Final window: same layout, the end-date line promoted above the offer line
- Expired (old link or cached view): regular price plus one line, "This offer ended {end_date}"
- Holdout: no banner at all

**Why it works:** The genuine list price sits beside the offer price, so the saving is visible and checkable. The end date is fixed, so the urgency is real and survives a reload. The terms line says what the user pays after the offer, which heads off bill shock at renewal.

**Apply when:** An in-product offer the user didn't ask for: campaign, lifecycle moment, launch window. Use the modal only for a high-value, one-time offer, and never over an active task.

### Pattern B: Discount applied at plan summary / checkout
```
[Plan summary:]
  [Plan: {plan} · {seats} seats · billed {cadence}]
  [{plan}, {seats} seats ....................................... ${list_total}]
  [{offer_name} — {N}% off for {duration} ....................... −${discount}]
  [Unused time on {current_plan} (mid-cycle change only) ........ −${credit}]
  [Tax: {tax_line}]
  [Total today .................................................. ${total_today}]
  [Next bill: ${next_bill} on {next_bill_date}  ·  From {discount_end_date}: ${list_total}/{period}]
  ["Have a code?" — collapsed link, only if codes are in scope]
     [Code field → valid: discount line appears · invalid / expired / not eligible: one-line reason, price unchanged]
  [CTA: "{confirm action} — ${total_today}"]   [Back]
```

**States:**
- Auto-applied: the discount line is present on load
- Code entered: valid / invalid / expired / not eligible / already used
- No offer: the discount line is absent (no "$0 off" line)
- Payment failed: inline reason plus retry; the discount stays applied

**Why it works:** Every number that decides the charge is on one screen: list price, discount, proration credit, tax, total today, and the price after the offer ends. The user never discovers the post-promo price on the first full invoice. Keeping the code field collapsed stops users without a code from leaving to go and find one.

**Apply when:** The user is already choosing a plan, or arrived with a promo link or code. Also the default layout for any plan summary, with or without a discount.

---

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
  [Bundle selector: next bundle {N} seats — seats sell in bundles, not one at a time (monday-context.md)]
  [Price: "{bundle_total}/month for {N} seats (+{delta} vs today) — billed {monthly/annually}"]
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
  [Label: "600 credits remaining — ≈ {N} {task} at your pace"]
  [Small: "Resets {billing-cycle date}" or "Add credits anytime"]
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
[Small: "Your work is saved" — only once state preservation ships; not native today (see monday-context.md)]
```

**Critical elements:** Names the agent, names the step, reassures state is saved, single top-up CTA with price visible, admin path.

### Pattern C: Top-up modal
```
[Modal:]
  [Headline: "Top up AI credits"]
  [Current balance: "0 credits remaining"]
  [Package options:]
    ○ {bucket} credits/mo — ${price}/mo  (≈ {N} {task})
    ● {next bucket} credits/mo — ${price}/mo  (≈ {N} {task})  [RECOMMENDED badge]
    ○ {bucket+2} credits/mo — ${price}/mo  (≈ {N} {task})
  [Buckets and prices from monday-context.md; today a top-up moves the account to a larger monthly bucket — one-time packs aren't published]
  [Selected package summary: "2,000 credits for $X — billed monthly, cancel anytime"]
  [CTA: "Top up and resume"]  [Dismiss: "Notify my admin instead"]
```

**Critical elements:** Three package options (anchors mid-tier choice), task translation on every option, "resume" in the CTA, admin path as secondary.

---

## Cancellation flow (surface 6)

### Pattern A: Reason → one matched offer → confirm (multi-step)
```
[Step indicator: 1 Reason · 2 Your options · 3 Confirm]        [Every step: "Continue to cancel →"]

[Screen 1 — Reason:]
  [Header: acknowledges the decision — no guilt]
  [Notice line, only if the contract has one: "Renews {renewal_date} · notice deadline {notice_date}"]
  [Value recap: {N} boards · {N} automations · {N} agent runs this {period}]
  [One question, single-select: {reason_1} … {reason_n} · Other (optional free text)]
  [CTA: "Continue"]   [Link: "Keep my plan"]

[Screen 2 — One offer, matched to the reason (skipped when the map says "none"):]
  [Offer card: {offer} — {what changes} · from {effective_date} · {price_delta}]
  [CTA: "{accept offer}"]   [Same-weight link: "No thanks, continue to cancel"]

[Screen 3 — Confirm:]
  [Plan ends {end_date}. You won't be charged again.]
  [Data: "{retention rule}"  · [Export data]]
  [Way back: "Change your mind before {end_date} — reactivate in one click"]
  [CTA: "Cancel plan"]   [Link: "Keep my plan"]

[After confirm — in-app banner until {end_date}:]
  ["{plan} ends {end_date}" · [Reactivate]]
```

**States:**
- Reason (1), offer (2), confirm (3), offer accepted (confirmation of what changed plus undo), after-state banner
- Routing screen instead of step 1: non-admin (request to admin) or sales-assisted (account team, date, contact)
- Error: the cancel didn't save; inline reason plus retry

**Why it works:** One question and one offer that fits the answer, with the way out on every screen. The flow asks without trapping. A notice deadline shown before the offer stops the offer from reading as a way to dodge a renewal. The confirm screen answers the three questions people cancel with: when it ends, what happens to the data, and how to come back.

**Apply when:** A self-serve admin cancels. The number of offers is fixed at one; the reasons and the reason → offer map come from the spec.

### Pattern B: Downgrade confirmation with loss list (keep / lose / when)
```
[Modal or page — "Move to {lower_plan}":]
  [When: "Changes on {effective_date}. Until then you keep everything in {current_plan}."]
  [You keep — listed first:]
    ✓ {kept_item}
    ✓ {kept_item}
  [What changes — from this account's usage, most-used first:]
    ✕ {feature} — used on {N} boards → {read-only | switched off, not deleted | removed} on {effective_date}
    ✕ {feature} — {N} runs this month → {what happens}
  [Irreversible — only if any exist:]
    ⚠ "{item} is deleted on {effective_date} and can't be restored on re-upgrade"  [Export]
  [Price: ${current_price}/mo → ${new_price}/mo from {effective_date} · billed {cadence}]
  [Precondition — only for seat reductions: "Deactivate {N} users first" → link to user management]
  [CTA: "Schedule the change"]   [Secondary: "Keep {current_plan}"]
  [Small: "Undo anytime before {effective_date}"]
```

**States:**
- Default: keep list, loss list, price
- Irreversible loss present: warning row plus export beside it
- Precondition unmet: CTA disabled, precondition line first
- Scheduled: confirmation with the effective date and undo

**Why it works:** The keep list comes first, so the lower plan reads as a place to land rather than a punishment. The loss list uses the account's own usage, so it's specific and nothing is invented. Irreversible loss sits before the confirm button, where consent can still be given, and the effective date answers "when".

**Apply when:** Downgrading to a lower tier or Free, reducing seats, or moving to a smaller credit package. Also the landing screen when a right-size offer is accepted in Pattern A.

---

---

## Trial flow (surface 7)

### Pattern A: Trial expiry modal (final day)
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

### Pattern B: Mid-trial activation nudge (Proof phase — see playbooks/trial-flows.md)
```
[Non-blocking banner at top of workspace:]
"You have {N} days left in your Pro trial — [Set up your first AI agent →]"
[Dismiss ×]
```

**Apply when:** User hasn't activated key feature yet. Drive aha moment before asking for payment.

---

## Wireframe delivery format

Always deliver wireframes as single-file HTML:
- Low-fi — neutral greys, real copy, clear structure
- All states shown (if multi-state surface): use tabs or stacked sections
- Mobile note in the annotation panel header: "Mobile: {what stacks or collapses}"

File: `.monetization/{feature-slug}/03-wireframe.html` — built after `02-copy.md` exists, using its recommended copy verbatim

Reference the pattern used in the wireframe's opening comment:
```html
<!-- Pattern: {pattern name} — adapted for monday.com credit depletion, existing-user cohort -->
```

---

## Annotation panel — mandatory pattern

**Never place annotation badges inline in the wireframe body.** Inline badges interrupt the visual hierarchy and make the wireframe unreadable as a design artifact. Annotations belong in a separate panel; callout markers on wireframe elements are small and non-disruptive.

### Layout

```
┌─────────────────────────────────────────────┬──────────────────────┐
│                                             │  Annotations    [×]  │
│           Wireframe body                    │  ─────────────────── │
│           (full readable width)             │  C1  Copy note       │
│           [1] [2] small callout markers     │  D1  Design note     │
│           anchored to elements              │  O1  Open item       │
│                                             │                      │
└─────────────────────────────────────────────┴──────────────────────┘
```

- Panel is **fixed on the right**, 300px wide, full viewport height, independently scrollable
- A **"Annotations" toggle button** (top-right corner of page) collapses/expands the panel; when collapsed, wireframe fills the full width
- Wireframe body has `margin-right: 316px` when panel is open; `margin-right: 0` when closed

### Callout markers on wireframe elements

Small circular markers (24px diameter) sit **outside the text flow** — positioned absolutely relative to their nearest `position: relative` ancestor, or floated to the far right of their container. They don't push other content around.

```html
<!-- Correct: marker floated right, doesn't interrupt copy -->
<div class="wf-element" style="position: relative;">
  <span class="callout callout-copy" data-id="C1">C1</span>
  <h1>Don't lose what you built</h1>
</div>

<!-- Wrong: badge rendered as a block inside the text flow -->
<div class="badge copy-badge">C1 — Replaces "Choose the right plan"...</div>
<h1>Don't lose what you built</h1>
```

### CSS for callouts and panel

```css
/* Callout marker — anchored to element, doesn't affect layout */
.callout {
  position: absolute;
  top: 4px;
  right: -32px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  font-size: 10px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: default;
  z-index: 10;
  color: #fff;
}
.callout-copy    { background: #2563eb; }   /* C# — blue */
.callout-design  { background: #16a34a; }   /* D# — green */
.callout-open    { background: transparent; color: #d97706; border: 2px dashed #d97706; }   /* O# — dashed: blocked on an open item */
.callout-touch   { background: #7c3aed; }   /* T# — friction touchpoint from the flow map */

/* Annotation panel */
#annotation-panel {
  position: fixed;
  top: 0; right: 0;
  width: 300px;
  height: 100vh;
  background: #f8fafc;
  border-left: 1px solid #e2e8f0;
  overflow-y: auto;
  padding: 16px;
  font-size: 13px;
  z-index: 100;
}

/* Annotation entry */
.ann-entry {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  padding: 8px 0;
  border-bottom: 1px solid #e2e8f0;
}
.ann-badge {
  flex-shrink: 0;
  width: 28px;
  height: 20px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
}
.ann-copy    { background: #2563eb; }
.ann-design  { background: #16a34a; }
.ann-open    { background: #d97706; }
.ann-text    { color: #334155; line-height: 1.4; }
```

### HTML structure

```html
<!-- Toggle button — always visible -->
<button id="ann-toggle" onclick="togglePanel()" 
  style="position:fixed; top:12px; right:12px; z-index:200; 
         background:#1e293b; color:#fff; border:none; border-radius:6px; 
         padding:6px 12px; font-size:12px; cursor:pointer;">
  Annotations
</button>

<!-- Annotation panel -->
<div id="annotation-panel">
  <div style="font-weight:700; font-size:13px; color:#0f172a; margin-bottom:12px; padding-bottom:8px; border-bottom:2px solid #e2e8f0;">
    Annotations
    <div style="font-size:11px; font-weight:400; color:#64748b; margin-top:2px;">
      Mobile: [describe what stacks or collapses]
    </div>
  </div>

  <!-- Legend -->
  <div style="display:flex; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
    <span style="font-size:11px; color:#2563eb;">● C# copy</span>
    <span style="font-size:11px; color:#16a34a;">● D# design</span>
    <span style="font-size:11px; color:#d97706;">● O# open</span>
  </div>

  <!-- Entries — one per annotation -->
  <div class="ann-entry">
    <span class="ann-badge ann-copy">C1</span>
    <span class="ann-text">Replaces "Choose the right plan" — escape pain/guilt framing</span>
  </div>
  <div class="ann-entry">
    <span class="ann-badge ann-design">D1</span>
    <span class="ann-text">Moved above price (was below CTA)</span>
  </div>
  <div class="ann-entry">
    <span class="ann-badge ann-open">O1</span>
    <span class="ann-text">BLOCKED: AI Actions translation string — awaiting final wording from copy</span>
  </div>
</div>

<script>
function togglePanel() {
  const panel = document.getElementById('annotation-panel');
  const body  = document.getElementById('wireframe-body');
  const btn   = document.getElementById('ann-toggle');
  const open  = panel.style.display !== 'none';
  panel.style.display = open ? 'none' : 'block';
  body.style.marginRight = open ? '0' : '316px';
  btn.textContent = open ? 'Annotations' : 'Hide annotations';
}
</script>
```

### Open items — two-state prototype control

When an open item has two possible answers (e.g. whether a price line includes credits), show both states with a toggle rather than picking one:

```html
<div class="open-toggle" style="border:2px dashed #d97706; border-radius:6px; padding:8px 12px;">
  <div style="font-size:11px; color:#d97706; margin-bottom:6px;">O1 — open: awaiting decision</div>
  <div id="ot1-a" class="ot-state">State A: $19/seat/month</div>
  <div id="ot1-b" class="ot-state" style="display:none">State B: $19/seat/month (includes 2,000 AI credits)</div>
  <button onclick="toggleOT('ot1')" style="font-size:11px; margin-top:6px; cursor:pointer;">Toggle state</button>
</div>
<script>
function toggleOT(id) {
  const a = document.getElementById(id+'-a');
  const b = document.getElementById(id+'-b');
  a.style.display = a.style.display === 'none' ? '' : 'none';
  b.style.display = b.style.display === 'none' ? '' : 'none';
}
</script>
```
