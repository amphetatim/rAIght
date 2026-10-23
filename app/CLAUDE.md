# app/ – implementation context

Loaded automatically when Claude works inside `app/`. Keep it short and specific to the code.

## What we build

A **pure clickable demo**, frontend only ([ADR 0006](../docs/decisions/0006-pure-clickable-demo.md)), deadline 20 Nov 2026. Framework: _TBD by the Tech Leads (#18 → ADR 0007)_ – until then no framework, no dependencies, no scaffolding.

## Planned layout (confirm with ADR 0007)

| Path | Content | Issue |
|---|---|---|
| `app/data/` | Finished sample data (JSON) – see [sample-data.md](../docs/technical/sample-data.md) | D1 |
| `app/` shell | Navigation, layout, design tokens | P0 |
| one folder/file per page | Start · Learn · Plan (triage) · Inventory · Dashboard · Agent detail · Escalations | P1–P7 |

## Rules

- **Build only what the [demo script](../docs/technical/demo-script.md) shows.** If a task isn't in it, ask before building.
- **No backend, no API calls, no external systems.** Pages read `app/data/*.json` directly.
- **Don't calculate metrics.** Show the values from the sample data. If a number looks wrong, fix the data, not the page.
- **State is client-side only** (triage answers, retired agent, filters) and may reset on reload.
- **Providers are shown by name only** (Copilot Studio, Power Automate, OpenAI, n8n) – no logos.
- **All UI follows [design-system.md](../docs/technical/design-system.md)** (derived from the pitch deck; slide 3 is the dashboard reference). Use its tokens, never hard-coded colours, no characters/logos it forbids.
- **Stay inside your page.** Shared parts (shell, tokens, data files) change only via P0/D1 or with the owner's OK.
- Use glossary names in code and UI: `agent_reason`, `same_path_share`, `ladder_step`, `uniform_agent`.
