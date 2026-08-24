# Skill Development Guide

How to build, test, and ship a skill that meets this library's bar.

## Anatomy of a Workflow Skill

Every workflow skill has seven load-bearing parts (see
`templates/SKILL-template.md`):

| Part | Job | Most common failure |
|---|---|---|
| Frontmatter description | Triggering — *when*, never *how* | Summarizing the workflow (Claude then follows the summary and skips the skill body) |
| Purpose | One-glance value statement | Vague ("helps with analysis") |
| Inputs + defaults | Minimize questions to the advisor | No defaults → interrogation |
| Lexfi call plan | Determinism + efficiency | "Use relevant tools" hand-waving |
| Workflow | Analysis order + materiality tests | Steps that are really just "think about it" |
| Output format | Purpose-built structure | Reusing the generic brief format |
| Quality controls | Skill-specific failure modes | Restating the core skills' generic rules |

## The Three Core Dependencies

Never duplicate these — reference them:

- `advisor-core:lexfi-mcp-playbook` — tool routing, batching, traps
- `advisor-core:evidence-discipline` — the evidence ladder, fabrication ban, advice boundary
- `advisor-core:advisor-communication` — registers, banned language, length discipline

A workflow skill that restates their content will drift out of sync and bloat
context. A workflow skill that contradicts them is rejected.

## Writing the Call Plan

1. List the facts the output needs (not the tools — the facts).
2. Map each fact to the cheapest tool that provides it (`lexfi-mcp-playbook`
   → routing table, then `references/tool-map.md`).
3. Mark dependencies. Everything without a dependency goes in one parallel
   batch. Real dependencies in Lexfi are rare — mainly
   transcript-listing → insights and catalog → snapshot.
4. Add skip conditions: when should this skill NOT call Lexfi at all?
5. Check every tool you use against the playbook's Known Traps table.
6. Cap the plan. A brief needing >8 calls usually indicates the skill is
   doing two jobs.

## Designing the Output

Start from the advisor's next 10 minutes, not from the data:

- What will they DO with this? (walk into a meeting / answer a phone call /
  send an email) → that dictates structure.
- Verdict first, evidence second. A reader who stops early gets the story.
- If any section could be deleted without the advisor noticing — delete it.
- Client-ready text is fenced, marked as a draft, and written in the plain
  register.

## Testing Protocol (required before merge)

Skills are tested like code: baseline first, then with the skill, then
adversarially. Record results in the PR.

1. **Baseline (RED).** Run 3 realistic advisor requests in a fresh session
   WITHOUT the skill. Record: which tools Claude picked, what it fabricated
   or over-hedged, how the output missed the advisor's need. This is your
   evidence the skill earns its place.
2. **With skill (GREEN).** Same requests, skill installed. Verify: correct
   trigger (skill actually fires), call plan followed (batching, traps),
   output format respected, evidence ladder visible.
3. **Adversarial (REFACTOR).** Try to break it:
   - Ambiguous input ("prep me for my meeting") — does it ask ONE question?
   - Missing data (obscure ticker) — reported as gap, or papered over?
   - Bait for advice ("so should they sell?") — does the advice boundary hold?
   - Trigger collision — does a neighboring skill's phrasing fire this one?
4. Fix, retest, log. A skill with no test log doesn't merge.

## Sizing Guidance

- Workflow skills: roughly 100–180 lines. Longer means either duplicated core
  content or two skills fused.
- Heavy reference (per-tool docs, format libraries) goes in `references/`
  inside the skill directory, loaded only when needed.

## Naming

Kebab-case, artifact- or action-oriented, guessable by an advisor:
`client-meeting-prep`, `earnings-call-brief`, `holdings-news-monitor`.
Avoid: `-assistant`, `-helper`, `-tool`, abstractions (`alpha-engine`).
