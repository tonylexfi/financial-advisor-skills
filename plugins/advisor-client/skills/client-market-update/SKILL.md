---
name: client-market-update
description: Use when an advisor needs a client-ready market update letter or note — "write my monthly client update", "draft a market note for clients", "something I can send clients about this month" — periodic communication, not a reaction to one event.
license: MIT
---

# Client Market Update

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication (client-ready register)

## Purpose

Produce a 250–400 word client-ready market letter — plain language, calm,
factual — plus a short advisor-only appendix with the data behind every claim
so the advisor can defend each sentence.

## Required Inputs

Period covered (default: the current month). Everything else optional:
audience notes (retirees vs accumulation clients), house view to reflect,
topics to include/avoid.

## Lexfi MCP Calls

One parallel batch:

- `get_market_overview` + `get_sector_performance` — the tape
- `get_daily_sp500_index` + `get_daily_vix_index` (period window) — the arc of the period, not just today
- `get_macro_news` (limit ~15) — the period's dominant storylines
- `get_us_macro_regime` — backdrop framing
- `get_economic_calendar` — the "looking ahead" paragraph; ask only for the few days around known majors (CPI, jobs, FOMC via `get_cb_calendar`), never a 4-week dump (heavy payload trap)

Add `get_rate_probabilities` only when rates/Fed were the period's story.
Do NOT pull single-stock data — this is a market letter, not a portfolio letter.

## Workflow

1. **Find the period's story.** From index arc + macro news: what would a professional say this month was *about*? One theme, maximum two.
2. **Select 3–4 client-relevant facts** that carry the story. Translate every figure to plain language ("U.S. stocks rose about 3%" — round, no decimals theater).
3. **Draft the letter** (structure below). Write for a smart non-professional.
4. **Build the advisor appendix**: each sentence of the letter → the data point behind it.

## Output Format

```
=== CLIENT LETTER (draft for your review) ===

[Period] Market Update

Para 1 — What happened: the period in 2–3 plain sentences.
Para 2 — Why: the driver, explained without jargon.
Para 3 — Perspective: context that keeps clients calm and invested —
         history, diversification, or the distinction between headlines
         and portfolios. Factual, not pep-talk.
Para 4 — Looking ahead: what we're watching (never what we predict).

[Advisor signature placeholder]

=== ADVISOR APPENDIX (do not send) ===
Claim-by-claim data backing (table), figures with as-of dates,
anything deliberately simplified and what the precise version is.
```

## Quality Controls

- Zero jargon in the letter (bps, curve, risk-on, valuation multiples all banned).
- No predictions, no performance promises, no "opportunity" selling.
- Every letter claim appears in the appendix with a source.
- Round numbers in the letter; precise numbers in the appendix.
- Ends with the one-line draft notice per advisor-communication.

## Failure Handling

If a data pull fails, write the letter without that claim — never approximate
market returns from memory in a client-facing document.
