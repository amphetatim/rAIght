# Data model

> 📝 **Draft** – a starting point derived from the concept. Field names and types are confirmed by the backend and data owners before the first implementation PR.

Terms follow the [glossary](../concept/09-glossary.md).

## Entities

### Agent (agent inventory)

| Field | Type | Note |
|---|---|---|
| `id` | string | rAIght's own ID |
| `name` | string | e.g. "Interview scheduling agent" |
| `provider` | enum | `copilot_studio`, `power_automate`, `openai`, `n8n` ([ADR 0005](../decisions/0005-scope-external-agents.md)) |
| `provider_agent_id` | string | The agent's/flow's ID in the provider |
| `owner` | string | Process owner (mock name) |
| `purpose` | string | One line |
| `ladder_step` | enum | `rule`, `workflow`, `classic_ml`, `genai_call`, `agent`, `multi_agent` |
| `agent_reason` | string, optional | One-line reason when `ladder_step` is `agent` or `multi_agent` |
| `status` | enum | `active`, `retired` |
| `created_at` | datetime | |

### Run log

One record per run of an automation, **normalised**: every source adapter converts its provider's log format into this schema, so metrics never depend on the provider.

| Field | Type | Note |
|---|---|---|
| `id` | string | |
| `agent_id` | string | → Agent |
| `started_at` | datetime | |
| `tokens_in` | integer | |
| `tokens_out` | integer | |
| `steps` | list of Step | Ordered tool calls – the *path* |
| `outcome` | enum | `success`, `escalated`, `failed` |

### Step

| Field | Type | Note |
|---|---|---|
| `order` | integer | Position in the path |
| `tool` | string | e.g. `read_application`, `send_email` |

## Derived metrics (not stored, or cached)

| Metric | Definition |
|---|---|
| `total_tokens` | Σ (`tokens_in` + `tokens_out`) per agent and period |
| `same_path_share` | Share of an agent's runs whose `steps` sequence equals the most frequent sequence |
| `uniform_agent` | `same_path_share` ≥ threshold (config, e.g. 0.8) over at least *n* runs |
| `unused_agent` | No runs within the configured period |

## Example run log (JSON)

```json
{
  "id": "run_0001",
  "agent_id": "agent_interview_scheduling",
  "started_at": "2026-10-20T09:15:00Z",
  "tokens_in": 1840,
  "tokens_out": 420,
  "steps": [
    { "order": 1, "tool": "read_request" },
    { "order": 2, "tool": "check_calendar" },
    { "order": 3, "tool": "send_invite" }
  ],
  "outcome": "success"
}
```
