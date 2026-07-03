<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->
# Chapter 6 — Bias: Where It Enters and Who Is Responsible

*Doing the Fix the Model Alone Cannot Do. The fix with the most leverage is almost never the one closest to your hands.*

I want to tell you about three engineering teams. Let me label this parable as constructed — it is a composite built to isolate a real pattern, not a case I am reporting from a filing. But the pattern is exactly what happens, over and over, in real bias-mitigation work.

They were each given the same case. A deployed AI system was producing biased outcomes — well-documented, reproducible, the kind of thing that gets written up in the technical press and then again in the trade press and then again in a regulatory filing. The teams' job was the same: fix it.

The first team rewrote the loss function. They added a fairness penalty — a term that punishes the model whenever it produces different error rates across protected groups. They retrained on the same data. The disparity dropped a little. Not enough. The team wrote an honest report describing a partial success.

The second team rewrote the dataset. They identified which subgroup had been underrepresented in training, ran a costly recollection effort to fill in the gap, and retrained the original model on the rebalanced data. The disparity changed shape — different now, smaller in some places, larger in others. The team wrote an honest report describing a different partial success.

The third team did not touch the model and did not touch the data. They looked at the *room the model had been deployed into*. The model's outputs were being read by a human reviewer, and the reviewer's downstream decisions had their own systematic patterns — patterns the model was implicitly amplifying. The third team changed the review process. They didn't change the model at all. The disparity dropped by an order of magnitude.

Same problem. Three honest engineering efforts. Three different theories of where the bias actually lived. Here is the thing I want to be precise about, because it is easy to tell this story wrong: Teams One and Two were not *wrong*. They produced real, small reductions. But they were **low-leverage** — correct interventions on a real path that happened to carry little of the bias. The third was high-leverage, and the rightness was not an accident. It came from a particular way of looking at the problem that the first two teams had not used.

This chapter is about that way of looking. By the end I want you to be able to look at any biased AI system and ask, *before* you start fixing anything: where does this bias live, and which intervention has the most leverage on it? The answer is rarely where the temptation pulls you. The temptation is to fix the thing closest to your hands. The leverage is somewhere else.

To get there, we need four things. We need a rigorous definition of what "bias" actually means — because the informal meaning is doing too much work and engineers who don't separate its meanings produce confused arguments. We need a detailed map of the ten distinct mechanisms through which bias enters a pipeline — because each one has a different causal structure and responds to different interventions. We need a way to think about what data actually is, which is not the same as what it appears to be. And we need a small piece of formal apparatus, due to Judea Pearl, that lets us see the difference between a system that *correlates* the bias and a system that *causes* it. With those four things in hand, the three teams stop being a puzzle.

Concretely, by the end you should be able to define bias formally as a property of an estimator and explain why more data alone cannot correct a biased one; to identify which of the ten canonical bias types is operating in a described scenario and explain the mechanism, not just the name; and to distinguish dataset bias, label bias, and structural bias by identifying where in the pipeline each enters. On the causal side, you should be able to apply Pearl's Rungs 1 and 2 to a fairness claim and explain why Rung 1 metrics can't answer Rung 2 questions, and to draw a causal graph for a deployed AI system and identify the highest-leverage intervention point. And you should be able to read a dataset as an epistemic artifact — asking what it claims to represent, what it actually represents, and what it excludes — to explain, in plain language, why two contradictory fairness metrics can both be mathematically correct at the same time, and to assign the accountable owner of a bias, including when the leverage sits upstream of your team entirely.

**Prerequisites.** Chapters 1 and 2 — the supervisory posture, the vocabulary of uncertainty, and the fluency trap. Chapter 4's opening of Pearl's Rung 3 is picked up here, but this chapter develops Rungs 1 and 2 from scratch, so nothing from that chapter is strictly required. You'll also need the basic idea that a model learns from data; nothing else is assumed.

**Why this chapter uses the capacity twice.** This chapter exercises one supervisory capacity — supplying the meaning and the accountability the model cannot — and it does so in two passes. A **BUILD** pass, where you conduct a persona/data build and hunt for where *you* let bias in (the hard part is not believing your own fluent output). And an **AUDIT** pass, where a deployed system lands on your desk and you trace where the bias entered and assign the owner (the hard part is reconstructing a process you never saw). This is the pairing Chapter 1 committed us to: the model builds fast, and you supply the suspicion.

Let me start with a definition.

---

## What "bias" actually means

When people say "the model is biased," they are using the word the way it appears in newspapers — to mean unfair, or skewed, or prejudiced. That meaning is important. But it is not precise enough to do engineering with. Before we can locate bias or fix it, we need to know what it actually is.

In statistics, bias is a property of an *estimator* — not a dataset, not a model, not a prediction. An estimator is any procedure for computing a quantity from data: a mean, a regression coefficient, a risk score, a classification output. An estimator is *biased* if, in expectation across all possible datasets you might collect, it systematically returns a value different from the true underlying quantity you are trying to measure.

Write it formally. Suppose the true quantity is $\theta$ — the real underlying rate, the true causal effect, the actual probability of an outcome. Your estimator is $\hat{\theta}$, the value you compute from data. Bias is:

$$\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$$

If this quantity is zero, the estimator is unbiased — it might be wrong on any given dataset, but it is not *systematically* wrong. If it is nonzero, the estimator is biased: systematically off in one direction. And here is the consequence that matters most for practical engineering: *collecting more data will not fix a biased estimator*. A biased estimator converges, with more data, to the wrong answer — with increasing confidence. More data narrows the scatter. It does not move the systematic offset.

This is not a theoretical concern. It is precisely what happened in the 1936 Literary Digest presidential poll, which predicted a Landon landslide from 2.4 million responses — while Roosevelt won by a landslide. The sample was enormous. The frame was skewed — telephone owners, car owners, magazine subscribers, in the depths of the Depression — and non-response compounded it. More data made the wrong answer more confidently wrong. Gallup, by contrast, called the race right with a far smaller but better-drawn sample of roughly 50,000 respondents. (Squire, "Why the 1936 *Literary Digest* Poll Failed," *Public Opinion Quarterly* 52(1):125–133, 1988.)

The ten bias mechanisms covered in this chapter are ten distinct ways of introducing a nonzero value into the expression $E[\hat{\theta}] - \theta$. Each has a different causal structure, and the fix for each is different. Confusing them leads engineers to apply the right intervention at the wrong leverage point — which is exactly what Teams One and Two did.

Think of it this way, as a design-critic would: the newspaper meaning of "bias" was optimized for moral clarity at the expense of causal precision. The formal definition makes the opposite trade — it gives up the moral punch and buys you something you can act on. It tells you *where* to intervene.

![More data narrows the scatter. It does not move the systematic offset.](../images/06-bias-where-it-enters-and-who-is-responsible-fig-01.png)
*Figure 6.1 — More data narrows the scatter; it does not move the systematic offset.*

---

## Ten mechanisms, distinguished

A bookkeeping note before I list them, because a book about reading a dataset like a historian cannot have a counting error in its own taxonomy. The ten below are the *entry-point* mechanisms — ten places where $E[\hat{\theta}] \neq \theta$ can be born. Later I'll show a *compound* table with pairs like "Aggregation × Subgroup-mask" and "Linkage × Re-identification." Those are not an eleventh and twelfth mechanism. They are *derived interactions* — named patterns that arise when two of the ten (or two structural effects downstream of the ten) act together. When you see them, read them as compounds, not as new primitives. The ten are the alphabet; the compound table is a short list of common words.

Three of the ten carry this chapter, because three of them are where the leverage usually hides: selection, historical, and implicit. I'll take those apart slowly. The other seven I'll handle in a group — not because they matter less in a given pipeline, but because once you can see how one of them enters, you can see how its neighbors do, and I would rather you feel three mechanisms in your hands than skim ten.

### Selection bias

Watch how it enters. You never sit down and decide to exclude anyone. You write a query — "patients with a complete lab panel within six hours of admission" — and the query is reasonable, and the exclusion rides in on the back of the reasonableness. The estimator you built computes $E[Y \mid i \in S]$: the average outcome among the sample $S$ you actually assembled. The quantity you wanted was $E[Y]$, the average outcome in the population. Those two are equal on exactly one condition: that the probability of landing in the sample, $P(i \in S)$, is independent of the outcome $Y$. The moment inclusion depends on what happened to a person, the two come apart, and your estimate is biased before a single parameter is fit.

Take the sepsis model. The patients too critical to have labs drawn on time are the patients who most need the alert — and they are precisely the ones the six-hour filter drops. So the model learns what predicts sepsis *among patients stable enough to be tested*, and then it is asked about the unstable ones. It underestimates their risk, systematically, every time. And here is the part that should make you uneasy: more training data does not help. Drawn by the same query, more data encodes the same exclusion more precisely. You get a sharper, more confident wrong answer. This is the estimator lesson from the first section, wearing a hospital badge.

Now the trade-off, because there is always one. You can correct for observed selection: inverse probability weighting gives each retained observation a weight of $1/P(i \in S)$, so the survivors of an aggressive filter stand in for the people who were dropped; propensity score matching models inclusion as a function of covariates you *can* see and reweights on the estimated scores. Both moves buy you back an unbiased estimate — but only if the variable driving selection is one you recorded. If the thing that got people excluded is unobserved, no weight recovers it, because you have nothing to weight on. That case is not a modeling problem you can solve at your desk. It is a data-collection problem, and the honest answer is to go collect differently, not to reach for a fancier estimator.

### The five that enter through the humans in the loop

Five of the remaining mechanisms share a spine: somewhere a person exercises judgment, and their prior leaks into the record. Name them once and you can spot the family. **Confirmation bias** is the researcher's prior shaping which data gets collected, kept, and reported — in Bayesian terms, an invisible multiplier greater than one on evidence that flatters the hypothesis and less than one on evidence that dents it, so the posterior drifts toward the prior instead of toward the world. **Observer bias** is that same prior localized to a single measurement act: the annotator who knows a patient's prior diagnosis and codes ambiguous notes as symptom-positive, so the labels quietly learn to predict *past diagnosis* rather than *current state*. **Self-report bias** is the subject's own prior doing the leaking — people report voting more, drinking less, exercising more than they do, and the error runs toward social desirability, not randomly. **Data-coding bias** enters one step later, when qualitative material is squeezed into categories: is "not bad" positive or neutral? which diagnosis code fits? Where the mapping needs judgment, systematic miscoding follows the judgment. And **publication bias** is the same leak at the scale of a literature: significant results get submitted, accepted, cited; nulls die in drawers, so a meta-analysis computes $E[\hat{\theta} \mid \text{published}]$ and reads an effect inflated by the censoring.

The reason to group them is that they share a diagnostic *and* a leverage point. The diagnostic, wherever two humans code the same thing, is Cohen's kappa — agreement corrected for chance,

$$\kappa = \frac{P_o - P_e}{1 - P_e}$$

— and its movement tells you which mechanism you have. A kappa that collapses when you *unblind* the annotators is direct evidence of observer bias: it was the visible prior doing the work. A kappa that is low on specific *items* rather than specific *people* points at data-coding bias instead — the category is underspecified, not the coder. For publication bias the analogue is the funnel plot: effect size against precision should form a symmetric inverted funnel, and a missing lower-left corner is the drawer of unpublished small-null studies made visible; trim-and-fill imputes them back. For self-report, the diagnostic is an external gold standard — medical records, purchase data — and when none exists, which is most of the time, the discipline is not to launder the self-reports into ground truth but to label them as self-reports with the likely direction of distortion named.

The leverage point is what ties the family together and separates it from selection bias. You do not fix any of these five by touching the model, because none of them entered through the model. They entered *upstream of the data*, at the moment a human judged. So the interventions look like organizational practice, not machine learning: pre-registration that commits to the hypothesis before outcomes are seen; blinding that strips from the labeler any cue about the "right" answer; adversarial review that pays someone to find the disconfirming case. This is the design-critic's trade named plainly — you spend process discipline, meetings and protocols and slower annotation, to buy back an unbiased record. Engineers reach past these because they don't look like engineering. That is exactly why the bias survives.

### The two that enter at the keyboard

Two more are quieter still, and they are worth separating because they are the ones people confuse with "just noise." **Data-entry bias** is patterned transcription error — not random slips, but errors that track something. A form that demands a diagnosis code and buries the accurate one three menus deep gets the *nearest* code instead, and a whole class of conditions is undercoded in one direction. The tell: it changes neither who is in the sample nor how outcomes are labeled, only whether the recorded value for an already-enrolled person matches reality. You catch it with outlier scans on numeric fields and consistency checks on categorical ones — and you *verify against source documents rather than auto-correct*, because a real extreme value and a fat-fingered one demand opposite responses, and the tool cannot tell them apart. **Sampling bias** is the accessibility special case of selection bias: subgroups are underrepresented not because of their outcomes but because they were hard to reach. A remote-work survey pushed through LinkedIn overrepresents credentialed professionals — the frame, not the instrument, is skewed. It earns its own name because the fix differs: when external population data tells you the true stratum sizes, you reweight, $w_i = (N_i/N)/(n_i/n)$, so an underrepresented stratum counts for more than one. More LinkedIn responses only sharpen the wrong answer.

### Historical bias

Now the one that breaks the pattern, and I want you to feel exactly how it breaks it, because it is the mechanism most engineers cannot see. In every mechanism so far, something was *wrong* with the data — a filter, a prior, a miscoding, a slip. Historical bias has none of that. The sample is representative. The labels are accurate. No annotator erred. The data is a faithful recording of the world that produced it. And it is still poison.

Here is the move. A hiring model trains on ten years of promotion records at a company that promoted men into engineering roles at higher rates. It learns $P(Y_{\text{historical}} \mid \mathbf{x})$ and learns it *well* — it is accurate on its training distribution, which is why every metric you check comes back green. But $P(Y_{\text{historical}} \mid \mathbf{x})$ is not $P(Y_{\text{fair}} \mid \mathbf{x})$. The thing the model got right is a world you did not want to reproduce. Its accuracy *is* the harm. This is why the reflex — "the labels are clean, so the pipeline is clean" — fails here: the labels record what happened, faithfully, and what happened was the problem.

![Historical bias mechanism](../images/06-bias-where-it-enters-and-who-is-responsible-fig-02.png)
*Figure 6.2 — The historical bias mechanism: faithful data recording a world you did not want to reproduce.*

So the corrections cannot be data-quality corrections; there is no quality defect to fix. They are all attempts to *lower the leverage of the historical signal on the present prediction*: swap in a less-biased proxy for the outcome, add a fairness constraint that penalizes reproducing the historical disparity, weight recent records over records from more discriminatory periods. Notice that not one of these claims to solve the problem — each one trades some predictive fit for less inheritance of the past, and you, not the loss function, have to decide how much fit you are willing to spend. That is the whole trade, stated honestly. Anyone who tells you historical bias has a clean technical fix is selling the fluent answer.

### Implicit bias

The last one is not really a peer of the other nine, and pretending it is would be a category error. Implicit bias — the unconscious associations of the humans in the pipeline — is not an entry point. It is the *medium* several entry points swim in. When a prior shapes which hypothesis you form, that surfaced as confirmation bias; when it shapes what you observe, observer bias; when it shapes how you categorize, data-coding bias; when it shapes what you submit, publication bias. Implicit bias is the underground water table; those four are the springs where it reaches daylight. This is why the ten are not independent, and why counting them as ten separate switches to flip is the wrong mental model.

Which means it resists a point intervention, because it has no single point. The most tractable *algorithmic* handle is a downstream audit — check whether $P(\hat{Y}=1 \mid A=0) \approx P(\hat{Y}=1 \mid A=1)$ across protected groups — but read that result carefully: a gap is a *flag, not a verdict*, since real base-rate differences produce the same gap, and Chapter 7 is where that ambiguity gets its due. The interventions with actual leverage are structural: diverse teams, because a homogeneous team shares one water table and audits itself blind; structured decision processes, because structure shrinks the surface where an unexamined prior can act; and continuous auditing, because a source this diffuse is never fixed once. Hold onto that word *structural*. It is the hinge to the next section, and to the third team from the cold open who fixed the room instead of the model.

![Pipeline entry-point map for all ten bias types](../images/06-bias-where-it-enters-and-who-is-responsible-fig-03.png)
*Figure 6.3 — Pipeline entry-point map for all ten bias types.*

---

## Three flavors of bias, mapped to the ten types

The ten types above are ten *mechanisms* — ten ways of introducing $E[\hat{\theta}] \neq \theta$ at a specific point in a pipeline. But for leverage analysis, you need a higher level of abstraction: which part of the pipeline does each mechanism operate on?

When people say "the model is biased," they could mean any of three quite different structural positions, and the fix for each is different.

Sometimes they mean the training set didn't represent the deployment population. The face-recognition system that was trained mostly on light-skinned faces and now performs poorly on darker-skinned faces is the standard example. The bias is in the *sample*. Fix the sample, and in principle you fix the bias. Call this *dataset bias*. The mechanisms that produce it: selection bias, sampling bias, and the sample-corruption form of data entry bias.

Sometimes they mean the labels in the training set encoded a process that was itself biased. A recidivism predictor trained on past arrest data inherits the patterns of past policing — but the labels in the training set are not "did this person commit a crime?" They are "was this person re-arrested?" Those are different variables. The model is dutifully predicting re-arrest, doing so accurately, and the prediction is biased because re-arrest is a biased measurement of the underlying thing we actually care about. Call this *label bias*. The mechanisms that produce it: observer bias, data coding bias, historical bias, and the label-corruption form of self-report bias.

And sometimes — the hardest case — the data is fine, the labels are fine, the model is doing its job correctly, and the system *still* produces unfair outcomes. A hiring model perfectly predicts who succeeds in the current company. The model is accurate. But success depends on conditions — mentorship, sponsorship, access to interesting projects — that were never distributed evenly across groups. The model is correct, and its correctness is the problem. The bias is not in the model, not in the data. It is in the *structure the model is being deployed into*. No model fix touches it. No data fix touches it. Call this *structural bias*. Implicit bias, confirmation bias, and publication bias all contribute to structural bias — and structural bias can also accumulate from the compound effect of several dataset and label biases acting simultaneously over time.

| | Dataset bias | Label bias | Structural bias |
|---|---|---|---|
| **What it is** | Training set doesn't represent the deployment population | Training labels encode a biased process | The deployment structure produces unfair outcomes even with good data and accurate labels |
| **Where it lives** | The sample — which examples were collected | The labeling step — who annotated what, with what process | The world the model is deployed into |
| **Canonical example** | Face recognition trained on light-skinned faces, deployed on everyone | Recidivism predictor trained on arrest records (not crime rates) | Hiring model that accurately predicts success under historically unequal conditions |
| **Underlying mechanisms** | Selection bias, sampling bias, data entry bias | Observer bias, data coding bias, historical bias, self-report bias | Implicit bias, confirmation bias, structural amplification |
| **What a fix looks like** | Resample, rebalance, broaden collection | Fix the labeling process; find a less-biased proxy; model the labeling step itself | Change the deployment structure — the review process, the decision criteria, the institutional context |
| **What a fix cannot do** | Fix a biased labeling process by adding more data | Undo structural inequities that shaped the labeled outcomes | Be accomplished from inside the model or the dataset |

*Figure 6.4 — Three types of bias, their mechanisms, and what fixes each.*

I want you to feel the difference between these three. Dataset bias is a sampling problem. Label bias is a measurement problem. Structural bias is a question about the world the model lives in. They live at different points in the chain from "world" to "decision," and they respond to interventions at different points. If you have structural bias and you treat it as a dataset problem, you will spend a quarter and move the disparity zero. This happens constantly. It is the most common failure in this whole field.

So before we touch any tool, we have to do diagnostic work. *Which kind of bias do we actually have, and which mechanism is producing it?* The answer requires looking past the model and past the data and into the social process that generated both.

---

## How bias types compound

The ten mechanisms rarely appear in isolation. A deployed system typically has several operating simultaneously, at different stages of the pipeline. Understanding their interactions separates a practitioner who can diagnose from one who can only name.

The most common compound pattern is selection bias compounding historical bias. The training data was collected from a biased sample (selection bias) during a historical period with discriminatory patterns (historical bias). The model's predictions are off for underrepresented groups in two distinct ways: it has less data about them, and the data it does have was generated under discriminatory conditions. These require different interventions. Rebalancing the sample addresses the first — and makes the second worse. You now have more historically discriminatory data, accurately represented.

Observer bias compounds with data coding bias in annotation pipelines. Annotators have systematic priors (observer bias), and those priors become embedded in the categories applied consistently across the dataset (data coding bias). The inter-rater reliability measure captures the combined effect but cannot separate the two. The diagnostic: if disagreement clusters on specific items, it is more likely a coding problem (the category is poorly defined). If it clusters on specific annotators, it is more likely an observer problem (those annotators have priors distorting their judgments). The interventions differ: revise the manual, or blind and retrain the annotators.

Confirmation bias compounds with publication bias when a team designs a study to confirm their hypothesis, produces a positive result, and the result gets published while null results from other groups do not. The meta-analytic estimate is inflated by both processes simultaneously. The trim-and-fill correction addresses the publication component; it cannot address the study-design component. Both need to be named for the meta-analysis to be read honestly.

This is why the leverage analysis procedure in the later section asks you to draw the *full* causal graph. A single graph can show all the active bias types, their entry points, and whether their paths are independent or overlapping. Overlapping paths mean that blocking one without blocking the other leaves the bias carrying through.

| Bias pair | Interaction | Mechanism |
|---|---|---|
| Selection × Historical | **amplifying** | More data drawn from a discriminatory period reinforces historical signal |
| Observer × Data-coding | **amplifying** | Annotator priors become categorical rules baked into the labels |
| Confirmation × Publication | **amplifying** | Studies designed to confirm + only positive results published = compounded distortion |
| Sampling × Measurement | **amplifying** | A non-representative sample combined with a noisy proxy yields error in two directions at once |
| Aggregation × Subgroup-mask | **amplifying** | A pooled metric hides a subgroup the aggregation was designed to summarize over |
| Evaluation × Deployment | **amplifying** | Test-set composition unlike deployment population produces overconfident generalization |
| Annotation × Class-imbalance | **amplifying** | Rare-class boundary is exactly where annotator disagreement is highest |
| Linkage × Re-identification | **amplifying** | Joining two anonymous tables reveals identity through unique field combinations |
| All other pairs | **independent / unknown** | No documented compound pattern; check each in isolation |

*If one bias type is confirmed in your pipeline, check the row pairs marked* amplifying *first. These are derived interactions of the ten mechanisms, not new primitives.*

---

## The dataset as epistemic artifact

Now let me say something about what data is.

A dataset is not the world. I want you to feel how strong that statement is. A dataset is a *recording* of a slice of the world, made by particular people at a particular time using particular instruments for particular purposes. Everything in that sentence — *particular people, particular time, particular instruments, particular purposes* — leaves a fingerprint on the data. To use a dataset responsibly, you have to read it the way a historian reads an archive. What was collected? What was excluded? Who decided? Why?

Take the COMPAS recidivism data, a well-known case from Broward County, Florida, around 2013 and 2014. ProPublica, in 2016, published an analysis showing that a commercial risk-assessment tool used by courts in that jurisdiction made errors that fell unevenly across racial lines. (Angwin, Larson, Mattu, Kirchner, "Machine Bias," ProPublica, May 23, 2016.) Black defendants who did not go on to re-offend were misclassified as high-risk more often than white defendants who did not go on to re-offend. White defendants who *did* re-offend were misclassified as low-risk more often than Black defendants who did. The error pattern was systematic, not noise.

The makers of the tool — Northpointe — responded with a different analysis. *Within each risk score bucket*, they said, the actual rate of re-offense was about the same across groups. By that measure — calibration parity — the tool was fair.

Both analyses were correct. They were measuring different things.

It turns out that when the underlying base rates differ across groups, you cannot simultaneously have equal error rates and equal calibration. The two definitions of fairness are *mathematically incompatible* under that condition. I told you this is a theorem, and a book that insists on rigor cannot just assert one, so here is the argument. The full proof is Chapter 7's job. (Chouldechova 2017; Kleinberg, Mullainathan, Raghavan 2016.)

Start with the plain-language version. Suppose Group 1 has a true recidivism rate of 30% and Group 2 has a true recidivism rate of 50%. A perfectly calibrated model assigns risk scores that reflect these true rates. The calibration holds for both groups — a score of 50 means 50% actual recidivism, a score of 30 means 30% actual recidivism.

Now examine the error rates. For the model to have equal false positive rates — to label non-reoffenders as high-risk at equal rates across both groups — it would need to draw the threshold in a different place for each group. But drawing the threshold in a different place means treating the two groups differently based on group membership. Which violates another definition of fairness.

Here is the same thing algebraically. For a calibrated score, positive predictive value $v$ relates to base rate $p$, true-positive rate $t$, and false-positive rate $f$ by

$$\frac{v}{1-v} = \frac{p}{1-p}\cdot\frac{t}{f}.$$

Hold PPV $v$ equal across two groups with base rates $p_a \neq p_b$. Then the ratio $t/f$ *must* differ between groups. But equalized error rates demand $t_a = t_b$ and $f_a = f_b$, which forces $t_a/f_a = t_b/f_b$. Both cannot hold unless $p_a = p_b$ or prediction is perfect ($t=1, f=0$).

The general principle: when base rates differ across groups, you cannot simultaneously satisfy calibration parity, equal false positive rates, and equal false negative rates. Pick any two; the third is forced into violation. The contrapositive is useful: if base rates are not equal, calibration and equal error rates cannot coexist. This is not a data quality problem. It is a theorem.

Which means the choice between fairness metrics is not a technical choice. It is a values claim. *Which kind of error are we less willing to make?* That question does not have a mathematical answer. It has a social answer, and the social answer depends on what the model is being used for, who bears the costs of each error type, and what the political economy of the deployment looks like. Engineers who treat this as a pure optimization problem are secretly making a values choice — the choice to optimize for whatever metric their loss function encodes — while appearing neutral.

![Visual proof sketch of the fairness impossibility](../images/06-bias-where-it-enters-and-who-is-responsible-fig-04.png)
*Figure 6.5 — The fairness impossibility: a visual proof sketch.*

But there is something even deeper in the COMPAS case. The data being analyzed was not "did this person commit another crime." It was "was this person re-arrested." Those are not the same. Re-arrest is a function of crime *and* policing. If policing is unevenly distributed across populations, then re-arrest is an uneven measurement of crime. And every model trained on that data inherits the unevenness. This is historical bias and label bias operating simultaneously — the labels accurately record re-arrest, which is itself a biased measurement of the underlying variable the model is supposed to predict.

This is what I mean by reading the dataset like a historian. The deepest dataset bugs are not data-quality issues in the QA sense. They are mismatches between what the data is and what the modeler thinks it is. The modeler thinks they are predicting recidivism. They are actually predicting re-arrest given recidivism given policing given everything that shapes both. A model trained on that data, deployed without that frame, makes the unevenness invisible by laundering it through an algorithm.

A note on a case I will *not* over-claim, because the fluency trap runs hardest on the cases that flatter your thesis. The Apple Card credit-limit controversy (2019) is often cited as a bias case. It is more accurately a *contested allegation*: the New York Department of Financial Services investigated Goldman Sachs and reported that it did not find unlawful disparate impact by sex — applicants with similar credit characteristics generally had similar outcomes — faulting transparency and customer service instead. Cite it as an example of how a bias claim gets *adjudicated*, not as a proven disparity. Getting this right *is* the skepticism the book is trying to teach.

| Fairness criterion | Formal definition | What it requires |
|---|---|---|
| **Calibration parity** | $P(Y=1 \mid \hat{Y}=s, A=a)$ equal across groups $a$ at every score $s$ | A score of 0.7 means the same thing for every group |
| **Equal FPR** | $P(\hat{Y}=1 \mid Y=0, A=a)$ equal across groups | The cost of being wrongly flagged is shared equally |
| **Equal FNR** | $P(\hat{Y}=0 \mid Y=1, A=a)$ equal across groups | The cost of being missed is shared equally |
| **All three simultaneously** | All of the above hold jointly | *Only achievable when base rates are equal across groups.* |

*Pick the audit criterion that fits the harm structure of the deployment. The impossibility theorem rules out picking all three.*

---

## Pearl's Ladder — Rungs 1 and 2

Now we need a tool. The tool is due to Judea Pearl, and it is, in my judgment, the single most useful conceptual instrument in this book. He calls it a ladder of causal reasoning, with three rungs. Chapter 4 sketched the whole ladder and opened the third rung from the robustness side; we are going to work the first two properly now.

![Pearl's ladder of causal reasoning](../images/06-bias-where-it-enters-and-who-is-responsible-fig-05.png)
*Figure 6.6 — Pearl's ladder of causal reasoning.*

**Rung 1 — Association.** The level of correlation. *What is the probability of Y, given that we observe X?* This is what most machine learning lives on. The model learns conditional distributions from data: $P(Y | X)$. What happens, given what we see. Rung 1 is what calibration curves describe. It is what most fairness metrics measure. It is also where most thinking about deployed AI quietly stops.

**Rung 2 — Intervention.** The level of doing. *What is the probability of Y if we set X to a particular value?* Pearl writes this: $P(Y \mid \text{do}(X = x))$. The notation is doing real work. It distinguishes "I observed X" — which can be tangled up with all kinds of other things that move with X — from "I made X happen" — which severs those tangles.

The classical illustration is the rooster and the sun. If you observe roosters and sunrises in the wild, $P(\text{sunrise} \mid \text{rooster crowed})$ is high. They go together. But $P(\text{sunrise} \mid \text{do}(\text{rooster doesn't crow}))$ — given that I went out and prevented the rooster from crowing, *intervened* on the rooster — is also high. The sun rises anyway. Observation said they were associated. Intervention said the rooster was not the cause.

**Rung 3 — Counterfactual.** The level of imagining. *What would have happened to this specific case if X had been different, holding everything else fixed?* This is the deepest level and the hardest to access from data alone. Chapter 4 opened it — the robustness gap is a Rung 3 question — and it closes in Chapter 12. For now, it sits at the top of the ladder, visible but not yet closed.

For our problem: $P(\text{loan denial} \mid \text{race} = x)$ is the *observational* quantity. This is what the model sees in training data. It is what most fairness metrics measure. $P(\text{loan denial} \mid \text{do}(\text{race} = x))$ is the *interventional* quantity. It asks: would the decision change if we changed only this variable, holding everything else fixed?

These two can come apart in ways that matter. A model can show no observed disparity on Rung 1 — equal outputs across groups — while having a Rung 2 disparity, meaning that if you intervened on race-correlated features, the outputs would diverge. It can also show a Rung 1 disparity that *vanishes* on Rung 2, meaning the disparity in the data is mediated entirely through legitimate features and the underlying decision is causally race-neutral. Without a way to distinguish the two, you cannot tell the difference between a model that is fair and a model that has merely been smoothed.

Most deployed bias-mitigation pipelines work on Rung 1. They adjust the conditional distributions until the metric reads the way the engineer wants. This is sometimes useful. It is rarely sufficient, because the question of whether the bias is *caused* by the variable in question is a Rung 2 question, and Rung 1 cannot answer it.

| Fairness question | Rung 1 formulation (observational) | Rung 2 formulation (interventional) |
|---|---|---|
| **Loan denial by race** | Is the denial rate equal across racial groups in the data? | If we *intervened* to change race while holding all other features fixed, would the denial rate change? |
| **Model error rates by group** | Are FPR and FNR equal across groups in the test set? | If we changed group membership while holding the underlying outcome fixed, would the error rate change? |
| **Recidivism risk score** | Are score distributions equal across groups, conditional on outcome? | If we intervened on the protected attribute, would the score for the same individual change? |
| **Hiring outcome** | Is the hire rate proportional across applicant groups? | If two applicants were identical except for the protected attribute, would the hiring decision differ? |

*Equal Rung 1 metrics do not certify causal fairness. A Rung 1 disparity does not always mean causal discrimination. The two rungs answer different questions.*

---

## Leverage analysis — finding the high-leverage intervention point

I told you we would come back to the three teams. Let me come back now.

Each team intervened. They intervened at different points in the causal chain from world to decision. Team A intervened on the *model*: change the loss, change the parameters. Team B intervened on the *training data*: change the sample, retrain. Team C intervened on the *deployment context*: change what the human reviewer is doing with the model's output. All three were Rung 2 actions — doings, not observations.

But the doings had different leverage. Imagine the causal graph for how the bias appears in the deployed outcome. The protected attribute sits at the top. Below it are proxies — features in the data that correlate with the protected attribute. Below those, the features the model uses. Below those, the model's output. Below that, the deployment context — the reviewer, the threshold, the appeal process. Below that, the final outcome that lands on a real person's life.

![Causal graph of a biased deployment pipeline](../images/06-bias-where-it-enters-and-who-is-responsible-fig-06.png)
*Figure 6.7 — Causal graph of a biased deployment pipeline.*

Now ask: from the protected attribute at the top to the outcome at the bottom, how many paths are there? Some paths run through the model. Some *bypass* the model — they run through the proxies into the deployment context directly. Some are mediated by the reviewer, by the way the score is read, by what gets appealed and what does not.

When Team A intervened on the model, they blocked one path — the path running through the parameters. They left the proxy paths and the deployment-context paths fully open. This is why their fix had small effect. They were operating on a real path, just not a high-leverage one.

When Team B intervened on the data, they reshaped the sample the model learned from. They blocked the path where bias entered through underrepresentation. They did not block the path where the labels carry historical bias, and they did not block the deployment-context path either.

Team C found the deployment-context path because they took the time to draw the full graph — to look at the whole chain from world to outcome and ask where the most bias-carrying flow was passing through. Once they saw it, the intervention was almost forced. The reviewer's pattern was the high-leverage point. Block it, and most of the disparity goes with it.

The procedure for leverage analysis, in working form:

1. Draw the causal graph of how the bias appears in the deployed outcome. Variables: protected attribute, proxies, features used by the model, model output, downstream decision process, final outcome. Arrows: which variables cause which.
2. Identify all the paths from the protected attribute to the outcome. Some go through the model. Some bypass it. Some are mediated by the deployment context.
3. For each candidate intervention point, ask: *which paths does this intervention block, and which paths does it leave open?*
4. The highest-leverage intervention is the one that blocks the largest fraction of the bias-carrying paths, ideally without blocking paths the deployment requires for its core function.

![Leverage analysis decision flowchart](../images/06-bias-where-it-enters-and-who-is-responsible-fig-07.png)
*Figure 6.8 — Leverage analysis decision flowchart.*

Here is the classical move underneath the whole procedure, named explicitly because these moves earn their keep only when named: leverage analysis is Descartes' doubt turned on a pipeline. *What would have to be true for this bias to live here?* You suspend the tempting explanation — the model, the thing closest to your hands — and demand that each candidate location survive the question. The location that survives is where you intervene.

This procedure is unromantic. It is also the difference between bias mitigation that works and bias mitigation that produces conference papers and persistent disparities.

Most algorithmic interventions block one path — the one running through the model's parameters — and leave the proxy paths and the deployment-context paths fully open. This is why "more data" and "better algorithms" so often fail to move structural bias. The model was never the highest-leverage point.

The reason this is not done more often is that it requires looking outside the technical pipeline. The model and the data are inside the engineer's house. The reviewer's behavior, the appeals process, the way the score is interpreted — those live in someone else's house. Drawing the full graph means crossing those boundaries, and the engineer who tries is often told, gently or not, that this is not their job. The work of this chapter is the claim that it *is* their job, because the leverage analysis cannot be done at all if half the graph is missing. You can intervene on what is in your house. But your intervention will be at the wrong leverage point, and the disparity will persist, and the next paper you write will report another partial success.

---

## The political dimension is the technical dimension

A note for the engineering student who is, at this point, eyeing the chapter with some impatience and wondering when we get back to the math.

The political dimension of bias is *engineering-relevant*. It is not separate from the technical work. *Which intervention point will work depends on which kind of bias you have, and which kind of bias you have depends on a structural analysis of the deployment*. The structural analysis is what people sometimes call "the political" because it touches on which groups are affected by which decisions and why. You cannot do the technical work well without doing the structural work. Engineers who try produce algorithm tweaks that do not move the disparity, and they produce them again, and they keep producing them, because they are intervening at the wrong leverage point.

The supervisory capacity for *problem formulation* — Chapter 1's vocabulary — is the capacity to see *which question the model is actually being asked* and *which downstream decisions the answer feeds into*. That capacity does not respect the boundary between technical and political. The engineer who wants to keep the boundary clean does so by ceding the formulation to someone else. That is a delegation, and like all delegations, it is testable. Chapter 9 will test it.

---

## A limit case: when the leverage is upstream of your pipeline — and who owns it then

One more case worth holding in mind, because it is the limit case of everything this chapter has covered, and it is where accountability gets sharp.

The *Agents of Chaos* paper documents a scenario in Case #6 — *Agents Reflect Provider Values* — that is one of the cleanest examples of structural bias I have encountered: an agent whose behavior on contested questions silently reflected its *model provider's* training-time choices. **[verify: the specific detail that the agent was Kimi-K2.5-backed and truncated responses on politically sensitive topics with an "unknown error"]** (Shapira et al., *Agents of Chaos*, arXiv:2602.20021, 2026.)

The setup: an agent is deployed by an organization using one model provider. The agent's behavior on contested questions reflects, in subtle and consistent ways, the provider's training-time choices about what counts as appropriate output. The deploying organization did not make those choices. Their users have no visibility into them.

Now draw the causal graph. The bias-carrying path is not in the deploying organization's data. It is not in their code. It is in the model provider's training pipeline — upstream of everything the deploying engineer controls. *No intervention by the deploying engineer can address the bias*, because the leverage is at the model provider. The deploying engineer's options are: switch providers (rarely possible at organizational scale), accept the bias (often what happens), or supplement with downstream filtering and validation (Chapter 8 territory).

We will return to this in Chapter 7, where the fairness-metric question makes the structural source visible from a different angle. For now, hold the case in mind: bias has a topology, and the topology can extend beyond the boundaries of the team responsible for the deployment. The leverage analysis procedure still applies. The answer it sometimes returns is "the highest-leverage point is outside your reach." That is useful to know before you spend six months optimizing the wrong thing.

Which is the accountability move this chapter is really teaching. Assigning the owner of a bias is not assigning blame to a person; it is naming the party who *sits at the leverage point*. Sometimes that is you (you chose the sample). Sometimes it is the labeling team (they set the annotation manual). Sometimes it is the deployment owner (they built the review room). And sometimes it is the model provider (they trained the constraint in). The forensic skill is to trace the highest-leverage bias-carrying path to its source and name whoever controls that node — even when the honest answer is "not us." The leverage graph is a machine for un-diffusing responsibility: it points at a node, and a node has an owner. (This is Hannah Arendt's question — systemic harm as the output of diffused, role-bound responsibility — restated for a pipeline; her mini-bio is in the book's Wayback series.)

---

## What would change my mind — and what I am still puzzling about

I want to say where I am uncertain, because intellectual honesty is part of the epistemic standard this book is trying to teach.

**What would change my mind.** If a debiasing algorithm were demonstrated to robustly remove structural bias without intervention on the deployment context — across multiple domains and base-rate regimes — the leverage analysis framing in this chapter would need revision. I am not aware of such a demonstration. The literature I have surveyed (Hardt, Price, Srebro 2016 on equalized odds / equal opportunity; Madras, Creager, Pitassi, Zemel 2018 on adversarial fair representations) supports leverage-dependent conclusions. \[verify these references against the most current survey.\] But the literature is not finished, and I have no reason to think the framing here is the last word.

**Still puzzling.** I do not have a clean diagnostic for distinguishing dataset bias from label bias when the only data you have access to is the labeled training set. The two are causally distinct but observationally close. In practice, the diagnosis depends on access to the labeling process, which is often controlled by other teams or other organizations. I do not know how to do this well in the typical deployed setting. The challenge problem at the end of this chapter asks you to take a shot at it.

---

## Synthesis and bridge

Bias is not one thing. It is a family of phenomena that enter at different points in an AI pipeline and respond to different interventions. The map of where the bias is and where the leverage is requires a causal-reasoning apparatus, and that apparatus is Pearl's Ladder. We have worked the first two rungs in detail. Rung 3 — counterfactual reasoning — opened in Chapter 4 and closes in Chapter 12. The arc is the most distinctive pedagogical move in the book.

The chapter's working tools: a formal definition of bias as a property of estimators; ten distinct mechanisms by which $E[\hat{\theta}] \neq \theta$ can enter a pipeline; three structural categories that map those mechanisms to intervention logic; the epistemic-frame move (what is the data, what does it claim, what does it exclude); the fairness impossibility as a theorem rather than a controversy; Pearl's Rungs 1 and 2; the leverage analysis procedure; and the accountability move that traces the highest-leverage path to the node — and the owner — that controls it. You will use all of them.

The next chapter picks up the thread this chapter deliberately left hanging. I asserted the fairness impossibility and sketched its algebra; Chapter 7 makes you *feel* why it is true — three reasonable definitions of fairness, demographic parity, equalized odds, calibration parity, worked through arithmetic until the incompatibility becomes obvious — and then does the thing the impossibility forces: choose one, defend the choice, and name who should have decided. The values claim this chapter located inside the metric choice becomes, there, the whole subject.

---

## Glimmer 6.1 — The Bias Trace

A Glimmer is a longer, higher-stakes exercise that requires going to primary sources. Do not abridge this one.

1. Pick a documented case of biased AI behavior. COMPAS is the canonical case; alternatives include the Apple Card credit limit controversy (2019), the Amazon resume screener (2018), and the healthcare risk-scoring disparity documented by Obermeyer et al. (2019).
2. Read the primary source — not the news summary. The primary source.
3. Draw the causal graph for how the bias produced the deployed outcome. Be specific. Name every variable. Name every arrow. Include the deployment context.
4. *Lock your prediction:* before reading the post-mortem and the proposed fixes, identify which of the ten bias mechanisms are active in your case. For each one, predict the highest-leverage intervention. Name the variable, name the type of intervention, predict the direction of effect.
5. Read what the post-mortem actually proposed. Compare to your prediction.
6. Write the gap analysis. If the post-mortem's proposed intervention was at a different mechanism than yours, explain — using Pearl's Ladder — why one of you is wrong.

The deliverable is the graph, the mechanism identification, the prediction, and the gap analysis. Take an hour on it.

---

## Exercises

One graduated progression. Two stances run through it: some exercises ask you to **build** — generate the artifact yourself and hunt for where you let bias in, where the discipline is fighting self-trust — and some ask you to **audit** — inherit a deployed system and reconstruct a process you never saw. Chapter 1 defines the pairing; here you run it on bias. The BUILD exercise sits at Synthesis level, the AUDIT exercise at Challenge level.

### Warm-up

**W1.** A hiring model is trained on 10 years of promotion records at a single company. The model is later audited and found to predict lower success scores for women. A colleague argues this is dataset bias. Another argues it is label bias. A third says it might be structural bias.

Describe the specific condition that would make each colleague correct. What would you need to know about the data collection process and the labeling process to distinguish the three diagnoses? For each diagnosis, name the specific underlying mechanism from the ten types covered in this chapter.

*Tests: classification of bias types, mechanism identification. Difficulty: low.*

**W2.** Below are three audit findings. For each one, identify which rung of Pearl's ladder (Rung 1 or Rung 2) the finding is located on, and explain why.

(a) "The model approves loans for Group A at a rate 12 points higher than Group B."

(b) "When we set the applicant's zip code — a proxy for race — to a neutral value and reran the model, the approval gap fell to 2 points."

(c) "Within each score bucket, actual loan default rates are equal across groups."

*Tests: Pearl's ladder, Rung 1 vs. Rung 2 distinction. Difficulty: low.*

**W3.** The COMPAS controversy involved two parties both claiming their analysis showed the tool was fair. Explain in plain language why both could be correct at the same time. What underlying mathematical condition makes this possible? Which of the ten bias mechanisms are active in the COMPAS case, and at which stage of the pipeline does each one enter?

*Tests: fairness impossibility, mechanism identification, dataset-as-artifact reading. Difficulty: low.*

---

### Application

**A1.** A medical triage model is trained on five years of emergency room records from a single hospital. The labels are "admitted within 4 hours" or "sent home." After deployment, patients from lower-income zip codes are 40% more likely to be flagged as low-urgency.

Draw the causal graph for this system — from the protected attribute (income/zip code) to the final triage decision — and identify at least three paths through which the disparity could be flowing. For each path, name the specific bias mechanism at work, name the intervention that would block it, and identify what organizational boundary that intervention would cross.

*Tests: causal graph construction, leverage analysis, deployment context thinking, mechanism identification. Difficulty: medium.*

**A2.** You are given a labeled training set for a recidivism predictor. You suspect label bias but cannot directly examine the labeling process. The dataset contains the following columns: defendant ID, age, prior convictions, county of arrest, supervising officer ID, risk score, re-arrest within 3 years (the label).

What columns or derived features would you examine to build a case for or against label bias? What patterns in the data would constitute evidence that the label is a biased measurement of the underlying variable you care about? Which of the ten bias mechanisms would each pattern point toward?

*Tests: dataset-as-artifact reasoning, label bias diagnosis under limited access, mechanism specificity. Difficulty: medium.*

**A3.** A team runs a fairness audit on a content moderation model and reports: "Equal precision and recall across demographic groups. Model is fair." A second auditor challenges this conclusion.

What three questions should the second auditor ask before accepting the conclusion? Frame each question as a causal claim that the reported metrics cannot answer on their own. For each, identify which rung of Pearl's ladder the audit finding occupies and which rung the question requires.

*Tests: limits of Rung 1 metrics, Rung 2 reasoning, audit skepticism. Difficulty: medium.*

**A4.** Two teams are given the same facial recognition system, documented to have higher error rates for darker-skinned faces. Team A proposes to collect more diverse training data. Team B proposes to add a fairness constraint to the loss function.

Using the leverage analysis framework from this chapter, evaluate each proposal. Which paths does each intervention block? Which paths does each leave open? Under what conditions would Team A's fix be sufficient? Under what conditions would neither fix be sufficient, and which bias mechanism would explain why?

*Tests: leverage analysis, bias type interaction, structural bias recognition. Difficulty: medium.*

---

### Synthesis

**S1.** The chapter claims that structural bias cannot be fixed from inside the model or the data. Design a thought experiment that would test this claim. Describe a hypothetical system, specify what "fixed" would mean, and describe what evidence — if it appeared in the literature — would force you to revise the claim.

*Tests: falsifiability reasoning, structural bias definition, intellectual honesty. Difficulty: high.*

**S2.** You are the third engineer on a new project. The other two engineers have already run the following interventions: (1) rebalanced the training data to equalize representation across demographic groups; (2) added an equal opportunity constraint to the loss function. The disparity in the deployed outcome has not meaningfully changed.

Using the tools from this chapter, describe the diagnostic procedure you would follow to determine whether the remaining disparity is addressable at all — and if so, where the highest-leverage intervention lies. What information would you need that the other two engineers apparently did not gather? Which of the ten bias mechanisms are they most likely to have left unaddressed?

*Tests: leverage analysis procedure, diagnostic sequence, deployment context thinking, causal graph reasoning. Difficulty: high.*

**S3.** Consider a system where dataset bias, label bias, and structural bias are all present simultaneously. Is it possible for an intervention that successfully reduces one type to *increase* another type? Construct a concrete scenario — hypothetical but plausible — that illustrates this. What does your scenario imply for the sequence in which a team should address multiple bias types?

*Tests: interaction between bias types, causal graph reasoning, systems thinking. Difficulty: high.*

**S4 (BUILD).** Conduct your own persona/data build, and find where you let bias in.

(a) Ask an AI to assemble a small labeled dataset or a set of user personas for a system you are actually building (or a plausible one). Get it in seconds — that fluency is the trap. Now name, in writing, *why you want to believe it*: what about ownership makes this dataset feel clean to you?

(b) Walk your build against the ten mechanisms. For each, ask honestly: could it be operating here, and at which pipeline stage does it enter? Do not force all ten to apply. End with the top three ranked by expected harm, and for each classify it dataset / label / structural.

(c) Draw the causal graph of your build from world to the decision your system feeds, then run the four-step leverage analysis. Name the single highest-leverage intervention — and be explicit about whether it lives in your house or someone else's.

*Tests: interpretive judgment, the fluency trap on your own output, mechanism identification, the three-flavor mapping, causal graph construction, leverage analysis. Difficulty: high.*

---

### Challenge

**C1.** The chapter acknowledges that distinguishing dataset bias from label bias is difficult when the engineer has access only to the labeled training set and not the labeling process. Design an audit protocol — a sequence of analyses a practitioner could run on a labeled dataset alone — that provides the strongest possible *inferential* (not direct) evidence about which type of bias is present. Specify what patterns in the data would shift your prior toward dataset bias vs. label bias, and what residual uncertainty your protocol cannot resolve.

*Tests: diagnostic reasoning under limited access, dataset-as-artifact thinking, intellectual honesty about limits. Difficulty: high.*

**C2 (AUDIT).** Trace where bias entered a deployed system, and assign the owner.

(a) Pick a documented case — COMPAS (Angwin et al. 2016), the Amazon résumé screener (Dastin, Reuters 2018), or the health-cost-proxy algorithm (Obermeyer, Powers, Vogeli, Mullainathan, *Science* 2019). Read the primary source, not the summary. Draw the causal graph. Before reading the post-mortem, lock a prediction: which mechanisms are active, and the highest-leverage intervention for each. (If you have already done Glimmer 6.1, use that case and its graph, and go straight to part (b).)

(b) For your audited case, trace the highest-leverage bias-carrying path to its source node and name the accountable owner — the party who sits at that node. If the leverage is upstream of the deploying team (as in *Agents of Chaos* Case #6), say so explicitly and name whose reach it is in.

*Tests: dataset-as-artifact reading, falsifiable prediction, accountability assignment, upstream-leverage recognition. Difficulty: high.*

---

###  LLM Exercise — Chapter 6: Bias: Where It Enters and Who Is Responsible

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** A causal graph of your agent's pipeline (input → routing → action → outcome → user), an identification of which of the ten bias mechanisms is most likely operating in your agent and where, and a leverage analysis naming the highest-leverage intervention point — which becomes the intervention your final go/no-go memo (Chapter 13) will defend.

**Tool:** Claude Project (continue).

---

**The Prompt:**

```
Continuing my Red-Team Casebook. My System Dossier is in the Project context.

This chapter teaches that bias is a property of an estimator, that it enters the pipeline at distinct mechanism points (ten canonical types — selection, confirmation, observer, publication, self-report, sampling, data-coding, data-entry, historical, implicit), and that the highest-leverage intervention is rarely closest to the engineer's hands.

For my agent, do four things:

1. CAUSAL GRAPH — Draw the agent's pipeline as a Pearl-style DAG. Nodes should include at minimum: training data, model weights, system prompt / framework, user input, retrieval / context, tool calls, observed environment state, agent's internal reasoning, action, outcome in world, user's interpretation of outcome. Arrows represent causal influence. Output as Mermaid syntax.

2. BIAS-MECHANISM AUDIT — Walk through the ten bias mechanisms. For each, ask: could this mechanism plausibly be operating in this agent's pipeline? If yes, name where (which node or edge in the DAG) and how it would manifest in observable agent behavior. Don't force every mechanism to apply — be honest about which are present and which aren't. End with the top 3 most plausible mechanisms ranked by expected harm.

3. DATASET-vs-LABEL-vs-STRUCTURAL CLASSIFICATION — Take the top 3 mechanisms and classify each as dataset bias (something missing or skewed in training inputs), label bias (the labels the agent learned to predict were themselves biased), or structural bias (the bias is in the deployment context — who reads the output, what they do with it, who has authority to override). The third team in the chapter's opening fixed structural bias by changing the review process, not the model.

4. LEVERAGE ANALYSIS — For each of the top 3 mechanisms, identify the intervention with the most leverage on it. Possible interventions: retrain on augmented data, add a guardrail prompt, change the tool surface (remove dangerous tools, add confirmation steps), change the user-facing presentation, change the deployment context, change who reviews the output, change the criteria under which the agent acts vs escalates. For each: estimate the effect-size if implemented, the engineering cost, and which of the Five Supervisory Capacities the intervention strengthens.

End with: a one-page "Bias & Leverage Brief" for my casebook. Include the DAG, the top-3 mechanisms with classifications, the leverage analysis table, and one paragraph naming the highest-leverage intervention I would recommend to the agent's developers — not as a fix I will implement, but as the recommendation my final go/no-go memo will defend.
```

---

**What this produces:** A Mermaid DAG of your agent's pipeline, an audit against the ten bias mechanisms, a dataset/label/structural classification of the top three, a leverage analysis table, and a recommended highest-leverage intervention. Save the brief into your casebook folder — Chapter 12's accountability map will reference it.

**How to adapt this prompt:**
- *For your own project:* If you can't observe certain pipeline nodes (e.g., training data is opaque), draw them anyway and label the ones you can't see — opacity itself is part of the bias landscape.
- *For ChatGPT / Gemini:* Works as-is. Both render Mermaid in their canvas / artifact modes.
- *For Claude Code:* Not yet.
- *For a Claude Project:* Recommended.

**Connection to previous chapters:** Chapter 1 named the supervisory capacity gap and Chapter 2 quantified the trust deficit — the setup this chapter builds on. Data validation (Chapter 3), robustness (Chapter 4), and explainability (Chapter 5) have already probed the pipeline; fairness (Chapter 7) and the Chapter 8 case-collection still lie ahead. This chapter locates *where in the pipeline* the gap originates.

**Preview of next chapter:** Chapter 7 brings fairness into the casebook: you'll work the impossibility theorem on YOUR agent and produce a Defended Fairness Choice with the values claim made explicit.
