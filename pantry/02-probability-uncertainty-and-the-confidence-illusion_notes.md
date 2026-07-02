# Research Notes: Chapter 02 — Probability, Uncertainty, and the Confidence Illusion
**Corresponding chapter:** chapters/02-probability-uncertainty-and-the-confidence-illusion.md · **Editor note:** notes/02-probability-uncertainty-and-the-confidence-illusion.md · **Generated:** 2026-07-01

## Chapter summary
The chapter argues that a model's stated probability is not a fact about the world but a claim conditional on base rate, calibration, loss distribution, and distributional stability — and that intuition reliably ignores the prior. It derives the counterintuitive base-rate result by counting bodies before invoking Bayes, then generalizes to calibration failure and heavy-tailed loss. Its three most empirically load-bearing claims (distribution shift, softmax overconfidence, OOD-detection limits) were editor-flagged `[verify]`; two of the three resolve cleanly.

## A. Load-bearing claims → sources

### A1. Base-rate neglect: a rare-disease positive test is usually a false positive
- **Claim:** With prevalence ~1/1000–1/10,000 and a ~1–5% false-positive rate, a positive result implies only ~1–2% posterior probability of disease; intuition wildly overestimates it.
- **Source:** W. Casscells, A. Schoenberger, T. B. Graboys, "Interpretation by physicians of clinical laboratory results," *New England Journal of Medicine* 299(18):999–1001 (1978). PubMed: pubmed.ncbi.nlm.nih.gov/692627/ · DOI: 10.1056/NEJM197811022991808 · primary
- **Verdict:** CONFIRMED — Classic study: 60 Harvard subjects (house officers, students, attendings); disease prevalence 1/1000, false-positive rate 5%; most answered ~95% when the correct answer is ~2%. This is the canonical empirical anchor for the chapter's set piece.

### A2. Base-rate neglect is a general reasoning failure (representativeness)
- **Claim:** People substitute similarity/representativeness for probability and ignore the prior even when told it explicitly.
- **Source:** D. Kahneman & A. Tversky, "On the psychology of prediction," *Psychological Review* 80(4):237–251 (1973) — the lawyer/engineer problem. · primary
- **Verdict:** CONFIRMED — The 70/30 vs 30/70 base-rate manipulation produced near-identical judgments; foundational base-rate-neglect result. Supports the "intuition ignores the prior" thesis beyond the medical case.

### A3. Modern neural networks are systematically overconfident (miscalibrated)
- **Claim:** Modern deep nets output probabilities far higher than their empirical accuracy warrants; the softmax/loss-training regime produces overconfidence.
- **Source:** C. Guo, G. Pleiss, Y. Sun, K. Q. Weinberger, "On Calibration of Modern Neural Networks," ICML 2017. arXiv: arxiv.org/abs/1706.04599 · primary
- **Verdict:** CONFIRMED — Central, well-known result: depth/width/weight-decay/BatchNorm worsen calibration; temperature scaling (single-parameter Platt variant) fixes much of it. This is the chapter's calibration anchor and resolves cleanly.

### A4. A network can assign near-certain confidence to meaningless inputs
- **Claim:** Confidence is a property of the model, not evidence about the input; a net can be 99.9% confident on garbage.
- **Source:** A. Nguyen, J. Yosinski, J. Clune, "Deep Neural Networks are Easily Fooled: High Confidence Predictions for Unrecognizable Images," CVPR 2015. arXiv: arxiv.org/abs/1412.1897 · primary
- **Verdict:** CONFIRMED — Evolutionary/gradient-ascent images unrecognizable to humans classified with >99% confidence. Strong supplementary support for "the confident number is decorative"; not in the editor's flag list but directly reinforces A3.

### A5. Distribution shift makes lab-validated models fail in deployment (Hume→engineering)
- **Claim:** A COVID chest-radiograph classifier looked accurate but had learned confounding shortcuts (hospital-source markers, not pathology) and failed at new hospitals.
- **Source:** A. J. DeGrave, J. D. Janizek, S.-I. Lee, "AI for radiographic COVID-19 detection selects shortcuts over signal," *Nature Machine Intelligence* 3(7):610–619 (2021). DOI: 10.1038/s42256-021-00338-7 · nature.com/articles/s42256-021-00338-7 · primary
- **Verdict:** CONFIRMED — Exactly as the editor flagged (DeGrave et al. 2021, Nat. Mach. Intell.). The chapter's only real-world distribution-shift case; resolves cleanly.

### A6. Heavy-tailed loss breaks the "average is reassuring" intuition
- **Claim:** In heavy-tailed loss worlds the next observation can move the mean arbitrarily; a tiny average loss can coexist with a single catastrophic loss that is the only one that matters.
- **Source:** N. N. Taleb, *The Black Swan* (2007), and the standard fact that the CLT requires finite variance / iid. · secondary (conceptual, standard result)
- **Verdict:** CONFIRMED as a mathematical claim (CLT preconditions). CAUTION: the chapter layers this onto the Chapter-1 Swedish triage case ("average loss tiny, catastrophic loss the only one that mattered"), which is itself [UNVERIFIED] (see Ch.1 notes A6). The heavy-tail math is sound; the specific numbers about the triage case are not evidenced.

## B. Resolving the editor's [verify] flags

- **B1 — Pandemic medical-imaging distribution shift (note line 18, "DeGrave et al. 2021, Nature Machine Intelligence"):** RESOLVED → CONFIRMED. DeGrave, Janizek & Lee 2021, *Nat. Mach. Intell.* 3:610–619, DOI 10.1038/s42256-021-00338-7. (A5)
- **B2 — Softmax/loss overconfidence (note line 19, "Guo et al. 2017, On Calibration of Modern Neural Networks"):** RESOLVED → CONFIRMED. Guo, Pleiss, Sun & Weinberger, ICML 2017, arXiv:1706.04599. (A3)
- **B3 — OOD-detection limits (note line 20, "Krell et al. 2024"):** [UNVERIFIED]. No paper by "Krell et al. 2024" on OOD-detection limits located. The nearest real, citable results are: Morteza & Li, "Provable Guarantees for Understanding Out-of-Distribution Detection," AAAI 2022 (arXiv:2112.00787); and Meinke, Hein et al., "Provably Robust Detection of Out-of-distribution Data," NeurIPS 2022. **Recommendation:** replace the Krell citation with one of these real OOD papers, or mark [UNVERIFIED] until the intended source is located. A resolution would need the actual author/venue for the "OOD detection has fundamental limits" falsification condition.

## C. Domain examples / cases (real, cited)
- **C1 — Casscells/Schoenberger/Graboys 1978:** physicians answering ~95% vs correct ~2% on a 1/1000-prevalence test. The base-rate set piece, in a real clinical population. primary.
- **C2 — DeGrave et al. 2021:** COVID CXR shortcut-learning; the real distribution-shift failure. primary.
- **C3 — Guo et al. 2017 / Nguyen et al. 2015:** modern-net overconfidence and high-confidence-on-nonsense; the calibration-illusion evidence. primary.
- **C4 — Kahneman & Tversky 1973:** lawyer/engineer base-rate neglect; generalizes the failure beyond medicine. primary.

## D. Open flags (still [UNVERIFIED] — cut or dig deeper)
- **Krell et al. 2024 (B3):** not found. Substitute Morteza & Li 2022 (AAAI) or Meinke/Hein 2022 (NeurIPS), or locate the intended paper.
- **Heavy-tail claims about the Ch.1 triage case (A6):** quantitative claims ("average loss tiny") ride on the [UNVERIFIED] Swedish case; keep the heavy-tail math, drop or hedge the specific case numbers.
- **"99% accurate" conflates sensitivity/specificity (editor gap):** not a citation issue; the chapter should name that "accuracy" is standing in for both error rates (a precision-about-numbers chapter should not use the loose shortcut unflagged).

## Sources
Primary:
- Casscells, W., Schoenberger, A., Graboys, T. B. "Interpretation by physicians of clinical laboratory results." *NEJM* 299(18):999–1001 (1978). DOI: 10.1056/NEJM197811022991808 · https://pubmed.ncbi.nlm.nih.gov/692627/
- Kahneman, D. & Tversky, A. "On the psychology of prediction." *Psychological Review* 80(4):237–251 (1973).
- Guo, C., Pleiss, G., Sun, Y., Weinberger, K. Q. "On Calibration of Modern Neural Networks." ICML 2017. https://arxiv.org/abs/1706.04599
- Nguyen, A., Yosinski, J., Clune, J. "Deep Neural Networks are Easily Fooled." CVPR 2015. https://arxiv.org/abs/1412.1897
- DeGrave, A. J., Janizek, J. D., Lee, S.-I. "AI for radiographic COVID-19 detection selects shortcuts over signal." *Nat. Mach. Intell.* 3:610–619 (2021). DOI: 10.1038/s42256-021-00338-7 · https://www.nature.com/articles/s42256-021-00338-7
- Morteza, P. & Li, Y. "Provable Guarantees for Understanding Out-of-Distribution Detection." AAAI 2022. https://arxiv.org/abs/2112.00787 (candidate replacement for Krell)
- Meinke, A., Hein, M. et al. "Provably Robust Detection of Out-of-distribution Data." NeurIPS 2022. (candidate replacement for Krell)

Secondary:
- Taleb, N. N. *The Black Swan* (2007) — heavy-tail / CLT-precondition framing.

[UNVERIFIED] Krell et al. 2024 (OOD-detection limits) — not located; real substitutes above.
