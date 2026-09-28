# Scenario cards — who hits this surface, and why

Adapted from the Pragmatic Institute's *use scenario*: a short story that puts a market problem in context, from the persona's point of view, including the current result. Here it's the front half of the journey map. The screens come later, in the spec.

## The problem card

| Field | Question it answers | Rule |
|---|---|---|
| **Name** | *What* problem | A problem, not a feature: "Team outgrew its seats mid-project", not "Seat expansion modal" |
| **Persona** | *Who* has it | One of the monetization personas below, with tier and role |
| **Trigger** | *Why* it happens now | The observable event: "invites a 6th member on a 5-seat bundle", "credit balance hits 0 during an agent run" |
| **Frequency** | *When* / how often | From a query ([evidence-queries.md](evidence-queries.md)), split from `00-sizing.md` when it exists. Never a guess, never a `{slot}` |
| **Current result** | What happens today | The real, frustrating outcome, e.g. "invite fails; admin finds out from a Slack message 2 days later". For a new surface, what they do instead of the surface |
| **Evidence** | Is it real? | Counts, tickets, cancel-reason share, research, each with its source |
| **Impact** | How bad | ARR at risk or conversion lost, from the scenario's share of `00-sizing.md`'s ARR at stake. Without a sizing file, a 1–5 severity with one line of justification |

**Reframing sentence.** Every card opens with one line: **{persona}** struggles with **{problem}** when **{context}** because **{why it matters}**. It turns a feature request ("add a pause button") back into the problem ("a seasonal team pays for 3 idle months because leaving is the only option").

**Day in the life.** Under the card, 3–6 sentences in the first person: the persona's context, the trigger, what they do, and the current result. Concrete: a board name, a count, a time of day. No UI words ("modal", "CTA") — this is the problem, not the design.

## Monetization personas

Map every scenario to one of these, and to its cohort in [monday-context.md → User cohorts](../../../context/monday-context.md#user-cohorts) (cite it; don't restate the cohort's levers here).

| Persona | Can buy? | What they want at the surface | Typical surfaces |
|---|---|---|---|
| **Admin / billing owner** | Yes | Predictable cost, no surprises, a decision they can defend | Pricing page, tier upgrade, seat expansion, credit top-up, cancellation, downgrade |
| **IC member** | No | Keep working; not be the one who "broke the budget" | Paywall, limit hit, credit depletion — always needs the "Notify admin" path |
| **Viewer / guest** | No, and may not be a seat | Look, comment, not get billed | Invite and role changes, seat triggers |
| **Trial user** | Yes, at the end | Find out whether it works for their team before paying | Trial phases, trial expiry, first paywall |
| **Existing paid, low use** | Yes | Pay less, or leave cleanly | Downgrade, cancellation, right-size prompts |
| **Sales-assisted account** | Through a contract | A quote, procurement, security review | Enterprise gates, invoice-billed plan changes |

## How many scenarios, and which

- **At least 3.** One per persona that meets the surface, plus the variants that change the path. Cancellation, for example, needs one scenario per top cancel reason (price, low use, switching, temporary pause), because each reason gets a different offer.
- **IC and admin are always a pair.** Only admins change billing, so on every surface the person who hits it and the person who can act (buy, cancel, downgrade, top up) may differ. The IC hits the friction and the admin pays. Missing either half hides the handoff, which is where most of these journeys break.
- **Write for the proficient majority.** The U-curve: the loudest feedback comes from the extremes, novices and power users. It's where we listen, not what we build for. The typical, competent user is where we should listen. Size scenarios by frequency, and let the most frequent one set the main path.
- **Edge cases earn their place by frequency.** Before adding a "what if?" scenario, ask whether the persona will actually do it. If the data says a case is common (e.g. seat overage on monthly plans), promote it to a scenario. If it's rare, leave it to the spec's edge-case list.

## What stays out of a scenario

The WHAT is the problem: name, persona, trigger, frequency, evidence, impact. It belongs here.

The HOW is the solution: screens, flows, copy, thresholds. It belongs to the journey table (steps), the spec (screens), and the copy skill (words). A scenario that says "the user sees a modal" has jumped ahead. Rewrite it as what the user was trying to do.

## Source

Pragmatic Institute framework, *Planning → Use Scenarios* (problem card anatomy, "articulate problems from the persona's point of view", the U-curve of market input), adapted for monetization surfaces.
