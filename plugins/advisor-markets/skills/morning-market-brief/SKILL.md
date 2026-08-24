---
name: morning-market-brief
description: Use when an advisor wants the daily pre-open or start-of-day market rundown — "morning brief", "what do I need to know today", "catch me up before the open" — optionally scoped to a watchlist.
license: MIT
---

# Morning Market Brief

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

A two-minute scannable brief that arms an advisor for the day: tape, the one
story that matters, today's calendar, and anything on their watchlist that
needs attention before clients start calling.

## Inputs

All optional: watchlist tickers (persisted from context if previously given),
client-topic focus areas.

## Lexfi MCP Calls

One parallel batch, every day, no more:

- `get_market_overview` — indices
- `get_sector_performance` — leadership
- `get_market_movers` (`actives`) — tape character
- `get_macro_news` (limit 12) — overnight storylines
- `get_economic_calendar` (today + tomorrow) — catalysts
- `get_daily_vix_index` (10 days) — risk backdrop trend
- `get_stock_quote` + `get_stock_news` for watchlist (single batched calls) — only if a watchlist exists

Add `get_cb_calendar` on weeks with policy meetings. Nothing else without an
explicit ask — this brief's value is discipline, not breadth.

## Workflow

1. Pull the batch.
2. Pick THE story: the one development most likely to shape today. One, not three.
3. Triage watchlist: flag only names with news or moves >1.5× their recent daily range; everything else is one "quiet" line.
4. Compress per output format. Kill anything an advisor wouldn't act on or get asked about.

## Output Format

```
MORNING BRIEF — [date]

THE STORY
One bolded sentence + two supporting lines.

TAPE
Indices / sectors / vol in a 3-line table. Trend arrows vs yesterday.

TODAY'S CALENDAR
Time-ordered, only market-moving items, with why each matters (≤1 line each).

WATCHLIST FLAGS
Name | Move | Why | Client relevance — flagged names only.
"Rest of watchlist: quiet." if applicable.

CLIENT QUESTION OF THE DAY
The question clients are most likely to ask today, with a 2-line answer.

Sources & data as-of: [one line]
```

## Quality Controls

- Whole brief reads in ≤2 minutes.
- THE story is singular. If tempted to list three, the top one wins.
- Calendar filtered to items that move markets, not everything.
- No stale overnight numbers presented as live — timestamps on quotes.
