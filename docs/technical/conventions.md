# Coding conventions

How we write and review code. Applies to everyone – and to Claude. Tool-specific parts (formatter, linter, test runner) are filled in once the stack ADR is accepted.

## 1. Git and pull requests

| Rule | Detail |
|---|---|
| One issue → one branch → one PR | Branch: `<type>/<issue>-<short-name>`, e.g. `feature/12-token-usage-chart`. Types: `feature`, `fix`, `docs`, `spike` |
| Never commit to `main` | Everything goes through a PR with at least 1 approval |
| Small PRs | Aim for **< ~400 changed lines**. Bigger → split. Small PRs get real reviews, big ones get waved through |
| Commit messages | [Conventional Commits](https://www.conventionalcommits.org/): `feat: add token usage chart (#12)`, `fix: …`, `docs: …`, `test: …`, `refactor: …`, `chore: …`. English, imperative |
| Merge | Squash merge; the PR title becomes the commit on `main`, so give it a Conventional Commit title |
| Draft PRs | Open early as draft if you want feedback |

## 2. AI-assisted code (Claude)

- **You are responsible for every line you submit**, whoever typed it. Don't open a PR with code you haven't read and understood – you must be able to explain it in review.
- Let Claude **plan before coding** for anything beyond a small change (use `/start-issue`).
- One task per Claude session. Use `/clear` between unrelated tasks so old context doesn't leak in.
- Ask Claude for tests together with the code, and check that the tests actually test something.
- Run `/pr-ready` before opening a PR – it runs checks and the reviewer subagent.
- Don't accept large, unexplained rewrites. If Claude changes more than the issue needs, ask why or revert.

## 3. Code quality

| Area | Rule |
|---|---|
| Names | Descriptive, in English, glossary terms from [09-glossary.md](../concept/09-glossary.md) (`same_path_share`, not `ratio2`) |
| Functions | Small, one job. If you need "and" to describe it, split it |
| Duplication | Reuse before rewriting. Search the codebase first |
| Dead code | No commented-out code, no unused functions – Git remembers |
| Types | Typed at boundaries (API, data model): TypeScript `strict` / Python type hints |
| Errors | No silent failures. Clear error messages. Validate input at the API boundary |
| Config | No magic numbers for thresholds (e.g. "uniform" share, "unused" period) – put them in one config place |
| Comments | Explain *why*, not *what* |

## 4. Checks

We build a pure clickable demo ([ADR 0006](../decisions/0006-pure-clickable-demo.md)) – there is no logic to unit-test.

- Before merging: **click through the part of the [demo script](demo-script.md)** your PR touches, in the browser.
- Numbers on screen come from `app/data/` and must match across pages.
- No production hardening (auth, retries, load) – out of scope.
- Lint must pass (once set up).

## 5. Formatting and linting

Automated, never discussed in review. _Tools TBD with the stack_ (e.g. Prettier + ESLint for TypeScript, Ruff for Python). Format on save, and run lint before pushing.

## 6. Security and data

- No secrets in the repo. Use `.env` (git-ignored) and commit a `.env.example` with dummy values.
- **Mock data only.** No real names, e-mails or candidate data – even in tests.
- No course material (slides, exams) in the repo.

## 7. Dependencies

A new dependency is a **structural change**: say in the PR which package, why, and why the existing ones don't do it. Prefer well-maintained, widely used packages.

## 8. Docs

- API, data model or architecture changed → update [`docs/technical/`](.) in the same PR.
- Team-wide decision → new ADR in [`docs/decisions/`](../decisions/).
- Setup or workflow changed → update [`docs/handbook/`](../handbook/).
