# Media Plan — Chapter 11: Communicating Uncertainty: Calibrating Claims to Evidence

Zones detected: 18 · video 2 · figure 1 · graph 2 · table 2 · served 9 · dropped 2

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Same evidence, three verbs — the frozen ladder as an evidence-priced upgrade path | MC | video (Candidate 01) | 9/10 |
| 2 | The one-line ladder is a deliberate projection of a two-axis space (caution × strength) | VG | figure (cajal FIGURE 1) | Important |
| 3 | Aggregate calibration metrics arithmetically wash out subgroup failure | PQ | video (Candidate 02) | 8/10 |
| 4 | Epic Sepsis: developer-reported vs externally validated performance | PQ | graph (GRAPH 1) | Critical |
| 5 | ECE is bin-dependent — the same predictions yield different ECEs under different binning | PQ | graph (GRAPH 2) | Important |
| 6 | Which calibration metric to report when — computes / detects / blind spot | SP/DC | table (TABLE 1) | Important |
| 7 | Epistemic vs aleatoric uncertainty — which hedge is honest | CT | table (TABLE 2) | Supplementary |
| 8 | Three-layer document structure | VG | SERVED | — |
| 9 | Brier score decomposition (uncertainty / resolution / calibration) | MC | SERVED | — |
| 10 | Reliability-diagram miscalibration shapes (over/under/sigmoidal/local) | VG | SERVED | — |
| 11 | Temperature scaling mechanism and its non-transfer limits | MC | SERVED | — |
| 12 | Conformal prediction mechanism and exchangeability assumption | MC | SERVED | — |
| 13 | Verb taxonomy as fluency-trap detector on AI output | MC | SERVED | — |
| 14 | Evidence-level → warranted-verb mapping (L0–L5 ladder) | DC | SERVED | — |
| 15 | Per-verb epistemic posture / minimum evidence / misuse | CT | SERVED | — |
| 16 | Subgroup ECE exemplar numbers (aggregate-mask made visible) | PQ | SERVED-POORLY | — |
| 17 | Five prose moves for saying you don't know in writing | EN | dropped — moves are discursive; a table would flatten what the prose teaches | — |
| 18 | Six-step peer critique protocol | EN | dropped — already a numbered list; no comparison dimension | — |

## Graph cards

```
GRAPH 1 — Epic Sepsis: what the developer reported vs what external validation found
Priority: Critical
Reader question: How far did the deployed model's real performance fall from its
  marketed performance, on each metric that matters clinically?
Family + first candidate: comparison → dumbbell/dot-range (AUC claimed-range vs
  observed point) with companion bars for PPV and missed-case rate
Data status: provided — Wong et al. 2021 (JAMA Internal Medicine,
  doi:10.1001/jamainternmed.2021.2626), as cited in the chapter: AUC 0.63 vs
  developer-reported 0.76–0.83; PPV 12% (88% of alerts false alarms); 67% of
  sepsis cases missed (1,709 of 2,552); cohort 27,697 patients / 38,455
  hospitalizations at Michigan Medicine. These are the chapter's confirmed,
  real numbers — the only "provided" graph data in the chapter.
DATA SPEC:
  Unit of observation: one (metric, source) pair
  Fields: metric : categorical (AUC | PPV | sepsis cases missed);
          source : categorical (developer-reported | external validation);
          value : numeric; value_hi : numeric (for the 0.76–0.83 claimed range)
  Denominator: PPV over alerts fired; missed-case rate over 2,552 septic
          patients; AUC is denominator-free
  Expected n: ~5 rows
  Likely source: Wong et al. 2021 as cited in-chapter (no new data needed)
Exclusions: no hospital-level breakdown, no ECE (not reported for this case),
  no illustrative extensions or extrapolated series — cited values only.
```

```
GRAPH 2 — ECE bin-dependence: same predictions, different bin counts, different ECE
Priority: Important
Reader question: How much does a reported ECE move when nothing changes but the
  number of bins — i.e., why is an ECE without its binning spec not reproducible?
Family + first candidate: time-series-style line → ECE (y) vs bin count M (x),
  one line per prediction set (2–3 sets)
Data status: spec needed / illustrative-only possible — must be computed on an
  actual prediction set (public model logits or a synthetic set). The chapter's
  ECE rules of thumb (0.02–0.05 "well-calibrated", >0.10 "systematic") are
  flagged [verify]/illustrative in the text — do NOT draw them as reference
  lines presented as findings.
DATA SPEC:
  Unit of observation: one (prediction set, bin count) pair
  Fields: bins : int; ece : numeric; prediction_set : categorical
  Denominator: N predictions per set (fixed within each line)
  Expected n: M ∈ {5…50} × 2–3 sets ≈ 90–140 rows
  Likely source: computed from any public held-out prediction dump (e.g.,
          CIFAR/ImageNet logits) or a clearly-labeled synthetic set
Exclusions: no MCE overlay, no adaptive/equal-mass binning variants, no
  threshold rules-of-thumb, no subgroup dimension (that is Candidate 02's job).
```

## Table cards

```
TABLE 1 — Calibration metric chooser: what each metric computes, detects, and cannot see
Heuristic: SP / DC
Priority: Important
Reader question: Which calibration metric do I report for this deployment, and
  what must accompany it for the number to mean anything?
Proposed shape: 6 × 5, class: comparison-table
Rows: Brier score (decomposed), ECE, MCE, reliability diagram, subgroup ECE,
  conformal coverage
Columns: what it computes | range or guarantee | what it detects | structural
  blind spot | must be reported with (e.g., binning spec, subgroup list,
  exchangeability assumption)
Exclusions: formulas stay in prose (all four already displayed); the L0–L5
  evidence ladder and the failure-mode table already exist — do not duplicate
  their columns; no proper-scoring-rule theory.
```

```
TABLE 2 — Epistemic vs aleatoric uncertainty: which hedge is honest
Heuristic: CT
Priority: Supplementary
Reader question: Is this uncertainty reducible with more evidence, and how do I
  phrase the hedge accordingly?
Proposed shape: 2 × 4, class: comparison-table
Rows: epistemic, aleatoric
Columns: definition | reducible by more data? | deployed-AI example (from the
  chapter: unseen rare subgroup vs genuinely noisy outcomes) | how the written
  hedge should read
Exclusions: no Bayesian formalism, no uncertainty-decomposition math, no
  overlap with the five prose moves (which stay in prose).
```

## Served zones
- SERVED — three-layer document structure: Figure 11.1 (layered document structure).
- SERVED — Brier decomposition: Figure 11.2 plus the displayed decomposition equation.
- SERVED — reliability-diagram miscalibration shapes: Figure 11.3 (2×2 grid of the four deviation patterns).
- SERVED — temperature scaling mechanism/limits: Figure 11.4.
- SERVED — conformal prediction mechanism: Figure 11.5.
- SERVED — verb audit of AI output: Figure 11.6 plus the worked "conclusively demonstrates" paragraph.
- SERVED — evidence→verb mapping: two existing tables (evidence-available table and the L0–L5 calibration evidence ladder).
- SERVED — per-verb posture/evidence/misuse: the 8-row verb taxonomy table (frozen ladder order).
- SERVED-POORLY — subgroup-ECE masking exemplar: the 6-row subgroup table makes the reader compute the aggregate-vs-subgroup contrast from exact values, but the argument is a magnitude comparison (rare-disease ECE 0.103 vs global 0.018), not a lookup; suggest a companion graph — sorted subgroup-ECE dot plot with a global-ECE reference line — clearly labeled illustrative-only, since the table's values are exemplar, not measured. Keep the table as the audit template it also is.

## Pointers
- Figure cards: pantry/11-communicating-uncertainty-calibrating-claims-to-evidence-cajal.md
- Video candidates from this chapter: vids/video-ideas.md (Candidates 01, 02 — delivered to parent for assembly)
