---
name: monetization
description: This skill should be used when the user's intent is unclear or spans multiple monetization skills, or when they say "monetization copilot", "help me with monetization", "where do I start", "not sure which skill to use", "I'm working on [any monetization surface or research task]". This is the router — it reads intent, maps to the right skill, and orchestrates multi-skill workflows. It produces no artifact of its own.
version: 0.1.0
---

# Monetization Copilot — Router

Read the user's intent and route to the correct skill. This skill produces no artifact. It orchestrates.

Use this when:
- The request is vague or spans more than one skill ("help me design and research a paywall")
- The user doesn't know which skill applies
- A task requires multiple skills run in sequence

---

## Routing table

| What the user says | Route to | What it does |
|-------------------|---------|-------------|
| "research how X prices", "competitive pricing", "how do companies sell AI credits", "benchmark our model" | `pricing-intelligence` | Competitor research, landscape scans, model benchmarking |
| "review this design", "critique this paywall", "score this upgrade modal" | `monetization-design-reviewer` | CRO rubric score + prioritised improvement list |
| "spec out a surface", "wireframe a paywall", "design brief for a trial flow", "I need a spec for..." | `monetization-surface-spec` | Full spec + low-fi wireframe |
| "write copy for this CTA", "rewrite this upgrade prompt", "the copy feels flat" | `improve-conversion-surfaces-copy` | Benefit-led copy rewrite with 2–3 options |
| Multi-step / unclear | Continue below → |

---

## Multi-skill workflow patterns

When a request spans multiple skills, sequence them in the right order and hand the user off explicitly.

### Research → Spec
> "I want to design a credit top-up flow — can you research how other tools do it and then spec ours?"

Sequence:
1. `pricing-intelligence` → monetization model benchmarking (sub-workflow B: AI credits)
2. `monetization-surface-spec` → credit UI spec, using benchmark findings as input

Handoff: "I'll start with the benchmark research. Once that's done, I'll use the findings to spec the surface — you'll end up with both a competitive picture and a ready-to-use spec."

---

### Spec → Copy → Wireframe → Review
> "I need to build a paywall for AI Agents on Free tier, get it reviewed, and write the copy"

Sequence:
1. `monetization-surface-spec` → paywall spec (`01-spec.md`) — names the reason and direction, doesn't write final copy
2. `improve-conversion-surfaces-copy` → the actual headline/CTA copy from that reason (`02-copy.md`)
3. `monetization-surface-spec` (re-invoked) → wireframe built with the real copy, not placeholders (`03-wireframe.html`)
4. `monetization-design-reviewer` → CRO score of the real thing (`04-review.md`) — a flagged copy line is a revision request against `02-copy.md`, not a first draft

Handoff: "I'll spec the paywall, write the actual copy from that spec's reason, build the wireframe around that real copy, then score the whole thing. Four artifacts by the end, and the review will be scoring real language, not placeholder text."

---

### Review → Spec (from existing design)
> "Here's our current upgrade modal — it's not converting well, help me fix it"

Sequence:
1. `monetization-design-reviewer` → score the existing design, identify root cause
2. `monetization-surface-spec` → re-spec the surface with fixes applied
3. If the fix touches copy: `improve-conversion-surfaces-copy` → the actual replacement lines, then `monetization-surface-spec` rebuilds the wireframe with them — same rule as a fresh spec, real copy before the wireframe, not after

Handoff: "I'll start by scoring the existing design to pinpoint what's failing, then produce a revised spec. You'll see exactly what's wrong before we design the fix."

---

### Research → Positioning
> "How does Asana price compared to us? We're about to run a pricing page test"

Sequence:
1. `pricing-intelligence` → company research (Asana) + pricing page teardown
2. Offer: `monetization-surface-spec` → spec a pricing page variant using competitive findings

---

## When intent is still unclear

Ask one question — the answer will route unambiguously:

> "Are you trying to (a) research a competitor or industry, (b) spec or wireframe a surface, (c) review an existing design, or (d) write copy for a surface?"

Don't ask more than one. Don't explain the skills before asking.

---

## Output from the router

The router's only output is a routing decision + handoff message. Format:

```
**Routing to:** {skill-name}
**Why:** {one sentence}
**What you'll get:** {artifact names and what they contain}

Starting now → [proceeding to skill]
```

For multi-skill sequences:

```
**Sequence:** {skill 1} → {skill 2} → {skill 3}
**Artifacts:** {list — e.g. "benchmark research doc, spec doc, wireframe HTML, copy options"}
**Starting with:** {skill 1 name} — {one sentence on what it does first}
```

Then immediately begin the first skill. Don't wait for the user to confirm the routing.
