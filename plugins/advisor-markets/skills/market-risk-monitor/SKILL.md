---
name: market-risk-monitor
description: Use when assessing how stressed or complacent markets are — "how risky is the market right now", "are we seeing stress", "check risk conditions", before risk-heavy client conversations, or on volatility spikes.
license: MIT
---

# Market Risk Monitor

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

A cross-indicator risk dashboard with a single honest verdict: are conditions
normal, elevated, or stressed — each indicator read against its own history,
not in isolation.

## Inputs

All optional: lookback for context (default 6 months), specific worry to probe
(rates, credit, geopolitics).

## Lexfi MCP Calls

One parallel batch:

- `get_daily_vix_index` (6 months) — level AND trend vs history
- `get_macro_yield_curve` (6 months) — 2s10s slope and direction
- `get_cnn_fear_greed_index` — equity sentiment (NOT `get_fear_greed_index`, which is crypto)
- `get_macro_uncertainties` (180 days) — policy/geopolitical/trade uncertainty vs range
- `get_sector_performance` — defensives vs cyclicals leadership
- `get_macro_credit_liquidity` — credit conditions
- `get_us_macro_regime` — recession-stress probability trend

## Workflow

1. Pull batch. For each indicator compute: current level, percentile-ish position in the lookback window, direction over 2 weeks.
2. Score each: NORMAL / ELEVATED / STRESSED, with the comparison that justifies it ("VIX 24 vs 6-month median ~15").
3. Look for divergences (e.g., vol calm while uncertainty indices spike) — divergence is signal, report it.
4. Verdict: the overall read plus the 1–2 indicators driving it. Never average away a red flag: one STRESSED indicator is named in the verdict even if the composite is calm.

## Output Format

```
MARKET RISK MONITOR — [date]

VERDICT
**NORMAL / ELEVATED / STRESSED** — one sentence of justification.

DASHBOARD
Indicator | Now | vs 6-mo range | 2-wk direction | Read
(VIX, 2s10s, equity F&G, uncertainty, credit, defensives-vs-cyclicals,
recession-stress prob)

DIVERGENCES & NOTES
What doesn't line up, and one marked interpretation of why.

WHAT WOULD CHANGE THE VERDICT
2–3 concrete triggers (levels/events), so the advisor knows what to watch.

CLIENT CONVERSATION ANGLE
2 lines: how to frame current risk conditions with a nervous (or greedy) client.

Sources & data as-of: [one line]
```

## Quality Controls

- Every read is level-vs-history, never raw level alone.
- VIX changePercent decimal trap handled (playbook).
- Verdict language is probabilistic; no crash calls, no all-clears.
- Divergences reported, not resolved by fiat.
