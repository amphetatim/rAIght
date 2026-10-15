# 1 · Problem & thesis

## The challenge

> *Design the way SAP can become an Autonomous Enterprise while remaining Net Zero compatible.*

Framing we agreed on: make SAP's existing Autonomous Enterprise strategy net zero compatible, focusing on **efficiency** rather than quantitative modelling. Success means business impact stays **neutral or better**.

## The tension

| Autonomous Enterprise | Net zero by 2030 |
|---|---|
| Agents and AI in more and more processes | At least 90% gross reduction of value-chain emissions (2023 baseline) |
| Each agent plans, calls tools, checks and retries | Target validated by SBTi and tied to executive pay |
| More autonomy → more compute → more energy | Residual emissions may only be neutralised by removals (max. 10%) |

Source: SAP sustainability challenge intro (1 Oct 2026); SAP Integrated Report.

## Root cause

The waste is not AI itself, but **using the wrong tool**: an agent doing a task a simple workflow could do. Process owners build their own automations, are trained on the tool but not on *when to use which step*, and never see what their agents consume.

## Thesis: the automation ladder

**Always use the lowest step that does the job.**

| Step | Example (recruiting) |
|---|---|
| 1 Rule | Check that all required documents are uploaded |
| 2 Workflow | Send status notifications at each stage of an application |
| 3 Classic ML | Suggest optional onboarding modules by role |
| 4 GenAI call | Draft a personalised message from a template |
| 5 Agent | Schedule a multi-round panel across time zones |
| 6 Multi-agent | Coordinate an international relocation across HR, IT and facilities |

Compute and energy need rise with every step.

## Key idea: agents explore, workflows execute

Agents are useful for new, messy cases. Once logs show that an agent keeps taking the same path, that path is frozen into a workflow, and the agent only handles the remaining exceptions. The ladder becomes a **cycle**, not a one-off choice.
