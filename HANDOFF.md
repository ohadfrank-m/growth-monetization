# Handoff — context for continuing this plugin in Claude Code

This file exists because a lot of the *why* behind this repo's structure was decided in a planning conversation that won't carry over when you open this in a new environment. `CLAUDE.md`, the README, and the templates capture the *what*. This file captures the *why* — so the next session (or the next person) doesn't have to reverse-engineer decisions from the file structure alone.

Read this once, then treat it as background — it's not meant to be loaded into every skill's context.

---

## Origin and goal

This plugin was scoped as a **Growth-Monetization-Product plugin** for monday.com's growth squads — teams owning pricing pages, paywalls, trials, upgrade triggers, credit/consumption UI, and cancellation flows. The starting point was two existing skills: `pricing-intelligence` (a mature, PricingSaaS-backed research skill) and `monetization-design-reviewer` (a CRO rubric reviewer). The brief was to extend these into a coherent plugin with a proper information architecture, not just a folder of unrelated skills.

Four intended clusters were discussed: **Pricing Intelligence**, **Monetization Surfaces Design**, **Monetization Data**, **Monetization PM**. Only the first two are built (Wave 1). Data and PM are Wave 2 — see below.

---

## Why we borrowed patterns from julianoczkowski's repos

Two reference repos shaped the structure: `product-manager` (Pragmatic Framework as 18 Claude skills) and `designer-skills` (8 skills for the design process). Both are private/semi-private, but their public documentation (Medium article for product-manager, full README for designer-skills) revealed four patterns worth stealing:

1. **A router skill** (`/pm-copilot`, `/design-flow`) that reads intent, orchestrates, and produces no artifact itself. This became our `monetization` skill.
2. **Artifacts compound into a dossier** — every skill writes into a per-feature folder with a consistent naming scheme, so a session produces an ordered deliverable set, not scattered files. This became `.monetization/{feature-slug}/01-spec.md`, `02-wireframe.html`, etc.
3. **Standardised output structure per artifact type** — every skill's output looks the same shape regardless of which skill produced it. This became `templates/ARTIFACT_HEADER.md`, `research-output.md`, `surface-spec.md`.
4. **Skills are sequenced but independently invokable** — the router suggests a flow, but nothing forces you through it. Every artifact ends with a `→ Next step` block instead of hard dependencies.

**Deliberate deviation from the reference pattern:** Julian's routers were written *first*, then the flow skills were built underneath. We inverted this — the router (`skills/monetization/SKILL.md`) was built **last**, after `pricing-intelligence` and `monetization-surface-spec` were both fleshed out. Rationale: a router written before its downstream skills exist ends up shallow and gets rewritten twice once the skills reveal their actual shape. This turned out right — the router's routing table is essentially a compressed summary of skills that already existed by the time it was written.

---

## Deviation added 2026-09-25: the router owns the chain

Pattern 4 above ("sequenced but independently invokable… every artifact ends with a `→ Next step` block") didn't survive first real use. A trial-expiry screenshot run through the router produced a review whose copy rows said "revise with `improve-conversion-surfaces-copy`" and stopped, ending on a "want me to mock it up?" question. The user had to re-prompt each skill and got four artifacts instead of one answer.

What changed: the router now announces a chain and runs it end to end. Skills omit next-step blocks and optional offers while a chain runs (rules live once, in `skills/monetization-pm-router/SKILL.md` → Chain mode rules). Any chain containing a review ends in `05-requirements.md`, a synthesis a designer and engineer can build from directly. The router is no longer artifact-free. Skills are still independently invokable, and standalone runs keep the next-step block.

Why the synthesis rules are strict (verbatim copy, no invented tokens/numbers/claims, every review row traced): the value of `05-requirements.md` is that nobody has to re-open the other artifacts. That only holds if nothing in it is guessed.

## Why `adapters/` (Cursor/ChatGPT-specific files) was cut from Wave 1

Originally planned: separate adapter files per environment (Cursor `.mdc` rules, a ChatGPT system prompt). Cut because:
- The Anthropic plugin format (`.claude-plugin/plugin.json` + `skills/`) already works natively in Claude and Cursor without a translation layer
- Maintaining three parallel versions of unproven skills wastes effort before the skills themselves are stable
- ChatGPT doesn't support MCP the same way — a real ChatGPT adapter is a bigger lift than a thin wrapper, and premature until Wave 1 skills are validated in real use

**If picking this up:** Wave 2 is the right time to revisit ChatGPT support, if it's still wanted. Cursor needs no adapter — just the MCP config documented in `mcp-setup.md`.

---

## The `context/monday-context.md` decision — read this before touching that file

This file exists because skills kept needing monday.com-specific facts (pricing, AI credit structure, tier gating, cohort definitions) and that content was originally duplicated across `CLAUDE.md` and individual `SKILL.md` files. We consolidated it into one owned, versioned file.

**Ownership model chosen:** manual updates by a named owner (frontmatter `owner` field), not an automated pull from an internal source — yet. The person building this plugin explicitly said: *"Let's start with me updating it, later we can potentially connect it to internal 'brains' we have for AI credits, monetization etc."* So:

- **Now:** the owner edits the file directly, bumps `last-updated`, adds a changelog row. `pricing-intelligence` can be pointed at monday.com's own public pricing page to audit whether the file has drifted.
- **Later (Wave 2+):** the plan is to connect this file to monday.com's internal AI Brain sources (there are several — `AI Brain - Payments`, and others for finance/marketing/product knowledge, visible in this org's MCP list). When that connection exists, this file's role shifts from "the data" to "a pointer + cache," and the update ritual changes. Don't build that connection speculatively — wait until it's explicitly requested.

**Data in the file right now:** pulled from public sources (monday.com's pricing page, support.monday.com articles, third-party pricing breakdowns) in September 2026, because no internal source was available in that session. The owner was asked to verify pricing/tier data, the surfaces inventory, and the "current squad focus" section — those are the parts most likely to be stale or wrong. Check the changelog at the bottom of that file for what's been verified since.

---

## QA pass — what was caught and fixed before the first commit

A full QA pass was run before pushing (broken links, orphaned skill references, JSON validity, environment-specific language, file-numbering consistency). Notable fixes, in case similar issues creep back in during future edits:

- **Two skills were referenced constantly but not actually in the repo** (`monetization-design-reviewer`, `improve-conversion-surfaces-copy`) — they existed elsewhere in this environment's skill library and were copied in. If you fork or rebuild this plugin elsewhere, make sure both are present under `skills/`, not just referenced.
- **`monday-context.md` was originally nested inside `monetization-surface-spec/references/`** — moved to a top-level `context/` folder so `pricing-intelligence` and `monetization-design-reviewer` could reference it too, without a skill-to-skill reach-around.
- **Output file numbering was inconsistent** across skills (some used `01-brief.md`/`03-spec.md`, others `01-spec.md`/`02-wireframe.html`). Fixed to one global convention, now documented in `CLAUDE.md`: `01-spec`, `02-wireframe`, `03-review`, `04-copy`.
- **`plugin.json` didn't match Claude Code's actual manifest schema**, and there was no `marketplace.json` — the install command in the README (`/plugin marketplace add ...`) would have failed. Both were rebuilt to spec.
- **`mcp-setup.md` originally described *this specific environment's* MCP connection status** ("already connected in Claude.ai") — useless and confusing to an outside user. Rewritten to be setup instructions for a stranger, with per-environment commands.

Run through the same checks (broken relative links, JSON validity, no environment-specific language) after any future edit batch — there's no CI for this repo yet.

---

## What's genuinely unfinished (Wave 1 gaps)

- **`monetization-surface-spec` has 7 surface types** but only `credit-ui.md` got the full deep-dive treatment (patterns, anti-patterns, trigger logic, copy hooks) because AI credits were flagged as the squad's top priority. The other six (`pricing-pages.md`, `paywalls.md`, `promotions.md`, `upgrade-triggers.md`, `cancellation.md`, `trial-flows.md`) exist and are usable, but are lighter — mostly mandatory-sections checklists pointing at the shared `wireframe-patterns.md` and `copy-hooks.md`. Deepen these as real specs get written against them and patterns emerge.
- **No CI / validation script.** Nothing automatically checks broken links or schema drift when someone edits a skill. Worth adding if the repo gets multiple contributors.
- **`context/monday-context.md`'s squad-focus and surfaces-inventory sections** are the least verified parts of that file — flagged for the owner to confirm, unconfirmed as of this handoff.

---

## Wave 2 — scoped but not started

Two more skills were planned and intentionally deferred:

- **`monetization-data`** — Kremer-backed conversion analytics: trial→paid funnels, credit consumption by segment, paywall performance, cohort upgrade analysis. This is where `context/monday-context.md`'s eventual connection to internal AI Brain sources would likely also live, since both are "pull live internal data" problems.
- **`monetization-pm`** — PRD writer, A/B experiment designer, pricing-model workshop, launch readiness checklist.

Both are named in the README's "Coming in Wave 2" section so the plugin doesn't feel unfinished to an outside user, but neither has any scaffolding yet. Start the same way Wave 1 started: read the existing adjacent skills in this environment (`data:analyze`, `data:write-query`, `product-management:write-spec` were all available and relevant when this was scoped) before writing anything from scratch.

---

## If you're Claude, reading this in a fresh Claude Code session

Read `CLAUDE.md` first — it's auto-loaded and has the operational rules. Read this file second, once, for judgment context. Don't re-summarize this file into `CLAUDE.md` or any skill — it would bloat the always-loaded context for information that's only useful when *extending* the plugin, not when *running* it. Delete this file once its contents are no longer relevant (e.g., after Wave 2 ships and the deferred-adapters decision is moot), or move it to a `docs/decisions/` folder if the pattern of writing these repeats.
