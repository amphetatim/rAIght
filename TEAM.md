# Team Scrumsterz – rAIght

> **Not more AI, but rAIght.**
> rAIght gives process owners the know-how and the visibility to build every automation on the lowest step that does the job – and to turn repetitive agents into workflows themselves.

This file is the single source of truth for **who does what**. Changes to roles go through a pull request.

## Team

### Product

| Name | GitHub | Role | Responsibilities |
|---|---|---|---|
| Tim | [@amphetatim](https://github.com/amphetatim) | **Product Owner** (repo owner) | Decides *what* we build and in which order: prioritised backlog, user stories and acceptance criteria, demo script (with Wenxuan), weekly sync, final scope decisions. Owner-only repo settings (branch protection, collaborators, board access) |

### Business & Pitch

| Name | GitHub | Role | Responsibilities |
|---|---|---|---|
| Julian | [@22jj02](https://github.com/22jj02) | **Business Case** (lead) → later **Pitch & Content** | Value proposition, CO₂ and cost savings model (tokens → energy → CO₂ → €), pricing and incentives for the CIO office, assumptions and risks. Once the business case is done: supports Tinja with the pitch deck and video |
| Tinja | [@tinjanyberg](https://github.com/tinjanyberg) | **Pitch & Content** (lead) | Early on: supports Julian (research, numbers) and drafts the training content (ladder and triage examples). Later: leads the pitch deck and pitch video |

### Tech

| Name | GitHub | Role | Responsibilities |
|---|---|---|---|
| Wenxuan | [@Venson101](https://github.com/Venson101) | **Tech Lead** (with Ebubekir) + **Frontend / UX** + **Repo structure** | Tech Lead for the frontend side and the repo: architecture decisions with Ebubekir, reviews of structural PRs, project setup/CI. Wireframes and user flow; demo pages **P0 shell** and **P1 start page**. Repo structure: folder layout, labels, CODEOWNERS, templates, PR hygiene |
| Ali | [@aluschek](https://github.com/aluschek) | **Frontend** (lead) | Demo pages **P5 dashboard** and **P6 agent detail** (with Ivan) |
| Ebubekir | [@ebu2000](https://github.com/ebu2000) | **Tech Lead** (with Wenxuan) + **Backend** | Tech Lead for the backend/data side: leads the stack decision (#18) with Wenxuan, keeps the sample data consistent, reviews PRs touching structure/data, makes sure `main` runs end to end. Sample data **D1** (with Kyoungmi), demo pages **P3 plan/triage** and **P7 escalations** |
| Ivan | [@Ivangb-626](https://github.com/Ivangb-626) | **Frontend / data** | Demo pages **P4 inventory** and **P6 agent detail** (with Ali) |
| Kyoungmi | [@KyoungmiKwon](https://github.com/KyoungmiKwon) | **Data** | Sample data **D1** (with Ebubekir), demo page **P2 learn** |

### Tech Leads

Ebubekir and Wenxuan share the role: **Ebubekir** covers backend, data model and API; **Wenxuan** covers frontend, repo structure and CI. Decisions that affect both sides (stack, architecture) they take together and record as an ADR. Either can approve a structural PR.

### Pairs

- **Frontend:** Ali + Wenxuan (Wenxuan designs, Ali leads the implementation, both build)
- **Data:** Kyoungmi + Ebubekir (sample data D1)
- **Dashboard + detail:** Ali + Ivan (P5, P6)
- **Business:** Julian + Tinja

## Shared responsibilities

| Task | Owner |
|---|---|
| Checks | Every developer clicks through their part of the demo script before merging |
| Code review | Every PR needs 1 approval, ideally from the other sub-team (frontend ↔ backend), rotating |
| CI / deployment | Set up by the Tech Leads (Wenxuan); everyone keeps their own part green |
| Sample data | Kyoungmi, Ebubekir (D1) |
| Demo environment and screen recording for the video | Whole tech team in the final sprint, coordinated by the Tech Leads, delivered to Tinja |
| Bug bash before the pitch | Everyone, final sprint |

## Interfaces

| Interface | Between | When |
|---|---|---|
| User stories and priorities | Tim (PO) ↔ Tech Leads | Weekly sync |
| User flow, wireframes, demo script | Tim (PO) ↔ Wenxuan | Sprint 1 |
| Technical feasibility of scope | Tech Leads → Tim (PO) | When a story is unclear or too big |
| Savings figures → sample data | Julian ↔ Kyoungmi / Ebubekir | Week 1 (numbers must fit the business case) |
| Training content → UI | Tinja ↔ Wenxuan | Sprint 1–2 |
| Demo recording → video | Tech team ↔ Tinja | Final sprint |

## Ways of working

- **No Scrum Master.** The developers organise themselves on the board; the PO runs the weekly sync.
- **Weekly sync:** all 8, 30 min, run by Tim *(day/time TBD)*. Agenda: what's done (demo) → priorities for next week → blockers.
- **Board:** GitHub Projects (repo → *Projects*) – *Backlog → Ready → In progress → In review → Done*. Every task, technical or not, is an issue on the board with an owner.
- **Board rules:**
  1. Pick from *Ready* only, top first (the PO keeps it ordered); assign yourself before you start.
  2. Max. 2 items *In progress* per person.
  3. Blocked? Comment on the issue and mention the person you need.
  4. *Done* only when the PR is merged.
- **Labels:** `user-story`, `task`, `bug`, `frontend`, `backend`, `data`, `business`, `pitch`, `training`, `structure`
- **Files that don't belong in Git** (Excel business case, pitch deck, video): OneDrive/Teams – link them in the related issue. *(Folder link TBD)*
- **Decisions** made in chat are written into the related issue, this file or an ADR.
- **Git workflow, PRs and Definition of Done:** see [CONTRIBUTING.md](CONTRIBUTING.md).
- **Why we set it up this way:** see the [team handbook](docs/handbook/README.md).
