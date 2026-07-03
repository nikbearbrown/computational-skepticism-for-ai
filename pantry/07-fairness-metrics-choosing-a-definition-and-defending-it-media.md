# Media Plan — Chapter 7: Fairness Metrics: Choosing a Definition and Defending It

Zones detected: 13 · video 2 · figure 1 · graph 2 · table 0 · served 8 · dropped 0

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Impossibility arithmetic — calibration forces TPR/FPR apart when base rates differ | MC | video (Candidate 01) | 9/10 |
| 2 | Worked two-regime example (calibration-satisfying vs equalized-odds-satisfying tables) | PQ | graph (GRAPH 1) — SERVED-POORLY by tables | Important |
| 3 | Continuous forcing: base-rate gap vs required TPR/FPR-ratio divergence | PQ | graph (GRAPH 2) | Important |
| 4 | Three definitions + embedded values claims | CT | SERVED | — |
| 5 | COMPAS: both sides factually right, values disagreement | CT | SERVED | — |
| 6 | Lipschitz condition — same equation, opposite guarantee depending on d | VG | figure (FIGURE 1) — SERVED-POORLY by Fig 7.2 | Important |
| 7 | Counterfactual fairness three-step (abduction–action–prediction) | MC | SERVED | — |
| 8 | Three causal paths A→Ŷ (direct / indirect / spurious) | VG | SERVED | — |
| 9 | GE Index α parameter shifts sensitivity across the distribution | PQ | SERVED | — |
| 10 | GE decomposition into within-group + between-group | PQ | SERVED | — |
| 11 | Debiasing toolkit three families (pre / in / post-processing) | CT | SERVED | — |
| 12 | Defended-choice six-step deliverable structure | EN | SERVED | — |
| 13 | The relocation motif — every exit (d, causal graph, α/bᵢ) relocates the same values choice | MC/VG | video (Candidate 02) | 8/10 |

## Graph cards

```
GRAPH 1 — The same model under two fairness regimes: what equalizes and what splits
Priority: Important
Reader question: When calibration is enforced, which quantities diverge between the
  two groups — and when equalized odds is enforced, which diverge instead?
Family + first candidate: comparison→paired dumbbell (one dot pair per metric,
  two small-multiple panels, one per regime)
Data status: provided — but ILLUSTRATIVE: these are the chapter's own worked numbers,
  chosen to make the arithmetic visible. Label the graph "worked example," never findings.
DATA SPEC:
  Unit of observation: one metric × group × regime cell
  Fields: regime : categorical(2) [calibration-satisfying, equalized-odds-satisfying];
          metric : categorical(4) [TPR, FPR, PPV, positive prediction rate];
          group : categorical(2) [A (base rate 0.6), B (base rate 0.3)];
          value : float 0–1
  Denominator: each rate conditioned per its confusion-matrix definition
  Expected n: 16 values (2 × 4 × 2)
  Likely source: the two in-chapter worked tables (thresholds 0.5/0.5 and 0.5/0.6)
Exclusions: thresholds as annotations only; no accuracy series; no demographic-parity panel
```

```
GRAPH 2 — How the base-rate gap forces error rates apart under calibration
Priority: Important
Reader question: As the gap between group base rates grows, how strongly is the
  TPR/FPR ratio forced to diverge between groups — and where does the forcing vanish?
Family + first candidate: relationship→line (analytic curve; coefficient
  p_b(1−p_a) / p_a(1−p_b) as a function of p_b, one line per fixed p_a)
Data status: illustrative-only possible — an exact analytic identity, computable to
  arbitrary precision, but NOT empirical data. Label as "the theorem's coefficient,"
  not measurements.
DATA SPEC:
  Unit of observation: one (p_a, p_b) pair
  Fields: p_b : float grid 0.05–0.95; p_a : categorical(3) fixed values e.g. 0.3/0.5/0.7;
          coefficient : float (=1 marks the no-forcing line)
  Denominator: — (dimensionless ratio)
  Expected n: ~200 grid points × 3 lines
  Likely source: computed from the odds identity in-chapter (Chouldechova 2017)
Exclusions: no ROC curves; no COMPAS empirical rates; no demographic-parity constraint;
  no perfect-prediction degenerate branch beyond a single annotation
```

## Table cards

None — every table-worthy zone (definitions/values, COMPAS claims, framework comparison, toolkit families) already carries a styled table.

## Served zones

- SERVED — Three definitions + values claims: 4-column comparison table after the formal definitions.
- SERVED — COMPAS both-sides-right: 5-column table with the *"Both sides were right about the numbers"* caption.
- SERVED — Counterfactual three-step procedure: Fig 7.3.
- SERVED — Three causal paths: Fig 7.4.
- SERVED — GE α sensitivity: Fig 7.5.
- SERVED — GE within/between decomposition: Fig 7.6 (already a stacked bar).
- SERVED — Toolkit three families: comparison table with limitation caption.
- SERVED — Defended-choice six-step structure: Fig 7.7.
- SERVED-POORLY — Worked two-regime example (zone 2): two markdown tables doing a graph's job — the reader's task is comparing which quantities align vs split across regimes (shape), not looking up values; suggest graph (GRAPH 1).
- SERVED-POORLY — Lipschitz d-dependence (zone 6): Fig 7.2's caption is a placeholder ("Illustration") and the zone's teaching load is a two-panel contrast (same pair, two choices of d, opposite guarantees) that the general Lipschitz-bound illustration does not carry; suggest figure (FIGURE 1 in the cajal plan). Do not modify Fig 7.2; this is a suggested rework.

## Pointers
- Figure cards: pantry/07-fairness-metrics-choosing-a-definition-and-defending-it-cajal.md
- Video candidates from this chapter: vids/video-ideas.md (Candidates 01, 02 of this scouting pass — assembled by the parent)
