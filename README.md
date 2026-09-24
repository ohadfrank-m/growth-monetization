# Growth Monetization Plugin

[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-000?style=flat-square)](https://claude.ai/code)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-000?style=flat-square)](https://cursor.com)
[![Skills](https://img.shields.io/badge/skills-5-333?style=flat-square)](#the-skills)
[![monday.com](https://img.shields.io/badge/built_for-monday.com-ff3366?style=flat-square)](https://monday.com)

A monetization copilot for growth product squads — research how competitors price, spec and wireframe any monetization surface, score designs against a CRO rubric, and write benefit-led conversion copy. Every command produces a real artifact. Skills chain into each other. Your work accumulates in a single folder you can hand to design or engineering.

Built for: pricing pages · paywalls · upgrade flows · credit/consumption UI · trial flows · cancellation flows

---

## The flow

Skills follow a deliberate sequence. Run `/monetization` to be guided through automatically, or invoke any skill individually.

```
/monetization                    ← start here if unsure — routes to the right skill
      │
      ├── /pricing-intelligence  ← research: how competitors price, what models dominate
      │         │
      │         ▼
      ├── /monetization-surface-spec  ← spec + wireframe any surface from a brief or design
      │         │
      │         ▼
      └── /monetization-design-reviewer  ← CRO rubric score + prioritised fix list
                │
                ▼
          /improve-conversion-surfaces-copy  ← benefit-led copy rewrites
```

Run them in sequence or start anywhere. Each skill reads what the previous one produced.

---

## Installation

### Claude Code (recommended)

```bash
/plugin marketplace add ohadfrank-m/growth-monetization
/plugin install growth-monetization@growth-monetization
```

Skills load automatically. Invoke by name or let `/monetization` route for you.

To try locally before installing:

```bash
claude --plugin-dir /path/to/growth-monetization
```

To update when new skills ship:

```bash
/plugin update growth-monetization@growth-monetization
```

### Cursor

Clone the repo, then add to your project's `.cursor/rules/`:

```bash
git clone https://github.com/ohadfrank-m/growth-monetization
```

Copy `CLAUDE.md` content into `.cursor/rules/monetization.mdc`. Add required MCP servers to `~/.cursor/mcp.json` — see [mcp-setup.md](mcp-setup.md).

### Claude Desktop / Claude.ai

Add as a custom skill or copy skill content into your project context. Skills work without the plugin format — paste the SKILL.md content of any individual skill as a system prompt or project instruction.

---

## Required MCP connections

| MCP | Used by | How to connect |
|-----|---------|---------------|
| **monday.com** | All skills — board logging | Add `https://mcp.monday.com/mcp` as a remote MCP server |
| **PricingSaaS** | `pricing-intelligence` | Add `https://mcp.pricingsaas.com` — see [mcp-setup.md](mcp-setup.md) |
| **Figma** | `monetization-surface-spec`, `monetization-design-reviewer` | Add `https://mcp.figma.com/mcp` |
| **Web search** | All skills — enrichment, benchmarks | Native to Claude — no setup needed |

Skills degrade gracefully when an MCP is unavailable and tell you what's affected.

---

## The skills

### `/monetization` — Router

The entry point. Reads your intent and routes to the right skill. Sequences multi-skill workflows automatically. Start here when you're not sure which skill applies, or when a task spans multiple skills ("research how competitors price this, then spec our version").

Produces no artifact of its own — it orchestrates.

---

### `/pricing-intelligence` — Competitive research

Research how any company prices. Map an industry landscape. Benchmark a pricing model ("how do AI companies sell credits?"). Monitor a watchlist for changes. Generate a pricing battlecard. Tear down a competitor's pricing page.

**Requires:** PricingSaaS MCP + web search

**Workflows:**

| What you ask | What you get |
|-------------|-------------|
| "How does Notion price?" | Company deep-dive — plans, packaging logic, history, what it means for monday.com |
| "How do AI companies sell credits?" | Model benchmark — credit unit names, package sizes, rollover policies, top-up UX across 8+ tools |
| "Map the work management pricing landscape" | HTML landscape report — all players, price bands, model patterns, market-level signals |
| "What changed in pricing this week?" | Weekly digest — watchlist changes, key moves, signal vs. noise |
| "Tear down Asana's pricing page" | Page teardown — hierarchy, copy psychology, what works and what doesn't |
| "Build a battlecard: monday vs Asana" | Battlecard — plan comparison, objection handling, negotiation intelligence |

All outputs log to the **Pricing Intelligence** board on monday.com automatically.

---

### `/monetization-surface-spec` — Spec and wireframe

Produce a complete spec and low-fi HTML wireframe for any monetization surface. Works from a brief ("I need a credit depletion modal for Pro users"), a Figma link, or a screenshot of an existing design.

**Requires:** Figma MCP (when working from an existing design)

**Surface types covered:**

| # | Surface | Triggered when |
|---|---------|---------------|
| 1 | Pricing page | Plan comparison — public or in-app |
| 2 | Paywall / feature gate | User tries to access a locked feature |
| 3 | Promotion | Discount, limited-time offer, upsell |
| 4 | Tier upgrade trigger | Usage limit hit, seat expansion |
| 5 | Credit / consumption UI | Running low, credit meter, top-up flow |
| 6 | Cancellation flow | User initiates cancel or downgrade |
| 7 | Trial flow | Trial start, mid-trial nudge, expiry |

**What you get for every surface:**

- `01-spec.md` — full structured spec: trigger condition, user cohort, section-by-section layout table, copy strategy, success metrics, edge cases (credit debt, admin-gated purchase, mobile, repeat exposure, enterprise)
- `02-wireframe.html` — low-fi interactive wireframe, all states, annotated

Copy writing is explicitly handed off to `/improve-conversion-surfaces-copy` — the spec names the reason and direction, the copy skill writes the options.

---

### `/monetization-design-reviewer` — CRO design review

Score any monetization design, screenshot, Figma frame, or wireframe against an 8-dimension CRO rubric (value clarity, timing, copy, friction, trust, escape hatch, hierarchy, mobile), weighted by surface type. Delivers a verdict and a single ranked punch list with severity, category, and effort for every fix.

**Requires:** Figma MCP (optional — screenshots work too)

**What you get:** `03-review.md` — weighted score out of 100, ship / don't-ship verdict, ranked improvement table, one benchmark example. Optional low-fi prototype of the fixed version.

---

### `/improve-conversion-surfaces-copy` — Conversion copy

Rewrite persuasive copy so every line maps to a real reason people buy, not a feature description. Works on headlines, CTAs, upgrade prompts, pricing tiers, and email. Picks up the reason and direction named in a spec or review automatically.

**What you get:** `04-copy.md` — 2–3 options per element, varied by angle, with one marked ★ Recommended and why.

---

## Your work persists

Every artifact lands in `.monetization/` in your working directory, numbered in workflow order:

```
.monetization/
├── credit-depletion-modal/
│   ├── 01-spec.md          ← /monetization-surface-spec
│   ├── 02-wireframe.html   ← /monetization-surface-spec
│   ├── 03-review.md        ← /monetization-design-reviewer
│   └── 04-copy.md          ← /improve-conversion-surfaces-copy
├── trial-expiry-screen/
│   ├── 01-spec.md
│   └── 02-wireframe.html
└── research/
    ├── notion-pricing-2026-09.md
    └── ai-credits-benchmark-2026-09.md
```

Every file uses the same header block (plugin, skill, feature, cohort, date, status). Returning to a feature later, the skill detects what's already there and picks up from the next step. Iterations get a version suffix instead of overwriting.

---

## Key principles

**Artifacts over answers.** Every skill produces a real deliverable — a spec doc, a wireframe, a research report — not a chat response. The artifact is what you hand to design or engineering.

**Skills chain.** Every artifact ends with a `→ Next step` block pointing to the logical next skill and a copy-pasteable prompt to trigger it. You shouldn't need to know the workflow — it's embedded in the output.

**monday.com context always applied.** AI credits, Vibe design tokens, tier structure, cohort differences (new user vs. existing), B2B PLG dynamics (IC hits the wall, admin buys) — all applied automatically without being asked.

**One source of truth for monday.com facts.** Plans, prices, AI credit packages, gating, and trial terms live in [`context/monday-context.md`](context/monday-context.md). Skills cite it instead of guessing. It has a named owner and a changelog — see the file header for how to update it.

**Copy is always handed off.** No skill writes final copy. The spec names the persuasion angle and the reason from the 15 reasons people buy — then explicitly routes to `/improve-conversion-surfaces-copy` for the actual rewrite with options.

---

## Repo structure

```
growth-monetization/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── CLAUDE.md                          ← plugin-wide rules and conventions
├── context/
│   └── monday-context.md              ← monday.com source of truth (owned, versioned)
├── templates/                         ← artifact header + research and spec templates
├── skills/
│   ├── monetization/                  ← router
│   ├── pricing-intelligence/
│   ├── monetization-surface-spec/
│   ├── monetization-design-reviewer/
│   └── improve-conversion-surfaces-copy/
└── mcp-setup.md
```

## Contributing

- **Updating monday.com facts:** edit `context/monday-context.md`, bump `last-updated`, add a changelog row
- **Changing a skill:** keep `SKILL.md` lean; put detail in the skill's `references/`
- **Adding a skill:** add a folder under `skills/`, then add it to the router table in `skills/monetization/SKILL.md` and to this README

## Coming in Wave 2

- `/monetization-data` — Kremer-backed conversion analytics: trial→paid funnels, credit consumption by segment, paywall performance, cohort upgrade analysis
- `/monetization-pm` — PRD writer, A/B experiment designer, pricing model workshop, launch readiness checklist

---

## Security

These files are instructions for local AI tools. Review skills before using them in sensitive contexts. Keep your API keys and MCP credentials on trusted machines.

---

## Built by monday.com Growth

Questions or contributions: open an issue or submit a PR.
