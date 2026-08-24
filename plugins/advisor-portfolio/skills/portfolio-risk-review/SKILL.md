---
name: portfolio-risk-review
description: Use when reviewing what risks a portfolio actually carries — "review the risk in this portfolio", "concentration check", "how exposed is this book to rates", before client risk conversations or after market regime shifts.
license: MIT
---

# Portfolio Risk Review

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

A structural risk read of a portfolio — concentration, sector tilts, macro
sensitivities, and a narrative stress sketch — grounded in current market
conditions, producing conversation material for the advisor, not a compliance
document or an optimizer output.

## Required Inputs

Holdings WITH weights (or amounts). Without weights, ask once; if unavailable,
proceed equal-weighted and label every conclusion accordingly.

## Optional Inputs

Benchmark, client risk profile/mandate, specific worry to stress.

## Lexfi MCP Calls

- **Batch 1 (parallel):** `get_stock_quote` (all tickers, one call),
  `get_company_profile` for names whose sector is unknown, `get_etf_holdings`
  for ETF positions ≥5% (look through them), `get_sector_performance`,
  `get_us_macro_regime`, `get_daily_vix_index` (3 months),
  `get_macro_yield_curve` (3 months).
- **Batch 2 (targeted):** `get_key_metrics` for the top-5 weights (leverage,
  valuation vulnerability).

## Workflow

1. **Map the book**: weights by name → sector → theme. Look through material ETFs. Compute top-1/top-5/top-10 concentration and effective number of positions (state the arithmetic).
2. **Tilts**: sector weights vs benchmark if given, vs broad-market sector mix otherwise (labeled as such).
3. **Macro sensitivities** — qualitative, evidence-tied: rate sensitivity (duration proxies, financials/growth mix), cycle sensitivity (cyclicals share, regime probabilities), single-theme dependence (e.g., AI-capex names across sectors counted as ONE cluster).
4. **Stress narrative**: for the current regime's 1–2 most plausible adverse scenarios, walk through which holdings get hit and roughly how hard — a reasoned story with named channels, explicitly NOT a quantitative stress test.
5. **Rank findings** by size × plausibility; keep the top 3–5.

## Output Format

```
PORTFOLIO RISK REVIEW — [book] — [date]

HEADLINE READS (3–5)
Bolded one-liners, ranked. The risks this portfolio actually carries.

CONCENTRATION
Top-1/5/10 weights, effective positions, single-name flags (>8% ≈ attention,
>15% ≈ headline). Cross-holding theme clusters.

SECTOR & THEME TILTS
Table vs [benchmark/market], only tilts >±3pts, with the risk each implies.

MACRO SENSITIVITIES
Rates / cycle / dominant theme — each: exposure (fact) → channel (signal) →
read (interpretation).

STRESS SKETCH: [scenario]
Narrative walk-through, clearly labeled qualitative.

CONVERSATION STARTERS
3 questions the advisor can put to the client, tied to the reads above.

Sources, assumptions & data as-of: [includes equal-weight caveat if applicable]
```

## Quality Controls

- All arithmetic shown or reproducible; no black-box scores.
- "Qualitative, not a stress test" labeled where applicable.
- Theme clusters counted across sectors (the 2025 lesson: sector diversification can hide one trade).
- Findings are conversation material; allocation decisions stay with the advisor.
