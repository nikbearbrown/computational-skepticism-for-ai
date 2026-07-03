# Media Plan — Chapter 8: Validating Agentic AI: When Autonomous Systems Misbehave

Zones detected: 18 · video 3 · figure 1 · graph 0 · table 2 · served 12 · dropped 0

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Ash false-success mechanism — completion report and world state contradict, nothing notices | MC | video (Candidate 03) | 9/10 |
| 2 | The false-success catch — gate, act, verify world state independently, compare, stop | MC | figure (FIGURE 1) | Critical |
| 3 | Prediction system vs consequence system | VG | SERVED | — |
| 4 | Autonomy-competence gap (L4 actions, L2 understanding) | VG | SERVED | — |
| 5 | OpenClaw agent architecture | VG | SERVED | — |
| 6 | Four-category taxonomy mapped to the eleven cases | CT | SERVED | — |
| 7 | Effective vs documented data scope — indirect requests extract more than the spec (Cases #2/#3) | MC/VG | video (Candidate 05) | 7/10 |
| 8 | Case #7 escalation chain (remediation conflated with obedience) | MC | SERVED | — |
| 9 | Case #8 channel-boundary identity spoofing | MC | SERVED | — |
| 10 | Compact cases #4/#5, #9/#10, #11 | EN | SERVED | — |
| 11 | The cases that held (#12–#16): genuine robustness vs contingent luck | EN/CT | table (TABLE 2) | Supplementary |
| 12 | Fundamental vs contingent failure routing | DC | SERVED | — |
| 13 | Four validation lenses applied to agents | CT | SERVED | — |
| 14 | Cascading hallucination — per-agent error rates don't add, they compound | MC/PQ | video (Candidate 04) | 8/10 |
| 15 | Multi-agent failure modes overview | EN | SERVED | — |
| 16 | Responsibility across five actors | SP | SERVED | — |
| 17 | Validation vs design boundary — the validator's this-week deliverable | CT | table (TABLE 1) | Important |
| 18 | Five Supervisory Capacities × cases | CT | SERVED | — |

## Graph cards

None. This chapter's claims are qualitative case mechanics; the only quantitative shapes in the prose (~60,000 tokens over nine days, ~10MB attachments, the 2%+3%→~30% compounding) are either passing mentions or explicitly illustrative rhetoric. The compounding curve is carded as the static fallback of video Candidate 04 rather than as a standalone graph — if built, it must be labeled illustrative (analytic independence curve vs a stipulated cascade model, not measurements).

## Table cards

```
TABLE 1 — Validator's deliverable vs designer's proposal for the same failure
Heuristic: CT
Priority: Important
Reader question: For a given agent failure, which responses are validation-scope
  (this week, on an agent you cannot redesign) and which are design proposals
  (a different discipline)?
Proposed shape: 4 × 3, class: comparison-table
Rows: false success report (Case #1); non-owner compliance (Case #2); sensitive
  disclosure (Case #3); resource loop / DoS (Cases #4–#5)
Columns: the failure (one line) | design proposal — out of validator scope |
  validation-scope intervention (gating condition, independent state check,
  monitoring alert, budget cap)
Exclusions: taxonomy classification and fundamental/contingent verdicts (already
  tabled elsewhere); implementation detail of any redesign; Chapter 9's delegation-map
  machinery
```

```
TABLE 2 — The cases that held (#12–#16): what resisted, and under what condition
  the resistance fails
Heuristic: EN
Priority: Supplementary
Reader question: Which attacks failed, was each resistance verified authority or
  contingent luck, and what named condition would break it?
Proposed shape: 5 × 4, class: data-table
Rows: #12 direct prompt injection refused; #13 email spoofing rejected; #14 data
  tampering declined; #15 social engineering resisted; #16 emergent safety coordination
Columns: attack attempted | agent behavior [verify] | basis of resistance
  (verified vs circular/unjustified) [verify] | failure condition to test
Exclusions: the eleven failure cases; four-lens analysis; exercise S3's answers
Note: the chapter itself flags the case-to-behavior mapping [verify]; every cell in
  columns 2–3 must be checked against Shapira et al. before this table is built.
```

## Served zones

- SERVED — Prediction vs consequence system: Fig 8.1.
- SERVED — Autonomy-competence gap: Fig 8.2.
- SERVED — OpenClaw architecture: Fig 8.3.
- SERVED — Taxonomy → cases mapping: 4-row table plus Fig 8.5 (case routing).
- SERVED — Effective-scope lookup side of Cases #2/#3: the 5-row data-source audit template table (documented vs effective scope, disclosure conditions) — the video candidate covers the mechanism, the table covers the audit lookup.
- SERVED — Case #7 escalation chain: Fig 8.7.
- SERVED — Case #8 channel-boundary spoofing: Fig 8.8.
- SERVED — Compact cases #4/#5, #9/#10, #11: 3-row table.
- SERVED — Fundamental vs contingent routing: 5-row table with the "patch ships the failure" caption.
- SERVED — Four lenses applied to agents: 4-row table.
- SERVED — Multi-agent failure modes overview: Fig 8.10 (the mechanism-in-motion of cascading is the video's job; the mode inventory is served).
- SERVED — Responsibility across five actors: 5-row template table.
- SERVED — Supervisory capacities × cases: 5-row table.
- SERVED-POORLY — none at the media level; but note two caption/numbering slips: a table is captioned "*Figure 8.4*" (taxonomy mapping) and another "*Figure 8.9*" (four lenses) — tables labeled as figures, which will break figure numbering downstream. Editorial fix, not a media card.

## Pointers
- Figure cards: pantry/08-validating-agentic-ai-when-autonomous-systems-misbehave-cajal.md
- Video candidates from this chapter: vids/video-ideas.md (Candidates 03, 04, 05 of this scouting pass — assembled by the parent)
