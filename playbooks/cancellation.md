# Cancellation & downgrade — CRO playbook

Surface type 6. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

## The goal
Save customers worth saving. Let go of those who aren't a fit. Never manipulate. Always learn.

A good cancel flow recovers 25–35% of at-risk customers — not through dark patterns, but by matching the right offer to the real reason.

## Cancel flow architecture

```
Cancel intent → Exit survey → Dynamic save offer → Confirmation → Post-cancel
```

Every step is optional to the user. Never trap.

## Step 1: cancel intent interception

The moment the user clicks "Cancel subscription" is the highest-intent retention moment in the entire product lifecycle. Most products waste it with a generic "Are you sure?"

**Better intercept patterns:**
- **Value recap card**: "Before you go — here's what your team accomplished this month: [personalized stats]"
- **Pause offer**: "Need a break? Pause your account for up to 3 months" — shown before the survey for high-engagement users
- **Direct routing**: For accounts flagged as at-risk by health score, route to CS before the cancel flow

**What not to do:**
- Immediate confirmation dialog with no save attempt
- "Are you sure you want to leave your team behind?" — guilt, not value
- Multi-step confirmation maze designed to confuse (FTC Click-to-Cancel rule violation risk)

## Step 2: exit survey

**One question. 5–8 options. Optional free text.**

| Reason | Save offer to show |
|--------|-------------------|
| Too expensive | Discount (20–30% for 2–3 months) OR downgrade offer |
| Not using it enough | Pause (1–3 months) OR free onboarding session |
| Missing a feature | Roadmap preview + workaround OR direct feature feedback |
| Switching to competitor | Competitive comparison + targeted discount |
| Technical issues / bugs | Immediate CS escalation — don't offer discount, fix the problem |
| Temporary / seasonal | Pause — this is exactly the use case for it |
| Business closed / changed | No save offer. Acknowledge gracefully. Ask for feedback. |
| Other | Free text, surface to product team |

**Survey copy principles:**
- Frame as "Help us improve" not "Why are you abandoning us?"
- No negative options ("I hate the product") — keep it neutral and diagnostic
- Make it feel fast — "Takes 30 seconds"

## Step 3: dynamic save offer

Match the offer to the reason. A discount won't save someone who isn't using the product.

**Discount offer:** 20–30% off for 2–3 months is the sweet spot. Show the dollar amount saved, not just the percentage. Time-limit the offer. Avoid 50%+ discounts — trains cancellation behavior.

**Pause offer:** 1–3 months max (longer pauses rarely reactivate). Keep data, settings, and integrations intact. Auto-reactivation with 7-day advance notice email. 60–80% of pausers return to active status.

**Downgrade offer:** Frame as "right-size your plan" not "downgrade". Show explicitly what they *keep* (more important than what they lose). Make the path back up visible immediately.

**Feature/roadmap offer:** Show the specific feature they're missing + ETA if available. "Here's the workaround teams use today" reduces churn while feature ships. Offer to notify them when it launches.

**High-value account offer:** For top 20% by MRR, route to live CS chat or scheduled call. Personal email from account manager > automated offer. Response rate 3–5x higher than automated flows for this segment.

## Step 4: cancellation confirmation

If they still want to cancel after all of the above — make it clean.

**Must include:** clear statement of when access ends (exact date, not "at end of billing period"); what happens to their data (retention period, export option); reactivation path ("You can come back anytime — your data will be waiting"); one final low-friction offer if not already shown.

**Must not include:** hidden confirmation steps; auto-checked boxes that re-subscribe them; confusing language about what "cancellation" means.

## Step 5: post-cancel experience

**Immediately after cancel:** confirmation email with access end date and data retention info; easy "I changed my mind" reactivation link (active for 48–72h); clear reactivation path in the app (don't hide the "reactivate" button).

**Win-back sequence (7 / 30 / 90 days):** Day 7 — "We've made some improvements — here's what's new". Day 30 — "Your data is still here — come back anytime". Day 90 — special reactivation offer (time-limited).

## Downgrade experience (separate from cancel)

Downgrade is often treated as a mini-cancel. It shouldn't be. A user who downgrades and stays is worth more than one who churns.

**Downgrade flow design:**
1. Show what they're losing — specific features, not plan names
2. Show what they're keeping — lead with this if the lower plan is still solid
3. Offer a delay — "Stay on Pro for 30 more days while you evaluate" (especially good if renewal is near)
4. Confirm the specific date — "Your plan changes on [date], not immediately"
5. No guilt — "Totally fine — here's what to expect"

**Loss framing:** Loss aversion is real but must be used ethically. "You'll lose access to: [list of features currently in use]" — personalized to actual usage. "You've never used [feature]" — omit from the loss list (don't manufacture fear). Show data loss risk separately and prominently if applicable (exports, integrations).

## Benchmarks

*Directional only — these figures pre-date the evidence-tag standard and carry no source. Don't cite them as fact in a review; the sourced material is in the AI-native reference set below.*

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Cancel flow save rate | <10% | 25–35% | 40%+ |
| Pause offer acceptance | <10% | 15–25% | 30%+ |
| Discount offer acceptance | <10% | 20–30% | 35%+ |
| Post-cancel reactivation (90 days) | <5% | 10–15% | 20%+ |
| Downgrade → upgrade within 90 days | <5% | 12–18% | 25%+ |

## Best-in-class examples

*Pre-dates the evidence-tag standard — the patterns are sound, but any figures here are unsourced. Tagged teardowns are in the AI-native reference set below.*

**Duolingo** — Cancel flow shows personalized streak data ("You've learned for 47 days straight — here's what you'd lose"). Loss aversion anchored to real behavior, not abstract features.

**Spotify** — Pause offer shown before exit survey for users who haven't opened the app in 30+ days. Matches the inactivity signal to the right offer.

**HubSpot** — For high-value accounts, cancel click routes to a "let's talk" flow with live CS availability shown. 3x higher save rate vs automated discount offers for this segment.

**Notion** — Downgrade confirmation shows feature-by-feature "what you keep / what you lose" with actual data from the user's workspace (e.g., "You have 3 databases that require Pro — here's what happens to them").

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Hidden or buried cancel button | Dark pattern, erodes trust |
| More than one "Are you sure?" step | Confirmation maze — regulatory risk (FTC Click-to-Cancel) |
| Guilt-trip copy | Brand damage, no lift evidence |
| Offering the same discount regardless of reason | A discount won't save someone who isn't using the product |
| No downgrade option — only "stay" or "cancel" | Forces churn that a right-sized plan could have prevented |

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture before citing in a review.

The honest headline: **none of the four runs an aggressive save flow.** They retain through landing spots (a free tier that keeps your data), partial downgrades, and pricing mechanics — not through discount offers. That's a regulatory advantage and a missed revenue opportunity at the same time. The steal is their clean mechanics; the opportunity is layering a reason-matched save step on top.

### At a glance

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Where cancel lives | [Teardown needed] | Admin → Settings → Plan → Cancel plan | Billing settings (Owner/Admin) | Settings → Billing → Cancel |
| Exit survey | [Teardown needed] | Yes — one cancellation reason, then confirm | [Teardown needed] | Not documented |
| Save offer | Not documented | Not documented | Reported: offers other tiers / fewer members | None; no coupons by policy |
| Landing spot | Free plan (100 credits) | Starter (3 files/project, 1 project) | Free Forever (data kept, 60MB storage) | Free (history preserved) |
| Partial downgrade | Legacy plans kept | Seat downgrades per person | Drop AI add-on without cancelling plan | Max → Pro at period end |
| Access end | — | End of billing period | End of billing period | End of billing period; cancel 24h before renewal |

### Figma — clean mechanics, harsh landing

**What they ship [Verified].** Cancel from Admin → Settings → Plan → Cancel plan; Figma asks for a cancellation reason, then confirms. Paid features run until the end of the billing period, then the team drops to Starter: 3 Figma Design/Sites files and 3 files per other product in a project, one project per team. Over the limit, the team is locked and files become view-only until reorganized; files are not deleted. Published Sites are unpublished; Make apps stay live on the figma.site subdomain but lose custom domains. The Help Center gives a pre-downgrade checklist (move files to drafts, consolidate to one project).

**Why it works.** Nothing is deleted, and the "what happens" consequences are specific and documented. A one-question reason capture is the minimum viable exit survey.

**Where it breaks.** A locked team with view-only files reads as coercion to users who didn't read the checklist — forum threads show owners who feel forced to resubscribe. The consequence list lives in the Help Center, not in the cancel flow.

**Steal for monday.com.** Bring the consequence list *into* the flow, personalized: "3 of your boards use Pro automations — here's what happens to each on [date]." Put the export/reorganize actions on the confirmation screen, not in a help article.

### ClickUp — partial cancellation of the AI layer

**What they ship [Verified/Reported].** Cancelled workspaces stay on the paid plan until the period ends, then move to Free Forever; tasks, docs, and structure remain, premium features lock, storage drops to 60MB. The AI add-on can be cancelled separately from the workspace plan. The flow reportedly offers moving to a different paid tier or adjusting members instead of full cancellation **[Reported]**. Some guides claim disabling auto-renew without downgrading requires contacting support **[Reported — verify]**.

**Why it works.** Separately cancellable AI is the most important retention mechanic in this set: a customer who doesn't see AI value can shed that layer and keep the core product.

**Where it breaks.** If auto-renew control really requires support, it's the kind of friction FTC Click-to-Cancel targets. A 60MB landing spot is effectively unusable for teams.

**Steal for monday.com.** When the exit reason is AI-related ("AI credits too expensive" / "not using AI"), offer *reduce credit package* before *cancel plan* — shed the credit layer, keep seats. Makes the credit decision reversible and protects the seat base.

### Claude — the frictionless benchmark

**What they ship [Verified].** Settings → Billing → Cancel. Cancellation takes effect at the end of the billing period; access continues until then; Anthropic tells users to cancel at least 24 hours before the billing date to avoid the next charge. Upgrades apply immediately (prorated); Max → Pro downgrades take effect at the next cycle. Conversation history is preserved on downgrade. App-store subscriptions cancel through Apple/Google. No discount offers — the Help Center states Support can't issue one-off discounts.

**Why it works.** Two steps, plain language, exact timing rules stated upfront. This is what "compliant by default" looks like, and it builds the kind of trust that makes re-subscription easy.

**Where it breaks.** Zero save attempt. A Max 20x user cancelling because of cost gets no "switch to Max 5x" or "Pro + usage credits with a cap" option in the flow.

**Steal for monday.com.** Claude's mechanics as the compliance baseline (cancel reachable in two clicks from settings; exact end date; renewal cutoff stated), plus one right-size step: "Most teams who leave for cost move to [smaller package] instead — [X] credits, $[Y]/mo." One offer, one screen, skippable.

### Clay — retention through pricing mechanics

**What they ship [Verified].** Credit rollover up to 2x the monthly allocation reduces "we paid for credits we didn't use" churn after quiet months. On repricing, legacy plans were kept indefinitely for existing customers — no forced migration moment. Free plan exists as a landing spot. The cancel flow itself isn't publicly documented **[Teardown needed]**.

**Why it works.** The most common usage-product churn reason — "we didn't use what we paid for" — is addressed before cancellation, by rollover.

**Where it breaks.** A 2x rollover cap still wastes credits for seasonal teams running quarterly campaigns **[Reported]**.

**Steal for monday.com.** Show rolled-over balance in the cancel intercept: "You have 4,200 unused credits — they carry into next month." Accumulated balance is a concrete loss anchor that seat-only SaaS doesn't have.

### Save-step design for AI credit products (synthesized from the four)

| Exit reason | Right move | Borrowed from |
|---|---|---|
| "AI too expensive" | Reduce credit package, keep seats | ClickUp separate AI cancel |
| "Didn't use the credits" | Show rollover balance + pause credit purchases | Clay rollover |
| "Hit limits too often" | Package upgrade with overage cap, not cancel | Claude usage credits + caps |
| "Too expensive overall" | One right-size plan offer | Claude Max → Pro path (made explicit) |
| "Moving work elsewhere" | Export + clear data-retention date | Figma "nothing is deleted" |

### Copy bank — AI cancellation

| Moment | Pattern | Example for monday.com |
|---|---|---|
| Timing clarity | Exact date + renewal rule | "Your plan stays active until [date]. You won't be charged again." |
| Credit balance anchor | Balance, not guilt | "You have 4,200 unused AI credits in your account" |
| AI-layer shed | Keep the core | "Keep your boards and seats — just switch to a smaller credit package" |
| Personalized consequence | Specific assets | "2 agents and 3 AI Blocks will stop running on [date]. Your boards stay." |
| Reversal | Make coming back easy | "Change your mind before [date]? One click and nothing changes." |

### Sources (checked 2026-09-24)

- Figma: https://help.figma.com/hc/en-us/articles/360046216313-Upgrade-or-downgrade-your-plan · https://forum.figma.com/report-a-problem-6/how-can-i-edit-my-files-after-not-resubscribing-49097
- ClickUp: https://legalclarity.org/how-to-cancel-your-clickup-subscription-step-by-step/ · https://consultevo.com/clickup-cancel-plan-guide/ · https://cancelmates.com/cancel/cancel-clickup-subscription · https://www.bardeen.ai/answers/how-to-cancel-clickup-subscription
- Claude: https://support.claude.com/en/articles/8325617-cancel-your-pro-or-max-subscription · https://www.ssdnodes.com/learn/cancel-or-downgrade-claude-plan · https://claudepricing.com/billing-cancellation · https://blog.nachonacho.com/best/claude-promo-codes/
- Clay: https://www.clay.com/blog/introducing-clay-pricing-3-0-the-most-flexible-credit-system-on-the-market · https://www.docket.io/resources/research/clay-pricing · https://lagrowthmachine.com/clay-pricing/

## monday.com-specific notes

- AI Agents context: if a user is canceling because agents didn't deliver value, a discount won't help. The save offer should be a re-onboarding session with a CS specialist.
- Credit-based model: cancellation after credit depletion is a specific pattern — user exhausted their allocation and didn't see enough value to buy more. The save offer here is a free credit top-up + guided value moment, not a plan discount.
- Admin vs. end user: in B2B, the person clicking cancel may not be the economic buyer. Design must route "request to cancel" to admin review for multi-seat accounts.
- Regulatory: monday.com operates globally. FTC Click-to-Cancel (US), EU consumer directives, and Israeli consumer protection laws all mandate accessible cancellation. Legal review required before shipping any cancel flow changes.
