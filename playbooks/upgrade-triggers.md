# Tier upgrade triggers — CRO playbook

Surface type 4: plan-level limits — seats, features, automations. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

Credit / consumption limits are a different emotional state and have their own playbook: [credit-ui.md](credit-ui.md). Don't conflate the two — a seat cap is a blocked-and-frustrated moment; a credit meter is an anxious, mid-task moment.

## When to show

- User attempts to add a seat beyond plan limit
- User tries to enable a feature locked to a higher tier
- Admin views usage dashboard and sees team at capacity
- Usage is consistently at 80–90% of plan limits (proactive nudge before the wall)

## Design principles

1. **Contextualize the limit** — "Your team has used 9 of 10 seats" is better than "You've reached your limit"
2. **Show the delta** — What does the next tier unlock? Make it specific, not a full plan comparison.
3. **Route to the right person** — In B2B, the user hitting the limit is often not the buyer. Provide a "notify admin" path alongside the upgrade CTA.
4. **Don't block the current task** — If the user was doing something, let them finish it (or save state) before presenting the upgrade.

## Screen structure

```
[Context: what they hit]
"Your team is at 10/10 seats"

[Upgrade delta — what they get next]
"Pro includes up to 25 seats, plus:"
• [1-2 most relevant features for this team]

[Social proof if available]
"Teams like [similar company type] move to Pro when they reach this point"

[Primary CTA]  [Notify admin]
[Maybe later — dismiss]
```

## Proactive vs. reactive triggers

- **Reactive** (at 100%): necessary but lowest-satisfaction moment. User is already blocked.
- **Proactive** (at 70–80%): higher satisfaction, higher CVR. User isn't frustrated yet.
- **Recommendation**: show a non-blocking nudge at 75%, a more prominent prompt at 90%, full gate at 100%.

## Wireframe patterns

**Pattern A — usage limit reached (inline):**
```
[Usage bar: ████████░░ 8/10 automations]
[Inline notification below bar:]
  "You've used 8 of your 10 monthly automations."
  "Upgrade to Pro for unlimited automations."
  [CTA: "Upgrade to Pro"]  [Link: "See what Pro includes"]
```
Why it works: usage bar makes the limit visible and concrete. Limit + consequence + action in one view.

**Pattern B — seat expansion modal:**
```
[Modal:]
  [Headline: "Add more team members"]
  [Current: "You have {N} seats — {N} are used"]
  [Seat selector: [−] 3 [+] additional seats]
  [Price: "+$X/month — billed {monthly/annually}"]
  [CTA: "Add seats"]  [Dismiss: "Not now"]
```
Apply when: user tries to invite someone when at seat limit. Offer the expansion in the moment.

## Benchmarks

*Directional only — these figures pre-date the evidence-tag standard and carry no source. Don't cite them as fact in a review; the sourced material is in the AI-native reference set below.*

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Tier gate → upgrade CVR | <5% | 8–15% | 20%+ |
| Proactive nudge (75%) → upgrade CVR | <3% | 5–10% | 15%+ |

## Best-in-class examples

*Pre-dates the evidence-tag standard — the patterns are sound, but any figures here are unsourced. Tagged teardowns are in the AI-native reference set below.*

**GitHub Copilot (Business)** — Seat limit hit triggers email to org admin AND in-product notification to the blocked user with a "request access" flow. Separates the user-facing experience from the buyer-facing action.

**Zapier** (task limits) — Zap-level usage bar visible on every automation. Turns invisible usage into a tangible, always-present signal. Normalizes awareness of limits before they're hit.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| "You've hit your limit" with no number or consequence | Frustration with no path forward |
| Upgrade CTA with no view of what the next tier changes | Friction, zero motivation |
| Surprise hard stop with no warning threshold | User feels ambushed, not informed |

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture before citing in a review.

### At a glance — who hits the limit vs. who pays

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Limit type that triggers upgrade | Capability (CRM, API) + volume | Seat type | Plan (workspace-wide) + automation runs | Usage tier / seat tier |
| IC → admin path | N/A (unlimited seats) | Best-in-class request flow | Weak — upgrade applies to whole workspace | Owner-set spend limits per seat tier / member |
| Proration | — | Yes, credit for unused seat time | Yes | Yes, upgrades immediate and prorated |
| Signature move | Docs steer top-up buyers to tier upgrade | 3-day temporary access + request reason | — | Seat tiers (1.25x / 6.25x) inside one team plan |

### Figma — the reference implementation for IC → admin upgrades

**What they ship [Verified].**
- **Request moment:** users request a seat when they attempt an action their seat doesn't allow (e.g., creating a file in a product they lack). With manual approval, they get a one-time 3-day temporary access per paid seat type while the admin reviews.
- **Admin side:** request lands in the admin dashboard showing where it was sent from, the request reason, current seat, time, and cost of the new seat. A Reminders tab surfaces users who nudged. Email + in-app notification go to admins; the requester is notified of the decision both ways.
- **Policy control:** per seat type, admins choose manual approval, manual unless a paid seat is already available (default), or auto-approve (buys a seat if none free). Auto-approve comes with daily/weekly digest emails listing new paid seats.
- **Billing:** approved seats are prorated; if the user already held a paid seat, the unused time is credited.

**Why it works.** Every step removes a reason for the admin to say no: the reason is attached, the cost is shown, the user is already productive, and the default policy auto-fills idle seats. Digests make auto-approve safe for finance.

**Where it breaks.** One-time temporary access: a declined user loses the grace path for that seat type permanently. Accidental seat upgrades are a known refund-request category **[Reported]**.

**Steal for monday.com.**
1. Request modal with a required one-line reason ("What do you need it for?") — it's the admin's approval argument.
2. Admin request card: requester, feature/limit hit, where, reason, price delta in the seat *bundle* (monday sells bundles, per [monday-context.md](../context/monday-context.md)).
3. Default policy "auto-approve if a paid seat is idle" — zero-cost yes.
4. Digest email for auto-approved upgrades.

### ClickUp — the counter-example on workspace-wide upgrades

**What they ship [Reported/Verified].** Every member of a workspace must be on the same plan, so one person needing a Business feature moves everyone to Business pricing; the AI add-on is also billed on every paid member. Free guests can auto-convert to paid members — one reported case saw a bill jump from ~$150 to ~$1,200 **[Reported]**. Automation runs are tiered (Free 100/mo, Unlimited 1,000/mo, Business 10,000/mo) and are a natural volume trigger.

**Why it works (for revenue).** Maximizes expansion per upgrade event.

**Where it breaks.** The upgrade decision becomes a budget decision for the whole workspace, so ICs rarely trigger it, and surprise seat conversions erode admin trust.

**Steal for monday.com.** The automation-runs meter is the right proactive trigger (monday already has an automation cap per [monday-context.md](../context/monday-context.md)). Never convert a guest or viewer to paid without an explicit admin action — show "Invite as member (+1 seat in your bundle)" vs. "Invite as guest (free)" at invite time.

### Clay — no seat triggers, so capability does the work

**What they ship [Verified].** Unlimited seats on every plan, so upgrades are driven by capability (CRM sync and API on Growth) and credit volume. Clay's docs state that one-time top-ups carry a 30% premium and that upgrading the Data Credit tier is more cost-effective for regular needs.

**Why it works.** The docs copy does the upsell: the top-up is always available (no hard wall) but is priced to make the tier upgrade the rational choice for anyone who tops up twice.

**Steal for monday.com.** After the second top-up in a billing period, show the math: "You've topped up twice this month. The 8,000-credit package costs less than what you've spent." Price architecture + a trigger on the pattern, not the moment.

### Claude — seat tiers and spend controls inside one team

**What they ship [Verified].** Team plans have standard seats (1.25x Pro usage) and premium seats (6.25x Pro). Owners can enable usage credits and set monthly spend limits for the organization, by seat tier, or per member; the member list shows month-to-date spend so owners can optimize seat assignments. Individual Pro→Max upgrades apply immediately with prorated billing.

**Why it works.** Mixed seat tiers solve the "only 3 of 20 people are heavy users" problem without upgrading the whole team. The MTD spend column is the admin's upgrade trigger: a member consistently paying overage is a premium-seat candidate.

**Steal for monday.com.** An admin view that flags heavy AI users on overage: "3 members used more than [X] credits in top-ups this month — a larger package would save $[Y]." Upgrade trigger built from observed spend, shown to the payer.

### Copy bank — upgrade triggers

| Moment | Pattern | Example for monday.com |
|---|---|---|
| IC request modal | Ask for the reason | "Tell [Admin name] why you need Pro — we'll include it in the request" |
| Admin request card | Who, what, cost | "Dana hit the automation limit on 'Q4 Launch' board · Needs Pro · +$[X]/mo in your 10-seat bundle" |
| Proactive volume nudge | Number + consequence | "188 of 250 automations used — at this pace you'll hit the limit on [date]" |
| Top-up → package nudge | Show the math | "Two top-ups this month cost $[X]. The next package is $[Y] and includes more." |
| Guest vs. member at invite | Make the cost explicit | "Invite as guest (free, view only)" / "Invite as member (uses 1 seat)" |

### Sources (checked 2026-09-24)

- Figma: https://help.figma.com/hc/en-us/articles/1500003870721-Approve-or-decline-seat-upgrade-requests · https://help.figma.com/hc/en-us/articles/4414038570007-Set-approval-settings-for-new-seats · https://help.figma.com/hc/en-us/articles/15506350302615-Get-notified-when-people-upgrade-to-a-paid-seat · https://help.figma.com/hc/en-us/articles/360041061034-Manage-billing-on-the-Professional-plan · https://help.figma.com/hc/en-us/articles/360040453433-Make-a-seat-request
- ClickUp: https://quackback.io/blog/clickup-pricing · https://www.eesel.ai/blog/clickup-pricing · https://get-alfred.ai/blog/clickup-pricing
- Clay: https://university.clay.com/docs/actions-data-credits
- Claude: https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans · https://www.ai-toolbox.co/claude-management-and-productivity/claude-usage-limits-2026

## monday.com-specific notes

- Automation cap (250/mo on Standard) is the highest-volume tier-upgrade trigger today — proactive nudge at 75% ("188/250 automations used") outperforms the reactive hard-stop message.
- Seat expansion: always show the bundle price delta (bundles of 3/5/10/15/20/25/30/40), never a per-seat price that implies granular add-one purchasing.
- Route ICs who hit a seat or feature cap to "notify admin" — they cannot self-purchase.
