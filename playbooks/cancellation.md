# Cancellation & downgrade — CRO playbook

Surface type 6. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks). Cohort: **existing paying users**.

## Core rule

Save the customers worth saving by matching one honest offer to the real reason — and make leaving easy. Every step is optional to the user; nothing traps them. The strongest retention is upstream of the flow: a product the customer depends on, and a downgrade that still works.

## Benchmarks

| Metric | Number | Tag | Applies to | Source | Checked |
|---|---|---|---|---|---|
| Top stated cancel reasons (≈3M cancel sessions) | "Budget limitations" 33%, "infrequent usage" 31% | [Verified] | mixed | [Churnkey State of Retention 2025](https://churnkey.co/reports/state-of-retention-2025) | 2026-09-25 |
| Pause offer acceptance, across all cancel sessions | 19% | [Verified] | mixed | [Churnkey State of Retention 2025](https://churnkey.co/reports/state-of-retention-2025) | 2026-09-25 |

Price is the stated reason in about a third of cancellations, not most — so a discount answers only one reason in three.

## Legal context — guidance, not legal advice

**Reviewed by legal: not yet.** Until it is, this section is guidance, not a requirement. Every cancel-flow change goes to legal before shipping. Most of these rules protect **consumers** (personal-use buyers); B2B team plans are largely out of scope, but monday sells to individuals too.

| Jurisdiction | What it requires | Source (primary) |
|---|---|---|
| **California** (ARL, AB 2863; contracts entered, amended or extended on or after July 1, 2025) | Online cancellation "at will", with no steps that obstruct or delay — via a prominently located link or button (which may sit in the account, profile or settings) or a pre-formatted termination email. A flow **may** show a discount, retention benefit, or the effects of cancelling, **provided it simultaneously shows** a prominently located "click to cancel" link or button. No limit on the number of offers. Consumers only (personal, family or household use) | [AB 2863 text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2863), §17602(d)(1), (e)(2); [§17601](https://law.justia.com/codes/california/code-bpc/division-7/part-3/chapter-1/article-9/section-17601/) |
| **Germany** (§312k BGB, since July 1, 2022) | Consumer contracts concluded online need a "Verträge hier kündigen" button leading to a confirmation page with a "jetzt kündigen" button | [§312k BGB](https://dejure.org/gesetze/BGB/312k.html) |
| **EU** (Directive 2023/2673, new Art. 11a CRD, from June 19, 2026) | A mandatory online **withdrawal** function for the 14-day right of withdrawal in consumer distance contracts. Not an ongoing-subscription cancel button; no save-offer rules | [Reported] — primary text not read; [K&L Gates summary](https://www.klgates.com/thought-leadership/New-EU-Withdrawal-Button-Requirement-Practical-Implications-and-Recommendations-for-US-and-Global-Online-Sellers-7-8-2026) |
| **UK** (DMCC Act subscription regime) | Expected to commence in **spring 2027**, with secondary legislation and CMA guidance still to come. Separately, the CMA can already fine up to 10% of global turnover for existing consumer-law breaches (since April 6, 2025) | [Government response, Apr 2, 2026](https://www.gov.uk/government/consultations/consultation-on-the-implementation-of-the-new-subscription-contracts-regime/outcome/government-response-to-consultation-on-the-implementation-of-the-new-subscription-contracts-regime-web-accessible-version); CMA powers [Reported] |
| **US federal** | The FTC "Click-to-Cancel" rule was vacated by the 8th Circuit on July 8, 2025; the FTC still enforces against deceptive flows case by case — see [case: ftc-cancellation-enforcement](cases.md#ftc-cancellation-enforcement) | [Reported] — law-firm summary |

## Patterns

### Flow architecture

```
Cancel intent → Reason (one question) → One reason-matched offer (+ "continue to cancel" beside it) → Confirmation → Post-cancel
```

Every step is optional to the user. Where California's rule applies, the "click to cancel" option sits on the same screen as any offer, not after it.

### Step 1 — cancel intent

The click on "Cancel" is the highest-intent retention moment in the lifecycle; a generic "Are you sure?" wastes it.

- **Value recap:** what the account has actually built — boards, automations, agent runs — with real counts in slots (`{N} automations`), never guilt.
- **Pause offer** for high-engagement accounts, before the survey.
- **Route high-value or at-risk accounts** (by health score or MRR) to a person before the automated flow.

### Step 2 — reason (one question, 5–8 options, optional free text)

| Reason | Offer to show |
|---|---|
| Too expensive | Downgrade or right-size (fewer seats, smaller credit package), or a modest time-limited discount |
| Not using it enough | Pause, or a guided re-onboarding session |
| Missing a feature | Roadmap note + today's workaround; notify on launch |
| Switching to a competitor | A person (CS), not a coupon |
| Technical issues | Escalate to support before any offer — fix the problem |
| Temporary / seasonal | Pause |
| Business closed / changed | No offer. Acknowledge, ask for feedback |

Frame the question as "help us improve", neutral and diagnostic, and fast. Powtoon reports reason-matched offers plus a 30-day watch list with support outreach lifted its save rate from 8% to 13% [Reported — [Brightback case study](https://brightback.com/blog/powtoon-case-study), seen via search only].

### Step 3 — one reason-matched offer

- **Pause:** keep data, settings and integrations intact; auto-resume with advance notice. Canva offers "Pause for 3 months" with no charges and a reminder before resuming (annual plans only within 2 months of renewal) [Verified — [Canva help](https://www.canva.com/help/pause-annual-canva-plan/)]; Mailchimp offers 3- or 6-month pauses, at most two per 12 months [Verified — [Mailchimp help](https://mailchimp.com/help/close-an-account/)].
- **Downgrade / right-size:** frame it as "right-size your plan". Show what they *keep* first, then what changes, and make the way back up visible. Asana reportedly suggests a plan sized to actual seat usage instead of a fixed discount [Reported — [Userpilot](https://userpilot.com/blog/cancellation-flow-examples/)].
- **Discount:** test the minimum that works — in TouchNote's cancel flow, a 40% offer performed almost identically to 50% [Reported — vendor case study, [Chargebee](https://www.chargebee.com/customers/touchnote/)]. Show the amount saved; time-limit it.
- **Feature / roadmap:** the missing feature, its ETA if known, and the workaround teams use now.

### Step 4 — confirmation

**Must include:** the exact date access ends; what happens to data (retention period, export); the way back ("change your mind before {date}"). Canva lets users undo with "Stay on Canva Teams" until the period ends [Verified — [Canva help](https://www.canva.com/help/cancel-canva-plan/)].
**Must not include:** hidden confirmation steps, pre-checked re-subscribe boxes, or confusing language about what "cancel" means.

### Step 5 — after cancelling

A confirmation email with the end date and data-retention terms; an easy reactivation path in the app; a short win-back sequence (what's new → your data is still here → a time-limited return offer).

### Downgrade is not a mini-cancel

A customer who downgrades and stays is worth more than one who churns.

1. Show what they're losing — the features they actually use, not plan names. Omit what they've never used; don't manufacture fear.
2. Show what they keep — lead with it if the lower plan is solid.
3. Offer a delay — "stay on Pro until {date} while you decide".
4. Confirm the exact date the change takes effect.
5. State any **irreversible loss in the flow**, before confirm — e.g. Airtable permanently removes snapshots outside Free's two-week window on downgrade [Verified — [Airtable support](https://support.airtable.com/articles/3051898591)].

## Company teardowns

### Canva — the honest landing spot

**What they ship [Verified — [Canva help](https://www.canva.com/help/cancel-canva-plan/)].** Cancel plan → Continue cancellation → reason (required) → optional feedback → Cancel subscription. Paid features run to the period end, then the account moves to Free; designs, Brand Kit and shared folders are kept, and premium elements in designs become watermarked. Canva Free includes up to 20 AI uses a month [Verified — [Canva pricing](https://www.canva.com/pricing/)].
**Why it works.** Leaving feels like a step down, not an exit — the free plan is genuinely usable.
**Steal for monday.com.** Build the downgrade path as a product, not a cancel-flow afterthought.

### Notion — documented consequences, AI switched off not deleted

**What they ship [Verified — [Notion help](https://www.notion.com/help/plan-downgrade)].** Change plan → pick any lower plan → Continue → feedback → Downgrade; the consequences are documented per target plan. On downgrade, "all existing Custom Agents are switched off, but not deleted". Since May 13, 2025 full Notion AI sits on Business and Enterprise ([case: notion-2025-ai-bundling](cases.md#notion-2025-ai-bundling)), so leaving Business removes it. Whether the in-flow screen shows workspace-specific counts is [Teardown needed].
**Steal for monday.com.** "Switched off, not deleted" is the right promise for agents, AI Blocks and automations — if it's true, say it in the flow.

### Asana — right-size before cancel, but a notice window

**What they ship.** A cancel flow that reportedly offers a plan sized to the account's real seat usage [Reported]. Only the billing owner or admin can cancel; it takes effect at renewal; paid-feature projects lock but can be exported to CSV [Reported — via the cancellation benchmark; help-center URL to add]. The Subscriber Terms require 30 days' written notice to reduce seats or downgrade [Verified — [Asana terms](https://asana.com/terms/subscriber-terms)].
**Where it breaks.** A customer who decides late pays another term — at odds with click-to-cancel norms.
**Steal for monday.com.** The seat right-size offer maps directly onto monday's seat bundles; skip the notice window.

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture before citing in a review.

The honest headline: **none of the four runs an aggressive save flow.** They retain through landing spots (a free tier that keeps your data), partial downgrades, and pricing mechanics — not through discount offers. That's a regulatory advantage and a missed revenue opportunity at the same time. The steal is their clean mechanics; the opportunity is layering a reason-matched save step on top.

### At a glance

| | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Where cancel lives | [Teardown needed] | Admin → Settings → Plan → Cancel plan | Billing settings (Owner/Admin) | Settings → Billing → Cancel |
| Exit survey | [Teardown needed] | Yes — one cancellation reason, then confirm | [Teardown needed] | Not documented |
| Save offer | Not documented | Not documented | Reported: discount; other tiers / fewer members | None; no coupons by policy |
| Landing spot | Free plan (100 credits) | Starter (3 files/project, 1 project) | Free Forever (data kept, 60MB storage) | Free (history preserved) |
| Partial downgrade | Legacy plans kept | Seat downgrades per person | Drop AI add-on without cancelling plan | Max → Pro at period end |
| Access end | — | End of billing period | End of billing period, or immediately if chosen [Verified] | End of billing period; cancel 24h before renewal |

### Figma — clean mechanics, harsh landing

**What they ship [Verified].** Cancel from Admin → Settings → Plan → Cancel plan; Figma asks for a cancellation reason, then confirms. Paid features run until the end of the billing period, then the team drops to Starter: 3 Figma Design/Sites files and 3 files per other product in a project, one project per team. Over the limit, the team is locked and files become view-only until reorganized; files are not deleted. Published Sites are unpublished; Make apps stay live on the figma.site subdomain but lose custom domains. The Help Center gives a pre-downgrade checklist (move files to drafts, consolidate to one project).

**Why it works.** Nothing is deleted, and the "what happens" consequences are specific and documented. A one-question reason capture is the minimum viable exit survey.

**Where it breaks.** A locked team with view-only files reads as coercion to users who didn't read the checklist — forum threads show owners who feel forced to resubscribe. The consequence list lives in the Help Center, not in the cancel flow.

**Steal for monday.com.** Bring the consequence list *into* the flow, personalized: "3 of your boards use Pro automations — here's what happens to each on [date]." Put the export/reorganize actions on the confirmation screen, not in a help article.

### ClickUp — partial cancellation of the AI layer

**What they ship [Verified/Reported].** Cancelled workspaces stay on the paid plan until the period ends, then move to Free Forever; tasks, docs, and structure remain, premium features lock, storage drops to 60MB. The AI add-on can be cancelled separately from the workspace plan. The flow reportedly offers a discount, a different paid tier, or fewer members instead of full cancellation **[Reported]**. Owners and admins can cancel an add-on's auto-renewal in-app (Settings → Plans → Add-ons → Cancel) without changing the workspace plan, and downgrade the workspace from Billing at cycle end or immediately **[Verified — ClickUp help]**. There's a 30-day money-back guarantee **[Verified — [ClickUp pricing](https://clickup.com/pricing)]**.

**Why it works.** Separately cancellable AI is the most important retention mechanic in this set: a customer who doesn't see AI value can shed that layer and keep the core product.

**Where it breaks.** A 60MB landing spot is effectively unusable for teams.

**Steal for monday.com.** When the exit reason is AI-related ("AI credits too expensive" / "not using AI"), offer *reduce credit package* before *cancel plan* — shed the credit layer, keep seats. Makes the credit decision reversible and protects the seat base.

### Claude — the frictionless benchmark

**What they ship [Verified].** Settings → Billing → Cancel. Cancellation takes effect at the end of the billing period; access continues until then; Anthropic tells users to cancel at least 24 hours before the billing date to avoid the next charge. Upgrades apply immediately (prorated); Max → Pro downgrades take effect at the next cycle. Conversation history is preserved on downgrade. App-store subscriptions cancel through Apple/Google. No discount offers — the Help Center states Support can't issue one-off discounts.

**Why it works.** Two steps, plain language, exact timing rules stated upfront. This is what "compliant by default" looks like, and it builds the kind of trust that makes re-subscription easy.

**Where it breaks.** Zero save attempt. A Max 20x user cancelling because of cost gets no "switch to Max 5x" or "Pro + usage credits with a cap" option in the flow.

**Steal for monday.com.** Claude's mechanics as the compliance baseline (cancel reachable in two clicks from settings; exact end date; renewal cutoff stated), plus one right-size step: "Keep monday on a smaller package — {N} credits, ${price}/mo." One offer, one screen, skippable.

### Clay — retention through pricing mechanics

**What they ship [Verified].** Credit rollover up to 2x the monthly allocation reduces "we paid for credits we didn't use" churn after quiet months. On repricing, legacy plans were kept indefinitely for existing customers — no forced migration moment. Free plan exists as a landing spot. The cancel flow itself isn't publicly documented **[Teardown needed]**.

**Why it works.** The most common usage-product churn reason — "we didn't use what we paid for" — is addressed before cancellation, by rollover.

**Where it breaks.** A 2x rollover cap still wastes credits for seasonal teams running quarterly campaigns **[Reported]**.

**Steal for monday.com.** monday credits don't roll over (official for Notetaker; the general rule is still to confirm), so this doesn't apply today. If that changes, show the carried balance in the cancel intercept: "You have {N} unused credits — they carry into next month." An accumulated balance is a concrete loss anchor that seat-only SaaS doesn't have.

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
| Credit balance anchor | Balance, not guilt | "You have {N} unused AI credits in your account" (only if rollover exists) |
| AI-layer shed | Keep the core | "Keep your boards and seats — just switch to a smaller credit package" |
| Personalized consequence | Specific assets | "2 agents and 3 AI Blocks will stop running on [date]. Your boards stay." |
| Reversal | Make coming back easy | "Change your mind before [date]? One click and nothing changes." |

### Sources (checked 2026-09-24)

- Figma: https://help.figma.com/hc/en-us/articles/360046216313-Upgrade-or-downgrade-your-plan · https://forum.figma.com/report-a-problem-6/how-can-i-edit-my-files-after-not-resubscribing-49097
- ClickUp: https://help.clickup.com/hc/en-us/articles/6303101719831 · https://help.clickup.com/hc/en-us/articles/13673035695127 · https://clickup.com/pricing · https://legalclarity.org/how-to-cancel-your-clickup-subscription-step-by-step/ · https://consultevo.com/clickup-cancel-plan-guide/ · https://cancelmates.com/cancel/cancel-clickup-subscription · https://www.bardeen.ai/answers/how-to-cancel-clickup-subscription
- Claude: https://support.claude.com/en/articles/8325617-cancel-your-pro-or-max-subscription · https://www.ssdnodes.com/learn/cancel-or-downgrade-claude-plan · https://claudepricing.com/billing-cancellation · https://blog.nachonacho.com/best/claude-promo-codes/
- Clay: https://www.clay.com/blog/introducing-clay-pricing-3-0-the-most-flexible-credit-system-on-the-market · https://www.docket.io/resources/research/clay-pricing · https://lagrowthmachine.com/clay-pricing/

## Anti-patterns

| Anti-pattern | Why it fails | Who did it |
|---|---|---|
| Cancel hidden or obstructed | Regulatory risk (California, Germany; FTC case law) and lasting distrust | Amazon, Adobe — see [case: ftc-cancellation-enforcement](cases.md#ftc-cancellation-enforcement) |
| A save offer without "click to cancel" beside it | Violates California's ARL for consumer contracts since July 2025 | Generic dark-pattern flows |
| More than one "Are you sure?" | A confirmation maze | Common |
| The same offer regardless of reason | A discount won't save someone who isn't using the product | Common |
| No pause option | Loses the customers who only need a break | Common |
| Guilt-trip copy ("Don't leave your team behind") | Brand damage | Common |
| Maximum discount as the default | If a smaller offer works as well, the extra is lost margin (TouchNote: 40% ≈ 50% [Reported]) | Common |
| No downgrade — only stay or cancel, or a downgrade that goes straight to Free | Forces churn a right-sized plan could have prevented | Figma Organization/Enterprise downgrade via support only [Verified — [Figma help](https://help.figma.com/hc/en-us/articles/360046216313-Upgrade-or-downgrade-your-plan)] |
| Irreversible loss behind a downgrade, not stated in the flow | Re-upgrading can't restore it, so consent must come before confirm | Airtable snapshots [Verified] |
| An advance-notice window for self-serve reductions | Late deciders pay another term | Asana — 30 days' notice [Verified] |
| Early-termination fee hidden at signup | Bill shock at cancel; enforcement risk | Adobe (alleged) — see [case: ftc-cancellation-enforcement](cases.md#ftc-cancellation-enforcement) |

## monday.com-specific notes

- **AI Agents:** if the reason is "agents didn't deliver value", a discount won't help — offer a guided re-onboarding with a CS specialist.
- **Credits:** a customer who exhausted credits and didn't buy more didn't see enough value. The offer is a guided value moment and a smaller credit package — shed the credit layer, keep the seats — not a plan discount. Packages and tiers per [monday-context.md](../context/monday-context.md).
- **Seat right-size:** seats are sold in bundles of 3/5/10/15/20/25/30/40 ([monday-context.md](../context/monday-context.md)) — offer the next bundle down that fits actual usage.
- **Admin vs. IC:** in B2B the person clicking cancel may not be the economic buyer. For multi-seat accounts, route "request to cancel" to the admin.
- **Legal:** monday operates globally. California, Germany, the EU withdrawal rule, the UK regime from 2027, and Israeli consumer protection law all bear on cancellation for consumer customers. Legal review before shipping any cancel-flow change.

## Sources

Checked 2026-09-24 (AI-native set) and 2026-09-25 (everything else).

- Churnkey: https://churnkey.co/reports/state-of-retention-2025
- TouchNote (Chargebee): https://www.chargebee.com/customers/touchnote/
- Powtoon (Brightback): https://brightback.com/blog/powtoon-case-study
- California: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2863 · https://law.justia.com/codes/california/code-bpc/division-7/part-3/chapter-1/article-9/section-17601/
- Germany: https://dejure.org/gesetze/BGB/312k.html
- EU: https://www.klgates.com/thought-leadership/New-EU-Withdrawal-Button-Requirement-Practical-Implications-and-Recommendations-for-US-and-Global-Online-Sellers-7-8-2026 · https://www.iubenda.com/en/blog/the-new-online-withdrawal-function-what-eu-directive-2023-2673-means-for-your-business/
- UK: https://www.gov.uk/government/consultations/consultation-on-the-implementation-of-the-new-subscription-contracts-regime/outcome/government-response-to-consultation-on-the-implementation-of-the-new-subscription-contracts-regime-web-accessible-version · https://www.ashurst.com/en/insights/liftoff-for-the-cmas-consumer-direct-enforcement-powers/
- US: https://www.sidley.com/en/insights/newsupdates/2025/07/us-ftc-click-to-cancel-rule-struck-down
- Canva: https://www.canva.com/help/cancel-canva-plan/ · https://www.canva.com/help/pause-annual-canva-plan/ · https://www.canva.com/pricing/
- Mailchimp: https://mailchimp.com/help/close-an-account/
- Notion: https://www.notion.com/help/plan-downgrade · https://www.notion.com/help/upgrade-or-downgrade-your-plan · https://www.notion.com/releases/2025-05-13
- Asana: https://asana.com/terms/subscriber-terms · https://userpilot.com/blog/cancellation-flow-examples/
- Airtable: https://support.airtable.com/articles/3051898591
- Figma: https://help.figma.com/hc/en-us/articles/360046216313-Upgrade-or-downgrade-your-plan
