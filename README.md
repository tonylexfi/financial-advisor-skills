# Financial Advisor Skills for Claude

**Recurring advisor workflows as installable Claude Skills — powered by [Lexfi MCP](https://lexfi.ai).**

An advisor thinks *"I need to prep for tomorrow's client meeting"* and Claude
already knows the workflow: identify the holdings, pull current intelligence
through Lexfi, separate facts from interpretation, and hand back a one-page
brief — in the advisor's language, at the advisor's altitude.

```
You:    Prep me for tomorrow's review with the Hendersons — portfolio attached,
        they're nervous about tech concentration.

Claude: [client-meeting-prep] → CLIENT MEETING BRIEF
        THE ONE THING: NVDA reported Wednesday — beat and raise, stock +9%,
        which pushed their tech sleeve from 34% to 37% of the portfolio...
```

## Who This Is For

Wealth advisors, financial planners, private bankers, relationship managers,
portfolio managers, and CIO/committee teams. **No technical background
required** — install once, then ask for the workflow in plain language. The
skills handle tool selection, data retrieval, and analysis discipline
invisibly.

## Why These Are Different

Most "finance prompts" are generic templates over the model's stale general
knowledge. These skills are **structured workflows over live financial
intelligence**:

1. **MCP-native.** Every skill defines exactly which Lexfi tools to call, in
   what order, what to batch, and what to skip. No wasted calls, no guessed data.
2. **Evidence-disciplined.** Outputs separate **Fact → Signal → Interpretation
   → Recommendation**. Missing data is reported missing, never fabricated. An
   inference is never dressed as a fact.
3. **Advisor-first.** Every output is built to be used between meetings: what
   changed, why it matters, what to ask, what to watch. Triage over digest.
4. **Two registers.** Advisor-facing briefs are dense and professional;
   client-ready drafts are plain-language, calm, and always delivered as
   drafts for the advisor's review — the advisor stays the decision-maker.

## Architecture

```
                    ┌─────────────────────────────┐
   Advisor request  │   Workflow skill            │   Lexfi MCP
  ─────────────────▶│   (client-meeting-prep, …)  │◀──────────────
                    │                             │  earnings calls,
                    │  built on advisor-core:     │  fundamentals, news,
                    │  · lexfi-mcp-playbook       │  sentiment, macro,
                    │  · evidence-discipline      │  CB communication,
                    │  · advisor-communication    │  rates pricing, …
                    └─────────────────────────────┘
```

`advisor-core` is the substrate every workflow skill imports: the Lexfi tool
routing table (with its real traps documented), the evidence ladder, and the
communication standard. Workflow skills stay small because the shared
discipline lives in one place.

## Installation

**Prerequisite:** the Lexfi MCP server connected to your Claude environment
(Claude Desktop, Claude Code, or claude.ai connectors). See
[docs/lexfi-mcp.md](docs/lexfi-mcp.md).

### Claude Code

```bash
claude plugin marketplace add lexfi/financial-advisor-skills
claude plugin install advisor-core@financial-advisor-skills   # required first
claude plugin install advisor-client@financial-advisor-skills
claude plugin install advisor-markets@financial-advisor-skills
# ... any other category you need
```

### Manual (any Claude Skills environment)

```bash
git clone https://github.com/lexfi/financial-advisor-skills
cp -r financial-advisor-skills/plugins/advisor-core/skills/* ~/.claude/skills/
cp -r financial-advisor-skills/plugins/advisor-client/skills/* ~/.claude/skills/
```

Always install `advisor-core` — every workflow skill depends on it.

## Skill Library

| Plugin | Skill | You say... |
|---|---|---|
| **advisor-core** | `lexfi-mcp-playbook` | (used automatically by other skills) |
| | `evidence-discipline` | (used automatically) |
| | `advisor-communication` | (used automatically) |
| **advisor-client** | `client-meeting-prep` | "Prep me for my meeting with..." |
| | `client-market-update` | "Draft my monthly client letter" |
| | `portfolio-change-explainer` | "Help me explain why we sold X" |
| | `why-did-the-market-move` | "Why is the market down today?" |
| **advisor-markets** | `morning-market-brief` | "Morning brief" |
| | `market-risk-monitor` | "How stressed is the market right now?" |
| **advisor-companies** | `earnings-call-brief` | "What did NVDA report?" |
| | `company-snapshot` | "Brief me on Palantir" |
| **advisor-portfolio** | `holdings-news-monitor` | "Scan my book for anything happening" |
| | `portfolio-risk-review` | "Review the risk in this portfolio" |
| **advisor-macro** | `central-bank-monitor` | "What's priced for the next Fed meeting?" |
| | `macro-regime-brief` | "Where are we in the cycle?" |
| **advisor-cio** | `investment-committee-brief` | "Prep Thursday's IC memo" |

Tier 2/3 roadmap (thesis challenge, management guidance tracker, sector
rotation monitor, EM country briefs, and more): [docs/design-notes.md](docs/design-notes.md).

## Example Workflows

**The daily loop** — `morning-market-brief` at the open → `why-did-the-market-move`
when a client calls → `holdings-news-monitor` before close.

**The review cycle** — `holdings-news-monitor` (what happened) →
`portfolio-risk-review` (what it means structurally) → `client-meeting-prep`
(the meeting) → `portfolio-change-explainer` (after decisions are made).

**The macro stack** — `macro-regime-brief` quarterly → `central-bank-monitor`
each policy week → `client-market-update` monthly.

More composition recipes: [docs/advisor-workflows.md](docs/advisor-workflows.md).

## What These Skills Will Not Do

- Give personalized investment advice or account-level buy/sell instructions —
  outputs inform the **advisor's** process; suitability stays human.
- Fabricate or estimate missing financial data.
- Present market predictions as facts, or model signals as certainties.
- Send client-facing text anywhere — client drafts are always drafts.

These aren't disclaimers bolted on at the end; they're enforced by
`evidence-discipline`, which every skill imports.

## Contributing

New skills welcome — the bar is a real recurring advisor workflow, made
materially better by Lexfi data. Read [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/skill-development.md](docs/skill-development.md), start from
[templates/SKILL-template.md](templates/SKILL-template.md).

## License

MIT — see [LICENSE](LICENSE).
