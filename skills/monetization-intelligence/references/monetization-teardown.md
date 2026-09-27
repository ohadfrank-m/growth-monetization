# Monetization teardown workflow

How one company makes money, as a system: what it charges for, how it packages it, where the product asks for money, how accounts grow, and how it holds on to them. Price is one row of this, not the whole report.

## When to run

- "Monetization strategy of X" / "how does X make money" / "X's packaging" / "how does X expand accounts" / "full teardown of X"
- Before a packaging or pricing decision where one competitor is the reference point
- As the deep version of company research — offer it at the end of [company-research.md](company-research.md) when the user's question is about strategy, not just price

---

## Step 1: Plans, prices and history

Run [company-research.md](company-research.md) Steps 1–4 for the plan structure, current prices, and change history. Don't repeat that work here — reference its output.

## Step 2: The system, layer by layer

For each layer, state what the company does, the evidence (tag + source), and the signal it sends about their strategy.

| Layer | What to establish |
|-------|------------------|
| **Value metric** | What they charge for (seats, usage, credits, records, outcomes) and whether it grows with the value the customer gets |
| **Packaging** | What changes between tiers; which feature is the main reason to move up; what's an add-on vs. included |
| **Price points & discounting** | List prices, annual vs. monthly gap, visible promotions, typical negotiated discount (link [negotiation-intelligence.md](negotiation-intelligence.md) if pulled) |
| **Free / trial model** | Freemium limits, trial length and tier, card required, what's gated — pull from [freemium-trial-tracker.md](freemium-trial-tracker.md) |
| **AI monetization** | How AI is sold: included, credits, add-on, separate tier; what happens at the limit |
| **Expansion paths** | How revenue per account grows: seats, usage/credits, tier upgrades, add-ons, new products — and which one the product pushes hardest |
| **Surface map** | Every place the product asks for money — see Step 3 |
| **Retention & cancellation** | Save offers, pause, downgrade paths, what's lost on cancel |
| **Self-serve ceiling** | Where self-serve stops and sales starts — see *Self-serve ceiling checklist* below |

### Self-serve ceiling checklist

Record each line with its evidence tag, source URL and checked date. Where the vendor publishes no cap, say "no published cap", not "unlimited".

| Capture | What to record |
|---|---|
| Max seats online | Largest seat count purchasable by card without talking to sales; seat steps near the top (e.g. bundles, increments) |
| Contact-sales-only plans | Which tiers have no self-serve checkout; the CTA text used ("Contact sales", "Get a demo") |
| Plan-level seat bands | Minimums and maximums per plan (e.g. "1–10 members", "10+ members") |
| Annual-only thresholds | Plans, add-ons or seat counts that require annual billing |
| Payment-method gates | Card only vs invoice/PO/ACH/wire, and the minimum order for invoicing |
| Security and procurement gates | Which tier first gets SAML SSO, SCIM, audit log, data residency, HIPAA/BAA, DPA/security review — the usual reasons an account is forced to Enterprise |
| Routing in product | How the product sends a large or blocked account to sales (seat picker cap, "talk to us" at checkout, admin console banner) |
| Signal | What the ceiling says about their motion — a low ceiling pushes deals to sales; a high one keeps mid-market self-serve |

Compare against monday's ceiling from [context/monday-context.md](../../../context/monday-context.md) (seat bundles and where custom quotes start). Never state it from memory.

## Step 3: Surface map

List each monetization surface the company runs — pricing page, paywalls / feature gates, limit and seat prompts, credit meter and depletion, top-up, trial start and expiry, upgrade prompts, cancellation — with its trigger and one line on how it works.

This is a light pass: one row per surface, evidence-tagged. For any surface that matters to the question, run [surface-benchmark.md](surface-benchmark.md) for that surface in depth instead of guessing. Mark surfaces behind a login you couldn't see as `[Teardown needed]` — never describe them from inference.

## Step 4: Strategic read

- **The model in one sentence** — e.g. "Seat-led land, credits-led expand: the free tier gets people in, AI credits are the upsell".
- **Where the money actually comes from** — the expansion path the whole system is built around, and the evidence for it.
- **What's unusual** — any layer that breaks the category norm, and why they might be doing it.

## Step 5: So what for monday.com

Read [context/monday-context.md](../../../context/monday-context.md) and compare layer by layer against monday's current model.

- **Layer comparison** — a table: layer · this company · monday.com · implication.
- **Pricing headroom** — pressure up or down on monday's prices or packaging.
- **Positioning implication** — how monday should frame itself against this model in deals and on the pricing page.
- **Experiment to consider** — one hypothesis, metric, tier, cohort.
- **Threat signal** — the part of their system most likely to pull monday's customers or deals.

End with **Suggested playbook updates** for any surface findings, per [surface-benchmark.md](surface-benchmark.md) Step 7.

---

## Output file

`.monetization/research/{company-slug}-monetization-{YYYY-MM}.md`, using [../../../templates/research-output.md](../../../templates/research-output.md). Offer a battlecard afterwards (standalone only).

## Next step (standalone)

```
---
→ Next step: monetization-intelligence — benchmark the surface that matters most across competitors
→ Prompt: "How do {Company} and its competitors run {surface}?"
```
