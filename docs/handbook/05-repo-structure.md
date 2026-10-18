# 05 – Repo structure

```
rAIght/
├── CLAUDE.md                  # Claude: project context + rules, loaded every session
├── CLAUDE.local.md            # your personal Claude notes (git-ignored)
├── README.md                  # entry point for humans
├── TEAM.md                    # who does what, GitHub handles
├── CONTRIBUTING.md            # how we work: issues, branches, PRs, DoD
├── .claude/
│   ├── settings.json          # shared permissions + hook registration
│   ├── hooks/protect-structure.sh
│   ├── commands/              # /start-issue, /pr-ready, /update-docs
│   └── agents/reviewer.md     # review subagent
├── app/                       # implementation (IS 613)
│   ├── CLAUDE.md              # rules for all code
│   ├── frontend/  (planned)   # + own CLAUDE.md
│   ├── backend/   (planned)   # + own CLAUDE.md
│   └── analysis/  (planned)   # + own CLAUDE.md
├── docs/
│   ├── concept/               # WHAT and WHY – concept from IS 615 (source of truth)
│   ├── technical/             # HOW – architecture, data model, API, conventions, demo script
│   ├── decisions/             # ADRs – decisions that affect the whole team
│   ├── handbook/              # this – explanations for humans, not loaded by Claude
│   ├── presentations/         # decks (.pptx)
│   └── eventstorming-board/   # interactive board (partly outdated)
└── .github/
    ├── CODEOWNERS
    ├── pull_request_template.md
    └── ISSUE_TEMPLATE/        # user story, task/spike, bug
```

## Why it's split this way

| Folder | Audience | Loaded by Claude |
|---|---|---|
| `CLAUDE.md` files | Claude | Automatically (root always, sub-folders when working there) |
| `docs/concept/` | Everyone, esp. PO and business | On demand, when a task needs the *why* |
| `docs/technical/` | Developers + Claude | On demand, before changing code structure, data or API |
| `docs/decisions/` | Everyone | On demand, to avoid reopening settled questions |
| `docs/handbook/` | Humans | No (only the mapping table, during structural changes) |

**Demo script = scope boundary:** we build a demo, not a production system ([ADR 0004](../decisions/0004-demo-first-scope.md)). `docs/technical/demo-script.md` lists exactly what the demo shows; anything not in it isn't built. When a feature request comes up, check it against the script first.

**Concept vs. technical:** `concept/` says what the product must do; `technical/` says how we build it. If they disagree about *what*, the concept wins; change it deliberately (structural change) rather than letting code drift.

## Adding a new folder

A new top-level folder or a new `app/` sub-folder is a structural change: add it here, to the tree in [`README.md`](../../README.md), and – for code folders – a `CLAUDE.md` and a `CODEOWNERS` line.

_Last updated: 2026-10-18_
