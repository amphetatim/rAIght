# rAIght

> **Not more AI, but rAIght.**
> A toolkit that helps SAP process owners build every automation on the lowest step that does the job – and turn agents that keep repeating themselves into lean workflows on their own.

Team project by **Scrumsterz** – University of Mannheim, IS 615 *Enterprise Cloud Design & Development* (concept) and IS 613 (implementation).

---

## The idea in 30 seconds

SAP wants to become an **Autonomous Enterprise** and, at the same time, cut its value-chain emissions by at least 90% by 2030. Every AI agent plans, calls tools and retries, so it needs far more compute than a fixed workflow. Process owners build their own automations and tend to reach for an agent by default – nobody checks whether it still needs to be one.

rAIght gives the process owner three things:

| Part | What it does |
|---|---|
| **Learn** | Training on the *automation ladder* (rule → workflow → classic ML → GenAI call → agent → multi-agent) and a short *triage* the process owner applies herself |
| **Monitor** | A dashboard on existing run logs: token usage per agent and how often an agent takes the same path |
| **Convert** | Guided conversion: a draft workflow built from an agent's most frequent paths. The agent keeps only the exceptions. Unused agents are retired. |

**The process owner owns the whole lifecycle.** There is no separate AI developer in the loop (see [ADR 0001](docs/decisions/0001-process-owner-owns-the-lifecycle.md)).

## Repository structure

```
rAIght/
├── README.md                  ← you are here
├── CONTRIBUTING.md            ← how we work together (branches, PRs, issues)
├── app/                       ← implementation (IS 613) – stack not decided yet
├── docs/
│   ├── concept/               ← the full concept from IS 615, as Markdown
│   ├── decisions/             ← architecture & design decision records (ADRs)
│   ├── presentations/         ← our decks (.pptx) – see its README for which are current
│   └── eventstorming-board/   ← interactive EventStorming board (HTML, partly outdated)
└── .github/                   ← issue and pull request templates
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
- [ ] Team organisation and roles for IS 613
- [ ] Technology stack decided ([app/README.md](app/README.md))
- [ ] Release 1 (walking skeleton) – see the **R1** milestone in Issues

## Getting started as a team member

1. Accept the collaborator invitation for this repository.
2. Read this README, [CONTRIBUTING.md](CONTRIBUTING.md) and the [user story map](docs/concept/06-user-story-map.md).
3. Pick an issue from the current milestone, assign yourself, and work on a branch.

## Note on course material

Lecture slides, exams and other course material are **not** stored here: several are marked *SAP internal* and all are copyrighted. Keep this repository **private**.
