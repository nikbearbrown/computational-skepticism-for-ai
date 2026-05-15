# Chapter 12 — Communicating Uncertainty: Calibrating Claims to Evidence
*The Verb Is Doing Epistemic Work You Are Not Noticing.*

I want to start with the same finding written three different ways. The evidence is identical in each case: a model achieved 87% accuracy on a held-out test set drawn from the deployment distribution, with no significance test reported and no confidence interval computed.

Here is sentence A: *We conclude that the new model is more accurate than the prior model.*

Here is sentence B: *We find that the new model achieves 87% accuracy on the held-out test set, compared to the prior model's 84% on the same set.*

Here is sentence C: *We observe that the new model produces 87% accuracy on this single held-out evaluation; whether the difference from the prior model is statistically significant is not yet established.*

Three sentences. The evidence supports sentence C. The evidence is partly compatible with sentence B — *find* is a stronger verb than *observe*, and it carries some implied generalization, but the implied generalization is not yet warranted by what we have. The evidence does not support sentence A. *Conclude* implies a settled judgment, and a single accuracy number on one test set, without significance testing or confidence intervals, is not a settled judgment.

Engineers default to sentence A. Engineering papers are full of conclusions stated more strongly than the evidence permits. This is not malicious. It is mostly inattention to a particular kind of calibration — the calibration of the *verb* of a claim to the evidence the claim is built on. The verb is doing real epistemic work, and most engineering writers do not notice the verb at all.

The fix is a taxonomy. We are going to build it now.

---

**Learning objectives.** By the end of this chapter you should be able to:

- Apply the verb taxonomy to any claim in a technical document and identify whether the verb is warranted by the evidence
- Use the verb taxonomy as a fluency-trap detector on AI-generated output
- Structure a validation document in three audience layers — plain English summary, technical detail, reproducibility appendix — without losing critical nuance in translation
- Name specific uncertainty in prose — distinguishing epistemic from aleatoric, quantifying where possible, avoiding throat-clearing hedges
- Compute and interpret the core trust calibration metrics: Brier score, Expected Calibration Error, reliability diagrams, and the proper-scoring-rule family
- Identify which trust calibration failure mode a deployment is exhibiting from its metric profile
- Give and receive peer critique on the verb-evidence calibration of a peer's validation writing

**Prerequisites.** Chapter 11 (uncertainty visualization — this chapter is its paired textual counterpart). Chapter 4 (the Frictional method and prediction-locking — peer critique is the same epistemic discipline applied collectively). Chapter 2 (probability and calibration foundations). No prerequisites beyond Chapter 2 for the metrics section.

---

## The verb taxonomy

A working hierarchy. Each verb implies a specific epistemic posture toward the evidence. Choose the verb whose posture matches what your evidence actually warrants.

*Hypothesize.* "We hypothesize that X." Posture: an idea, not yet tested, that we are about to investigate. The evidence required is a coherent reason to investigate, not evidence that the hypothesis is true. Used at the front of a paper, in proposals, in framing future work.

*Suggest.* "The data suggest that X." Posture: the data is consistent with X but does not distinguish X from alternatives. The evidence required is an observation that points toward X without ruling out other explanations. Common when an experiment was not designed to test X but X emerged from the analysis.

*Observe.* "We observe that X." Posture: the data shows X under these specific conditions. No claim about generalization beyond the conditions. The evidence required is a clean observation, with the observation conditions stated. The most defensible verb when the evidence is from a single experiment or a single dataset.

*Find.* "We find that X." Posture: across the evidence we have looked at, X holds. Slightly stronger than observe — it implies multiple observations or robustness to some variation in conditions. The evidence required is at least replication, ideally with some sensitivity analysis.

*Show.* "We show that X." Posture: the evidence demonstrates X with sufficient strength that X is the operational reading. The evidence required is replication, robustness, alternative-explanation ruling-out. This is a strong verb. Do not use it lightly.

*Demonstrate.* "We demonstrate that X." Posture: a constructed proof or near-proof. The evidence required is an experiment specifically designed to test X, ideally with formal guarantees or strong inferential control. Rare in deployed engineering work; common in formal verification.

*Conclude.* "We conclude that X." Posture: the question that motivated the work is settled by the evidence. The evidence required is full analysis, alternatives considered and rejected, sensitivity analysis, and a finding that survives the analysis. *This is the strongest verb in the taxonomy short of mathematical proof.* Very few claims warrant it.

*Prove.* "We prove that X." A mathematical proof. Reserved for formal claims with formal evidence.

The taxonomy is not exhaustive — *characterize*, *report*, *describe*, *quantify*, *establish* each occupy specific niches — but it covers most of the useful range. The exercise, every time you draft something, is to read your draft sentence by sentence and ask whether the verb you used matches the evidence the sentence is built on.

| Verb | Epistemic posture | Minimum evidence required | Correct use example | Common misuse |
|---|---|---|---|---|
| **Hypothesize** | Tentative; pre-evidence | A defensible reason to consider the claim | "We hypothesize that calibration degrades on the rare-disease subgroup" | Used as a softener for a claim already supported by data |
| **Observe** | Direct; descriptive | A measurement and the measurement procedure | "We observe ECE = 0.04 on the global test set" | Used to soften a causal claim ("we observe the model causes…") |
| **Find** | Direct; established by the analysis | The analysis result, the comparison, the n | "We find subgroup ECE exceeds global ECE by 2.3× on the elderly cohort" | Used for a one-shot anecdote |
| **Suggest** | Cautious inference | Evidence consistent with the inference; alternatives not ruled out | "These results suggest miscalibration concentrates in the elderly subgroup" | Used in place of *find* when the evidence already supports the stronger verb |
| **Indicate** | Stronger inference; multiple lines of evidence | Convergent results from independent analyses | "Cross-site replication indicates the subgroup pattern is not site-specific" | Used as a synonym for *suggest* |
| **Demonstrate** | Established; replicated | Reproducible result, named replication, no live alternative | "We demonstrate that the subgroup gap persists under three calibration methods" | Used for a single-study finding |
| **Conclude** | Action-warrant; takes a position | A conclusion that survives the alternatives the team has named and tested | "We conclude the deployment cannot ship without subgroup-specific recalibration" | Used as a paragraph-ending stylistic flourish |
| **Prove** | Decisive; mathematically or by formal verification | A proof, formal or empirical with a closed-form alternative space | "We prove the bound holds for all inputs in the certified region" | Used in any non-formal engineering setting |

*Most engineering writing sits between* observe *and* find. *Most engineering writing uses* conclude. *The gap is the problem.*

This is unromantic editing. There is no inspiration in it. You are downgrading verbs because the evidence does not warrant the original verb, and the prose loses some of the punch you put into it. I want to tell you that this is also the most operationally important single skill in technical communication of validation findings. The careful engineer's writing reads, at first, as quieter than the careless engineer's. It also survives reading.

---

## Two readers, one document

Validation findings often get communicated to two audiences at the same time. There are technical readers — peers, reviewers, engineers in adjacent teams — and there are non-technical readers — deployment partners, executive sponsors, regulators, affected populations.

The instinct, when this is recognized, is to write two documents. A technical paper and an executive summary. The two-document approach is sometimes appropriate. It is often inefficient, and the executive summary often loses critical nuance in translation, because the translation happens after the technical work is done and the translator did not have the technical decisions in their bones.

A working alternative is *layered writing*. The technical and non-technical content live in the same document, layered so that each reader can find their level without translation.

The pattern is three layers, and you should be able to point to each one in your draft.

*Layer 1.* A short, prose-paragraph summary at the start of every section. Plain English. No equations. No specialized terminology beyond what the deployment partner already knows. The summary covers what the section finds and why it matters for the deployment decision. A non-technical reader can read only Layer 1 across the document and have a working understanding.

*Layer 2.* The technical detail. Methods, equations, tables, references. Written for the technical reader who needs to evaluate the work. Layer 2 is specific where Layer 1 is general; Layer 2 is rigorous where Layer 1 is plain.

*Layer 3.* Appendices, supplementary materials. The reproducibility detail. Hyperparameters, code, data documentation, full sensitivity analyses. For the reader who wants to reproduce or audit.

The layered approach is harder to write than two separate documents. It is easier to maintain, easier to keep consistent, and produces fewer translation errors. It also mirrors the structure of good validation work: the executive question is addressed by the executive layer, the technical question by the technical layer, and the reproducibility question by the reproducibility layer.

Layer 1 is not "dumbed down." Dumbing down is condescending and loses information. Layer 1 is a specific, careful, accurate summary in plain English. Plain English is *harder* to write than jargon. The technical reader benefits from Layer 1 as much as the non-technical reader does — it forces the writer to articulate what the section is really doing, which is sometimes a useful discovery for the writer.

<!-- → [IMAGE: Layered document structure — a single document shown as a vertical stack. Three clearly labeled bands: Layer 1 (plain English summary, executive reader enters here), Layer 2 (technical detail, peer reviewer enters here), Layer 3 (appendix / reproducibility detail, auditor enters here). Three reader-type labels on the right, each with an arrow pointing to the layer they primarily use. Key callout: "all three layers live in the same document — no translation required." Figure 12.2] -->

---

## Metrics and measures of trust calibration

Uncertainty in prose requires a language of hedges and qualifications. But engineers are accountable to numbers, and the prose-level calibration of claims needs grounding in quantitative measures of whether the model's stated confidence actually tracks reality. This section develops those measures — what they compute, what they detect, and what each one cannot see.

The core question is simple to state and hard to answer: *when the model says it is 80% confident, is it actually right about 80% of the time?* A model that answers "yes" to this question consistently is calibrated. A model that answers "no" in a systematic direction is miscalibrated, and the direction of miscalibration matters.

### The Brier score: a proper scoring rule

The Brier score is the foundational metric for probabilistic prediction quality. For a binary outcome, it is the mean squared difference between the predicted probability and the actual binary outcome across all predictions:

$$\text{BS} = \frac{1}{N} \sum_{i=1}^{N} (p_i - y_i)^2$$

where $p_i \in [0,1]$ is the model's predicted probability for instance $i$ and $y_i \in \{0, 1\}$ is the actual outcome.

The Brier score runs from 0 (perfect calibration on every prediction) to 1 (perfectly wrong on every prediction). A random classifier predicting $p_i = 0.5$ for all instances achieves $\text{BS} = 0.25$. A well-calibrated classifier should substantially beat this baseline.

The Brier score is a *proper scoring rule*: it is minimized, in expectation, when and only when the model reports the true probability. This is the key property that distinguishes proper scoring rules from raw accuracy metrics. Accuracy rewards the model for being right; it does not penalize the model for being confidently right when the situation warranted hedging. The Brier score penalizes both miscalibration and poor discrimination simultaneously.

The Brier score decomposes into three interpretable components:

$$\text{BS} = \underbrace{\overline{y}(1 - \overline{y})}_{\text{Uncertainty}} - \underbrace{\text{REL}}_{\text{Resolution}} + \underbrace{\text{CAL}}_{\text{Calibration}}$$

where $\overline{y}$ is the base rate of positive outcomes, REL is the resolution (how much the model's predictions vary around the base rate — capturing discrimination power), and CAL is the calibration component (how much predicted probabilities deviate from empirical frequencies in each score bin). A deployment that reports a single Brier score is collapsing these three into one number. The decomposition is what lets you diagnose *why* the score is what it is.

For example: a model with a low Brier score but poor resolution is one that is well-calibrated but predicts close to the base rate for every instance — it is honest about uncertainty but useless for triage. A model with high resolution but poor calibration is one that discriminates well but whose probabilities are misleading — it ranks cases correctly but the absolute numbers cannot be trusted.

<!-- → [INFOGRAPHIC: Brier score decomposition — three-part stacked bar. Left bar shows Uncertainty term (fixed for given base rate). Right bar shows Brier score split into Resolution (subtracted, shown in green) and Calibration error (added, shown in red). Two example profiles beneath: Model A (low calibration error, low resolution) labeled "honest but unhelpful"; Model B (high resolution, high calibration error) labeled "discriminates but misleads." Caption: "The Brier score collapse hides which of the three components is driving the number. Always decompose." Figure 12.3] -->

### Expected Calibration Error: binning the predictions

The Expected Calibration Error (ECE) is the most commonly reported calibration metric in deployed systems. It operates by binning predictions into equal-width intervals and measuring the weighted average gap between mean predicted confidence and mean actual accuracy in each bin:

$$\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N} \left| \text{acc}(B_m) - \text{conf}(B_m) \right|$$

where $M$ is the number of bins, $B_m$ is the set of instances falling in bin $m$, $\text{acc}(B_m)$ is the fraction of instances in that bin that were actually positive, and $\text{conf}(B_m)$ is the mean predicted probability of instances in that bin.

A perfectly calibrated model has $\text{ECE} = 0$. In practice, well-calibrated deployed models often have $\text{ECE}$ in the range of 0.02–0.05. A value above 0.10 is a clear signal of systematic miscalibration.

The ECE is intuitive and easy to report, but it has a structural weakness: its value depends on the number and width of bins chosen. Small changes in bin count can produce meaningfully different ECE values on the same data. The ECE is therefore best understood as a directional indicator rather than a precise measurement, and it should always be accompanied by the binning specification. *An ECE reported without the number of bins is not fully reproducible.*

An alternative that avoids this dependence is the *Maximum Calibration Error* (MCE), which reports the worst-case gap across bins rather than the weighted average:

$$\text{MCE} = \max_{m \in \{1,\ldots,M\}} \left| \text{acc}(B_m) - \text{conf}(B_m) \right|$$

MCE is useful in safety-critical deployments where the worst-case failure mode matters more than the average. A system that looks well-calibrated on average (low ECE) but has a specific confidence range where it is systematically overconfident (high MCE in that bin) may be dangerous even when the aggregate ECE looks acceptable.

### The reliability diagram

The reliability diagram — sometimes called the calibration plot — is the visual equivalent of the ECE computation. For each bin, it plots mean confidence on the x-axis and mean accuracy on the y-axis. A perfectly calibrated model falls on the diagonal. Systematic deviation from the diagonal reveals the miscalibration pattern.

The shape of the deviation is diagnostic:

- **Overconfidence** (curve below the diagonal): the model's predicted probabilities are higher than warranted. A model predicting "90% positive" that is actually right 70% of the time is overconfident. This is the dominant failure mode in modern deep neural networks and large language models.
- **Underconfidence** (curve above the diagonal): predicted probabilities are lower than warranted. Less common, but seen in models trained with heavy regularization or label smoothing.
- **Sigmoidal pattern**: overconfident at the extremes, underconfident in the middle. Common in gradient-boosted tree models.
- **Well-calibrated in aggregate but locally miscalibrated**: the aggregate reliability diagram looks good, but specific subpopulations or confidence ranges show large deviations. This is the failure mode that aggregate metrics miss entirely.

<!-- → [CHART: Four reliability diagrams in a 2×2 grid. Panel 1: perfectly calibrated (points on the diagonal). Panel 2: overconfident (points below diagonal, gap between points and diagonal shaded). Panel 3: underconfident (points above diagonal). Panel 4: sigmoidal pattern (below diagonal at low and high confidence, above diagonal in the middle). Each panel labeled with failure mode name and one-sentence description of which model type typically produces it. Histogram of prediction frequency shown at bottom of each panel. Caption: "The shape of the deviation from the diagonal tells you what kind of miscalibration you have. The aggregate ECE does not." Figure 12.4] -->

### Subgroup calibration: where aggregate metrics lie

The single most important limitation of aggregate calibration metrics is that they are aggregate. A system with low global ECE can be catastrophically miscalibrated for a specific subgroup if that subgroup is small enough to be washed out in the overall average.

The Epic Sepsis Model illustrates the structural problem. The model's aggregate performance metrics looked acceptable across the full deployed population. The failure — a PPV of 12%, meaning 88% of pages to clinicians were false alarms — only became visible through external validation at a specific deployment site, with a specific patient population, where the model had never been validated before.

The methodological implication: run a separate reliability diagram and separate ECE for each named subgroup in the deployment. At minimum: demographic subgroups, severity strata, and any subgroup you have reason to believe differs from the training distribution. The aggregate metric is evidence the model is calibrated on average. It is not evidence the model is calibrated for the patient in front of you.

For each subgroup $g$, compute:

$$\text{ECE}_g = \sum_{m=1}^{M} \frac{|B_m^g|}{N_g} \left| \text{acc}(B_m^g) - \text{conf}(B_m^g) \right|$$

and report both the global $\text{ECE}$ and the full distribution of $\{\text{ECE}_g\}$. If the maximum subgroup $\text{ECE}$ is substantially higher than the global $\text{ECE}$, the aggregate metric is concealing a real problem.

| Subgroup | N | Base rate | Global ECE (reference) | Subgroup ECE | Subgroup MCE | Flag (Y if subgroup ECE > 2× global) |
|---|---|---|---|---|---|---|
| **Adult, ages 18–64** | 8,420 | 0.034 | 0.018 | 0.019 | 0.041 | N |
| **Pediatric, ages 0–17** | 1,210 | 0.012 | 0.018 | 0.029 | 0.062 | **Y** |
| **Elderly, ages 65+** | 2,850 | 0.078 | 0.018 | 0.044 | 0.091 | **Y** |
| **Pregnancy-related** | 380 | 0.022 | 0.018 | 0.071 | 0.118 | **Y** |
| **Rare-disease cases** | 95 | 0.420 | 0.018 | 0.103 | 0.176 | **Y** |
| **Global (aggregate)** | 12,955 | 0.041 | — | 0.018 | 0.039 | — |

*This table, completed for every deployment, makes the aggregate-mask failure mode visible before it reaches patients.*

### Temperature scaling: the fix and its limits

When a deployed model is overconfident — the most common miscalibration pattern — temperature scaling is the simplest post-hoc correction. The model's logit outputs (before the softmax) are divided by a single learned scalar $T > 1$:

$$p_i^{\text{scaled}} = \text{softmax}(z_i / T)$$

For $T > 1$, this flattens the probability distribution, reducing overconfidence. For $T < 1$, it sharpens the distribution. The parameter $T$ is learned by minimizing the negative log-likelihood on a held-out calibration set after the model's weights are fixed.

Temperature scaling preserves model accuracy (it does not change which class is predicted, only the probability assigned) and is computationally trivial. These properties explain its prevalence. Its limitations are structural:

- Temperature scaling applies a single correction to all predictions. It cannot correct miscalibration that varies by confidence level, by input type, or by subgroup.
- Temperature scaling calibrated on one distribution does not transfer to another. A model temperature-scaled on validation data from one hospital will likely be miscalibrated when deployed at a different hospital.
- Temperature scaling addresses the symptom (overconfident numbers) without addressing the cause (what the model learned that made it overconfident). A miscalibrated model that has been temperature-scaled is not a well-calibrated model. It is a miscalibrated model whose outputs have been adjusted.

The Platt scaling and isotonic regression alternatives offer more flexibility at the cost of more parameters and greater overfitting risk on small calibration sets. Isotonic regression, being non-parametric and monotone, can in principle fit any miscalibration pattern — but it will overfit the calibration set if it is small, and overfitting here degrades exactly the calibration you were trying to improve.

None of these methods address distribution shift. When the deployment population differs from the calibration population — which is the normal situation for a model deployed across multiple sites, over time, or on a population with different demographics — post-hoc calibration on historical data is not a calibration guarantee for the current deployment.

<!-- → [IMAGE: Temperature scaling effect diagram — two reliability diagrams side by side. Left: pre-scaling, curve below diagonal (overconfident). Right: post-scaling with T=1.8, curve closer to diagonal. Annotation: "T>1 flattens the distribution. The ranking of predictions is unchanged." Below both diagrams: two small panels showing "calibration set" and "deployment set" with an arrow between them labeled "distribution shift" and a note: "Temperature scaled on the calibration set. The deployment set is not the calibration set." Caption: "Temperature scaling corrects the symptom. It does not transfer across distribution shift." Figure 12.6] -->

### From calibration metrics to trust claims

Now the connection to the verb taxonomy.

A model with $\text{ECE} = 0.03$ on its validation set is a model for which I can reasonably *find* that calibration is adequate on that set. The calibration finding is grounded in a specific metric on a specific evaluation. This supports the verb *find*.

If I have run subgroup calibration analyses and all subgroup ECEs are within 2× the global ECE, I can reasonably *find* calibration is adequate across the tested subgroups. I still cannot *conclude* that the model is calibrated in the deployment, because deployment distribution shift may invalidate the calibration set.

If the model has been validated externally, the calibration holds under distribution shift, and I have subgroup analyses, I can *show* calibration is adequate for this deployment — using *show* as the strongest defensible verb, not *conclude* or *demonstrate*.

The table that closes the analysis:

| Evidence available | Warranted verb for calibration claim |
|---|---|
| Single evaluation set, ECE reported, no subgroup analysis | *observe* |
| Multiple evaluation sets, ECE consistent, no subgroup analysis | *find* |
| Multiple evaluation sets, subgroup analysis, ECE acceptable | *find* |
| External validation, subgroup analysis, distribution match documented | *show* |
| External validation + subgroup + prospective study | *demonstrate* |
| Formal proof of calibration guarantee (conformal prediction) | *prove* (with stated assumptions) |

This table is not decoration. I use it to write Layer 2. Every calibration claim in a validation report should be traceable to a row in this table, and the verb in the prose should match the row.

| Evidence level | Warranted verb | What is established | What remains uncertain | What evidence would move to the next row |
|---|---|---|---|---|
| **L0 — internal-only ECE** | hypothesize | The model's reliability diagram has been examined on the training set | Generalization, subgroup behavior, deployment shift | Held-out evaluation on a non-training split |
| **L1 — held-out test ECE** | observe | Calibration on a held-out split from the same source | Subgroup variation, distribution shift | Subgroup decomposition |
| **L2 — subgroup ECE** | find | Subgroup-specific calibration patterns identified | Generalization across sites, across time | External replication |
| **L3 — replicated subgroup ECE** | suggest | Pattern holds across at least one independent site or cohort | Causal mechanism; deployment-context behavior | Stress-test under named distribution shift |
| **L4 — replicated under stress** | indicate | Pattern survives a named distribution shift | Whether the deployment population matches the validated population | A monitored deployment with calibration tracking |
| **L5 — validated in deployment** | demonstrate | Calibration holds under live deployment conditions | The next regime; novel subpopulations not in the validation set | (Subsequent regimes require fresh validation) |

*The verb follows from the evidence. The table makes the derivation explicit and the upgrade path visible.*

### The conformal prediction guarantee — and what it costs

Conformal prediction offers something the metrics above do not: a provable finite-sample coverage guarantee. For a given significance level $\alpha$, a conformal predictor produces a prediction set $C(x)$ such that:

$$P(y \in C(x)) \geq 1 - \alpha$$

This holds regardless of the model architecture or the data distribution, subject to one assumption: exchangeability of the data (a condition weaker than i.i.d., requiring only that the joint distribution is invariant to the ordering of data points).

The mechanism: after training a base model, compute a *non-conformity score* $s_i$ for each instance in a held-out calibration set — a measure of how unusual the instance appears to the model. Compute the $(1-\alpha)$-quantile of these scores, call it $\hat{q}$. For a new test instance, include in the prediction set all labels for which the non-conformity score is at most $\hat{q}$.

For a binary classifier, this often reduces to choosing a probability threshold that guarantees the coverage level. The cost is that the prediction sets may be larger than a single label — the model may need to say "positive or negative, I'm not sure" for ambiguous cases. This is not a failure. It is the model being honest about its uncertainty in a formally grounded way.

The critical limitation: the coverage guarantee is *marginal*, not conditional. It holds on average over test instances drawn from the same exchangeable distribution as the calibration set. It does not hold for specific subgroups or for specific inputs. A conformal predictor can satisfy its marginal guarantee while systematically failing on a minority subgroup — and the subgroup failure is not visible from the global coverage guarantee.

Distribution shift breaks the exchangeability assumption. When the deployment population differs from the calibration set, the conformal guarantee no longer applies. This is not a theoretical concern: it is the dominant failure mode in deployed medical AI. The conformal guarantee is a guarantee about the calibration population, not about the deployment population.

The verb warranted by conformal coverage: *prove* — but only for the exchangeability-holding case. When deployment involves distribution shift, *show* is the strongest defensible verb, with the assumption explicitly documented.

<!-- → [INFOGRAPHIC: Conformal prediction mechanism — three panels. Panel 1: calibration set with non-conformity scores shown as a sorted bar chart, (1-α)-quantile marked. Panel 2: test instance with its non-conformity score compared to q-hat, prediction set shown. Panel 3: two deployment scenarios — same population ("marginal guarantee holds") and shifted population ("exchangeability violated, guarantee does not apply"). Caption: "Conformal prediction proves the guarantee holds under exchangeability. Distribution shift is not exchangeability." Figure 12.8] -->

### What calibration metrics cannot see

A clean list before moving on.

Calibration metrics measure whether the model's stated probabilities match empirical frequencies. They do not measure whether the model is answering the right question. The Epic Sepsis Model was "calibrated" in a narrow sense — within score buckets, the base rates were approximately consistent. The model was answering the wrong question: it was encoding clinician suspicion rather than predicting sepsis onset. No calibration metric catches this. The construct validity failure — the gap between what the model predicts and what the deployment needs predicted — is upstream of calibration measurement.

Calibration metrics measure average agreement between probabilities and frequencies. They do not measure whether the probabilities are *useful* for the decision being made. A model with perfect calibration but no resolution (predicting the base rate for every instance) has ECE = 0 and is completely useless for triage. The Brier decomposition separates these — which is why the decomposition matters more than the raw score.

Calibration metrics measure what was observed in the evaluation set. They do not project to the deployment environment. Distribution shift, population drift, temporal non-stationarity — none of these are visible in a calibration metric computed on historical data. The metric is honest about the evaluation; the evaluation may not be representative of the deployment.

These are not failures of calibration metrics. They are the scope boundary of what calibration metrics measure. The supervisory work continues past the metric, into the construct, the deployment context, and the validation design. The metric is necessary. It is not sufficient.

| Failure mode | What it looks like | Why standard metrics miss it | What would catch it instead |
|---|---|---|---|
| **Construct validity failure** | Calibration is excellent on the label, but the label measures the wrong thing for the deployment question | ECE / MCE assume the label is the construct; they cannot diagnose the gap between proxy and target | Construct review with a domain expert; explicit label-to-construct mapping in the model card |
| **Calibration without usefulness** | Probabilities are well-calibrated but cluster near the base rate; the model cannot rank cases | Calibration metrics treat all probability values equivalently; they don't reward discrimination | AUROC or precision-recall; decision-curve analysis |
| **Distribution shift** | Calibration was good in evaluation but the deployment population has shifted | Static evaluation cannot see live-population drift | Deployment-time calibration monitoring with drift alarms |

*The metric is honest about the evaluation. The evaluation may not be representative of the deployment. These are different problems.*

---

## Saying you do not know in writing

Uncertainty visualization is one part of communicating uncertainty. We covered that in the previous chapter. Uncertainty in prose is the other part, and it is harder. Error bars are a known visual primitive. Saying, in writing, *I am uncertain in this specific way for this specific reason* requires more skill, because prose has no error bars.

A few moves that work.

The first move is to specify the kind of uncertainty. *We are uncertain about X because the test set is small / the deployment distribution may differ / the labeling process is noisy / the metric is sensitive to the choice of threshold.* Naming the reason is more useful than asserting the uncertainty.

The second move is to quantify when possible and hedge specifically when not. *The 95% confidence interval is [0.81, 0.89]* is more useful than *the result is approximately 0.85*. When confidence intervals are not available, name what you would need to construct them and why it is not available.

The third move is to distinguish epistemic from aleatoric uncertainty. Epistemic uncertainty is uncertainty in your knowledge — it could be reduced with more evidence. Aleatoric uncertainty is uncertainty in the system itself — it is irreducible. A model's uncertainty about a rare demographic subgroup it has never seen is epistemic: more data would reduce it. A model's uncertainty about individual outcomes in a genuinely noisy system is aleatoric: more data will not help. Conflating the two produces hedges that read as either timid or evasive.

The fourth move is to avoid the throat-clearing hedge. *We note that further work is needed* is a phrase that conveys no information. If further work is needed, name the specific further work. If you do not know what further work is needed, the hedge is doing rhetorical work the analysis cannot back. Strike the sentence. The reader is owed a specific gap or no gap claim at all.

The fifth move is to state what would change your mind. The phrase appears at the bottom of every chapter. It belongs in your validation writing too. *The finding above would be revised in the face of evidence X.* The reader can evaluate, if they have evidence X, whether to expect a revision. The forward commitment is more honest than the bare statement, and — this is the part I keep finding surprising — it is also easier to write, because it gives you a structured place to put the qualifications you would otherwise scatter through the prose.

---

## Why solitary review does not work — and the peer critique protocol

Validation writing is not a solitary activity, and I want to name why, because the field treats it as one.

The reason is structural. You cannot fully evaluate your own writing for verb-evidence calibration mismatches, because you wrote the sentences with the strongest verbs that felt true to you, and the feeling was a function of how the evidence sat in your head when you wrote — which is no longer accessible to you when you re-read. The mismatches you produced are exactly the ones you cannot see. *Your blind spots are blind to you.* This is not a moral failing; it is a fact about how writing works.

The structural solution is collective. Other readers can see the mismatches, because they did not write the sentences and the evidence does not sit in their heads in the way that produced the verbs. This is why peer critique is part of any honest validation infrastructure — not because two opinions are better than one, but because there is a class of error that is invisible to the person who made it and visible to anyone else.

The trick to making it work is that the critique has to be specific. *Your verbs are too strong* is not a useful comment. *In §3.2 you wrote "we conclude" but the supporting evidence is a single test set without significance testing — "we observe" would match the evidence* is useful. The same rule applies to uncertainty hedges, layer separation, and limitations.

The structured peer critique protocol:

1. **Read the draft.** Once for content, once for structure.
2. **Identify three things that work.** Specifically. Not "well-written" but "the data validation section uses the §5 procedure from Chapter 5 effectively because [specific reason]." The praise is diagnostic, not social.
3. **Identify three places where the verb taxonomy is mismatched.** Name the verb, the sentence, the evidence the verb requires, and the verb that would match the evidence.
4. **Identify three places where uncertainty in prose is missing or evasive.** Which hedge is throat-clearing? What specific gap could replace it? Which uncertainty is unnamed?
5. **Identify one structural concern.** Where does the draft's organization make the argument harder to follow than necessary, and what alternative organization would help?
6. **Pose one question the draft does not answer.** A question that, if answered in the next revision, would strengthen the work.

The receiving student gets multiple critiques and is not expected to incorporate every comment. Many comments will conflict. The synthesis is to *integrate the critiques into a sharpened argument* — a revision that addresses the substantive issues and stands behind the choices the writer is making despite some of the comments. The critique-given matters as much as the critique-received: the ability to find calibration mismatches in a peer's work is the same skill as finding them in your own, and the external direction makes the blind spots visible.

This is a Chapter 4 callback in operational form. The Frictional method made the prediction-lock the load-bearing element of individual work. Peer critique makes *the inability to recognize one's own blind spots* the structural problem the cohort solves together.

---

## The verb taxonomy applied to AI output

A useful turn — and this one matters specifically for the kind of work this book is about.

The verb taxonomy is not just a tool for human writers. It applies to AI output as well, and using it as a checking instrument is one of the most operationally useful supervisory moves available.

When an AI produces a paragraph that contains *"this conclusively demonstrates that X"* — what is the verb's evidentiary requirement? *Conclusively demonstrates* is the strongest verb in the taxonomy short of *prove*. The evidentiary requirement is full analysis, alternative-explanation ruling-out, replication, sensitivity analysis. Did the AI perform any of those? Has the AI's evidence been independently checked?

If the answer is no, the AI's verb is unwarranted. The supervisor's move is to replace *conclusively demonstrates* with *suggests* or *observes*, and to explicitly note that the stronger reading is not yet warranted.

Think of this as the verb taxonomy *operating as a fluency-trap detector*. AI outputs reach for strong verbs because the language models behind them were trained on text that frequently uses strong verbs, often when not warranted. The supervisor reading AI output should treat the verb itself as a flag. *What is the evidentiary base for this verb? Is the base sufficient?*

In practice, downgrading verbs in AI output is one of the highest-leverage editing moves you can make. It is also one of the most defensible — the underlying claim does not change. The calibration of how the claim is presented changes. Most AI-generated paragraphs are improved by one or two verb downgrades, and the resulting paragraph reads more like the work of a careful engineer than the work of an enthusiastic press release.

<!-- → [IMAGE: Annotated AI-generated paragraph — four to six sentences, each strong-verb usage circled in one color, appropriate downgraded verb written above it in another color. Margin annotations show the evidentiary gap that motivates each downgrade. Example: "conclusively demonstrates" → "suggests," annotated "no replication, no significance test." Student uses this as a model for annotating their own AI-output review exercises. Figure 12.10] -->

---

## What survives review

A clean note for the engineer about to draft anything that an adversarial reader will eventually see.

The structure that survives review tends to look like this. A Layer 1 summary at the top — what the work found, what it did not find, what the deployment implication is, in plain English. A method section with the validation pipeline. A findings section with verbs calibrated to evidence and uncertainty named specifically. A calibration metrics section reporting the Brier score (decomposed), ECE (with binning specification and subgroup breakdown), reliability diagram, and — for safety-critical deployments — MCE. A limitations section that is real, not performative — names the actual things the analysis could not catch and what would change to catch them. An explicit *what would change my mind* section. An AI use disclosure as a structured appendix. A reproducibility appendix with code, data, and analysis trails.

The structure is not elegant. It is *legible to an adversarial reviewer*, which is the relevant property. A reviewer can scan, locate any specific claim, find its evidentiary base, find its limitations, find the AI use, find the reproducibility detail. The reviewer's job becomes possible. Most writeups make the reviewer's job harder than it needs to be, often because the writeup was structured for the writer's convenience and not the reader's.

The pivotal move is to write for the adversarial reviewer. Not to defeat them. To *support* them. The reviewer is your validation collaborator. The structure should make their work easy. If your writeup is hard to review, your validation is, in practice, weaker than it would otherwise be — not because the analysis is bad but because the analysis is harder for anyone else to use.

---

## Glimmer 12.1 — The peer critique as collective synthesis

A Glimmer is a longer, higher-stakes exercise. This one is the operational form of the cohort-as-validation-infrastructure claim.

1. Submit your research project draft for peer critique.
2. Receive critiques from two peers using the six-step protocol in the section above.
3. Write the synthesis: which substantive issues you are addressing, which comments you are accepting, which you are pushing back on and why, and how the revised draft will respond to each.
4. Submit the revised draft alongside the synthesis.

Two additional deliverables:

5. Submit the critiques you provided to two other peers.
6. *Lock your prediction* before reading the receiving peer's synthesis: which of your critiques will they accept, which will they push back on, which will they ignore? State the prediction with stakes. Compare against what they actually did. The gap is the learning event.

The grade is on three things: the critique-given (rigor and specificity per the six-step protocol), the synthesis (coherence and honesty about what was changed and why), and the prediction-vs-result gap on step 6.

The cohort is functioning if the critiques surface real calibration issues; the cohort is over-functioning if the critiques are converging on a single preferred voice; the cohort is under-functioning if the critiques are too polite or too generic to be useful. The Glimmer makes each of these failure modes visible — and the failure mode itself is pedagogically useful information about the cohort's collective calibration.

---

## Where this leaves us

The verb of a claim is calibrated to the evidence. The verb taxonomy is the working tool, and most engineering writing reaches for verbs one or two notches stronger than the evidence supports. Audience layering supports technical and non-technical readers in the same document without losing nuance to translation. Uncertainty in prose is harder than uncertainty in visualization and requires specific naming, quantification where possible, and the distinction between epistemic and aleatoric uncertainty.

Calibration metrics — Brier score, ECE, reliability diagrams, MCE, subgroup breakdowns — are the numerical grounding for the verbal calibration. The Brier decomposition tells you whether the problem is discrimination, calibration, or base rate. The reliability diagram tells you the direction and shape of miscalibration. Subgroup ECE tells you whether the aggregate metric is masking a local failure. Temperature scaling corrects the symptom; it does not address the cause and does not transfer across distribution shift. Conformal prediction provides a provable guarantee under exchangeability; that guarantee dissolves under distribution shift. The calibration evidence ladder maps from available evidence to warranted verb, closing the loop between metrics and prose.

Peer critique is collective validation infrastructure, structurally necessary because your blind spots are blind to you. The structural form of a writeup that survives review is legible to the adversarial reviewer.

This chapter is the second half of the communication act. The previous chapter covered the visual side. This one covers the textual side. Together they are the supervisory capacity for *communicating validation findings*, which is, structurally, where validation work meets its readers.

The next chapter pivots. We have validated a system, mapped our delegation, communicated the findings. But when a system fails — and our validation missed it — *who is responsible?* That question is the next chapter, and it is where the counterfactual we opened earlier closes. The accountability question has been hanging over the book since Chapter 1. We are about to give it the answer the book can give.

---

**What would change my mind.** If a tool emerged that automatically calibrated verb choices in technical writing against the underlying evidence — across diverse domains, with reliability against engineer-default overclaiming — the verb-taxonomy framing of this chapter would weaken to "the writer's checklist that the tool implements." Some grammar tools are partial steps in this direction. They do not yet implement the evidentiary check. On calibration metrics: if a single metric emerged that captured discrimination, calibration, and subgroup coverage simultaneously in a way that was robust to distribution shift and did not require binning choices, the multi-metric approach in this chapter would simplify. The Kernel Calibration Error (kCE) is a step in this direction; as of the time I am writing, it has not replaced ECE in widespread practice.

**Still puzzling.** I do not have a clean way to teach the audience layering skill at scale. Some students pick it up quickly; others write for one audience or the other and resist the integration. The instructional pattern that works best, in my experience, is to have students rewrite each other's work for the other audience and observe what is lost. This is labor-intensive. I do not have an efficient version. On calibration metrics: I do not have a clean rule for how subgroup ECE findings should change the deployment decision. The table in this chapter specifies when to report subgroup ECE. It does not specify what ratio of subgroup-to-global ECE should trigger a deployment halt. That threshold is a values question, and I do not yet have a principled way to teach it.

---

## Exercises

### Warm-up

**W1.** Below are five sentences from engineering validation reports. For each sentence, identify the verb used, name the minimum evidence that verb requires, and state whether the evidence described in the sentence is sufficient to warrant the verb. If not, write a replacement sentence with a verb that matches the actual evidence.

(a) "We conclude that the model is robust to distribution shift." (Evidence: tested on one out-of-distribution dataset, no significance test.)

(b) "The data suggest that accuracy degrades in low-light conditions." (Evidence: accuracy dropped from 91% to 78% on a single evening-lighting test set.)

(c) "We observe that precision is 0.84 on the held-out evaluation set." (Evidence: one evaluation run on a clean held-out set.)

(d) "We demonstrate that the system outperforms the baseline." (Evidence: the system outperforms the baseline on three of five benchmarks, two benchmarks show no difference.)

(e) "We find that the failure mode does not occur in production." (Evidence: no failures observed in 200 production queries over two weeks.)

**W2.** Explain in plain language the difference between epistemic and aleatoric uncertainty. Give one example of each from a deployed AI system. For your epistemic uncertainty example, name the specific evidence that would reduce it. For your aleatoric uncertainty example, explain why it cannot be reduced.

**W3.** A colleague gives you this sentence as peer critique: "Your uncertainty section is too hedgy." Using the rules for specific critique from this chapter, rewrite the feedback as a critique that is actually actionable. Your rewrite should name the sentence, the hedge, and what a replacement would look like.

**W4.** A binary classifier achieves the following Brier score decomposition on a validation set with base rate $\bar{y} = 0.20$: Uncertainty = 0.160, Resolution = 0.045, Calibration = 0.028. Compute the total Brier score. Interpret each component: what does the Resolution term tell you about the model's discriminative power? What does the Calibration term tell you about the model's probability honesty? Is this a better or worse score than a model that predicts $\hat{p} = 0.20$ for every instance?

**W5.** An ECE is reported as 0.04. What is the minimum additional information you need before you can evaluate whether this ECE is meaningful? List at least three pieces of context that the number alone does not provide.

---

### Application

**A1.** You are reviewing an AI-generated paragraph from a validation report. The paragraph reads:

> "Our analysis conclusively demonstrates that the model achieves state-of-the-art performance across all evaluated domains. The results clearly show that the proposed approach resolves the fairness concerns raised in prior literature. We therefore conclude that deployment is warranted."

Apply the verb taxonomy to every strong verb in this paragraph. For each: name the verb, state its evidentiary requirement, identify whether the paragraph provides that evidence, and write a replacement sentence with a verb that matches what the paragraph actually supports.

**A2.** You are writing a section of a validation report on a medical triage AI. Your primary audience is clinical informaticists who will make the deployment decision. Your secondary audience is the hospital's legal and compliance team. Your tertiary audience is a technical reviewer who may want to reproduce your analysis.

Write the same finding — "The model achieves 89% sensitivity on the held-out test set; sensitivity on the subgroup of patients over 75 is 81%" — in all three layers: Layer 1 (plain English), Layer 2 (technical detail with the appropriate statistical context), and Layer 3 (specify what would go in the reproducibility appendix, without writing the full appendix). Each layer should be written for its actual audience.

**A3.** Your peer reviewer returns your validation report with this comment on the limitations section:

> "§4.3: 'We note that further work is needed to assess performance on underrepresented populations.' This is throat-clearing. Replace."

Write the replacement. Your replacement should name the specific uncertainty, identify whether it is epistemic or aleatoric, quantify it if possible (or state why quantification is not available), and include a "what would change this" commitment.

**A4.** A deployment partner reads your validation report and says: "The Layer 1 summary says the model is ready. The Layer 2 findings show sensitivity is 12 points lower on one demographic group. You have contradicted yourself."

Diagnose the specific writing failure and explain what went wrong structurally. Is this a verb-calibration problem, a layer-separation problem, a limitations problem, or some combination? Write a corrected Layer 1 summary that accurately reflects the Layer 2 findings without requiring the deployment partner to read Layer 2 to catch the discrepancy.

**A5.** A model has the following calibration profile: global ECE = 0.035 (10 bins), reliability diagram shows modest overconfidence between 0.6 and 0.9. Subgroup analysis: ECE for the primary demographic group = 0.030; ECE for the secondary demographic group (15% of deployment population) = 0.092; ECE for the tertiary demographic group (5% of population) = 0.141.

Using the calibration evidence ladder from this chapter, determine the warranted verb for a global calibration claim. Then determine the warranted verb for a claim about the tertiary subgroup. What do the different warranted verbs imply for how the Layer 1 summary should be written?

**A6.** Apply temperature scaling to the following scenario. A classifier's pre-scaling ECE is 0.11, indicating systematic overconfidence. After temperature scaling with $T = 1.8$, the ECE on the calibration set drops to 0.03. The validation set is drawn from a single hospital over 2019–2021. The deployment target is a network of hospitals across three different health systems, deploying in 2026.

What verb is warranted for the post-scaling calibration claim when applied to the calibration hospital? What verb is warranted for the same claim applied to the deployment network? Why do these differ, and what would close the gap?

---

### Synthesis

**S1.** The chapter argues that peer critique is structurally necessary — not because two opinions are better than one, but because there is a class of error invisible to the writer and visible to anyone else. Identify two other contexts in earlier chapters of this book where the same structural argument appears under a different name. For each one, explain how the logic maps to the peer-critique argument in this chapter.

**S2.** The Brier score decomposition separates discrimination (Resolution) from calibration (Calibration error) and base rate uncertainty. The Epic Sepsis Model case study in this chapter's source material describes a model with acceptable AUC (a discrimination metric) and poor calibration in deployment. Using the Brier decomposition framework, explain mechanically why a model can have high Resolution and high Calibration error simultaneously. What does this combination look like in a reliability diagram? What does it mean for a clinical decision-maker using the model?

**S3.** You are asked to design a peer critique protocol for a cohort of ten engineers reviewing each other's validation reports. The protocol must produce specific, actionable feedback rather than general impressions, and it must be completable in a 90-minute session. Specify: the structure of the session, the criteria reviewers use, the form a comment must take to be considered actionable under your protocol, and what the protocol cannot catch even when executed correctly.

---

### Challenge

**C1.** The verb taxonomy is presented in this chapter as a tool for human writers editing their own work and reviewing AI output. Propose a formal specification for an automated verb-calibration tool — one that takes a paragraph and its evidence base as input and outputs a verb-calibration assessment. Specify: the representation of "evidence base" the tool would require, the decision rule mapping evidence to warranted verb, the failure modes of the tool (cases where it would produce wrong assessments), and the class of verb mismatches it cannot catch even in principle. Your proposal should make clear why this tool, even if perfectly implemented, would not replace the peer-critique infrastructure the chapter describes.

**C2.** The chapter claims that the subgroup ECE table should be included in every deployment validation report, and that a maximum subgroup ECE substantially above the global ECE is a flag requiring response. But the chapter does not specify what ratio constitutes "substantially above" or what response is required. Design a decision framework for subgroup ECE findings: what threshold triggers a flag, what organizational or technical actions each flag level requires, and how the framework handles tradeoffs between subgroup calibration and deployment feasibility. Identify the values questions your framework embeds and explain how a different organization might reasonably set different thresholds.

---

###  LLM Exercise — Chapter 12: Communicating Uncertainty

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** A two-pass audit of your casebook's writing — first a verb-calibration pass against every claim in the case files, then a calibration-metric computation on the prediction-locks you wrote in Chapters 4, 5, and 8. The casebook then goes to peer critique using the chapter's protocol.

**Tool:** Claude chat for the verb audit (it's analytical reading work). Claude Code for the calibration-metric computation. Cowork to apply the rewrites.

---

**The Prompt:**

```
Continuing my Red-Team Casebook. The casebook now contains: System Dossier, Bias-and-Leverage Brief, Frictional journal with locked predictions, Data Frame Audit, Self-Explanation Audit, Defended Fairness Choice, Robustness Probe Results, casebook-index, individual case files (5–11), delegation maps, dashboards.

This chapter teaches:
- VERB TAXONOMY: hypothesize → suggest → find → observe → conclude. Each verb implies a specific epistemic posture; engineers default to "conclude" when "find" or "suggest" is what the evidence warrants.
- THREE-LAYER DOCUMENT: plain English summary; technical detail; reproducibility appendix.
- CALIBRATION METRICS: Brier score, Expected Calibration Error (ECE), reliability diagrams, proper scoring rules. SUBGROUP calibration matters more than aggregate.
- PEER CRITIQUE: solitary review does not work for verb-calibration; collective synthesis catches what self-review misses.

For my casebook, do four things:

PASS 1 — VERB AUDIT (Claude chat):
Walk through every CLAIM in my casebook (case write-ups, dashboards, delegation maps, fairness defense). For each:
- Identify the verb the claim uses (or implies)
- Identify the evidence the claim is built on
- Determine whether the verb is warranted, weaker than warranted, or stronger than warranted
- Mark each over-reach with [VERB] and propose the calibrated rewrite
Flag the FIVE WORST over-reaches with explicit before/after rewrites.

PASS 2 — CALIBRATION METRIC COMPUTATION (Claude Code):
I made prediction-locks in Chs 4, 5, 8 with confidence scores (low/medium/high or numeric). I observed the actual outcomes when I ran the cases in Ch 9. Compute:
- BRIER SCORE on the binary predictions (right vs wrong)
- ECE on the confidence-binned predictions
- A reliability diagram (Mermaid or matplotlib)
If I made fewer than ~10 predictions, the metrics are noisy; report them with their uncertainty (or use Wilson intervals on the bin frequencies). Identify any subgroup of predictions where calibration is notably worse — e.g., predictions about social-coherence cases vs predictions about self-model cases.

PASS 3 — DOCUMENT RESTRUCTURE:
Restructure the casebook into the three-layer form:
- LAYER 1 — Plain English summary (1–2 pages): the core findings, the recommendation, the calibration metric, the limits — in language a non-engineer reviewer could read in 5 minutes
- LAYER 2 — Technical detail (the existing case write-ups, delegation maps, fairness defense, dashboards)
- LAYER 3 — Reproducibility appendix: probe scripts, prediction-lock log, AI Use Disclosure, all primary sources cited
Show me the Layer 1 summary, freshly written and verb-audited.

PASS 4 — PEER CRITIQUE PROTOCOL:
Draft the email I would send to a peer reviewer (a classmate, a colleague, or a domain expert) requesting verb-evidence-calibration peer critique. The protocol from the chapter has structure: what to share, what specific failures to look for, how to format the response. Use it.

Output:
- The verb-audit report with the 5 worst over-reaches and rewrites
- The calibration metrics file (Brier, ECE, reliability diagram, subgroup calibration if applicable)
- The Layer 1 plain-English summary (verb-audited)
- The peer-critique request email
```

---

**What this produces:** A verb-audit report with rewrites, computed Brier / ECE / reliability diagram on your own predictions, the Layer 1 plain-English casebook summary, and a peer-critique request ready to send.

**How to adapt this prompt:**
- *For your own project:* Be willing to send the peer-critique request to an actual peer. Solitary review really does not work — the chapter is right about this.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Recommended for the metric pass — it's the kind of small numeric script that goes faster in Code than in chat.
- *For Cowork:* Save all four outputs to the casebook folder.

**Connection to previous chapters:** This chapter audits everything previous. The Frictional prediction-locks (Ch 4), the case files (Ch 9), the dashboards (Ch 11), and the fairness defense (Ch 7) all get verb-audited and calibration-checked.

**Preview of next chapter:** Chapter 13 builds the responsibility-attribution map for the failures your casebook documents. Who is responsible — the agent's developers, the model provider, the deployer, the user? You'll work the same multi-party analysis that Chapter 13 demonstrates on the §16.5 case, but applied to YOUR cases.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Florence Nightingale** spent the 1850s building — and the 1860s defending — the first sustained public-policy argument that combined explicit statistical evidence with deliberately legible visual communication. Her *coxcomb* polar-area diagrams of Crimean mortality were not decoration; they were the calibrated visual translation of an uncertain estimate into a claim a Parliament could read at the right level of confidence and act on. The chapter's argument — that communicating uncertainty honestly is itself a craft, distinct from running the analysis — is Nightingale's working method, applied to AI outputs whose audiences are usually less statistically literate than the Parliament she addressed.

![Florence Nightingale, c. 1860s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/florence-nightingale.jpg)
*Florence Nightingale, c. 1860s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Florence Nightingale, and how does her use of statistical visualization to communicate uncertain estimates to non-statistical audiences (Parliament, the War Office) connect to the craft of honestly communicating an AI system's confidence to a non-technical audience? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Florence Nightingale"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why *visual* statistical communication can be either honest or misleading, in plain language
- Ask it to compare Nightingale's coxcomb diagrams to the visualization choices in this chapter for an AI confidence interval
- Add a constraint: "Answer as if you're writing the public-facing summary of a model's uncertainty for a non-technical executive"

What changes? What gets better? What gets worse?
