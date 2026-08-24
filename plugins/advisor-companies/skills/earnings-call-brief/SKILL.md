---
name: earnings-call-brief
description: Use when analyzing a company's earnings — "what did X report", "summarize the NVDA call", "how was the quarter", "did they beat", management tone questions, or prepping talking points after a holding reports.
license: MIT
---

# Earnings Call Brief

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

Turn an earnings event into what an advisor actually needs: the quarter in one
line, results vs expectations, what management's tone and guidance imply, and
a client-ready talking point — without reading a 60-page transcript.

## Required Inputs

Ticker. Default: most recent reported quarter.

## Lexfi MCP Calls

Strict sequence (the two-step is mandatory — see playbook):

1. **Batch 1 (parallel):** `get_earnings_calls_by_ticker` (find the call, copy
   `transcript_id`), `get_earnings_surprises` (beat/miss history),
   `get_analyst_estimates` (`period: quarter` — the hurdle; rows come
   far-future-first, so raise `limit` to reach near-term quarters),
   plus the reaction: `get_stock_quote` if the call was within the past week,
   otherwise `get_historical_prices` (report date ± 5 days) — today's quote is
   NOT the reaction to an older print.
2. **Batch 2:** `get_earnings_call_insights` with `ticker` + `transcriptId`,
   `tables: ["ais", "metrics", "communication"]`. Add `includeTranscript: true`
   ONLY if the user asks for verbatim quotes (50–200 KB payload).
3. **Optional:** `get_stock_news` (symbol) if the price reaction diverges from
   the headline numbers — the market may be trading something else.

## Workflow

1. **Numbers vs hurdle**: actual vs consensus EPS/revenue; place this quarter in the beat/miss pattern from surprise history.
2. **Tone**: from insight metrics + communication table — confident/cautious, tone shift vs prior quarters if available. Tone is a signal, label it as one.
3. **Guidance**: raised/held/cut/none. Guidance change usually outweighs the quarter itself — order the brief accordingly.
4. **Reaction vs results**: if the stock fell on a beat (or rose on a miss), that divergence is the story; investigate via news before writing.
5. **Compose** per format below.

## Output Format

```
EARNINGS BRIEF — [TICKER] [quarter] — reported [date]

THE QUARTER IN ONE LINE
Beat/miss + guidance direction + market reaction, one sentence.

NUMBERS
Metric | Actual | Consensus | Surprise — EPS, revenue, +key segment if notable.
Beat/miss streak context (one line).

GUIDANCE & MANAGEMENT TONE
What changed in guidance (fact). Tone read with basis (signal).
[Interpretation clearly marked: what this suggests about trajectory.]

MARKET REACTION
Move + whether it matches the print; divergence explained or flagged as open.

WHAT IT MEANS FOR HOLDERS
2–3 lines for the advisor: thesis-relevant changes, risks to watch, and
whether anything warrants a client conversation.

--- CLIENT TALKING POINT (draft) ---
2–3 plain-language sentences an advisor can use verbatim with a client
who holds the name.

Sources & data as-of: [one line]
```

## Quality Controls

- Never analyze a call without insights actually retrieved — if the transcript
  isn't in Lexfi yet, say so; do not reconstruct the quarter from headlines
  without labeling the difference.
- Management claims attributed ("management expects"), never adopted.
- Surprise figures shown with both actual and estimate, not just "beat by 8%".
- Partial insight tables (per-table errors) → use what returned, list gaps.
