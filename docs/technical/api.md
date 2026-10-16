# API (frontend ↔ backend contract)

> ⏳ **To be written after the stack decision.** Ebubekir (backend) and Ali (frontend) agree on it together before the first dashboard PR.

The frontend uses **only** the endpoints listed here. A new or changed endpoint is a structural change: update this file in the same PR.

## Format per endpoint

```
### GET /agents/{id}/metrics
Purpose:   …
Params:    period (optional, e.g. 30d)
Response:  200 { "agent_id": "...", "total_tokens": 0, "same_path_share": 0.0, "uniform_agent": false }
Errors:    404 if agent unknown
```

## Endpoints

_None yet._
