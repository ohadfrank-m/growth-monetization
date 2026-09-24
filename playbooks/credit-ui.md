# Credit / consumption UI — CRO playbook

Surface type 5: running low on credits, credit meter, metering dashboard, top-up flow. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

The highest-priority surface type for monday.com given the AI Agents launch, and the one with the most novel UX problems in this plugin — most companies don't yet have a settled pattern for this.

This file was previously forked across two skills with different benchmarks and different best-in-class examples for the same surface. It's merged here as the single source; don't re-fork it.

## The credit psychology problem

Credits create a different anxiety than seat limits. Users fear *running out mid-task* more than they fear hitting a hard cap. Design for the anxiety state, not the depleted state. Tier upgrade triggers (a blocked-and-frustrated moment — see [upgrade-triggers.md](upgrade-triggers.md)) and credit depletion (an anxious, mid-task moment) require different design approaches even though both are "usage limits."

## When this surface appears

- **Warning state:** credit balance drops below warning threshold (e.g., 20% or 50 credits remaining)
- **Depletion state:** credit balance reaches 0 mid-session or mid-task
- **Depletion mid-task:** balance hits 0 while an AI agent is actively running — highest-risk moment
- **Credit meter (persistent):** visible in dashboard or sidebar at all times when credits are < 100% or < threshold
- **Top-up flow:** user initiates a credit purchase (self-serve or admin)
- **Post-top-up confirmation:** credits added, task can resume

## The always-on credit meter

The persistent meter is the single most important credit surface — it sets the mental model before any upgrade moment.

- **Placement:** visible in the primary workspace chrome, not buried in settings. If a user has to hunt for their balance, every downstream depletion feels like a surprise.
- **Always translate:** never show a bare number. "820 credits" alone is meaningless. Pair with task translation: "820 credits ≈ ~160 agent actions." The translation is the product's job, not the user's math.
- **State progression:** healthy → warning → critical → depleted (color shift green → yellow → orange → red). The color shift is the ambient early warning; it should change *before* any modal fires.
- **Hover/tap detail:** reveal burn context — "You've used 340 credits this week, mostly on document summaries."
- **Scoring note:** a meter that shows a number with no translation is an automatic value-clarity ≤2 on the design-reviewer rubric.

## Burn-rate forecasting

Forecasting is what converts passive awareness into proactive top-up. It's the highest-leverage credit UI pattern.

- **Show the projection, not just the balance:** "At your current rate, you'll run out in ~4 days." Rate-based framing drives top-ups far more than a static remaining count.
- **Accuracy matters more than precision:** a forecast that's visibly wrong destroys trust worse than no forecast. Use a conservative range ("~3–5 days") over a false-precise single number if the data is noisy.
- **Tie the forecast to a moment:** "…which means you'll run out before your Friday report." Anchoring the projection to a known deadline sharply increases action.

## Credit-to-task translation

The difference between a meter users understand and one they resent.

- Every credit-denominated surface — meter, depletion, top-up, pricing page, trial — must express credits in tasks the user recognizes.
- Translation must be **honest and stable:** if "1 agent action ≈ 5 credits" on the pricing page but the meter implies a different rate, trust breaks. One rate, everywhere.
- Prefer the user's own recent actions as the unit ("≈ 40 more document summaries at your usage") over abstract catalog actions.

## Warning → depletion progression

**Proactive nudge (30–40% remaining):** non-blocking banner or sidebar card. Framing: "You're getting great value from AI — here's how to keep the momentum." Show what credits are being used on — makes the value tangible.

**Urgent nudge (10–15% remaining):** more prominent, persistent, but still dismissible. Specific: "You have ~X AI actions left. After that, [specific thing] stops working." Include a preview of what buying credits unlocks.

**Depleted state:** the most sensitive moment — user is blocked. Never just show an error. Show what stopped, why, and how to fix it immediately. Provide a one-click "get more credits" path with pre-filled quantity.

Best-in-class pattern for the warning state — **Notion AI**: running-low banner lives in the editor sidebar, doesn't interrupt writing. Shows "X AI responses remaining this month." One-click "Get more" button. Non-blocking, contextual.

Best-in-class pattern for progressive states — **HubSpot AI**: three states — healthy (no meter visible), warning (meter appears at 20%), critical (meter turns red + pulse animation), each with progressively stronger messaging. Users aren't surprised by depletion; the warning state gives them time to act.

Best-in-class pattern for depletion messaging — **Intercom Fin**: leads with the task, not the credits — "Your AI conversation agent has paused — you've run out of AI credits", not "You have 0 credits." Users understand what stopped in terms they care about.

## Top-up flow

The purchase moment when a user chooses to add credits rather than upgrade a plan.

- **Default the recommended quantity:** pre-select the "best value" tier — most users anchor to the default. Don't present a blank quantity field.
- **Show per-credit price at each tier** so volume value is legible; label the volume tier "best value" explicitly.
- **Show the plan-upgrade alternative alongside:** "Or upgrade to Pro — includes X credits/month at a lower effective rate." A pure top-up path hides the often-better subscription option.
- **One-click, no re-entry:** payment on file should mean top-up is a single confirm. Re-entering card details at the depletion moment is a conversion killer.
- **Confirm what they just bought in tasks:** "Added 2,000 credits ≈ ~400 agent actions." Close the loop in the same unit.

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
Critical elements: three package options (anchors mid-tier choice), task translation on every option, "resume" in the CTA, admin path as secondary.

## Agentic mid-task depletion (critical experience)

If an agent exhausts credits mid-task, this is the highest-stakes credit moment in the product.

- **Never fail silently.** Save task state, explain what happened in one line, and offer an immediate resume path.
- **Non-blocking where possible:** an inline "you're out of credits — top up to let the agent finish" beats a full-screen error that discards the in-progress work.
- **Preserve the artifact.** Whatever the agent produced up to the depletion point must survive. Losing partial work turns a top-up moment into a churn moment.
- **Post-purchase resume:** auto-resume or an explicit "Resume task" CTA — a user who has credits but doesn't know how to continue is a support ticket waiting to happen.

```
[Inline banner in agent run interface:]
[⚠️] "Your AI agent has paused — you're out of credits"
[Subtext: "{Agent name} stopped at step {N}. Top up to continue where you left off."]
[CTA: "Top up credits — {package size} for ${price}"]  [Secondary: "Notify admin"]
[Small: "Your work is saved"]
```

## Dual-gated trial display (monday-specific)

The 1,500-credit dual-gated trial structure gates on both time and credits. The UI must make **both** gates legible without creating double anxiety.

- Show the binding constraint — whichever runs out first. If credits will deplete before the trial clock, lead with credits; if time is shorter, lead with days.
- Don't show two racing countdowns with equal weight — that reads as a trap. One primary constraint, one secondary line.
- On the tighter gate, pair with the value recap and the clear post-trial path (buy credits / pick a plan).

## Benchmarks

*Directional only — these figures pre-date the evidence-tag standard and carry no source. Don't cite them as fact in a review; the sourced material is in the AI-native reference set below.*

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Credit depletion → purchase CVR | <10% | 15–25% | 30%+ |
| Credit warning (30% left) → purchase CVR | <5% | 8–12% | 18%+ |
| Forecast-shown → proactive top-up CVR | <5% | 8–14% | 20%+ |
| Top-up flow completion (payment on file) | <40% | 55–70% | 80%+ |
| Meter comprehension (users who can state what a credit buys) | <30% | 50–65% | 80%+ |
| Mid-task depletion → resume (vs. abandon) | <30% | 45–60% | 75%+ |

## Best-in-class metering references

*Pre-dates the evidence-tag standard — the patterns are sound, but any figures here are unsourced. Tagged teardowns are in the AI-native reference set below.*

**OpenAI API dashboard** — burn-rate projection ("at this rate, runs out in X days") is the model for forecasting. Rate framing drives top-ups better than raw balance.

**Anthropic / Claude usage** — two-window meter (session + weekly) with reset times, and pay-to-continue under a spending cap. Full teardown in the AI-native reference set below.

**Vercel** — usage dashboard with per-resource meters and clear overage pricing shown *before* the overage happens; no surprise bills.

**Linear (cycle capacity)** — turns invisible consumption into an always-present, low-anxiety signal, normalizing awareness before any limit is hit.

## Credit pricing presentation

- Show per-credit price at each tier to enable comparison.
- Highlight the "best value" option (volume pricing) — anchors toward higher purchase.
- If upgrading to a plan includes credits, show the effective credit cost vs. buying standalone.
- Avoid presenting credits purely as a number without context — "500 credits" means nothing without "≈ 500 AI actions."

## Anti-patterns

| Anti-pattern | Specific failure | Fix |
|-------------|-----------------|-----|
| Bare credit number | "500 credits" with no task translation | Always add "≈ 500 AI actions" |
| Hard stop mid-agent-task | Task fails, state lost | Save state, pause task, offer resume |
| Full-screen blocking modal in agentic flow | Breaks flow, scary UX | Inline banner at warning threshold |
| No IC → admin path | IC dead-ends, admin never knows | "Notify admin" button always present |
| Post-purchase no resume path | User has credits, doesn't know how to continue | Auto-resume or explicit "Resume task" CTA |
| Credit expiry not communicated | Surprise at month end | Show expiry prominently if credits don't roll over |

## AI-native reference set: Clay · Figma · ClickUp · Claude

Mandatory reference set for every playbook — and the most important one for this surface. Evidence tags: **[Verified]** vendor docs, **[Reported]** third-party, **[Teardown needed]** capture before citing in a review.

### At a glance — the credit UI stack, pattern by pattern

| Pattern | Clay | Figma | ClickUp | Claude |
|---|---|---|---|---|
| Pre-action cost estimate | **Best-in-class** — total, per-column, rows affected | Published per-task ranges in Help Center | — | — |
| Big-spend warning | Yes — warns when a run uses a large share of monthly budget | — | — | — |
| Persistent meter | Credit dashboard (time-series balance) | User + admin usage views, CSV export on Org/Ent | [Teardown needed] | Settings → Usage: session + weekly bars with reset times |
| Warning before wall | Via budget warning | [Teardown needed] | [Teardown needed] | "Approaching 5-hour limit" |
| Depletion behavior | Auto top-up keeps runs going | Paid AI off until reset; free AI stays on; daily cap on Starter/View | Automatic AI features pause | Blocking message + reset time |
| Continue-past-limit | Auto top-ups (admin, card on file) | Shared pool + PAYG to a spend limit | Credit packs ($10 / 10k) | Usage credits at API rates, monthly cap, auto-reload, alerts |
| Rollover | Up to 2x monthly allocation | None | None (trial credits don't reset) | Usage credits generally don't expire |
| Admin controls | Auto top-up threshold + amount | Pool purchase; per-user caps not available (as of Mar 2026) | Workspace-level | Spend caps: org / seat tier / member, MTD spend column |

### Clay — cost transparency before the spend

**What they ship [Verified].**
- **Pre-run estimate:** when a column run would trigger downstream columns, Clay shows total estimated credits, a per-column breakdown, and the number of rows affected. It applies to manual runs *and* automated ones (scheduled imports, auto-update).
- **Variable pricing honesty:** variable-cost models show a per-row estimate marked with a tilde (~); final cost is set after the run.
- **Budget warning:** a warning fires before a run that would use a significant portion of the workspace's monthly credit budget.
- **History:** Overview tab charts credit balance as a time series so you can see when credits were spent; CSV export on all views.
- **Auto top-ups:** admins on paid self-serve plans set a trigger threshold (at least 15% of plan credits) and an amount (min 250 credits); charged to the card on file so a run in progress keeps going instead of stopping.
- **Rollover:** unused credits roll over up to 2x the monthly allocation. One-time top-ups carry a 30% premium.

**Why it works.** Clay moves the anxiety from *after* the spend to *before* it. The user commits to a known cost for a known number of rows — the same mental model as a checkout. Auto top-up solves mid-run depletion structurally.

**Where it breaks.** Failed lookups still consume credits (paying for three providers that return nothing) — the most-cited trust complaint in third-party coverage. Estimates are non-binding for variable models.

**Steal for monday.com.** This is the pattern for agents and AI Blocks:
- Before an AI Block runs on a column: "~[X] credits · [N] items · ≈[Y]% of this month's balance" with Run / Run on 10 items first.
- Before scheduling a recurring agent: "~[X] credits per run · [Z] runs/month ≈ [total]."
- Big-run warning above a threshold (e.g., >20% of remaining balance).
- Auto top-up for admins, framed as "keep agents running."
- Decide explicitly whether failed/empty AI outputs consume credits — and say so in the estimate.

### Figma — per-person allowance, graceful degradation, pooled rescue

**What they ship [Verified].** Credits belong to individual seats, reset monthly, no rollover, not shareable. Starter and View seats also have a 150-credit daily cap. When credits run out, paid AI features are disabled until the next reset while free features stay available, and an admin-purchased shared pool acts as a buffer (subscription at a better rate + pay-as-you-go up to a spend limit). Users and admins can track usage; Org/Enterprise admins export CSV history. Per-user caps weren't available at enforcement (March 2026) **[Verified at the time — recheck]**.

**Why it works.** Free AI features staying live means depletion degrades the product rather than breaking it. The shared pool is the right fix for per-seat limits: the heavy user draws from the account, not from a colleague.

**Where it breaks.** At enforcement (Mar 18, 2026) users reported running out within hours of real Figma Make work; the forum thread is a case study in launching limits on a feature people had used unmetered. Model selection changes cost up to ~8x for the same action **[Reported]**, and the meter can't warn about that unless cost is shown at model choice.

**Steal for monday.com.** (1) Classify every AI capability as credit-consuming vs. free (monday already keeps an AI Feature Catalog — per [monday-context.md](../context/monday-context.md)) and keep the free ones live at zero balance. (2) If a cheaper model/mode exists, show the credit delta at the selector. (3) Never enforce a new limit without a comms ramp and a ready purchase path (Figma had one week between add-on launch and enforcement — take more).

### ClickUp — credits under a seat subscription

**What they ship [Verified].** AI Super Credits power automatic AI features (Super Agents, Autopilot Agents, AI Fields, AI Cards). Allowances: Brain 1,500 per user/mo, Everything AI 5,000 per user/mo; Free 500 per workspace and paid-without-AI 1,000 per user, both one-time. When trial credits run out, automatic features pause until an add-on or credit pack is bought. Extra credits $10 per 10,000. Subject to a fair-use policy.

**Why it works.** Splitting "chat/writing = unlimited in the seat" from "automatic agents = metered" is a clear mental model: humans typing are flat-rate, machines running are metered.

**Where it breaks.** Automatic features fail quietly — a paused AI Field looks like missing data. Seat price + credits stack makes the bill hard to predict (the top theme in third-party reviews).

**Steal for monday.com.** Adopt the "interactive = included, autonomous = metered" split in how credit UI *explains* consumption, even if pricing differs. For any autonomous feature, the paused state is designed first: inline marker on every affected item, a board-level banner, and an owner notification.

### Claude — the two-window meter and the pay-to-continue exit

**What they ship [Verified].**
- **Meter:** Settings → Usage shows progress for the five-hour session and the weekly limit, each with its reset time.
- **Progression:** "Approaching 5-hour limit" warning → blocking message stating when usage is available again.
- **Continue path:** paid plans can turn on usage credits — billed separately at API rates, under a monthly spending cap you set (or unlimited), with auto-reload below a threshold and alerts when approaching limits. Real-time consumption and month-to-date spend are shown in Settings → Usage.
- **Team:** owners set limits org-wide, by seat tier, or per member; a member who hits their cap is paused until reset.
- **Education:** Help Center explains what burns usage (long threads, higher effort, attachments) and what doesn't (reused project content is cached).

**Why it works.** The reset time turns depletion into a wait-or-pay decision instead of a dead end. Spending caps make pay-as-you-go safe to enable. Teaching users *why* usage burns reduces "the limits are unfair" sentiment.

**Where it breaks.** Two stacked windows are harder to reason about than one balance. Third-party reports say a promotional credit claim enabled usage credits by default for some users, who were then charged past plan limits **[Reported]** — continue-past-limit billing must always be an explicit opt-in.

**Steal for monday.com.** (1) Show the *refill date* on every depletion surface. (2) Top-up with a monthly cap as the default admin setting. (3) A "why did this cost so much?" explainer on the usage page, per capability. (4) Overage is always opt-in; the admin sees a confirmation of the cap they set.

### Copy bank — credit UI

| Moment | Pattern | Example for monday.com |
|---|---|---|
| Pre-run estimate | Cost + scope + share of balance | "~450 credits · 300 items · about 15% of your remaining balance" |
| Big-run warning | Name the share | "This run uses about half of what's left this month. Try it on 10 items first?" |
| Persistent meter | Balance + translation + refill | "2,140 credits left ≈ 40 agent runs · refills [date]" |
| Forecast | Rate + deadline | "At this pace you'll run out around [date], before your cycle refills" |
| Depleted (interactive) | What stopped + resume | "Sidekick needs more credits to answer — top up or wait until [date]" |
| Depleted (autonomous) | Where it stopped | "AI stopped updating 'Sentiment' on 120 items · Top up to resume" |
| Overage opt-in | Cap is the headline | "Keep agents running past your balance — up to $[cap]/month. You'll get an alert at 80%." |

### Sources (checked 2026-09-24)

- Clay: https://university.clay.com/docs/credit-usage · https://university.clay.com/docs/actions-data-credits · https://www.clay.com/blog/introducing-clay-pricing-3-0-the-most-flexible-credit-system-on-the-market · https://www.cleanlist.ai/blog/2026-03-12-clay-pricing-changes-2026
- Figma: https://help.figma.com/hc/en-us/articles/33459875669015-How-AI-credits-work · https://www.vibecodingacademy.ai/blog/figma-ai-credits-everything-you-need-to-know · https://forum.figma.com/share-your-feedback-26/figma-make-ai-credit-limits-not-feasible-51713/index4.html · https://www.appshot.app/posts/2026-07-09-figma-ai-credits-explained/
- ClickUp: https://help.clickup.com/hc/en-us/articles/20686299081879-ClickUp-Brain-AI-feature-availability-and-limits · https://www.rock.so/blog/clickup-pricing
- Claude: https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans · https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans · https://www.ai-toolbox.co/claude-management-and-productivity/claude-usage-limits-2026 · https://ccforeveryone.com/guides/claude-code-limits-and-pricing

## monday.com-specific notes

- AI credits are new (May 2026 launch) — users have no prior mental model. The first-ever credit depletion experience must be educational, not just transactional.
- New users (14-day trial) have an urgency lever (time). Credit UI should reinforce "you're getting value now — don't let it stop."
- Existing users (credit balance, no time limit) have no urgency lever. Must create desire, not FOMO — show value received, not scarcity.
- Agent mid-task interruption: if a Sidekick agent runs out of credits mid-task, this is a critical experience. Must save task state, explain what happened, and provide an immediate path to resume. Never just fail silently.
- Admin vs. end user: in B2B, end users hit credit walls but admins hold the credit wallet. Every credit-facing surface needs a "notify your admin" path that generates an actionable admin notification, not a dead end.
