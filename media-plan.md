# Media Plan — Computational Skepticism for AI

Media-scout pass, 2026-07-03. One read of chapters 01–13; every high-assertion
zone routed to its best medium. Cards live in `pantry/<chapter>-media.md`
(all zones + graph/table cards), `pantry/<chapter>-cajal.md` (figure cards,
renderer-ready), and `vids/video-ideas.md` (32 video candidates, builder-ready).
The intro (00) and working notes (97-, `_`-prefixed) were not scanned.

The book is already table- and figure-saturated (20–30 styled tables, 2–12
CAJAL figures per chapter) and has **zero rendered graphs** — so the value
here is concentrated in the graph lane (23 cards), the video slate (32), and
a handful of genuine figure gaps (Ch10, Ch13).

## Per-chapter summary

| Chapter | Zones | Video | Figure | Graph | Table | Served | Critical items |
|---|---|---|---|---|---|---|---|
| 01 The Skeptic's Toolkit | 12 | 3 | 0 | 2 | 0 | 6 | Sepsis icon-array graph |
| 02 Probability & Confidence Illusion | 15 | 4 | 0 | 3 | 0 | 8 | — |
| 03 Data Validation | 12 | 1 | 1 | 2 | 1 | 5 | — |
| 04 Robustness | 15 | 2 | 0 | 1 | 0 | 9 | — |
| 05 Model Explainability | 14 | 3 | 0 | 3 | 0 | 6+1p | — |
| 06 Bias | 18 | 3 | 2 | 3 | 1 | 7 | COMPAS graph; ten-mechanisms table |
| 07 Fairness Metrics | 13 | 2 | 1 | 2 | 0 | 8 | — |
| 08 Validating Agentic AI | 18 | 3 | 1 | 0 | 2 | 12 | False-success-catch figure |
| 09 Delegation & Supervision | 12 | 1 | 2 | 1 | 0 | 7 | — |
| 10 Visualization Under Validation | 19 | 3 | 5 | 2 | 3 | 3+1p | Catalog-toggle graph; Challenger graph; deceptive-catalog table |
| 11 Communicating Uncertainty | 18 | 2 | 1 | 2 | 2 | 9 | Epic Sepsis claimed-vs-observed graph |
| 12 Accountability | 18 | 3 | 1 | 0 | 0 | 10 | — |
| 13 The Limits of AI | 21 | 2 | 5 | 2 | 3 | 7 | Categorical-boundary figure; Epic-Sepsis-loop figure |
| **Total** | **205** | **32** | **19** | **23** | **12** | **97+2p** | 10 Critical |

(`+1p` = one SERVED-POORLY finding; details in the chapter's media plan.)

## Critical items (build first)

1. **GRAPH — Sepsis alert flood vs misses, icon array** (Ch1; Wong et al. 2021, data spec needed from paper). The book's opening case; recurs in Ch2 — build once, reference twice.
2. **GRAPH — COMPAS false-positive/false-negative rates by race** (Ch6; ProPublica data, provided, `[verify]` exact rates against primary).
3. **TABLE — Ten bias mechanisms master lookup** (Ch6; currently ~2,500 words of prose with no lookup surface).
4. **FIGURE — The false-success catch: gate → act → verify world state → compare → stop** (Ch8; the chapter's central working skill exists only as scattered prose).
5. **GRAPH — Interactive deceptive-catalog toggle** (Ch10; one illustrative dataset, misleading choices flipped on/off; must carry ILLUSTRATIVE label).
6. **GRAPH — Challenger O-ring damage vs launch temperature** (Ch10; real Rogers Commission data, spec needed).
7. **TABLE — Deceptive visualization catalog as 10×4 audit checklist** (Ch10).
8. **GRAPH — Epic Sepsis: developer-claimed vs externally observed performance** (Ch11; Wong et al. 2021, data provided — the strongest real-data graph in the book).
9. **FIGURE — Categorical boundary schematic: sample vs world** (Ch13).
10. **FIGURE — Epic Sepsis circular-signal loop** (Ch13; build only if video Candidate 25 is not picked).

## Video slate

32 candidates in `vids/video-ideas.md`, ordered by score: 13 at 9/10, 12 at
8/10, 7 at 7/10. Consolidation needed at pick-time (noted in the file
header): Candidates 13/14 are both Taleb's turkey; 01/27 are adjacent Ch2
confidence-arithmetic concepts; 23/25 share the Epic Sepsis case. Budget
guidance from the cajal canon is one video per chapter or thematic cluster —
the 9/10 row alone (one per chapter, no collisions) is a coherent
first-production slate.

## SERVED-POORLY roll-up (existing media doing the wrong job)

- Ch1 Fig 1.5 cost-asymmetry bars: quantitative-looking bars for illustrative
  numbers — schematic or explicit label suggested.
- Ch2 Fig 2.8 calibration curve and Fig 2.10 PPV-vs-base-rate: chart-shaped
  claims shipped as static illustrative PNGs; Fig 2.10 is the book's best
  first-d3 candidate (analytic curve, base-rate slider, zero honesty risk).
- Ch4 Fig 4.6 robustness-scaling plateau: load-bearing quantitative curve as
  static image; d3 replacement specced from Bartoldson et al. 2024.
- Ch7 worked-example tables (calibration vs equalized-odds): tables doing a
  graph's job — paired dumbbell specced, illustrative-labeled.
- Ch10 Fig 10.3 two-dashboards thumbnail: cannot show the choice-by-choice
  flip that is the zone's teaching — video Candidate 22 or the catalog-toggle
  graph.
- Ch11 subgroup-ECE table: magnitude comparison presented as lookup —
  companion dot plot specced; table stays as audit template.
- Ch12 16-row capacity catalog: exceeds comparison span; the prose itself
  concedes it "does not earn its length" — split or trim suggested.

## Editorial flags (not media — fix in text)

- Ch3 Figs 3.1/3.6: captions/alt text are literally "Diagram"/"Illustration".
- Ch5 Fig 5.6: caption truncated to "SHAP vs".
- Ch6: a markdown table is captioned "Figure 6.4", desyncing every later
  figure number from its fig-NN.png filename.
- Ch8: two tables captioned as figures ("Figure 8.4", "Figure 8.9").
- Ch10: five unrendered authorial figure placeholders (`FIGURE 10.0/10.A/
  10.B/10.1/10.2`) — four are implemented by this pass's cards, one
  (10.A error-rate axis) contradicts the chapter's own `[verify]` flag and
  was re-specced as ordering-only. Also "Sankov diagrams" → **Sankey** (typo).
- Ch12: figure numbering skips 12.6 (12.5 → 12.7).

## Data honesty

Graph cards state data status individually. Real-data graphs: Epic Sepsis
(Wong et al. 2021), COMPAS (ProPublica), Literary Digest/Gallup, Challenger
(Rogers Commission), Florida firearm murders (Reuters/Chan 2014), Cleveland
& McGill channel ranking, robustness scaling (Bartoldson et al. 2024).
Everything else is spec-needed or explicitly ILLUSTRATIVE, matching the
book's own no-fabrication policy — several chapters' numbers are flagged
illustrative by the author and the cards preserve those flags.
