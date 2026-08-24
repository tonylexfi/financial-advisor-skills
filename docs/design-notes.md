# Design Notes — Strategy, Benchmark, Taxonomy

The reasoning behind the repository. Read this before proposing structural
changes.

## 1. Repository Strategy

**Thesis:** advisors don't need more financial information — they need
recurring workflows executed with live data and professional discipline. So
the unit of value here is a *workflow*, not a prompt and not a dataset.

Three architectural commitments follow:

1. **Core/workflow split.** Tool knowledge, evidence rules, and voice live
   once in `advisor-core`; workflow skills stay ~150 lines and can't drift
   from the shared discipline. This is the single biggest maintainability
   decision in the repo.
2. **MCP-native by construction.** Every workflow skill ships a concrete call
   plan (tools, params, batching, skip conditions) instead of "use available
   tools". Determinism is what makes outputs auditable — an advisor can ask
   "where did this number come from" and get an answer.
3. **Category plugins.** Advisors install by job family (client, markets,
   companies, portfolio, macro, cio), not all-or-nothing. A solo RIA installs
   3 plugins; a CIO team installs all 7.

**Product bar:** every output must survive the question *"would a good
advisor pay attention to this between meetings?"* Anything encyclopedic fails.

## 2. Competitive Benchmark

### anthropics/financial-services

- **Adopted:** marketplace + plugin architecture; category bundles; skills as
  the unit, plugins as the distribution; validation scripting; the idea of a
  shared core plugin holding connectors/discipline.
- **Rejected:** the agent-plugin + skill-sync machinery (copies of skills
  synced by script). Powerful for their multi-agent product, but a
  maintenance tax with no payoff at this library's scale — cross-references
  beat synced copies.
- **Gap we fill:** their wealth-management vertical is modeling/IB-centric
  (comps, DCF, LBO). Advisors' actual week — meeting prep, client letters,
  book scans — is unserved.

### JoelLewis/finance_skills

- **Adopted:** domain-plugin layout with an always-installed `core`
  (our `advisor-core` is the same move, applied to discipline instead of
  math); consistent SKILL.md section contract; cross-reference conventions;
  install.sh fallback.
- **Rejected:** 91 knowledge skills. That library teaches Claude *concepts*
  (return calculations, Reg BI). Concepts don't need live data and largely
  duplicate model knowledge; we build workflows over live intelligence
  instead, and keep the count small deliberately.

### himself65/finance-skills

- **Adopted:** agent-skills open-standard frontmatter (name + description,
  portable across agents); per-skill directories; social/narrative data as a
  first-class intelligence category (our highlights tools).
- **Rejected:** flat "collection of interesting analyses" curation
  (options-payoff, saas-valuation-compression…). Analytically fun, but no
  recurring advisor pulls them weekly — our four-gate contribution test
  (recurring, Lexfi-improved, distinct, decision-adjacent) exists precisely
  to keep this out.

### Patterns none of the three had, which we added

- An explicit **evidence ladder** (Fact→Signal→Interpretation→Recommendation)
  enforced by output formats.
- A **tool-trap registry** (weather-vs-forecast, crypto-vs-equity sentiment,
  decimal units, two-step transcript retrieval) — learned from the live Lexfi
  schemas; this is where MCP skills actually fail in practice.
- **Two-register communication** with client text always fenced and marked
  as a draft.
- **Composition documentation** (advisor-workflows.md) — chains, not just
  units.

## 3. Skill Taxonomy & Prioritization

Selection filter (in order): frequency of the workflow × value of live data ×
distinctness × advisor-facing (not analyst-facing). Tier 1 is capped at what
one maintainer can keep excellent.

### Tier 1 — shipped (13 workflow + 3 core)

Client: client-meeting-prep, client-market-update,
portfolio-change-explainer, why-did-the-market-move.
Markets: morning-market-brief, market-risk-monitor.
Companies: earnings-call-brief, company-snapshot.
Portfolio: holdings-news-monitor, portfolio-risk-review.
Macro: central-bank-monitor, macro-regime-brief.
CIO: investment-committee-brief.

### Tier 2 — next (advanced workflows, same categories)

- `sector-rotation-monitor` (markets) — leadership shifts + flows
- `management-guidance-tracker` (companies) — guidance vs delivery across quarters, per holding
- `earnings-season-planner` (companies/portfolio) — book-wide reporting calendar + hurdles
- `investment-thesis-review` (companies) — thesis vs accumulated evidence
- `watchlist-intelligence` (portfolio) — candidate monitoring distinct from holdings
- `inflation-intelligence`, `labor-market-intelligence` (macro) — single-pillar deep dives
- `weekly-market-intelligence` (markets) — the Friday wrap, client-appendix included

### Tier 3 — specialized

- `investment-thesis-challenge` (cio) — standalone red-team of any thesis
- `market-scenario-analysis` (cio) — structured what-if narratives
- `em-country-brief` (macro) — weekly-series country workflows (catalog→snapshot machinery)
- `client-risk-conversation-prep` (client) — risk-tolerance conversations, regime-aware
- `research-agenda-generator` (cio) — gaps in the desk's coverage
- `narrative-tracker` (markets) — social/discourse trend workflows on the highlights tools

Deliberately excluded: portfolio optimizers, trade recommenders, performance
reporting (books-of-record own it), tax/estate advice, options strategy
builders — wrong side of the advice boundary or wrong data layer.

## 4. Testing Note

Skill descriptions and structures here follow tested conventions (trigger-only
descriptions, core-skill cross-references). Per-skill baseline/adversarial
test logs are required at contribution time (docs/skill-development.md); the
initial library should be run through that same protocol against a live
Lexfi-connected environment before the public launch tag.
