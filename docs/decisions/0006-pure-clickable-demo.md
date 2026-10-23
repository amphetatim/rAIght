# ADR 0006 – Pure clickable demo: frontend only, finished sample data

- **Status:** accepted
- **Date:** 2026-10-23
- **Supersedes:** parts of [ADR 0004](0004-demo-first-scope.md) – source adapters, API, and metrics "computed for real"

## Context

The deadline is **20 November 2026**. With ADR 0004 we still planned mock source adapters per provider, an API contract, a data model with run-log ingestion and real metric calculation. For what we need – a demo that tells Lena's story convincingly in the pitch and the video – that is more than necessary, and it splits six developers across layers nobody sees.

## Decision

We build a **purely clickable demo**:

| Area | Decision |
|---|---|
| Architecture | **Frontend only.** No backend, no API, no source adapters, no database |
| Data | **Finished sample data** in a few JSON files in `app/data/`: agents with their metrics already filled in (tokens, runs, same-path share, top paths, flags, suggestion), escalations, learning and triage content. The tech team elaborates the data foundation ([sample-data.md](../technical/sample-data.md)) |
| Metrics | **Not calculated** in the demo. The values in the sample data are written so the story works and stay consistent with each other |
| Interactions | Navigation, triage questions, retire button, filters – client-side state only, reset on reload |
| Providers | Still **named** in the UI (Copilot Studio, Power Automate, OpenAI, n8n – [ADR 0005](0005-scope-external-agents.md)), no logos, no connections |
| Backlog | **One issue per page** (P0–P7) plus sample data (D1) and the recording (X1). The old fine-grained user stories become checklists inside the page issues |
| Framework | Chosen by the Tech Leads (#18) – any frontend setup that runs locally and can be screen-recorded. Recorded as **ADR 0007** |

## Consequences

- Much smaller build; every developer owns a page, so work runs in parallel.
- `api.md` is obsolete; `data-model.md` is replaced by `sample-data.md`.
- Unit tests for metric logic are no longer needed – there is no logic. Quality check = clicking through the [demo script](../technical/demo-script.md).
- PR #26 (Python run-log validation and metrics) is not needed for the demo.
- In the pitch we say clearly: the demo shows **illustrative data**. The concept – plain statistics on run logs, no AI checking the AI ([ADR 0002](0002-no-ai-to-check-ai.md)) – still holds for the real product.
