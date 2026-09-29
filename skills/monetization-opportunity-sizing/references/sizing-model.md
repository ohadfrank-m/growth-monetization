# Sizing model — reach × conversion × lift × ARPA

Read this before writing `00-sizing.md`. It fixes what each input means, which query produces it, and how the cases and the verdict are computed, so two people sizing the same surface get the same number.

Every figure in this file is a symbol or a labelled illustration. Real query results go only in `.monetization/` artifacts.

## The model

**ARR at stake per year = R × c × ℓ × a**

| Symbol | Input | Definition | Source |
|---|---|---|---|
| **R** | Reach | Distinct accounts that hit the trigger in the window, annualized (×365/90 for a 90-day window; as-is for 12 months) | Kramer |
| **c** | Current conversion | Share of R reaching the objective within **N** days of their first trigger in the window | Kramer |
| **N** | Conversion window | The day by which 80% of historical conversions after the trigger have happened | Kramer (the lag distribution) |
| **ℓ** | Addressable lift | Relative lift in c a better surface could plausibly produce — low / base / high below | Kramer (monday's own history) |
| **a** | ARPA | Incremental ARR per converted account | BigBrain prices × Kramer mix |

R × c × ℓ is the number of extra conversions per year; × a is their ARR.

### ARPA

a = Σₚ (share of converters landing on plan or package *p*) × (annual list price of *p* per seat) × (median seats of converters on *p*)

- Prices come from BigBrain (the Payments brain), per billing period. For a credit package, the price is the package's, not per seat.
- The mix and the seat medians come from Kramer.
- **Check against realized ARR.** Ask Kramer for the median ARR change of converters in the window. When it differs from a by more than 20%, say why in the file (discounts, mid-cycle proration, a mix shift) and tell the user. Keep the list-based a in the model unless the user picks the realized one — never switch silently.

### The lift cases

| Case | With past experiments on this surface type | Without them |
|---|---|---|
| **Low** | The smallest positive primary-metric lift among them | 0.25 × g |
| **Base** | Their median lift | 0.5 × g |
| **High** | g | g |

**g — the internal ceiling gap** = (c_best − c) / c, where c_best is the conversion of the best comparable segment: same trigger and tier, split on a dimension the surface could change (the surface variant seen, the role who hit the trigger, whether the admin was notified), at least 50 accounts. Name the dimension in the file.

The 0.25 and 0.5 shares are this plugin's convention for "closes a quarter / half of the gap to monday's own best segment". They're stated in the file as the convention, not presented as evidence.

**No lift evidence at all** (no past experiments, no segment converting above c): don't invent one. Show a single case at the MDE the traffic supports (Testability below), labelled "break-even: the smallest lift a test could detect", and the verdict answers whether that lift would justify the build.

### Surface-specific reading

| Surface | "Conversion" c | ARR at stake means |
|---|---|---|
| Pricing page, paywall, tier upgrade, trial | Paid conversion or upgrade within N | New or expansion ARR |
| Credit UI | Top-up or package purchase within N of the warning state | Expansion ARR |
| Cancellation, downgrade | Save rate: cancel-starters still paying at 90 days | Retained ARR (a = ARR of the saved accounts) |
| Promotion | Incremental conversion vs a holdout — never redemption | Incremental ARR **net of discount cost** |

## The query set

Ask these in one `data-expert-agent` session, filling the braces from the trigger. Aggregates only; the rules in [evidence-queries.md](../../monetization-journey-map/references/evidence-queries.md) apply (show the question, the source, the range, the run date; say what the number counts).

| Input | Question |
|---|---|
| R | "Distinct accounts that {trigger event} in the last 90 full days, by tier, billing period, and the role of the user who triggered it (admin / member)" |
| c | "Of those accounts, the share that {objective event} within {N} days of their first {trigger event} in the window, by the same segments" |
| N | "For accounts that {objective event} after {trigger event} in the last 12 months, the distribution of days between them — the day by which 50% and 80% had converted" |
| c_best | "{c}, split by {dimension}; segments with fewer than 50 accounts reported as <50" |
| Past lifts | "Concluded experiments on {surface type} in the last 24 months: primary metric, relative lift, significance, and whether it shipped" |
| Mix | "Of the accounts that converted, the share landing on each plan or credit package, with the median seat count per plan" |
| Realized check | "Median ARR change in the 30 days after conversion for those accounts" |

For the IC / admin pair, the role split in R also sizes the admin-request path — pass it to the journey.

Ask BigBrain, per plan or package in the mix: "Current annual and monthly list price of {plan / package} per seat (or per package) for new self-serve accounts."

## Testability

From [experiment-design.md](../../monetization-growth-pm/references/experiment-design.md) §5, with p₁ = c, δ = c × ℓ_base, and E = R / 52 accounts per week:

- n per arm = 7.85 × [p₁(1−p₁) + p₂(1−p₂)] / δ², p₂ = p₁ + δ
- Runtime = ⌈2n / (E × allocation)⌉ whole weeks, min 2, plus N days before readout
- **Reads?** yes when the runtime ≤ the longest test the team will run
- The MDE the traffic supports: the δ that makes the runtime equal the longest test

**Illustration — not monday data.** R = 52,000/yr → E = 1,000/week; c = 10%; ℓ_base = 10% → δ = 1 pp; n ≈ 14,750 per arm; at 100% allocation, runtime ≈ 30 weeks. Against a 6-week limit, the test won't read, and the verdict is ship + holdout or a bolder change.

## Go / no-go

| Verdict | When | What happens next |
|---|---|---|
| **Go — test** | Base-case ARR ≥ the bar **and** the test reads | The chain continues; the measurement plan is an A/B |
| **Go — ship + holdout** | Base-case ARR ≥ the bar, test doesn't read | The chain continues; the plan is ship to a share with a holdout (experiment-design §1) |
| **Re-scope** | Base < bar ≤ high | Name the re-scope: widen the trigger, pool surfaces with the same trigger, or a bolder change (bigger MDE) |
| **No-go** | High-case ARR < the bar | Say so plainly. The chain stops unless the user overrides |
| **Not sized — no data** | The user continued without Kramer (Data gate) | The chain continues. Every input and result is `[Not measured]`. Never a Go or No-go on unmeasured inputs |

No bar from the user: the verdict line reports ARR at stake and testability only, and an Open item asks Product — name TBD for the bar.

A verdict of Re-scope or No-go is never softened into a Go. The point of sizing first is to find that out before anything's designed.
