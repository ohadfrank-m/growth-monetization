# Copy craft — evidence-backed microcopy rules

Read this when writing options for any monetization surface. The spine (15 reasons, one primary reason per asset, 2–3 options by angle, ★ Recommended) lives in SKILL.md; this file is how each *line* gets written. Guardrails — what never to write — live in [copy-guardrails.md](copy-guardrails.md). Surface CRO knowledge (benchmarks, examples, thresholds) lives in [playbooks/](../../../playbooks/README.md) and is cited, not restated.

Each rule: **rule** → why (source, tag) → surfaces → slot pattern. Slots in `{braces}` are never filled with invented monday numbers — prices, credits, limits and trial terms come from [monday-context.md](../../../context/monday-context.md).

Surfaces: 1 pricing page · 2 paywall · 3 promotion · 4 upgrade trigger · 5 credit/consumption UI · 6 cancellation · 7 trial flow.

Research effects come from other categories (web usability, retail, lab studies). They say which way to lean, not how much a monday surface will move — cite them as directional and let tests decide.

---

## CTA labels

**C1. Verb + the thing gained. Never a bare "Get started", "Learn more", "Submit" or "Upgrade".**
- Why: generic labels fit any goal, so they pull users into flows they didn't mean to enter — NN/g's eye-tracking saw users stop looking for information once "Get Started Now" appeared ([Harley & Flaherty, NN/g 2017](https://www.nngroup.com/articles/get-started/)) [Verified]. Labels should be specific, sincere, substantial, succinct — succinct traded off last ([Moran, NN/g 2019](https://www.nngroup.com/articles/better-link-labels/)) [Verified]. Lead commands with a verb ([Kaley, NN/g 2019](https://www.nngroup.com/articles/ui-copy/)) [Verified]; Mailchimp requires a verb in every button ([Web Elements](https://styleguide.mailchimp.com/web-elements/)) [Verified]. The design reviewer's Copy-quality 5 anchor already demands a CTA that names what's unlocked.
- Surfaces: all.
- Pattern: `{Verb} {outcome/object}` — `Keep {agent_name} running` · `Add {N} seats` · `Top up and resume` · `Keep my setup`. "Get started" only when the headline above it already names the outcome (e.g. trial day 1).

**C2. The CTA answers the headline.**
- Why: monday's own golden rule — CTAs respond directly to the header ([Vibe UX Writing Handbook](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/values/rulesUXWriting.tsx)) [Verified].
- Surfaces: all.
- Pattern: headline `{agent_name} paused — out of AI credits` → CTA `Top up and resume`. If the CTA could sit under a different headline unchanged, it's too generic.

**C3. When a click costs money or changes state, the label says so.**
- Why: a bare "Continue" causes click hesitation; "Continue to Payment" says what's next ([Baymard checkout guide 2026](https://baymard.com/blog/checkout-flow-ux-optimization)) [Verified]. Label the state the system moves into ([NN/g 2019](https://www.nngroup.com/articles/ui-copy/)) [Verified]. A button that does more than it says is a guardrail breach (see copy-guardrails G8).
- Surfaces: 1, 2, 4, 5, 7.
- Pattern: `Pay ${total} and upgrade` · `Start {plan} — ${price}/{period}` · `Review order` (when the next screen is the real confirm).

**C4. 1–4 words, under 20 characters, sentence case, no punctuation.**
- Why: monday's Button spec: 1–2 words, never more than 4, under 20 characters including spaces; no periods or exclamation marks; sentence case, never title case or all caps ([Vibe Button](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/components/Button/Button.mdx)) [Verified]. NN/g: 2–4-word commands ([2019](https://www.nngroup.com/articles/ui-copy/)) [Verified].
- Surfaces: all; hardest on mobile (M2).
- Pattern: `Keep my setup` (13) · `Add seats` (9). If the outcome needs more words, move them to the line above the button.

**C5. One primary CTA. The decline is secondary, visible and neutrally worded.**
- Why: monday's golden rule "One CTA"; one primary button per modal, extras as tertiary; one CTA per alert banner ([Vibe handbook](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/values/rulesUXWriting.tsx), [Modal](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/components/Modal/Modal.mdx), [AlertBanner](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/components/AlertBanner/AlertBanner.mdx)) [Verified]. Decline wording is a guardrail (G1, G12).
- Surfaces: all.
- Pattern: primary `{Verb} {outcome}` + tertiary `Not now` · `Stay on {current_plan}` · `Continue to cancel`. A prompt that recurs needs a way to say no for good — see G12.

---

## Headlines

**H1. Put the reason or outcome in the first two words.**
- Why: scanners see about the first two words (~11 characters) of a line; 35% of tested links were misunderstood from those alone, and a link starting "Introducing" scored 0% on reasonable predictions ([Nielsen, NN/g 2009](https://www.nngroup.com/articles/first-2-words-a-signal-for-scanning/)) [Verified]. GOV.UK's research background finds the same first-two-words effect ([GDS 2013](https://www.gov.uk/government/publications/govuk-content-principles-conventions-and-research-background/govuk-content-principles-conventions-and-research-background)) [Verified]. monday's rule: bottom line first ([Vibe](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/values/rulesUXWriting.tsx)) [Verified].
- Surfaces: all.
- Pattern: `Keep {N} automations running after {date}` — not `Your trial is ending soon, don't lose…`. Never open with "Introducing", "Meet", "We're excited".

**H2. Plain and objective beats clever and promotional.**
- Why: in Morkes & Nielsen's test, concise text improved usability 58%, scannable 47%, objective (non-promotional) 27%, all three 124% ([NN/g 1997](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/)) [Verified]. Headlines should make sense on their own — no puns, no clickbait ([Loranger & Nielsen, NN/g 2017](https://www.nngroup.com/articles/microcontent-how-to-write-headlines-page-titles-and-subject-lines/)) [Verified]. monday's brand voice rules out hype and unsubstantiated superlatives ([brand-monday.com tone of voice](https://www.brand-monday.com/tone-of-voice)) [Verified].
- Surfaces: all; strongest on 1 and 3, where promotional register creeps in.
- Pattern: `{Specific outcome} {for whom / by when}`. One idea per headline; wordplay only where the message is simple (see voice anchors: "light and engaging" tone), never on payment or errors.

**H3. Concrete beats abstract: name the asset, the task, the count.**
- Why: the same claim worded concretely is judged more likely true ([Hansen & Wänke 2010, PSPB, doi:10.1177/0146167210386238](https://doi.org/10.1177/0146167210386238)) [Verified — abstract]. In >1,000 real service conversations, concrete language raised satisfaction and purchase, because customers read it as being listened to ([Packard & Berger 2021, JCR, doi:10.1093/jcr/ucaa038](https://doi.org/10.1093/jcr/ucaa038)) [Verified — abstract; spoken service context, directional for UI].
- Surfaces: all; mandatory on 5 (task translation is owned by [credit-ui.md](../../../playbooks/credit-ui.md)) and 6/7 (personalized consequence).
- Pattern: `{agent_name} ran {N} times this week` — not `Your AI is working hard`. `{N} of your boards use {feature}` — not `Some features will be limited`.

**H4. Give a reason when you ask — a real one, sized to the ask.**
- Why: in Langer et al.'s copier study, a small request with no reason got 60% compliance; with an empty "because" 93%; with a real reason 94%. For a larger request the empty reason did nothing (24% = 24%) and only a real reason helped (42%) ([Langer, Blank & Chanowitz 1978, JPSP, doi:10.1037/0022-3514.36.6.635](https://doi.org/10.1037/0022-3514.36.6.635)) [Verified — cells of ~15–25 people]. An upgrade is a large ask: "because" works only when what follows is information.
- Surfaces: 2, 4, 5, 7.
- Pattern: `{Ask} so {concrete consequence from their usage}` — `Add {N} seats so {invitee_count} invited teammates can edit`. Not `Upgrade because you deserve more`.

**H5. Write from the user's side of the screen.**
- Why: monday's rule — focus on what the user wants to do and stands to gain, not your own perspective ([Vibe](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/values/rulesUXWriting.tsx)) [Verified].
- Surfaces: all.
- Pattern: `Your {asset} …` / `You can {outcome}` — not `We've introduced…` / `monday now offers…`.

---

## Numbers and prices

**N1. Show the price where the decision is made.**
- Why: business buyers name pricing as their top information need and leave B2B sites that hide it; sample prices or typical-scenario costs are acceptable when exact prices are complex ([Loranger, NN/g 2013](https://www.nngroup.com/articles/show-price/); [Nielsen, NN/g 2006](https://www.nngroup.com/articles/show-prices-for-common-scenarios/)) [Verified]. The trial playbook lists "upgrade CTA with no price" as an anti-pattern.
- Surfaces: 1, 2, 4, 5, 7.
- Pattern: `{plan} · ${price}/seat/mo, billed {period}` next to the CTA. For credits: `{N} credits — ${price}` plus a task translation only from `credit-ui.md` / monday-context (never "1 credit ≈ 1 AI action" — retired).

**N2. Show the total the user will actually pay, up front.**
- Why: 40% of US shoppers who abandoned checkout cite extra costs too high, the top reason (excluding browsers) ([Baymard list, updated 2025-09-22](https://baymard.com/lists/cart-abandonment-rate)) [Verified — consumer ecommerce, directional]. Hiding fees until checkout *raises* spend — StubHub buyers spent ~21% more and were 14% more likely to buy ([Blake et al. 2021, Marketing Science, doi:10.1287/mksc.2020.1261](https://doi.org/10.1287/mksc.2020.1261)) [Verified — figures from the NBER working paper] — which is exactly why regulators now target it (copy-guardrails G4).
- Surfaces: 1, 2, 4, 5.
- Pattern: `${total}/mo for {N} seats` · `{N}-seat bundle — ${bundle_total}/mo`. monday sells seats in bundles (monday-context): a per-seat price shown without the bundle minimum reads as the cheaper number. Show the bundle total beside it.

**N3. Percent or dollars: pick by the size of the number, and test.**
- Why: for high-priced items a dollar discount tends to seem larger, for low-priced items a percent ([Chen, Monroe & Lou 1998, J Retailing, doi:10.1016/S0022-4359(99)80100-6](https://doi.org/10.1016/S0022-4359(99)80100-6)) [Reported — direction from summaries; abstract not read]. Berger's "rule of 100" heuristic: under $100 use %, over $100 use $ ([jonahberger.com](https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/)) [Reported — author heuristic, not a study].
- Surfaces: 1, 3, 6 (discount offer).
- Pattern: per-seat monthly prices are usually small → `Save {N}%`; a team's annual saving is usually large → `${annual_saving} a year`. Default to both: `Save {N}% — ${annual_saving}/year for your team` (the promotions playbook's anchoring pattern).

**N4. Small-period framing for the price line; never at the cost of the total.**
- Why: framing a cost as a small recurring amount brings everyday expenses to mind as the comparison and raises acceptance ([Gourville 1998, JCR, doi:10.1086/209517](https://doi.org/10.1086/209517)) [Verified — abstract]. A per-payment price shown without the number of payments or total is "price comparison prevention" (FTC 2022, Appendix A — see copy-guardrails G5).
- Surfaces: 1, 3, 4.
- Pattern: `${per_seat_month}/seat/mo · billed annually (${annual_total})`. The small number leads; the commitment sits on the same line, not behind a tooltip.

**N5. Format numbers for the eye.**
- Why: numerals, commas from 1,000, no ".00" unless there are cents, % with numerals ([GOV.UK A–Z](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/); [Mailchimp Grammar](https://styleguide.mailchimp.com/grammar-and-mechanics/)) [Verified].
- Surfaces: all.
- Pattern: `$1,200` not `$1200.00`; `{N}%` not `{N} percent`; `{used} of {limit}` not `{used}/{limit}` where screen readers or non-technical admins read it.

**N6. Anchor to the genuine list price; let the recommendation carry the choice, not a decoy.**
- Why: the first number seen sets expectations ([Tversky & Kahneman 1974, Science, doi:10.1126/science.185.4157.1124](https://doi.org/10.1126/science.185.4157.1124)) [Verified]; price anchoring is real but its size is disputed ([Ariely, Loewenstein & Prelec 2003, doi:10.1162/00335530360535153](https://doi.org/10.1162/00335530360535153) vs. weaker replication [Maniadis, Tufano & List 2014, doi:10.1257/aer.104.1.277](https://doi.org/10.1257/aer.104.1.277)) [Verified]. Decoys work in stylized numeric displays ([Huber, Payne & Puto 1982, doi:10.1086/208899](https://doi.org/10.1086/208899)) but often vanish in realistic ones ([Frederick, Lee & Baskin 2014, doi:10.1509/jmr.12.0061](https://doi.org/10.1509/jmr.12.0061)) [Verified — abstracts]. The Economist-subscription decoy is a classroom demo from a book [Reported].
- Surfaces: 1, 3, 6.
- Pattern: `~~${list}/mo~~ ${offer}/mo` (the list price must be the real selling price — promotions.md *Legal context*). Recommended-plan badge names who it's for: `Best for {team_type}`. `Most popular` only with data behind it (G15).

**N7. When a default is set, the label states what it commits the user to.**
- Why: defaults move choices strongly — organ-donor consent ~82% opt-out vs ~42% opt-in ([Johnson & Goldstein 2003, Science, doi:10.1126/science.1091721](https://doi.org/10.1126/science.1091721)) [Verified — study; the two percentages Reported]; across 58 studies the average default effect is d = 0.68, stronger in consumer settings ([Jachimowicz et al. 2019, doi:10.1017/bpp.2018.43](https://doi.org/10.1017/bpp.2018.43)) [Verified — abstract]. Power is why pre-selected *paid* add-ons are a guardrail (G13).
- Surfaces: 1 (annual is the default — monday-context), 5 (auto top-up), 7.
- Pattern: `Billed annually — ${annual_total} today` on the pre-selected toggle; the monthly option shows its own total.

---

## Loss vs gain framing

**L1. Once the user has built something, frame the choice as keeping it.**
- Why: losses loom larger than gains ([Kahneman & Tversky 1979, doi:10.2307/1914185](https://doi.org/10.2307/1914185); [Tversky & Kahneman 1991, doi:10.2307/2937956](https://doi.org/10.2307/2937956)) [Verified]; owners demand more than twice what buyers pay for the same item ([Kahneman, Knetsch & Thaler 1990, doi:10.1086/261737](https://doi.org/10.1086/261737)) [Verified]; people value what they built themselves — but only once it's finished ([Norton, Mochon & Ariely 2012, doi:10.1016/j.jcps.2011.08.002](https://doi.org/10.1016/j.jcps.2011.08.002)) [Verified]. Size is contested: a 2024 meta-analysis puts the mean loss-aversion coefficient near 2 ([Brown et al., JEL, doi:10.1257/jel.20221698](https://doi.org/10.1257/jel.20221698)); Gal & Rucker argue the general claim is overstated ([2018, doi:10.1002/jcpy.1047](https://doi.org/10.1002/jcpy.1047)) [Verified — abstracts]. Lean on it; test it.
- Surfaces: 4, 5, 6, 7 (mid-trial, expiry).
- Pattern: `Keep {N} {assets} running after {date}` · `{asset_name} stops on {date}`.

**L2. Before the user owns anything, frame the gain.**
- Why: the endowment and IKEA effects need ownership or completed effort; pre-aha there is nothing to lose (inference from L1 sources; trial phases are owned by [trial-flows.md](../../../playbooks/trial-flows.md)).
- Surfaces: 1, 2 (new user), 7 (phase 1).
- Pattern: `Set up {first_outcome} in {N} minutes` — no deadline, no "don't lose".

**L3. A loss frame names real, specific consequences — nothing invented or inflated.**
- Why: framing shifts choices sharply even when facts are identical — 72% picked the sure option when framed as lives saved; 78% picked the gamble when framed as deaths ([Tversky & Kahneman 1981, doi:10.1126/science.7455683](https://doi.org/10.1126/science.7455683)) [Verified; replicated in Many Labs 1]. That power is why a technically true but misleading presentation is still a misleading action for consumers (UCPD Art. 6; FTC "net impression") — copy-guardrails G16.
- Surfaces: 4, 5, 6, 7.
- Pattern: `{N} of your boards use {feature} — on {date} they become {state}. Your data stays.` Omit what they've never used (cancellation.md).

**L4. The loss is the user's, never the company's feelings or their team's guilt.**
- Why: monday's own value — keep it stress-free; don't manipulate or guilt users even when they choose the less profitable option ([Vibe values](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/values/valuesUXWriting.tsx)) [Verified]. Confirmshaming is a guardrail (G1, G17).
- Surfaces: 6, 4, 7.
- Pattern: `Your {asset} stays until {date}` — not `Don't leave your team behind`.

---

## Urgency and deadlines

**U1. Deadline copy is a date, a time and a time zone.**
- Why: a deadline is only legitimate when real (promotions.md *Urgency — only real deadlines*); false limited-time claims are blacklisted for consumers (copy-guardrails G2).
- Surfaces: 3, 7, 1 (launch offers).
- Pattern: `Offer ends {date} at {time} {tz}` · `For your first renewal only`. No "soon", "last chance", "hurry".

**U2. Progress meters start from progress already made — for goals, not for spend.**
- Why: café customers bought faster as they neared a reward, and a 12-stamp card with 2 stamps pre-filled was completed faster than a plain 10-stamp card needing the same 10 purchases ([Kivetz, Urminsky & Zheng 2006, JMR, doi:10.1509/jmkr.43.1.39](https://doi.org/10.1509/jmkr.43.1.39)) [Verified — abstract].
- Surfaces: 7 (activation checklist), onboarding nudges on 2 and 4. **Not** credit spend on 5 — a credit meter is a budget, not a goal; gamifying spend works against the user (thresholds and meter copy are owned by `credit-ui.md`).
- Pattern: `{done} of {total} set up — {next_step} next` where signup and first actions count as done steps.

**U3. Scarcity only when it is real and relevant to this buyer.**
- Why: scarce items are valued more ([Worchel, Lee & Adewole 1975, doi:10.1037/0022-3514.32.5.906](https://doi.org/10.1037/0022-3514.32.5.906)) [Verified — citation; effect Reported]; SaaS seats and credits are not scarce, so most scarcity claims would be false (G3).
- Surfaces: 3.
- Pattern: genuine capacity only — `{N} places left in the {date} onboarding session`.

**U4. Reminders say what happens, when, and how to stop it.**
- Why: California requires pre-renewal and pre-trial-end notices with amount, date and how to cancel for consumer auto-renewals ([BPC §17602](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17602)) [Verified]; it's also the trust-safe default for B2B admins.
- Surfaces: 7, 3, renewal notices.
- Pattern: `Your {plan} renews on {date} for ${amount}. Change or cancel in {location}.`

---

## Error and limit states

**E1. What happened → why (if it helps) → the one next step. No blame, no "Oops", no "sorry" in validation.**
- Why: plain language, name the problem precisely, offer a fix, never blame the user, keep their input ([Neusesser & Sunwall, NN/g 2023](https://www.nngroup.com/articles/error-message-guidelines/)) [Verified]; GOV.UK drops "sorry" from validation errors ([Service Manual](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)) [Verified]; monday's tone for errors and payment is professional and reliable ([Vibe handbook](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/ux-writing-handbook.mdx)) [Verified].
- Surfaces: 1, 2, 4, 5 (payment failed, purchase pending, credits not yet applied).
- Pattern: `Your card ending {last4} was declined. Update your payment method to keep {plan} active.` · `Credits are on the way — they'll appear within {time}.`

**E2. Specific, adaptive messages — never a generic "Invalid {field}".**
- Why: 98% of sites use generic validation messages; test users spent up to 5 minutes fixing simple errors; write several field-specific messages because the back end already knows the failure ([Scott, Baymard 2023](https://baymard.com/research-articles/adaptive-validation-error-messages)) [Verified].
- Surfaces: checkout, top-up, seat entry (1, 4, 5).
- Pattern: `{field} {specific problem} — {how to fix}` · `Seat count must be one of {bundle_sizes}`.

**E3. A limit state names the limit, the count, what changes at the limit, and both paths (IC and admin).**
- Why: surface guidance in `copy-hooks.md` (surface 4) and `upgrade-triggers.md` / `credit-ui.md` (thresholds owned there — cite, don't restate). Give full context so users know where they are ([Vibe golden rules](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/values/rulesUXWriting.tsx)) [Verified].
- Surfaces: 4, 5.
- Pattern: `{used} of {limit} {unit} used — at {limit}, {what_stops}.` Admin CTA `{Verb} {capacity}`; IC CTA `Ask {admin_name} to {action}`.

**E4. Say the work is safe.**
- Why: keep the user's input ([NN/g 2023](https://www.nngroup.com/articles/error-message-guidelines/)) [Verified]; state preservation is a Friction-and-flow 5 anchor in the rubric.
- Surfaces: 2, 4, 5, 7.
- Pattern: `Your {draft/run} is saved — {action} to continue where you left off.`

---

## Length and scannability

**S1. Budget every line; people read a fifth of it.**
- Why: users read at most 28% of words on a page, about 20% realistically; each extra 100 words buys ~4.4 seconds ([Nielsen, NN/g 2008](https://www.nngroup.com/articles/how-little-do-users-read/)) [Verified]. Microcopy is under three sentences; concision includes preventing truncation ([Dykes, NN/g 2026](https://www.nngroup.com/articles/3-cs-microcopy/)) [Verified].
- Surfaces: all.
- Pattern: headline + one supporting line + CTA for modals, banners and gates. Anything more is secondary content (M1).

**S2. Short sentences, short words, active voice.**
- Why: split sentences over 25 words; prefer "buy" to "purchase", "help" to "assist"; active voice ([GOV.UK clear language](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/)) [Verified]. Experts prefer plain, scannable text too ([Loranger, NN/g 2017](https://www.nngroup.com/articles/plain-language-experts/)) [Verified]; target 8th grade for broad audiences, 12th for B2B ([Nielsen, NN/g 2015](https://www.nngroup.com/articles/legibility-readability-comprehension/)) [Verified].
- Surfaces: all.
- Pattern: one clause per sentence on the surface; save the "because" clause for H4.

**S3. Strike filler and hedges.**
- Why: GOV.UK's words to avoid include *deliver, empower, facilitate, impact, leverage, streamline, utilise* ([A–Z](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/)) [Verified]; monday's brand voice avoids hype, jargon, "best-in-breed" speak and wishy-washy qualifiers like *just, kind of, possibly* ([brand-monday.com](https://www.brand-monday.com/tone-of-voice)) [Verified]. Extends SKILL.md's filler list.
- Surfaces: all.
- Pattern: replace each with the concrete outcome (H3).

**S4. More than three options → the copy names one and says who each is for.**
- Why: the jam study — 30% bought from 6 jams vs 3% from 24 ([Iyengar & Lepper 2000, doi:10.1037/0022-3514.79.6.995](https://doi.org/10.1037/0022-3514.79.6.995)) [Verified]; but a meta-analysis found a mean effect near zero ([Scheibehenne et al. 2010, doi:10.1086/651235](https://doi.org/10.1086/651235)), and a later one found overload is real when choices are complex and preferences uncertain ([Chernev et al. 2015, doi:10.1016/j.jcps.2014.08.002](https://doi.org/10.1016/j.jcps.2014.08.002)) [Verified — abstracts]. Credit packages and tier grids are exactly that case.
- Surfaces: 1, 5 (package choice).
- Pattern: each option gets a `For {use_case}` line; one carries `Recommended for {their_usage_signal}`.

---

## Mobile

**M1. Front-load and cut further on mobile — secondary detail goes behind disclosure.**
- Why: NN/g's 2016 study (276 participants) found comprehension on phones was not worse — ~3 points higher — but difficult text was read more slowly, so brevity still matters ([Moran, NN/g 2016](https://www.nngroup.com/articles/mobile-content/)) [Verified]; defer secondary content ([Nielsen, NN/g 2011](https://www.nngroup.com/articles/defer-secondary-content-for-mobile/)) [Verified]. The older "twice as difficult" finding (2011) is superseded — don't cite it alone.
- Surfaces: all; the reviewer checks at 375px.
- Pattern: when a line wraps past two lines at 375px, write an explicit mobile variant in `02-copy.md` (`Mobile:` row) rather than letting it truncate.

**M2. CTA labels must fit without truncation.**
- Why: C4 budget (under 20 characters — Vibe) and NN/g's concision rule on truncation.
- Surfaces: all.
- Pattern: `Keep my setup` not `Continue with Pro and keep my setup`.

**M3. No material term lives only in a tooltip.**
- Why: phones have no hover; the FTC lists fees hidden behind tooltips as hiding material information ([Bringing Dark Patterns to Light, 2022, pp.7–9](https://www.ftc.gov/reports/bringing-dark-patterns-light)) [Verified].
- Surfaces: 1, 4, 5, 7.
- Pattern: price, billing period, renewal and credit expiry sit in body text on the same card as the CTA.

---

## monday.com voice anchors

Two official public sources. In-product copy follows the **Vibe UX Writing Handbook**; marketing surfaces (pricing page hero, promotional email) also follow the **brand tone of voice**. Where they differ, in-product wins inside the product.

**Vibe UX Writing Handbook** — monday's design system ([Storybook: Foundations → UX Writing Handbook](https://vibe.monday.com/); source: [GitHub, ux-writing-handbook.mdx](https://github.com/mondaycom/vibe/blob/master/packages/docs/src/pages/foundations/ux-writing-handbook/ux-writing-handbook.mdx), last changed 2025-10-29) [Verified]:

| Layer | What it says (paraphrased) | Applies to monetization copy as |
|---|---|---|
| Principles | Clarity (simple language, concision) · Consistency (approved terminology, same format for similar messages) · Accessibility (inclusive, readable) | Same term for the same thing across surfaces: pick "AI credits" (or whatever monday-context uses) and never alternate |
| Personality | The ultimate assistant: expert and reliable (owns mistakes, shows the fix); proactive and supportive (anticipates needs) | Warn before depletion, not after; payment errors say what monday will do |
| Voice | Empathetic and conversational ("human to human"); positive and professional (affirmative language) | "You/your", affirmative phrasing ("Keep…", "Add…") over negatives ("You can't…") |
| Tone spectrum | *Light and engaging* for simple messages and delight moments (feature announcements, empty states); *professional and reliable* where reassurance matters (system errors, anything involving payment) | Promotions and launches may be light; paywalls, credit depletion, billing, cancellation are professional and reliable |
| Golden rules | Bottom line first · give full context · user's point of view · one CTA · CTAs respond to the header · cut the fluff | Rules H1, E3, H5, C5, C2, S1 |
| Values | Work for the users · stay consistent · **keep it stress-free** · gradual complexity · no passive-aggressive or offensive language · write for all readers | The stress-free value is monday's own anti-confirmshaming rule — see copy-guardrails G1 |

The one line to quote in a review: "Do not manipulate or guilt users, even if they choose to do something less profitable for you." — Vibe UX Writing Handbook, Values.

Component rules that bind microcopy ([Vibe components](https://github.com/mondaycom/vibe/tree/master/packages/docs/src/pages/components)) [Verified]: Button — 1–2 words, max 4, under 20 characters, sentence case, no periods or exclamation marks; Modal — title + CTA + close, one primary button; AlertBanner — one CTA plus dismiss; Toast — short, with a follow-up or undo action.

**Brand tone of voice** — [brand-monday.com/tone-of-voice](https://www.brand-monday.com/tone-of-voice), linked as "Our brand guidelines" from the [monday.com press kit](https://monday.com/p/news/press-kit/) [Verified]:

- Four traits: **Confident** (lead with data and customer success; no hype, no hedging), **Fluff-free** (plain words, active voice, concise not abrupt), **Playful** (light, never silly, never at the cost of clarity), **Passionate** (energetic; don't use the word "passionate").
- Product lines carry their own tone ([brand-monday.com/products](https://www.brand-monday.com/products)): Work Management premium / visionary / knowledgeable; CRM self-aware / spicy, bold but not mean, no competitor names; Dev edgy / indie; Service dynamic / empowering / cool. A cross-product promotion (surface 3) takes the tone of the product being sold.

**Tension to know:** Vibe's Button page uses "Get started" as its length/case example. That is formatting guidance, not label advice — rule C1 still applies to monetization CTAs.

---

## Sources

Checked 2026-09-27.

- NN/g: https://www.nngroup.com/articles/get-started/ · https://www.nngroup.com/articles/learn-more-links/ · https://www.nngroup.com/articles/better-link-labels/ · https://www.nngroup.com/articles/ui-copy/ · https://www.nngroup.com/articles/3-is-of-microcopy/ · https://www.nngroup.com/articles/3-cs-microcopy/ · https://www.nngroup.com/articles/first-2-words-a-signal-for-scanning/ · https://www.nngroup.com/articles/microcontent-how-to-write-headlines-page-titles-and-subject-lines/ · https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ · https://www.nngroup.com/articles/how-little-do-users-read/ · https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/ · https://www.nngroup.com/articles/legibility-readability-comprehension/ · https://www.nngroup.com/articles/plain-language-experts/ · https://www.nngroup.com/articles/show-price/ · https://www.nngroup.com/articles/show-prices-for-common-scenarios/ · https://www.nngroup.com/articles/ecommerce-taxes-fees/ · https://www.nngroup.com/articles/mobile-content/ · https://www.nngroup.com/articles/defer-secondary-content-for-mobile/ · https://www.nngroup.com/articles/error-message-guidelines/
- Baymard: https://baymard.com/lists/cart-abandonment-rate · https://baymard.com/blog/checkout-flow-ux-optimization · https://baymard.com/research-articles/adaptive-validation-error-messages
- GOV.UK: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/ · https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/ · https://www.gov.uk/government/publications/govuk-content-principles-conventions-and-research-background/govuk-content-principles-conventions-and-research-background · https://www.gov.uk/service-manual/design/writing-for-user-interfaces
- Mailchimp: https://styleguide.mailchimp.com/web-elements/ · https://styleguide.mailchimp.com/grammar-and-mechanics/
- Research (DOIs confirmed via Crossref): see inline links; bias originals are in [sources.md §4](sources.md).
- Berger: https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/
- monday: https://github.com/mondaycom/vibe/tree/master/packages/docs/src/pages/foundations/ux-writing-handbook · https://github.com/mondaycom/vibe/tree/master/packages/docs/src/pages/components · https://www.brand-monday.com/tone-of-voice · https://www.brand-monday.com/products · https://monday.com/p/news/press-kit/
