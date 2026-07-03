# CAJAL Figure Plan — Chapter 10: Visualization Under Validation: Honest, Misleading, and the Choices Between

FIGURE 1 — Cleveland-McGill perception hierarchy as a ranked ladder
Heuristic: VG
Priority: Important
Concept (one sentence): Visual channels transmit quantity with decreasing accuracy in a fixed order — position on a common scale, length, angle/slope, area, volume, color — and picking a chart type is picking a rung.
Reader/audience: engineer who has read the numbered list; needs the ordering as a pin-up reference.
Type: hierarchy
Components (6): the six rungs top-to-bottom, each with a thumbnail example chart — dot plot (position), bar chart (length), pie (angle), bubble (area), 3D bar (volume), heat swatch (color).
Exclusions: NO numeric error rates — the chapter flags the commonly quoted percentages [verify] and states the ordering is the durable result; no Cleveland-McGill experimental design; no uncertainty-technique content. (Corrects the authorial placeholder <!-- FIGURE 10.A -->, which asked for an error-rate axis.)

FIGURE 2 — Visual weight: uncertainty as decoration vs uncertainty as finding
Heuristic: VG
Priority: Important
Concept (one sentence): A bold "94.3% accuracy" with a thin error bar argues "this is the answer, with a quibble," while the same estimate rendered at equal visual weight with its 91–97% (95% CI) range argues "the uncertainty is part of the finding."
Reader/audience: engineer who defaults to headline-metric dashboards.
Type: comparison panels
Components (5): left panel — big bold central estimate, thin gray error bar; right panel — estimate and interval at equal weight; annotation naming what the left version demotes; the two headlines; one caption line. (Numbers are the chapter's own illustrative example.)
Exclusions: no catalog items beyond visual weight; no calibration-curve content; no quantile dotplot (FIGURE 4's job). (Implements the authorial placeholder <!-- FIGURE 10.2 -->.)

FIGURE 3 — Where does the uncertainty go? The disclosure decision tree
Heuristic: MC
Priority: Important
Concept (one sentence): Two questions route the disclosure — does knowing the uncertainty materially change the conclusion (yes → prominent in the chart), and if not, would a serious reader need it to evaluate the work (yes → caption/footnote, no → methodology appendix) — with the hostile reader as the test.
Reader/audience: engineer deciding where a CI or proxy caveat belongs.
Type: process flowchart / decision tree
Components (5): entry question; yes-branch → "prominent in chart"; no-branch → second question; yes → "visible caption/footnote"; no → "methodology appendix"; caption line "Hierarchy is not hiding — the test is the hostile reader."
Exclusions: the three worked examples (Catalonia, hurricane cone, calibration curve) stay in prose. (Implements the authorial placeholder <!-- FIGURE 10.B -->.)

FIGURE 4 — The same 20% risk, three encodings
Heuristic: VG
Priority: Important
Concept (one sentence): One 20% failure probability shown as a bold percentage with a thin CI bar, as a shaded confidence band, and as a quantile dotplot (20 dots, 4 filled) with a one-line natural-frequency narration — the dotplot moves the encoding to position and count, the channels lay readers actually decode.
Reader/audience: engineer choosing an uncertainty display for a non-technical committee (mirrors Exercise 5).
Type: comparison panels
Components (4): the three encodings side by side + the natural-frequency sentence under the dotplot ("Out of 20 deployments like this one, expect about 4 failures").
Exclusions: no Gigerenzer breast-cancer worked numbers (chapter marks the phrasing approximate); no HOPs/animation; no perception-hierarchy ladder (FIGURE 1's job).
Note: this figure is the static fallback for video Candidate 04.

FIGURE 5 — Anatomy of an honest chart frame
Heuristic: VG
Priority: Supplementary
Concept (one sentence): The epistemic disclosures live inside the chart frame — title states the question, subtitle states the answer, a specific source line is the warrant, a three-sentence methods note names the choices, and a proxy is named as a proxy in the title.
Reader/audience: engineer who treats source lines as footer decoration.
Type: annotated example
Components (5): title slot ("the question"); subtitle slot ("the answer"); in-frame source line with a vague-vs-specific pair ("World Bank data" vs the full indicator citation); methods note ("binned / smoothed / excluded"); proxy-naming label ("News-story counts about kidnappings," not "Kidnappings").
Exclusions: no GDELT Nigeria retelling beyond the one proxy label; no full Evergreen–Emery checklist; no uncertainty encodings.

Recommended: 5 figures, Mixed density. (Four of the five implement or correct figure placeholders the author already left in the chapter as HTML comments.)
