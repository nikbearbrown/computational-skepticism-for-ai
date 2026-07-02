# Chapter 6 — Bias: Where It Enters, Who's Responsible

*The fix with the most leverage is almost never the one closest to your hands.*

I want to tell you about three engineering teams. I am going to label this parable as constructed — it is a composite built to isolate a real pattern, not a case I am reporting from a filing. But the pattern is exactly what happens, over and over, in real bias-mitigation work.

Each team gets the same case. A deployed AI system is producing biased outcomes — documented, reproducible, the kind of thing that reaches the technical press, then the trade press, then a regulatory filing. Their job is the same: fix it.

Team One rewrites the loss function. They add a fairness penalty — a term that punishes the model whenever its error rates diverge across protected groups — and retrain on the same data. The disparity drops a little. Not enough. They write an honest report describing a partial success.

Team Two rewrites the dataset. They find the underrepresented subgroup, run a costly recollection effort, retrain the original model on the rebalanced data. The disparity changes shape — smaller in some places, larger in others. They write an honest report describing a different partial success.

Team Three touches neither model nor data. They look at the *room the model was deployed into*. The model's outputs were read by a human reviewer, and the reviewer's downstream decisions had their own systematic patterns — patterns the model was quietly amplifying. Team Three changed the review process. The disparity dropped by an order of magnitude.

Same problem. Three honest efforts. Three different theories of where the bias actually lived. Two of those theories were not *wrong* — they produced real, small reductions — but they were **low-leverage**: correct interventions on a real path that carried little of the bias. The third was high-leverage, and the difference was not luck. It came from a way of looking at the problem the first two teams did not use.

Here's what this chapter is actually about: that way of looking. By the end I want you to be able to look at any biased system and ask, *before* you fix anything — where does this bias live, and which intervention has the most leverage on it? The temptation pulls you toward the thing closest to your hands. The leverage is somewhere else.

**Learning objectives.** By the end you should be able to:

- Define bias formally as a property of an estimator, and explain why more data cannot correct a biased one
- Identify which mechanism is operating in a described scenario — and explain the mechanism, not just name it
- Distinguish dataset bias, label bias, and structural bias by where each enters the pipeline
- Apply Pearl's Rungs 1 and 2 to a fairness claim and explain why a Rung 1 metric can't answer a Rung 2 question
- Draw the causal graph of a deployed system and name the highest-leverage intervention point
- Read a dataset as an epistemic artifact — what it claims to represent, what it actually represents, what it excludes
- Assign the accountable owner of a bias, including when the leverage sits upstream of your team entirely

**Prerequisites.** Chapters 1 and 2 — the supervisory posture, the vocabulary of uncertainty, and the fluency trap. This chapter exercises **Interpretive Judgment [IJ]**: supplying the meaning and the accountability the model cannot.

This chapter runs the capacity twice — a **BUILD** pass, where you conduct a persona/data build and hunt for where *you* let bias in (the hard part is not believing your own fluent output), and an **AUDIT** pass, where a deployed system lands on your desk and you trace where the bias entered and assign the owner (the hard part is reconstructing a process you never saw).

---

## What "bias" actually means

When people say "the model is biased," they mean it the newspaper way — unfair, skewed, prejudiced. That meaning matters. It is not precise enough to engineer with.

In statistics, bias is a property of an *estimator* — not a dataset, not a model, not a prediction. An estimator is any procedure that computes a quantity from data: a mean, a regression coefficient, a risk score, a classifier output. An estimator is *biased* if, in expectation across all the datasets you might collect, it systematically returns a value different from the true quantity you're trying to measure.

Formally. Let $\theta$ be the true quantity — the real rate, the true causal effect. Let $\hat{\theta}$ be what you compute from data. Bias is:

$$\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$$

If this is zero, the estimator is unbiased — wrong on any given dataset, maybe, but not *systematically* wrong. If it's nonzero, the estimator is biased: off in one direction, every time. And here is the consequence that matters most: *collecting more data will not fix a biased estimator*. It converges, with more data, to the wrong answer — with increasing confidence. More data narrows the scatter. It does not move the systematic offset.

<!-- → [INFOGRAPHIC: two dartboard scatters — "unbiased/high variance" (spread around bullseye) vs "biased/low variance" (tight cluster off-center); caption: more data shrinks the cluster, never moves its center] -->

This is not theoretical. It is the 1936 *Literary Digest* poll, which predicted a Landon landslide from 2.4 million responses while Roosevelt won by a landslide. The sample was enormous. The frame was skewed — telephone owners, car owners, magazine subscribers, in the depths of the Depression — and non-response compounded it. More data made the wrong answer more confidently wrong. Gallup called the race right with about 50,000. (Squire, "Why the 1936 *Literary Digest* Poll Failed," *Public Opinion Quarterly* 52(1):125–133, 1988.)

Every mechanism in this chapter is a different way of forcing $E[\hat{\theta}] - \theta$ nonzero. Each has a distinct causal structure. Each responds to a different intervention. Confusing them is how you apply the right fix at the wrong leverage point — which is exactly what Teams One and Two did.

## Ten mechanisms — a note on the count before I list them

I am going to name ten mechanisms, and I want to be honest with you about a bookkeeping problem, because a book about reading a dataset like a historian cannot have a counting error in its own taxonomy. The ten below are the entry-point mechanisms — ten places $E[\hat{\theta}] \neq \theta$ can be born. Later I'll show a *compound* table with pairs like "Aggregation × Subgroup-mask" and "Linkage × Re-identification." Those are not eleventh and twelfth mechanisms. They are *derived interactions* — named patterns that arise when two of the ten (or two structural effects downstream of the ten) act together. When you see them, read them as compounds, not as new primitives. The ten are the alphabet; the compound table is a short list of common words.

The ten: **selection, confirmation, observer, publication, self-report, sampling, data-coding, data-entry, historical, implicit.** I'll compress the mechanics; each is a formula and a diagnostic.

- **Selection bias.** Your sample was drawn by a process whose inclusion probability depends on the outcome. You compute $E[Y \mid i \in S]$; you wanted $E[Y]$. A sepsis model trained only on patients stable enough to get a full lab panel in six hours learns to predict sepsis in *testable* patients and underestimates the genuinely critical ones. Correction: inverse-probability weighting ($1/P(i \in S)$), propensity matching — both fail if the covariate driving selection is unobserved.
- **Confirmation bias.** The researcher's prior shapes what's collected and reported. In Bayes' terms it corrupts the likelihood — a multiplier >1 on confirming data, <1 on disconfirming. The intervention lives *upstream of data collection*: pre-registration, blind analysis, an assigned adversary. These look like org practices, not model fixes, because the bias enters before the data does.
- **Observer bias.** Confirmation bias localized to a measurement act. The annotator who knows the patient's prior diagnosis codes ambiguous language toward it: $E[Y_i - Y_i^*] \neq 0$. Fix at the labeling step — blind the annotator. Measured by a drop in Cohen's $\kappa$ between blinded and unblinded conditions.
- **Publication bias.** The literature is a censored sample of conducted research — significant results get through. A meta-analysis computes $E[\hat{\theta} \mid \text{published}]$, inflated. Diagnostic: funnel-plot asymmetry. Correction: trim-and-fill.
- **Self-report bias.** Participants misreport toward social desirability: $E[X_i - X_i^*] \neq 0$. People report voting more, drinking less. Correction needs an external gold standard; when none exists, report it as self-reported and name the likely direction.
- **Sampling bias.** A selection special case where the mechanism is *accessibility*, not outcome. A LinkedIn survey about remote work overrepresents degreed professionals. Because external population data tells you who's underrepresented, the fix is reweighting: $w_i = (N_i/N)/(n_i/n)$.
- **Data-coding bias.** Mapping qualitative information to categories introduces systematic distortion — "not bad" coded consistently wrong. Diagnostic: inter-rater $\kappa$. Disagreement clustered on *items* means the category is ill-defined; clustered on *annotators* means observer bias.
- **Data-entry bias.** Patterned transcription error — a form that requires a code leads clinicians to enter the nearest findable one, undercoding hard-to-find conditions. The bias is in the tool. Detect by outlier and consistency checks; verify against source, don't auto-correct.
- **Historical bias.** The data is *correct*, and that's the problem. A hiring model on ten years of promotion records learns $P(Y_{\text{historical}} \mid \mathbf{x})$, not $P(Y_{\text{fair}} \mid \mathbf{x})$. No data-quality fix touches it, because nothing was mis-recorded. Mitigations reduce the historical signal's leverage; none fully solve it.
- **Implicit bias.** Unconscious associations in the humans in the pipeline. Not one artifact but the ambient source several others emerge from — it runs *through* confirmation, observer, coding, publication. The ten are not independent.

<!-- → [INFOGRAPHIC: a pipeline (world → sample → labels → model → deployment) with the ten mechanisms pinned to the stage each enters; this diagram is what would surface the ten-vs-compound distinction visually] -->

They optimized the newspaper meaning of "bias" for moral clarity at the expense of causal precision. The formal definition trades the moral punch for something you can act on: it tells you *where* to intervene.

## Three flavors — mechanism mapped to leverage

The ten are mechanisms. For leverage you need one level up: which *part* of the pipeline does each operate on? "The model is biased" collapses three structurally different situations.

**Dataset bias** — the training set didn't represent the deployment population. Face recognition trained on light-skinned faces. The bias is in the *sample*. Mechanisms: selection, sampling, the sample-corruption form of data-entry. Fix the sample, fix the bias.

**Label bias** — the labels encoded a biased process. A recidivism predictor's labels aren't "committed a crime"; they're "was re-arrested." Different variables. The model dutifully, accurately predicts re-arrest, and the prediction is biased because re-arrest is a biased *measurement* of the thing you care about. Mechanisms: observer, data-coding, historical, the label-corruption form of self-report.

**Structural bias** — the hardest. Data fine, labels fine, model correct, outcome still unfair. A hiring model perfectly predicts success in a company where success depended on mentorship and sponsorship never evenly distributed. The model is right, and its rightness is the problem. Mechanisms: implicit, confirmation, publication — *and* the compound accumulation of several dataset and label biases over time.

<!-- → [TABLE: three columns dataset/label/structural bias — rows: what it is, where it lives, canonical example, underlying mechanisms, what a fix looks like, what a fix cannot do] -->

Feel the difference. Dataset bias is a sampling problem. Label bias is a measurement problem. Structural bias is a question about the world the model lives in. Treat structural bias as a dataset problem and you'll spend a quarter and move the disparity zero. That is the single most common failure in this field.

## The dataset as epistemic artifact — and the COMPAS case

A dataset is not the world. It is a *recording* of a slice of the world, made by particular people, at a particular time, with particular instruments, for particular purposes — and each of those particulars leaves a fingerprint. To use it responsibly, read it like a historian reads an archive. What was collected? What was excluded? Who decided? Why?

Take COMPAS — a commercial recidivism risk tool used in Broward County, Florida. In 2016, ProPublica reported that its errors fell unevenly across race: Black defendants who did not re-offend were flagged high-risk more often than white defendants who did not; white defendants who did re-offend were missed more often. (Angwin, Larson, Mattu, Kirchner, "Machine Bias," ProPublica, May 23, 2016.) Northpointe, the maker, replied that within each score bucket the actual re-offense rate was about equal across groups — calibration parity. Both analyses were correct. They measured different things.

I need to prove that both can be right, because I told you this is a theorem and a book that insists on rigor cannot assert one. Here is the argument; the full proof is Chapter 7's job (Chouldechova 2017; Kleinberg, Mullainathan, Raghavan 2016). For a calibrated score, positive predictive value relates to base rate $p$, true-positive rate $t$, and false-positive rate $f$ by

$$\frac{v}{1-v} = \frac{p}{1-p}\cdot\frac{t}{f}.$$

Hold PPV $v$ equal across two groups with base rates $p_a \neq p_b$. Then the ratio $t/f$ *must* differ between groups. But equalized error rates demand $t_a = t_b$ and $f_a = f_b$, which forces $t_a/f_a = t_b/f_b$. Both can't hold unless $p_a = p_b$ or prediction is perfect ($t=1, f=0$). When base rates differ, calibration and equal error rates are algebraically incompatible. That's the theorem, and it means the choice between them is not technical — it is a *values* claim about which error you're less willing to make. An engineer who "just optimizes the loss" is making that values choice while appearing neutral.

But COMPAS has a deeper layer. The data was not "did this person commit another crime." It was "was this person re-arrested." Re-arrest is a function of crime *and* policing. Where policing is uneven, re-arrest is an uneven measurement of crime, and every model trained on it inherits the unevenness. The modeler thinks they're predicting recidivism. They're predicting re-arrest given recidivism given policing given everything that shapes both — and deploying without that frame *launders* the unevenness through an algorithm. That is the deepest kind of dataset bug: not a data-quality defect but a mismatch between what the label measures and what the modeler thinks it measures.

A note on a case I will *not* over-claim, because the fluency trap runs hardest on cases that flatter your thesis. The Apple Card credit-limit controversy (2019) is often cited as a bias case. It is more accurately a *contested allegation*: the New York Department of Financial Services investigated Goldman Sachs and found no unlawful disparate impact by sex — applicants with similar credit characteristics generally had similar outcomes — faulting transparency and customer service instead. Cite it as an example of how a bias claim gets adjudicated, not as a proven disparity. Getting this right *is* the skepticism the book teaches.

## Pearl's Ladder — Rungs 1 and 2

Now the tool. Judea Pearl's ladder of causal reasoning — three rungs. We use the first two here; Rung 3 opens in Chapter 8's neighborhood and closes at the book's end.

**Rung 1 — Association.** *What is $P(Y \mid X)$?* What happens, given what we observe. Most machine learning lives here. Calibration curves live here. Most fairness metrics live here. Most thinking about deployed AI quietly stops here.

**Rung 2 — Intervention.** *What is $P(Y \mid \text{do}(X=x))$?* The `do` operator severs the tangles that ride along with observing $X$. Observe roosters and sunrises together and $P(\text{sunrise} \mid \text{rooster crowed})$ is high. But $P(\text{sunrise} \mid \text{do}(\text{no crow}))$ — go out and silence the rooster — is still high. Observation said associated; intervention said not the cause.

**Rung 3 — Counterfactual.** *What would have happened to this specific case had $X$ been different, everything else fixed?* Hardest to reach from data. It sits above us for now.

For bias: $P(\text{denial} \mid \text{race}=x)$ is observational — what the model sees, what most metrics measure. $P(\text{denial} \mid \text{do}(\text{race}=x))$ is interventional — would the decision change if we changed only race, holding all else fixed? These come apart. A model can show no Rung 1 disparity while having a Rung 2 one, or a Rung 1 disparity that vanishes on Rung 2 because it's mediated entirely through legitimate features. Rung 1 cannot tell a fair model from a merely smoothed one, because *is this bias caused by the variable* is a Rung 2 question and Rung 1 cannot answer it.

<!-- → [TABLE: four fairness questions (loan by race, error rates by group, risk score, hiring) in Rung 1 observational vs Rung 2 interventional formulations — student should see the two rungs ask different questions] -->

## Leverage analysis — and how bias types compound

Back to the three teams. Each intervened — all Rung 2 doings, not observations. Team A on the *model* (change the loss). Team B on the *data* (change the sample). Team C on the *deployment context* (change what the reviewer does). Same kind of action; different leverage.

Draw the graph. Protected attribute at the top. Below it, proxies — features that correlate with it. Below those, the features the model uses; the model's output; the deployment context — reviewer, threshold, appeal; the final outcome on a real life. Now count the paths from top to bottom. Some run through the model. Some *bypass* it — proxies straight into the deployment context. Some are mediated by how the reviewer reads the score.

<!-- → [INFOGRAPHIC: the causal DAG protected-attribute → proxies → features → model output → deployment context → outcome, with multiple paths highlighted; the ones bypassing the model shaded — this figure carries the leverage argument, which is a claim about graph topology] -->

Team A blocked one path — through the parameters — and left proxy and deployment paths wide open. Small effect. Team B reshaped the sample, blocking the underrepresentation path, leaving the label-carried historical path and the deployment path open. Team C drew the *whole* graph, found the reviewer's pattern was where most bias-carrying flow passed, and blocked it. The procedure:

1. Draw the causal graph from world to deployed outcome.
2. Enumerate every path from protected attribute to outcome — through the model, bypassing it, mediated by deployment.
3. For each candidate intervention, ask which paths it blocks and which it leaves open.
4. The highest-leverage intervention blocks the largest fraction of bias-carrying paths without breaking the deployment's core function.

Compounding is why step 1 says *full* graph. Selection compounds historical: rebalance the sample and you fix underrepresentation while giving yourself *more* historically discriminatory data, accurately represented. Observer compounds data-coding: annotator priors harden into categorical rules. Confirmation compounds publication. Overlapping paths mean blocking one and not the other leaves the bias carrying through.

<!-- → [TABLE: compound bias pairs (Selection×Historical, Observer×Data-coding, Confirmation×Publication, ...) with interaction=amplifying and the mechanism of each; note these are derived interactions of the ten, not new primitives] -->

Here is the Cartesian move under all of this, named explicitly because the book's classical moves earn their keep only when named: leverage analysis is Descartes' doubt turned on a pipeline. *What would have to be true for this bias to live here?* You suspend the tempting explanation (the model) and demand that each candidate location survive the question. The location that survives is where you intervene.

The reason this isn't done more: it requires looking outside the technical pipeline. The model and data are in the engineer's house. The reviewer, the appeals process, the way the score is read — someone else's house. The claim of this chapter is that crossing that boundary *is* the engineer's job, because you cannot do the leverage analysis at all with half the graph missing. This is **problem formulation** refusing to respect the line between technical and political — because which intervention works depends on which bias you have, and which bias you have is a structural fact about the deployment.

## When the leverage is upstream of everyone — and who owns it then

One limit case, because it's where accountability gets sharp. *Agents of Chaos* documents an agent whose behavior on contested questions silently reflected its *model provider's* training-time choices — a Kimi-K2.5-backed agent that truncated responses on politically sensitive topics with "unknown error." (Shapira et al., *Agents of Chaos*, arXiv:2602.20021, 2026, Case #6 — "Agents Reflect Provider Values.") The deploying organization made none of those choices; its users had no visibility into them.

Draw the graph. The bias-carrying path is not in the deployer's data or code. It is in the provider's training pipeline — upstream of everything the deploying engineer controls. *No intervention by the deploying engineer addresses the bias.* The options are switch providers (rarely feasible at scale), accept it, or add downstream filtering. Bias has a topology, and the topology can extend past your team's boundary. The leverage analysis still applies. The answer it sometimes returns is: the highest-leverage point is outside your reach. That is worth knowing before you spend six months optimizing the wrong thing.

Which is the accountability move this chapter is really teaching. Assigning the owner of a bias is not assigning blame to a person; it is naming the party who *sits at the leverage point*. Sometimes that's you (you chose the sample). Sometimes it's the labeling team (they set the annotation manual). Sometimes it's the deployment owner (they built the review room). And sometimes it's the model provider (they trained the constraint in). The forensic skill is to trace the highest-leverage path to its source and name whoever controls that node — even when the honest answer is "not us." Hannah Arendt's *Eichmann in Jerusalem* (1963) is the ancestor of this move: systemic harm is rarely the work of a monster; it is the predictable output of a system that diffuses responsibility across so many roles that no one feels accountable. The leverage graph is a machine for un-diffusing it: it points at a node, and a node has an owner.

## What would change my mind — and what I'm still puzzling about

If a debiasing algorithm were shown to robustly remove structural bias *without* intervening on the deployment context — across domains and base-rate regimes — the leverage framing here would need revision. I'm not aware of such a demonstration; the literature I've read (Hardt, Price, Srebro 2016 on equalized odds; Madras, Creager, Pitassi, Zemel 2018 on adversarial fair representations) supports leverage-dependent conclusions. And I do not have a clean diagnostic for distinguishing dataset bias from label bias when all you can see is the labeled training set. They are causally distinct and observationally close. The challenge exercise asks you to take a shot at it.

---

## Exercises

### BUILD — conduct your own persona/data build, and find where you let bias in

**B1.** Ask an AI to assemble a small labeled dataset or a set of user personas for a system you are actually building (or a plausible one). Get it in seconds — that fluency is the trap. Now name, in writing, *why you want to believe it*: what about ownership makes this dataset feel clean to you? *Tests: [IJ], the fluency trap on your own output. Difficulty: low.*

**B2.** Walk your build against the ten mechanisms. For each, ask honestly: could it be operating here, and at which pipeline stage does it enter? Do not force all ten to apply. End with the top three ranked by expected harm, and for each classify it dataset / label / structural. *Tests: mechanism identification, the three-flavor mapping. Difficulty: medium.*

**B3.** Draw the causal graph of your build from world to the decision your system feeds, then run the four-step leverage analysis. Name the single highest-leverage intervention — and be explicit whether it lives in your house or someone else's. *Tests: causal graph construction, leverage analysis, [IJ]. Difficulty: medium.*

### AUDIT — trace where bias entered a deployed system, and assign the owner

**A1.** Pick a documented case — COMPAS (Angwin et al. 2016), the Amazon résumé screener (Dastin, Reuters 2018), or the health-cost-proxy algorithm (Obermeyer, Powers, Vogeli, Mullainathan, *Science* 2019). Read the primary source, not the summary. Draw the causal graph. Before reading the post-mortem, lock a prediction: which mechanisms are active, and the highest-leverage intervention for each. *Tests: dataset-as-artifact reading, falsifiable prediction. Difficulty: medium.*

**A2.** For your audited case, trace the highest-leverage bias-carrying path to its source node and name the accountable owner — the party who sits at that node. If the leverage is upstream of the deploying team (as in *Agents of Chaos* Case #6), say so explicitly and name whose reach it is in. *Tests: accountability assignment, upstream-leverage recognition. Difficulty: medium.*

**A3.** A hiring model trained on ten years of one company's promotion records scores women lower. One colleague calls it dataset bias, one label bias, one structural. State the specific condition under which each is right, what you'd need to know about collection and labeling to distinguish them, and the mechanism behind each diagnosis. *Tests: bias-type classification, mechanism specificity. Difficulty: medium.*

### Synthesis

**S1.** The chapter claims structural bias can't be fixed from inside the model or the data. Design the thought experiment that would test — and could falsify — this claim. Specify what "fixed" means and what evidence in the literature would force you to revise it. *Tests: falsifiability, structural-bias definition. Difficulty: high.*

**S2.** You're the third engineer. The first two rebalanced the data and added an equalized-odds constraint; the deployed disparity hasn't moved. Describe the diagnostic procedure that determines whether the remaining disparity is addressable at all, and where the highest-leverage point is. What did the first two most likely fail to gather? *Tests: leverage procedure, diagnostic sequence. Difficulty: high.*

### Challenge

**C1.** Design an audit protocol — analyses on a labeled dataset *alone* — that gives the strongest possible *inferential* evidence about whether dataset or label bias dominates, when you cannot see the labeling process. Specify which patterns shift your prior each way, and name the residual uncertainty your protocol cannot resolve. *Tests: diagnosis under limited access, honesty about limits. Difficulty: high.*
