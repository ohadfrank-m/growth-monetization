---
name: monetization-surface-spec
description: This skill should be used when the user wants to "spec out a paywall", "wireframe a credit depletion modal", "design brief for an upgrade flow", "create a spec for a pricing page", "build a trial expiry screen", "spec a cancellation flow", "what should a credit meter look like", "create an upgrade trigger for [feature]", "write a design brief for a monetization surface", "I need a spec for [any of — paywall, feature gate, upgrade prompt, credit top-up, trial flow, cancellation screen, pricing page]". Produces a structured spec artifact and low-fi HTML wireframe. Connects to Figma MCP when a design already exists.
version: 0.6.0
---

# Monetization Surface Spec

Produce a complete spec artifact and low-fi HTML wireframe for any monetization surface. The spec is the contract between PM and design — specific enough that two designers produce the same surface from it.

This skill is invoked twice per surface, not once: first to write the spec (names the reason and hands off for copy), then again — after `improve-conversion-surfaces-copy` has written the real headline/CTA copy — to build the wireframe around that real copy. Don't collapse these into one pass; a wireframe built before copy exists ships with placeholder text nobody ever comes back to fix.

This skill covers both modes:
- **From brief:** "I need a paywall for AI Agents on Free tier" → generates full spec + wireframe
- **From existing design:** "Here's our current credit modal, turn it into a proper spec" → reverse-engineers spec from design, identifies gaps

---

## Input handling

Accept any of the following as input:

- **Natural language brief** — "I need a spec for..." → run [brief-intake.md](references/brief-intake.md) to extract the required fields, then proceed
- **Figma link** — use Figma MCP to pull design context before speccing (see Figma ingestion below)
- **Screenshot or image** — analyze the existing design, then spec it
- **Existing partial spec** — fill the gaps and produce the wireframe
- **Benchmark output** — from `monetization-intelligence`, translate findings directly into a surface spec
- **Journey map** — `00-journey.md` from `monetization-journey-map`: the scenarios, the steps and the wireframe state ids come from it (see the flow map rule in Step 4). Read it before anything else when it exists

When input is minimal (just a surface name), run the brief intake before proceeding — don't produce a spec from vague input.

---

## Surface types

Identify the surface type first. It determines which reference file and which spec sections are mandatory.

| # | Surface | When it appears | Reference | Playbook (CRO rationale, benchmarks, examples) |
|---|---------|----------------|-----------|-----------|
| 1 | **Pricing page** | Public or in-app plan comparison | [pricing-pages.md](references/pricing-pages.md) | [pricing-pages.md](../../playbooks/pricing-pages.md) |
| 2 | **Paywall / feature gate** | User tries to access a locked feature | [paywalls.md](references/paywalls.md) | [paywalls.md](../../playbooks/paywalls.md) |
| 3 | **Promotion** | Discount, limited-time offer, upsell banner/modal | [promotions.md](references/promotions.md) | [promotions.md](../../playbooks/promotions.md) |
| 4 | **Tier upgrade trigger** | Usage limit hit, seat expansion, plan upgrade nudge | [upgrade-triggers.md](references/upgrade-triggers.md) | [upgrade-triggers.md](../../playbooks/upgrade-triggers.md) |
| 5 | **Credit / consumption UI** | Running low on credits, credit meter, top-up flow | [credit-ui.md](references/credit-ui.md) | [credit-ui.md](../../playbooks/credit-ui.md) |
| 6 | **Cancellation flow** | User initiates cancel or downgrade | [cancellation.md](references/cancellation.md) | [cancellation.md](../../playbooks/cancellation.md) |
| 7 | **Trial flow** | Trial start, mid-trial nudge, trial expiry | [trial-flows.md](references/trial-flows.md) | [trial-flows.md](../../playbooks/trial-flows.md) |

If the surface type is ambiguous, ask — one question.

The reference file per type covers what to put *in the spec*. The playbook covers *why* — read it before drafting; don't skip to the reference file alone.

---

## Figma ingestion (when design exists)

When given a Figma link, pull design context before writing the spec:

1. `get_design_context` or `get_metadata` — frame structure, layers, component instances
2. `get_screenshot` — visual hierarchy and mobile readiness assessment
3. `get_variable_defs` — check Vibe token binding; flag any hardcoded values

Read copy directly from layer text. If the MCP can't reach the frame, ask for a screenshot — one request.

---

## Workflow

### Step 1: Brief intake

If input is a brief or surface name, extract these fields before proceeding. Ask only what's missing — don't re-ask what's already provided.

Required fields:
- **Surface type** — from the 7 types above
- **Trigger condition** — exact condition that shows this surface (e.g., "credit balance < 50", "user clicks locked feature", "trial day 7")
- **User cohort** — new-user (urgency lever) or existing-user (capability lever)
- **Tier context** — which tier(s) this applies to
- **Primary objective** — the single conversion outcome
- **Existing design, if any** — a live version changes the spec from greenfield to redesign (read it first)

For missing fields: infer from context where obvious (a "credit depletion modal" is surface type 5, existing-user cohort). Ask every genuinely ambiguous one together, in one message — the plugin's intake protocol ([CLAUDE.md](../../CLAUDE.md), "Intake — ask, never assume"). Inside a Growth PM chain, the Growth PM asked these up front; stop and ask only for a gap it didn't cover. Never fill a gap with a guess and flag it.

Full intake protocol: [brief-intake.md](references/brief-intake.md)

### Step 2: Load surface type reference

Read the reference file for the identified surface type. It contains:
- The states the surface can be in
- Mandatory spec sections for this surface
- The trigger logic block (conditions, frequency cap, dismiss, re-show)
- Pattern decision rules and surface-specific edge cases

Best-in-class patterns, benchmarks and anti-patterns live in the surface's playbook, which the reference links to — read both.

### Step 3: Research (optional but recommended)

Standalone, offer benchmark research **inside the intake message** (one more question, not a second round trip): "Pull 3 best-in-class examples of this surface before I write the spec?" — recommended Yes for a new surface.

If yes, start from the surface's playbook examples in [../../playbooks/](../../playbooks/), then run web research for current ones. Results feed directly into the References section of the spec.

In a Growth PM chain, don't ask. If the chain produced a research artifact (`.monetization/research/{topic-slug}-{YYYY-MM}.md`, path passed by the Growth PM), read it: cite its competitor examples in the References section and use its "So what for monday.com" section to shape the copy direction — no fresh web research. Without one, use the surface's playbook examples for References.

### Step 4: Write the spec

Check the anti-patterns in [spec-checklist.md](references/spec-checklist.md) before and after drafting.

Use the surface spec template: [../../templates/surface-spec.md](../../templates/surface-spec.md)

Apply monday.com context from [monday-context.md](../../context/monday-context.md) throughout — don't wait to be asked.

**Flow map — every surface is a journey, not a screen.** Monetization surfaces rarely live on one screen: cancel → reason → save offer → confirmation; limit hit → upgrade prompt → checkout → back to work. Map the journey before the layout:

- **When `00-journey.md` exists, the journey owns the steps.** The flow map is its on-surface and hand-off rows, in order, each cited by J#, with the journey's friction → reduction carried over. Don't re-derive or reorder them. User context lists the journey's scenarios (S1…Sn) with their frequencies, and the scenario-ranked primary edge cases are treated as main paths. If the spec needs a step the journey lacks, add it as `J{n}+` and say why, so the journey can be updated.

- **Multi-screen surfaces** (cancellation, upgrade → checkout, trial start and expiry, credit top-up, paywall → trial start): a flow map table, one row per screen, in order — `# · Screen · Purpose · Key elements · Arrives from · Goes to (incl. abandon) · Friction point · Reduction`. Every screen names its friction point — where a user is likely to hesitate, get confused, or drop off — and the design choice that reduces it. If a screen truly has none, write "none" and why.
- **Single-screen surfaces** (a banner, an inline gate): one line naming the screen before (what the user was doing) and the screen after (where each action lands), with the friction at the hand-off.
- If a surface benchmark exists for this surface, build the flow map from its "Flow implications for the spec" and cite the competitors each screen borrows from.

**Copy strategy section:** Name the primary reason from the 15 reasons people buy, name the copy direction, and explicitly hand off to `improve-conversion-surfaces-copy`. Never write final copy in the spec.

**Success metrics — real baselines only.** Every baseline in the Success metrics table comes from `00-sizing.md` (`monetization-opportunity-sizing`) or from a Kramer query shown in the spec, with its source tag. This section is behind the plugin's Data gate ([CLAUDE.md](../../CLAUDE.md), "Data gate — real data is required"): check for a `data-expert-agent` / `kramer` tool before writing the spec. With none, stop before writing anything and name the missing MCP. Never write a `{slot}` baseline. The target is at least the MDE the traffic supports — a smaller target can't be read.

**Edge cases:** Address every edge case in [spec-checklist.md](references/spec-checklist.md) — credit debt, admin-gated purchase, mobile, repeat exposure, enterprise, loading/empty/error states. Mark non-applicable ones as N/A with one-line rationale — no silent omissions.

### Step 5: Deliver the spec, then hand off for copy — before the wireframe

Write the spec to: `.monetization/{feature-slug}/01-spec.md`

Do **not** build the wireframe yet. The wireframe gets built from the real headline/CTA copy `improve-conversion-surfaces-copy` writes next — not from placeholder text. Building it now and rewriting it later wastes a pass and means the wireframe never actually reflects the words it'll ship with.

End the spec with the next step block — unless this is running in a Growth PM chain, in which case omit it and let the Growth PM continue (see chain mode rules in [monetization-growth-pm](../monetization-growth-pm/SKILL.md)):
```
---
→ Next step: improve-conversion-surfaces-copy — write the actual headline/CTA copy from the reason and direction named above
→ Prompt: "Write copy for .monetization/{feature-slug}/01-spec.md"
```

### Step 6: Build the wireframe — re-entry point, after copy exists

This is a separate invocation of this skill, triggered once `.monetization/{feature-slug}/02-copy.md` exists (the user asks to build the wireframe, or continues the chain from copy's own next-step prompt). If `02-copy.md` doesn't exist yet when this is invoked, stop and hand off to `improve-conversion-surfaces-copy` first — don't build a wireframe with bracketed placeholder text when real copy is one skill call away.

Produce a low-fi HTML wireframe that follows the **wireframe contract** below. The contract lives here, in the skill, so every run — and every environment, including one without the `references/` folder — produces the same shape. [wireframe-patterns.md](references/wireframe-patterns.md) adds per-surface layouts on top; it never overrides the contract.

#### Wireframe contract

| Element | Rule |
|---------|------|
| **File** | One self-contained `.html` — inline CSS and JS, no external assets, readable in light and dark mode |
| **Header comment** | The artifact header fields, plus `Built from:` (which spec and copy versions) and, in revision mode, `fix-loop pass:` and `Fixes:` (the review rows applied) |
| **Copy** | Every visible string is the ★ Recommended option from the latest copy version, verbatim. Slots stay as `{slot}`; sample values (names, counts) are allowed only if the annotation panel says they're samples |
| **States** | Every state the spec defines (e.g. healthy / warning / critical / depleted, default / non-admin / trial-used), each reachable from a **state switcher** row of buttons at the top **and** from the URL hash — `03-wireframe.html#critical` opens that state, so each can be rendered for review without clicking. When `00-journey.md` exists, every J step with a **Wireframe state** id is a state here with exactly that id: the journey board embeds `03-wireframe.html#{id}`. Read the state from the hash in script and switch it through a `data-state` attribute; never give a DOM element `id="{state}"`, or a page embedding the wireframe by hash scrolls to that element and the frame renders blank |
| **Hierarchy** | Sections in the spec's top-to-bottom order; the primary CTA is the only filled button on screen |
| **Escape hatch** | Always visible in every state that asks for anything |
| **Flow strip** | Multi-screen surfaces show the screens as a left-to-right sequence with arrows between them, in flow-map order, above or instead of the state switcher (each screen still opens by URL hash). Abandon paths are drawn as a branch off the step where they happen |
| **Pins** | A small numbered/lettered circle on each annotated element: spec section letters (`A`, `D6`), review rows it fixes (`R1.3`, `R2.1`), a **dashed** pin for anything blocked on an open item (`O3`), and a **touchpoint pin** `T{n}` on each friction point from the flow map, with its reduction in the annotation panel |
| **Annotation panel** | A side panel (stacked below on mobile) listing every pin: what the element does, trigger/dismiss rules, and what each dashed pin waits on. In revision mode, a "What changed in vN" list first |
| **Tokens** | Neutral greys, declared as CSS variables named for the Vibe token each stands in for (`--vibe-warning`). Name a real Vibe token only if confirmed via Figma variables or the Vibe MCP; otherwise "token TBD". States must differ without color too (pattern, glyph, border weight) |
| **Mobile** | At ≤600px: single column, the state's main banner or CTA first, persistent chrome (meters, sidebars) collapsed to a header row. No horizontal overflow at a true 375px viewport |

Keep it low-fi — structure and hierarchy, not final visual design. The copy is real and ship-ready even though the visual treatment isn't.

Output: `.monetization/{feature-slug}/03-wireframe.html`

Build the wireframe by default once copy exists. Skip it only if the user asks for the spec and copy alone.

**From a requirements doc (after the Review → Fix → Synthesize chain).** If `05-requirements.md` exists, build from it instead of `01-spec.md` + `02-copy.md` — it's the resolved version of both. Use its Final copy strings verbatim and apply every Design change. Keep the `03-` filename even though it's written after `05-`: the number identifies the artifact type, not the order it was produced.

**Annotation rule — critical:** Never render `C#` / `D#` / `O#` annotations as inline DOM elements inside the wireframe body. Inline badges interrupt visual hierarchy and make the wireframe unreadable as a design artifact. Instead:
- Place a small circular callout marker (absolute-positioned, 24px, non-disruptive) on the corresponding wireframe element
- List all annotation text in the fixed right-side annotation panel
- Open items get a **dashed** `O#` marker and, when two states are possible, a toggling prototype control in the wireframe — not a placeholder

Use the annotation-panel structure, CSS classes and toggle script in [references/wireframe-patterns.md](references/wireframe-patterns.md#annotation-panel--mandatory-pattern). Where that file and the wireframe contract above differ — dashed open-item pins, `T{n}` touchpoint pins, the flow strip, URL-hash states — the contract wins.

### Step 7: Revision mode — inside the Growth PM's fix loop

Triggered when the Growth PM passes review rows with Fix path `wireframe` or `spec` (see the Growth PM's [Fix loop](../monetization-growth-pm/SKILL.md)). This revises the chain's own design; it isn't a fresh spec.

- **Apply only the rows passed in.** Don't re-litigate the rest of the design — unflagged sections stay exactly as they were.
- **`spec` rows first:** write `01-spec-v{N}.md` (next free number) with only the flagged sections changed, then rebuild the wireframe from it.
- **Wireframe:** write `03-wireframe-v{N}.html`, where N is the next free version number for the wireframe; put `fix-loop pass: {1|2}` in the header. Use the ★ Recommended strings from the **latest** copy version — the copy skill runs before this in each pass.
- **Pin every changed element** with its review row (`R1.3` = row 3 of `04-review.md`, `R2.1` = row 1 of `04-review-v2.md`) in the annotations, so the re-review can find each fix without diffing.
- **Partly-blocked rows:** build the fixable part with a visibly marked `{slot}` or a prototype switch between the possible answers; never guess the missing fact.
- Never overwrite an earlier version.

End with the next step block — omitted in a Growth PM chain, same as above:
```
---
→ Next step: monetization-design-reviewer — score the spec, copy, and wireframe together
→ Prompt: "Review .monetization/{feature-slug}/"
```

---

## Output standards

- Use the artifact template: [../../templates/surface-spec.md](../../templates/surface-spec.md)
- Header block on every file
- Surface structure table is non-negotiable — no prose layout descriptions
- Copy strategy names the reason, states the direction, hands off — never writes final copy in the spec itself
- Edge cases addressed even when N/A
- Wireframe always delivered as an `.html` file, never inline — without a filesystem (a chat session), deliver the same self-contained HTML as a code block or artifact, and name it in the ledger
- Wireframe is always built *after* `improve-conversion-surfaces-copy` has run — never with bracketed placeholder text when real copy exists one skill call away

---

## monday.com context

Read [context/monday-context.md](../../context/monday-context.md) before every spec for current tiers, prices, AI credit packages, feature gating, trial terms, and cohorts. It's a cache: verify every price, limit, credit amount, gate and trial term the spec cites against BigBrain (search for `AI Brain` / `bigbrain`; in a Growth PM chain, use the answers from its Step 1c) and cite `[Brain — {name}, {date}]`. A mismatch with the context file is listed in the spec's Open items and told to the user, never silently used ([CLAUDE.md](../../CLAUDE.md), Source of truth). Never quote a price or limit from memory.

---

## Additional references

- Brief intake protocol: [brief-intake.md](references/brief-intake.md)
- Surface-type specific guidance (what goes in the spec): in `references/` per surface type
- CRO rationale, benchmarks, and best-in-class examples per surface type (shared with `monetization-design-reviewer` — owned once, cited here, never duplicated): [../../playbooks/](../../playbooks/)
- Wireframe patterns and best-in-class examples: [wireframe-patterns.md](references/wireframe-patterns.md)
- Copy hooks per surface type: [copy-hooks.md](references/copy-hooks.md)
- Anti-patterns and edge cases: [spec-checklist.md](references/spec-checklist.md)
- monday.com strategy and pricing data: [context/monday-context.md](../../context/monday-context.md)
- Surface-type quick index: [surface-types.md](references/surface-types.md)
