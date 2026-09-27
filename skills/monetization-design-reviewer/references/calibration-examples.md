# Calibration examples — what a 1, 3 and 5 look like

Read with `scoring-rubric.md`. These examples calibrate the anchors so two reviewers land on the same number. They are **not** CRO benchmarks: those live in `playbooks/`. Evidence tags as in [playbooks/README.md](../../../playbooks/README.md); `[Illustrative]` marks a generic case with no real public example. FTC and DOJ items are **allegations** (Amazon settled without admission). Legal items are guidance; reviewed by legal: not yet.

## Per-dimension anchors

### Value clarity

| Score | What it looks like | Example |
|---|---|---|
| 1 | The unit hides the cost or the outcome: a bare credit number, "tokens", "coins", or a plan name as the headline. | The FTC names paying in virtual currency to hide the real cost as a dark pattern, "Intermediate Currency" ([FTC 2022, p. 23](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf)) [Verified]. On a credit meter: "2,340 credits left" with no task or money translation [Illustrative] |
| 3 | The value is there but generic, or it's documented off-surface. | Figma's downgrade consequences are specific but live in the Help Center, not in the cancel flow ([cancellation.md](../../../playbooks/cancellation.md), Figma teardown) [Verified via playbook] |
| 5 | The outcome and the cost are legible where the decision happens. | HubSpot publishes included credits per tier plus a per-action rate sheet ([pricing-pages.md](../../../playbooks/pricing-pages.md), AI credits) [Verified via playbook]. Whether HubSpot's in-product meter shows it is [Teardown needed] |

### Timing / trigger logic

| Score | What it looks like | Example |
|---|---|---|
| 1 | Fires before value, or lands where the affected user never sees it. Recurs after a decline. | Airtable warns about automation limits only by email to the owner ([upgrade-triggers.md](../../../playbooks/upgrade-triggers.md)) [Verified via playbook]. Amazon's cancel flow showed "Remind Me Later" four times on the way to cancelling (FTC v. Amazon ¶134) [Verified — allegation] |
| 3 | Reactive: fires at 100% of the limit, or a fixed calendar nudge that ignores behaviour. | trial-flows → "Calendar-only nudges that ignore behaviour" [Illustrative instance] |
| 5 | Proactive at the playbook threshold, capped after a decline, and non-blocking inside a task. | After June 2025, Cursor added visibility of approaching limits ([case: cursor-2025-pricing](../../../playbooks/cases.md#cursor-2025-pricing)) [Verified]. That shows the proactive half only; frequency capping is [Teardown needed] |

### Copy quality

| Score | What it looks like | Example |
|---|---|---|
| 1 | The headline is a label, the CTA is generic or misleading, the decline shames. | FTC's confirmshaming example, "No, I don't want to save money" (FTC 2022, p. 25) [Verified]. Amazon's "Continue to Cancel" did not cancel (¶128) [Verified — allegation] |
| 3 | The CTA is specific but repeated across choices, or the headline hints at a benefit without naming it. | Linear uses "Get started" on every self-serve plan ([pricing-pages.md](../../../playbooks/pricing-pages.md)) [Verified via playbook]. Headline not assessed |
| 5 | The headline names the outcome, each CTA names what it unlocks, the decline is neutral, confirms name the consequence. | Cursor's tier-specific CTAs: "Get Pro", "Get Teams", "Contact sales" ([pricing-pages.md](../../../playbooks/pricing-pages.md)) [Verified via playbook]. That meets the CTA half; the headline is [Teardown needed] |

### Friction & flow

| Score | What it looks like | Example |
|---|---|---|
| 1 | Leaving takes several times more steps than joining, links throw users out of the flow, info has to be re-entered. | ABCmouse, as alleged: 6–9 screens to cancel, each with links out of the path (FTC 2022, pp. 13–14) [Verified — allegation]. Amazon: six clicks on desktop, eight on mobile, against one or two to enrol (¶¶114, 140, 142) |
| 3 | Reasonable, but with one or two removable steps, or a policy step on top. | Asana requires 30 days' written notice to reduce seats or downgrade ([cancellation.md](../../../playbooks/cancellation.md)) [Verified via playbook]. The UI may be fine; the policy adds a step |
| 5 | Minimal steps, the same medium as sign-up, state preserved. | Claude: Settings → Billing → Cancel, effective at period end ([Claude help](https://support.claude.com/en/articles/8325617-cancel-your-pro-or-max-subscription)) [Verified]. In-flow screens [Teardown needed] |

### Trust signals

| Score | What it looks like | Example |
|---|---|---|
| 1 | Material terms hidden: fees in fine print or behind hover icons, undisclosed limits. | Adobe, as alleged: the early-termination fee sat in small print or behind hover icons while the monthly price was prominent ([FTC 2024](https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling)) [Verified — allegation] |
| 3 | Proof present but generic or badly placed. | "Trusted by 50,000+ teams" in the footer, away from the CTA [Illustrative]. pricing-pages → "Social proof only at the bottom" |
| 5 | A relevant risk-reducer at the point of commitment, and all terms on the screen. | ClickUp shows a 30-day money-back guarantee on its pricing page ([cancellation.md](../../../playbooks/cancellation.md)) [Verified via playbook]. Its placement relative to the CTA is [Teardown needed] |

### Escape hatch quality

| Score | What it looks like | Example |
|---|---|---|
| 1 | A maze: repeated save screens, the real exit last, keep options visually dominant. | Amazon's "Iliad" flow (¶¶113–148; worked example below) [Verified — allegation]. FTC's false-hierarchy example: a bright orange keep button above a small pale-gray cancel link (FTC 2022, p. 23) [Verified] |
| 3 | The exit exists but is de-emphasized, or has to be scrolled to. | A text-link "No thanks" at under 4.5:1 contrast under a filled CTA [Illustrative]. Fails EH2 |
| 5 | Visible, honest, one action. An offer, if any, sits beside a clear continue. | Claude cancel (above) [Verified steps]. California ARL: any save offer must be shown *simultaneously* with the click-to-cancel option ([cancellation.md](../../../playbooks/cancellation.md) Legal context) [Verified via playbook] |

### Visual hierarchy

| Score | What it looks like | Example |
|---|---|---|
| 1 | Emphasis works against the user's task. | FTC's Misdirection example: a highlighted subtotal with the fees below in plain styling (FTC 2022, p. 23) [Verified]. Amazon's second cancel page led with a bold saving and an orange "Switch to annual payments" button (¶129) [Verified — allegation] |
| 3 | Readable, but secondary elements compete with the CTA. | Recommended plan singled out only by extra height ([pricing-pages.md](../../../playbooks/pricing-pages.md) anti-pattern) [Illustrative instance] |
| 5 | Passes the squint test: one recommended plan by emphasis, aligned rows and CTAs. | Canva's "Recommended" badge on Business singles out one plan by emphasis ([pricing-pages.md](../../../playbooks/pricing-pages.md)) [Verified via playbook]. The full squint test on that page is [Teardown needed] |

### Mobile readiness

| Score | What it looks like | Example |
|---|---|---|
| 1 | The key option is hidden, targets are under 24 px, content scrolls in two dimensions. | Amazon mobile cancel, as alleged: 8 pages and 8 clicks, with options visible only after scrolling (¶¶142–146) [Verified — allegation] |
| 3 | Works but cramped: a horizontally scrolling comparison table with no locked first column, targets 24–43 px. | [Illustrative] |
| 5 | Reflows at 320 CSS px, primary and decline ≥44 px, recommended plan first when stacked, comparison as tabs or accordion. | [Illustrative]. No public teardown captured. `pricing-pages.md` Mobile holds the pattern |


---

## Worked example — Amazon Prime "Iliad" cancel flow (as alleged, pre-April 2023)

**Why this one:** the most thoroughly documented public monetization flow. The FTC complaint describes every page, button, label and order on desktop and mobile. **Source:** *FTC v. Amazon.com, Inc.*, No. 2:23-cv-00932, complaint filed 06/21/23, ¶¶113–148 ([PDF](https://www.ftc.gov/system/files/ftc_gov/pdf/amazon-rosca-public-redacted-complaint-to_be_filed.pdf)) [Verified — allegations]. Amazon changed the flow around April 2023 (¶113) and settled in Sept 2025 without admission ([case: ftc-cancellation-enforcement](../../../playbooks/cases.md#ftc-cancellation-enforcement)).

**Surface:** Cancellation · **Cohort:** existing paying consumers · **Weights:** Cancellation column.

**The documented flow:**
- Prime Central → "Manage Membership" → "End Membership".
- Page 1: a benefit-usage recap, with "Remind Me Later", "Continue to Cancel" and "Keep My Benefits", plus links that leave the flow (¶¶127–128).
- Page 2: discounted and annual alternatives, the saving in bold, an orange "Switch to annual payments" button, and a vague warning that items "will be affected" (¶¶129–132).
- Page 3: five options. Only the last, "End Now", cancels at once; "End on {date}" turns off auto-renew with no refund (¶¶133–139).
- The refund limit was not disclosed (¶141). Mobile: 8 pages, 8 clicks, final options below a scroll (¶¶142–146).

| Dimension | Score | Rationale (anchor · criterion) | Weight | Points (score × weight × 20) |
|---|---|---|---|---|
| Value clarity | 2 | The usage recap on page 1 is concrete (a strength). But what each end option does ("End on {date}" vs "End Now", refund or not) and what "will be affected" means are unclear. Fails VC3 on refund terms | 0.10 | 4.0 |
| Timing / trigger | 1 | The same save options for every user, with no reason asked. "Remind Me Later" recurs 4× after being passed over (¶134). Fails TM2 ★ | 0.15 | 3.0 |
| Copy quality | 2 | "End Now" is specific, but "Continue to Cancel" doesn't cancel, twice (CQ4 ★ caps at 2). Keep labels are inconsistent ("Keep My Benefits" / "Keep My Membership") | 0.15 | 6.0 |
| Friction & flow | 1 | Six clicks on desktop and eight on mobile, against one or two to enrol. Links eject users from the flow (FF1 ★, FF4) | 0.15 | 3.0 |
| Trust signals | 2 | "You still have 7 days left" reassures, and pause has a one-click resume. The refund limit is undisclosed (TS1 ★ caps at 2) | 0.05 | 2.0 |
| Escape hatch | 1 | A maze: three save pages, the real exit last of five, keep options repeated (EH3 ★, EH4) | 0.25 | 5.0 |
| Visual hierarchy | 2 | The orange annual-switch button and bold saving lead page 2, and the exit is placed last (VH3 ★ caps at 2). The styling of "End Now" isn't described, so this isn't scored 1 | 0.08 | 3.2 |
| Mobile readiness | 1 | Final options need a scroll to be seen, and the flow grows to 8 pages (MR4). Target sizes aren't documented and stay Pending | 0.07 | 1.4 |
| **Total** | | | **1.00** | **27.6 / 100** |

**Math:** Σ(score × weight) = 0.20 + 0.15 + 0.30 + 0.15 + 0.10 + 0.25 + 0.16 + 0.07 = **1.38**; × 20 = **27.6**.
**Verdict:** "Back to the drawing board. Core value or flow is broken." (<50 band). The dark-pattern gate would also fire: EH3 fails, and so do CQ4 and TS1.

**What the weighting did.**
- Escape hatch alone cost 20 of the 25 points it could carry.
- Under the Promotion column, the same eight scores give 31.6. The low Escape weight there hides most of the obstruction, which is why the column choice matters.
- **The averaging trap:** keep Escape = 1 but raise everything else (VC 5, T 4, C 5, F 4, Tr 5, VH 5, M 5). That gives 0.50 + 0.60 + 0.75 + 0.60 + 0.25 + 0.25 + 0.40 + 0.35 = 3.70 → **74.0**, "Ship after the 🔴/🟠 fixes", for a flow that still obstructs. That is the case for the *Dark-pattern gate* in [scoring-rubric.md](scoring-rubric.md#dark-pattern-gate--overrides-the-band).

**What a 5 on Escape hatch looks like here:** Settings → Billing → Cancel, with at most one reason-matched offer shown beside "Continue to cancel", and the end date and refund terms on the confirm screen. See the Claude and Canva entries in `cancellation.md`.
