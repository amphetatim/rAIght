# Architecture

> 📝 **Draft.** Components follow from Release 1 of the [user story map](../concept/06-user-story-map.md). Technologies are filled in once the stack ADR is accepted.

## Components (Release 1)

```
 Mock run-log generator ──► Run-log ingestion ──► Store ──► Metrics ──► API ──► Dashboard UI
   (app/analysis)              (app/backend)                 (backend /      (app/frontend)
                                                              analysis)
                                                                         └──► Triage page,
                                                                              agent-reason form,
                                                                              training pages
```

| Component | Responsibility | Owner(s) |
|---|---|---|
| Mock run-log generator | Simulated run logs for the four recruiting agents (tokens, steps, output) | Kyoungmi |
| Run-log ingestion | Read and validate run logs, store them | Ivan |
| Agent inventory | Agents with owner, purpose, ladder step, agent reason | Ebubekir |
| Metrics | Token usage per agent, same-path share, unused detection – plain statistics ([ADR 0002](../decisions/0002-no-ai-to-check-ai.md)) | Kyoungmi, Ivan |
| API | Exposes inventory and metrics to the frontend ([api.md](api.md)) | Ebubekir |
| Dashboard UI | Usage, same-path share and suggestion per agent; retire action | Ali |
| Triage & training UI | Ladder and triage pages, agent-reason form | Wenxuan |

## Open questions

- Stack and hosting (local only vs. cloud) – see [app/README.md](../../app/README.md)
- Storage: files, SQLite or a database service?
- Are metrics computed on request or pre-computed?
