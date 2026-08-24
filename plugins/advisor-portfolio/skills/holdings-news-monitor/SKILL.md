---
name: holdings-news-monitor
description: Use when scanning a portfolio, model, or watchlist for developments — "anything happening in my holdings", "scan the book", "check my positions for news", periodic portfolio surveillance across many tickers at once.
license: MIT
---

# Holdings News Monitor

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

Triage, not digest: scan every holding, surface ONLY material developments,
and say explicitly that the rest is quiet. The advisor's scarce resource is
attention; this skill spends it for them.

## Required Inputs

Ticker list (pasted portfolio, watchlist, or model). Weights welcome — they
drive materiality.

## Optional Inputs

Lookback (default 7 days), materiality sensitivity (default: normal).

## Lexfi MCP Calls

One parallel batch regardless of list size:

- `get_stock_quote` — ALL tickers, one comma-separated call
- `get_stock_news` — symbols filter with the full list (one call), raise `limit` with list size
- `get_earnings_calls_by_ticker` — only for names with earnings-looking headlines, to confirm reports in window
- `get_market_overview` — baseline to separate market beta from name-specific moves

Escalate (batch 2) only for names flagged material: `get_stocks_news_sentiment`
(symbol) or earnings insights per earnings-call-brief's sequence.

## Materiality Test

A development is material if ANY of:
- Price move > ~1.5× the name's recent daily range, net of market move
- Earnings report, guidance change, M&A, management change, regulatory action
- News that touches a thesis or client concern stated in context
- Weight ≥5% AND any non-routine news

Routine noise (price-target tweaks, listicle mentions, sympathy moves already
explained by the market line) is NOT material. When in doubt on a big
position, flag it; on a small one, drop it.

## Output Format

```
HOLDINGS MONITOR — [n] names — window: [dates]

NEEDS ATTENTION ([k])
Holding | Weight | Development | Why it's material | Suggested next step
(next step = advisor process: "read the call brief", "review with client" —
never trade instructions)

WORTH KNOWING ([m])
One line each — real but non-urgent.

QUIET ([n-k-m] names)
Single line listing them: "No material developments."

PORTFOLIO-LEVEL NOTE
Only if a theme cuts across names (one macro/sector driver hitting several
holdings) — otherwise omit the section.

Sources & data as-of: [one line]
```

## Quality Controls

- Every input ticker appears in exactly one bucket — none silently dropped;
  unresolvable tickers listed as such.
- NEEDS ATTENTION is short. >5 items → re-check materiality before shipping.
- Sympathy moves attributed to the market, not manufactured into stories.
- No advice; next steps are process steps.
