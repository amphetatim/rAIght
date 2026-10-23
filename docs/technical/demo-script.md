# Demo script

> 📝 **Skeleton – owned by Tim (PO), with Wenxuan (UX).** This is the **scope boundary** for the build ([ADR 0004](../decisions/0004-demo-first-scope.md)): what isn't in this script isn't built. Every step names the issue that delivers it.

**Story:** Lena, Recruiting Operations Lead at SAP HR, learns when an agent is really needed, builds an automation with the triage, and later finds out that some of her agents behave like workflows.

**Target length:** about 3–4 minutes (fits the pitch video).

## Steps

| # | What Lena does | What the audience sees | Real / mocked | Issue |
|---|---|---|---|---|
| 1 | Opens rAIght, starts the ladder module | Automation ladder with recruiting examples | Static content | #1 |
| 2 | Opens the triage cheat sheet | Triage questions on one page | Static content | #2 |
| 3 | Plans a new automation, answers the triage | Triage result: ladder step; if *agent* → one-line agent reason | Real UI logic, saved in memory/fixture | #3 |
| 4 | *(time passes)* Agents have been running | "Run logs imported from agent platform" | Mocked adapter, fixture run logs | #4, #19 |
| 5 | Opens the dashboard | Per agent: tokens/month, same-path share, suggestion | **Metrics computed for real** on fixtures | #6, #7 |
| 6 | Sees "Application status – 94 % same path – Convert to workflow" | Uniform agent flagged | Real calculation, threshold from config | #7 |
| 7 | Sees an unused agent, retires it | Agent status → retired, disappears from usage | Real UI state change, mocked persistence | #8 |
| 8 | *(optional)* An unknown case is escalated to her | Escalation entry in her list | Mocked event | #5 |

## Demo data requirements (for #19)

The fixtures must make the story work:

- **Application status**: about 94 % same path → flagged *uniform* → "Convert to workflow"
- **Document check**: about 91 % → "Replace with rule"
- **Offer letters**: about 88 % → "Use template"
- **Interview scheduling**: about 52 % → "Keep agent for complex panels"
- **One unused agent** (no runs in the last 90 days) for step 7. *Open: which one? The concept has only the four above; propose a fifth, e.g. a reference-check reminder.*

Values follow the illustrative table in [03-solution.md](../concept/03-solution.md).

## Named (simulated) systems

Shown in the UI and the architecture slide, always served by mock adapters:

| System | Role in the story |
|---|---|
| SAP agent platform (e.g. Joule Studio / SAP Build) | Where Lena's agents run; source of run logs |
| SAP AI Core | Token usage per call |
| SAP SuccessFactors Recruiting | The HR process the agents automate |

_Names are to be confirmed by the team; they're for credibility, not integration._

## Out of the demo

Login, roles, real persistence, guided conversion (R2), carbon budget (R3), agent inventory for pre-existing agents (H3), data-protection handling (H6).
