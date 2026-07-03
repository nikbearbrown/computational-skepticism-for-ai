# CAJAL Figure Plan — Chapter 8: Validating Agentic AI: When Autonomous Systems Misbehave

FIGURE 1 — The false-success catch: gate, act, verify world state, compare, stop
Heuristic: MC
Priority: Critical
Concept (one sentence): The validation loop for consequence systems — before an irreversible action, gate on confirmation from the owner (not the requester); after it, observe world state independently of the agent's report; compare report against world; on divergence, fire the stop condition — because the agent's completion report is one datum, not evidence of completion.
Reader/audience: has read the Ash case (Case #1); knows what an audit trail is; does not yet distinguish "read the trail" from "verify the world" — the exact confusion this figure exists to prevent (in Case #1 the trail itself was wrong).
Type: process flowchart
Components (6):
  1. Proposed irreversible action (e.g., anything described as "nuclear" / "wipe")
  2. Gating condition — independent confirmation from the OWNER, not the requesting party
  3. Action executes; agent's completion report captured to the trail
  4. Independent world-state check (e.g., the actual Proton Mail server), performed outside the agent
  5. Comparison node: report vs observed world state
  6. Two exits: match → log and proceed · mismatch → stop condition + alert to a human
Exclusions: no taxonomy categories, no multi-agent variants, no Case #1 narrative detail (Fig 8.6 already carries the failure chain), no Chapter 9 delegation-map clauses

Recommended: 1 figure, Mechanistic density. (Chapter already carries 8 CAJAL figures; this is the only unserved figure zone — it depicts the chapter's central working skill, which currently lives only in prose spread across the Explainability-lens paragraph and the boundary section.)
