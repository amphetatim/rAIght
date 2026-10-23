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

- **Demo-first** ([ADR 0004](../docs/decisions/0004-demo-first-scope.md)): build only what the [demo script](../docs/technical/demo-script.md) shows. If a task isn't in it, ask before building.
- **All external data goes through mock source adapters, one per provider** ([ADR 0005](../docs/decisions/0005-scope-external-agents.md)), named like the real services (`copilotStudio.getRunLogs()`, `powerAutomate.getRunLogs()`, `openAI.getRunLogs()`, `n8n.getRunLogs()`), reading fixtures and returning the **common run-log schema**. Metrics never branch on the provider. Never call real external systems.
- The frontend gets data only via the endpoints/functions in [docs/technical/api.md](../docs/technical/api.md). They can be in-process functions or a thin fixture server; no auth, no production error handling.
- The data shape is defined in [docs/technical/data-model.md](../docs/technical/data-model.md). If you need a new field, update that file in the same PR.
- **Metrics are deterministic statistics** (counts, shares, sums) – no model calls ([ADR 0002](../docs/decisions/0002-no-ai-to-check-ai.md)).
- **Mock data only.** Run logs are simulated (fixtures must match the demo script's data requirements). No real personal data.
- **Metrics must be real calculations** on that data. Never hard-code a metric result to make the demo look right; fix the fixtures instead.
- Use glossary names in code: `agent_reason`, `same_path_share`, `run_log`, `ladder_step`, `uniform_agent`.
