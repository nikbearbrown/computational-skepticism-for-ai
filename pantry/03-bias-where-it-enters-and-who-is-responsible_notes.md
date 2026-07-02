# Research Notes: Chapter 03 — Bias: Where It Enters and Who Is Responsible
**Corresponding chapter:** chapters/03-bias-where-it-enters-and-who-is-responsible.md · **Editor note:** notes/03-bias-where-it-enters-and-who-is-responsible.md · **Generated:** 2026-07-01

## Chapter summary
The chapter reframes bias as a family of mechanisms entering an AI pipeline at distinct points, argues the highest-leverage fix usually lives off-model (in deployment structure), and shows via the fairness-impossibility result that choosing a fairness metric is a values choice, not a technical one. Its strongest move is the COMPAS "re-arrest is not crime" analysis. Its main gaps are provenance: COMPAS, the fairness "theorem," and the "Glimmer" cases were all editor-flagged `[verify]` — nearly all resolve to strong primary sources.

## A. Load-bearing claims → sources

### A1. The fairness impossibility is a real theorem, not a controversy
- **Claim:** When base rates differ across groups and prediction is imperfect, a risk score cannot simultaneously satisfy calibration/predictive parity AND equal false-positive/false-negative rates. Metric choice is therefore a values decision.
- **Source (a):** A. Chouldechova, "Fair prediction with disparate impact: A study of bias in recidivism prediction instruments," *Big Data* 5(2):153–163 (2017). arXiv:1703.00056 · DOI: 10.1089/big.2016.0047 · primary
- **Source (b):** J. Kleinberg, S. Mullainathan, M. Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," ITCS 2017. arXiv:1609.05807 · primary
- **Verdict:** CONFIRMED — Both results are real and are precisely the incompatibility the chapter asserts. Chouldechova proves predictive parity + error-rate balance cannot co-hold under unequal prevalence; Kleinberg–Mullainathan–Raghavan prove three fairness conditions (calibration, balance for positive class, balance for negative class) are jointly satisfiable only in degenerate cases. Cite both and present it as *their* theorem (resolving the editor's "asserted not proved / uncited" gap).

### A2. COMPAS: the canonical fairness failure, and the re-arrest≠crime insight
- **Claim:** COMPAS flagged Black defendants as higher-risk-but-not-reoffending at ~2× the white rate; the deeper problem is the label — the data measures re-arrest, a function of crime *and* policing, not crime.
- **Source:** J. Angwin, J. Larson, S. Mattu, L. Kirchner, "Machine Bias," ProPublica, May 23, 2016. propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing · methodology: propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm · primary (investigative)
- **Verdict:** CONFIRMED — Attribution, date, authors, and the false-positive-rate disparity are correct. Note for balance: Northpointe and later scholars (Flores/Bechtel/Lowenkamp rejoinder; Corbett-Davies et al.) contested ProPublica's framing — this is itself the fairness-impossibility playing out (both sides right under different definitions), which strengthens the chapter's point. CONTESTED-but-real: the case is real; its interpretation is exactly the values dispute the chapter names.

### A3. Fairness-mitigation methods exist and are formally defined
- **Claim:** There are formal fairness criteria beyond metric-tweaking (equalized odds, learned fair representations).
- **Source (a):** M. Hardt, E. Price, N. Srebro, "Equality of Opportunity in Supervised Learning," NIPS 2016. arXiv:1610.02413 · primary
- **Source (b):** D. Madras, E. Creager, T. Pitassi, R. Zemel, "Learning Adversarially Fair and Transferable Representations," ICML 2018. arXiv:1802.06309 · primary
- **Verdict:** CONFIRMED (Hardt et al. 2016) — equalized-odds criterion, exactly as cited. Madras et al. 2018 (LAFTR) is real and is about fair/transferable representations; confirm the editor's intended claim maps to it (the ICML 2018 LAFTR paper is the standard "Madras et al. 2018" fairness reference).

### A4. Structural bias: an agent inherits its provider's values
- **Claim:** An agent's behavior silently reflects the political/policy constraints of the LLM provider behind it.
- **Source:** N. Shapira et al., *Agents of Chaos* (2026), Case Study #6 "Agents Reflect Provider Values." agentsofchaos.baulab.info/report.html · arXiv:2602.20021 [confirm ID] · primary
- **Verdict:** CONFIRMED — Case #6 is exactly this: a Kimi-K2.5-backed agent's API "repeatedly truncated responses with 'unknown error' on politically sensitive topics" (Hong Kong politics, Jimmy Lai), silently shaping behavior. Verbatim objective: *"Test how LLM provider policies and biases silently affect agent behavior."* The book's citation ("Case #6, Agents Reflect Provider Values") is accurate. (Same count/ID caveat as Ch.1: report body numbers 16 cases; confirm arXiv ID on arxiv.org.)

### A5. Sampling bias: more data does not fix a biased frame (Literary Digest 1936)
- **Claim:** A huge sample drawn from a skewed frame gives a confidently wrong answer; sample size cannot cure sampling bias.
- **Source:** *The Literary Digest* 1936 presidential poll (predicted Landon 57–43; actual Roosevelt 62–38). Scholarly analysis: P. Squire, "Why the 1936 Literary Digest Poll Failed," *Public Opinion Quarterly* 52(1):125–133 (1988). · primary (analysis) + historical
- **Verdict:** CONFIRMED — ~2.4M-ballot sample; frame skewed to phone/car/subscription owners plus non-response bias; Gallup called it right with ~50,000. Standard, well-documented case.

### A6. Proxy/label bias in deployed health algorithms (Glimmer cluster + estimator theory)
- **Claim:** Using a convenient proxy for the true target injects structural bias (cost as proxy for illness).
- **Source:** Z. Obermeyer, B. Powers, C. Vogeli, S. Mullainathan, "Dissecting racial bias in an algorithm used to manage the health of populations," *Science* 366(6464):447–453 (2019). DOI: 10.1126/science.aax2342 · primary
- **Verdict:** CONFIRMED — The algorithm predicted health *cost*, not health *need*; because less is spent on Black patients, equal-risk-score Black patients were sicker. Remedy raised Black patients getting extra help from 17.7%→46.5%. Perfect proxy-bias exemplar and directly supports the estimator definition Bias(θ̂)=E[θ̂]−θ (the proxy shifts E[θ̂] off θ).

## B. Resolving the editor's [verify] flags

- **B1 — COMPAS (note line 19, "Angwin et al., ProPublica 2016, Machine Bias"):** RESOLVED → CONFIRMED. Angwin, Larson, Mattu, Kirchner, ProPublica, 2016-05-23. (A2)
- **B2 — Agents of Chaos Case #6 "Agents Reflect Provider Values" (note line 20):** RESOLVED → CONFIRMED. Shapira et al. 2026, Case Study #6; title and case number verified against the report. (A4)
- **B3 — Hardt et al. 2016 / Madras et al. 2018 (note line 21):** RESOLVED → CONFIRMED. Hardt, Price & Srebro, "Equality of Opportunity in Supervised Learning," NIPS 2016 (arXiv:1610.02413); Madras, Creager, Pitassi & Zemel, "Learning Adversarially Fair and Transferable Representations," ICML 2018 (arXiv:1802.06309). Confirm each in-text claim matches (equalized odds ↔ Hardt; fair representations ↔ Madras/LAFTR). (A3)
- **B4 — Glimmer citations (note line 22): Apple Card (2019), Amazon resume screener (2018), Obermeyer et al. (2019):**
  - Amazon 2018 — CONFIRMED: Reuters (Dastin), Oct 2018; scrapped recruiting tool that penalized "women's" and downgraded women's-college résumés (trained on 10 yrs of male-skewed résumés). Real, well-documented.
  - Obermeyer et al. 2019 — CONFIRMED (A6), *Science*, DOI 10.1126/science.aax2342.
  - Apple Card 2019 — CONFIRMED-with-nuance: the Hansson/Wozniak viral allegations and NY DFS investigation are real (Nov 2019). BUT the DFS 2021 finding concluded **no unlawful disparate impact by sex** ("applications from women and men with similar credit characteristics generally had similar outcomes"), faulting transparency/customer-service instead. **Use with care:** cite it as a *contested/investigated* allegation, not a proven bias case, or the chapter overclaims. CONTESTED.
- **B5 — Fairness-impossibility theorem uncited (note line 23):** RESOLVED → cite Chouldechova 2017 and Kleinberg–Mullainathan–Raghavan 2016 (A1). Add a two-line counting-argument sketch as the editor recommends.

## C. Domain examples / cases (real, cited)
- **C1 — COMPAS** (Angwin et al. 2016): fairness case + label-artifact insight. primary.
- **C2 — Obermeyer et al. 2019** (*Science*): proxy/label bias, cost-vs-need. primary.
- **C3 — Amazon recruiting tool** (Reuters 2018): historical/training-data bias, scrapped. secondary (news).
- **C4 — Literary Digest 1936** (Squire 1988): sampling-frame bias; size ≠ fix. primary analysis.
- **C5 — Agents of Chaos CS#6** (Shapira et al. 2026): structural/provider-values bias. primary.
- **C6 — Apple Card 2019** (NY DFS 2021; WaPo/CNN 2019): allegation + investigation that found no unlawful sex disparity — good teaching case *about* how a bias claim gets adjudicated, if framed honestly. contested.

## D. Open flags (still [UNVERIFIED] / needs care)
- **Apple Card as a "bias case" (B4):** the DFS investigation cleared Goldman of unlawful sex discrimination. Reframe as contested/investigated, not proven, or drop.
- **Three-teams parable (editor gap):** unlabeled constructed anecdote doing heavy argumentative work; flag as composite (as Ch.1 flags Ash). Not a citation issue.
- **Ten-mechanism taxonomy vs compound table (editor gap):** internal counting inconsistency; not a sourcing issue but must be reconciled.
- **arXiv ID 2602.20021:** confirm on arxiv.org (same caveat as Ch.1).

## Sources
Primary:
- Angwin, J., Larson, J., Mattu, S., Kirchner, L. "Machine Bias." ProPublica, 2016-05-23. https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
- Chouldechova, A. "Fair prediction with disparate impact." *Big Data* 5(2):153–163 (2017). DOI: 10.1089/big.2016.0047 · https://arxiv.org/abs/1703.00056
- Kleinberg, J., Mullainathan, S., Raghavan, M. "Inherent Trade-Offs in the Fair Determination of Risk Scores." ITCS 2017. https://arxiv.org/abs/1609.05807
- Hardt, M., Price, E., Srebro, N. "Equality of Opportunity in Supervised Learning." NIPS 2016. https://arxiv.org/abs/1610.02413
- Madras, D., Creager, E., Pitassi, T., Zemel, R. "Learning Adversarially Fair and Transferable Representations." ICML 2018. https://arxiv.org/abs/1802.06309
- Obermeyer, Z., Powers, B., Vogeli, C., Mullainathan, S. "Dissecting racial bias in an algorithm used to manage the health of populations." *Science* 366(6464):447–453 (2019). DOI: 10.1126/science.aax2342
- Shapira, N. et al. *Agents of Chaos* (2026), Case Study #6. https://agentsofchaos.baulab.info/report.html · arXiv:2602.20021 [confirm ID]
- Squire, P. "Why the 1936 Literary Digest Poll Failed." *Public Opinion Quarterly* 52(1):125–133 (1988).

Secondary:
- Dastin, J. "Amazon scraps secret AI recruiting tool that showed bias against women." Reuters, Oct 2018. (via MIT Tech Review: https://www.technologyreview.com/2018/10/10/139858/)
- NY Dept. of Financial Services, report on Apple Card / Goldman Sachs sex-discrimination probe (2021); coverage: Washington Post / CNN (Nov 2019). — CONTESTED; no unlawful disparity found.
