# 6 · User story map

**Vision:** rAIght gives process owners the know-how and the visibility to build every automation on the lowest step that does the job – and to turn repetitive agents into workflows themselves.

**Persona:** Lena, process owner (see [persona](02-persona-and-pov.md)).

## Backbone

| Usage step | Get started | Plan an automation | Build it | Run it | Review it | Improve it |
|---|---|---|---|---|---|---|
| **Activities** | Learn the ladder · Practise triage | Describe the task · Apply the triage | Build in her tool · Note why an agent | Handle requests · Escalate exceptions | Check the dashboard · Act on flags | Convert to workflow · Retire agent |

## Releases

| Release | Name | Goal |
|---|---|---|
| **R1** | Walking skeleton – *Learn & see* | Covers the whole journey once, in its simplest form. Needs no new data. |
| **R2** | Act – *Convert with help* | Makes the lean option the easy option |
| **R3** | Steer – *Budgets & sharing* | Steering and scaling |
| *Beyond* | *SAP integration & offering* | Migrate into the SAP stack, add SAP agents as a source, offer to customers ([ADR 0005](../decisions/0005-scope-external-agents.md)) |

## User stories

Format: *As Lena (process owner), I want … so that …*

### R1 – Walking skeleton

| ID | Activity | I want … | … so that |
|---|---|---|---|
| R1-01 | Get started | a short ladder module with recruiting cases | I recognise when a workflow is enough |
| R1-02 | Get started / Plan | the triage questions on one page (cheat sheet) | I can apply them without help |
| R1-03 | Build | to note in one line why I chose an agent | I can revisit the choice later |
| R1-04 | Run | every run to be logged automatically (tokens, steps, output) | I can see what my automations do |
| R1-05 | Run | unknown cases to be routed to me | nothing goes wrong silently |
| R1-06 | Review | token usage per agent | I see which agents are expensive |
| R1-07 | Review | the same-path share per agent | I see which agents act like workflows |
| R1-08 | Improve | to retire an unused agent | it stops consuming resources |

### R2 – Act

| ID | Activity | I want … | … so that |
|---|---|---|---|
| R2-01 | Plan | the triage built into the build tool | I don't have to remember it |
| R2-02 | Plan | to find similar existing automations | I can reuse instead of building |
| R2-03 | Build | to start from a workflow template | the lean option is the easy option |
| R2-04 | Review | a nudge when one of my agents is flagged | I don't have to check the dashboard all the time |
| R2-05 | Improve | a draft workflow from my agent's frequent paths | I can convert it without a developer |
| R2-06 | Improve | standard cases routed to the workflow, exceptions to the agent | the agent only does what needs an agent |

### R3 – Steer

| ID | Activity | I want … | … so that |
|---|---|---|---|
| R3-01 | Get started | a refresher built from real conversions | I learn from other teams' cases |
| R3-02 | Review | my usage compared with my unit's carbon budget | my unit stays within budget |
| R3-03 | Improve | to share my conversion as a training case | others learn from it |

All stories also exist as **GitHub issues** with the matching milestone.
