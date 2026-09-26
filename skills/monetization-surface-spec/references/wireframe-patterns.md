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
