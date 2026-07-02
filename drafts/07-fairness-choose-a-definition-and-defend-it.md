# Chapter 7 — Fairness: Choose a Definition and Defend It

*Three reasonable definitions, one dataset. You cannot have all three — and which one gives is not a math question.*

I want to hand you a problem, and then prove to you that it has no clean solution, and then show you that the absence of a clean solution is the whole point.

You've built a binary classifier — a yes/no prediction. Loan approval, recidivism, a hiring screen. It runs on a population with two groups, A and B. The model predicts; the world produces outcomes; you can compare them.

You want it to be fair, so you write the requirement. First draft: *demographic parity* — the model says yes at the same rate in both groups. Equal treatment in the prediction itself. That sounds like fairness.

You think more. Equal yes-rates aren't enough if the model is wrong about A and B differently. Second draft: *equalized odds* — the true-positive rate and false-positive rate match across groups. The model makes its mistakes evenly. That sounds like fairness too, in a different sense.

You think more still. Even equal error rates might not be enough if the model's stated probabilities *mean* different things per group. Third draft: *calibration parity* — when the model says "seventy percent," the real positive rate is seventy percent in A and in B. The numbers mean the same thing for everyone. Fairness again, yet another sense.

Three reasonable definitions. Each captures something fairness intuitively requires. You set out to satisfy all three.

Here's what's actually happening: you can't. Not because your tools are weak or your data is thin. *You cannot satisfy all three on the same dataset, simultaneously, when base rates differ between the groups* — and on real data they usually do. This is a theorem, proved independently in 2016 by Kleinberg, Mullainathan, and Raghavan, and by Chouldechova. This chapter has two jobs: make you *feel* why the impossibility is true — as arithmetic, not authority — and hand you a method for what to do about it. The impossibility doesn't let you dodge the question. It forces a choice, and engineering choices have to be defended.

**What you'll be able to do after this chapter:**

- State the impossibility theorem precisely — which three properties can't coexist, under what condition
- Define demographic parity, equalized odds, and calibration parity formally, and name the values claim each embeds
- *Work the arithmetic* that forces the incompatibility — not gesture at it
- Read the COMPAS case as an instance of the theorem playing out with real consequences
- Produce a *defended metric choice* for a deployment: a values claim you sign, in a fixed six-step format
- Name who should have decided — and why the engineer who "just optimizes" decided by default

**Prerequisites.** Chapter 2's probability foundations; Chapter 6's Pearl's ladder and its account of why base-rate differences exist and may not be model-correctable. This chapter exercises **Problem Formulation [PF]** (deciding what the fairness mission is before the model sees it) and **Interpretive Judgment [IJ]** (signing for a values claim the math cannot make). BUILD: choose and defend a definition for a system you're building. AUDIT: judge COMPAS's definition, prove the impossibility, name who should have decided.

---

## Three definitions, tightly

*Demographic parity* (statistical parity): the positive-prediction rate doesn't depend on group.

$$P(\hat{Y}=1 \mid A=a) = P(\hat{Y}=1 \mid A=b)$$

A statement about the model's *outputs*, before anyone compares them to ground truth.

*Equalized odds*: error rates don't depend on group — true-positive rate equal, false-positive rate equal.

$$P(\hat{Y}=1 \mid Y=1, A=a) = P(\hat{Y}=1 \mid Y=1, A=b)$$
$$P(\hat{Y}=1 \mid Y=0, A=a) = P(\hat{Y}=1 \mid Y=0, A=b)$$

A statement about the model's *errors*, conditional on the truth. (Hardt, Price, Srebro, "Equality of Opportunity in Supervised Learning," NeurIPS 2016.)

*Calibration parity* (predictive parity): stated probabilities track empirical frequencies equally in both groups.

$$P(Y=1 \mid \hat{P}=p, A=a) = P(Y=1 \mid \hat{P}=p, A=b) = p \quad \forall p$$

A statement about whether the probability outputs are *honest*, the same way for everyone.

They look compatible. They are not.

<!-- → [TABLE: three metrics — columns: formal definition, what it's a statement about (outputs/errors/honesty), the values claim embedded] -->

## The arithmetic — the actual proof, not a gesture

I told you this is a theorem, so I owe you the proof. Here it is, following Chouldechova (2017). We don't need heavy machinery — Bayes' rule does the work.

Fix one group with base rate (prevalence) $p = P(Y=1)$. Let the classifier have true-positive rate $t = P(\hat{Y}=1 \mid Y=1)$ and false-positive rate $f = P(\hat{Y}=1 \mid Y=0)$. The positive predictive value — precision, PPV, call it $v$ — is the probability someone is truly positive given a positive prediction. By Bayes:

$$v = P(Y=1 \mid \hat{Y}=1) = \frac{p\,t}{p\,t + (1-p)\,f}.$$

Rearrange (divide through, take the odds form) and you get a clean identity linking all four quantities:

$$\frac{v}{1-v} = \frac{p}{1-p}\cdot\frac{t}{f}.$$

Now put two groups side by side, base rates $p_a$ and $p_b$. Suppose the classifier is calibrated — which, for a binary score, forces equal PPV across groups (a score means the same thing everywhere is exactly the statement that $v_a = v_b$). Write the identity for each group and take the ratio:

$$\frac{v_a/(1-v_a)}{v_b/(1-v_b)} = \frac{p_a/(1-p_a)}{p_b/(1-p_b)}\cdot\frac{t_a/f_a}{t_b/f_b}.$$

Calibration set the left side to $1$ ($v_a = v_b$). So the right side must equal $1$, which means

$$\frac{t_a}{f_a} = \frac{p_b(1-p_a)}{p_a(1-p_b)}\cdot\frac{t_b}{f_b}.$$

Look at the coefficient. It equals $1$ only when $p_a = p_b$. Whenever base rates differ, the ratio $t/f$ is *forced* to differ across groups. But equalized odds demands $t_a = t_b$ **and** $f_a = f_b$ simultaneously, which forces $t_a/f_a = t_b/f_b$ — the coefficient to be $1$ — which we just showed requires equal base rates. Contradiction. The only escapes are $p_a = p_b$ (equal base rates) or perfect prediction ($t=1$, $f=0$, so there are no false positives to distribute unequally).

That is the whole theorem, and it took four lines of algebra. Kleinberg, Mullainathan, and Raghavan (ITCS 2017) prove the three-way version — calibration, balance for the positive class, balance for the negative class are jointly achievable only in those same degenerate cases. Run the reasoning backward and demographic parity adds a *third* constraint (equal positive-prediction rates) that in general breaks both of the others.

<!-- → [INFOGRAPHIC: the impossibility triangle — three nodes (demographic parity, equalized odds, calibration parity), edges labeled with the constraint each pair imposes; caption: pick any two, the third breaks when base rates differ] -->

Sit with this. Three reasonable definitions. They cannot all hold. *One of them has to give* — and which one gives is not a technical question. It is a claim about which error you're less willing to make, whom you're willing to wrong, and who bears the cost. That question has a social answer, not a mathematical one. The engineer who treats it as pure optimization is still choosing — they're choosing whatever their loss function encodes — while appearing neutral. That is the move this chapter exists to make impossible.

## The COMPAS case — the theorem in public

The most famous instance played out in public in 2016. COMPAS — a commercial recidivism risk tool — was used in Broward County, Florida. ProPublica reported that its false-positive rate was substantially higher for Black defendants: defendants who did not go on to be re-arrested were flagged high-risk more often if they were Black. That is a violation of equalized odds. (Angwin, Larson, Mattu, Kirchner, "Machine Bias," ProPublica, May 23, 2016; public data at github.com/propublica/compas-analysis.)

Northpointe, the maker, replied that the tool was calibrated: within each risk-score bucket, the actual re-arrest rate was about equal across groups. A seven meant about the same likelihood whether the defendant was Black or white. That is a satisfaction of calibration parity. (Dieterich, Mendoza, Brennan, "COMPAS Risk Scales," Northpointe, 2016.)

Both were right about their numbers. The base rates of re-arrest in the available data differed across groups, and the theorem you just watched me prove says that given that difference, calibration and equalized odds *cannot both hold*. ProPublica and Northpointe were not having a factual disagreement more data could settle. They were having a *values* disagreement about which definition of fairness should win — dressed as a factual one.

<!-- → [TABLE: COMPAS — what ProPublica measured (equalized odds, ~2x FPR, real) vs what Northpointe measured (calibration, equal per-bucket rate, real); last column: the values claim each side embeds] -->

And judge the tool's *definition*, because that is the audit deliverable. COMPAS's implicit chosen definition was calibration parity — a defensible choice for a decision-maker who wants a score they can read uniformly. But the deployment context is criminal sentencing, where the cost of a false positive falls on a specific person's liberty, and calibration parity is precisely the definition that lets false-positive rates diverge. Whether that was the right definition is not answerable from the confusion matrix. It is answerable only by naming who bears which error and deciding whom the system should protect. Nobody signed that decision as a values claim. It was smuggled in as a modeling default. That is the failure — not the arithmetic, which was correct on both sides.

## Each metric is a values claim

Make the claims explicit, because the chapter's lesson lives here.

*Demographic parity* claims: equal positive-prediction rates matter, independent of underlying base-rate differences — because the prediction itself carries a consequence (a job, a loan, a procedure) that should be allocated equally. Structural redress over conditional accuracy.

*Equalized odds* claims: equal error rates matter — the harm of being wrongly flagged should fall equally, and group membership shouldn't change your risk of being wronged.

*Calibration parity* claims: the probabilities should mean the same thing for everyone, so a downstream decision-maker can treat a 70% as a 70% regardless of group.

Each is a coherent value. None is the obviously correct one. Which fits depends on the deployment: who uses the prediction, what decision it feeds, who bears the cost of error, and whether the base-rate difference is itself something the deploying organization has any stance on. That last clause is where problem formulation does its work — sometimes the base-rate difference is the thing you're morally responsible *for*, and then demographic parity's redress claim gets teeth.

## Where the metrics stop — briefly

Three quick extensions, because a defended choice should know what it's ruling out.

**Individual fairness** (Dwork, Hardt, Pitassi, Reingold, Zemel, "Fairness Through Awareness," ITCS 2012) formalizes "treat similar individuals similarly" as a Lipschitz condition, $D(M(x), M(y)) \le d(x,y)$: the difference in *treatment* is bounded by the difference in *individuals*. It is elegant, and its entire force rests on the choice of the similarity metric $d$ — who counts as comparable for this task. That choice is a values choice that precedes the math, at least as consequential as the group-metric choice. A $d$ that calls two people similar when one was historically denied the resources that generate the model's features *bakes the inequity into the fairness condition itself*. And "fairness through unawareness" — just drop the sensitive attribute — is not a fairness guarantee; zip code, surname, and occupation reconstruct it. Dropping the attribute is a documentation choice, not a fairness one.

**Counterfactual fairness** (Kusner, Loftus, Russell, Silva, "Counterfactual Fairness," NeurIPS 2017) asks a Rung 2 / Rung 3 question at the individual level: would this person's decision change if they'd belonged to a different group, holding their background fixed? Answering it requires a *structural causal model* — you have to commit to which variables cause which. That is more knowledge than the data alone provides. Its power and its cost are the same fact: it can distinguish a direct discriminatory path from a legitimate mediated one, but only if you're willing to declare which paths are illegitimate — another values call.

**The Generalized Entropy Index** (Speicher et al., "A Unified Approach to Quantifying Algorithmic Unfairness," KDD 2018) gives a *continuous* measure of unfairness that decomposes exactly into within-group and between-group components — telling you not just how much unfairness exists but where it comes from, which determines whether a group-level or individual-level remedy is the right tool.

<!-- → [TABLE: four frameworks (group / individual / counterfactual / GE index) — columns: what it catches, what it needs (data / a d-metric / a causal model / a cardinal benefit), what it misses] -->

None of these escapes the impossibility, and none tells you whether the prediction *task itself* is fair to formulate. A model that perfectly predicts re-arrest is doing well on re-arrest metrics — but re-arrest is not the construct society cares about, and that gap is upstream of every metric. The classical anchor here is Mill: *Utilitarianism* (1861) maximizes aggregate welfare, *On Liberty* (1859) protects individual claims that aggregate welfare cannot override, and Mill knew the two don't reconcile in a single quantity. Choosing a fairness definition is Mill's move — fit the definition to the harm structure of *this* problem, defend it in writing, and accept that the alternatives you ruled out would have been defensible under a different harm structure.

## The defense is the deliverable

So what do you actually hand over? The standard answer in ML training is a number — a model, a metric hitting a target. The impossibility theorem makes that not enough, because the choice of metric isn't technical and the model alone doesn't show the work.

The deliverable is a *defended choice*, in this fixed structure. You'll produce something in this form on every fairness deliverable from here on:

1. **Specify the deployment.** Who uses the prediction, what decisions follow, who bears the cost of error, what the base-rate distribution looks like — and as much as you can say about *why* it looks that way.
2. **Compute the candidate metrics.** Demographic parity, equalized odds, calibration parity, any others relevant. Show the values. Show the trade-offs.
3. **Name the conflict.** Where do the metrics disagree, and what values claim does each disagreement embed?
4. **State your choice.** Which metric you prioritize, which trade-offs you accept.
5. **Defend it in writing.** Why this metric, in this deployment, given who bears the costs and who benefits. Connect the metric to the cost-bearers and the construct the deployment is meant to serve.
6. **Name what would change your mind.** What evidence or argument would make you revise.

<!-- → [INFOGRAPHIC: the six-box defended-choice scaffold as a vertical flow, with COMPAS filled in as the worked example so the reader sees the format populated] -->

There are tools to *implement* a choice — pre-processing (reweight/resample the data), in-processing (fairness penalty or adversarial loss), post-processing (per-group thresholds). Each has a cost, and per-group thresholds invite separate-treatment objections and may not be legally permissible. But none of them resolves the impossibility. They let you pick which metric to satisfy at the expense of others; they do not give you all three, and they do not reach structural bias upstream of your data — Chapter 6's lesson returning. The toolkit implements a values choice. It does not absolve you of making it.

## Who should have decided

The audit question the blueprint asks is: *name who should have decided.* For COMPAS, the answer is not "the engineers who fit the model." It is the party accountable for the sentencing policy the tool serves — the court system, the jurisdiction, the body that owns the trade-off between a wrongly-flagged defendant's liberty and a missed-risk public-safety cost. The engineers' failure was not choosing wrong; it was choosing *silently*, letting a loss function stand in for a decision that belonged to someone with the authority and the accountability to sign it. When regulation specifies the metric — say, a regulator mandates equalized odds for credit scoring — that doesn't dissolve the problem; it *relocates* the decision to the regulator, and leaves open which base-rate differences the regulator has taken a stance on and which it has left to the deployer. Someone always decides. The only question is whether they did it on the record.

## What would change my mind — and what I'm still puzzling about

If a fairness metric were proposed that demonstrably escaped the impossibility in realistic base-rate regimes, without trivializing one of its constituent claims, the "defense as deliverable" framing would be less essential. I haven't seen one — the proposals I've read sit inside the trade-off space the theorem defines. And I do not have a clean way to elicit, from affected populations at scale, which metric they would prioritize for a deployment that affects them. Engineering practice makes the choice on the engineer's authority, sometimes with compliance review. That is not satisfactory, and integrating participatory design with the technical defense remains underspecified. I'm working on it.

---

## Exercises

### BUILD — choose and defend a fairness definition for a system you're building

**B1.** For a real (or plausible) system you'd build, run step 1 of the defended-choice structure: specify the deployment fully — users, decisions, cost-bearers, base-rate distribution and why it's shaped that way. Push yourself on the last clause; it's where the values are. *Tests: [PF], deployment specification. Difficulty: low.*

**B2.** Instantiate the three metrics for your system in terms of quantities you could observe or estimate, then either compute them or specify the exact experiment that would. Show which two conflict most sharply for *your* base rates — worked on your numbers, not COMPAS's. *Tests: metric instantiation, the impossibility on your own case. Difficulty: medium.*

**B3.** Produce the full six-step defended choice for your system, ending with step 6 named honestly. Then write one paragraph as the person who would *reasonably disagree* with your choice — and say why you still sign yours. *Tests: [IJ], the defense as a signed values claim. Difficulty: medium.*

### AUDIT — judge COMPAS, prove the impossibility, name who should have decided

**A1.** Reproduce the four-line proof from the chapter starting from Bayes' rule: derive the odds identity $v/(1-v) = [p/(1-p)](t/f)$, then show calibration forces $t/f$ to differ across groups when $p_a \neq p_b$, contradicting equalized odds. State both escape hatches explicitly. *Tests: the theorem, worked not asserted. Difficulty: medium.*

**A2.** Judge COMPAS's implicit fairness definition. Name the definition it chose, the deployment context, whom each error type falls on, and whether the choice fits the harm structure. Then name *who should have decided* — the party with the authority and accountability to sign that values claim — and explain why "the engineers optimized the loss" is not an answer. *Tests: judging a definition, accountability assignment. Difficulty: medium.*

**A3.** A colleague says: "Just use demographic parity everywhere — equal yes-rates is the most intuitive fairness and easy to audit." Build the strongest counterargument. Under what deployment conditions would demographic parity produce outcomes most people would call *less* fair than a calibrated model? *Tests: values-claim reasoning, deployment-dependence. Difficulty: medium.*

### Synthesis

**S1.** For a recidivism system used in sentencing, state what each of the four frameworks (group, individual, counterfactual, GE index) would flag and what it would miss. Is there a deployment where all four are jointly satisfied? What would it require? *Tests: integration across frameworks. Difficulty: high.*

**S2.** Does regulatory specification of a metric resolve the chapter's problem or relocate it? If a regulator mandates equalized odds for credit scoring, name the questions the specification does not answer. *Tests: [PF], accountability relocation. Difficulty: high.*

### Challenge

**C1.** The open problem: there's no clean way to elicit, from affected populations, which metric they'd prioritize. Propose a method — specific enough to fail in identifiable ways. Name it, describe it in one deployment, and name two ways it could produce misleading results. *Tests: participatory design under uncertainty, honesty about limits. Difficulty: high.*
