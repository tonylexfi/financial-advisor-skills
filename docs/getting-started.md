# Getting Started

Five minutes from zero to your first brief.

## 1. Connect Lexfi MCP

The skills read market intelligence through the Lexfi MCP server. Connect it
once in your Claude environment:

- **claude.ai / Claude Desktop:** Settings → Connectors → add the Lexfi
  connector and sign in with your Lexfi account.
- **Claude Code:** `claude mcp add lexfi <lexfi-mcp-endpoint>` (see
  [lexfi-mcp.md](lexfi-mcp.md) for details).

Verify: ask Claude *"Using Lexfi, what's the current market overview?"* — you
should see a live index snapshot, not a knowledge-cutoff answer.

## 2. Install the Skills

```bash
claude plugin marketplace add lexfi/financial-advisor-skills
claude plugin install advisor-core@financial-advisor-skills
claude plugin install advisor-client@financial-advisor-skills
claude plugin install advisor-markets@financial-advisor-skills
```

`advisor-core` is required. Add other categories as needed (companies,
portfolio, macro, cio).

## 3. Run Your First Workflow

Just describe the job — skills trigger on natural language:

> Morning brief. My watchlist is AAPL, MSFT, NVDA, JPM, XOM.

> Prep me for Friday's annual review with a client holding 40% SPY, 25% AGG,
> 20% NVDA, 15% cash. They're worried about the NVDA position.

> Client just called asking why the market dropped — give me something.

## 4. Make It Yours

- **Paste context freely.** Portfolios, model names, client concerns — skills
  use what you give and ask at most one question when something essential is
  missing.
- **Set standing context.** Tell Claude your book's watchlist or house view
  once per session (or keep it in a project/CLAUDE.md file) and every skill
  will use it.
- **Client drafts are drafts.** Anything marked client-ready is for your
  review and personalization. Nothing is ever sent anywhere.

## Privacy Notes

- Client data you paste stays in your Claude conversation; skills never
  transmit it to Lexfi or anywhere else. Lexfi calls carry tickers and market
  queries, not client identities.
- Prefer initials or labels ("Client H") over full client names — the
  skills work identically.
