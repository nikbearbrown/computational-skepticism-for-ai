# CAJAL Figure Plan — Chapter 7: Fairness Metrics: Choosing a Definition and Defending It

FIGURE 1 — Same equation, opposite guarantee: the similarity metric d decides
Heuristic: VG
Priority: Important
Concept (one sentence): Two loan applicants identical on every financial feature but zip code pass through the same Lipschitz condition twice — once with d ignoring zip code (outputs forced together) and once with d encoding it (outputs free to diverge) — showing that the fairness guarantee lives entirely in the choice of d.
Reader/audience: has just met the (D, d)-Lipschitz inequality in this section; comfortable with distance-as-similarity intuition; no measure theory assumed.
Type: comparison panels
Components (5):
  1. The applicant pair — matched feature stack (credit history, income, DTI) plus a differing zip-code badge
  2. Panel A: d defined on financial variables only → d(x,y) small → M(x), M(y) clamped together (treated alike)
  3. Panel B: d encodes zip-code distance → d(x,y) large → M(x), M(y) permitted to diverge (different treatment allowed)
  4. The shared inequality D(M(x), M(y)) ≤ d(x, y) spanning both panels — same equation, both times
  5. One-line takeaway strip: "the values choice is d — it precedes the math"
Exclusions: no total-variation formula, no FTA-vs-FTU contrast, no computational-hardness aside, no proxy-reconstruction discussion

Note: this card is the suggested rework for the zone Figure 7.2 currently holds (placeholder caption "Illustration"). Do not modify Fig 7.2 directly.

Recommended: 1 figure, Mixed density. (Chapter already carries 7 CAJAL figures; this is the only unserved or mis-served figure zone.)
