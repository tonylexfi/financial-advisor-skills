---
name: lexfi-mcp-playbook
description: Use when any financial-advisor skill needs current market, company, macro, sentiment, or central-bank data — before calling any Lexfi MCP tool, when unsure which tool answers a question, when a tool name looks ambiguous, or when a Lexfi call fails or returns unexpected units.
license: MIT
---

# Lexfi MCP Playbook

## Overview

Lexfi MCP is the financial data and intelligence layer for every skill in this
library. This playbook is the routing table: which tool answers which advisor
question, in what order, and which traps to avoid. Workflow skills reference
this playbook instead of re-documenting tools.

**Core principle: fewest calls that fully answer the question.** Every call has
latency and token cost. Plan the call set before making the first call, batch
independent calls in parallel, and never re-fetch what is already in context.

## Tool Availability

Lexfi tools may be **deferred** in a session (visible by name only). Load every
tool you plan to use in ONE ToolSearch batch before the first call — never one
at a time. Tool names carry an `mcp__<server>__` prefix; the bare names used
below and in `references/tool-map.md` are the suffix.

## Routing by Advisor Question

| Advisor question | Tool sequence |
|---|---|
| "Where is the market today?" | `get_market_overview` → `get_sector_performance` (parallel) |
| "Why did X move?" | `get_stock_quote` + `get_stock_news` (parallel); add `get_stocks_news_sentiment` if tone trend matters |
| "What did management say last quarter?" | `get_earnings_calls_by_ticker` → copy `transcript_id` → `get_earnings_call_insights` |
| "Is the market pricing Fed cuts?" | `get_rate_probabilities` (bank code, not name) |
| "Has the Fed's tone changed?" | `get_cb_insights` (bankId `fed`, `ecb`, …) |
| "How risky is the tape right now?" | `get_daily_vix_index` + `get_macro_yield_curve` + `get_cnn_fear_greed_index` + `get_macro_uncertainties` (parallel) |
| "What macro regime are we in?" | `get_us_macro_regime` → `get_macro_inflation` if inflation detail needed |
| "What's on the calendar?" | `get_economic_calendar` (date window) + `get_cb_calendar` (parallel) |
| "Is this stock expensive?" | `get_key_metrics`; add `get_analyst_estimates` for forward view |
| "Who's beating estimates?" | `get_earnings_surprises` per ticker |
| "What's inside this ETF?" | `get_etf_holdings` |
| "What's the social narrative?" | `get_stocks_x_highlights` / `get_stocks_reddit_highlights` / `get_stocks_stocktwits_highlights` |
| "Insider conviction?" | `get_insider_trades` (symbol filter) |
| "Country snapshot (EM)?" | `get_macro_weekly_series_catalog` → `get_macro_weekly_snapshot` |

Full per-tool notes: `references/tool-map.md`. Read it before composing a new
call plan for a workflow not listed above.

## Known Traps (cost real briefs before — check every one)

| Trap | Reality |
|---|---|
| `get_forecast` | **Weather**, not financial. Use `get_macro_forecasts` for macro projections. |
| `get_fear_greed_index` | **Crypto** (Alternative.me). Equity sentiment = `get_cnn_fear_greed_index`. |
| `get_etf_flows` | **Crypto spot ETFs only** (BTC/ETH/SOL). Not equity fund flows. |
| VIX `changePercent` | Units are inconsistent between schema docs (decimal) and live data (percent). Sanity-check against `change / prior close` before scaling — never blindly multiply. |
| `get_earnings_call_insights` | Requires `transcriptId` from `get_earnings_calls_by_ticker` first. Never guess IDs. |
| `includeTranscript=true` | 50–200 KB+ payload. Only when verbatim quotes are required; default to insight tables. |
| `get_cb_insights` bankId | Short codes only (`fed`, `ecb`, `boe`, `boj`) — full bank names fail. Numeric indices arrive as decimal strings; parse before comparing. |
| `get_rate_probabilities` | Latest snapshot per bank only, ~10 forward meetings. No history — don't claim "pricing has shifted" from one call. |
| `get_macro_weekly_snapshot` | Needs exact sheet names ("Brazil", "International"). Discover via `get_macro_weekly_series_catalog` first. |
| `get_economic_calendar` | Global and unfiltered — a 7-day window can return 140 KB+ (5,000+ lines). Use 1–2 day windows; scan for major-economy, market-moving events only. |
| `get_cb_insights` rows | One date can yield multiple conference rows — full press conferences plus "quote shorts" clips with their own indices. Read the `summary` block and full conferences; ignore clip rows. |

## Call Discipline

1. **Plan before calling.** List needed facts → map to fewest tools → mark which are parallel-safe.
2. **Batch parallel calls.** Quotes, news, VIX, calendar have no interdependencies — one round trip.
3. **Sequence only true dependencies.** transcript listing → insights; catalog → snapshot.
4. **Subset when the tool allows it.** `get_earnings_call_insights` `tables:["ais","metrics"]` beats fetching all six tables; date-window every history tool.
5. **Do not call Lexfi at all when** the user asks for formatting/rewording, all data is already in the conversation, or the question is conceptual ("what is duration?").

## Failure Handling

- Tool error or empty result → say so in the output ("No Lexfi data returned for X"), never fill the gap from general knowledge without labeling it `[model knowledge — not Lexfi data]`.
- Ticker resolution failure → try `TICKER:CC` country suffix or `country` param before giving up.
- Partial data (some tables error) → use what returned; list what's missing in the brief's Sources section.
- Stale timestamps → report the `as_of` date next to the figure. Never present old data as current.

## Red Flags — Stop and Re-plan

- About to call the same tool twice with the same arguments
- About to call more than ~8 tools for a single brief without a written plan
- About to present a number without knowing which call produced it
- About to use `get_forecast`, `get_fear_greed_index`, or `get_etf_flows` for equities
