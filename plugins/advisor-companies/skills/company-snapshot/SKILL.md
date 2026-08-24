---
name: company-snapshot
description: Use when an advisor needs to get current on a company fast — "brief me on X", "client asked about this stock", "what's going on with Tesla", a name entering a portfolio or conversation — general company intelligence, not earnings-specific.
license: MIT
---

# Company Snapshot

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

A one-page current picture of a company: what it does, how it's priced, what's
happened lately, what the narrative is, and the risks — enough for an advisor
to hold an informed client conversation in ten minutes.

## Required Inputs

Ticker or resolvable company name.

## Lexfi MCP Calls

One parallel batch (add-ons only on divergence):

- `get_company_profile` — identity
- `get_stock_quote` — current state
- `get_historical_prices` (12 months) — the arc
- `get_key_metrics` (4 annual + latest) — valuation vs own history
- `get_stock_news` (symbol, limit 15) — recent developments
- `get_stocks_news_sentiment` (symbol, 30 days) — tone trend
- `get_earnings_surprises` — execution consistency

Add-ons: `get_insider_trades` if price and news diverge;
`get_analyst_estimates` if the question is forward-looking;
`get_stocks_x_highlights` only if the user asks about narrative/chatter.

## Workflow

1. Identity in two lines — assume the advisor knows roughly what the company is; skip boilerplate description unless obscure.
2. Price arc: 12-month shape, drawdown from high, vs sector (from context).
3. Valuation: current multiples vs the company's own 4-year range — "expensive vs itself" is more defensible than vs peers you didn't retrieve.
4. Developments: cluster the 15 headlines into 2–4 storylines; date each.
5. Sentiment: direction over 30 days, as signal.
6. Risks: only evidence-backed ones (from news, metrics, execution history) — no generic "competition, regulation, macro" filler.

## Output Format

```
COMPANY SNAPSHOT — [TICKER] — [date]

WHO / WHERE
2 lines: what it does; price, 12-mo arc, distance from high.

VALUATION
Multiple | Now | 4-yr range | Read — 3–4 rows, one-line verdict vs own history.

WHAT'S HAPPENING
2–4 dated storylines, one line each, facts first.

NARRATIVE & TONE
News-sentiment trend (signal) + notable divergences from price.

EXECUTION
Beat/miss pattern one-liner.

RISKS WORTH NAMING
2–4, each tied to retrieved evidence.

IF A CLIENT ASKS
2-line plain-language answer to "should I be worried about / excited about X?"
— framed as perspective, not advice.

Sources & data as-of: [one line]
```

## Quality Controls

- Every risk maps to evidence; generic risk filler banned.
- Valuation verdicts always relative to retrieved history, not vibes.
- Sentiment ≠ fundamentals (evidence-discipline).
- One page. Depth on request only.
