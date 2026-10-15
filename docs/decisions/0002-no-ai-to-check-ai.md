# ADR 0002 – Monitoring uses statistics on existing logs, not AI

- **Status:** accepted
- **Date:** 2026-10-02

## Context

To find agents that behave like workflows, we could let another AI model review agent behaviour. That would add compute and emissions – the very thing rAIght is meant to reduce.

## Decision

The dashboard uses **simple statistics on run logs that already exist**: token usage, and the share of runs with an identical sequence of steps (same-path share). AI-based review is reserved for **sampled, targeted** cases and is not part of Release 1.

## Consequences

- Release 1 needs no new data source and no model calls → feasible early.
- Agents must write run logs with tokens and steps; agents found outside the platform (see hotspot H3) only show token usage until they log steps.
- Text similarity alone is not enough (hotspot H4); path similarity is the primary signal.
