# Journey board — contract for `03-journey.html`

The board shows the whole journey on one page, with the real design on every step. It's built from `00-journey.md` (the steps and scenarios), the latest `03-wireframe` version (the on-surface screens) and the latest `02-copy` version (the words on off-surface steps). It adds no new design, only the arrangement.

## Contract

| Element | Rule |
|---|---|
| **File** | One self-contained `.html` in the same folder as the wireframe. Inline CSS and JS; the only external references are the wireframe file(s) it embeds by relative path. Readable in light and dark mode |
| **Header comment** | The artifact header fields, plus `Built from:` naming the journey, wireframe and copy versions |
| **Grid** | Columns = journey steps in J# order, grouped under the five stage headings (before · trigger · on-surface · hand-off · after). Rows = one lane per scenario (S1, S2, …), labelled with the scenario name and persona |
| **Cells** | A lane shows a card only on the steps its scenario passes through. Other cells are empty, so each scenario's path reads left to right. Branches (`J4a`, `J4b`) sit as stacked cards in the same column |
| **On-surface steps** | Embed the real state: `<iframe src="03-wireframe.html#{state}" loading="lazy" title="J{n} — {step}">`, rendered at 1280×800 and scaled down with a CSS transform to fit the card. Click, or Enter on focus, opens the state full size (a new tab, or an overlay with the iframe at 100%). Use the latest wireframe version from the ledger |
| **Off-surface steps** | A low-fi card per channel: email (subject, preview line, CTA), admin notification (who gets it, what it says, the action), invoice or billing line, sales handoff. Strings are the ★ Recommended options from the latest copy version. A string with no copy yet is a **dashed** open item `O{n}`, never lorem ipsum |
| **Card label** | `J{n} · {step}` · channel glyph · the state of mind and reason from the step table, in one line |
| **Pins** | `T{n}` friction pins on the card where the journey names friction, with the reduction in the side panel. Dashed `O{n}` pins for open items. Same visual language as the wireframe contract in [monetization-surface-spec](../../monetization-surface-spec/SKILL.md) |
| **Side panel** | Every pin, then per scenario: its path (J#s), its end state, and any gap from the coverage check. Collapsible, same toggle as the wireframe annotation panel |
| **Scenario filter** | Buttons (All · S1 · S2 · …) that dim every lane except the selected one. It's also reachable by URL hash (`03-journey.html#S2`), so each scenario renders for review without clicking |
| **Missing states** | An on-surface step whose state id isn't in the wireframe gets an empty frame labelled "missing state {id}", plus a panel entry. It's never silently skipped |
| **Tokens** | The wireframe's CSS variables (neutral greys named for Vibe tokens, per [wireframe-patterns.md](../../monetization-surface-spec/references/wireframe-patterns.md)). Channel and stage differences don't depend on color alone (glyph plus label) |
| **Mobile** | At ≤600px, lanes stack: one scenario at a time (the filter becomes a select), steps top to bottom, and iframes are replaced by a "View J{n}" link that opens the state. No horizontal overflow at a true 375px viewport |

## Skeleton

```html
<!-- plugin: growth-monetization · skill: monetization-journey-map · feature: {slug}
     Built from: 00-journey.md · 03-wireframe{-vN}.html · 02-copy{-vN}.md -->
<header>
  <h1>Journey: {surface}</h1>
  <nav class="scenario-filter">[All] [S1 {name}] [S2 {name}] …</nav>
  <button id="toggle-panel">Annotations</button>
</header>
<main class="board" style="--steps: {N}">
  <div class="stage-row">before · trigger · on-surface · hand-off · after (spanning their columns)</div>
  <section class="lane" id="S1">
    <h2>S1 · {scenario} — {persona}</h2>
    <article class="card on-surface" data-j="J3">
      <div class="thumb"><iframe src="03-wireframe.html#reason" loading="lazy" title="J3 — Reason"></iframe></div>
      <p class="label">J3 · Reason · in-app · "wants out fast" · avoid effort</p>
      <span class="callout callout-touch">T2</span>
    </article>
    <article class="card off-surface email" data-j="J8">…subject, preview line, CTA from 02-copy…</article>
  </section>
  …
</main>
<aside id="annotation-panel">…pins, per-scenario path and end state…</aside>
```

Scale the embedded frame with `transform: scale(var(--thumb-scale))` on a fixed 1280×800 iframe inside an `overflow: hidden` box, so the wireframe renders at desktop width and shrinks as a picture, instead of reflowing into a squeezed mobile layout.

## Review renders

The Growth PM renders the board next to the wireframe states: `renders/v{N}-journey.png` at 1440px, plus one render per scenario hash (`#S1`, `#S2`) and a true-375px render ([Capturing screens](../../monetization-growth-pm/SKILL.md#capturing-screens-for-a-review)).
