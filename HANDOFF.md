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

1. **A router skill** (`/pm-copilot`, `/design-flow`) that reads intent, orchestrates, and produces no artifact itself. This became our `monetization` skill (now `monetization-growth-pm`, see the renames below).
2. **Artifacts compound into a dossier** — every skill writes into a per-feature folder with a consistent naming scheme, so a session produces an ordered deliverable set, not scattered files. This became `.monetization/{feature-slug}/01-spec.md`, `02-wireframe.html`, etc. *(Numbering since changed — current scheme in `CLAUDE.md` → Output folder.)*
3. **Standardised output structure per artifact type** — every skill's output looks the same shape regardless of which skill produced it. This became `templates/ARTIFACT_HEADER.md`, `research-output.md`, `surface-spec.md`.
4. **Skills are sequenced but independently invokable** — the router suggests a flow, but nothing forces you through it. Every artifact ends with a `→ Next step` block instead of hard dependencies.

**Deliberate deviation from the reference pattern:** Julian's routers were written *first*, then the flow skills were built underneath. We inverted this — the router (`skills/monetization/SKILL.md`) was built **last**, after `pricing-intelligence` and `monetization-surface-spec` were both fleshed out. Rationale: a router written before its downstream skills exist ends up shallow and gets rewritten twice once the skills reveal their actual shape. This turned out right — the router's routing table is essentially a compressed summary of skills that already existed by the time it was written.

---

## Deviation added 2026-09-25: the router owns the chain

Pattern 4 above ("sequenced but independently invokable… every artifact ends with a `→ Next step` block") didn't survive first real use. A trial-expiry screenshot run through the router produced a review whose copy rows said "revise with `improve-conversion-surfaces-copy`" and stopped, ending on a "want me to mock it up?" question. The user had to re-prompt each skill and got four artifacts instead of one answer.

What changed: the router now announces a chain and runs it end to end. Skills omit next-step blocks and optional offers while a chain runs (rules live once, in `skills/monetization-growth-pm/SKILL.md` → Chain mode rules). Any chain containing a review ends in `05-requirements.md`, a synthesis a designer and engineer can build from directly. The router is no longer artifact-free. Skills are still independently invokable, and standalone runs keep the next-step block.

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
- **Later (Wave 2+):** the plan is to connect this file to monday.com's internal AI Brain sources (there are several — `AI Brain - Payments`, and others for finance/marketing/product knowledge, visible in this org's MCP list). When that connection exists, this file's role shifts from "the data" to "a pointer + cache," and the update ritual changes. Don't build that connection speculatively — wait until it's explicitly requested. **Requested and built 2026-09-28** — see "Pulled forward" at the end of this file.

**Data in the file right now:** pulled from public sources (monday.com's pricing page, support.monday.com articles, third-party pricing breakdowns) in September 2026, because no internal source was available in that session. The owner was asked to verify pricing/tier data, the surfaces inventory, and the "current squad focus" section — those are the parts most likely to be stale or wrong. Check the changelog at the bottom of that file for what's been verified since.

---

## QA pass — what was caught and fixed before the first commit

A full QA pass was run before pushing (broken links, orphaned skill references, JSON validity, environment-specific language, file-numbering consistency). Notable fixes, in case similar issues creep back in during future edits:

- **Two skills were referenced constantly but not actually in the repo** (`monetization-design-reviewer`, `improve-conversion-surfaces-copy`) — they existed elsewhere in this environment's skill library and were copied in. If you fork or rebuild this plugin elsewhere, make sure both are present under `skills/`, not just referenced.
- **`monday-context.md` was originally nested inside `monetization-surface-spec/references/`** — moved to a top-level `context/` folder so `pricing-intelligence` and `monetization-design-reviewer` could reference it too, without a skill-to-skill reach-around.
- **Output file numbering was inconsistent** across skills (some used `01-brief.md`/`03-spec.md`, others `01-spec.md`/`02-wireframe.html`). Fixed to one global convention at the time: `01-spec`, `02-wireframe`, `03-review`, `04-copy`. *Superseded:* copy moved before the wireframe and sizing/journey were added — the current scheme (00 sizing and journey · 01 spec · 02 copy · 03 wireframe and board · 04 review · 05 requirements) is in `CLAUDE.md` → Output folder.
- **`plugin.json` didn't match Claude Code's actual manifest schema**, and there was no `marketplace.json` — the install command in the README (`/plugin marketplace add ...`) would have failed. Both were rebuilt to spec.
- **`mcp-setup.md` originally described *this specific environment's* MCP connection status** ("already connected in Claude.ai") — useless and confusing to an outside user. Rewritten to be setup instructions for a stranger, with per-environment commands.

Run through the same checks (broken relative links, JSON validity, no environment-specific language) after any future edit batch — there's no CI for this repo yet.

---

## What's genuinely unfinished (Wave 1 gaps)

- **`monetization-surface-spec` has 7 surface types** but only `credit-ui.md` got the full deep-dive treatment (patterns, anti-patterns, trigger logic, copy hooks) because AI credits were flagged as the squad's top priority. The other six (`pricing-pages.md`, `paywalls.md`, `promotions.md`, `upgrade-triggers.md`, `cancellation.md`, `trial-flows.md`) exist and are usable, but are lighter — mostly mandatory-sections checklists pointing at the shared `wireframe-patterns.md` and `copy-hooks.md`. Deepen these as real specs get written against them and patterns emerge. *Since then every surface type got its own playbook in `playbooks/` (with the AI-native reference set) and a fuller spec reference; re-check this gap before acting on it.*
- **No CI.** `scripts/lint-playbooks.py` now checks playbook structure, evidence tags, links and source dates, but nothing runs it automatically, and nothing checks skill-level links, manifests or cross-file consistency. Worth a CI job if the repo gets multiple contributors.
- **`context/monday-context.md`'s squad-focus and surfaces-inventory sections** are the least verified parts of that file — flagged for the owner to confirm, unconfirmed as of this handoff.

---

## Wave 2 — scoped but not started

Two more skills were planned and intentionally deferred:

- **`monetization-data`** — *partly pulled forward 2026-09-28 as `monetization-opportunity-sizing`; see the end of this file.* Kremer-backed conversion analytics: trial→paid funnels, credit consumption by segment, paywall performance, cohort upgrade analysis. This is where `context/monday-context.md`'s eventual connection to internal AI Brain sources would likely also live, since both are "pull live internal data" problems.
- **`monetization-pm`** — PRD writer, A/B experiment designer, pricing-model workshop, launch readiness checklist.

Neither has a README section any more (the "Coming in Wave 2" section was removed); `monetization-pm`'s experiment-design part now lives in `skills/monetization-growth-pm/references/experiment-design.md`, the rest has no scaffolding yet. Start the same way Wave 1 started: read the existing adjacent skills in this environment (`data:analyze`, `data:write-query`, `product-management:write-spec` were all available and relevant when this was scoped) before writing anything from scratch.

---

## If you're Claude, reading this in a fresh Claude Code session

Read `CLAUDE.md` first — it's auto-loaded and has the operational rules. Read this file second, once, for judgment context. Don't re-summarize this file into `CLAUDE.md` or any skill — it would bloat the always-loaded context for information that's only useful when *extending* the plugin, not when *running* it. Delete this file once its contents are no longer relevant (e.g., after Wave 2 ships and the deferred-adapters decision is moot), or move it to a `docs/decisions/` folder if the pattern of writing these repeats.

## Rename added 2026-09-25: router → Monetization Growth PM

`monetization-pm-router` is now `monetization-growth-pm`. Invoking it means the full product work (scoping how far and how deep, the chain, the fix loop, requirements); a user who wants one piece calls that skill directly, and each skill runs its own intake when called alone. Earlier sections above say "router" — that's the same skill under its old name.

## Rename added 2026-09-25: pricing-intelligence → monetization-intelligence

The research skill's scope grew from what competitors charge to the whole monetization system — model, packaging, price, expansion paths — and how competitors run each surface (upgrade, cancellation, paywall, trial, top-up). Two workflows were added: surface benchmark and monetization teardown. Earlier sections above say `pricing-intelligence`; it's the same skill under its old name. The monday.com board keeps its name, "Pricing Intelligence".

## Pulled forward 2026-09-28: ask, never assume · real data · BigBrain

Two failures from real runs drove this, and both had the same root: the plugin let the model fill gaps itself.

**Assumptions in the output files.** Intake only ran on standalone calls — CLAUDE.md said "Inside a Growth PM chain, skip intake entirely", and the Growth PM's scoping question only covered how far, research and depth. So a chain filled cohort, tier, trigger, objective and constraints on its own, and the user's global "flag assumptions" rule turned those guesses into an improvised "Assumptions (flagged)" section in the artifacts. The heading never existed in the repo; the model invented it. What changed: the Growth PM runs one required-context intake for the whole chain (Step 1b), mid-chain gaps stop and ask, confirmed inputs go into the header (`confirmed with user`, `inferred`), and any `Assumptions` / "confirm or correct" section is a hard fail in the quality gate. An Open item with an owner is the only thing that stays open — for facts nobody in the conversation can answer.

**No data.** Snowflake was optional ("None of the MCPs are required"), and the journey map's fallback was a `{slot}` plus an Open item for Data — which the model stretched into improvised "Analyst data request" sections. Nothing sized the opportunity, so a chain could design, review and write requirements for a surface nobody had shown was worth building. What changed:

- **A data gate that pushes, then lets you continue** (CLAUDE.md, "Data gate"). Every data-dependent run searches for the Kramer tools (`data-expert-agent`, `kramer`) and, where it states monday facts, a BigBrain brain. Missing → name the MCP, say what it unlocks, link `mcp-setup.md`, and ask once per chain: Connect now (recommended) / Continue without data. Continuing, the whole flow runs; each unmeasured number is marked `[Not measured]` in place and each file opens with one line saying the data tools weren't connected. That is the only trace — the improvised "Analyst data request" section and any list of pulls for an analyst are gone, and an unmeasured number is not an Open item. A failed query is retried once, then marked the same way. Research and copy are exempt: they make no monday-number claims.
  - *Why not a hard stop:* the first version (same day) blocked the run outright. The owner softened it: a run without data is still worth having as long as nothing unmeasured is passed off as measured.
- **`monetization-opportunity-sizing`**, the first real piece of Wave 2's `monetization-data`. It writes `00-sizing.md` before the journey — reach × conversion × addressable lift × ARPA, low / base / high, every input shown with its query — and a go / no-go line that can stop the chain (or **Not sized — no data** when the user continued without Kramer). Addressable lift comes only from monday's own history (past experiments, the gap to the best comparable segment) so the model can't import a competitor's claimed lift. Its baselines are the ones the journey and the measurement plan use, so nothing downstream re-queries or slots them.
- **Researchio reused, not rebuilt.** The "why" behind a baseline hands off to the Researchio plugin's `kramer-pull` → `data-breakdown` when it's installed, instead of a second breakdown pipeline here.

**BigBrain, and why the context file changed role now.** The "connect to AI Brains later" plan in the context-file section above was the owner's call; sizing made it urgent, because ARPA needs current prices and a public-page cache nobody had verified internally isn't good enough to put an ARR number on. BigBrain is now the source of truth for plans, prices, credits, gating and trial terms, checked at run time (once per chain, Growth PM Step 1c). `monday-context.md` is a cache and pointer with a `verified-against` field — still "none yet" at this commit, because this change was written in an environment with no internal MCPs connected. A mismatch between a brain and the file is always reported, never silently used; non-public brain answers are never copied into the repo, only pointed to.

**Not yet done:** no end-to-end run on real data. Kramer and BigBrain weren't connected where this was written, so the gate, the sizing queries and the BigBrain fact check were linted but not exercised. The first run in an environment with both connected should check that the tool searches find them, that the query set in `skills/monetization-opportunity-sizing/references/sizing-model.md` returns what the model expects, and then set `verified-against` in the context file.
