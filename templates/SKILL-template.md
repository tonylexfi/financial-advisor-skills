---
name: skill-name-kebab-case
description: Use when [triggering situations, symptoms, and example advisor phrasings — NEVER a summary of the workflow. Third person. Under 500 chars.]
license: MIT
---

# Skill Title

**REQUIRED BACKGROUND:** advisor-core:lexfi-mcp-playbook, advisor-core:evidence-discipline, advisor-core:advisor-communication

## Purpose

One or two sentences: what the advisor gets and why it saves them time or
makes them better in the meeting. If you can't say it in two sentences, the
skill is probably two skills.

## Required Inputs

The minimum the advisor must provide. Define defaults for everything you can
(lookback windows, scope). If input is missing, ask ONE compact question —
never interrogate.

## Optional Inputs

What sharpens the output if provided.

## Lexfi MCP Calls

The call plan — this section is the heart of an MCP-native skill:

- Which tools, with which parameters (windows, limits, table subsets)
- What runs in ONE parallel batch vs what genuinely must be sequenced
- Conditional calls ("only if X") and explicit skip conditions
- Which playbook traps apply (check `lexfi-mcp-playbook` → Known Traps)

## Workflow

Numbered steps from inputs → analysis → prioritization. State the materiality
test if the skill triages. State where interpretation happens so the evidence
ladder is enforced by structure.

## Output Format

A purpose-built format for THIS workflow — not the generic brief. Show it as a
fenced block. Rules of thumb:

- Verdict/most-important-thing first
- Tables for ≥3 comparable items
- Client-ready sections clearly fenced off and marked as drafts
- End with one compact "Sources & data as-of" line

## Quality Controls

3–6 checks specific to this skill (coverage guarantees, banned failure modes,
length caps). Generic rules live in the core skills — don't repeat them.

## Failure Handling

What to do on tool errors, unresolvable tickers, empty results, partial data.
Default: report gaps honestly, deliver everything else.
