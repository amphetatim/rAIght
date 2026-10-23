# Architecture

> **Pure clickable demo** ([ADR 0006](../decisions/0006-pure-clickable-demo.md)): frontend only, finished sample data, no backend. Framework: _TBD (#18 → ADR 0007)_.

## The demo

```
 app/data/*.json  ──►  pages (P1–P7)  inside the app shell (P0)
 finished sample        Start · Learn · Plan · Inventory · Dashboard · Agent detail · Escalations
 data (D1)              client-side state only (triage answers, retired agent, filters)
```

| Part | Responsibility | Issue | Owner(s) |
|---|---|---|---|
| App shell | Navigation, layout, design tokens, loading the JSON files | P0 | Wenxuan |
| Sample data | Agents with finished metrics, summary, content texts ([sample-data.md](sample-data.md)) | D1 | Kyoungmi, Ebubekir |
| Start page | Welcome, the four steps, headline numbers | P1 | Wenxuan |
| Learn | Automation ladder, triage cheat sheet | P2 | Kyoungmi |
| Plan an automation | Clickable triage, agent reason | P3 | Ebubekir |
| Agent inventory | All agents across providers | P4 | Ivan |
| Dashboard | Summary, attention list, agent table | P5 | Ali |
| Agent detail | Paths, suggestion, retire | P6 | Ali, Ivan |
| Escalations *(optional)* | Cases routed to Lena | P7 | Ebubekir |

**Not built:** backend, API, provider connections, database, login, deployment pipeline (unless needed for the recording).

## The real product (for the pitch only)

The real rAIght would read run logs from each provider through one source adapter per provider, normalise them into one schema ([data-model.md](data-model.md)) and calculate the metrics with plain statistics ([ADR 0002](../decisions/0002-no-ai-to-check-ai.md)). This is shown on a slide, not built.
