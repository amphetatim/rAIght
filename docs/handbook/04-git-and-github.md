# 04 – Git and GitHub

The day-to-day rules are in [`CONTRIBUTING.md`](../../CONTRIBUTING.md). This page explains the setup behind them.

## Permissions on a personal repo

The repo is owned by Tim's personal account (`amphetatim`). On personal repos GitHub has **no roles** for collaborators (no Admin/Maintain/Triage) – everyone invited gets the same collaborator access. We decided against moving to a GitHub organisation.

| Collaborators can (everyone, incl. Wenxuan) | Only the owner can (Tim) |
|---|---|
| Push branches, open/review/merge PRs | Branch protection / rulesets |
| Create issues, labels, milestones | Add/remove collaborators |
| Edit `CODEOWNERS`, templates, workflows | Repo settings (merge options, visibility, rename/delete) |
| | Secrets for CI/deployment |

**So:** Wenxuan is responsible for repo structure and tells Tim when an owner-only setting needs changing.

## Branches and PRs – why

| Rule | Why |
|---|---|
| Never commit to `main` | `main` is always the working, agreed version – the demo runs from it |
| One issue → one branch → one PR | Easy to review, easy to revert, clear history |
| Small PRs | Reviewers actually read them |
| Squash merge | One clean commit per PR on `main` |
| Conventional Commits | Readable history; type tells you what kind of change it was |

## CODEOWNERS

`.github/CODEOWNERS` maps paths to people. When a PR touches a path, GitHub **requests a review** from its owners automatically. With the ruleset option *"Require review from Code Owners"* their approval becomes **mandatory**.

- Code owners must have write access (all collaborators do).
- The **last matching line wins**.
- `app/frontend/`, `app/backend/`, `app/analysis/` are planned paths – adjust when the stack ADR fixes the layout.

## Protecting `main` ⏳ pending

**Status:** not active yet. On a free personal account, rulesets/branch protection are only enforced on **public** repos; our repo must stay **private** (course material). Tim will enable it after getting **GitHub Pro via the GitHub Student Developer Pack** (free).

**Steps, once Pro is active:**

1. Repo → **Settings** → **Rules** → **Rulesets** → **New ruleset** → **New branch ruleset**
2. Name `protect-main`, Enforcement **Active**, Bypass list **empty**
3. Target branches → **Include default branch**
4. Rules:
   - ✅ Restrict deletions
   - ✅ Require a pull request before merging → 1 approval, ✅ dismiss stale approvals, ✅ require conversation resolution, ✅ **require review from Code Owners**
   - ✅ Block force pushes
   - ☐ Require status checks to pass → turn on once CI exists
5. **Create**
6. Settings → General → Pull Requests: allow **squash merging only**, ✅ automatically delete head branches
7. Test: `git push origin main` from a local change → must be rejected. Then update this section to "✅ active".

**Until then:** the rules hold by agreement, Claude refuses direct pushes to `main` (`.claude/settings.json`), and everyone uses PRs.

## Project board

Created by Tim on 23 Oct 2026 in the repo (repo → *Projects*). It belongs to Tim's account, so **Tim manages access**.

1. Columns: *Backlog → Ready → In progress → In review → Done*
2. Fields: *Release* (R1/R2/R3), *Workstream* (frontend, backend, data, business, pitch), optional *Size* (S/M/L)
3. Settings → **Manage access**: Wenxuan **Admin**, everyone else **Write**
4. Board rules (no Scrum Master – the board replaces the coordination): see *Ways of working* in [`TEAM.md`](../../TEAM.md)

## Labels

`page` (P0–P7), `data` (D1), `pitch`, `business`, `task`, `bug`, plus `pitch-only` for R2/R3 stories that are not built. Milestone: **Demo – 20 Nov** ([ADR 0006](../decisions/0006-pure-clickable-demo.md)).

_Last updated: 2026-10-23_
