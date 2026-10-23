# rAIght

> **Not more AI, but rAIght.**
> A toolkit that helps process owners build every AI automation on the lowest step that does the job – and turn agents that keep repeating themselves into lean workflows on their own.

Team project by **Scrumsterz** – University of Mannheim, IS 615 *Enterprise Cloud Design & Development* (concept) and IS 613 (implementation).

---

## The idea in 30 seconds

SAP employees build more and more AI automations themselves, with external tools like **Copilot Studio, Power Automate, OpenAI and n8n**. Every agent plans, calls tools and retries, so it costs far more tokens – and CO₂ – than a fixed workflow, and nobody checks whether it still needs to be an agent. SAP's **CIO office** asked a taskforce (us) to cut those costs and emissions without slowing adoption. rAIght is the answer: first internal, later migrated into the SAP stack and offered to customers ([ADR 0005](docs/decisions/0005-scope-external-agents.md)).

rAIght gives the process owner three things:

| Part | What it does |
|---|---|
| **Learn** | Training on the *automation ladder* (rule → workflow → classic ML → GenAI call → agent → multi-agent) and a short *triage* the process owner applies herself |
| **Monitor** | A dashboard on existing run logs: token usage per agent and how often an agent takes the same path |
| **Convert** | Guided conversion: a draft workflow built from an agent's most frequent paths. The agent keeps only the exceptions. Unused agents are retired. |

**The process owner owns the whole lifecycle.** There is no separate AI developer in the loop (see [ADR 0001](docs/decisions/0001-process-owner-owns-the-lifecycle.md)).

**Scope of the implementation:** a **pure clickable demo** along a defined [demo script](docs/technical/demo-script.md), frontend only, on finished sample data – deadline 20 Nov 2026 ([ADR 0006](docs/decisions/0006-pure-clickable-demo.md)).

## Repository structure

```
rAIght/
├── README.md                  ← you are here
├── TEAM.md                    ← who does what (roles, GitHub handles)
├── CONTRIBUTING.md            ← how we work together (branches, PRs, issues)
├── CLAUDE.md                  ← shared context for Claude Code (+ .claude/)
├── app/                       ← implementation (IS 613) – stack not decided yet
├── docs/
│   ├── concept/               ← the full concept from IS 615, as Markdown
│   ├── technical/             ← architecture, data model, API, coding conventions
│   ├── decisions/             ← architecture & design decision records (ADRs)
│   ├── handbook/              ← how and why our setup works – read when unclear
│   ├── presentations/         ← our decks (.pptx) – see its README for which are current
│   └── eventstorming-board/   ← interactive EventStorming board (HTML, partly outdated)
└── .github/                   ← issue/PR templates, CODEOWNERS
```

## Concept documents

| # | Document | Content |
|---|---|---|
| 1 | [Problem & thesis](docs/concept/01-problem-and-thesis.md) | The challenge, the tension, the automation ladder |
| 2 | [Persona & point of view](docs/concept/02-persona-and-pov.md) | Lena, PoV, How might we |
| 3 | [Solution](docs/concept/03-solution.md) | Learn → Build → Monitor → Convert, triage, dashboard, guided conversion |
| 4 | [Value proposition & business model](docs/concept/04-value-proposition-and-business-model.md) | VPC, BMC, carbon budget, outlook |
| 5 | [Product vision box](docs/concept/05-product-vision-box.md) | Front, back, who/what/where/when/why |
| 6 | [User story map](docs/concept/06-user-story-map.md) | Backbone, releases R1–R3, all user stories |
| 7 | [EventStorming](docs/concept/07-eventstorming.md) | Corrected Big Picture: bounded contexts, events, pivotal events |
| 8 | [Hotspots, assumptions & risks](docs/concept/08-hotspots-assumptions-risks.md) | Open questions and how we handle them |
| 9 | [Glossary](docs/concept/09-glossary.md) | Ubiquitous language |

## Status

- [x] Concept (IS 615) – done, pitched on 2 Oct 2026
- [x] Team organisation and roles for IS 613 ([TEAM.md](TEAM.md))
- [x] Shared Claude Code setup ([handbook](docs/handbook/02-claude-setup.md))
- [ ] `main` protected (pending GitHub Pro)
- [ ] Technology stack decided ([app/README.md](app/README.md))
- [ ] Clickable demo – pages P0–P7, sample data D1, recording X1 (milestone **Demo – 20 Nov**)

## Getting started as a team member

1. Accept the collaborator invitation for this repository.
2. Read this README, [TEAM.md](TEAM.md), [CONTRIBUTING.md](CONTRIBUTING.md) and the [user story map](docs/concept/06-user-story-map.md).
3. Developers: set up Claude Code as in [handbook 02](docs/handbook/02-claude-setup.md#first-time-setup-per-developer).
4. Pick an issue from the current milestone, assign yourself, and work on a branch.

## Note on course material

Lecture slides, exams and other course material are **not** stored here: several are marked *SAP internal* and all are copyrighted. Keep this repository **private**.
