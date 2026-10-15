# 9 · Glossary (ubiquitous language)

Use these terms consistently – in docs, issues, code and the UI.

| Term | Meaning |
|---|---|
| **Process owner** | Person in a business unit who builds, runs and is accountable for her own automations. The only actor across the rAIght lifecycle. |
| **Automation ladder** | Rule → workflow → classic ML → single GenAI call → agent → multi-agent. Use the lowest step that does the job. |
| **Ladder step** | One level of the automation ladder. |
| **Triage** | Short decision tree the process owner learns in training and applies herself while building. Its result is the ladder step. |
| **Agent reason** | One-line justification recorded when the process owner chooses an agent. |
| **Agent inventory** | Register of all automations and agents with owner and purpose, including those built before rAIght. The basis for monitoring. |
| **Run log** | Record of one run of an automation: tokens, steps (tool calls), output. |
| **Same-path share** | Share of an agent's runs that took an identical sequence of steps. Simple statistics on run logs. |
| **Output / path similarity** | How alike an agent's replies (output) or its tool-call sequences (path) are across runs. |
| **Uniform agent** | An agent whose runs have become near-identical: it behaves like a workflow but costs like an agent. |
| **Unused agent** | An agent without runs for a defined period. |
| **Escalation** | Handing a request the automation cannot solve reliably to a human. |
| **Conversion** | Turning the frequent paths of a uniform agent into a workflow. Done by the process owner. |
| **Guided conversion** | rAIght's support for conversion: a draft workflow generated from the agent's frequent paths. |
| **Exception scope** | The cases an agent still handles after conversion. |
| **Pivotal event** | An event where responsibility passes from one bounded context to the next. |
| **Carbon budget** | Annual cap on AI-related emissions (or compute as a proxy) per business unit. Prevents the rebound effect. |
| **Rebound effect** | Efficiency gains leading to more usage, so total consumption falls less than expected or rises. |
