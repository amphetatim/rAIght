# ADR 0004 – Demo-first scope

- **Status:** accepted
- **Date:** 2026-10-18
- **Partly superseded by:** [ADR 0006](0006-pure-clickable-demo.md) – no source adapters, no API, metrics not calculated; pure clickable demo on finished sample data
- **Amended by:** [ADR 0005](0005-scope-external-agents.md) – the external systems are now third-party providers (Copilot Studio, Power Automate, OpenAI, n8n), not SAP platforms

## Context

IS 613 asks for a working prototype of rAIght, not a production system. A real implementation would need integrations with SAP systems (agent platform, SAP Build, SAP AI Core, HR systems), authentication, persistence and data protection, which is far more than a course project can or needs to deliver. Without a clear boundary, effort goes into plumbing nobody sees in the demo.

## Decision

We build a **demo**: software that runs reliably along a defined **demo script** and makes the concept tangible.

| Area | In the demo |
|---|---|
| External systems (providers: Copilot Studio, Power Automate, OpenAI, n8n; HR system: SuccessFactors) | **Named and shown** in UI and architecture, served by **mock adapters** with fixture data |
| APIs | Defined in [`api.md`](../technical/api.md) so the architecture is credible; implemented only as far as the demo needs them (in-process functions or a thin fixture server) |
| Data | Generated mock run logs (JSON fixtures), designed so the demo story works |
| Metrics (token usage, same-path share, unused) | **Computed for real** on the mock data. This is the core of the idea, it's cheap, and it must be honest |
| Auth, roles, persistence beyond what the demo needs, scaling, data protection, production error handling | **Out of scope.** Covered in the pitch/business case where relevant |
| Scope boundary | The [demo script](../technical/demo-script.md): what isn't in the script isn't built |

**Seam rule:** all external data goes through one mock adapter layer whose functions are named like the real services (e.g. `copilotStudio.getRunLogs()`). Today they read fixtures; in principle they could call a real API.

## Consequences

- Much less work on infrastructure; the focus is on the visible journey and the metric logic.
- A simple stack and local execution are enough; deployment only if the course requires it.
- Hotspots H3 (agent inventory for existing agents, #20) and H6 (data protection / works council, #21) are not built; they're addressed in the pitch and business case.
- Tests focus on the metric functions; the rest is checked by running the demo script.
- Risk: the demo looks "too real". In the pitch, say clearly which parts are simulated.
