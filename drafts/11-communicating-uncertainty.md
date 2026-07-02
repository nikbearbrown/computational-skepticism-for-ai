# Chapter 11 — Communicating Uncertainty

Here are three sentences reporting the exact same result. In every case the evidence is identical: a model scored 87% accuracy on a held-out test set drawn from the deployment distribution, with no significance test and no confidence interval computed.

- **A:** "We conclude that the new model is more accurate than the prior model."
- **B:** "We find that the new model achieves 87% accuracy on the held-out test set, compared to the prior model's 84% on the same set."
- **C:** "We observe that the new model produces 87% accuracy on this single held-out evaluation; whether the difference from the prior model is statistically significant is not yet established."

The numbers never changed. What changed was the verb — *conclude*, *find*, *observe* — and each verb claims a different amount of evidence. Sentence A claims the question is settled; the evidence doesn't settle it. Sentence C claims exactly what the evidence supports and nothing more. Engineers default to sentence A, and they do it without noticing, because the verb feels like grammar rather than a claim.

It's a claim. The verb of a sentence does epistemic work, and calibrating that verb to the evidence — downgrading it when the evidence is thinner than the verb implies — is, in my experience, the single most operationally useful skill in communicating a validation finding. Here's what I want you to be able to do by the end: **calibrate the verbs in a report you write, mapping every claim to its proof** — and downgrade the verbs in an AI-written claim that someone hands you. Same skill, two directions. This is [IJ]: reading a claim in context and interpreting what it's actually licensed to say.

## The classical move: warranted assertion

Philosophers call the underlying idea *warranted assertibility* — you're entitled to assert something in proportion to your evidence for it. The move is old; what's new is applying it as a mechanical instrument to validation writing, where the verb is the dial. And there's a real-world precedent that proves the dial works at scale: the IPCC's calibrated-language scheme (Mastrandrea et al., 2010), which pins climate assessment language to a defined confidence scale and a set of calibrated likelihood terms, so that "likely" and "very likely" mean specific probability ranges rather than vibes. If a discipline as contested as climate science can hold verbs to evidence, so can we.

Here is the ordering I'm going to freeze and use for the rest of the chapter — weakest claim to strongest:

> **hypothesize** → **suggest** → **observe** → **find** → **show** → **demonstrate** → **conclude** → **prove**

I'm being deliberate about freezing exactly one ordering, because a verb ladder that contradicts itself is worse than none — it gives you false confidence that you calibrated. So: *observe* is weaker than *find* (a single observation under specific conditions is weaker than a result established across variation). *Suggest* sits below *observe* (it's an inference the data is merely consistent with). *Prove* is reserved for mathematics or formal verification. That's the canonical ladder. Every table and exercise in this chapter conforms to it.

One honest complication, so you don't get burned later: this ladder is really flattening a *two-dimensional* thing into one line. "Suggest" and "indicate" measure inferential *caution*; "observe," "find," and "show" measure evidential *strength*. Those are different axes, which is why verb ladders tend to wobble if you're not careful. I've forced them into one line on purpose, and I'll defend the choice: for the practical job of not over-claiming in a validation report, a single defended ladder is more useful than a correct-but-unusable grid. Just know that's what I did.

| Verb | Minimum evidence required | Correct use |
|---|---|---|
| Hypothesize | None; pre-evidence | "We hypothesize that miscalibration concentrates in the elderly cohort." |
| Suggest | Data consistent with X, doesn't distinguish X from alternatives | "These results suggest miscalibration concentrates in the elderly subgroup." |
| Observe | Direct, descriptive; a single dataset under stated conditions | "We observe ECE = 0.04 on the global test set." |
| Find | Established by the analysis; robust to some variation | "We find subgroup ECE exceeds global ECE by 2.3× on the elderly cohort." |
| Show | The evidence demonstrates X; a strong verb | "External validation shows the pattern holds across sites." |
| Demonstrate | Established and replicated | "A prospective study demonstrates the calibration holds in deployment." |
| Conclude | The motivating question is settled; takes a position | "We conclude deployment is warranted for the adult cohort." |
| Prove | Decisive; mathematical or formal | "We prove marginal coverage under exchangeability." |

Most engineering writing sits between *observe* and *find*. Most engineering writing *uses* conclude. That gap is the entire problem.

## Two readers, one document

Before the metrics, one structural point, because how you *layer* a document determines whether the verb calibration survives contact with a reader. Write in three layers. **Layer 1** is a plain-English prose summary at the start of every section, no equations. **Layer 2** is the technical detail — methods, equations, tables. **Layer 3** is the appendices — hyperparameters, code, sensitivity analyses. Layer 1 is not "dumbed down." Plain English is *harder* to write than jargon, because jargon lets you hide an un-calibrated verb behind a technical term. The layered document beats keeping two separate documents, because two documents drift, and every translation between them is a chance to lose the nuance that the calibration was protecting.

## The metrics: is the confidence honest?

Now the machinery. The core question every calibration metric answers is: *when the model says it's 80% confident, is it right about 80% of the time?* If yes, consistently, it's calibrated. If it's systematically off in one direction, it's miscalibrated — and the direction matters.

**The Brier score.** For a binary outcome, it's the mean squared distance between the predicted probability and the actual outcome:

$$\text{BS} = \frac{1}{N}\sum_{i=1}^{N}(p_i - y_i)^2$$

where $p_i \in [0,1]$ is the predicted probability and $y_i \in \{0,1\}$ is the outcome. It runs from 0 (perfect) to 1 (perfectly wrong); a coin-flip classifier at $p=0.5$ scores 0.25. What makes it a *proper scoring rule* is that it's minimized, in expectation, only when the model reports the true probability — so it penalizes the confidently-right-when-you-should-have-hedged case that raw accuracy rewards. And it decomposes into three interpretable pieces:

$$\text{BS} = \underbrace{\bar{y}(1-\bar{y})}_{\text{Uncertainty}} - \underbrace{\text{Resolution}}_{\text{how much predictions vary}} + \underbrace{\text{Calibration}}_{\text{deviation from empirical frequency}}$$

The decomposition is the useful part: a model can have a *low* Brier score by predicting near the base rate every time — honest, and useless for triage, because it has no *resolution*. A model can *rank* cases perfectly and still be miscalibrated, so the numbers you'd act on are untrustworthy. The single collapsed score hides which of those you have. Always decompose. (The decomposition traces to Murphy, 1973; the score to Brier, 1950.)

**Expected Calibration Error.** Bin the predictions into intervals, and take the weighted average gap between mean confidence and mean accuracy in each bin:

$$\text{ECE} = \sum_{m=1}^{M}\frac{|B_m|}{N}\left|\text{acc}(B_m) - \text{conf}(B_m)\right|$$

$M$ bins, $B_m$ the instances in bin $m$, $\text{acc}(B_m)$ the fraction actually positive, $\text{conf}(B_m)$ the mean predicted probability. Perfect calibration gives ECE = 0. You'll hear rules of thumb — well-calibrated deployed models "often" land around 0.02–0.05, and above 0.10 signals systematic miscalibration. Use those as rough practitioner heuristics, not facts: I could not source those specific thresholds to a primary study, so they're [UNVERIFIED], and worse, ECE is *bin-dependent* — its value shifts with the number and width of bins, so no fixed threshold is scale-free. The concrete consequence: an ECE reported without its binning specification is not reproducible. Report the bins, every time. (The ECE/MCE binning definitions come from Naeini, Cooper, and Hauskrecht, 2015.)

**The reliability diagram** plots mean confidence on the x-axis against mean accuracy on the y-axis; perfect calibration is the diagonal. The *shape* of the deviation is diagnostic in a way the single ECE number can't be. Below the diagonal: overconfidence. Above it: underconfidence. An S-curve: overconfident at the extremes, underconfident in the middle. And the dangerous one — well-calibrated in aggregate, badly miscalibrated locally — which the aggregate ECE cannot see at all.

A word on a claim you'll hear repeated: that overconfidence is *the dominant failure mode* in modern deep networks and large language models. Guo, Pleiss, Sun, and Weinberger (2017) did show that modern deep networks — deeper, wider, with weight decay and batch norm — are overconfident relative to older, shallower ones. But "dominant, regardless of architecture" is contested: Minderer et al. (2021) found that newer non-convolutional architectures like vision transformers and MLP-Mixers are often *better* calibrated. So overconfidence is a well-documented and common failure mode in a large class of models — not a universal law, and the extension to LLMs specifically isn't nailed to a single canonical study. Cite Guo for the phenomenon; hold the superlative.

## Where aggregate metrics lie: subgroup calibration and a real body count

Here's the failure that matters most, and it has a real case attached. The **Epic Sepsis Model** — a proprietary sepsis-prediction tool deployed across hundreds of hospitals — had aggregate performance that looked acceptable across the deployed population. Then it was externally validated. Wong et al. (2021), studying 27,697 patients across 38,455 hospitalizations at Michigan Medicine, found an AUC of **0.63** (against a developer-reported 0.76–0.83), a positive predictive value of **12%** — meaning 88% of the alerts fired at clinicians were false alarms — and the model **missed 67% of sepsis cases** (1,709 of 2,552 septic patients). These figures are confirmed, and they're the best-documented real case in the book for a simple, brutal point: the aggregate number can look fine while the deployment is failing.

The tool for catching this is **subgroup ECE** — compute ECE within each subgroup, not just globally:

$$\text{ECE}_g = \sum_{m=1}^{M}\frac{|B_m^g|}{N_g}\left|\text{acc}(B_m^g) - \text{conf}(B_m^g)\right|$$

Report the global ECE *and* the full distribution across subgroups. If the worst subgroup's ECE is much larger than the global figure, the aggregate is a mask.

<!-- → [TABLE: subgroup ECE worked example — columns: Subgroup | N | Base rate | Global ECE (reference) | Subgroup ECE | Subgroup MCE | Flag if subgroup ECE > 2× global. Rows for adult, pediatric, elderly, pregnancy-related, rare-disease, and a global aggregate row. The point: aggregate ECE 0.018 hides subgroup ECEs above 0.10.] -->

There's a deeper trap the Epic model also illustrates, and no calibration metric catches it. The model was "calibrated" in a narrow sense — within its score buckets, the base rates were roughly consistent. But it was answering the *wrong question*: it encoded clinician suspicion rather than predicting sepsis onset. That's a construct-validity failure, and it lives *upstream* of calibration. The metric is honest about the evaluation it was given. It has nothing to say about whether the evaluation represents the deployment. Those are different problems, and only one of them is a math problem.

## Fixes and their limits

**Temperature scaling** divides the logits by a learned scalar $T$ before the softmax: $T>1$ flattens overconfident probabilities, $T<1$ sharpens them, and $T$ is learned by minimizing negative log-likelihood on a held-out calibration set with the model's weights frozen. It preserves accuracy and it's computationally trivial. And here's the honest limit, which I'd underline: a miscalibrated model that's been temperature-scaled is not a well-calibrated model. It's a miscalibrated model whose outputs have been adjusted. A single global scalar can't fix miscalibration that varies by confidence level, by input region, or by subgroup, and it doesn't transfer across a distribution shift — the correction learned at one hospital doesn't hold at the next. Platt scaling and isotonic regression are more flexible and correspondingly easier to overfit. None of them touch distribution shift.

**Conformal prediction** offers something stronger and more honest: a prediction *set* $C(x)$ with a coverage guarantee, $P(y \in C(x)) \geq 1-\alpha$, that holds regardless of model or distribution — *subject to exchangeability* (a weaker condition than i.i.d.). The cost is real: the guarantee is bought with prediction sets that can contain more than one label, the model's honest way of saying "positive or negative, I'm not sure." And the limitation that matters for deployment: the guarantee is *marginal*, not *conditional*. It can hold on average while systematically failing a minority subgroup. Distribution shift breaks exchangeability, which is why it fails in exactly the deployed-medical-AI settings where you'd most want it. The warranted verb: *prove*, but only under exchangeability; under distribution shift, *show*, with the assumption documented. (Angelopoulos and Bates, 2021, is the accessible introduction; Vovk, Gammerman, and Shafer, 2005, is the foundation.)

## Saying "I don't know" in writing

Five moves, because vague uncertainty is worse than none — it signals doubt without letting the reader locate it. **One:** specify the *kind* — small test set, distribution mismatch, noisy labels, threshold-sensitive metric. **Two:** quantify when you can — "the 95% confidence interval is [0.81, 0.89]" beats "approximately 0.85." **Three:** distinguish epistemic (reducible with more evidence) from aleatoric (irreducible system noise). **Four:** kill the throat-clearing hedge — "we note that further work is needed" carries zero information; name the specific work or strike the sentence. **Five:** state what would change your mind.

## The verb taxonomy as a fluency-trap detector

Point the ladder at AI output and it becomes a detector. When an AI hands you "this conclusively demonstrates that X," run the check: did the analysis actually do the work that *demonstrate* requires? If not, downgrade — to *suggests*, or *observes*. AI reaches for strong verbs because it was trained on strong-verb text, so the fluency and the over-claim arrive together. Downgrading the verb is the highest-leverage, most-defensible edit you can make, because the factual content usually doesn't change — only the epistemic posture does. (Be honest that "only the posture changes" is itself a slight over-claim: verbs carry action-warrant, so downgrading *can* change a deployment decision. When it does, that's the taxonomy earning its keep, not failing.)

## Why you can't do this alone

Your blind spots are, by construction, blind to you. The verb-evidence mismatches you produced are precisely the ones you can't see — another reader can. So the calibration has to be social. A workable peer-critique protocol: read the draft twice (once for content, once for structure); name three things that work, specifically; identify three verb-taxonomy mismatches (name the verb, the sentence, the evidence required, and the verb that fits); flag three places where uncertainty is missing or evasive; raise one structural concern; and pose one question the draft doesn't answer. The receiver integrates the critiques into a sharper argument — and is allowed to push back. Write for the adversarial reviewer. Not to defeat them — to *support* them.

## Where this leaves you

The verb is a claim, and you can calibrate it to the evidence with one frozen ladder, from *hypothesize* to *prove*. The calibration metrics — Brier decomposed, ECE reported with its bins, the reliability diagram's shape, subgroup ECE — tell you whether the model's confidence is honest, with the Epic Sepsis Model standing as the confirmed case where the aggregate looked fine and the deployment killed the point. The fixes (temperature scaling, conformal prediction) each buy something real at a real cost, and none of them touches distribution shift. And the whole discipline is social, because the mismatches you can't see are exactly the ones you made.

The previous chapter fought the misleading chart. This one fights the misleading verb — and the verb is harder, because there's no axis to truncate and no color to tilt. There's just the word, quietly claiming more than the evidence gave it.

## Exercises

### BUILD

**B1 — Calibrate the verbs in a report you write; map each claim to its proof.** Take a validation report you're actually writing. For every substantive claim, underline the verb, locate it on the frozen ladder (*hypothesize → suggest → observe → find → show → demonstrate → conclude → prove*), and write next to it the minimum evidence that verb requires. Where the evidence falls short, downgrade the verb — and where it exceeds the verb, you may upgrade. Produce a two-column map: claim → the specific proof (a metric, a table, a test) that licenses its verb. Any claim with no entry in the proof column is the finding of the exercise.

**B2 — Report a calibration metric honestly.** For a model you've built or evaluated, compute the Brier score and decompose it into uncertainty, resolution, and calibration; compute ECE and report it *with its binning specification*; and compute subgroup ECE for at least three subgroups. Write the Layer-1 plain-English paragraph that states, in warranted verbs, what these numbers license you to claim about the model's confidence — and what they don't.

### AUDIT

**A1 — Downgrade the verbs in an AI-written claim someone sent you.** Take a paragraph written by an AI (or forwarded to you as AI-assisted). Mark every over-reaching verb. For the worst offenders, write the before/after: the original verb, the sentence, the evidence the verb demands, whether that evidence is present, and the downgraded verb that fits. Then state, in one sentence per case, whether the downgrade changes any *action* a reader might take — because if it does, the verb was doing more than decorating.

**A2 — Catch the missing binning spec.** You're handed a claim of the form "the model is well-calibrated (ECE = 0.04)." List at least three pieces of missing context that make the number un-reproducible or un-interpretable, and say what you'd have to see before you'd let the verb "well-calibrated" stand.
