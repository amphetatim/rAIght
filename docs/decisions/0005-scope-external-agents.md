# ADR 0005 – Scope: external agents and automations

- **Status:** accepted
- **Date:** 2026-10-23
- **Amends:** [ADR 0004](0004-demo-first-scope.md) (named systems), concept docs 01–05, 08, 09

## Context

The IS 615 concept placed rAIght *inside SAP's own low-code / agent platform*. For IS 613 that is hard to make credible: we don't know how many agents actually run in SAP software, and finding out is harder than the build itself.

Most self-built AI automations at a company like SAP are created with **third-party tools** that employees already have – Microsoft Copilot Studio, Power Automate with AI steps, OpenAI assistants, n8n and similar. That is also where sprawl nobody reviews happens ("shadow AI").

We are free to frame the project and the pitch as we like; it does not have to answer the original sustainability challenge.

## Decision

1. **Scope A – automations, not chat.** rAIght covers **agents and automations that employees build themselves** and that run a process (each run = a sequence of steps/tool calls). **Chat usage** of assistants (e.g. asking Copilot to draft an email) is **out of scope**: it has no path to analyse, nothing to convert, and monitoring it would mean monitoring employees.
2. **External providers only (for now).** Sources are third-party tools: **Microsoft Copilot Studio, Power Automate (AI Builder), OpenAI (Assistants / GPTs), n8n** – extendable via one adapter per provider. SAP-internal agent platforms are not a source in this phase.
3. **SAP integration is a later stage.** Once the business case is proven internally, rAIght is migrated into the SAP stack (e.g. running on SAP BTP, SAP agents as an additional source) and offered to SAP customers as a service.
4. **Pitch framing.** SAP's **CIO office** commissions an internal **taskforce** to cut **token costs and CO₂ emissions** of employee-built AI automations without slowing adoption. rAIght is the taskforce's answer: first used internally ("customer zero"), later sold. The **sustainability office** is a stakeholder (CO₂ reporting).
5. **Conversion stays within the tool.** A uniform agent becomes the lower ladder step in the same tool (Copilot Studio agent → Power Automate flow; n8n AI node → plain n8n workflow).

## Consequences

- Concept, demo script, data model and architecture name **external providers** instead of SAP platforms. The persona (Lena, SAP HR recruiting) stays; she builds with Copilot Studio and n8n.
- Agents get a `provider` field; run logs from all providers are normalised into **one schema** by provider-specific mock adapters.
- **Hotspot H3 (agent inventory) becomes central**: rAIght first has to find agents across tools. In the demo: a mocked import from all providers (#20, light).
- New open question: how much step-level data each provider exposes (tokens, tool-call sequence). A short spike checks this so the demo story stays plausible; the demo itself stays mocked ([ADR 0004](0004-demo-first-scope.md)).
- CO₂ per token for external providers is not published reliably – tokens remain a **proxy** (H5).
- Business case and pitch are rebuilt around the CIO office's commission (tokens, licences, CO₂) and the later product stage.
- The tech-stack decision becomes ADR 0006.
