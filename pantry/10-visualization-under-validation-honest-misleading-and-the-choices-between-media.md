# Media Plan — Chapter 10: Visualization Under Validation: Honest, Misleading, and the Choices Between

Zones detected: 19 · video 3 · figure 5 · graph 2 · table 3 · served 3 (+1 served-poorly) · dropped 3

Note for the builder: this chapter contains four authorial HTML placeholders (`<!-- FIGURE 10.0 -->`, `<!-- FIGURE 10.A -->`, `<!-- FIGURE 10.B -->`, `<!-- FIGURE 10.1 -->`, `<!-- FIGURE 10.2 -->`) that were planned but never rendered. The cards below inherit and, where needed, correct those specs — they are NOT served, since nothing is rendered. Also: "Sankov and alluvial diagrams" in the Flow family is a typo for **Sankey** — fix when building TABLE 1.

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Reuters inverted-axis chart: murders rose, readers saw a decline | MC | video (Candidate 01) | 9/10 |
| 2 | Same CSV, two dashboards, opposite beliefs — five 30-second choices | MC | video (Candidate 02) | 8/10 |
| 3 | Natural frequencies / quantile dotplot: 20 dots beat "20%" | PQ | video (Candidate 04) | 7/10 |
| 4 | Deceptive-catalog toggle: one dataset with misleading choices switched on/off | PQ | graph (GRAPH 1) | Critical |
| 5 | Challenger: O-ring damage vs temperature, the chart never drawn | PQ | graph (GRAPH 2) | Critical |
| 6 | FT Visual Vocabulary nine question families → chart selection | DC | table (TABLE 1) | Important |
| 7 | Deceptive visualization catalog: honest use vs dishonest use per move | CT | table (TABLE 2) | Critical |
| 8 | Aleatoric uncertainty technique roster: use-when / watch-for | EN | table (TABLE 3) | Important |
| 9 | Cleveland-McGill perception hierarchy as a ranked ladder | VG | figure (FIGURE 1) | Important |
| 10 | Visual weight: uncertainty as decoration vs uncertainty as finding | VG | figure (FIGURE 2) | Important |
| 11 | Disclosure hierarchy decision tree (prominent / caption / appendix) | MC | figure (FIGURE 3) | Important |
| 12 | The same 20% risk in three encodings (static fallback for Candidate 04) | VG | figure (FIGURE 4) | Important |
| 13 | Anatomy of an honest chart frame (title=question, subtitle=answer, source=warrant) | VG | figure (FIGURE 5) | Supplementary |
| 14 | Four cases side by side (Challenger, Catalonia, Reuters, Snow) | CT | SERVED | — |
| 15 | Seven-step working sequence for picking and showing | MC | SERVED | — |
| 16 | Living-deck changelog slide | VG | SERVED | — |
| 17 | McLuhan medium-is-the-message applied to the dashboard | — | dropped | — |
| 18 | GDELT Nigeria "kidnapping rates" proxy case | — | dropped | — |
| 19 | Catalonia poll bars (uncertainty exceeds effect) | — | dropped | — |

## Graph cards

```
GRAPH 1 — The deceptive-catalog toggle: one dataset, misleading choices switched on and off
Priority: Critical
Reader question: How does the same validation result change its apparent meaning as each catalog choice — truncated axis, inconsistent panels, color asymmetry, buried calibration, omitted uncertainty — is flipped on and off?
Family + first candidate: comparison→bar/dot panels with per-catalog-item toggles (honest ↔ misleading state per control); calibration curve as one panel
Data status: illustrative-only possible — the chapter's CSV (94% headline accuracy, three underperforming subgroups, calibration overconfident at high probabilities) is a deliberate authorial construction. The rendered graph MUST label the data "illustrative validation result — constructed for demonstration"; never present it as findings.
DATA SPEC:
  Unit of observation: one subgroup × metric cell of the constructed validation result (plus calibration-bin rows)
  Fields: subgroup : cat; accuracy : float; n : int; ci_low : float; ci_high : float; predicted_prob_bin : float; observed_freq : float
  Denominator: predictions per subgroup; predictions per probability bin for the calibration panel
  Expected n: 4 subgroup rows (overall + 3), ~10 calibration bins
  Likely source: synthesized to match the shape the chapter describes in its opening
Exclusions: dual-axis and 3D moves (keep to 4–5 toggleable choices so each is legible); axis inversion (belongs to the Reuters case, which the chapter explicitly keeps out of the catalog); no implication of a real deployed system
```

```
GRAPH 2 — The Challenger chart that was never drawn: O-ring damage vs launch temperature, untested region included
Priority: Critical
Reader question: Plotted with the untested cold region shaded and the 31°F launch-day forecast marked, is the temperature–damage pattern readable as anything but "do not launch"?
Family + first candidate: relationship→scatter (damage/erosion index vs joint temperature per prior launch), shaded no-data band below the coldest prior launch, vertical marker at the launch-day forecast
Data status: spec needed — the underlying data is real and public (Rogers Commission report; Tufte's reconstruction in Visual Explanations) but must be pulled from source and cited; do not sketch from memory.
DATA SPEC:
  Unit of observation: one shuttle launch prior to STS-51-L
  Fields: flight : id; joint_temp_F : float; damage_index : int (or erosion/blow-by incident count); date : date
  Denominator: counts per launch
  Expected n: ~24 prior launches
  Likely source: Report of the Presidential Commission on the Space Shuttle Challenger Accident (1986); Tufte, Visual Explanations (1997)
Exclusions: the causal-chain narrative (cold → harder rubber → longer seating → blow-by) stays in prose and the case table; the encoding-vs-omission historiography debate (the chapter already adjudicates it, following Tufte)
```

## Table cards

```
TABLE 1 — FT Visual Vocabulary: nine question families as a chart-selection reference
Heuristic: DC
Priority: Important
Reader question: Given the question my chart must answer, which family does it fall in and which chart types belong to that family?
Proposed shape: 9 × 3, class: comparison-table
Rows: Deviation, Correlation, Ranking, Distribution, Change over time, Part-to-whole, Magnitude, Spatial, Flow
Columns: What it answers | Chart types that belong here | Validation-context example
Exclusions: Abela's four-family decision tree (one prose sentence covers it); the pie-chart caution (stays prose). Fix "Sankov" → "Sankey" in the Flow row.
Note: authorial placeholder <!-- FIGURE 10.0 --> already specifies this table; this card confirms it.
```

```
TABLE 2 — The deceptive visualization catalog as an audit checklist
Heuristic: CT
Priority: Critical
Reader question: For each of the ten misleading moves, what is its honest use, its dishonest use, and how do I tell which one I am looking at?
Proposed shape: 10 × 4, class: comparison-table
Rows: truncated axis; inconsistent axes across panels; aggregation hiding distribution; color asymmetry; cherry-picked time windows; scale trickery; chartjunk/3D effects; missing baseline; labels that prejudge; selective uncertainty visualization
Columns: Move | Honest use | Dishonest use | How to tell the difference
Exclusions: axis inversion (the chapter explicitly notes it is NOT a catalog item — it lives in the Reuters case); Tufte's and Cairo's longer lists (named in prose as further reading)
Note: authorial placeholder <!-- FIGURE 10.1 --> already specifies this table; this card confirms it. This is the checklist Exercises 6 and 14 depend on — Critical.
```

```
TABLE 3 — Aleatoric uncertainty techniques: use-when and watch-for
Heuristic: EN
Priority: Important
Reader question: Which uncertainty technique fits my data, audience, and medium — and what is each technique's known failure mode?
Proposed shape: 9 × 4, class: comparison-table
Rows: error bars; confidence-interval bands; fan charts; box plot; violin plot; strip/jittered dot plot; quantile dotplot; hypothetical outcome plots (HOPs); gradient line plots
Columns: Use when | Watch for | Audience fit (lay/expert) | Works in static print?
Exclusions: epistemic-uncertainty practices (different section, different card); exact Gigerenzer worked numbers (chapter marks phrasing as approximate); the hurricane-cone 66% detail beyond one "watch for" cell [verify against NHC wording when building]
```

## Served zones

- SERVED — four cases side by side (Challenger, Catalonia, Reuters, Snow): rendered comparison table with lesson and honest-version columns.
- SERVED — seven-step working sequence: Figure 10.2 (vertical flowchart).
- SERVED — living-deck changelog: Figure 10.1 (mock changelog slide).
- SERVED-POORLY — two-dashboards opening: Figure 10.3 is a static thumbnail, but the zone's teaching is that each ~30-second choice flips the argument on identical data — a static thumbnail cannot show the flip. Suggest video (Candidate 02) or interactive graph (GRAPH 1 covers the same mechanism at the catalog section).
- SERVED-POORLY (latent) — placeholder <!-- FIGURE 10.A --> specifies a "right axis: approximate error rate" for the perception hierarchy, which contradicts the chapter's own [verify] flag on those percentages; FIGURE 1 card corrects the spec (ordering only, no numbers).

Dropped: McLuhan medium-is-message (the opening zone and prose carry it; no independent structure to draw); GDELT Nigeria proxy case (narrative teaches it; its practice content is carded as FIGURE 5); Catalonia poll bars (the chapter itself rules "sometimes the right chart is no chart" and flags the case's primary source as unfound — rendering it would contradict the text).

## Pointers
- Figure cards: pantry/10-visualization-under-validation-honest-misleading-and-the-choices-between-cajal.md
- Video candidates from this chapter: vids/video-ideas.md (Candidates 01, 02, 04)
