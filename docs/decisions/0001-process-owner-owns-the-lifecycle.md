# ADR 0001 – The process owner owns the whole lifecycle

- **Status:** accepted
- **Date:** 2026-10-02

## Context

Early drafts (first concept deck, EventStorming board) assumed that an AI developer or engineer builds automations and converts agents into workflows, and that triage is a separate approval step.

## Decision

The **process owner** is the only actor across the lifecycle:

- she learns the automation ladder and the triage in **training**
- she **applies the triage herself** while building – there is no approval gate
- she reads the dashboard and **converts her own agents** to workflows

AI developers may support in practice, but consulting them is **out of scope** for rAIght.

## Consequences

- rAIght must make conversion doable without coding skills → **guided conversion** (draft workflow from frequent paths).
- There is no up-front check of triage decisions → the **dashboard is the check after the fact** (hotspot H2).
- Process owners' time is the main cost and adoption risk → incentives (carbon budget) matter (hotspot H7).
- The EventStorming board and the first concept deck are outdated on this point.
