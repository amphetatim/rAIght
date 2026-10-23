# 8 · Hotspots, assumptions & risks

## Hotspots (open questions)

| ID | Context | Question | Suggested next step |
|---|---|---|---|
| H1 | Enablement | Is the training mandatory for every process owner, or only for those who build agents? | Short module for all, full training before building an agent |
| H2 | Design & Build | Is self-applied triage enough without a check? | Dashboard as the check after the fact; optional peer review for agents |
| H3 | Design & Build | How do agents built in external tools get into the inventory? **Central since [ADR 0005](../decisions/0005-scope-external-agents.md)** | See [agent inventory options](#h3-agent-inventory-options); demo: mocked import from all providers |
| H4 | Monitoring | Similar text is not the same as similar steps – which similarity counts? | Test both on pilot logs; use path similarity as primary signal |
| H5 | Monitoring | Tokens are not energy: providers give no reliable emissions per token | Use tokens as a proxy; request energy data from hyperscalers |
| H6 | Monitoring | Logs may hold personal data (GDPR) and allow conclusions about employees (works council, § 87 BetrVG) | Pseudonymise logs; involve data protection and works council before the pilot |
| H7 | Conversion | Do process owners have the time and skills to convert? | Guided conversion; carbon budget as incentive |
| H8 | Monitoring | How much step-level data (tokens, tool-call sequence) do Copilot Studio, Power Automate, OpenAI and n8n expose? | Short spike by the Tech Leads; the demo stays mocked |

## H3: agent inventory options

| Option | Catches | Misses | Effort |
|---|---|---|---|
| Admin export per provider (Copilot Studio, Power Automate, OpenAI org, n8n) | Everything built in company tenants | Private accounts | Low |
| LLM gateway / API usage grouped by key or app | Most agents calling an LLM | Private keys, external tools | Low |
| Cloud / AI billing per cost centre | Where to look | Which agent exactly | Low |
| Technical users and service accounts | Agents acting in SAP systems | Text-only agents | Medium |
| Self-registration campaign (with amnesty) | Owner and purpose | Forgotten agents | Medium |
| Existing compliance inventories (e.g. EU AI Act) | Documented systems | Low-risk agents | Low |
| Network monitoring of AI endpoints | True shadow AI | Attribution; works council issue | High |

**Recommendation:** provider exports + gateway data, cross-checked with billing; owners confirm a pre-filled registration; from then on **no AI gateway access without registration**.

## Assumptions & risks

| Assumption / risk | How rAIght handles it |
|---|---|
| Lena applies the triage correctly on her own | The dashboard shows a wrong choice as a uniform agent |
| Process owners have time to convert | Guided conversion; carbon budgets give a reason |
| Provider run logs contain tokens and steps | Check per provider (H8); tokens as a proxy for energy |
| Logs may contain personal data | Pseudonymisation; data protection and works council involved early |
| Cheaper AI leads to more AI (rebound effect) | Carbon budget per business unit caps total use |
| Efficiency KPIs get gamed (Goodhart's law) | Always pair efficiency KPIs with value KPIs (task success, time saved) |
| Strict rules slow down innovation | Innovation sandbox with a fixed budget |
