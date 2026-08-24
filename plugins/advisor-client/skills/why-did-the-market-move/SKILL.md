---
name: why-did-the-market-move
description: Use when a client or advisor asks why the market or a specific stock moved — "why is the market down today", "client is asking about the selloff", "what happened to NVDA this morning" — same-day or recent move attribution.
license: MIT
---

# Why Did the Market Move?

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

Fast, honest attribution of a market or single-name move: what actually
happened, the drivers ranked by evidence strength, and a calm client-ready
paragraph. Optimized for speed — an advisor uses this while the phone rings.

## Required Inputs

The move in question (index or ticker; default: today's broad market if
unspecified).

## Lexfi MCP Calls

**Broad market move** — one parallel batch:
`get_market_overview`, `get_sector_performance`, `get_macro_news` (limit 15),
`get_daily_vix_index` (2 weeks), `get_economic_calendar` (today ± 1 day).

**Single-name move** — one parallel batch:
`get_stock_quote`, `get_stock_news` (symbol), `get_market_overview` (to
separate name-specific from market beta), `get_stocks_news_sentiment` (symbol,
14 days) if no obvious headline.

## Workflow

1. **Size the move first.** Is it actually unusual? A 0.8% index day or a 2%
   move in a high-beta name may need de-dramatizing, not explaining. Check
   against recent range (VIX level, sentiment trend).
2. **Rank candidate drivers by evidence:**
   - CONFIRMED: timestamped event (release, headline, earnings) matching the move's timing and direction
   - LIKELY: sector-wide pattern or calendar event without direct confirmation
   - SPECULATIVE: narrative/flow explanations — label them as such
3. **Decompose single names**: market move × beta vs name-specific residual, qualitatively ("half of this is just the tape").
4. **Write both registers** (below).

Honesty rule: "no clear catalyst — this looks like flows/positioning" is a
legitimate and common answer. Never manufacture a cause.

## Output Format

```
MARKET MOVE BRIEF — [what] — [timestamp]

WHAT HAPPENED
One line with the numbers.

DRIVERS (ranked)
1. [CONFIRMED] ...
2. [LIKELY] ...
3. [SPECULATIVE] ...

IS THIS UNUSUAL?
Move vs recent range / vol backdrop, one or two lines.

WHAT WE'RE WATCHING
1–3 items that decide whether this extends or fades.

--- CLIENT-READY PARAGRAPH (draft) ---
3–5 plain sentences: what happened, most-supported reason, perspective.
Calm, no predictions.

Sources & data as-of: [one line]
```

## Quality Controls

- Driver ranks reflect evidence, not narrative appeal.
- Timing checked: a "cause" published after the move is not a cause.
- Client paragraph contains zero jargon and zero forecasts.
- Total advisor section scannable in under a minute.
