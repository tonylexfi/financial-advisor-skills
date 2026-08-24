# Test Log — Initial Library Verification

Date: 2026-08-24 · Environment: Claude (Fable 5) + live Lexfi MCP · Tester: repo author

## Layer 1 — Structural validation

`scripts/validate.py`: **PASS** — 16 skills; frontmatter contract, name/dir
match, trigger-style descriptions, core cross-references, marketplace sources.

## Layer 2 — Live verification of call plans (real Lexfi MCP)

| Call-plan element | Result |
|---|---|
| `get_market_overview`, `get_sector_performance`, `get_market_movers` | ✅ live index/sector data |
| `get_daily_vix_index` windowed | ✅ — **defect found, fixed** (see below) |
| Two-step earnings: `get_earnings_calls_by_ticker` → `get_earnings_call_insights` (NVDA, `tables:["ais","metrics"]`) | ✅ transcript_id resolution, AI summary + sentiment metrics returned; subsetting works |
| `get_rate_probabilities` (fed) | ✅ 10 forward meetings, as-of dates present; snapshot-only trap confirmed correct |
| `get_us_macro_regime` windowed | ✅ regime transitions with probabilities |
| `get_cb_insights` (fed, 90d trend) | ✅ hawk/dove indices + trend — **doc gap found, fixed** |
| `get_stock_quote` multi-symbol batch | ✅ one call, three tickers |
| `get_economic_calendar` 7-day window | ⚠️ works but **140 KB / 5,879 lines** — **trap added, 3 skills patched** |
| `get_earnings_surprises`, `get_analyst_estimates` (NVDA) | ✅ — **ordering gap found, fixed** |
| `get_historical_prices` windowed | ✅ |

### Defects found and fixed during testing

1. **VIX `changePercent` units** — schema says decimal; live data returns
   percent (−0.18 on 15.9 close → field −1.13208). Trap rewritten from
   "multiply by 100" to "sanity-check against change/close before scaling".
2. **`get_economic_calendar` payload bomb** — global, unfiltered; 7 days ≈
   140 KB. Trap added; `client-meeting-prep`, `client-market-update`,
   `investment-committee-brief` re-specified to tight 1–3 day windows.
3. **`get_cb_insights` duplicate rows** — "quote shorts" clips appear as
   extra conference rows per date with their own indices. Guidance added:
   use `summary` + full conferences, ignore clip rows.
4. **`get_analyst_estimates` ordering** — rows come far-future-first;
   near-term hurdle needs a higher `limit`. Noted in tool-map +
   `earnings-call-brief`.
5. **Reaction ≠ today's quote** — `earnings-call-brief` originally used
   `get_stock_quote` for the market reaction; wrong for any non-recent call.
   Re-specified: quote only if reported within the past week, else
   `get_historical_prices` (report date ± 5 days).

## Layer 3 — End-to-end skill execution

`earnings-call-brief` executed on NVDA Q1 FY27 following the patched call
plan verbatim (two batches, 6 calls). Abridged output as produced:

```
EARNINGS BRIEF — NVDA Q1 FY27 — reported May 20, 2026

THE QUARTER IN ONE LINE
Clear beat (EPS $1.87 vs $1.76, revenue $81.6B vs $78.4B est.) with Q2
guidance of $91B ±2% — yet the stock closed -1.8% the next day.

NUMBERS
Metric  | Actual | Consensus | Surprise
EPS     | $1.87  | $1.76     | +6.3%
Revenue | $81.6B | $78.4B    | +4.1%
20 consecutive quarterly EPS beats since Feb 2023 (fact, Lexfi surprises).

GUIDANCE & MANAGEMENT TONE
Q2 FY27 guided to $91B ±2%; new $80B buyback; dividend raised to $0.25
(facts, call summary). Management-section sentiment 0.51 vs Q&A 0.24, low
uncertainty scores (signals, Lexfi call metrics). [Interpretation: prepared
remarks notably more confident than Q&A — pattern consistent with
management steering around China questions.]

MARKET REACTION
-1.8% day-after close (223.47 → 219.51) despite beat-and-raise; -6% over
the following 4 sessions. Divergence flagged: market focus on excluded
China revenue and flat mid-70s margin guidance (risk factors named in the
call) is the leading explanation [interpretation].

WHAT IT MEANS FOR HOLDERS
Execution intact; the open items are China licensing (zero revenue in
outlook) and margin plateau. Worth a client conversation only for
concentrated positions.

--- CLIENT TALKING POINT (draft) ---
NVIDIA's results again came in ahead of expectations, and the company
raised its outlook for next quarter. The share price slipped anyway —
investors are focused on how much future growth is already priced in and
on uncertainty about sales to China. Nothing in the report changes the
company's underlying trajectory.

Sources & data as-of: Lexfi MCP (surprises, call insights, prices), Aug 24.
```

Verified against the skill's quality controls: evidence ladder labels
present; divergence investigated rather than ignored; management claims
attributed; no advice; client paragraph jargon-free. **PASS.**

## Not yet covered

Adversarial trigger-collision tests across all 13 skills and baseline (RED)
comparisons per docs/skill-development.md remain open for the launch tag;
contributions must include them per CONTRIBUTING.md.
