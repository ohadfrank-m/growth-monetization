# Scoring Rubric — Anchors & Weighting

Read this for **every** review, with [calibration-examples.md](calibration-examples.md) when a score is borderline. It exists so that two different reviewers scoring the same design land in the same place. Score against the anchor definitions below — not intuition.

---

## How to score

1. Score each of the 8 dimensions **1–5** using the anchor tables.
2. Look up the **weight** for the surface type you're reviewing.
3. Multiply each dimension score by its weight, sum, and normalize to **/100**.
4. A dimension that genuinely doesn't apply (rare) is excluded and the weights renormalized — state when you do this.

Only 1, 3, and 5 are defined per dimension. A **2** is "closer to 1 than 3"; a **4** is "closer to 5 than 3." Never leave a score unanchored.

---

## Dimension anchors

### Value clarity — *does the user immediately understand what they get?*
- **1** — No clear value; user can't tell what they'd gain or why. Feature names only, no outcome.
- **3** — Value is stated but generic ("more power", "advanced features"); requires effort to grasp the benefit.
- **5** — The specific outcome is obvious in <3 seconds; benefit is concrete and tied to the user's job.

### Timing / trigger logic — *is this shown at the right moment?*
- **1** — Wrong moment: pre-aha, mid-unrelated-task, or interrupts an agent's flow; recurs after dismiss.
- **3** — Acceptable moment but not optimal; reactive (fires at 100% limit) rather than proactive.
- **5** — Fires at peak intent (just after an activation milestone, or proactively before the limit — the thresholds in the surface's playbook, e.g. 80/90% for tier limits in `playbooks/upgrade-triggers.md`, 80/95% used for credits in `playbooks/credit-ui.md`); respects dismiss + frequency caps; non-blocking in agentic contexts.

### Copy quality — *benefit-led headline, specific CTA?*
- **1** — Headline is a label ("Upgrade to Pro"); CTA is generic ("Upgrade", "Subscribe"); no anchoring.
- **3** — Headline hints at benefit; CTA is semi-specific; some anchoring but incomplete.
- **5** — Headline names the outcome; CTA names what's unlocked ("Unlock AI Agents"); price anchored with savings shown.

### Friction & flow — *how many steps to convert; any needless friction?*
- **1** — Multiple avoidable steps; re-entry of payment; confusing branch logic; dead ends.
- **3** — Reasonable but has 1–2 removable steps or a moment of hesitation.
- **5** — Minimal steps to yes; one-click where possible; state preserved; no re-entry of known info.

### Trust signals — *social proof, guarantees, risk reducers?*
- **1** — None present where they'd clearly help (e.g. a high-commitment upgrade with no reassurance).
- **3** — Some present but generic or poorly placed ("50,000+ teams" floating with no relevance).
- **5** — Relevant, well-placed proof or risk-reducer (guarantee, contextual usage proof, every material term on the commit screen) near the CTA.

### Escape hatch quality — *is the "no" path clear and non-manipulative?*
- **1** — Hidden/tiny close, guilt copy, or a maze; dark-pattern territory.
- **3** — Escape exists but is de-emphasized more than necessary, or slightly buried.
- **5** — "No" path is visible, honest, one action; declining is respected and easy.

### Visual hierarchy — *does the eye go to the right place first?*
- **1** — Competing focal points; primary CTA doesn't win; key value buried.
- **3** — Generally readable but the eye path isn't fully intentional; secondary elements over-weighted.
- **5** — Scannable, front-loaded layout that passes the squint test; primary CTA and core value dominate; supporting info recedes. (For monday: Vibe tokens used, no hardcoded values.)

### Mobile readiness — *would this work at 375px, and reflow at 320 CSS px?*
- **1** — Breaks, truncates, or hides the CTA on mobile; horizontal scroll; tap targets under 24×24 CSS px (WCAG 2.5.8).
- **3** — Works but cramped; some reflow awkwardness; comparison tables hard to scan.
- **5** — Fully responsive; CTA reachable; content re-prioritized sensibly for small screens.

---

## Anchor sources

A 5 must meet every criterion listed for its dimension. Missing one caps the score at 4; missing a ★ criterion caps it at 2. Criteria cite usability guidelines (NN/g, Baymard), accessibility standards (WCAG 2.2 AA) and consumer-protection texts. Legal items are design guidance; reviewed by legal: not yet. CRO thresholds (credit, tier and trial timing) are owned by the playbooks and cited, not restated.

### Value clarity

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| V1 | The headline or first line names the user's outcome, readable with no interaction. A plan name, or "AI-powered"/"Powered by AI" alone, fails. | NN/g, Nielsen 2011: communicate the value proposition within 10 seconds ([link](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/)). NN/g, Samsonov 2025: "AI is a technology, not a user benefit" ([link](https://www.nngroup.com/articles/powered-by-ai-is-not-a-value-proposition/)) | [Verified] · mixed |
| V2 ★ | No unit stands between the user and the real cost. Any credit or usage unit shows a task translation **and** the money price of the package. | FTC 2022 staff report, p. 23, names "Intermediate Currency" as a dark pattern ([PDF](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf)). deceptive.design "Currency confusion" ([link](https://www.deceptive.design/types)). The translation rule itself is owned by `playbooks/credit-ui.md` | [Verified] · legal / mixed |
| V3 | The total cost appears before the commit step: seat minimums, fees, the price after a promo or trial. | Baymard: 12% of US shoppers abandoned because they couldn't see the total cost upfront, 40% over extra costs ([link](https://baymard.com/lists/cart-abandonment-rate)). FTC 2022, pp. 8–9 (drip pricing) | [Verified] · consumer (directional for B2B) / legal |
| V4 | Where options are compared (pricing page, downgrade target): at most 5 options, the same attributes for each, differences easy to spot. | NN/g, Moran & Dykes 2024, comparison tables ([link](https://www.nngroup.com/articles/comparison-tables/)) | [Verified] · mixed |

### Timing / trigger logic

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| T1 ★ | No monetization modal before first meaningful engagement, right after login, or during a critical task. | NN/g, Kaley 2019, popup trends 1–5 ([link](https://www.nngroup.com/articles/popups/)). NN/g, Fessenden 2017: avoid modals in high-stakes processes ([link](https://www.nngroup.com/articles/modal-nonmodal-dialog/)) | [Verified] · mixed |
| T2 ★ | Once declined, the prompt is not re-shown in the same session. Either a frequency cap is specified, or a permanent "No" is offered next to "Not now". | FTC 2022, p. 24, "Nagging". EU DSA Art. 25(3)(b), repeatedly requesting a choice already made ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2065)) | [Verified] · legal |
| T3 | Proactive: fires at the playbook threshold, before the limit. | Credit thresholds: `playbooks/credit-ui.md`. Tier/seat: `playbooks/upgrade-triggers.md`. Trial phases: `playbooks/trial-flows.md` | per playbook |
| T4 | Inside a running task (an agent run, a board edit), the prompt is inline and non-blocking, or waits for a task boundary. | Hirsch et al., *Frontiers in Psychology* (doi 10.3389/fpsyg.2024.1465323): interruptions within a task chunk were costlier to resume than at chunk boundaries ([link](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1465323/full)) | [Verified] · lab study, directional |

### Copy quality

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| C1 | The primary CTA states the specific action or outcome. Bare "Get started", "Upgrade" and "Continue" fail. | NN/g, Harley & Flaherty 2017, "Get Started" stops users ([link](https://www.nngroup.com/articles/get-started/)). Baymard 2021: labels must say what will happen ([link](https://baymard.com/blog/button-design)) | [Verified] · mixed |
| C2 ★ | Decline copy is neutral: no confirmshaming, no guilt. | NN/g, Moran & Flaherty 2017 ([link](https://www.nngroup.com/articles/shaming-users/)). FTC 2022, p. 25, "Confirm Shaming". Mathur et al. 2019, Misdirection category ([link](https://arxiv.org/abs/1907.07032)) | [Verified] · mixed / legal |
| C3 | Confirmation buttons name the consequence ("Downgrade to {plan} on {date}" / "Keep {plan}"). Yes/No or "Are you sure?" fails. | NN/g, Nielsen 2018, confirmation dialogs ([link](https://www.nngroup.com/articles/confirmation-dialog/)) | [Verified] · mixed |
| C4 ★ | No trick wording: every label does what it says. A "Continue to cancel" that doesn't cancel, or a "No, cancel" that exits the cancel path, fails. | FTC 2022, p. 25, "Trick Questions". FTC v. Amazon complaint ¶128 ([PDF](https://www.ftc.gov/system/files/ftc_gov/pdf/amazon-rosca-public-redacted-complaint-to_be_filed.pdf)) | [Verified — allegations] · legal |
| C5 | Users' words, not internal jargon. An internal unit name shown with no explanation fails. | NN/g heuristic #2, match between system and real world ([link](https://www.nngroup.com/articles/ten-usability-heuristics/)) | [Verified] · mixed |

### Friction & flow

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| F1 ★ | Leaving is symmetric with joining: a cancel or downgrade takes no more steps than sign-up or upgrade did, in the same medium. | FTC 2022, p. 14: "at least as easy to use" as sign-up, same medium. DSA Art. 25(3)(c). California ARL via `playbooks/cancellation.md` Legal context | [Verified] · legal |
| F2 | Nothing already given in the same process has to be entered again. | WCAG 2.2 SC 3.3.7 Redundant Entry, Level A ([link](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html)) | [Verified] · standard |
| F3 | No forced registration and no fields the task doesn't need before the commit step. | Baymard: 18% abandon over forced account creation; ideal 7–8 fields vs 14.88 on average ([link](https://baymard.com/lists/cart-abandonment-rate)). FTC 2022, p. 24, "Forced Registration" | [Verified] · consumer (directional) |
| F4 | Every link inside a flow is labelled. Nothing throws the user out of the flow without warning. | FTC 2022, p. 13 (ABCmouse). FTC v. Amazon ¶127 | [Verified — allegations] · legal |
| F5 | Money and data commits can be undone, or have a review-and-confirm step. | WCAG 2.2 SC 3.3.4 Error Prevention (Legal, Financial, Data), AA ([link](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html)) | [Verified] · standard |

### Trust signals

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| R1 ★ | Every material term sits on the commit screen in body text: renewal, post-promo price, early-termination fee, seat minimum, credit expiry. Terms reachable only through a hover, pop-up or link fail. | FTC 2022, p. 14. FTC v. Adobe press release: fee disclosures in small print or behind hover icons ([link](https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling)) | [Verified — allegations] · legal |
| R2 | The reassurance (guarantee, security cue, relevant proof) sits right next to the CTA or payment fields. | Baymard: put badges near the encapsulated payment fields; 19% abandon from card distrust, 2025 data ([link](https://baymard.com/blog/perceived-security-of-payment-form)). `pricing-pages.md` anti-pattern "Social proof only at the bottom" | [Verified] · consumer (directional) |
| R3 ★ | Urgency, scarcity and social proof are real: no resetting timers, no activity messages of uncertain origin. | FTC 2022, p. 22, "Baseless Countdown Timer". Mathur et al. 2019, Urgency / Social Proof / Scarcity. deceptive.design, "Fake social proof", "Fake urgency" | [Verified] · legal / mixed |
| R4 | Claim words match the mechanics ("unlimited", "free"). | [case: cursor-2025-pricing](../../../playbooks/cases.md#cursor-2025-pricing) | [Verified] via playbook |

### Escape hatch quality

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| E1 | A modal or sheet has a visible close control in the tab order, the close target is ≥24×24 CSS px, and Esc closes it. | WCAG 2.2 SC 2.5.8 AA ([link](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)). WAI-ARIA APG modal dialog pattern ([link](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)) | [Verified] · standard |
| E2 ★ | No false hierarchy. The decline is a real control, not a pale link hidden under a bright button. Its text is ≥4.5:1 contrast and its boundary ≥3:1. | FTC 2022, p. 23, "False Hierarchy" (its example is a cancel flow). DSA Art. 25(3)(a). WCAG 1.4.3 ([link](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)) and 1.4.11 ([link](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)) | [Verified] · legal / standard |
| E3 ★ | Cancel or downgrade is reachable online, in **≤3 clicks from account settings to the final confirm**, and every save screen shows the continue option beside the offer. | FTC v. Amazon ¶¶114, 140, 142: six clicks on desktop and eight on mobile, alleged obstructive. Claude help: Settings → Billing → Cancel ([link](https://support.claude.com/en/articles/8325617-cancel-your-pro-or-max-subscription)). California ARL "simultaneously" rule via `cancellation.md` | [Verified] · legal / B2B SaaS |
| E4 | At most one confirmation step, and one reason-matched offer per cancel intent. | NN/g, Nielsen 2018: overused confirmations stop working. `cancellation.md` anti-pattern "More than one 'Are you sure?'" | [Verified] · mixed |

*The ≤3 threshold is this proposal's calibration choice, not a legal number. It sits between the documented good case (Claude: two clicks plus confirm) and the documented bad one (Amazon: six).*

### Visual hierarchy

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| H1 | Squint test (blur 5–10 px): the primary CTA and the core value are the top two focal points. At most 2 dominant elements and 3 type sizes. | NN/g, Gordon 2021, visual hierarchy ([link](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)) | [Verified] · mixed |
| H2 | Headings front-load the key information and the layout is scannable (layer-cake). Nothing decisive sits only in a right rail or below the cards. | NN/g, Pernice 2017: F-pattern is bad for users and businesses ([link](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)) | [Verified] · mixed |
| H3 ★ | Styling doesn't pull attention away from the true total or the user's chosen path. A highlighted subtotal above unhighlighted fees fails. | FTC 2022, p. 23, "Misdirection" | [Verified] · legal |
| H4 | The primary button has unique styling, consistent placement and a descriptive label. | Baymard 2021: 48% of ecommerce sites miss at least one of these ([link](https://baymard.com/blog/button-design)) | [Verified] · consumer (directional) |
| H5 | monday only: Vibe tokens, nothing hardcoded (existing rule, kept). | Reviewer-owned | — |

### Mobile readiness

| # | A 5 must meet | Source | Tag · Applies to |
|---|---|---|---|
| M1 ★ | At **320 CSS px** width, nothing scrolls in two dimensions. The one exception: a comparison table, which may scroll horizontally if its first column is locked. | WCAG 2.2 SC 1.4.10 Reflow, AA ([link](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)). NN/g, Schade 2017, mobile tables ([link](https://www.nngroup.com/articles/mobile-tables/)) | [Verified] · standard |
| M2 ★ | Every target is ≥24×24 CSS px (AA floor). For a 5, the primary CTA and the decline/close are ≥44×44. | WCAG 2.5.8 (AA, 24) and 2.5.5 (AAA, 44) ([link](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html)). Apple HIG 44 pt via `pricing-pages.md` Mobile. NN/g: 1 cm × 1 cm ([link](https://www.nngroup.com/articles/touch-target-size/)) | [Verified] · standard |
| M3 | Sticky CTAs, headers and banners never fully hide the focused element. | WCAG 2.2 SC 2.4.11 Focus Not Obscured (Minimum), AA ([link](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)) | [Verified] · standard |
| M4 | Every option on a decision screen is visible, or clearly signalled below the fold. The decline or cancel option is never the only one that needs a scroll. | FTC v. Amazon ¶¶144, 146: on mobile, the end-membership options could only be seen after scrolling | [Verified — allegations] · legal |
| M5 | Comparisons collapse to at most 2 columns, tabs or an accordion. | NN/g 2024 comparison tables (at most 2 items on mobile) | [Verified] · mixed |

---

## Dimension → anti-pattern map

When scoring a dimension, check the playbook anti-pattern rows listed against it. **Score against** = check when scoring that dimension; **Also informs** = the row feeds a second dimension. Row names are exact, from each playbook's Anti-patterns table in [../../../playbooks/](../../../playbooks/).

| Dimension | Score against (file → anti-pattern) | Also informs |
|---|---|---|
| **Value clarity** | credit-ui → Bare credit number, no task translation · credit-ui → Cost shown only after the spend · credit-ui → Credit docs that exist but can't be found at the moment of need · credit-ui → Depletion that names the balance, not what stopped · paywalls → Gate with no preview · pricing-pages → Credit amounts without task translation · pricing-pages → The same bullets on every plan · upgrade-triggers → Upgrade CTA with no view of what the next tier changes · upgrade-triggers → "You've hit your limit" with no number or consequence · cancellation → Irreversible loss behind a downgrade, not stated in the flow | paywalls → Gate forces a whole bundled tier for one feature · pricing-pages → AI bundled into a higher tier with no path for AI-only buyers · pricing-pages → Seat minimum hidden until checkout · trial-flows → Upgrade CTA with no price · promotions → A discount without the genuine original price |
| **Timing / trigger** | paywalls → Lock after N uses with no warning · upgrade-triggers → Warning only by email to the owner · upgrade-triggers → Surprise hard stop with no warning threshold · credit-ui → Hard stop mid-agent-task, work lost · credit-ui → Full-screen blocking modal in an agentic flow · paywalls → Hard-blocking modal mid-workflow · promotions → An offer during onboarding · promotions → The same discount every time the user visits pricing · promotions → A discount shown to loyal users who'd renew anyway · trial-flows → Upgrade ask before the activation milestone · trial-flows → Credit balance ends the trial before the milestone · trial-flows → Calendar-only nudges that ignore behaviour · trial-flows → Many never-resetting per-feature allowances · cancellation → The same offer regardless of reason | cancellation → Maximum discount as the default · promotions → The maximum discount by default (offer logic) · upgrade-triggers → Silent degradation in an agent flow · credit-ui → Silent downgrade to a lighter model in an agent flow |
| **Copy quality** | paywalls → Generic "This feature requires Pro" with no outcome · pricing-pages → The same CTA on every plan · trial-flows → Generic "Your trial is ending" · cancellation → Guilt-trip copy ("Don't leave your team behind") · upgrade-triggers → Vague or false upgrade benefit ("more", "unlimited" when it isn't) | upgrade-triggers → A limit moved by a packaging change, framed like a growth trigger · credit-ui → Depletion that names the balance, not what stopped · promotions → A discount without the genuine original price (anchoring) |
| **Friction & flow** | cancellation → More than one "Are you sure?" · cancellation → No downgrade — only stay or cancel, or a downgrade that goes straight to Free · cancellation → An advance-notice window for self-serve reductions · cancellation → No pause option · credit-ui → No IC → admin path · credit-ui → No resume path after purchase · paywalls → No IC path ("Notify admin") · paywalls → Pushing a higher tier than the feature needs · pricing-pages → "Contact sales" as the only Enterprise path · upgrade-triggers → Workspace-wide upgrade for one person's need · upgrade-triggers → Full pricing page at seat expansion · trial-flows → Upgrade CTA with no price | cancellation → Cancel hidden or obstructed · paywalls → Gate forces a whole bundled tier for one feature · credit-ui → Hard stop mid-agent-task, work lost |
| **Trust signals** | cancellation → Early-termination fee hidden at signup · credit-ui → Opaque mechanics ("unlimited" that isn't) · credit-ui → Credit expiry not communicated · credit-ui → Silent downgrade to a lighter model in an agent flow · paywalls → Promising "unlimited" when the tier is capped · pricing-pages → Seat minimum hidden until checkout · pricing-pages → A billing-model change explained unclearly · pricing-pages → Social proof only at the bottom · promotions → A countdown that restarts on reload · promotions → "Last chance" with no real deadline · promotions → An inflated "was" price · promotions → A usage-model change explained unclearly · trial-flows → Two official pages giving different trial allowances · trial-flows → Temporary access with no admin off switch · upgrade-triggers → Silent degradation in an agent flow · upgrade-triggers → Guest auto-converted to paid without admin action | cancellation → Irreversible loss behind a downgrade, not stated in the flow · upgrade-triggers → A limit moved by a packaging change, framed like a growth trigger |
| **Escape hatch** | cancellation → Cancel hidden or obstructed · cancellation → A save offer without "click to cancel" beside it · trial-flows → No visible lower option at expiry | cancellation → More than one "Are you sure?" · cancellation → Guilt-trip copy · cancellation → No downgrade — only stay or cancel… · credit-ui → Full-screen blocking modal in an agentic flow · paywalls → Hard-blocking modal mid-workflow |
| **Visual hierarchy** | pricing-pages → Feature lists start at different heights across plans · pricing-pages → CTAs at different heights across plans · pricing-pages → Recommended plan singled out only by height · pricing-pages → Feature table fully expanded above the fold | pricing-pages → The same CTA on every plan |
| **Mobile readiness** | *No playbook anti-pattern row is mobile-specific.* The only mobile guidance is the Patterns → Mobile list in `pricing-pages.md` (recommended plan first, 44 pt targets, table → accordion, true 375px viewport). | pricing-pages → Feature table fully expanded above the fold |

**Not scorable on a design:** promotions → "Measuring redemption instead of incrementality" and promotions → "No stacking rules" are spec or measurement issues. Route them to `monetization-surface-spec` rather than scoring them. The same goes for trial-flows → "Trial limit tighter than the plan after it" and "AI held back to Free levels in the trial": both are packaging decisions. Score the design's Value clarity consequence at most.

---

## Surface weighting matrix

Weights sum to 1.0 per surface. They encode what actually moves revenue on each surface — e.g. escape-hatch quality is minor on a pricing page but dominant on a cancel flow.

| Dimension | Pricing Page | Paywall / Gate | Promotion | Tier Upgrade | Credit / Consumption | Cancellation | Downgrade | Trial Flow |
|---|---|---|---|---|---|---|---|---|
| Value clarity | 0.20 | 0.22 | 0.15 | 0.18 | 0.20 | 0.10 | 0.15 | 0.20 |
| Timing / trigger | 0.05 | 0.18 | 0.20 | 0.20 | 0.20 | 0.15 | 0.12 | 0.22 |
| Copy quality | 0.15 | 0.15 | 0.20 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 |
| Friction & flow | 0.15 | 0.10 | 0.12 | 0.12 | 0.12 | 0.15 | 0.13 | 0.12 |
| Trust signals | 0.12 | 0.08 | 0.13 | 0.08 | 0.06 | 0.05 | 0.05 | 0.08 |
| Escape hatch | 0.03 | 0.07 | 0.05 | 0.07 | 0.07 | 0.25 | 0.20 | 0.08 |
| Visual hierarchy | 0.20 | 0.12 | 0.10 | 0.12 | 0.12 | 0.08 | 0.12 | 0.08 |
| Mobile readiness | 0.10 | 0.08 | 0.05 | 0.08 | 0.08 | 0.07 | 0.08 | 0.07 |

**Score = Σ (dimension_score × weight) × 20** → yields a 0–100 scale.

Example: a paywall scoring 5 on value clarity contributes 5 × 0.22 × 20 = 22 points toward 100.

---

## Verdict bands

| Weighted score | Verdict |
|---|---|
| 85–100 | Ship it. Minor polish only. |
| 70–84 | Ship after the 🔴/🟠 fixes. Fundamentally sound. |
| 50–69 | Not yet. Real conversion issues — rework before shipping. |
| <50 | Back to the drawing board. Core value or flow is broken. |

State the band verbatim in the one-line verdict.

### Dark-pattern gate — overrides the band

The weights can average away an obstruction: a cancel flow at Escape hatch 1 with every other dimension at 4–5 still scores 74 (worked in [calibration-examples.md](calibration-examples.md)). So, whatever the weighted score:

- **Escape hatch ≤ 2, or any ★ criterion failing on E2, E3, C2, C4, R1 or R3** (see *Anchor sources*) → the verdict is capped at **"Not yet."** State the gate and the failing criterion in the verdict line, and rank that fix first.

The score itself is reported unchanged; only the verdict is capped.
