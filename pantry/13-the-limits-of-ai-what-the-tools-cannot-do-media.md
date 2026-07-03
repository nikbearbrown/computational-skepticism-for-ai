# Media Plan — Chapter 13: The Limits of AI: What the Tools Cannot Do

Zones detected: 21 · video 2 · figure 5 · graph 2 · table 3 · served 7 · dropped 2

Existing media note: chapter already carries 2 CAJAL figures (13.1 accountability chain, 13.2 extended-mind catalog) and 5 styled tables. Cards below cover only unserved zones. Two additional cards (FIGURE 2, GRAPH 1 in the pointers below) are static fallbacks for the two video candidates — build only if the video is not picked.

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Turkey problem — 1,000 days of confirming evidence, catastrophic failure on day 1,001 | PQ/MC | video (Candidate 01; fallback: graph) | 9/10 |
| 2 | Categorical boundary argument — the sample cannot contain what the sampling excluded; scaling enlarges the region but never removes the boundary | VG | figure (FIGURE 1) | Critical |
| 3 | Epic Sepsis Model circular-signal mechanism — model learned to confirm clinical suspicion (blood-culture orders) rather than form it | MC | video (Candidate 02; fallback: figure) | 8/10 |
| 4 | Epic Sepsis internal-vs-external validation gap — marketed performance vs Wong et al. 2021 findings | PQ | graph (GRAPH 2) | Important |
| 5 | Chinese Room setup — person, rulebook, slips, indistinguishable outputs, no understanding | VG | figure (FIGURE 3) | Important |
| 6 | The two-questions gap — the question the system was tested on vs the question the deployment asks; validation scoped only to the first | VG | figure (FIGURE 4) | Important |
| 7 | Rapid-prototyping loop — 6 steps from specify-assumption to deployment decision | MC | figure (FIGURE 5) | Supplementary |
| 8 | Cognitive extremophile profile — superhuman in a narrow niche, weak-to-absent outside it | VG/PQ | figure (FIGURE 6) | Important |
| 9 | Mediocristan vs Extremistan — two data-generating worlds, two epistemic stances | CT | table (TABLE 1) | Important |
| 10 | Five components of the high-stakes engineering practice | EN | table (TABLE 2) | Important |
| 11 | When the limits bite — skepticism as safety mechanism vs skepticism as methodology | CT/DC | table (TABLE 3) | Important |
| 12 | Third calibration baseline — expected trajectory across the three baselines vs the 0.9 target | PQ | graph (GRAPH 3) | Important |

Dropped (not zones): Legg-Hutter definition aside (single citation, prose carries it); "What would change my mind" conditions (argumentative prose, no structure/quantity to show).

## Graph cards

GRAPH 1 — Turkey confidence trajectory: evidence-supported confidence rising for 1,000 days, collapse on day 1,001
Priority: Important (static fallback for video Candidate 01 — build only if the video is not picked)
Reader question: What does it look like when in-distribution evidence supports monotonically rising confidence right up to the moment of catastrophic out-of-distribution failure?
Family + first candidate: time series → line (single series with annotated terminal event)
Data status: illustrative-only possible — the turkey is Taleb's parable, not a dataset; the graph must be labeled as an illustration of the argument, not a measurement
DATA SPEC:
  Unit of observation: one day in the turkey's life
  Fields: day : int (1–1001); confidence_in_benevolence_model : float (monotonically rising, synthetic); event : categorical (routine feeding | Thanksgiving)
  Denominator: counts (index series, no rate)
  Expected n: 1,001 rows
  Likely source: synthetic, constructed per Taleb, The Black Swan (2007), turkey problem
Exclusions: no second series (no "real-world hazard" line — the whole point is the turkey cannot see it); no fat-tail mathematics; no Mediocristan/Extremistan panel (that is TABLE 1's job)

GRAPH 2 — Epic Sepsis Model: performance as marketed/internally validated vs external validation (Wong et al. 2021)
Priority: Important
Reader question: How large is the gap between the performance the vendor reported and the performance found in independent external validation?
Family + first candidate: comparison → paired/grouped bar (metric on x, internal vs external as pair)
Data status: spec needed — the chapter cites Wong et al. 2021 but states no numbers ("performed far worse than marketed, missing a large fraction of sepsis cases while flooding clinicians with alerts"); values must be pulled from the published external validation and vendor documentation before building
DATA SPEC:
  Unit of observation: one validation context × metric
  Fields: context : categorical (vendor-internal | external validation); metric : categorical (AUC, sensitivity/missed-case fraction, alert burden); value : float
  Denominator: hospitalizations in the respective validation cohort (for sensitivity and alert-burden rates)
  Expected n: 2 contexts × 2–3 metrics = 4–6 bars
  Likely source: Wong et al. 2021 (external validation of the Epic Sepsis Model, JAMA Internal Medicine) plus vendor-reported figures as cited there
Exclusions: no hospital-by-hospital breakdown; no timeliness/lead-time analysis; no ROC curves — the reader needs the gap, not the diagnostics; the circular-learning mechanism stays in video Candidate 02 / its fallback figure

GRAPH 3 — Calibration trajectory across the three baselines: expected pattern vs the 0.9 target
Priority: Important
Reader question: What shape should my own calibration trajectory have across the three baselines (Ch. 2 → Ch. 4 → Ch. 13), and how far does even the improved endpoint sit below the 0.9 target?
Family + first candidate: time series → range/band plot (three ordinal baseline points, expected-range band per point, horizontal reference line at 0.9)
Data status: illustrative-only possible — the chapter EXPLICITLY flags the ranges (0.4–0.6 → 0.6–0.75 → 0.7–0.85) as an [verify] expected pattern with "no data source behind the exact numbers"; the graph MUST carry that caveat visibly (label bands "expected pattern — illustrative") and show shape, not authoritative values. Upgrades to "provided" only if the course collects real cohort hit-rates.
DATA SPEC:
  Unit of observation: one calibration baseline administration (cohort-level)
  Fields: baseline : ordinal (1 = Ch. 2, 2 = Ch. 4, 3 = Ch. 13); expected_low : float; expected_high : float; target : float (0.9 constant); career_norm_low/high : float (0.5–0.7, the "most engineers" band, optional)
  Denominator: fraction of 90% confidence intervals containing the truth
  Expected n: 3 baseline points (+1 reference line, +1 optional norm band)
  Likely source: none — book's own illustrative ranges; real data only if instructor collects student baseline scores
Exclusions: no fabricated individual-student trajectories; no Brier/ECE side-panels; do not present the ranges as measured findings — the book's own caveat is part of the graph

## Table cards

TABLE 1 — Mediocristan vs Extremistan: two data-generating worlds, two epistemic stances
Heuristic: CT
Priority: Important
Reader question: Which world does my deployment live in, and what does that world do to the meaning of my validation metrics?
Proposed shape: 6 × 3, class: comparison-table
Rows: outlier influence on the average; effect of one more observation; epistemic stance rewarded; example domains; what high in-sample accuracy predicts; turkey risk for a validator
Columns: dimension | Mediocristan | Extremistan
Exclusions: power-law/fat-tail mathematics stays out; Taleb's other categories stay out; the turkey narrative itself stays in prose (and in video Candidate 01)

TABLE 2 — The five components of the engineering practice for high-stakes deployments
Heuristic: EN
Priority: Important
Reader question: What are the five things a supervisor must build when the categorical limits bite, and what does each look like when it is a fiction rather than a practice?
Proposed shape: 5 × 3, class: infographic-table
Rows: specify what can/cannot be tested; maintain human oversight where limits bite; build the override infrastructure; make limits visible to affected parties; have a stop condition
Columns: component | what it demands in practice | failure mode when absent (e.g., "override as documentation fiction", "refusal assumed away") — chapter states the failure mode explicitly for override and stop condition; mark the others [verify]
Exclusions: the limit-by-limit oversight detail (meaning/intentionality/gap) stays in prose; the open-problem status of "make limits visible" is a footnote, not a column

TABLE 3 — When the limits bite: skepticism as methodology vs skepticism as safety mechanism
Heuristic: CT/DC
Priority: Important
Reader question: For a proposed deployment, which regime am I in — skepticism as methodology or skepticism as the safety mechanism?
Proposed shape: 5 × 3, class: comparison-table
Rows: deployment-context specification; size and monitorability of the data-world gap; interpretation burden on outputs; consequence structure (Mediocristan-like vs Extremistan-like); anchor examples (manufacturing-line classifier vs clinical/AV/judicial/agentic/unbounded-LLM)
Columns: criterion | limits largely irrelevant (methodology) | limits bite (safety mechanism)
Exclusions: do not pre-build Exercise 11's full reusable rubric — stay with the chapter's stated contrasts and mark inferred cells [verify]; the five-component practice is TABLE 2's job

## Served zones
- SERVED — Three categorical limits overview (limit / meaning / why scaling fails / operational consequence): the chapter's 4-column limits table serves it well.
- SERVED — Turing vs Searle (claims, non-claims, common misreadings): the 4-column argument-comparison table serves it well.
- SERVED — AI's genuine strengths (retrieval/synthesis, generation, pattern recognition): strengths table with best-use column.
- SERVED — AI's structural weaknesses (problem formulation, plausibility auditing, interpretive judgment): weaknesses table with why-structural column.
- SERVED — Three-tier delegation map (delegate freely / with verification / do not delegate): delegation table.
- SERVED — Accountability chain (human picks up answerability at the checking instruments): Figure 13.1.
- SERVED — Extended-mind catalog (tool extends capacity, mind supplies judgment): Figure 13.2.

No SERVED-POORLY findings: the five existing tables are each doing a table's job (contrast/lookup), and neither existing figure is overloaded.

## Pointers
- Figure cards: pantry/13-the-limits-of-ai-what-the-tools-cannot-do-cajal.md
- Video candidates from this chapter: vids/video-ideas.md (Candidates 01, 02 as numbered in this pass — parent renumbers at assembly)
