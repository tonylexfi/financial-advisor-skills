# Advisor Workflows — Composition Recipes

Skills are modular; the leverage is in chaining them. Outputs of one skill are
context for the next — Claude carries the thread within a session.

## The Daily Loop

| When | Skill | Prompt |
|---|---|---|
| Pre-open | `morning-market-brief` | "Morning brief" (watchlist remembered in session/project context) |
| Client calls | `why-did-the-market-move` | "Client asking about the selloff — give me something" |
| Midday | `earnings-call-brief` | "What did [holding] report?" (on report days) |
| Close | `holdings-news-monitor` | "Scan the book" |

## The Review Cycle (per client, quarterly)

1. `holdings-news-monitor` — "Scan the Hendersons' portfolio, last 90 days" →
   what happened.
2. `portfolio-risk-review` — "Now review the structural risk" → what it means.
   (Reuses the holdings already in context — no re-pasting.)
3. `client-meeting-prep` — "Prep Friday's review; they're nervous about tech
   concentration" → the meeting brief, informed by both prior outputs.
4. After decisions: `portfolio-change-explainer` — "We trimmed NVDA to 12%,
   rationale: concentration. Draft the client note."

## The Macro Stack

- Quarterly: `macro-regime-brief` → backdrop for allocation conversations.
- Policy weeks: `central-bank-monitor` → "What's priced for Wednesday?"
- Monthly: `client-market-update` → the letter, consistent with the
  regime brief already in context.

## The Committee Rhythm (CIO teams)

1. `market-risk-monitor` + `macro-regime-brief` early in the week — the
   evidence base.
2. `investment-committee-brief` — "IC is Thursday; agenda: tech overweight,
   duration extension. House view attached." The challenge section stress-tests
   the house view against the week's evidence.
3. After the meeting: `client-market-update` or `portfolio-change-explainer`
   to communicate outcomes downstream.

## Composition Rules of Thumb

- **Order: facts → structure → communication.** Monitors and briefs first,
  reviews second, client-facing drafts last — each layer grounds the next.
- **Don't re-paste.** Skills read the session; say "same portfolio" and move on.
- **Standing context pays.** Keep watchlist, model portfolios, and house view
  in project instructions; every skill picks them up silently.
- **One skill per ask.** "Morning brief and also review this portfolio and
  draft a letter" works, but sequential asks produce sharper outputs.
