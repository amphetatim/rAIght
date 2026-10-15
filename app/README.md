# app/ – implementation (IS 613)

The code for rAIght lives here. **The technology stack is not decided yet.** Wait for the IS 613 requirements and record the decision as an ADR in [`docs/decisions/`](../docs/decisions/).

## What Release 1 needs technically

From the [user story map](../docs/concept/06-user-story-map.md), the walking skeleton needs:

| Need | Why |
|---|---|
| **Run log ingestion** | Read agent run logs (tokens, steps, output) – the only data source of the dashboard |
| **Metrics** | Token usage per agent; *same-path share* (share of runs with an identical sequence of steps) – simple statistics, no extra AI |
| **Dashboard UI** | Per agent: usage, same-path share, suggestion (e.g. "Convert to workflow") |
| **Agent inventory** | List of agents with owner and purpose, incl. a one-line reason why an agent was chosen |
| **Training content** | Ladder and triage material (can start as static pages) |

For a course prototype, the run logs can be **simulated** with realistic sample data for the four recruiting agents in the concept.

## Questions to settle once IS 613 starts

1. Is a stack prescribed (e.g. SAP BTP with CAP and SAPUI5/Fiori), or is it free?
2. Where does it run – locally only, or deployed to a cloud account the course provides?
3. Real or simulated run logs?

Until then, please don't add a framework here – it is easy to start, hard to undo.
