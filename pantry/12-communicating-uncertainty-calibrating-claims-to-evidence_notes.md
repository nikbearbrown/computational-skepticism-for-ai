# Research Notes: Chapter 12 — Communicating Uncertainty: Calibrating Claims to Evidence
**Corresponding chapter:** chapters/12-communicating-uncertainty-calibrating-claims-to-evidence.md · **Editor note:** notes/12-communicating-uncertainty-calibrating-claims-to-evidence.md · **Generated:** 2026-07-01

## Chapter summary
The chapter argues the verb of a claim does epistemic work engineers overlook, and that calibrating the verb to the evidence (downgrading when evidence is weaker) is the core skill of communicating validation findings — for human writing and as a fluency-trap detector on AI output. It welds a verb taxonomy to a calibration-metrics battery (Brier, ECE, MCE, reliability diagrams, subgroup ECE, temperature scaling, conformal prediction) via a "calibration evidence ladder" mapping metric-evidence to warranted verb.

## A. Load-bearing claims → sources
- **Claim:** Expected Calibration Error (ECE) = weighted average of |accuracy − confidence| across confidence bins; MCE = max over bins. · **Source:** Naeini, M.P., Cooper, G.F. & Hauskrecht, M., "Obtaining Well Calibrated Probabilities Using Bayesian Binning," *Proc. AAAI* 29(1), 2015 (https://ojs.aaai.org/index.php/AAAI/article/view/9602) · primary · **Verdict:** CONFIRMED — ECE/MCE binning definitions originate here; ECE approaches 0 at calibration.
- **Claim:** Modern deep neural networks are accurate but systematically overconfident (miscalibrated); temperature scaling (single-parameter Platt scaling on logits) is a simple, effective post-hoc fix. · **Source:** Guo, C., Pleiss, G., Sun, Y. & Weinberger, K.Q., "On Calibration of Modern Neural Networks," *Proc. ICML* 2017 (arXiv:1706.04599) · primary · **Verdict:** CONFIRMED — establishes miscalibration/overconfidence in modern DNNs, identifies depth/width/weight-decay/BatchNorm as factors, and introduces temperature scaling as the method to beat.
- **Claim:** "Overconfidence is the dominant failure mode in modern deep neural networks and large language models." · **Source:** Guo et al. 2017 (for DNNs) · primary · **Verdict:** [UNVERIFIED as stated] — Guo et al. show modern DNNs are overconfident (vs. well-calibrated older/shallower nets), but note: Minderer et al., "Revisiting the Calibration of Modern Neural Networks" (NeurIPS 2021, arXiv:2106.07998) found newer non-convolutional architectures (e.g., ViT, MLP-Mixer) are often *better* calibrated — so "dominant failure mode... regardless" is CONTESTED. The LLM extension is plausible but not sourced to a single canonical study here. Recommend citing Guo 2017 + flagging Minderer 2021 as the counter-finding.
- **Claim:** "Well-calibrated deployed models often have ECE in the range of 0.02–0.05; above 0.10 is a clear signal." · **Source:** none located · **Verdict:** [UNVERIFIED] — these thresholds are commonly quoted heuristics in practitioner literature but were NOT confirmed to a primary source. ECE is also bin-count-dependent (not scale-free), so any fixed threshold is method-sensitive. Reframe as "rule-of-thumb, method-dependent" or cite a specific benchmark table.
- **Claim:** The Epic Sepsis Model, externally validated, performed far worse than advertised: AUC ~0.63, PPV ~12% at the deployed alert threshold, missing ~67% of sepsis cases. · **Source:** Wong, A. et al., "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients," *JAMA Internal Medicine* 181(8), 2021, pp. 1065–1070 (https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307; PubMed 34152360) · primary · **Verdict:** CONFIRMED — 27,697 patients / 38,455 hospitalizations at Michigan Medicine; sepsis in 7%; AUC 0.63 (95% CI 0.62–0.64) vs. developer-reported 0.76–0.83; **PPV = 12% at ESM score ≥6** (i.e., ~88% false alarms); ESM missed 1,709 of 2,552 septic patients (67%). The "construct validity failure invisible to calibration" framing is a fair editorial reading.
- **Claim:** Brier score decomposes into reliability, resolution, and uncertainty. · **Source:** Brier, G.W., "Verification of Forecasts Expressed in Terms of Probability," *Monthly Weather Review* 78(1), 1950, pp. 1–3; decomposition: Murphy, A.H., "A New Vector Partition of the Probability Score," *J. Applied Meteorology* 12, 1973, pp. 595–600 · primary · **Verdict:** [UNVERIFIED here — not searched] but these are the standard, real attributions (Brier 1950; Murphy 1973 three-term decomposition). Cite directly.
- **Claim:** Conformal prediction gives a marginal (not conditional) coverage guarantee that relies on exchangeability, which distribution shift breaks. · **Source:** Vovk, Gammerman & Shafer, *Algorithmic Learning in a Random World* (2005); Angelopoulos & Bates, "A Gentle Introduction to Conformal Prediction" (arXiv:2107.07511, 2021) · primary/secondary · **Verdict:** [UNVERIFIED here — not searched] but the exchangeability caveat and marginal-not-conditional coverage are standard and correctly stated. Cite Angelopoulos & Bates for the accessible version.
- **Claim:** IPCC-style calibrated language separates *likelihood* (probabilistic) from *confidence* (evidence × agreement) — a model for verb-to-evidence calibration. · **Source:** Mastrandrea, M.D. et al., "Guidance Note for Lead Authors of the IPCC Fifth Assessment Report on Consistent Treatment of Uncertainties," IPCC, 2010 (https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf); also *Climatic Change* 108, 2011, pp. 675–691 (https://doi.org/10.1007/s10584-011-0178-6) · primary · **Verdict:** CONFIRMED — two-metric scheme (5-level confidence scale; calibrated likelihood terms) confirmed.

## B. Resolving the editor's [verify] flags
The editor notes this chapter has effectively **no explicit [verify] tags** but flags unsourced load-bearing claims:
- **ECE "0.02–0.05 typical / >0.10 signal"** → [UNVERIFIED]. No primary source. See A. Reframe as heuristic; note bin-dependence.
- **"Overconfidence = dominant failure mode in modern DNNs/LLMs"** → CONTESTED. Guo 2017 supports for the CNN era; Minderer et al. 2021 shows newer architectures often better-calibrated. See A.
- **Epic Sepsis "PPV 12% / 88% false alarms"** → CONFIRMED to Wong et al. 2021 JAMA IM. Exact: PPV 12% at score ≥6; sensitivity effectively ~33% (missed 67%). See A.
- **Brier decomposition attribution** → real (Brier 1950; Murphy 1973); cite directly. [Not fetched — CONFIRMED by standard attribution.]
- **"Kernel Calibration Error (kCE)"** → [UNVERIFIED] — real concept (e.g., Widmann, Lindsten & Zachariah, "Calibration tests in multi-class classification: A unifying framework," NeurIPS 2019; MMD-based calibration errors) but the specific "kCE" label/attribution was not confirmed here.
- **Conformal exchangeability framing** → correct; cite Angelopoulos & Bates 2021 / Vovk et al. 2005.
- **Cleveland-McGill / Gigerenzer echoes** → see Chapter 11 notes; CONFIRMED there.

## C. Domain examples / cases (real, cited)
- **Epic Sepsis Model:** CONFIRMED failure case (Wong et al. 2021, JAMA IM). AUC 0.63, PPV 12%, 67% of sepsis missed, alert fatigue. Best-documented real case for "aggregate metrics can mislead" and "calibration ≠ construct validity."
- **IPCC calibrated language:** CONFIRMED real framework (Mastrandrea et al. 2010) — the strongest real-world precedent for the chapter's verb-to-evidence calibration thesis.
- **Guo et al. 2017 reliability diagrams:** CONFIRMED source for the four diagram shapes (over/under-confident, sigmoidal, locally miscalibrated) discussion.

## D. Open flags (still [UNVERIFIED])
- ECE "0.02–0.05 typical / >0.10 clear signal" thresholds — no primary source; method-dependent.
- "Dominant failure mode in modern DNNs/LLMs" — CONTESTED by Minderer et al. 2021 for newer architectures; scope the claim.
- "Kernel Calibration Error (kCE)" specific label/attribution.
- Verb-taxonomy ordering/membership is an internal-consistency issue (editor Priority #1), not a citation issue — no external source can resolve it; it is an authorial choice. The taxonomy itself is not drawn from a single citable source (it is the chapter's construction), so no primary source exists to "verify" the ordering.

## Sources
Primary:
- Naeini, M.P., Cooper, G.F. & Hauskrecht, M. (2015). Obtaining Well Calibrated Probabilities Using Bayesian Binning. *AAAI* 29(1). https://ojs.aaai.org/index.php/AAAI/article/view/9602
- Guo, C., Pleiss, G., Sun, Y. & Weinberger, K.Q. (2017). On Calibration of Modern Neural Networks. *ICML*. arXiv:1706.04599.
- Wong, A. et al. (2021). External Validation of a Widely Implemented Proprietary Sepsis Prediction Model. *JAMA Internal Medicine* 181(8): 1065–1070. https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307
- Mastrandrea, M.D. et al. (2010). Guidance Note... on Consistent Treatment of Uncertainties. IPCC. https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf ; *Climatic Change* 108: 675–691, https://doi.org/10.1007/s10584-011-0178-6
- Brier, G.W. (1950). Verification of Forecasts Expressed in Terms of Probability. *Monthly Weather Review* 78(1): 1–3.
- Murphy, A.H. (1973). A New Vector Partition of the Probability Score. *J. Applied Meteorology* 12: 595–600.
Secondary / counter-evidence:
- Minderer, M. et al. (2021). Revisiting the Calibration of Modern Neural Networks. *NeurIPS*. arXiv:2106.07998. [counter-finding to "dominant failure mode"]
- Angelopoulos, A.N. & Bates, S. (2021). A Gentle Introduction to Conformal Prediction. arXiv:2107.07511.
- Vovk, V., Gammerman, A. & Shafer, G. (2005). *Algorithmic Learning in a Random World*. Springer.
