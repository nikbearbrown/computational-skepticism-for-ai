# Media Plan — Chapter 3: Data Validation: Reconstructing the Epistemic Frame Behind a Dataset

Zones detected: 12 · video 1 · figure 1 · graph 2 · table 1 · served 5 · dropped 2

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Silent join failure — you cannot compute the missingness of rows that never existed | MC | video | 9/10 (static already SERVED by Fig 3.1) |
| 2 | MCAR / MAR / MNAR — which missingness type, how detected, when imputation is safe | CT | table | Important |
| 3 | Channel effectiveness ranking — position outranks length outranks area/color (Cleveland & McGill) | PQ | graph | Important |
| 4 | Two variables perfectly dependent (y = x²) can show Pearson r ≈ 0 | PQ | graph | Important |
| 5 | "Boundary exceeds schema" is a spectrum — sharpest for email/chat, near-absent for sensor logs | VG | figure | Supplementary |
| 6 | Six structural failure modes invisible to procedural EDA | CT | SERVED | — |
| 7 | Access boundary = schema + everything its contents reference | VG | SERVED | — |
| 8 | Six-step epistemic-frame reconstruction procedure | MC | SERVED | — |
| 9 | Delegate freely / verify before trusting / do not delegate | DC | SERVED | — |
| 10 | Co-missingness structure across columns (missingno matrix) | VG | SERVED | — |
| 11 | Prediction-lock mechanism (hindsight erases the gap) | MC | dropped | no transition mechanism a video/figure adds beyond the prose |
| 12 | IQR rule vs Z-score rule for outlier flagging | CT | dropped | two-item contrast, prose carries it; Fig 3.5 adjacent |

## Graph cards

```
GRAPH 1 — Perceptual accuracy by visual channel (Cleveland & McGill ranking)
Priority: Important
Reader question: How much more accurately do people read position than length, angle, area, or color intensity — is the gap big enough to change how I build charts?
Family + first candidate: comparison→sorted dot plot (encoding on y, error on x, CI whiskers)
Data status: spec needed — real empirical results exist and are published; digitize from the source, do not invent
DATA SPEC:
  Unit of observation: one encoding condition (position-common-scale, position-nonaligned, length, angle/slope, area, color intensity)
  Fields: encoding : category; midmean_log_abs_error : number; ci_low : number; ci_high : number
  Denominator: judgment error (log2 absolute error of proportion estimates) — not a rate
  Expected n: 5–10 encoding conditions
  Likely source: Cleveland & McGill 1984, JASA 79(387):531–554, experimental results (midmeans + 95% CIs)
Exclusions: Stevens' power-law exponents (chapter calls it a bridge, not the finding); per-subject data; any chart-junk/style commentary. This graph exists so "position outranks color" stops being a slogan and becomes a measured gap.
```

```
GRAPH 2 — Perfect dependence, zero correlation
Priority: Important
Reader question: How can two variables be completely dependent and still produce r ≈ 0 — what does the scatter look like when the heatmap goes blind?
Family + first candidate: relationship→scatter, small multiples (3 panels: linear-with-noise r≈0.9; y = x² r≈0; circle/ring r≈0), Pearson r annotated per panel
Data status: illustrative-only possible — and legitimately so: the points are synthetic by mathematical construction, demonstrating a property of the Pearson statistic, not an empirical finding. Panels must be labeled as constructed data.
DATA SPEC:
  Unit of observation: one (x, y) point, tagged by panel
  Fields: panel : category; x : number; y : number (per-panel r computed and displayed)
  Denominator: counts (n points per panel)
  Expected n: ~200 points × 3 panels, generated from documented formulas + seed
  Likely source: generated (formulas in caption)
Exclusions: full Anscombe-quartet digression; mutual-information or distance-correlation sidebars; any suggestion the panels are real data.
```

## Table cards

```
TABLE 1 — Rubin's missingness taxonomy as a decision aid
Heuristic: CT
Priority: Important
Reader question: Which missingness type am I looking at, can I detect it from inside the data, and is imputation safe?
Proposed shape: 3 rows × 5 columns, class: comparison-table
Rows: MCAR, MAR, MNAR
Columns: what the missingness depends on; canonical example (from chapter: sensor dropout / young respondents skip income / high earners suppress income); detectable from within the dataset?; imputation safety; the question that detects it
Exclusions: Rubin's formal notation and the 1976/1987 citation apparatus (stays in the footnote); imputation algorithms; missingno tooling (Fig 3.2 owns that). Currently this three-way contrast lives entirely in one dense prose paragraph that students will re-read to compare — the chapter's other enumerations all got tables, this one didn't.
```

## Served zones
- SERVED — Six structural failure modes: existing 6×4 styled table ("The six failures") does exactly the lookup/contrast job.
- SERVED — Access boundary ⊃ schema: Fig 3.9 concentric boundary diagram, with a strong caption.
- SERVED — Six-step reconstruction procedure: Fig 3.10 linear workflow diagram ("keep this as a checklist").
- SERVED — Delegation three-way split: existing 3×3 styled table with rationale column.
- SERVED — Co-missingness structure: Fig 3.2 missingno-style matrix; caption already carries the pattern-vs-mechanism caveat.
- SERVED-POORLY — Opening join-failure zone / marks-and-channels zone: Fig 3.1 and Fig 3.6 have contentless alt text and captions ("Diagram", "Illustration"). Whatever they render, the caption does no teaching work and the figure cannot be audited against the zone. Suggest caption/alt rewrite when figures are revisited (not a new medium; noted for the figures pass).

## Pointers
- Figure cards: pantry/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset-cajal.md
- Video candidates from this chapter: vids/video-ideas.md (Candidate: "Why a Clean EDA Report Can Hide a Broken Dataset" — numbering assigned at book assembly)
