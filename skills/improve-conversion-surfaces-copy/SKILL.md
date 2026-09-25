---
name: improve-conversion-surfaces-copy
description: Ground persuasive writing in a real reason people buy, not a feature description. Use when writing or editing copy meant to make someone buy, subscribe, sign up, or act — landing pages, ads, offers, positioning, pricing pages, upgrade prompts, email CTAs. Also use when auditing a draft that reads as feature-speak, when someone asks "why would anyone buy this?", "make this benefit-led", "what's the hook?", "this copy feels flat", or "sharpen this pitch."
version: 0.3.0
---

# Improve Conversion Surfaces Copy

People buy to move toward a feeling or an outcome, never to own a feature. Copy that names what a product *is* or *does* leaves the reader to supply the reason themselves, and most won't. Name the reason first; let the feature prove it.

## The deliverable — options, one pick

This is where the value is. For every element: name the reason, give **2–3 options that differ by angle** (not just wording), mark one **★ Recommended** with a one-line why. The framework below is how you get there; this format is what the reader uses.

When presenting options, show the reason, the options, and the pick — don't bury the recommendation in prose:

**Element:** "Current Trial" banner (Pro tier, mid-trial upgrade page)
**Reason:** To escape pain/guilt of losing what's already built
**Options:**
- "Your trial ends soon — keep what you built"
- ★ **Recommended** — "Keep everything you've built" *(shortest, leads with the loss directly instead of the deadline — deadline framing pulls focus to the clock, not the stakes)*
- "Don't lose your Pro setup"

Keep this compact — three short lines per option, not three paragraphs. The point is a fast scan, not a debate.

## Required context

Standalone runs follow the plugin's intake protocol ([CLAUDE.md](../../CLAUDE.md), "Intake — standalone runs"): check this table, infer what's obvious, ask every real gap in one message, then run. Inside a Growth PM chain, skip it.

| Field | Why it changes the output | Infer from |
|-------|--------------------------|-----------|
| Surface and element(s) | What's being written — a CTA, a headline, a whole modal | The prompt, the attached screen |
| Cohort / journey stage | Picks the reason: effort/pain for people who don't know the problem yet, status/recognition for people deciding | Surface type (trial → new, credit depletion → existing) |
| The action it must drive | The CTA and the outcome the headline promises | "get them to upgrade", "keep them from cancelling" |
| Current copy (if rewriting) | Needed to write "Replaces" and to avoid re-proposing what failed | Screenshot text, pasted copy |
| Hard constraints | Character limits, facts that must stay true (prices, trial terms — from `monday-context.md`), words legal won't allow | The prompt; facts always from the context file |

## The move

For every line meant to persuade:

1. **Name the reason.** Match the line to a reason on the list below. A line that maps to none is feature-speak — cut it or rewrite it. *Done when every retained line traces to one named reason.*
2. **Say the outcome, not the mechanism.** What the buyer gets ("stop losing an hour a day to this"), not how it works ("automated workflow engine").
3. **Lead with the reason, prove with the feature.** Reason in the headline or first line; the feature sits underneath as evidence.
4. **Write the actual line — as 2–3 options, one recommended.** A description of what's wrong or which reason to use isn't the deliverable — the rewritten copy is. But a single rewrite presented as *the* answer hides the judgment call behind it; the reader can't tell if this was the obvious choice or one of several reasonable ones. For every flagged line, write 2–3 real options and mark which one to use.
   - Vary the options by **angle, not just wording** — e.g. one leaning on the primary reason straight, one pairing it with a secondary reason or bias from the checks below, one shorter/punchier. Three ways of saying the same bland thing isn't three options.
   - Mark the recommended option with **★ Recommended** and one line on why (which reason it hits hardest, or why it fits the journey stage better than the others). The other options stay real alternatives, not strawmen — each should be something you'd actually be fine shipping.
   - Skip the multi-option treatment only for very short, low-stakes fixes (a button label, a tooltip) where one strong line is obviously enough — use judgment, don't pad trivial fixes with options nobody needs.

This applies to audits and teardowns too, not just from-scratch drafts. When reviewing an existing page, don't stop at diagnosis — for every piece of copy called out as feature-speak or reason-less, write the options that would replace it, with one recommended. A table of "issue → reason → suggested direction" is half the job; "issue → reason → these are the options, this is the pick" is the whole job.

## The list

The working spine — 15 reasons people buy stuff:

1. To avoid effort
2. To feel happier
3. To save time
4. To be comfortable
5. To escape pain or guilt
6. To make money
7. To save money
8. To get recognition
9. To be healthier
10. To feel secure
11. To alleviate fear
12. To feel special
13. To increase status
14. To feel loved
15. To get knowledge

Beneath every reason sits one of eight deeper drives (Josh Kaufman, *The Personal MBA*) — the reason wearing work clothes:

**money · status · power · love · knowledge · protection · pleasure · excitement**

Write from the 15; check against the 8 that you've found the real driver rather than a surface benefit.

## Checks

- **One primary reason per asset.** A page that argues five reasons equally makes the reader feel none. Pick the primary; demote the rest to support.
- **Match the reason to the journey stage.** Effort, time, pain, guilt, and fear pull people who don't yet know they have a problem; recognition, status, love, and feeling special close people already deciding.
- **Test the phrasing against how a real buyer talks** — their vocabulary, not yours. Language accuracy is what makes a line land; guessed language reads as an ad and gets skipped.

## Scope and handoff

This skill covers copy only — naming the reason and rewriting the words. It does not cover layout, visual hierarchy, credit-meter UI patterns, or scoring a page against a design rubric.

When a request asks for both — e.g. a full pricing-page or paywall teardown — do the copy pass here (name each section's reason, flag feature-speak, rewrite with options), then explicitly call out that the design/layout side (visual hierarchy, where proof sits relative to the fold, credit-meter UI, Figma-level critique) belongs to `monetization-design-reviewer` and should be run alongside this one rather than guessed at here.

The division is specific, not just "you do design, I do copy": `monetization-design-reviewer` scores copy quality as one of its rubric dimensions and flags *which* lines are weak and *why* (the missing or buried reason) — but it hands the actual rewrite to this skill rather than inventing one itself. When picking up a copy item flagged that way, treat the named reason as the starting point and produce the options-with-recommendation output described above, same as any other flagged line.

## References

Read `references/sources.md` when the top-level guidance isn't enough — it encodes the full source material:

1. The 15 reasons people buy stuff (the original list)
2. The core human drives — Josh Kaufman, *The Personal MBA*
3. Buyer psychology cheatsheet — 19 biases mapped to buyer-journey stages, each with an action (Customer Camp)

## Plugin output

This skill runs at three different points in the plugin's pipeline — which one determines the file and the framing. Check what's already in `.monetization/{feature-slug}/` before writing anything.

**In a Growth PM chain** (the Growth PM announced a sequence before this ran), omit the next-step block in every case below — the Growth PM runs the next step itself. See the chain mode rules in [monetization-growth-pm](../monetization-growth-pm/SKILL.md).

**Standalone pass — no spec, no review.** A direct request ("rewrite our upgrade CTA") with neither `01-spec.md` nor `04-review.md` behind it. After intake, write the options for the elements asked about; quote the current string for each when rewriting. Save to `.monetization/{feature-slug}/02-copy.md` (next version if one exists). End with a next-step block pointing to `monetization-design-reviewer` if there's a live design to check the copy in, or `monetization-surface-spec` if the surface doesn't exist yet.

**First pass — right after the spec, before the wireframe exists.** If `01-spec.md` exists and there's no `02-copy.md` yet, this is a first pass. Start from the spec's named reason and direction instead of re-deriving them. This is the copy the wireframe gets built from, so write real, ship-ready lines — not more placeholders for someone to fix later. Save to `.monetization/{feature-slug}/02-copy.md` with the header from [templates/ARTIFACT_HEADER.md](../../templates/ARTIFACT_HEADER.md), and end with:

```
---
→ Next step: monetization-surface-spec — build the wireframe using the ★ Recommended copy above
→ Prompt: "Build the wireframe in .monetization/{feature-slug}/ using the copy in 02-copy.md"
```

**Revision pass — after a review flags a specific line** (including every pass of the Growth PM's fix loop, which hands over the rows with Fix path `copy`). `02-copy.md` already exists; this isn't a fresh draft. Start from the reason named by the review version that flagged the line (`04-review.md`, or `04-review-v2.md` on a second pass) (the review already did the diagnosis) and revise only what was flagged — don't re-litigate lines the review didn't call out. Save as the next free copy version (`02-copy-v2.md`, then `-v3`…), with `fix-loop pass: {N}` in the header when the fix loop called it — version it, per the plugin's iteration convention, rather than overwriting. In the fix loop, the wireframe is rebuilt from this next; otherwise the Growth PM's synthesis phase runs next. The Growth PM also calls this pass once after the loop exits, for 🟡 rows whose recommendation needs a new string — same rules, next version number, no re-review.

**Review-first pass — an existing design was reviewed, no copy artifact exists yet.** `04-review.md` exists but `01-spec.md` and `02-copy.md` don't (typical when a screenshot or Figma frame of a live surface was shared). This is a first draft for those lines, not a revision. Take each Copy/CRO row in `04-review.md`, start from the reason it names, and write options for that element only — don't rewrite lines the review didn't flag. Also write the strings for any **new** on-screen element a non-copy row adds (a Free link, a tag, a risk-reducer line, a personalization line). Those rows own the placement, but the words still come from this skill. Leave them out and the synthesis has nothing verbatim to use. Quote the current on-screen string for each element so the synthesis can show what's being replaced. Save to `.monetization/{feature-slug}/02-copy.md`. The Growth PM's synthesis phase runs next.
