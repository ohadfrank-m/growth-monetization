# Experiment design — making success metrics decision-grade

Read this in the synthesis phase, before writing the Measurement plan in `05-requirements.md`. It converts the spec's **Success metrics** table ([templates/surface-spec.md](../../../templates/surface-spec.md)) into a test someone can run and a decision nobody has to argue about afterwards. Every monday number (baseline, traffic, prices, credit amounts) is a `{slot}` filled by the data owner or cited from [monday-context.md](../../../context/monday-context.md). Never estimate one here.

Base rate to keep in mind: at Microsoft, only about one-third of well-designed experiments improved the metric they targeted [Verified — Kohavi, Crook & Longbotham 2009]. The default outcome is flat, so the plan decides up front what happens on flat.

## 1. Test, or ship?

| Change | Default | Why |
|---|---|---|
| Copy, layout, CTA on a live surface; no price, policy or entitlement change | A/B test if the MDE is reachable within `{max_runtime}` weeks; otherwise ship and watch guardrails pre/post against a holdout | Low risk, reversible |
| Required fix: legal/compliance (cancel ease, price disclosure), broken state, accessibility | Ship. Don't test | You can't hold back a required change from a control group |
| Trigger timing, thresholds, frequency caps (credit 80/95%, trial phase windows) | Test | [credit-ui.md](../../../playbooks/credit-ui.md) and [trial-flows.md](../../../playbooks/trial-flows.md) call these conventions, not tested optima |
| Offer, discount, credit grant | Test against a holdout, always (§6) | Redemption doesn't show incrementality ([promotions.md](../../../playbooks/promotions.md)) |
| List price, package, credit allotment, seat minimums | **No randomized concurrent price test in the same market by default.** Sequence: willingness-to-pay research → new-cohort or geo rollout → holdout. Legal review before any variant shows a different price | Fairness, B2B leakage, legal (below) |
| New surface, no baseline | Ship to `{rollout_%}` with a holdout; the first `{N}` weeks become the baseline | You can't size an MDE without a baseline |

**Why price A/B tests are different**
- **People compare prices, and they notice.** Amazon's five-day random DVD price test in 2000 ended with an apology, refunds to 6,896 customers (average $3.10), and a promise to charge every buyer the lowest tested price in any future test [Verified — Amazon press release]. For monday, that becomes a rule: decide before launch whether test-arm buyers keep their price or get moved to the lowest one, and write the decision into the plan.
- **B2B leakage.** Colleagues at one company see the logged-out pricing page on different cookies, and sales quotes list price. Randomize by company (account or email domain) or by geo, never by visitor, when the variant is a price.
- **Existing customers.** Never randomize a price increase across existing customers. That's a migration, and [promotions.md](../../../playbooks/promotions.md) ("A price change is a promotion problem") owns it. Test new pricing on new cohorts before migrating existing ones [Reported — Sequence, Kyle Poyar workshops]. Geo tests (markets with similar buyer behavior) are the other common route [Reported — Growth Unhinged, seen via search only]. Geo tests have few units, so read them as quasi-experiments (difference-in-differences), not as A/Bs (inference).
- **Legal — reviewed by legal: not yet.** The EU Consumer Rights Directive, as amended by the Omnibus Directive 2019/2161 (Art. 6(1)(ea)), requires telling consumers when a price is personalised by automated decision-making [Reported — Leiden Law Blog; EUR-Lex not read]. New York GBL §349-a requires the disclosure "THIS PRICE WAS SET BY AN ALGORITHM USING YOUR PERSONAL DATA" for personalized algorithmic pricing, where "consumer" means a natural person buying for personal use [Verified — NY Senate]. Legal has to decide whether a randomized test arm counts. Until it does, the plan carries an Open item (Legal — name TBD) marked as a ship blocker.
- **Willingness-to-pay methods set the range. They don't set the price.** Van Westendorp's price sensitivity meter (1976) asks four open price questions (too cheap / cheap / expensive / too expensive) [Verified — `pricesensitivitymeter` docs]. It suffers hypothetical bias: stated prices come out higher than real ones [Reported — Berman, Lenny's Newsletter]. Gabor–Granger (1966) asks buy/no-buy at set prices [Verified — Economica citation]. It reportedly gives systematically lower estimates, and conjoint gives relative WTP closer to real choices [Reported — Berman]. Use a survey to pick 2–3 price points, then run the rollout test on those.

## 2. Hypothesis — fill every slot

```
Because {evidence: review row R{v}.{n} / benchmark / data point + source},
we believe {change} on {surface} for {cohort: new | existing; IC | admin; tier}
will move {primary metric} from {baseline} by at least {MDE, relative %} within {window} days of first exposure,
because {mechanism: the reason to act from 01-spec.md}.
We will not ship if {guardrail} worsens by more than {tolerance}.
Unit: {account}. Arms: {control, variant}. Allocation: {50/50}. Decision owner: {name or role — name TBD}.
```

One primary metric per test, chosen in advance: Kohavi's OEC principle [Verified — experimentguide.com]. Secondary metrics explain the result but never decide it. Every added metric raises the false-positive rate, so limit them or correct for them (Optimizely applies Benjamini–Hochberg FDR to secondaries and keeps the primary separate) [Verified — Optimizely; GrowthBook].

## 3. Primary metric by surface — revenue, not clicks

The unit is the **account**: monday plans, seats and credit pools belong to the account ([monday-context.md](../../../context/monday-context.md)). Prefer a binary, near-surface form of the revenue event (converted yes/no within a window), because revenue per user is heavy-tailed and much noisier [Verified — Eppo]. Report net ARR as a secondary with outliers winsorized (clipped) at `{p99}`.

| Surface | Primary (per exposed account) | Secondary | Guardrails beyond §4 |
|---|---|---|---|
| Pricing page | Paid conversion within `{N}` days of first pricing-page view | Plan mix, annual share, net new ARR per exposed account | Refunds within `{N}` days; sales-assisted lead share (leakage into sales) |
| Paywall / feature gate | Paid upgrade within `{N}` days of first gate hit | Gate → checkout start; trial starts from the gate | Free→paid retention at `{D30}`; feature abandonment after the gate |
| Promotion | **Incremental** net ARR per *eligible* account vs holdout, net of discount cost, at `{90}` days | Redemption rate (diagnostic only) | Discounted-cohort retention at 90 and 180 days ([promotions.md](../../../playbooks/promotions.md)); full-price conversion in the holdout |
| Tier upgrade (upgrade trigger) | Upgrade within `{N}` days of the limit hit | Net expansion ARR per exposed account | Downgrade within `{60}` days; admin-notify complaint rate |
| Credit UI (meter, warning, depletion, top-up) | Top-up or package purchase within `{N}` days of reaching the warning state | Share of purchased credits burned within 30 days of top-up; time to resume the stopped task | Weekly AI usage per account (fear of running out suppresses use); credit-related tickets |
| Cancellation | Net retained ARR per cancel-starter at `{90}` days = save rate × 90-day retention of saved accounts | Save rate at 30 days; offer mix | Re-cancel rate; complaints/chargebacks; median time-to-cancel stays ≤ `{control}` (legal) |
| Downgrade | Retained ARR per downgrade-starter at `{90}` days (downgrade vs cancel mix) | Seats and credit package kept | Churn at 90 days of downgraders |
| Trial | Trial-to-paid (Free→Pro, the squad primary per [monday-context.md](../../../context/monday-context.md)) within `{N}` days of trial start | Activation milestone rate (one milestone, from [trial-flows.md](../../../playbooks/trial-flows.md)) | Month-2 paid retention (the M1 loss window); refunds |

Set the window `{N}` from the data: the day by which `{80}%` of historical conversions in control have happened. A window shorter than the conversion lag measures timing shifts, not lift.

## 4. Guardrails — a breach blocks ship

Standard monetization set. Pick the 3–5 that the change could plausibly hurt, because each extra guardrail adds false alarms [Verified — GrowthBook]:
refund/credit-refund requests · downgrades within `{60}` days · billing and credit support tickets (tagged) · credit-exhaustion complaints · churn at next renewal (§6 when it falls outside the test) · NPS/CSAT on the surface's follow-up survey · weekly AI usage (OKR 2 exposure) · page/modal error rate and load time.

- **Breach** = the guardrail is worse than control by more than its pre-registered tolerance `{T}`, at `{α_guardrail}`. A breach blocks ship. It isn't traded off against primary lift. Anyone who wants to override it takes it to the decision owner in writing.
- **Underpowered guardrails** (tickets, refunds: rare events): state their power in the plan. If a guardrail can't be powered inside the test, move it to the post-launch holdout (§6) with a rollback trigger (`{count}` events in `{days}`).
- Monitor guardrails with a sequential method so harm can stop the test early. That's the one place early stopping is allowed on a fixed-horizon test (§5).

## 5. Sample size, MDE, runtime

**Formula (two arms, binary primary, α = 0.05 two-sided, power 80%):**
`n per arm = (z₁₋α/₂ + z₁₋β)² · [p₁(1−p₁) + p₂(1−p₂)] / δ²`, where (1.96 + 0.84)² ≈ 7.85, p₁ is the baseline, p₂ = p₁ + δ, and δ is the absolute MDE.
Rule of thumb: `n ≈ 16 · p(1−p) / δ²` [Verified — Evan Miller; his calculator does the exact version].

**Worked example — slots, then a generic illustration (not monday data):**

| Slot | Value |
|---|---|
| Baseline `p₁` (primary, control, last `{8}` full weeks) | `{p₁}` — Data — name TBD |
| Relative MDE `r` (smallest lift worth shipping, from cost or ARR impact) | `{r}` → δ = p₁·r |
| n per arm | `{n}` from the formula |
| Eligible accounts per week × allocation share | `{E}` × `{a}` |
| Runtime | ⌈ n·arms / (E·a) ⌉ weeks, rounded up to whole weeks, min 2, **plus** the `{N}`-day conversion window before readout |

Illustration: p₁ = 5%, r = 10% → δ = 0.5 pp → ≈ 31,200 accounts per arm (rule of thumb: 30,400). Halving the MDE quadruples the sample. Kohavi et al. put it as 10× the sensitivity needing 100× the users [Verified — KDD 2013]. The spec's "Target" must be ≥ the MDE the traffic supports. A target below it is a hope, not a test.

**B2B-specific**
- **Small samples.** Kohavi et al. put the general floor at "at least thousands of active users" [Verified — KDD 2013]. If `{runtime}` exceeds `{max_runtime}`, don't run a test that can't answer. Instead: make the change bolder (a bigger MDE), move the primary closer to the surface, pool surfaces with the same trigger, or ship with a holdout.
- **Randomize the account, not the user.** When seats share one plan and one credit pool, split users of one account would see different offers for the same purchase. Assign by account ID [Verified — Statsig custom unit IDs]. If a per-user metric is analyzed under account randomization, don't use naive per-user standard errors. Users in one account are correlated. Use the delta method or cluster-robust SEs [Verified — Deng, Knoblich & Lu 2018; Statsig normalized metrics]. The sample inflates by the design effect `1 + (m−1)·ICC` (m = users per account) [Verified — cluster-trial literature, e.g. Cochrane/CASRAI].
- **Long conversion lags and annual billing.** An annual account's renewal falls outside any test. Either hold a long-term holdout to the first renewal (§6), or decide on a validated surrogate: a short-term index shown to predict the long-term outcome [Verified — Athey, Chetty, Imbens & Kang 2019]. An unvalidated proxy is just a secondary metric.
- **CUPED** (adjusting for each account's pre-period metric) cut variance by about 50% at Bing [Verified — Deng et al. 2013]. It works for existing-customer surfaces (credit UI, tier upgrade, cancellation, downgrade). It does nothing for new signups with no history (pricing page, trial), and it needs an autocorrelated metric [Verified — Statsig CUPED docs].
- **Sequential vs fixed horizon.** Checking a fixed-horizon test daily and stopping on significance can push the false-positive rate from 5% to 26.1% [Verified — Evan Miller]. Pre-commit to a fixed horizon for the primary. Use sequential or hybrid methods for guardrail monitoring, or when stopping early is worth wider intervals (Eppo's hybrid runs about 10–15% wider). Avoid fully sequential designs when the sample is constrained [Verified — Eppo].

## 6. Holdouts and incrementality

- **Promotions:** always hold out `{h}%` of the *eligible* audience with no offer. Report incrementality (offer arm minus holdout) net of discount cost. Redemption rate is a diagnostic, never the result ([promotions.md](../../../playbooks/promotions.md)).
- **Long-term holdout for trial and credit changes.** Keep `{h}%` of accounts on the old experience for `{months}` to catch renewal churn, cumulative effects, and novelty wearing off. Statsig's default is 1–2% for 3–6 months [Verified — Statsig holdouts]. That's consumer scale. At B2B volumes, size the holdout with the §5 formula against the renewal metric. Holdout metrics use lookback windows, not conversion windows [Verified — GrowthBook holdouts].
- A shipped test result isn't the long-run effect. Short-term effects often fail to predict long-term ones [Verified — Hohnhold, O'Brien & Tang 2015], so a holdout is what checks the ship decision.

## 7. Novelty, primacy, seasonality — minimum runtime

- **Run whole weeks** (7, 14, 21 days), never partial ones: day-of-week mix biases the result [Verified — Statsig; GrowthBook: at least 1–2 weeks]. B2B weekday/weekend usage makes this stricter (inference).
- **Novelty:** a 2.07% lift from an Edge coach mark vanished after the first visit [Verified — Dmitriev et al. KDD 2017]. New banners and modals get the same scrutiny. **Primacy:** some effects grow as users learn, e.g. a credit meter users start to trust (inference, by analogy to the paper's ads-blindness example). Check both by plotting the treatment effect by week since first exposure. Extend the test if the effect is still trending.
- **Seasonality:** don't let a readout span a known shock: a monday price or packaging change, a promotion in market, holiday weeks, or quarter/fiscal-year-end buying (inference for B2B). If it can't be avoided, list it as a threat in the plan.
- **Trust checks before reading anything:** a sample-ratio-mismatch (SRM) chi-square test on assignment counts. Kohavi's example: 50.2% vs 50.0% on about 1.6M users (p = 1.8e-6) means "stop analyzing" [Verified — Kohavi pitfalls deck]. SRM "most of the time" implies severe selection bias [Verified — Dmitriev et al.]. **Twyman's law:** an effect far above the MDE is presumed to be a bug until instrumentation, SRM and segments are checked [Verified — Dmitriev et al. §5.12].

## 8. Ship criteria — decide before launch

| Primary result (fixed horizon, CI) | Guardrails | Trust checks | Decision |
|---|---|---|---|
| Significant positive, point estimate ≥ `{ship_threshold}` | No breach | SRM pass, effect stable by week | **Ship**. Holdout per §6 |
| Significant positive | Any breach | Pass | **Don't ship.** Diagnose the breach; iterate |
| Flat (CI spans 0) | No breach | Pass | Ship **only** if pre-registered as "ship on flat" (clarity, compliance, cost reduction); otherwise keep control |
| Significant negative | Any | Pass | **Kill.** Record the learning |
| Any | Any | SRM fail, or Twyman flag unresolved | **Invalid.** Fix and rerun; no partial reads |
| Positive but decaying week over week | No breach | Pass | **Extend** `{weeks}`, then re-apply this table |

## 9. Into `05-requirements.md` — the Measurement plan block

Synthesis fills this from `01-spec.md` → Success metrics, the latest review, and this file. Every `{slot}` still open becomes an Open item (owner: Data/Analytics — name TBD, or Legal for price tests), and the Build order gets the instrumentation rows.

```markdown
## Measurement plan

**Decision:** {test | ship + holdout | ship, no test — reason (§1)} · **Decision owner:** {name / role — name TBD}
**Hypothesis:** {§2 template, filled}

| Role | Metric | Definition (event, window, unit) | Baseline | MDE / tolerance | Source |
|------|--------|----------------------------------|----------|-----------------|--------|
| Primary | {§3 row} | {event} within {N} days of first exposure, per account | {p₁ — pending: Data} | ≥ {r} relative | 01-spec Success metrics |
| Secondary | {…} | {…} | {…} | — (diagnostic) | |
| Guardrail | {…} | {…} | {…} | breach if worse by > {T} at {α} | |

**Design:** unit {account} · arms {n} · allocation {…} · n per arm {…} · runtime {W} whole weeks + {N}-day window · variance reduction {CUPED | none — new users} · analysis {fixed horizon; guardrails sequential}
**Holdout:** {h}% for {months} on {metric} — or "none: {reason}"
**Threats:** {novelty / seasonality / leakage / legal} → {mitigation}
**Ship table:** §8, with {ship_threshold}, {T}, and "ship on flat: yes/no" filled in
```

Instrumentation rows in Build order, each with acceptance criteria. Example: "exposure event fires once per account per state, carrying the assignment ID. A 7-day A/A or SRM check on staging traffic passes at p > 0.01."

## Sources

Checked 2026-09-27.

- Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments* (Cambridge UP, 2020): https://experimentguide.com/ [Verified — OEC emphasis on the book site; chapter text not read]
- Kohavi, Crook & Longbotham, "Online Experimentation at Microsoft" (2009): https://exp-platform.com/Documents/ExP_DMCaseStudies.pdf [Verified]
- Kohavi et al., "Online Controlled Experiments at Large Scale", KDD 2013: http://chbrown.github.io/kdd-2013-usb/kdd/p1168.pdf [Verified]
- Kohavi, "Trustworthy A/B Tests: Pitfalls" (eMetrics 2017 deck): https://exp-platform.com/Documents/2017-05-17EmetricsControlledExperimentsPitfallsKohaviNR.pdf [Verified]
- Dmitriev, Gupta, Kim & Vaz, "A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls", KDD 2017: https://exp-platform.com/Documents/2017-08%20KDDMetricInterpretationPitfalls.pdf [Verified]
- Fabijan et al., "Diagnosing Sample Ratio Mismatch", KDD 2019: https://dl.acm.org/doi/10.1145/3292500.3330722 [Reported — abstract via search only]
- Deng, Xu, Kohavi & Walker, CUPED, WSDM 2013: https://exp-platform.com/cuped/ [Verified]
- Deng, Knoblich & Lu, "Applying the Delta Method in Metric Analytics", KDD 2018: https://arxiv.org/abs/1803.06336 [Verified]
- Hohnhold, O'Brien & Tang, "Focusing on the Long-term", KDD 2015: https://research.google/pubs/focus-on-the-long-term-its-better-for-users-and-business/ [Verified]
- Sadeghi et al., "Novelty and Primacy: A Long-Term Estimator for Online Experiments" (2021): https://arxiv.org/abs/2102.12893 [Verified]
- Athey, Chetty, Imbens & Kang, "The Surrogate Index", NBER w26463 (2019): https://www.nber.org/papers/w26463 [Verified]
- Evan Miller, "How Not To Run an A/B Test": https://www.evanmiller.org/how-not-to-run-an-ab-test.html · sample size calculator: https://www.evanmiller.org/ab-testing/sample-size.html [Verified]
- Statsig docs — CUPED: https://docs.statsig.com/experiments/statistical-methods/methodologies/cuped · custom unit IDs: https://docs.statsig.com/guides/experiment-on-custom-id-types · normalized (clustered) metrics: https://docs.statsig.com/statsig-warehouse-native/metrics/normalized-metrics · holdouts: https://docs.statsig.com/experiments/holdouts-introduction · SRM: https://docs.statsig.com/stats-engine/methodologies/srm-checks [Verified]
- Statsig blog, "Reading Experimentation Tea Leaves" (2022): https://www.statsig.com/blog/reading-experimentation-tea-leaves [Verified]
- Eppo docs — analysis methods: https://docs.geteppo.com/statistics/confidence-intervals/analysis-methods/ · well-powered experiments: https://docs.geteppo.com/guides/advanced-experimentation/running-well-powered-experiments/ [Verified]
- Optimizely — FDR control: https://support.optimizely.com/hc/en-us/articles/4410283967245-False-discovery-rate-control [Verified]
- GrowthBook — experimenting: https://docs.growthbook.io/using/experimenting · holdouts: https://docs.growthbook.io/app/holdouts [Verified; holdouts page via search result]
- Design effect: https://casrai.org/guides/cluster-randomized-trials-icc-design-effect [Reported — search result; standard formula]
- Amazon, "Statement Regarding Random Price Testing" (Sept 2000): https://press.aboutamazon.com/2000/9/amazon-com-issues-statement-regarding-random-price-testing [Verified]
- NY General Business Law §349-a: https://www.nysenate.gov/legislation/laws/GBS/349-A [Verified — primary text]
- EU Omnibus Directive 2019/2161, personalised-price disclosure: https://www.leidenlawblog.nl/articles/personalised-pricing-is-happening-heres-what-you-need-to-know [Reported — EUR-Lex not read]
- Kristen Berman, "The ultimate guide to willingness-to-pay", Lenny's Newsletter (Feb 2024): https://www.lennysnewsletter.com/p/the-ultimate-guide-to-willingness [Reported]
- Van Westendorp (1976) PSM, via `pricesensitivitymeter` docs: https://max-alletsee.github.io/pricesensitivitymeter/ [Verified — method description]; Gabor & Granger, Economica 1966, doi:10.2307/2552272: https://www.scirp.org/reference/referencespapers?referenceid=212614 [Reported — citation only]
- Sequence, "New rules of B2B pricing — 20 workshops with Kyle Poyar": https://www.sequencehq.com/blog/the-new-rules-of-b2b-pricing-insights-from-20-pricing-workshops-with-kyle-poyar [Reported]; Growth Unhinged, "Your guide to price testing" (2022): https://www.growthunhinged.com/p/your-guide-to-price-testing [Reported — paywalled; geo-test claim seen via search only]
