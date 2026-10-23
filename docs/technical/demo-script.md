# Demo script

> 📝 **Owned by Tim (PO), with Wenxuan (UX).** This is the **scope boundary** for the build ([ADR 0006](../decisions/0006-pure-clickable-demo.md) – pure clickable demo, deadline 20 Nov 2026): what isn't in this script isn't built. Every step names the **page** that delivers it.

**Story:** SAP's CIO office asked a taskforce to cut token costs and CO₂ of employee-built AI automations. Lena, Recruiting Operations Lead at SAP HR, builds hers with Copilot Studio, Power Automate, OpenAI and n8n. With rAIght she learns when an agent is really needed, builds with the triage, sees all her agents across tools in one place, and finds out that some of them behave like workflows ([ADR 0005](../decisions/0005-scope-external-agents.md)).

**Target length:** about 3–4 minutes (fits the pitch video).

## Steps

| # | What Lena does | What the audience sees | Page |
|---|---|---|---|
| 0 | Opens rAIght | Start page: welcome, the four steps, headline numbers | P1 |
| 1 | Starts the ladder module | Automation ladder with recruiting examples | P2 |
| 2 | Opens the triage cheat sheet | Triage questions on one page | P2 |
| 3 | Plans a new automation, answers the triage | Ladder step as result; if *agent* → one-line agent reason | P3 |
| 4 | *(time passes)* Opens her inventory | All her agents from Copilot Studio, Power Automate, OpenAI and n8n in one list | P4 |
| 5 | Opens the dashboard | Summary numbers, "needs your attention", table with provider, tokens, same-path share | P5 |
| 6 | Clicks "Application status – 94 % same path" | Agent detail: paths taken, suggestion "Convert to workflow" | P6 |
| 7 | Opens the unused agent, retires it | Status → retired, numbers on the dashboard drop | P6, P5 |
| 8 | *(optional)* Checks escalations | Cases routed to her | P7 |

All numbers come from the finished sample data ([sample-data.md](sample-data.md), issue D1).

## Demo data requirements (D1)

The fixtures must make the story work:

- **Application status**: about 94 % same path → flagged *uniform* → "Convert to workflow"
- **Document check**: about 91 % → "Replace with rule"
- **Offer letters**: about 88 % → "Use template"
- **Interview scheduling**: about 52 % → "Keep agent for complex panels"
- **One unused agent** (no runs in the last 90 days) for step 7. Proposal: **Reference check reminder** (Copilot Studio), no runs for 124 days.

Values follow the illustrative table in [03-solution.md](../concept/03-solution.md).

## Named (simulated) systems

Shown in the UI and on the architecture slide by name only – no logos, no connections:

| System | Role in the story | Example agent |
|---|---|---|
| Microsoft Copilot Studio | Lena's conversational agents | Application status, Reference check reminder (unused) |
| Power Automate (AI Builder) | Flows with AI steps | Document check |
| OpenAI (Assistants) | Custom assistant via API | Offer letters |
| n8n | Workflow tool with AI nodes | Interview scheduling |
| SAP SuccessFactors Recruiting | The HR process the agents automate (not a source of run logs) | – |

_Provider assignment is a proposal; the team can change it._

## Out of the demo

Backend, API and metric calculation (ADR 0006), chat usage of assistants (ADR 0005), SAP-internal agent platforms (later stage), login, roles, real persistence, guided conversion (R2), carbon budget (R3), agent inventory for pre-existing agents (H3), data-protection handling (H6).
