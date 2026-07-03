# Media Plan — Chapter 1: The Skeptic's Toolkit

Zones detected: 12 · video 3 · figure 0 · graph 2 · table 0 · served 6 · dropped 1

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Epic Sepsis Model external validation: 2-in-3 missed, 18% of all patients alerted | PQ | graph | Critical |
| 2 | Turkey problem — confidence rises on correlation while the mechanism is invisible | MC | video | 8/10 |
| 3 | Solve–verify asymmetry inverts in AI deployment (production cheap, verification dear) | MC/PQ | video | 8/10 |
| 4 | Fluency trap — form boosts trust in the output AND in your own evaluation of it | MC | video | 7/10 |
| 5 | Google Flu Trends over-predicted flu in 100 of 108 weeks vs CDC ground truth | PQ | graph | Important |
| 6 | Cartesian doubt as an inspection protocol / three-move checklist | MC | SERVED | — |
| 7 | Plato's Cave — artifact vs world vs relationship (COVID X-ray shortcuts) | VG | SERVED | — |
| 8 | Five Supervisory Capacities (definition, failure mode, chapter mapping) | EN | SERVED | — |
| 9 | Popper demarcation — rhetorical claim vs falsifiable engineering claim | CT | SERVED | — |
| 10 | Institutional skepticism — where the moves live in a workflow | MC | SERVED | — |
| 11 | Solve/verify cost magnitudes as a bar chart | PQ | SERVED-POORLY | — |
| 12 | Knight Capital deployment sequence (8 servers, stale flag, dead code) | MC | dropped — prose narrates the sequence cleanly; chapter already at 7 figures | — |

## Graph cards

GRAPH 1 — The sepsis model's alert flood vs its misses, at population scale
Priority: Critical
Reader question: Out of all hospitalized patients, how large is the set the model alerted on, how small is the set that actually developed sepsis, and how little do the two sets overlap?
Family + first candidate: part-to-whole → icon array/waffle (10,000-patient grid: alerted, septic-and-caught, septic-and-missed), fallback proportional stacked bar
Data status: spec needed (headline rates provided — sensitivity 33%, alert rate 18%, n = 27,697 are stated in the chapter from Wong et al. 2021; exact 2×2 counts / PPV must be pulled from the paper's tables, not inferred)
DATA SPEC:
  Unit of observation: one hospitalized patient in the external-validation cohort
  Fields: alerted : bool, developed_sepsis : bool, count : int (aggregated 2×2)
  Denominator: all 27,697 hospitalized patients in the Michigan cohort
  Expected n: 4 cells (2×2), rendered as ~10,000 scaled icons
  Likely source: Wong et al., JAMA Internal Medicine 181(8), 2021, results tables
Exclusions: no AUC discussion, no vendor-vs-external metric comparison table, no threshold-sweep curve — one population, one snapshot. Note: this is the book's opening case and recurs in Ch. 2; build once, reference twice.

GRAPH 2 — Google Flu Trends drifting confidently away from CDC reality
Priority: Important
Reader question: How far, and for how many consecutive weeks, did the confident model's estimate run above what actually happened?
Family + first candidate: time series → dual line (GFT estimate vs CDC ILI rate, Aug 2011–Sep 2013), over-prediction band shaded
Data status: spec needed (the chapter states 100 of 108 weeks over-predicted and ~2× at the 2012–13 peak, from Lazer et al. 2014; weekly series must be sourced — CDC FluView is public, archived GFT estimates exist)
DATA SPEC:
  Unit of observation: one epidemiological week
  Fields: week : date, gft_estimate : float (% ILI), cdc_actual : float (% ILI)
  Denominator: % of physician visits that are influenza-like illness
  Expected n: ~108 weeks
  Likely source: Lazer, Kennedy, King & Vespignani, Science 2014 supplementary data; CDC FluView; archived Google Flu Trends estimates
Exclusions: no Zillow subplot (keep prose), no search-query mechanics, no post-2013 GFT revisions — the two-year divergence window only

## Table cards

None. The chapter's two structural tables (Popperian corrections; Five Capacities) already do the contrast work; no unserved lookup zone found.

## Served zones
- SERVED — Cartesian doubt protocol / three-move checklist: Fig 1.1 and Fig 1.3
- SERVED — Turkey confidence timeline (static): Fig 1.2 (video card adds the motion; static need is met)
- SERVED — Artifact vs world two-column split: Fig 1.4
- SERVED — Five Supervisory Capacities: full comparison table with failure modes and chapter map
- SERVED — Rhetoric vs falsifiable claim: comparison table
- SERVED — Institutional skepticism workflow: Fig 1.7
- SERVED — Fluency trap two-stage mechanism (static): Fig 1.6
- SERVED-POORLY — Solve/verify cost asymmetry (Fig 1.5, "Cost asymmetry bar chart"): a bar chart implies measured magnitudes, but the costs here are illustrative ("fractions of a cent" vs "an hour of senior labor") — in a book that warns against decorative numbers, a quantitative-looking chart of unmeasured values is the wrong register; suggest figure (schematic, non-quantitative seesaw/balance) or an explicit "illustrative" label. Video Candidate on the same zone covers the motion version.

## Pointers
- Figure cards: none (no pantry/01-the-skeptics-toolkit-cajal.md — chapter is figure-saturated; no unserved static zone justified a new figure)
- Video candidates from this chapter: vids/video-ideas.md — "The turkey with a spreadsheet" (8), "The asymmetry that flips" (8), "Fluency is the trap" (7)
