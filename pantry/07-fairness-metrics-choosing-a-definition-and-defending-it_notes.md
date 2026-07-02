# Research Notes: Chapter 07 — Fairness Metrics: Choosing a Definition and Defending It
**Corresponding chapter:** chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md · **Editor note:** notes/07-fairness-metrics-choosing-a-definition-and-defending-it.md · **Generated:** 2026-07-01

## Chapter summary
The chapter proves that demographic parity, equalized odds, and calibration cannot all hold simultaneously when base rates differ across groups (an impossibility theorem, not a tooling limit), proves it two ways (a PPV identity and Chouldechova's Bayes relation), grounds it in the COMPAS/ProPublica–Northpointe dispute, and then converts the residual statistical result into an irreducible values choice that must be defended in writing. It surveys group, individual, causal, and Generalized-Entropy-Index fairness and specifies a six-step "defended choice" deliverable. Core move: a statistically valid output can still be wrong about the question that matters.

## A. Load-bearing claims → sources
- **Claim:** Calibration/predictive parity and error-rate balance (equalized odds) are mutually incompatible when base rates (prevalence) differ across groups — an impossibility. · **Source:** Alexandra Chouldechova, "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments," *Big Data* 5(2):153–163, 2017, DOI:10.1089/big.2016.0047 (arXiv:1703.00056) · primary · **Verdict:** CONFIRMED — Chouldechova proves that when prevalence differs, a test cannot have equal PPV and equal false-positive/false-negative rates across groups. Her relation v/(1−v) = [p/(1−p)]·(t/f) linking PPV, prevalence, and error rates is exactly the chapter's identity. Directly supports the theorem.

- **Claim:** It is generally impossible to simultaneously satisfy calibration, balance for the positive class, and balance for the negative class except in degenerate cases (equal base rates or perfect prediction). · **Source:** Jon Kleinberg, Sendhil Mullainathan & Manish Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," *ITCS 2017* (LIPIcs vol. 67, 43:1–43:23); arXiv:1609.05807, 2016 · primary · **Verdict:** CONFIRMED — This is the formal impossibility result underpinning the chapter's "triangle." The two escape hatches (equal base rates OR perfect prediction) are stated in the paper; the editor is right that the second is under-emphasized in the chapter.

- **Claim:** Equalized odds / equal opportunity is a coherent group-fairness definition requiring equal TPR (and FPR) across groups, achievable by post-hoc threshold adjustment. · **Source:** Moritz Hardt, Eric Price & Nathan Srebro, "Equality of Opportunity in Supervised Learning," *NeurIPS/NIPS 2016*, pp. 3315–3323 (arXiv:1610.02413) · primary · **Verdict:** CONFIRMED — Origin of "equalized odds" and "equal opportunity"; the post-hoc adjustment method is theirs. Correctly used.

- **Claim:** COMPAS is a real deployed recidivism instrument; ProPublica showed Black defendants were disproportionately false-positive-flagged (~2× FPR), while Northpointe showed the tool was calibrated / had equal PPV — both correct on their own metric. · **Source:** Julia Angwin, Jeff Larson, Surya Mattu & Lauren Kirchner, "Machine Bias," *ProPublica*, May 23, 2016, https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing; methodology: Larson et al., "How We Analyzed the COMPAS Recidivism Algorithm," ProPublica, 2016; Northpointe rebuttal: William Dieterich, Christina Mendoza & Tim Brennan, "COMPAS Risk Scales: Demonstrating Accuracy Equity and Predictive Parity," Northpointe, 2016 · primary (journalism + company technical report) · **Verdict:** CONFIRMED — The dispute is real and the "both correct, measuring different properties" resolution is the standard scholarly reading (Chouldechova 2017 and Kleinberg et al. 2016 formalize why). The specific "~2× FPR" figure is ProPublica's and is reproducible from their public Broward County data (github.com/propublica/compas-analysis) — recommend citing that data anchor in-text.

- **Claim:** Individual fairness = "treat similar individuals similarly," formalized as a Lipschitz condition on a task-specific similarity metric. · **Source:** Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold & Richard Zemel, "Fairness Through Awareness," *ITCS 2012*, pp. 214–226 (arXiv:1104.3913) · primary · **Verdict:** CONFIRMED — Origin of the (D,d)-Lipschitz individual-fairness formulation the chapter uses.

- **Claim:** Counterfactual fairness — a decision is fair if it is unchanged in a counterfactual world where the individual's protected attribute differs; computed via abduction/action/prediction and requires a causal model. · **Source:** Matt J. Kusner, Joshua R. Loftus, Chris Russell & Ricardo Silva, "Counterfactual Fairness," *NeurIPS 2017*, pp. 4066–4076 · primary · **Verdict:** CONFIRMED — Definition, the abduction–action–prediction procedure, and the law-school success application are all in the paper. The chapter's caveat (needs an unverifiable causal model / more knowledge than data provides) is correct and is acknowledged by the authors; the editor's note that its severity is understated is fair.

- **Claim:** The Generalized Entropy Index measures inequality and decomposes into within-group + between-group components, usable as an algorithmic-fairness metric. · **Source:** Till Speicher, Hoda Heidari, Nina Grgić-Hlača, Krishna P. Gummadi, Adish Singla, Adrian Weller & Muhammad Bilal Zafar, "A Unified Approach to Quantifying Algorithmic Unfairness: Measuring Individual & Group Unfairness via Inequality Indices," *KDD 2018* (arXiv:1807.00787) · primary · **Verdict:** CONFIRMED — This paper imports the GEI (originally from the economics inequality literature, e.g., Shorrocks 1980) into fairness and gives the within/between decomposition. Recommend citing it for the GEI section.

## B. Resolving the editor's [verify] flags
The editor notes NO explicit `[verify]` tags in this chapter (cleaner than 5 and 6). Unsourced load-bearing claims flagged:
- **"On most real datasets base rates do differ."** → [UNVERIFIED] as a cited universal, but strongly supported: it is the premise that makes Chouldechova/Kleinberg bite in practice, and differing base rates across groups on real risk data are well documented (COMPAS itself is an instance). Recommend softening to "commonly" or citing COMPAS/empirical fairness surveys rather than asserting universally.
- **The two numeric example tables (calibration-satisfying vs equalized-odds-satisfying).** → INTERNAL, not a citation issue. [UNVERIFIED] as printed — the tables are not shown to actually satisfy the calibration constraint they name. Recommend adding a row demonstrating realized rates match assigned probabilities, or labeling them schematic (editor fix #2). Cannot be resolved by a source; must be shown or labeled.
- **COMPAS "~2× FPR of white defendants."** → RESOLVED to ProPublica (Angwin et al. 2016) and reproducible from the public compas-analysis dataset; add the citation anchor in-text.
- **"Two of the nine Botspeak pillars (Appendix A)."** → Internal forward-reference to the book's own framework; not externally verifiable and not a research item. Flag as book-internal.

## C. Domain examples / cases (real, cited)
- **COMPAS / ProPublica vs Northpointe** (Angwin et al. 2016; Dieterich et al. 2016; formalized by Chouldechova 2017 and Kleinberg et al. 2016) — the field's canonical case; the "both were right, they measured different properties" resolution is the chapter's best move and is well-sourced. Public data: github.com/propublica/compas-analysis.
- **Law-school success prediction** (Kusner et al. 2017) — real worked application of counterfactual fairness.
- **Generalized Entropy Index as fairness metric** (Speicher et al., KDD 2018) — real within/between decomposition instance.

## D. Open flags (still [UNVERIFIED])
1. "On most real datasets base rates do differ" — universalizing premise; soften or cite.
2. The two numeric tables — not shown to satisfy their claimed constraints; demonstrate or label schematic (internal, not sourceable).
3. COMPAS construct tension — re-arrest used as theorem input then disowned as a bad proxy; needs a forward-flag at point of use (editor fix #3). Note: the "re-arrest ≠ the construct society cares about" point is itself well established in the critical-fairness literature.
4. Botspeak pillars — book-internal forward reference, not externally verifiable.

## Sources
Primary:
- Chouldechova, A. (2017). Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments. *Big Data* 5(2):153–163. DOI:10.1089/big.2016.0047 · arXiv:1703.00056
- Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016/2017). Inherent Trade-Offs in the Fair Determination of Risk Scores. *ITCS 2017*, LIPIcs 67, 43:1–43:23. arXiv:1609.05807
- Hardt, M., Price, E., & Srebro, N. (2016). Equality of Opportunity in Supervised Learning. *NeurIPS 2016*, 3315–3323. arXiv:1610.02413
- Dwork, C., Hardt, M., Pitassi, T., Reingold, O., & Zemel, R. (2012). Fairness Through Awareness. *ITCS 2012*, 214–226. arXiv:1104.3913
- Kusner, M. J., Loftus, J. R., Russell, C., & Silva, R. (2017). Counterfactual Fairness. *NeurIPS 2017*, 4066–4076.
- Speicher, T., Heidari, H., Grgić-Hlača, N., Gummadi, K. P., Singla, A., Weller, A., & Zafar, M. B. (2018). A Unified Approach to Quantifying Algorithmic Unfairness. *KDD 2018.* arXiv:1807.00787
- Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). Machine Bias. *ProPublica*, May 23, 2016. https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
- Larson, J., Mattu, S., Kirchner, L., & Angwin, J. (2016). How We Analyzed the COMPAS Recidivism Algorithm. *ProPublica.* https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm · data: github.com/propublica/compas-analysis
- Dieterich, W., Mendoza, C., & Brennan, T. (2016). COMPAS Risk Scales: Demonstrating Accuracy Equity and Predictive Parity. Northpointe Inc. (technical rebuttal)

Secondary / background:
- Shorrocks, A. F. (1980). The Class of Additively Decomposable Inequality Measures. *Econometrica* 48(3):613–625. (origin of the GEI decomposition)
