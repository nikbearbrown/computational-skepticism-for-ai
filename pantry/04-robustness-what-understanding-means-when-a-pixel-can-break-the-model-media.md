# Media Plan — Chapter 4: Robustness: What "Understanding" Means When a Pixel Can Break the Model

Zones detected: 15 · video 2 · figure 0 · graph 1 · table 0 · served 9 · dropped 3

(The graph card replaces a SERVED-POORLY zone — Fig 4.6 — counted once, under graph.)

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Linearity hypothesis — per-coordinate ε-pushes accumulate to ε‖w‖₁ across thousands of dimensions | MC | video | 9/10 (static already SERVED by Fig 4.3) |
| 2 | Non-robust features — supervised loss can't tell robust from brittle features, so it bets on whichever predicts better | MC | video | 8/10 (static already SERVED by Fig 4.9) |
| 3 | Robustness scaling law — power-law gains plateau near 90%, where human accuracy on the fooling set also plateaus | PQ | graph (replaces Fig 4.6, SERVED-POORLY) | Important |
| 4 | Panda→gibbon flip under imperceptible perturbation | VG | SERVED | — |
| 5 | "Fragile" framing vs "learned a proxy" framing → different engineering responses | CT | SERVED | — |
| 6 | Six attack classes and what each targets | CT | SERVED | — |
| 7 | Adversarial robustness and distribution-shift robustness are separate axes | VG | SERVED | — |
| 8 | Robustness toolkit — what each tool does, costs, cannot do | SP | SERVED | — |
| 9 | Randomized smoothing — majority vote over thousands of noisy copies | MC | SERVED | — |
| 10 | Boundary tilting — decision boundary tangent to the manifold in low-variance directions | VG | SERVED | — |
| 11 | Same proxy-attack structure across image / NLP / tabular / agentic domains | CT | SERVED | — |
| 12 | Prompt sensitivity as instruction-layer adversarial robustness | MC | SERVED | — |
| 13 | Pearl's Ladder — Rung 3 opened, not closed | VG | SERVED | — |
| 14 | Honest robustness disclosure — profile / residual risk / monitoring | SP | SERVED | — |
| 15 | Identity spoofing (Case #8) as a video of its own | MC | dropped | analogy is an arrangement claim, not a transition; Fig 4.12 + cross-domain table serve it; Ch8 deepens it |
| — | PGD projection iteration as a figure | MC | dropped | equation + Fig 4.3 suffice; FGSM is the one-step special case |
| — | Certified radius formula R = (σ/2)(Φ⁻¹(pA) − Φ⁻¹(pB)) as a figure | PQ | dropped | Fig 4.7 carries the mechanism; the formula is lookup math, prose fine |

## Graph cards

```
GRAPH 1 — Adversarial robustness vs scale: the ~90% semantic plateau
Priority: Important
Reader question: Does robust accuracy keep climbing with model/data scale, or bend into a plateau — and where does the human ceiling on the same fooling set sit relative to it?
Family + first candidate: relationship→line (robust accuracy vs compute or model scale, log x-axis; measured points + power-law fit + horizontal human-ceiling reference band near 90%)
Data status: spec needed — real curves exist in Bartoldson et al., ICML 2024 (arXiv:2404.09349). The chapter confirms the 90% plateau and its semantic cause from the abstract but explicitly flags the 10^30-FLOPs extrapolation as [verify]: it must NOT be plotted as data (at most an annotation clearly marked as an unverified extrapolation, and preferably omitted until the book's own [verify] is resolved).
DATA SPEC:
  Unit of observation: one trained model configuration (or one point on the paper's scaling fit)
  Fields: compute_or_params : number (log scale); robust_accuracy : percent; series : {measured, power-law fit, human ceiling}
  Denominator: robust accuracy = correctly classified / evaluated CIFAR-10 images at the fixed L∞ perturbation budget used in the study
  Expected n: ~10–40 points plus fit line, single dataset (CIFAR-10, L∞)
  Likely source: digitized from Bartoldson, Diffenderfer, Parasyris, Kailkhura, "Adversarial Robustness Limits via Scaling-Law and Human-Alignment Studies," ICML 2024 figures
Exclusions: clean-accuracy curves; other datasets or norms; the 10^30 FLOPs figure as a plotted value; any defense-comparison overlay (the toolkit table owns that).
```

## Table cards

None. The chapter's contrast chains are already carried by four strong styled tables (attack taxonomy, toolkit, cross-domain proxy structure, robustness-profile template) — adding more would dilute them.

## Served zones
- SERVED — Panda→gibbon flip: Fig 4.1 side-by-side comparison with a caption that does real work.
- SERVED — Fragile vs proxy framings: Fig 4.2 two-column comparison diagram.
- SERVED — Boundary tilting: Fig 4.4 geometric diagram.
- SERVED — Adversarial vs distribution-shift axes: Fig 4.5 two-axis diagram.
- SERVED — Attack taxonomy: existing 6×5 styled table.
- SERVED — Robustness toolkit costs/limits: existing 6×4 styled table (with honest [verify] on the "≈9×" cost).
- SERVED — Randomized smoothing vote: Fig 4.7.
- SERVED — Cross-domain proxy structure + identity spoofing: 4×5 styled table plus Fig 4.12.
- SERVED — Prompt sensitivity: Fig 4.10; Pearl's Ladder Rung 3: Fig 4.11; verification scope: Fig 4.8; disclosure profile: the inline three-section template (a table is the right medium here — the chapter's own point is "a profile is a table, not a sentence").
- SERVED-POORLY — Robustness scaling plateau: Fig 4.6 renders a load-bearing quantitative claim (power-law growth, plateau, human ceiling) as a static illustrative line-chart image. This is a graph's job: the shape of the curve IS the argument, the real data exists in the cited paper, and the book has zero d3 graphs anywhere. Suggest graph — see GRAPH 1.

## Pointers
- Figure cards: none for this chapter (no pantry/04-…-cajal.md written; all structural zones already figured).
- Video candidates from this chapter: vids/video-ideas.md (Candidates: "Why an Invisible Change Can Flip a Model's Mind", "The Model That Called a Panda a Gibbon Wasn't Broken" — numbering assigned at book assembly)
