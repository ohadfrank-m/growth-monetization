# Playbooks — shared CRO knowledge

One file per monetization surface type. This is the single owned source for the *why* — CRO principles, benchmarks, best-in-class examples, anti-patterns, and monday.com-specific application — for that surface.

## Why this folder exists

Two skills need the same CRO knowledge for the same surface type: `monetization-surface-spec` needs it to write a spec that's grounded in what actually converts, and `monetization-design-reviewer` needs it to score a design against real benchmarks. Before this folder existed, each skill kept its own copy under its own `references/` folder. They drifted — most visibly on credit/consumption UI, where both skills had independently written a full deep-dive with different benchmarks and different best-in-class examples for the same surface.

This follows the same principle as [`context/monday-context.md`](../context/monday-context.md): one owned file, cited by every skill that needs it, never re-derived or copied into a skill-local reference.

## What lives here vs. what stays in a skill's own `references/`

| Here (`playbooks/`) | Skill-local `references/` |
|---|---|
| Why a pattern works, benchmarks, best-in-class examples, anti-patterns | The mandatory fields a spec must contain, or the rubric anchors/weights used to score |
| Shared across ≥2 skills | Genuinely specific to one skill's job |

If you're adding CRO knowledge (a benchmark, a new best-in-class example, an anti-pattern) — add it here, then cite it from any skill reference that needs it. Don't paste it into a skill folder.

## Files

- [pricing-pages.md](pricing-pages.md) — surface type 1
- [paywalls.md](paywalls.md) — surface type 2
- [promotions.md](promotions.md) — surface type 3
- [upgrade-triggers.md](upgrade-triggers.md) — surface type 4 (tier/seat limits — not credits)
- [credit-ui.md](credit-ui.md) — surface type 5 (credit/consumption — including metering, forecasting, top-up)
- [cancellation.md](cancellation.md) — surface type 6
- [trial-flows.md](trial-flows.md) — surface type 7 (trial start, mid-trial, expiry; owns trial phases)
- [cases.md](cases.md) — shared case library: stories that apply to several surfaces, told once and cited by id

## Mandatory AI-native reference set

Every playbook carries an **AI-native reference set** section with teardowns of **Clay, Figma, ClickUp, and Claude** — four AI SaaS companies that each monetize AI differently (usage-only; per-seat AI credits; seat plan + separate AI layer; usage-multiplier tiers). Any new playbook (e.g. trial flows) must include all four before it's cited by a skill.

Each teardown uses the same shape so the design reviewer can compare like with like:

**What they ship → Flow → UI → Copy pattern → Why it works → Where it breaks → Steal for monday.com**

Each section ends with an at-a-glance comparison table, a copy bank (patterns to hand to `improve-conversion-surfaces-copy` — not final copy), an anti-pattern list where relevant, and dated sources.

### Evidence tags

| Tag | Meaning | Can a review cite it as fact? |
|---|---|---|
| **[Verified]** | Vendor pricing page, help center, or official blog | Yes |
| **[Reported]** | Third-party article, forum, or review | Only with the caveat |
| **[Teardown needed]** | Pattern exists but UI/copy not captured | No — capture a screenshot first |

Tag edge cases:

- **Vendor text seen only in a search snippet** (the page itself wouldn't load) → `[Reported]`, with the search result as the source. It becomes `[Verified]` only once the page itself is read.
- **Legal and regulatory claims** → `[Verified]` only against the primary text (statute, regulator, court or settlement page), never a law-firm blog or news summary. Legal sections also carry a "reviewed by legal: {date}" line; until that's filled in, the section is guidance, not a requirement.
- **Inference** — a pattern that follows from documented facts but isn't itself documented (e.g. "Figma's activation milestone is the first shared file") — is written as inference ("likely", "suggests"), never tagged `[Verified]`.

Vendor UI strings are paraphrased unless they appear in a cited source. Re-verify before quoting a competitor's exact copy in a deliverable — these companies change pricing and UI frequently (Clay repriced March 2026; Figma changed AI credit packaging twice in 2026).

**Known gap:** best-in-class examples written before the AI-native set (Notion, Linear, Loom, Duolingo, Spotify, HubSpot, etc.) include conversion figures with no source. Treat those numbers as directional until sourced.

### Updating a playbook

- **A company already in the playbook:** update its block in place — don't add a second block. Keep the tag of the strongest evidence you have and replace the source and checked date.
- **A claim with no source:** find one, or move it to a clearly marked *directional* note, or delete it. Never leave it looking like a fact. When a new source contradicts an existing claim, replace the claim and say what changed in the commit.
- **Research output:** `monetization-intelligence` ends surface work with *Suggested playbook updates*, marked **new** or **replaces {what}**. The owner applies them here; the skill never edits a playbook itself.

## Playbook structure — every file

Sections, in this order. A section with nothing real to say is left out, not padded.

1. **Core rule** — the one principle that decides most design choices on this surface, in two or three sentences.
2. **Benchmarks** — only when backed by real evidence: a named report, dataset, or study you can open at its URL. If nothing qualifies, **leave the section out entirely** — no directional notes, no placeholder. Vendor marketing claims with no method, figures seen only second-hand in someone else's summary, and unsourced "industry benchmarks" don't qualify. A table: `Metric · Number · Tag · Applies to · Source (URL) · Checked`. **Applies to** is one of *B2B SaaS · PLG / prosumer · consumer app · mobile app · publisher · mixed · legal* (*mixed* = a vendor dataset spanning several of these). Benchmarks from consumer, mobile or publisher contexts are allowed, but labelled — a review may cite them only as directional for monday.com.
3. **Patterns** — the design decisions that matter on this surface (structure, triggers, thresholds, IC vs admin), each with the companies that show it.
4. **Company teardowns** — What they ship → Flow → UI → Copy pattern → Why it works → Where it breaks → Steal for monday.com. Stories that recur across surfaces live once in [cases.md](cases.md) and are cited as `[case: {id}]`, followed by the lesson for *this* surface only.
5. **AI-native reference set** — Clay · Figma · ClickUp · Claude (mandatory, see above).
6. **Anti-patterns** — a table: `Anti-pattern · Why it fails · Who did it (tag, source)`. "Most SaaS products" is allowed only when no named company fits.
7. **Copy bank** — patterns to hand to `improve-conversion-surfaces-copy`, never final copy.
8. **monday.com-specific notes** — how this surface applies to monday. **Every monday fact** (prices, packages, limits, credit behaviour, trial terms) comes from [context/monday-context.md](../context/monday-context.md) — never stated from memory or invented as an example. Illustrative numbers use slots (`{N} credits — ${price}`), not made-up values.
9. **Sources** — every URL cited above, with the date checked.

Playbooks for surfaces with consumer-protection rules (cancellation, promotions) add a **Legal context** section after Benchmarks: primary sources only, a "reviewed by legal: {date}" line, and a clear note of which rules are consumer-only.

**One owner per rule.** A threshold or rule that spans surfaces is owned by one playbook and cited by the others: credit thresholds by `credit-ui.md`, tier and seat limit thresholds by `upgrade-triggers.md`, trial phases by `trial-flows.md`.

**Generated views.** Any HTML hub or summary page of these playbooks is generated from the markdown and never edited by hand — the markdown is what the skills read.

## Owner

Same owner as `monday-context.md` (Growth Monetization PM). Update in place; no changelog required — these are best-practice references, not versioned facts.
