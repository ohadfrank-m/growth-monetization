# Paywalls & feature gates — CRO playbook

Surface type 2. Cited by `monetization-surface-spec` (write the spec) and `monetization-design-reviewer` (score against these benchmarks).

## Core principle
A paywall is a value conversation, not a wall. The best paywalls feel like a natural offer, not an interruption. Users should leave thinking "that makes sense" not "I got blocked."

## Paywall trigger types

| Trigger | Context | Key design constraint |
|---------|---------|----------------------|
| Feature gate | User clicks locked feature | Must show the feature value *before* the ask |
| Usage cap | User hits limit (seats, items, actions) | Show progress toward limit proactively — not just at 100% |
| Trial expiry | Trial period ending | Personalize with what they built/used during trial |
| Time-based nudge | N days of free use | Lowest urgency — must be dismissible, never recurring |
| Aha moment upsell | After key activation milestone | Highest intent — convert here |

## Paywall screen components (ranked by importance)

1. **Headline** — benefit-led, not feature-led. "Get unlimited automations" > "Upgrade to Pro"
2. **Feature preview** — screenshot, animation, or description of what they're unlocking. Never skip this.
3. **Differentiator line** — one sentence on why this feature exists / what pain it solves
4. **Price anchoring** — show monthly equivalent even if billed annually. Show savings vs monthly.
5. **Primary CTA** — specific: "Unlock Automations", "Start Pro — $X/mo"
6. **Secondary path** — downgrade, continue free, or "remind me later" — must be visible
7. **Social proof** (optional but lifts) — "Used by 50,000+ teams"

## Modal vs. full-page vs. inline

| Format | When to use | Conversion notes |
|--------|------------|-----------------|
| Modal | Feature gate, usage cap | High intent context — converts well if triggered correctly |
| Full page | Trial expiry, plan comparison | More deliberate — use when user has time to decide |
| Inline nudge | Low-urgency upsell, approaching limit | Non-blocking — lower CVR but lower annoyance |
| Tooltip / hover | Discovery of locked features | Awareness, not conversion — don't over-optimize here |

## Copy patterns that work

**Headline formulas:**
- "Unlock [Feature] to [Outcome]"
- "You're one step away from [Benefit]"
- "[Feature] is a Pro feature — here's why teams love it"
- "You've hit your free limit — here's what's next"

**CTA formulas:**
- "Unlock [Feature Name]" (most specific, highest CVR)
- "Start [Plan] — $X/month" (price-transparent, builds trust)
- "Continue with Pro" (trial-to-paid context)

**Avoid:**
- "Upgrade now" — zero benefit signal
- "Go Premium" — meaningless without context
- "Subscribe" — transactional, cold

## Timing rules

- **Do not show** during onboarding (first session, before activation)
- **Do not show** mid-task if the task doesn't require the locked feature
- **Wait 24–48h** after a dismiss before showing again
- **Session cap:** max 1 paywall per session (excluding feature gates triggered by user intent)
- **Best moment:** immediately after the user has completed something meaningful (just created their first board, just ran their first automation, etc.)

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Gate with no feature preview | User can't tell what they'd gain |
| Pushing a higher tier than needed to unlock the feature | Friction, feels like a bait-and-switch |
| Generic "This feature requires Pro" with no outcome named | Functional, not motivating |

## Benchmarks

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Paywall → upgrade CTR | <3% | 5–10% | 15%+ |
| Trial expiry paywall CVR | <10% | 15–25% | 30%+ |
| Feature gate CTR (high intent) | <8% | 12–18% | 25%+ |

## Best-in-class examples

**Notion** — Feature gate paywalls show a live preview of the blocked content blurred behind the modal. User can see exactly what they're missing. CVR benchmark: ~18–22% on database-related gates.

**Figma** — Trial expiry screen uses "Here's what you built" personalization with actual file thumbnails. Anchors loss aversion to real work, not abstract features.

**Linear** — Usage cap modals show a progress bar with team context ("Your team has created 95/100 issues this month"). Social proof of team usage increases urgency without guilt.

**Loom** — "You've watched this 3x" re-engagement paywall on high-value content. Intent signal used to time the ask.

## monday.com-specific notes

- AI Agents paywall: must show a preview of what the agent would *do* — not just that it exists. Show the output.
- Credit gates: "You've used X of Y AI credits" is not a paywall headline — it's a metric. Lead with what stops working when credits run out.
- Agentic flows: if a paywall interrupts an agent mid-task, the experience is broken. Design for non-blocking upgrade paths in agent contexts — inline banner, not full-screen modal.
- Existing users hitting credit walls: these users have no urgency lever (time-unlimited balance). The hook must be capability, not scarcity.
