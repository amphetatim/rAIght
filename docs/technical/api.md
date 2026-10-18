# API (frontend ↔ backend contract)

> ⏳ **To be written after the stack decision.** Ebubekir (backend) and Ali (frontend) agree on it together before the first dashboard PR.

The frontend uses **only** the endpoints listed here. A new or changed endpoint is a structural change: update this file in the same PR.

**Demo-first** ([ADR 0004](../decisions/0004-demo-first-scope.md)): this contract exists so the architecture is credible and frontend/backend can work in parallel. Endpoints are implemented **only as far as the [demo script](demo-script.md) needs them**: as in-process functions or a thin local server returning fixture-based data. No auth, no pagination, no versioning, minimal error handling. Mark each endpoint *implemented* or *documented only*.

## Format per endpoint

```
### GET /agents/{id}/metrics
Purpose:   …
Params:    period (optional, e.g. 30d)
Response:  200 { "agent_id": "...", "total_tokens": 0, "same_path_share": 0.0, "uniform_agent": false }
Errors:    404 if agent unknown
Demo:      implemented | documented only
```

## Endpoints

_None yet._
