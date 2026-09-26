# Scoring Rubric — Anchors & Weighting

Read this for **every** review. It exists so that two different reviewers scoring the same design land in the same place. Score against the anchor definitions below — not intuition.

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
- **5** — Relevant, well-placed proof or risk-reducer (guarantee, cancellation ease, contextual usage proof) near the CTA.

### Escape hatch quality — *is the "no" path clear and non-manipulative?*
- **1** — Hidden/tiny close, guilt copy, or a maze; dark-pattern territory.
- **3** — Escape exists but is de-emphasized more than necessary, or slightly buried.
- **5** — "No" path is visible, honest, one action; declining is respected and easy.

### Visual hierarchy — *does the eye go to the right place first?*
- **1** — Competing focal points; primary CTA doesn't win; key value buried.
- **3** — Generally readable but the eye path isn't fully intentional; secondary elements over-weighted.
- **5** — Clear F/Z path; primary CTA and core value dominate; supporting info recedes. (For monday: Vibe tokens used, no hardcoded values.)

### Mobile readiness — *would this work at 375px?*
- **1** — Breaks, truncates, or hides the CTA on mobile; horizontal scroll; tap targets too small.
- **3** — Works but cramped; some reflow awkwardness; comparison tables hard to scan.
- **5** — Fully responsive; CTA reachable; content re-prioritized sensibly for small screens.

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
