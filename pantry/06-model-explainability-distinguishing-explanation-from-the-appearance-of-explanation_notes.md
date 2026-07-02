# Research Notes: Chapter 06 — Model Explainability: Distinguishing Explanation from the Appearance of Explanation
**Corresponding chapter:** chapters/06-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md · **Editor note:** notes/06-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md · **Generated:** 2026-07-01

## Chapter summary
The chapter teaches the Shapley mathematics rigorously and then argues the mathematics is epistemically insufficient: a technically accurate feature attribution describes the model, not the world, and can be practically misleading in exactly the high-stakes cases where explanation is most needed. It fuses a full Shapley derivation (four axioms, worked loan example) with a Pearl-rung argument that SHAP operates at Rung 1 (association), and a Wittgensteinian language-game reading of the "Ash agent" deletion case. Core thesis: a correct explanation of the model's internal accounting does epistemic work it cannot warrant.

## A. Load-bearing claims → sources
- **Claim:** The Shapley value is the unique attribution satisfying its axioms (Efficiency/Symmetry/Dummy/Additivity), derived axiomatically. · **Source:** L. S. Shapley, "A Value for n-Person Games," in Kuhn & Tucker (eds.), *Contributions to the Theory of Games II*, Princeton Univ. Press, 1953, pp. 307–317 · primary · **Verdict:** CONFIRMED — Shapley derives a unique value from a small axiom set. Note on the editor's flag: in the cooperative-game literature the fourth classical axiom is **Additivity** (sometimes stated as **Linearity** in the more general linear-operator form). They are related; the chapter should use one name or note the equivalence explicitly (editor priority fix #1). Both names are legitimate in the literature — this is a naming reconciliation, not a factual error.

- **Claim:** SHAP unifies additive feature-attribution methods and is the unique additive attribution meeting local accuracy / missingness / consistency, grounded in Shapley values. · **Source:** Scott M. Lundberg & Su-In Lee, "A Unified Approach to Interpreting Model Predictions," *Advances in Neural Information Processing Systems 30 (NeurIPS/NIPS 2017)*, pp. 4765–4774 (arXiv:1705.07874) · primary · **Verdict:** CONFIRMED — This is the SHAP origin paper; "Efficiency" in Shapley terms corresponds to SHAP's local-accuracy property (attributions sum to the prediction deviation from baseline). The worked example's Σφ = prediction − baseline is the local-accuracy/Efficiency claim and is mathematically correct.

- **Claim:** Local surrogate explanations (LIME) approximate any classifier locally with an interpretable model; explanation is model-agnostic and local. · **Source:** Marco Tulio Ribeiro, Sameer Singh & Carlos Guestrin, "'Why Should I Trust You?': Explaining the Predictions of Any Classifier," *Proc. 22nd ACM SIGKDD (KDD 2016)*, pp. 1135–1144, DOI:10.1145/2939672.2939778 (arXiv:1602.04938) · primary · **Verdict:** CONFIRMED — LIME is correctly characterized as local + model-agnostic surrogate fitting.

- **Claim:** In high-stakes settings one should prefer inherently interpretable models over post-hoc explanations of black boxes; explaining black boxes can perpetuate harm. · **Source:** Cynthia Rudin, "Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead," *Nature Machine Intelligence* 1:206–215, 2019, DOI:10.1038/s42256-019-0048-x · primary · **Verdict:** CONFIRMED — Directly supports the chapter's "appearance of explanation" thesis and the transparency/explainability/interpretability trichotomy. Recommend citing where the trichotomy lands.

- **Claim:** SHAP explains the model, not the world — feature attributions are associative (Pearl Rung 1), not causal; the marginal-vs-conditional choice creates off-manifold ("Frankenstein") instances. · **Source:** Pearl rungs — Judea Pearl & Dana Mackenzie, *The Book of Why*, Basic Books, 2018 (ladder of causation); the marginal/conditional SHAP problem — Lundberg & Lee 2017 plus follow-ups (e.g., Aas, Jullum & Løland, "Explaining individual predictions when features are dependent," *Artificial Intelligence* 298:103502, 2021, DOI:10.1016/j.artint.2021.103502) · primary/secondary · **Verdict:** CONFIRMED for the associative-not-causal claim (SHAP is a function of the trained model's input–output behavior, no interventional semantics). The marginal-vs-conditional (interventional vs observational) distinction and the off-manifold sampling concern are documented in the dependence literature (Aas et al. 2021) — recommend citing it for the "Frankenstein instances" claim rather than asserting it.

- **Claim:** Wittgenstein's "language games" explain why a correct model self-report can mislead a human reader (their language game differs from the model's). · **Source:** Ludwig Wittgenstein, *Philosophical Investigations*, 1953 (language-games, §7 and passim) · primary · **Verdict:** CONFIRMED as a real, correctly attributed concept. Its application to model self-report is the chapter's own argument (legitimate but original) — frame as the author's reading, not as Wittgenstein's claim.

## B. Resolving the editor's [verify] flags
- **[verify and update] "What would change my mind" — causal feature-importance work.** → PARTIALLY RESOLVED. Real, current strands to cite: causal/Shapley-flavored attribution such as Janzing, Minorics & Blöbaum, "Feature relevance quantification in explainable AI: A causal problem," *AISTATS 2020* (arXiv:1910.13413), and Heskes et al., "Causal Shapley Values," *NeurIPS 2020* (arXiv:2011.01625). Confirms causal feature-importance is an active area; specific 2026 state-of-the-art still [UNVERIFIED] and should be refreshed at publication.

- **Radiologist / benign-biopsy case — unsourced, load-bearing.** → [UNVERIFIED]. No public source located; presented as a bare clinical anecdote. The general phenomenon (shortcut learning / spurious features in medical imaging) is real and citable — e.g., Geirhos et al., "Shortcut Learning in Deep Neural Networks," *Nature Machine Intelligence* 2:665–673, 2020, DOI:10.1038/s42256-020-00257-z; and DeGrave, Janizek & Lee, "AI for radiographic COVID-19 detection selects shortcuts over signal," *Nature Machine Intelligence* 3:610–619, 2021, DOI:10.1038/s42256-021-00338-7. Recommend either labeling the opening a composite or grounding it in these real shortcut-learning findings. NEVER cite the specific anecdote as sourced.

- **Ash / Proton deletion case — factual claims (persistence on Proton's servers, backups, recovery window) with no on-page source.** → RESOLVED to a real study: Natalie Shapira et al., *Agents of Chaos*, 2026 (agentsofchaos.baulab.info; arXiv:2602.20021) — a 14-day live red-teaming study of six autonomous agents including "Ash" (running Kimi K2.5). The chapter should carry the citation on-page rather than pointing "backward to an earlier chapter." The specific Proton backup/recovery mechanics should be verified against the paper's case write-up before publication — [UNVERIFIED] at the mechanic level pending a read of the primary.

- **"shap package uses 10 permutations by default" and TreeSHAP complexity O(TLD).** → [UNVERIFIED] on the exact default (implementation defaults drift across versions; the editor is right that it will age). TreeSHAP polynomial-time complexity is real: Lundberg et al., "From local explanations to global understanding with explainable AI for trees," *Nature Machine Intelligence* 2:56–67, 2020, DOI:10.1038/s42256-019-0138-9 (TreeSHAP is O(TLD²) in the original statement — verify the exact exponent against the paper before printing O(TLD)). Recommend citing the Nature MI trees paper and pinning any default to a stated shap version.

## C. Domain examples / cases (real, cited)
- **Loan Shapley worked example** — internally consistent with Efficiency/local-accuracy (Σφ = 0.17 = prediction − baseline); grounded in Shapley 1953 + Lundberg & Lee 2017.
- **Medical-imaging shortcut learning** (Geirhos et al. 2020; DeGrave et al. 2021) — real, citable grounding for the radiologist "confident in the wrong direction" phenomenon.
- **Agents of Chaos / "Ash"** (Shapira et al. 2026) — real study behind the deletion/language-game case; the "the agent did not lie" reading maps onto a documented agent.
- **Feature-dependence problem in SHAP** (Aas, Jullum & Løland 2021) — real support for marginal-vs-conditional / off-manifold "Frankenstein" instances.

## D. Open flags (still [UNVERIFIED])
1. Radiologist/benign-biopsy opening — no source; label composite or ground in shortcut-learning literature.
2. Ash/Proton specific mechanics (backups, recovery window) — verify against the *Agents of Chaos* primary before printing.
3. "shap uses 10 permutations by default" — version-dependent; pin to a stated version or drop.
4. TreeSHAP complexity exponent — confirm O(TLD) vs O(TLD²) against Lundberg et al. 2020.
5. Additivity vs Linearity axiom naming — reconcile (editor fix #1); factual reconciliation, not a citation.
6. "The case where we most need the explanation is exactly where the model is misaligned" — aphorism, asserted not argued; no source establishes the co-occurrence.

## Sources
Primary:
- Shapley, L. S. (1953). A Value for n-Person Games. In *Contributions to the Theory of Games II*, Princeton Univ. Press, 307–317.
- Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why Should I Trust You?": Explaining the Predictions of Any Classifier. *KDD 2016*, 1135–1144. DOI:10.1145/2939672.2939778 · arXiv:1602.04938
- Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. *NeurIPS 2017*, 4765–4774. arXiv:1705.07874
- Rudin, C. (2019). Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead. *Nature Machine Intelligence* 1:206–215. DOI:10.1038/s42256-019-0048-x
- Lundberg, S. M., et al. (2020). From local explanations to global understanding with explainable AI for trees. *Nature Machine Intelligence* 2:56–67. DOI:10.1038/s42256-019-0138-9
- Aas, K., Jullum, M., & Løland, A. (2021). Explaining individual predictions when features are dependent. *Artificial Intelligence* 298:103502. DOI:10.1016/j.artint.2021.103502
- Geirhos, R., et al. (2020). Shortcut Learning in Deep Neural Networks. *Nature Machine Intelligence* 2:665–673. DOI:10.1038/s42256-020-00257-z
- DeGrave, A. J., Janizek, J. D., & Lee, S.-I. (2021). AI for radiographic COVID-19 detection selects shortcuts over signal. *Nature Machine Intelligence* 3:610–619. DOI:10.1038/s42256-021-00338-7
- Wittgenstein, L. (1953). *Philosophical Investigations.* Blackwell.
- Shapira, N., et al. (2026). Agents of Chaos. https://agentsofchaos.baulab.info/ · arXiv:2602.20021

Secondary / adjacent:
- Pearl, J., & Mackenzie, D. (2018). *The Book of Why.* Basic Books. (ladder of causation)
- Janzing, D., Minorics, L., & Blöbaum, P. (2020). Feature relevance quantification in explainable AI: A causal problem. *AISTATS 2020.* arXiv:1910.13413
- Heskes, T., et al. (2020). Causal Shapley Values. *NeurIPS 2020.* arXiv:2011.01625
