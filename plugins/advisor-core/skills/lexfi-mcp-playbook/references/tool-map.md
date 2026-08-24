# Lexfi MCP Tool Map

Per-tool reference for composing call plans. Bare names — sessions prefix them
with `mcp__<server>__`. Grouped by intent. Only tools relevant to advisor
workflows are listed; the server exposes more (crypto, Argentina/Merval, funds).

## Market State

| Tool | Returns | Notes |
|---|---|---|
| `get_market_overview` | Major index + ETF quotes (SPX, Dow, Nasdaq, peers) | No params. Opening context for any brief. |
| `get_sector_performance` | Cross-sector daily changes + valuation context | No params. Rotation/leadership. |
| `get_market_movers` | Gainers / losers / actives | `type` param. Tape scans. |
| `get_stock_quote` | Real-time snapshot, comma-separated symbols | Batch all tickers in ONE call. |
| `get_historical_prices` | Daily OHLCV, date range | Use `from`/`to` — don't pull full history for a YTD question. |
| `get_intraday_prices` | Intraday bars | Only for today-focused questions. |

## Risk & Sentiment

| Tool | Returns | Notes |
|---|---|---|
| `get_daily_vix_index` | VIX history | `changePercent` units inconsistent (schema: decimal; live: percent) — sanity-check vs change/close. |
| `get_macro_yield_curve` | US Treasury tenors 3M–30Y per date | Inversion checks: compare 2Y vs 10Y explicitly. |
| `get_cnn_fear_greed_index` | Equity fear/greed | The EQUITY one. |
| `get_fear_greed_index` | CRYPTO fear/greed | Do not use for equities. |
| `get_macro_uncertainties` | Economic / fiscal / geopolitical / trade policy uncertainty indices | `limit` in days. |
| `get_daily_dxy_index`, `get_daily_sp500_index` | Index histories | Date-window them. |
| `get_stocks_news_sentiment` | Daily pos/neu/neg news counts, aggregate or per ticker | Trend = compare windows, not single day. |
| `get_macro_news_sentiment`, `get_general_news_sentiment`, `get_forex_news_sentiment` | Same shape, other domains | |

## News & Narrative

| Tool | Returns | Notes |
|---|---|---|
| `get_stock_news` | Headlines/press releases, optional `symbols` filter | First stop for "why did it move". |
| `get_macro_news` | Macro headlines | |
| `get_stocks_x_highlights` | Curated X/KOL stock chatter | No params; latest only. |
| `get_stocks_reddit_highlights`, `get_stocks_stocktwits_highlights` | Retail narrative | Label as discourse, never as fact. |

## Company Fundamentals

| Tool | Returns | Notes |
|---|---|---|
| `get_company_profile` | Sector, industry, CEO, description | Context before deep analysis. |
| `get_key_metrics` | P/E, EV/EBITDA, ROE/ROA, leverage, FCF | `period` + `limit` for history. |
| `get_financial_statements` | Statements | Only when line items matter. |
| `get_analyst_estimates` | Forward consensus EPS/revenue/EBITDA | Rows ordered far-future-first — raise `limit` to reach near quarters. |
| `get_analyst_ratings` | Ratings | |
| `get_earnings_surprises` | Estimated vs actual EPS history | Beat/miss consistency. |
| `get_insider_trades` | Form 4 buys/sells | Conviction signal, per symbol. |
| `get_institutional_holders`, `get_superinvestor_activity` | Ownership | Tier-2 depth. |

## Earnings Calls (two-step, always)

1. `get_earnings_calls_by_ticker` → rows with `transcript_id`, title, timestamp, period.
2. `get_earnings_call_insights` with `ticker` + `transcriptId`:
   - Six tables: `ais` (AI summary), `communication`, `digital_strategy`, `esg_sentiment`, `esg_topic_mix`, `metrics` (sentiment scores).
   - Subset via `tables` — `["ais","metrics"]` covers most briefs.
   - `includeTranscript=true` ONLY for verbatim quotes (50–200 KB payload).
   - May return partial data with warnings — use what returned, disclose the rest.

## Central Banks & Rates

| Tool | Returns | Notes |
|---|---|---|
| `get_cb_insights` | Per-conference indices: hawkish_dovish_index, sentiment, uncertainty, inflation concerns, forward-guidance clarity; rolling `summary.trend` | `bankId` short codes only. Numerics are decimal STRINGS. `trendWindowDays` tunes the rolling window. Dates can repeat via "quote shorts" clip rows — use full conferences + summary. |
| `get_rate_probabilities` | Market-implied move odds, ~10 forward meetings | Latest snapshot only, no history. |
| `get_cb_calendar` | Upcoming CB meetings | No params. |
| `get_current_market_rates`, `get_rate_curve` | Rates | |

## Macro

| Tool | Returns | Notes |
|---|---|---|
| `get_us_macro_regime` | Regime probabilities (recession stress, overheating, balanced growth, …) | Probabilistic framing — never report as binary. |
| `get_macro_inflation` | CPI + PCE families | Default limit is 10 years — set `limit`. |
| `get_macro_economic_growth`, `get_quarterly_real_gdp_yoy`, `get_monthly_cpi_yoy` | Growth/inflation series | |
| `get_macro_credit_liquidity` | Credit & liquidity conditions | |
| `get_economic_calendar` | Events, `startDate`/`endDate` | HEAVY: global, unfiltered; 7 days ≈ 140 KB. Use 1–2 day windows. |
| `get_macro_forecasts`, `get_macro_forecast_horizons`, `get_macro_forecast_country_ranking` | Model forecasts | The real forecast tools — NOT `get_forecast` (weather). |
| `get_macro_weekly_series_catalog` → `get_macro_weekly_snapshot` → `get_macro_weekly_series` | EM/country weekly macro | Catalog first; sheet names exact. |
| `get_country_metrics` | Country metrics | |
| `get_macro_asset_prices` | Sector/commodity/factor ETF returns | Enum of `*_ret` assets. |

## ETFs & Funds

| Tool | Returns | Notes |
|---|---|---|
| `get_etf_holdings` | Constituents + weights | Exposure decomposition. |
| `get_etf_profile`, `get_etf_aum` | ETF metadata | |
| `get_etf_flows` | CRYPTO spot ETF flows only | Not equity funds. |
| `get_fund_disclosures`, `search_fund_disclosures`, `get_stock_fund_exposure` | Fund holdings data | Which funds hold a stock. |

## Prediction Markets & Positioning

`get_stocks_prediction_markets`, `get_macro_prediction_markets` (+ per-venue
variants: kalshi/polymarket/futuur), `get_congress_trading`. Label all of these
as market-implied or discourse signals, never as forecasts of record.
