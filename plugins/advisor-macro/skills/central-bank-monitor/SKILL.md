---
name: central-bank-monitor
description: Use when central bank policy comes up — "what's the Fed going to do", "has the ECB turned dovish", "what's priced for the next meeting", FOMC/ECB/BoE/BoJ meeting prep, or when policy communication shifts move markets.
license: MIT
---

# Central Bank Monitor

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

The policy picture for one central bank in one page: what markets price, what
the bank has actually been saying (measured, not vibes), where pricing and
communication diverge, and the dates that matter.

## Required Inputs

Which central bank (default: Fed). Playbook trap: `bankId` short codes —
`fed`, `ecb`, `boe`, `boj`, etc.

## Lexfi MCP Calls

One parallel batch:

- `get_rate_probabilities` (bank) — implied odds for ~10 forward meetings.
  Snapshot only: never claim pricing "moved" from this call alone.
- `get_cb_insights` (bankId, `trendWindowDays: 90`) — hawkish/dovish index,
  sentiment, uncertainty, forward-guidance clarity + rolling trend. Numeric
  fields arrive as decimal strings — parse before comparing.
- `get_cb_calendar` — upcoming meetings.
- `get_macro_inflation` (limit ~24 months) + `get_quarterly_real_gdp_yoy` —
  the mandate data the bank is reacting to.

Add `get_cb_conference_transcript`/`includeTranscript` only for verbatim quotes.

## Workflow

1. **Pricing**: next meeting's odds + the path implied over the following 3–4 meetings, in plain numbers.
2. **Communication**: latest hawkish/dovish classification + 90-day trend; note guidance-clarity direction (a bank getting vaguer is a finding).
3. **The gap**: where market pricing and measured communication diverge — this tension is the brief's centerpiece when it exists.
4. **Mandate check**: is inflation/growth data moving toward or away from what the bank says it needs?
5. **Dates**: meetings + the key data releases before the next one.

## Output Format

```
CENTRAL BANK MONITOR — [BANK] — [date]

WHERE THINGS STAND
2 lines: current stance + what's priced for the next meeting.

MARKET PRICING
Meeting | Implied action | Probability — next ~4 meetings.
(Attributed: "markets price", never "the Fed will".)

WHAT THE BANK IS SAYING
Hawk/dove index now vs 90-day trend (signal, with numbers).
Latest meeting's classification + 1–2 notable communication shifts.

PRICING vs COMMUNICATION
Aligned, or the gap — and [interpretation] of who blinks, clearly marked.

MANDATE DATA
Inflation + growth trajectory vs target, 3 lines.

DATES THAT MATTER
Next meeting; key releases before it.

CLIENT ANGLE
2 plain-language lines on what the policy picture means for a typical
portfolio conversation (rates → bonds/cash yields), no predictions.

Sources & data as-of: [one line]
```

## Quality Controls

- Implied probabilities always attributed to market pricing.
- Tone indices are signals from a model — cite the index, don't editorialize it into fact.
- No "the Fed will cut in December" — only pricing and communication evidence.
