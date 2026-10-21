# Simulated run-log format (R1)

This document defines the sample run-log format for the four recruiting agents used in the rAIght prototype.

## Record shape

Each run log is one JSON object with the following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique run identifier |
| `agent_id` | string | yes | Agent identifier |
| `started_at` | string (ISO-8601 UTC) | yes | Run start timestamp |
| `tokens_in` | integer | yes | Input tokens consumed |
| `tokens_out` | integer | yes | Output tokens produced |
| `outcome` | enum | yes | `success`, `escalated`, or `failed` |
| `steps` | array of step objects | yes | Ordered execution path |

Step object fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `order` | integer | yes | Position in the path (1..n) |
| `tool` | string | yes | Tool/action name for that step |

## Dataset file

The dataset is stored in [`simulated-run-logs.json`](./simulated-run-logs.json) as a JSON array.

## Coverage for issue #19

Included agents:

- `agent_application_status`
- `agent_document_check`
- `agent_offer_letters`
- `agent_interview_scheduling`

Uniformity coverage:

- **Uniform agents** (high same-path share): `agent_application_status`, `agent_offer_letters`
- **Non-uniform agents** (mixed paths): `agent_document_check`, `agent_interview_scheduling`
