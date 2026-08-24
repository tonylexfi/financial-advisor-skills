---
name: client-meeting-prep
description: Use when an advisor is preparing for a client meeting, review, or call — "prep me for my meeting with...", "I'm seeing a client tomorrow", "get me ready for the quarterly review" — with or without a pasted portfolio.
license: MIT
---

# Client Meeting Prep

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

Turn a client context (holdings, concerns, meeting objective) into a one-page
brief the advisor can absorb in five minutes: what changed, what the client
will ask about, what to raise proactively.

## Required Inputs

- Some client context: holdings/tickers, a portfolio paste, a model name, or at minimum the topics the client cares about.

If the advisor gives nothing but a name, ask ONE compact question ("What does
the portfolio hold, and what's the meeting about?") — never interrogate.

## Optional Inputs

Meeting objective, client concerns/temperament, time since last meeting
(default: 90 days — this sets every lookback window), benchmark, restrictions.

## Workflow

### Step 1 — Frame

Extract: material holdings (>~3% weight or client-flagged), sectors/themes,
the meeting objective, and the lookback window. List them before any call.

### Step 2 — Plan calls (playbook discipline)

Default plan, pruned to what the meeting needs:

| Need | Calls | Parallel? |
|---|---|---|
| Position state | `get_stock_quote` (ALL tickers, one call) | ✔ batch 1 |
| Market context | `get_market_overview`, `get_sector_performance` | ✔ batch 1 |
| Holding developments | `get_stock_news` per material holding (cap ~6 holdings) | ✔ batch 1 |
| Risk backdrop | `get_daily_vix_index` (lookback window) | ✔ batch 1 |
| Macro context | `get_us_macro_regime`, `get_economic_calendar` (SHORT window — meeting week only; heavy payload trap) | ✔ batch 1 |
| Earnings since last meeting | `get_earnings_calls_by_ticker` → `get_earnings_call_insights` (`tables:["ais","metrics"]`) for holdings that reported | batch 2 (needs IDs) |
| Sentiment shift on a flagged name | `get_stocks_news_sentiment` (symbol) | only if a holding shows unusual price/news action |

Skip macro calls entirely for a single-topic meeting ("client wants to discuss
the NVDA position"); skip earnings calls when nothing reported in the window.

### Step 3 — Analyze

For each material holding: price move over window → driver (news/earnings/
sector beta) → does it touch the client's stated concerns? Separate facts,
signals, interpretation per evidence-discipline.

### Step 4 — Prioritize

Rank findings by: (1) client will likely ask about it, (2) changes the
portfolio conversation, (3) advisor looks unprepared without it. Cut the rest.

## Output Format

```
CLIENT MEETING BRIEF — [client/portfolio] — [date]
Meeting objective: ...   Window: since [date]

THE ONE THING
One sentence: the single development the advisor must know cold.

TOP 5 SINCE LAST MEETING
Ranked. Each: what happened (fact) → why it matters for THIS client (interpretation).

PORTFOLIO DEVELOPMENTS
Table: Holding | Move over window | Driver | Talking point

MARKET & MACRO BACKDROP
≤5 lines. Only what frames the client conversation.

LIKELY CLIENT QUESTIONS — WITH ANSWERS
3–5 Q&A pairs, in the client's voice, answers in advisor voice.

RAISE PROACTIVELY
2–3 items: risks/opportunities the client hasn't asked about. Framed as
"discuss/review", never as account instructions.

WATCH BEFORE THE MEETING
Anything landing between now and the meeting (earnings, CPI, FOMC).

Sources & data as-of: [one line]
```

## Quality Controls

- Every holding the advisor listed is either in the brief or explicitly marked "no material development".
- Every "Top 5" item traces to a retrieved fact.
- No account-level recommendations (see evidence-discipline advice boundary).
- Brief fits one page; overflow goes to an appendix only on request.

## Failure Handling

Ticker unresolvable → flag it in the brief, continue with the rest. No news
for a holding → "quiet period, no material news" is a valid, useful finding.
