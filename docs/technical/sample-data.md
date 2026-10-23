# Sample data

> 📝 **Draft – owned by Kyoungmi and Ebubekir (tech team).** The demo runs only on these files ([ADR 0006](../decisions/0006-pure-clickable-demo.md)). Values are **finished, not calculated** – they are written so the [demo script](demo-script.md) works. Refine the fields here before building pages (issue D1).

All files live in `app/data/`. Use glossary names ([09-glossary.md](../concept/09-glossary.md)).

## `agents.json` – Lena's automations, metrics already filled in

| Field | Type | Example / note |
|---|---|---|
| `id` | string | `app_status` |
| `name` | string | `Application status` |
| `provider` | enum | `copilot_studio`, `power_automate`, `openai`, `n8n` – shown by name, no logos ([ADR 0005](../decisions/0005-scope-external-agents.md)) |
| `owner` | string | `Lena` |
| `purpose` | string | One line |
| `ladder_step` | enum | `rule`, `workflow`, `classic_ml`, `genai_call`, `agent`, `multi_agent` |
| `agent_reason` | string | One-line reason why it's an agent |
| `status` | enum | `active`, `unused`, `retired` (retired only via the button in the demo) |
| `runs_30d` | integer | `1129` |
| `tokens_30d` | integer | `2100000` |
| `same_path_share` | number 0–1 | `0.94` |
| `uniform_agent` | boolean | `true` if it acts like a workflow – set by hand, consistent with `same_path_share` (≥ 0.8) |
| `days_since_last_run` | integer | `124` for the unused agent |
| `top_paths` | list | up to 3 × `{ "steps": ["read_request","lookup_status","send_reply"], "share": 0.94 }` |
| `suggestion` | string | `Convert to workflow`, `Replace with rule`, `Use template`, `Keep agent`, `Retire` |
| `suggestion_text` | string | One sentence why |

**The five agents** (values from [03-solution.md](../concept/03-solution.md) and the demo script):

| Agent | Provider | Same path | Suggestion |
|---|---|---|---|
| Application status | Copilot Studio | 94 % | Convert to workflow |
| Document check | Power Automate | 91 % | Replace with rule |
| Offer letters | OpenAI | 88 % | Use template |
| Interview scheduling | n8n | 52 % | Keep agent |
| Reference check reminder | Copilot Studio | – (no runs for 124 days) | Retire |

## `summary.json` – numbers for the start page and dashboard header

Totals must match `agents.json` (sum of tokens and runs, number of uniform and unused agents). Optional: a value per period (7 / 30 / 90 days) if the period switch is shown.

## `escalations.json` (only if P7 is built)

`{ "agent_id", "text", "time" }` – 2–3 entries.

## `content/` – texts

Ladder steps with recruiting examples, triage questions and outcomes, start-page texts. Written by Tinja, reviewed by Tim.

## Rules

- No real names or personal data – Lena is a persona.
- Numbers must be **consistent** across files; the click-through before merging checks this.
- If a page needs a new field, add it here first (structural change → confirm).
