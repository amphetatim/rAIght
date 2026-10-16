# How we work together

Simple rules so nine people can work in one repository without getting in each other's way. Change them together when they stop helping.

## 1. Work starts with an issue

- Every piece of work has an **issue**: a user story, a task, a spike (research) or a bug.
- **User stories** use the template *"As a process owner, I want … so that …"* and the label `user-story`.
- Releases are **milestones**: `R1 – Walking skeleton`, `R2 – Act`, `R3 – Steer`. They match the [user story map](docs/concept/06-user-story-map.md).
- Assign yourself before you start, so nobody works on the same thing twice.

## 2. Never commit directly to `main`

`main` is always the working, agreed version.

```bash
git checkout main
git pull
git checkout -b feature/12-token-usage-dashboard   # <type>/<issue-number>-<short-name>
# … work, commit …
git push -u origin feature/12-token-usage-dashboard
```

Branch types: `feature/` (new functionality), `fix/` (bug), `docs/` (documentation), `spike/` (experiments you may throw away).

## 3. Commits

Short, in English, imperative, with a [Conventional Commits](https://www.conventionalcommits.org/) prefix: *"feat: add token usage chart (#12)"*, not *"added stuff"*. Prefixes: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`. Details in [docs/technical/conventions.md](docs/technical/conventions.md).

## 4. Pull requests

- Open a **pull request** (PR) into `main` when your work is ready, or earlier as a *draft* if you want feedback.
- Write `Closes #12` in the PR description so the issue closes automatically on merge.
- **At least one other team member reviews** before merging.
- Keep PRs small: one story or task per PR (aim for < ~400 changed lines).
- Squash merge, so give the PR a Conventional Commit title.
- With Claude: run `/pr-ready` before opening the PR.

## 5. Definition of Done

A story is done when:

- [ ] the acceptance criteria in the issue are met
- [ ] someone else reviewed and approved the PR
- [ ] it is merged into `main` and `main` still runs
- [ ] tests are written and pass
- [ ] the docs are updated if behaviour, concept or setup changed

## 6. Decisions

Decisions that affect the whole team (tech stack, data model, scope changes) are written down as a short **ADR** in [`docs/decisions/`](docs/decisions/). Copy the format of an existing one and number it consecutively.

## 7. Coding with Claude

We all use Claude Code with a shared setup in the repo (`CLAUDE.md`, `.claude/`).

- Start an issue with `/start-issue <number>`, finish with `/pr-ready`.
- **You own every line you submit** – read and understand AI-generated code before opening a PR.
- **Structural files** (all `CLAUDE.md`, `.claude/`, `docs/technical|decisions|concept/`, `.github/`, this file, `TEAM.md`, `README.md`, dependency files) need an explicit confirmation before Claude changes them, and a code-owner review.
- Coding rules: [docs/technical/conventions.md](docs/technical/conventions.md). Why it's set up this way: [docs/handbook/](docs/handbook/README.md).

## 8. What does not go in here

- Lecture slides, exams, solutions and other course material (copyright, partly *SAP internal*)
- Passwords, API keys, tokens – use environment variables and a local `.env` file (it is git-ignored)
- Personal data
