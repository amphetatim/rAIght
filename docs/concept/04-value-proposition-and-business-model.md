# 4 · Value proposition & business model

rAIght starts as an **internal tool**: the SAP CIO office commissioned it from a taskforce; the users are process owners. Once proven, it becomes a product (see *Phase 2*).

> **The CIO office can automate more without increasing emissions – and spends less on AI.**

## Value proposition canvas (customer: CIO office)

| Customer profile | | Value map | |
|---|---|---|---|
| **Jobs** | Let employees automate with AI · control token and licence costs · keep SAP on its net zero path · govern shadow AI | **Products & services** | rAIght training · dashboard · guided conversion |
| **Pains** | Agent sprawl across external tools nobody reviews · token costs and emissions grow with every agent · no visibility per automation or provider | **Pain relievers** | Every agent visible with its usage · uniform agents flagged and converted · unused agents retired |
| **Gains** | Same or better service level · measurable progress to net zero · lower running cost | **Gain creators** | Process owners choose lean themselves, so it scales without a central team · savings visible per unit · AI budget freed for high-value use cases |

## Business model canvas

| Block | Content |
|---|---|
| **Customer segments** | Customer: CIO office · Users: process owners · Stakeholder: sustainability office |
| **Value proposition** | Autonomy without emission growth – *Not more AI, but rAIght.* |
| **Channels** | Connected to the tools process owners already use (Copilot Studio, Power Automate, OpenAI, n8n) · training · pilot in HR recruiting, then unit by unit |
| **Customer relationships** | Self-service · community of practice for process owners · recognition for lean teams |
| **Key activities** | Train process owners · run the dashboard · curate workflow templates · allocate and track carbon budgets · report savings |
| **Key resources** | Ladder & triage · dashboard on existing provider logs · one adapter per provider · template store · carbon accounting per run |
| **Key partners** | AI tool owners / IT (provider admin access, logs) · L&D · sustainability office · works council & data protection · providers and hyperscalers (energy data) |
| **Cost structure** | Training · dashboard build · **process owners' time** for conversions · change management |
| **Value captured** *(instead of revenue)* | Lower compute cost and emissions · less maintenance · AI budget freed for use cases that really need an agent |

*Revenue streams* in phase 1 are read as **value captured inside SAP**: lower token and licence costs, lower emissions. Phase 2 adds real revenue.

## Carbon budget and the rebound effect

A carbon budget per business unit guards against the **rebound effect**, where cheaper AI simply leads to more AI. It caps total emissions, so efficiency gains turn into absolute savings.

| | Before | After, no cap | After, with budget |
|---|---|---|---|
| Emissions per task | 10 g | 4 g | 4 g |
| Tasks automated | 1,000 | 3,000 | 1,500 |
| **Total** | **10 kg** | **12 kg** | **6 kg** |

*Illustrative numbers.* The budget also gives process owners a reason to convert: freed budget can be reinvested in use cases that really need an agent. It complements an **internal carbon price** on AI compute: the budget caps the total, the price steers individual decisions.

## Ideas from Exercise 4 (team vote)

1. Absolute carbon budget per business unit – 5 votes
2. Internal carbon price on AI compute – 3 votes
3. Pre-approved template store – 2 votes
4. Small-model-first default – team pick

## Phase 2 – from internal tool to SAP offering (outside the IS 613 build)

Once proven internally ("customer zero"), rAIght is **migrated into the SAP stack** (e.g. running on SAP BTP, with SAP's own agents as an additional source) and offered to **SAP customers as a service**, alongside SAP's sustainability products ([ADR 0005](../decisions/0005-scope-external-agents.md)).

- **Opportunity:** benchmarks no one else can provide, because SAP combines AI usage with business process context (with customer consent, aggregated and anonymised).
- **Tension:** cannibalisation of AI consumption revenue. Counter-argument: transparency builds trust and adoption.
- **Open check:** whether customer AI workloads on SAP's cloud count towards SAP's own value-chain emissions. If so, selling rAIght helps SAP reach net zero.
