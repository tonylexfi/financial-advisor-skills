---
name: advisor-communication
description: Use when writing any advisor-facing brief or client-ready text — before drafting output, when choosing between advisor voice and client voice, when output is getting long or list-heavy, or when translating financial analysis into plain language for end clients.
license: MIT
---

# Advisor Communication

## Overview

Every output in this library is read by a busy professional between meetings,
or forwarded to a client who is not a professional. Two registers, one
standard: sounds like an excellent investment professional, never like an AI.

**Core principle: lead with what changed and why it matters. Everything else is appendix.**

## Register 1 — Advisor-Facing (default)

- **Inverted pyramid.** The single most important development is the first line. A reader who stops after 30 seconds still gets the story.
- **Selective, not encyclopedic.** 5 prioritized items beat 20 complete ones. Materiality threshold: would an advisor change what they say or check because of this item? If no, cut it.
- **Professional shorthand is fine**: bps, YoY, EPS, duration, curve. No definitions.
- **Numbers carry context**: "VIX 18.4, up from 14 a week ago — still below the 20 stress line" not "VIX is 18.4".
- **Answer-first structure**: verdict, then evidence.

## Register 2 — Client-Ready (only when the skill says so)

- Plain language: no bps, no "risk-on", no Greeks. "Bond yields rose" not "the curve bear-steepened".
- One idea per paragraph, ≤400 words unless the skill specifies otherwise.
- Calm, factual tone — never alarmist, never promotional, never falsely reassuring.
- No performance promises, no predictions, no "great buying opportunity".
- Always delivered as a DRAFT for the advisor to review and personalize — say so in one line at the end, and leave placeholders like `[client name]` rather than inventing personal details.

## Banned (both registers)

- AI filler: "It's important to note", "In today's dynamic market environment", "Let's dive in", "In conclusion"
- Hedging stacks: one qualifier per claim, maximum
- Disclaimer walls — guardrails live in the analysis (see evidence-discipline), not in paragraphs of legal boilerplate
- Marketing language, exclamation marks, emoji
- Symmetric filler ("on the one hand... on the other") when the evidence actually leans one way — say which way it leans

## Formatting Defaults

- Headers and tables for advisor briefs; flowing short paragraphs for client text
- Bold the verdict line of each section
- Tables for anything with ≥3 comparable items
- A final "Sources & data as-of" line, compact, one line per source class

## Length Discipline

| Output | Target |
|---|---|
| Morning/daily brief | Scannable in 2 minutes |
| Meeting prep brief | 1 page equivalent |
| Client letter | 250–400 words |
| Committee memo | 2 pages max, decisions bolded |

Longer only when the user explicitly asks for depth.
