# app/ – implementation context

Loaded automatically when Claude works inside `app/`. Keep it short and specific to the code.

## Status

**Stack not decided.** Until the tech-stack ADR is accepted: no framework, no dependencies, no scaffolding here (see [README.md](README.md)).

## Planned layout (confirm with the stack ADR)

| Folder | Owners | Content |
|---|---|---|
| `app/frontend/` | Ali, Wenxuan | Dashboard, triage page, agent-reason form, training pages |
| `app/backend/` | Ebubekir, Ivan | API, data model, run-log ingestion, metrics endpoints |
| `app/analysis/` | Kyoungmi, Ivan | Mock run-log generator, same-path detection |

Each folder gets its own `CLAUDE.md` once it exists (structural change → confirm first).

## Rules that apply to all code

- The **frontend talks to the backend only via the endpoints in [docs/technical/api.md](../docs/technical/api.md)**. No direct data access.
- The data shape is defined in [docs/technical/data-model.md](../docs/technical/data-model.md). If you need a new field, update that file in the same PR.
- **Metrics are deterministic statistics** (counts, shares, sums) – no model calls ([ADR 0002](../docs/decisions/0002-no-ai-to-check-ai.md)).
- **Mock data only.** Run logs are simulated for the four recruiting agents in the concept. No real personal data.
- Use glossary names in code: `agent_reason`, `same_path_share`, `run_log`, `ladder_step`, `uniform_agent`.
