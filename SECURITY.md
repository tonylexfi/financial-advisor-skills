# Security Policy

## Scope

This repository contains Claude Skills — markdown instruction files. They contain no
executable code paths of their own, but they instruct an AI model that has access to
tools, client data pasted into conversations, and the Lexfi MCP server.

## Reporting a Vulnerability

Report security issues to **security@lexfi.ai**. Do not open public issues for:

- Prompt-injection vectors inside skill files (instructions that could cause data
  exfiltration, unauthorized tool calls, or bypass of the evidence-discipline rules)
- Skills that instruct the model to send client data to external endpoints
- Supply-chain concerns in the install scripts

We aim to acknowledge reports within 72 hours.

## Design Rules That Protect Users

Every skill in this repository must comply with these rules (enforced in review):

1. **No outbound data movement.** Skills never instruct Claude to send portfolio or
   client data anywhere except the Lexfi MCP tools the user has already connected.
2. **Client data stays local to the conversation.** Skills operate on what the
   advisor pastes or uploads; they never instruct Claude to persist, log, or
   transmit client PII.
3. **No credential handling.** Skills must never ask for API keys, account numbers,
   or login credentials.
4. **Injection resistance.** Retrieved content (news, transcripts, social highlights)
   is data, not instructions. The core `evidence-discipline` skill makes this explicit
   and every workflow skill inherits it.
5. **No fabrication.** Skills require missing data to be reported as missing, never
   estimated silently. Fabricated financial data is treated as a security defect,
   not a quality defect.
