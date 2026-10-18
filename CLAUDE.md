# rAIght – project context for Claude

> **Not more AI, but rAIght.** rAIght helps SAP process owners build every automation on the lowest step of the automation ladder that does the job, and turn agents that keep repeating themselves into workflows themselves.

Team **Scrumsterz**, University of Mannheim. IS 615 = concept (done), IS 613 = implementation (this repo's `app/`).

## The product in short

- **Persona:** Lena, Recruiting Operations Lead at SAP HR. She builds her own automations; there is **no AI developer in the loop** ([ADR 0001](docs/decisions/0001-process-owner-owns-the-lifecycle.md)).
- **Parts:** Learn (ladder + triage training) → Build (Lena applies triage, notes an *agent reason*) → Monitor (dashboard on run logs) → Convert (uniform agents → workflows).
- **Monitoring uses plain statistics on run logs, never AI** ([ADR 0002](docs/decisions/0002-no-ai-to-check-ai.md)). Don't add model calls to the metrics.
- **Demo-first** ([ADR 0004](docs/decisions/0004-demo-first-scope.md)): we build a demo, not a production system. External SAP systems are **named but mocked** via one adapter layer; APIs are defined but implemented only as far as the demo needs; no auth, real persistence, scaling or production hardening. **Metrics are computed for real** on mock data. The [demo script](docs/technical/demo-script.md) is the scope boundary: **don't build what it doesn't show**.
- **Current scope: Release 1 (walking skeleton)** – see [user story map](docs/concept/06-user-story-map.md). Don't build R2/R3 features unless the issue says so.
- Use the terms from the [glossary](docs/concept/09-glossary.md) in code, UI and docs (e.g. `same_path_share`, `agent_reason`, `uniform agent`).

## Tech stack

**Not decided yet** (see [app/README.md](app/README.md)). Until an ADR for the stack is accepted, do not add a framework, package manager or dependency to `app/`. Once decided, fill in:

| Part | Choice |
|---|---|
| Frontend | _TBD_ |
| Backend | _TBD_ |
| Analysis / mock data | _TBD_ (Python if needed – reference: Kyoungmi) |
| Tests / lint / format | _TBD_ |

## Commands

_TBD once the stack is decided_ – install, run, test, lint, format.

## Where things are

| Path | What | Read when |
|---|---|---|
| `app/` | Implementation – has its own `CLAUDE.md` | Working on code |
| `docs/concept/` | Concept from IS 615 (source of truth for *what* we build) | Unsure about a feature's intent |
| `docs/technical/` | Architecture, data model, API, coding conventions, **demo script** | Before changing structure, data or endpoints; demo script when unsure if something is in scope |
| `docs/decisions/` | ADRs | Before reopening a settled question |
| `docs/handbook/` | **Human documentation only** – see rule below | Only when updating it, or when explicitly asked |
| `TEAM.md`, `CONTRIBUTING.md` | Roles, ways of working, git rules | Questions about who/how |

## Rules for Claude

### 1. Structural changes need explicit confirmation

These files are **structural**. Before creating, editing, moving or deleting any of them – with any tool, including Bash – **stop and tell the user**: "This is a structural change to the project", which file, what changes and why. Then **wait for an explicit yes**. A hook (`.claude/hooks/protect-structure.sh`) also asks for confirmation, but don't rely on it.

- every `CLAUDE.md`, and everything in `.claude/`
- `docs/technical/**`, `docs/decisions/**`, `docs/concept/**`
- `.github/**`, `TEAM.md`, `CONTRIBUTING.md`, `README.md`, `.gitignore`
- dependency and build config: `package.json`, lockfiles, `pyproject.toml`, `requirements*.txt`, `Dockerfile`, `docker-compose*.yml`

Never edit these files via Bash (`sed -i`, `>`, `tee`, `mv`, `rm`) to get around the confirmation.

### 2. Keep the handbook in sync – but don't read it otherwise

`docs/handbook/` explains our setup for humans. **Don't read it** for normal tasks. But when a confirmed structural change affects something the handbook describes, **update the matching handbook page in the same change** and tell the user you did. The mapping is in the table at the top of [docs/handbook/README.md](docs/handbook/README.md) – reading that table is allowed whenever you make a structural change.

### 3. How to work on a task

1. Start from an issue. If there is none, ask for one or for the acceptance criteria.
2. Work on the issue's branch (`feature/12-short-name`), **never on `main`**.
3. For anything larger than a small, single-file change: propose a short plan first and wait for OK.
4. Stay inside the issue's scope. Ask before touching unrelated files.
5. Follow [docs/technical/conventions.md](docs/technical/conventions.md).
6. Run tests and lint before saying "done". Say clearly if something could not be tested.
7. If behaviour, data model or API changed, update `docs/technical/` (structural → confirm first).

### 4. Never

- commit secrets, `.env` files, personal data, or course material (slides, exams – copyrighted, partly *SAP internal*)
- push to `main`, force-push, or rewrite shared history
- add dependencies without saying so and giving a reason
- present code as tested when it wasn't

Personal notes go in `CLAUDE.local.md` (git-ignored).
