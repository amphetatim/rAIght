# Architecture

> 📝 **Draft.** Components follow from Release 1 of the [user story map](../concept/06-user-story-map.md) and the [demo script](demo-script.md). Technologies are filled in once the stack ADR is accepted.
>
> **Demo-first** ([ADR 0004](../decisions/0004-demo-first-scope.md)): external systems are named but mocked; only the metrics are computed for real.
> **Scope** ([ADR 0005](../decisions/0005-scope-external-agents.md)): sources are external providers – Copilot Studio, Power Automate, OpenAI, n8n.

## Components (Release 1)

```
 [simulated providers: Copilot Studio · Power Automate · OpenAI · n8n]
      │ one source adapter per provider (mock – reads fixtures)
      ▼ converts into ONE common run-log schema
 Mock run-log generator ──► Run-log ingestion ──► Store ──► Metrics ──► API ──► Dashboard UI
   (app/analysis)              (app/backend)                 (backend /      (app/frontend)
                                                              analysis)
                                                                         └──► Triage page,
                                                                              agent-reason form,
                                                                              training pages
```

| Component | Responsibility | In the demo | Owner(s) |
|---|---|---|---|
| Source adapters (mock) | One per provider, named like the real service (`copilotStudio.getRunLogs()`, `powerAutomate…`, `openAI…`, `n8n…`); each returns fixture data **in the common schema** ([data-model.md](data-model.md)) | Mocked by design | Ebubekir, Ivan |
| Mock run-log generator | Simulated run logs matching the demo script's data requirements | Script, run once → JSON fixtures | Kyoungmi |
| Run-log ingestion | Read run logs via the adapter | Light: load + basic shape check | Ivan |
| Store | Hold agents and run logs | In memory / JSON file; no database unless needed | Ivan |
| Agent inventory | Agents from **all providers** with owner, purpose, provider, ladder step, agent reason (H3) | Mocked import + in-memory changes (agent reason, retire) | Ebubekir |
| Metrics | Token usage per agent, same-path share, unused detection – plain statistics ([ADR 0002](../decisions/0002-no-ai-to-check-ai.md)) | **Real calculation**, unit-tested | Kyoungmi, Ivan |
| API | Exposes inventory and metrics to the frontend ([api.md](api.md)) | In-process functions or thin fixture server; no auth | Ebubekir |
| Dashboard UI | Usage, same-path share and suggestion per agent, provider column + filter; retire action | Real UI | Ali |
| Triage & training UI | Ladder and triage pages, agent-reason form | Real UI, static content | Wenxuan |

**Not built:** login/roles, real integrations, database, deployment pipeline (unless the course requires it), data-protection handling.

## Open questions

- Stack and hosting (local only vs. cloud) – see [app/README.md](../../app/README.md)
- Storage: in memory vs. JSON file (a database is likely unnecessary for the demo)
- Are metrics computed on request or pre-computed?
- What step-level data the real providers expose (hotspot H8) – affects how plausible the adapters are, not the demo itself
