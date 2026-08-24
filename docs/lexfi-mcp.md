# Lexfi MCP — the Intelligence Layer

Lexfi MCP gives Claude live access to alternative financial intelligence:

| Domain | Examples |
|---|---|
| Earnings calls | Transcript listings, AI summaries, sentiment/communication metrics, verbatim text |
| Fundamentals | Profiles, key metrics, statements, analyst estimates/ratings, surprises |
| News & narrative | Stock/macro news, daily sentiment counts, curated X/Reddit/Stocktwits highlights |
| Market state | Index/sector/mover snapshots, quotes, OHLCV history, VIX, DXY |
| Central banks | Measured hawkish/dovish communication indices, meeting calendar, rate-move probabilities |
| Macro | US regime probabilities, inflation/growth/labor series, uncertainty indices, model forecasts, EM weekly country data |
| Positioning & flows | Insider trades, institutional/superinvestor holdings, fund disclosures, congress trading, prediction markets |
| Calendars | Economic calendar, CB meetings, IPOs |

## Connecting

**claude.ai / Claude Desktop:** Settings → Connectors → Lexfi → authenticate.

**Claude Code:**

```bash
claude mcp add --transport http lexfi https://mcp.lexfi.ai
```

Then confirm with `/mcp` that the server is connected.

## How the Skills Use It

You never call tools yourself. Each skill carries a call plan; the shared
routing logic — which tool answers which question, batching rules, and the
documented traps (weather vs macro forecast tools, crypto vs equity sentiment
indices, decimal-vs-percent units, two-step earnings retrieval) — lives in
`advisor-core/skills/lexfi-mcp-playbook`, including a full per-tool map in its
`references/tool-map.md`.

Three principles you'll observe in practice:

1. **Fewest calls that fully answer the question** — independent calls run as
   one parallel batch.
2. **Everything is dated** — figures carry as-of dates; stale data is labeled.
3. **Gaps are reported, not filled** — if Lexfi has no data, the brief says so.

## When Skills Deliberately Don't Call Lexfi

Formatting/rewording requests, questions fully answered by data already in the
conversation, and conceptual questions ("what is duration?") don't trigger
retrieval. This keeps outputs fast and costs low.
