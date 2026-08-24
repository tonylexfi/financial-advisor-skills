---
name: investment-committee-brief
description: Use when preparing materials for an investment committee, CIO meeting, or house-view session — "prep the IC brief", "committee meeting Thursday", "build the weekly CIO memo" — decision-oriented team documents, not client materials.
license: MIT
---

# Investment Committee Brief

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

A two-page, decision-oriented committee memo: market state, what changed since
last meeting, the decisions on the table with evidence for AND against, and a
standing challenge section that stress-tests the house view. Committees fail
by consensus drift — this brief institutionalizes the dissent.

## Required Inputs

At least one of: the committee's current house view / positioning, decisions
under consideration, or topics on the agenda. Without any, ask one question —
a committee brief without a decision context is just a market report.

## Optional Inputs

Time since last meeting (default 1 week), prior memo for continuity,
watchlist/model holdings.

## Lexfi MCP Calls

- **Batch 1 (parallel) — state of the world:** `get_market_overview`,
  `get_sector_performance`, `get_daily_vix_index` (window),
  `get_macro_yield_curve` (window), `get_us_macro_regime`,
  `get_rate_probabilities` (fed), `get_macro_news` (limit 15),
  `get_cb_calendar` + `get_economic_calendar` (tight 1–3 day windows around key dates only — heavy payload trap).
- **Batch 2 — per agenda decision:** the minimum set that arms both sides;
  e.g. a "trim tech?" agenda item → `get_key_metrics` on bellwethers,
  `get_stocks_news_sentiment`, sector performance detail. Compose via the
  playbook routing table.

## Workflow

1. **Delta since last meeting** — only what CHANGED. Committees don't need the level restated.
2. **Per decision on the table**: strongest evidence FOR (facts/signals), strongest evidence AGAINST, and what data would settle it. Both sides sourced — no straw men.
3. **Challenge the house view**: take the stated positioning and argue the best-evidence case against it (marked interpretation). This section is mandatory whenever a house view was provided.
4. **Decision framing**: each agenda item ends in a decidable question, not a topic.

## Output Format

```
INVESTMENT COMMITTEE BRIEF — [date] — since [last meeting]

DELTA
What changed: 4–6 bolded one-liners with figures.

STATE OF THE WORLD
Compact dashboard table: equities / rates / vol / regime / policy pricing.
One line each, current + direction.

DECISIONS ON THE TABLE
For each agenda item:
  Question: [decidable phrasing]
  For: evidence (sourced)
  Against: evidence (sourced)
  Would settle it: [data/event]

CHALLENGE TO THE HOUSE VIEW
The best evidence-backed case against current positioning. 1–2 paragraphs,
marked interpretation. Steelman, not devil's-advocate theater.

RISK REGISTER
Top 3 portfolio-relevant risks, each: trigger → transmission → early indicator.

BETWEEN NOW AND NEXT MEETING
Calendar of deciding events.

Sources & data as-of: [one line]
```

## Quality Controls

- Every FOR has an AGAINST; a one-sided decision section means evidence
  gathering isn't done — say so rather than faking balance.
- Challenge section present whenever a house view exists.
- Two pages max; committee time is the scarcest input this skill touches.
- The memo frames decisions; it never records them as made.
