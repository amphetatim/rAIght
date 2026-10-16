# 01 – Team and roles

The authoritative list of people, roles and GitHub handles is [`TEAM.md`](../../TEAM.md). This page explains the reasoning.

## Why this split

We're 9 people: 3 who prefer non-technical work (Luisa, Julian, Tinja) and 6 who are comfortable coding.

| Decision | Reason |
|---|---|
| **Luisa as Product Owner** | The PO decides *what* gets built; developers decide *how*. A non-technical PO works well and keeps the business side connected to the product |
| **Julian → business case, then pitch** | The business case is needed early (it shapes which metrics we show). Once it's done, Julian has capacity and joins Tinja on pitch and content |
| **Tinja → content early, pitch later** | Pitch and video need a working product, so they come at the end. Until then Tinja supports Julian and writes the training content (ladder and triage examples) |
| **Tim as Tech Lead + Scrum Master** | One person holds the overview of architecture and sprint, and is the PO's contact |
| **Wenxuan responsible for repo structure** | Has GitHub experience. Tim stays repo owner (see [04](04-git-and-github.md) for why) |
| **Pairs (Ali + Wenxuan, Ebubekir + Ivan, Kyoungmi + Ivan)** | No single point of failure; review partner built in |
| **No dedicated DevOps/QA person** | Tests, reviews and the demo are shared – everyone tests their own code, reviews rotate |

## Where we keep what

| Content | Tool | Why |
|---|---|---|
| Roles, ways of working | GitHub: `TEAM.md`, `CONTRIBUTING.md` | Versioned, next to the code |
| All tasks, technical and non-technical | GitHub Projects board + Issues | One board for all 9; issues link to the PRs that close them. No Git knowledge needed – it's a Kanban board in the browser |
| User stories | GitHub Issues (template *User story*), milestones R1–R3 | PO prioritises on the board |
| Business case calculations | Excel (OneDrive) | Spreadsheet work; Git can't merge Excel |
| Pitch deck, video, drafts | OneDrive/Teams | Binary files – co-editing works there, not in Git. Link them from the related issue |
| Quick chat | WhatsApp/Teams | Decisions then go into an issue or a doc |

**Why not Excel for tasks:** a second task list drifts from GitHub within a sprint and has no link to code.

## Interfaces between the groups

See the table in [`TEAM.md`](../../TEAM.md#interfaces). The most time-critical one: **Julian's savings formula → Kyoungmi/Ivan's metrics**, because it shapes the data model.

_Last updated: 2026-10-16_
