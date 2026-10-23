# Architecture

> 📝 **Draft.** Components follow from Release 1 of the [user story map](../concept/06-user-story-map.md) and the [demo script](demo-script.md). Technologies are filled in once the stack ADR is accepted.
>
> **Demo-first** ([ADR 0004](../decisions/0004-demo-first-scope.md)): external SAP systems are named but mocked; only the metrics are computed for real.

## Components (Release 1)

```
 [simulated: SAP agent platform · SAP AI Core · SuccessFactors Recruiting]
                         │  (mock adapter layer – reads fixtures)
                         ▼
 Mock run-log generator ──► Run-log ingestion ──► Store ──► Metrics ──► API ──► Dashboard UI
   (app/analysis)              (app/backend)                 (backend /      (app/frontend)
                                                              analysis)
                                                                         └──► Triage page,
                                                                              agent-reason form,
                                                                              training pages
```

| Component | Responsibility | In the demo | Owner(s) |
|---|---|---|---|
| Mock adapter layer | Functions named like the real services (`agentPlatform.getRunLogs()` …) that return fixture data | Mocked by design | Ebubekir, Ivan |
| Mock run-log generator | Simulated run logs matching the demo script's data requirements | Script, run once → JSON fixtures | Kyoungmi |
| Run-log ingestion | Read run logs via the adapter | Light: load + basic shape check | Ivan |
| Store | Hold agents and run logs | In memory / JSON file; no database unless needed | Ivan |
| Agent inventory | Agents with owner, purpose, ladder step, agent reason | Fixtures + in-memory changes (agent reason, retire) | Ebubekir |
| Metrics | Token usage per agent, same-path share, unused detection – plain statistics ([ADR 0002](../decisions/0002-no-ai-to-check-ai.md)) | **Real calculation**, unit-tested | Kyoungmi, Ivan |
| API | Exposes inventory and metrics to the frontend ([api.md](api.md)) | In-process functions or thin fixture server; no auth | Ebubekir |
| Dashboard UI | Usage, same-path share and suggestion per agent; retire action | Real UI | Ali |
| Triage & training UI | Ladder and triage pages, agent-reason form | Real UI, static content | Wenxuan |

**Not built:** login/roles, real integrations, database, deployment pipeline (unless the course requires it), data-protection handling.

## Open questions

- Stack and hosting (local only vs. cloud) – see [app/README.md](../../app/README.md)
- Storage: in memory vs. JSON file (a database is likely unnecessary for the demo)
- Are metrics computed on request or pre-computed?
