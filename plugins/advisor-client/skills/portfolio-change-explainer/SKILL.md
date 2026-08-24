---
name: portfolio-change-explainer
description: Use when an advisor must explain a portfolio change to a client — a rebalance, a position added or trimmed, a model switch — "help me explain why we sold X", "draft the note about the rebalance", "client is asking why we bought this".
license: MIT
---

# Portfolio Change Explainer

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication (client-ready register)

## Purpose

Turn an already-made portfolio decision into a clear, honest client
explanation: what changed, why, and what it means for the client — grounded in
current data, without overselling the rationale or promising outcomes.

## Critical Boundary

This skill explains decisions the advisor ALREADY made. It never generates or
endorses the decision itself. If the advisor hasn't stated the rationale, ask
for it in one question — do not invent one, however plausible the trade looks.

## Required Inputs

- The change (what was bought/sold/trimmed, roughly when)
- The advisor's rationale, in any rough form

## Optional Inputs

Client sophistication, whether the change realized gains/losses (tax
sensitivity → add a "your advisor will discuss tax specifics" line, never tax
advice), delivery format (email vs talking points).

## Lexfi MCP Calls

Only what substantiates the advisor's stated rationale — typically 2–4 calls,
one batch:

- `get_stock_quote` + `get_stock_news` for the securities involved
- `get_key_metrics` if the rationale is valuation
- `get_sector_performance` or `get_us_macro_regime` if the rationale is rotation/macro
- `get_earnings_calls_by_ticker` → insights only if the rationale cites the last quarter

If retrieved data CONTRADICTS the stated rationale (e.g., "we sold on
deteriorating fundamentals" but metrics improved), tell the advisor privately
in the appendix before they send anything — do not silently paper over it.

## Workflow

1. Restate the change and rationale in one line; confirm understanding of anything ambiguous.
2. Retrieve supporting data (above).
3. Draft the client note: change → reason in plain language → what it means for the portfolio → what it does NOT mean.
4. Build advisor appendix: data backing, any tension between data and rationale, anticipated client pushback with suggested responses.

## Output Format

```
=== CLIENT NOTE (draft for your review) ===

What we changed
One or two sentences, concrete, no euphemism ("we sold", not "we optimized").

Why
The advisor's rationale in plain language, supported by 1–2 facts.
Attributed reasoning: "we believe", "in our view" — never "the market will".

What this means for you
Portfolio-level effect (diversification, risk, income) in one short paragraph.
What it does NOT mean (e.g., "this isn't a view that markets are about to fall").

[Draft notice + advisor signature placeholder]

=== ADVISOR APPENDIX (do not send) ===
- Data backing each claim (with as-of dates)
- ⚠ Tensions: where data cuts against the rationale, if anywhere
- Likely client pushback → suggested responses (2–3)
```

## Quality Controls

- The rationale in the note is the ADVISOR's, attributed as such.
- No outcome promises ("this positions us for gains" → banned).
- Tax/suitability specifics deferred to the advisor, in one line, only if relevant.
- ≤300 words for the client note.
