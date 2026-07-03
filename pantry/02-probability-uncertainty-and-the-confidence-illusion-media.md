# Media Plan — Chapter 2: Probability, Uncertainty, and the Confidence Illusion

Zones detected: 15 · video 4 · figure 0 · graph 3 · table 0 · served 8 · dropped 0

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | 99%-accurate test on a 1-in-10,000 disease → positive means ~1% (counting bodies) | PQ/MC | video | 9/10 |
| 2 | Heavy tails: the running mean that never settles (Gaussian vs Cauchy) | MC/PQ | video | 9/10 |
| 3 | Agent tool-call chain: "task complete" is a product of shrinking conditionals (0.612 vs 0.729) | MC | video | 7/10 |
| 4 | Temperature scaling: one parameter separates confidence from correctness | MC | video | 7/10 |
| 5 | Calibration curve as the diagnostic (stated confidence vs empirical frequency) | PQ | graph (+ SERVED-POORLY fig 2.8) | Important |
| 6 | PPV as a function of base rate (Glimmer 2.3 curve, where it crosses 50%) | PQ | graph (+ SERVED-POORLY fig 2.10) | Important |
| 7 | Human calibration baseline: engineers' "90%" intervals contain truth ~40–60% | PQ | graph | Supplementary |
| 8 | Three axioms of probability | EN | SERVED | — |
| 9 | Classical / frequentist / Bayesian interpretations | CT | SERVED | — |
| 10 | Conditional probability as a shrunken sample space (flag lowers the estimate) | MC | SERVED | — |
| 11 | Total probability theorem / fleet error-rate partition | MC | SERVED | — |
| 12 | Distribution shift as Hume's induction problem (confidence flat while world moves) | MC | SERVED | — |
| 13 | False-positive structure across domains (fraud, security, moderation, jailbreaks) | EN | SERVED | — |
| 14 | Bayes anatomy (prior/likelihood/posterior/normalizer) | EN | SERVED | — |
| 15 | Four diagnostic questions synthesis | EN | SERVED | — |

## Graph cards

GRAPH 1 — Reliability diagram of a real modern network, before and after temperature scaling
Priority: Important
Reader question: Where does a real model's stated confidence peel off the diagonal, and how much of the overconfidence does a single parameter remove?
Family + first candidate: relationship → paired reliability diagrams (stated confidence bins on x, empirical accuracy on y, diagonal reference; before-T and after-T panels or overlaid lines)
Data status: spec needed (Fig 2.8 is illustrative; real curves exist in Guo et al., ICML 2017, or can be reproduced honestly by running an open pretrained classifier on a labeled held-out set — the chapter's own Glimmer 2.4 pipeline generates exactly this data)
DATA SPEC:
  Unit of observation: one confidence bin (0.0–0.1 … 0.9–1.0)
  Fields: bin_midpoint : float, empirical_accuracy : float, n_in_bin : int, condition : {raw, temperature-scaled}
  Denominator: predictions per bin / all held-out predictions
  Expected n: 10 bins × 2 conditions
  Likely source: Guo, Pleiss, Sun & Weinberger 2017 (arXiv:1706.04599) reliability data, or a reproduction per Glimmer 2.4
Exclusions: no ECE/Brier scores on the chart (Ch. 11's job), no isotonic/Platt comparison, no distribution-shift panel — one model, one fix

GRAPH 2 — Positive predictive value vs base rate for a 99% sensitive/specific test
Priority: Important
Reader question: At what base rate does a positive result become more likely true than false, and how fast does PPV collapse below that?
Family + first candidate: relationship → line on log-x (base rate 1/100,000 → 1/100, PPV on y, 50% crossing annotated); natural first d3 interactive in the book (slider on base rate, optionally sensitivity/specificity)
Data status: provided (analytic — PPV computed directly from Bayes with sens = spec = 0.99; no measurement claimed, none needed)
DATA SPEC:
  Unit of observation: one base-rate value
  Fields: base_rate : float, ppv : float (optional: sensitivity, specificity as parameters)
  Denominator: PPV = true positives / all positives
  Expected n: continuous curve, ~50 sampled points
  Likely source: computed; matches Glimmer 2.3 exactly
Exclusions: no NPV curve, no ROC detour, no multiple-test-repetition scenario — one curve, one crossing point

GRAPH 3 — Where first-attempt forecasters actually land on the 90%-interval test
Priority: Supplementary
Reader question: When people write "90% confidence" intervals, what fraction actually contain the truth — and how far is the crowd from 0.9?
Family + first candidate: distribution → histogram of hit rates with a 0.9 reference line
Data status: illustrative-only possible today (the chapter's "most engineers score 0.4–0.6" is stated without a dataset); becomes real data if collected from the course cohort's own calibration-baseline exercise — that is the honest path and the better one
DATA SPEC:
  Unit of observation: one forecaster (one completed calibration baseline)
  Fields: forecaster_id : anon, n_questions : int, hit_rate : float
  Denominator: intervals containing truth / intervals written
  Expected n: one cohort (~30–200 forecasters)
  Likely source: the book's own calibration-baseline exercise results (returns in Ch. 4 and Ch. 13); published overconfidence studies as backdrop only
Exclusions: no per-domain breakdown, no comparison to superforecasters, no Ch. 13 longitudinal panel yet

## Table cards

None. The chapter's tables (axioms, interpretations, Bayes-term anatomy, machine posteriors, false-positive domains) already cover every lookup/contrast zone.

## Served zones
- SERVED — Three axioms: styled table
- SERVED — Classical/frequentist/Bayesian: comparison table
- SERVED — Conditional probability shrunken-space picture: Fig 2.1 (the counterintuitive flag example is carried fine by the worked prose)
- SERVED — Chain rule / tool-call chain (static): Fig 2.2 probability tree (video card adds the motion)
- SERVED — Total probability partition: Fig 2.3 + fleet worked example + machine table
- SERVED — Base-rate counting picture (static): Fig 2.5 icon array and Fig 2.6 before/after bars (video card adds the motion)
- SERVED — Distribution shift / confidence stays flat: Fig 2.7 (concept video covered by Ch. 1 turkey candidate — do not duplicate)
- SERVED — Heavy-tail regime (static): Fig 2.9 (dynamic version is video Candidate "The average that never settles"; its static fallback is a graph)
- SERVED — False-positive structure across domains: infographic table
- SERVED — Four diagnostic questions: Fig 2.11 diagnostic card
- SERVED-POORLY — Calibration curve (Fig 2.8): a data chart shipped as a static PNG figure with illustrative data, in the section that commands "do not trust a stated probability without seeing its calibration curve" — the book's most chart-shaped claim deserves a real chart on real data; suggest graph (GRAPH 1 above)
- SERVED-POORLY — PPV vs base rate (Fig 2.10): an analytic curve rendered as a static PNG "Line chart" while the caption itself says the shape is the lesson and asks students to predict the crossing point; suggest graph — this is the single best candidate for the book's first d3 interactive (base-rate slider), and the data is analytic so no honesty risk (GRAPH 2 above)

## Pointers
- Figure cards: none (no pantry/02-probability-uncertainty-and-the-confidence-illusion-cajal.md — chapter carries 10 figures already; no unserved static-structure zone found)
- Video candidates from this chapter: vids/video-ideas.md — "Why a 99%-accurate test is wrong about almost everyone it flags" (9), "The average that never settles" (9), "'Task complete' is a claim about a whole chain" (7), "The one-parameter fix that proves the confidence was decorative" (7)
