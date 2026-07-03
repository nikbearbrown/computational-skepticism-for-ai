# Media Plan — Chapter 6: Bias: Where It Enters and Who Is Responsible

Zones detected: 18 · video 3 · figure 2 · graph 3 · table 1 · served 7 · dropped 2

Scope note: end-of-chapter apparatus (Glimmer, Exercises, LLM Exercise) not scanned. The chapter already carries 8 CAJAL figures and 5 styled tables; only unserved zones are carded below.

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Three teams / leverage: the highest-leverage fix bypassed the model entirely (path-blocking on the causal graph) | MC | video | 9/10 (Candidate 02) |
| 2 | Historical bias: error-free, representative data that is still poison — accuracy IS the harm | MC | video | 9/10 (Candidate 03) |
| 3 | Bias as estimator property: more data converges, with confidence, to the wrong answer (Literary Digest 1936) | MC/PQ | video | 8/10 (Candidate 06) |
| 4 | Literary Digest (n=2.4M, wrong) vs Gallup (n≈50K, right) — the numbers themselves | PQ | graph | Important |
| 5 | COMPAS: false-positive and false-negative rates fall unevenly by race | PQ | graph | Critical |
| 6 | Funnel plot: the missing lower-left corner of unpublished null studies | PQ/VG | graph | Important |
| 7 | The ten entry-point mechanisms as a single lookup reference (currently prose-only across four sections) | EN | table | Critical |
| 8 | Implicit bias as water table; confirmation/observer/coding/publication as its four springs | VG | figure | Important |
| 9 | Provider-upstream bias: the leverage point outside the deploying team's reach (Agents of Chaos Case #6) | VG | figure | Supplementary |
| 10 | Estimator bias picture: scatter narrows, offset stays | VG | SERVED | — |
| 11 | Ten-mechanism pipeline entry-point map | VG | SERVED | — |
| 12 | Historical bias mechanism (static) | MC | SERVED | — |
| 13 | Dataset / label / structural contrast | CT | SERVED | — |
| 14 | Compound bias-pair interactions | CT | SERVED | — |
| 15 | Fairness impossibility (sketch + criteria lookup; full proof deferred to Ch7) | PQ | SERVED | — |
| 16 | Pearl Rung 1 vs Rung 2, four fairness questions | CT | SERVED | — |
| 17 | Sepsis six-hour-filter selection mechanism as standalone visual | MC | dropped | entry point served by Fig 6.3; estimator lesson carried by zone 3 video |
| 18 | Apple Card as adjudicated (not proven) bias claim | — | dropped | prose does this job; no visual adds |

## Graph cards

```
GRAPH 1 — 1936: the 2.4-million-response poll vs the 50,000-response poll
Priority: Important
Reader question: Did 48× the sample size get the Literary Digest any closer to the actual result than Gallup?
Family + first candidate: comparison → dot plot per poll (predicted FDR vote share vs actual, sample size labeled; log-scale n annotation)
Data status: provided (historical; the chapter gives n = 2.4M and ~50,000 — exact predicted vote shares must be pulled from Squire 1988 before rendering [verify])
DATA SPEC:
  Unit of observation: one poll (plus the actual result as reference line)
  Fields: poll : categorical (Literary Digest | Gallup), n : int, predicted_fdr_share : pct, actual_fdr_share : pct (~62.5 [verify]), error_pts : float
  Denominator: share of major-party popular vote
  Expected n: 2 polls + 1 reference value
  Likely source: Squire, "Why the 1936 Literary Digest Poll Failed," Public Opinion Quarterly 52(1), 1988
Exclusions: no other election years; no telephone/car-owner frame decomposition (prose handles it); no modern polling analogies
```

```
GRAPH 2 — COMPAS: the errors fall unevenly
Priority: Critical
Reader question: How differently do false-positive and false-negative rates land on Black vs white defendants?
Family + first candidate: comparison → grouped bar (error type × group, four bars)
Data status: provided (ProPublica 2016 published the rates and the underlying Broward County dataset is public; commonly cited values ≈ FPR 44.9% vs 23.5%, FNR 28.0% vs 47.7% — pull exact figures from the primary before rendering [verify])
DATA SPEC:
  Unit of observation: group × error type
  Fields: group : categorical (Black | white), error_type : categorical (FPR | FNR), rate : pct
  Denominator: FPR — non-reoffenders within group; FNR — reoffenders within group
  Expected n: 4 bars (derived from ~7,000 defendants, Broward County 2013–14)
  Likely source: Angwin et al., "Machine Bias," ProPublica 2016 + ProPublica's public COMPAS analysis repository
Exclusions: no calibration curves (Northpointe's counter-analysis stays a caption note — the full two-sided treatment is Chapter 7's job); no score-decile breakdown; no overall-accuracy series
```

```
GRAPH 3 — The funnel plot and the missing corner
Priority: Important
Reader question: What shape does an unbiased literature make on a funnel plot, and where does publication bias eat a corner out of it?
Family + first candidate: relationship → scatter of effect size vs precision (SE, inverted axis), two panels: symmetric funnel vs asymmetric funnel with lower-left corner missing
Data status: illustrative-only possible — the chapter asserts the shape, not a dataset. A real public meta-analysis (e.g., a metafor package example dataset) could substitute; otherwise label clearly as synthetic demonstration.
DATA SPEC:
  Unit of observation: one study
  Fields: study_id : int, effect_size : float, standard_error : float, published : bool
  Denominator: counts
  Expected n: ~60 studies per panel
  Likely source: synthetic, or a named public meta-analytic dataset (metafor examples)
Exclusions: no trim-and-fill imputed points drawn as if real (mention in caption only); no Egger's test statistics; no confirmation-bias compounding overlay (prose handles the compound)
```

## Table cards

```
TABLE 1 — Master reference: the ten bias mechanisms
Heuristic: EN
Priority: Critical
Reader question: Which of the ten mechanisms am I looking at, where does it enter the pipeline, what diagnostic exposes it, and what fix actually has leverage on it?
Proposed shape: 10 rows × 5 columns, class: data-table
Rows: selection, sampling, confirmation, observer, self-report, data-coding, data-entry, publication, historical, implicit
Columns: how it enters (one line), pipeline stage, tell-tale diagnostic (e.g., IPW/inclusion-vs-outcome check; kappa collapse on unblinding; kappa low on items not people; external gold standard; outlier + source-document check; funnel plot; green metrics + disparate outcomes; downstream group-rate audit), highest-leverage fix, flavor (dataset / label / structural)
Exclusions: compound interactions (existing compound-pairs table covers them); formal E[θ̂]−θ definitions (prose); fairness metric definitions (existing criteria table). Cells the prose does not state get [verify].
Justification for a new table in an already table-heavy chapter: the ten mechanisms — the chapter's own central taxonomy — are scattered across four prose sections with no single lookup surface; W1/A2/S4/C2 exercises and the LLM exercise all require walking "the ten," and today the reader must re-read ~2,500 words to do it.
```

## Served zones
- SERVED — More data narrows scatter but not offset: Fig 6.1.
- SERVED — Ten-mechanism pipeline entry-point map: Fig 6.3 (spatial map; the new TABLE 1 is the lookup complement, not a duplicate).
- SERVED — Historical bias mechanism (static): Fig 6.2.
- SERVED — Dataset / label / structural contrast: the large three-column table (captioned "Figure 6.4").
- SERVED — Compound bias-pair interactions: the amplifying-pairs table.
- SERVED — Fairness impossibility: Fig 6.5 visual proof sketch + fairness-criteria table; full worked treatment is deliberately Chapter 7's.
- SERVED — Pearl Rungs 1/2: Fig 6.6 + the four-question Rung 1/Rung 2 table; leverage procedure: Figs 6.7 and 6.8.

No SERVED-POORLY findings — but one bookkeeping flag for the parent: the dataset/label/structural markdown TABLE is captioned "*Figure 6.4*", which desynchronizes figure numbering (image fig-04.png is then captioned Figure 6.5, fig-05.png Figure 6.6, etc.). Renumber or recaption before any figure work references "Figure 6.N".

## Pointers
- Figure cards: pantry/06-bias-where-it-enters-and-who-is-responsible-cajal.md
- Video candidates from this chapter: vids/video-ideas.md — Candidates 02, 03, 06 in this scouting pass (parent assembles and renumbers).
