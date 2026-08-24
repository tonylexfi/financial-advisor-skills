# Contributing

## What Belongs Here

A skill earns its place by passing all four gates:

1. **Recurring workflow.** A real advisor does this weekly or more. One-off
   analyses don't become skills.
2. **Lexfi-improved.** Live data through Lexfi MCP makes the output materially
   better than model knowledge alone. If it doesn't, it's a prompt, not a skill
   for this library.
3. **Distinct.** It doesn't overlap an existing skill's trigger space. Extend
   an existing skill before adding a near-duplicate.
4. **Decision-adjacent.** The output helps an advisor decide, prepare,
   communicate, or save time — not just "interesting analysis".

## Process

1. Open an issue describing the workflow: who runs it, how often, what the
   output looks like, which Lexfi tools it needs.
2. Fork, copy `templates/SKILL-template.md` into
   `plugins/advisor-<category>/skills/<skill-name>/SKILL.md`.
3. Follow [docs/skill-development.md](docs/skill-development.md) — including
   the testing protocol. Untested skills are not merged.
4. Run `python3 scripts/validate.py` (structure + frontmatter checks).
5. PR with: the skill, a filled-in test log (from the testing protocol), and a
   sample output in `examples/` if the skill introduces a new output format.

## Review Standard

Reviewers check, in order:

- **Safety:** no fabrication paths, no advice-boundary violations, no
  instructions that could move client data outside the conversation, retrieved
  content treated as data (see SECURITY.md).
- **MCP plan:** minimal call set, correct sequencing, parallel batching,
  known traps handled (see `advisor-core/skills/lexfi-mcp-playbook`).
- **Evidence discipline:** output format forces Fact → Signal →
  Interpretation → Recommendation separation.
- **Trigger quality:** frontmatter description states *when to use* (symptoms,
  phrasings) — never a summary of the workflow.
- **Output design:** purpose-built format, not the generic brief template.
- **Length:** the skill is as short as it can be while unambiguous.

## Style

- Names: kebab-case, verb-or-artifact oriented (`client-meeting-prep`, not
  `meeting-preparation-assistant`).
- Cross-reference core skills by name (`advisor-core:lexfi-mcp-playbook`);
  never duplicate their content into workflow skills.
- American English, professional register, no marketing language.

## Versioning

Plugins carry semver in `plugin.json`. Breaking a skill's output format or
trigger space is a minor bump; typo/clarity fixes are patches.
