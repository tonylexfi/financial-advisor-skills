# Example — client-meeting-prep

Illustrative session (figures invented for demonstration).

## Advisor input

> Prep me for Thursday's quarterly review with Client H. Portfolio: 32% SPY,
> 18% AGG, 14% NVDA, 9% MSFT, 7% JPM, 6% XOM, 14% cash. Last met mid-May.
> They've been anxious about "the AI bubble."

## What the skill did (visible in the session)

1. Framed: 6 material holdings, 90-day window (May 24 → Aug 24), client
   concern = AI concentration.
2. Batch 1 (parallel): quotes (all 6, one call), market overview, sector
   performance, per-holding news, VIX (90d), US macro regime, economic
   calendar (2 weeks).
3. Batch 2: NVDA + MSFT reported in window → transcript listings → earnings
   insights (`tables: ["ais","metrics"]`).
4. Skipped: sentiment history (no anomalies), social highlights (not asked).

## Output

```
CLIENT MEETING BRIEF — Client H — Thu Aug 27
Meeting objective: quarterly review   Window: since May 15

THE ONE THING
NVDA's beat-and-raise quarter (Aug 20) pushed the position from ~11% to 14%
of the portfolio — the concentration the client is anxious about grew by
drift, not by any decision, and that's the conversation.

TOP 5 SINCE LAST MEETING
1. NVDA +31% over the window on data-center demand; guidance raised (fact).
   For this client: the "bubble" worry now has a bigger denominator (interpretation).
2. MSFT quarter in line, tone confident; stock +6% — steady, low talking-point risk.
3. Rate-cut odds for September moved to ~80% market-implied — supports the
   AGG sleeve conversation.
4. VIX drifted 15→13: markets calm; a good window for rebalancing talk
   (interpretation, not advice).
5. XOM flat despite crude softness — dividend narrative intact, no action items.

PORTFOLIO DEVELOPMENTS
Holding | Move (window) | Driver            | Talking point
NVDA    | +31%          | Earnings, AI capex| Drift → concentration discussion
MSFT    | +6%           | In-line quarter   | Quiet strength
JPM     | +4%           | Sector beta       | Nothing material
SPY     | +7%           | Broad rally       | Portfolio's engine this quarter
AGG     | +1.5%         | Cut pricing       | Rate path context
XOM     | -1%           | Crude softness    | Income holding doing its job

MARKET & MACRO BACKDROP
Balanced-growth regime probability rising; inflation drifting toward target;
markets pricing ~80% odds of a September cut (attributed to pricing, not a
forecast). Calm vol backdrop.

LIKELY CLIENT QUESTIONS — WITH ANSWERS
Q: "Is the AI thing a bubble? Should we get out of NVDA?"
A: Separate the business from the stock: revenue and guidance are being
   delivered, not just promised (fact). The position's growth is price drift.
   The decision point isn't bubble-or-not — it's what % of the portfolio you
   want one company to be. [Advisor's call on target weight.]
Q: "Why are we holding 14% cash when markets keep going up?"
A: [Needs your rationale — flagging so you're not surprised by it.]

RAISE PROACTIVELY
- Concentration review: NVDA at 14% — discuss a target weight policy.
- If cuts materialize, cash yield falls — worth revisiting the cash sleeve's purpose.

WATCH BEFORE THE MEETING
- PCE print Friday; NVDA typically moves with rates repricing.

Sources & data as-of: Lexfi MCP (quotes/news/earnings insights/regime/rate
pricing), Aug 24 close.
```

Note the discipline: drift math shown, market-implied odds attributed, the
cash question flagged as needing the *advisor's* rationale rather than
invented, and no buy/sell instruction anywhere.
