---
name: macro-regime-brief
description: Use when big-picture economy questions come up — "where are we in the cycle", "recession risk", "what's the macro backdrop", framing quarterly outlooks, or grounding portfolio positioning conversations in the current regime.
license: MIT
---

# Macro Regime Brief

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

A probabilistic read of the macro regime — cycle state, inflation, growth,
policy — that gives an advisor a defensible one-page backdrop for allocation
conversations, without pretending the cycle is knowable.

## Inputs

All optional: horizon of interest, portfolio context to connect the regime to.

## Lexfi MCP Calls

One parallel batch:

- `get_us_macro_regime` (12 months of series) — regime probabilities AND their trend
- `get_macro_inflation` (limit 24) — CPI/PCE trajectory
- `get_macro_economic_growth` — growth pulse
- `get_macro_yield_curve` (6 months) — what rates markets imply
- `get_rate_probabilities` (fed) — policy path pricing
- `get_macro_uncertainties` (180 days) — policy-risk overlay

Optional: `get_macro_forecasts` for model projections (the real forecast tool —
NOT `get_forecast`, which is weather); `get_macro_weekly_snapshot` for a
non-US country angle (catalog first).

## Workflow

1. **Regime now vs 6 months ago**: dominant regime probability + which probabilities are RISING — direction beats level.
2. **Pillars**: inflation (toward/away from target), growth (accelerating/decelerating), policy (restrictive/easing, per pricing), each in 2 lines: fact → signal.
3. **Coherence check**: do the pillars tell one story or contradict? Contradiction is the honest headline when present.
4. **Translate to allocation-relevant terms** — regime → what it historically means for stocks/bonds/cash conversations, framed as historical association, not forecast.

## Output Format

```
MACRO REGIME BRIEF — [date]

THE REGIME
**[Dominant regime], probability ~X%** — trend vs 6 months ago in one line.
Rising alternative: [regime] (signal to watch).

THE PILLARS
Pillar | Where it is | Direction | Read — inflation, growth, policy, uncertainty.

DOES IT COHERE?
One paragraph: the single story, or the named contradiction.

WHAT THIS REGIME USUALLY MEANS
3–4 lines connecting regime to portfolio conversation topics —
historical association, explicitly not prediction.

WHAT WOULD CHANGE THE PICTURE
2–3 concrete data triggers ahead (with dates from the calendar if near).

CLIENT-READY FRAMING (draft)
3 plain sentences describing the environment without jargon or forecasts.

Sources & data as-of: [one line]
```

## Quality Controls

- Regime stated as probability with trend, never "we are in X".
- Historical associations labeled as such.
- Contradictory pillars surfaced, not harmonized.
