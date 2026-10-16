# Team Scrumsterz – rAIght

> **Not more AI, but rAIght.**
> rAIght gives process owners the know-how and the visibility to build every automation on the lowest step that does the job – and to turn repetitive agents into workflows themselves.

This file is the single source of truth for **who does what**. Changes to roles go through a pull request.

## Team

### Business & Pitch

| Name | GitHub | Role | Responsibilities |
|---|---|---|---|
| Luisa | [@lulu122002](https://github.com/lulu122002) | **Product Owner** | Prioritised backlog, user stories and acceptance criteria, sprint reviews, final scope decisions |
| Julian | [@22jj02](https://github.com/22jj02) | **Business Case** (lead) → later **Pitch & Content** | Value proposition, CO₂ and cost savings model (tokens → energy → CO₂ → €), pricing and incentives for the CIO office, assumptions and risks. Once the business case is done: supports Tinja with the pitch deck and video |
| Tinja | [@tinjanyberg](https://github.com/tinjanyberg) | **Pitch & Content** (lead) | Early on: supports Julian (research, numbers) and drafts the training content (ladder and triage examples). Later: leads the pitch deck and pitch video |

### Tech

| Name | GitHub | Role | Responsibilities |
|---|---|---|---|
| Tim | [@amphetatim](https://github.com/amphetatim) | **Tech Lead + Scrum Master** (repo owner) | Architecture, sprint board and ceremonies, integration, CI/deployment setup; owner-only repo settings (branch protection, collaborators); main contact for the PO |
| Wenxuan | [@Venson101](https://github.com/Venson101) | **Frontend / UX + Repo Structure** | Wireframes, user flow, triage page, decision-note form, training module UI. Responsible for repo structure: folder layout, labels, CODEOWNERS, issue/PR templates, PR hygiene |
| Ali | [@aluschek](https://github.com/aluschek) | **Frontend** (lead) | rAIght dashboard (usage per agent, flagged agents, retire action), frontend structure |
| Ebubekir | [@ebu2000](https://github.com/ebu2000) | **Backend** | API and data model (agents, runs, decision notes), endpoints for the dashboard |
| Ivan | [@Ivangb-626](https://github.com/Ivangb-626) | **Backend** | Run-log ingestion and storage, token metrics per agent, retire/status logic |
| Kyoungmi | [@KyoungmiKwon](https://github.com/KyoungmiKwon) | **Data / Analysis** | Mock run-log generator, same-path detection (agents that behave like workflows), demo data. Python reference if Python is used |

### Pairs

- **Frontend:** Ali + Wenxuan (Wenxuan designs, Ali leads the implementation, both build)
- **Backend:** Ebubekir (API / data model) + Ivan (logs / metrics)
- **Data:** Kyoungmi works closely with Ivan (analysis runs on his log data)
- **Business:** Julian + Tinja

## Shared responsibilities

| Task | Owner |
|---|---|
| Tests | Every developer writes tests for their own code |
| Code review | Every PR needs 1 approval, ideally from the other sub-team (frontend ↔ backend), rotating |
| CI / deployment | Set up by Tim; everyone keeps their own part green |
| Demo data | Kyoungmi |
| Demo environment and screen recording for the video | Whole tech team in the final sprint, coordinated by Tim, delivered to Tinja |
| Bug bash before the pitch | Everyone, final sprint |

## Interfaces

| Interface | Between | When |
|---|---|---|
| User stories and priorities | Luisa ↔ Tim | Every sprint planning |
| User flow and wireframes | Luisa ↔ Wenxuan | Sprint 1 |
| Savings formula → metrics | Julian ↔ Kyoungmi / Ivan | Early (shapes the data model) |
| Training content → UI | Tinja ↔ Wenxuan | Sprint 1–2 |
| Demo recording → video | Tech team ↔ Tinja | Final sprint |

## Ways of working

- **Sprint length:** 1 week *(to be confirmed)*
- **Weekly sync:** all 9, 30 min – sprint review + planning *(day/time TBD)*
- **Board:** GitHub Projects – *Backlog → Sprint → In progress → Review → Done*. Every task (technical or not) is an issue on the board with an owner.
- **Labels:** `user-story`, `task`, `bug`, `frontend`, `backend`, `data`, `business`, `pitch`, `training`, `structure`
- **Files that don't belong in Git** (Excel business case, pitch deck, video): OneDrive/Teams – link them in the related issue. *(Folder link TBD)*
- **Decisions** made in chat are written into the related issue, this file or an ADR.
- **Git workflow, PRs and Definition of Done:** see [CONTRIBUTING.md](CONTRIBUTING.md).
- **Why we set it up this way:** see the [team handbook](docs/handbook/README.md).
