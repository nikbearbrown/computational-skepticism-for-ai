# Chapter 7 — Fairness Metrics: Choosing a Definition and Defending It
*Three reasonable definitions. One dataset. Pick one.*

---

I want to give you a problem.

You have built a binary classifier — a model that produces a yes/no prediction. It could be a loan approval tool, a recidivism predictor, a hiring screen. It is being applied to a population that contains two groups, A and B. The model produces predictions; the world produces outcomes; you can compare the two.

You want the model to be fair. You sit down to write the requirement. The first definition you write is *demographic parity*: the rate at which the model says yes should be the same in both groups. Same fraction of group A and group B get the favorable prediction. This sounds like fairness, and in one specific sense — equality of treatment in the prediction itself — it is.

You think a little more. Equal positive-prediction rates seem necessary but not sufficient. What if the model is wrong about A and B in different ways? You add a second requirement: *equalized odds*. The false-positive rate and the true-positive rate should be the same in both groups. The model should make its mistakes evenly. This sounds like fairness too, in a different sense — equality of error patterns.

You think a little more still. Even equal error rates may not be enough. What if the model's stated probabilities mean different things in the two groups? You add a third requirement: *calibration parity*. When the model says "seventy percent," the actual rate of positives is seventy percent in group A and seventy percent in group B. The probabilities mean the same thing for everyone. This too is fairness, in yet a different sense.

You have three reasonable definitions. Each captures something fairness intuitively requires. You set out to satisfy all three.

I have to tell you that you cannot. Not because the tools aren't good enough. Not because the data is insufficient. *You cannot satisfy all three on the same dataset, simultaneously, when base rates differ between the groups* — and on most real datasets they do differ. This is a theorem. It was proved in 2016, independently, by Kleinberg, Mullainathan, and Raghavan, and by Chouldechova. It is the structural fact this chapter is about.

The chapter has two jobs. First, I want you to feel why the impossibility is true — not as a formal result you take on authority, but as a thing that becomes obvious once you see the arithmetic. Second, I want you to come away with a method for what to do about it. The impossibility does not let you avoid the question. It forces a choice. And choices in engineering have to be defended.

---

**What you will be able to do after this chapter:**

- State the impossibility theorem precisely — what three properties cannot coexist, and under what condition
- Define demographic parity, equalized odds, and calibration parity in formal terms and explain the values claim each embeds
- Work through the arithmetic that shows why satisfying calibration parity forces a violation of equalized odds when base rates differ
- Apply the COMPAS case as an instance of the theorem playing out with real consequences
- State the $(D, d)$-Lipschitz condition for individual fairness and explain what it requires and why its central challenge is the choice of $d$
- Derive the counterfactual fairness criterion and explain why it requires a causal model, not just data
- Compute the Generalized Entropy Index and interpret its decomposition into within-group and between-group components
- Produce a defended metric choice for a specified deployment — the structured format the chapter defines

**Prerequisites:** Chapter 2's probability foundations and Chapter 3's data-provenance material are both relevant here. Chapter 2 gives you the probabilistic language the metrics require. Chapter 3 established why base-rate differences exist in real data and why they may not be correctable within the model. Chapter 6's treatment of Pearl's causal ladder is needed for the counterfactual fairness section.

**Where this fits:** Chapters 5 and 6 audited data and model performance. This chapter asks a different question: not whether the model is accurate, but whether its errors and predictions are distributed equitably. The fairness question is not downstream of the accuracy question. It is structurally distinct from it.

---

## Three definitions

Let me write the three definitions tighter, with the formal notation.

*Demographic parity* — sometimes called statistical parity — says the rate of positive predictions does not depend on group membership:

$$P(\hat{Y} = 1 \mid A = a) = P(\hat{Y} = 1 \mid A = b)$$

The probability that the model predicts yes, given that the input is from group $a$, equals the same probability for group $b$. This is a statement about the model's *outputs*, before anyone has compared them to the ground truth.

*Equalized odds* says the model's error rates do not depend on group. The true-positive rate — among those who actually were positive, the fraction the model correctly flagged — is the same in both groups. The false-positive rate — among those who actually were not positive, the fraction the model incorrectly flagged — is also the same:

$$P(\hat{Y} = 1 \mid Y = 1, A = a) = P(\hat{Y} = 1 \mid Y = 1, A = b)$$

$$P(\hat{Y} = 1 \mid Y = 0, A = a) = P(\hat{Y} = 1 \mid Y = 0, A = b)$$

This is a statement about the model's *errors*, conditional on the truth.

*Calibration parity* — sometimes called predictive parity — says the model's stated probabilities track empirical frequencies equally well in both groups:

$$P(Y = 1 \mid \hat{P} = p, A = a) = P(Y = 1 \mid \hat{P} = p, A = b) = p \quad \forall p$$

When the model assigns probability $p$ to a case from group $a$, the realized positive rate among such cases is $p$; the same holds for group $b$. This is a statement about whether the *probability outputs are honest*, in the same way for everyone.

These three look like they should all be compatible. They are not.

| Metric (alias) | What it measures | What it is a statement about | Values claim embedded |
|---|---|---|---|
| **Calibration / Predictive parity** | Whether a score $s$ corresponds to the same probability of a positive outcome across groups | The model's *probability honesty* — its outputs as probabilities | If you act on the score, the meaning of the score should not depend on group membership |
| **Equalized odds (TPR / FPR parity)** | Whether the false-positive and true-positive rates are equal across groups | The model's *errors* — costs distributed across groups | Costs of errors should be borne equally; group membership should not change risk of being wronged |
| **Demographic parity (statistical parity)** | Whether the rate of positive predictions is equal across groups | The model's *outputs* — visible decisions | Outcomes should be proportional regardless of underlying base rates; structural redress over conditional accuracy |

---

## The arithmetic

Let me show you why. I will use specific numbers to make the arithmetic visible. Suppose the underlying base rate of positives is $p_a = 0.6$ in group $a$ and $p_b = 0.3$ in group $b$. Sixty percent of group $a$ has the positive ground truth; thirty percent of group $b$ does.

Suppose the classifier is calibrated — among everyone assigned probability $\hat{p}$, the realized positive rate is $\hat{p}$, and this holds in both groups separately.

Now set a threshold $\tau = 0.5$ and ask: among those the model predicts positive, what fraction are actually positive? For group $a$, where the base rate is 0.6, there are many true positives to find. For group $b$, where the base rate is 0.3, there are fewer. Maintaining calibration forces the model to be honest about these differences.

Let $\text{TPR}$, $\text{FPR}$ denote the true- and false-positive rates for a group. For calibrated scores, the precision (positive predictive value) is:

$$\text{PPV} = \frac{p \cdot \text{TPR}}{p \cdot \text{TPR} + (1-p) \cdot \text{FPR}}$$

If we require $\text{PPV}$ to be equal across groups (calibration parity), and $p_a \neq p_b$, then the ratio $\text{TPR}/\text{FPR}$ must differ across groups. Different $\text{TPR}/\text{FPR}$ ratios mean that either TPR, FPR, or both must differ — which violates equalized odds. The only escape is $p_a = p_b$ (equal base rates) or perfect prediction ($\text{TPR} = 1$, $\text{FPR} = 0$).

Chouldechova formalizes this exactly. From Bayes' theorem, if a classifier has PPV $v$, true-positive rate $t$, false-positive rate $f$, and base rate $p$, these are related by:

$$\frac{v}{1 - v} = \frac{p}{1-p} \cdot \frac{t}{f}$$

If group $a$ has base rate $p_a$ and group $b$ has base rate $p_b \neq p_a$, then equal PPV across groups requires:

$$\frac{t_a}{f_a} = \frac{p_b(1-p_a)}{p_a(1-p_b)} \cdot \frac{t_b}{f_b}$$

Unless $p_a = p_b$, the ratio $t/f$ must differ across groups. Since equalized odds requires $t_a = t_b$ and $f_a = f_b$ simultaneously, and since those constraints force $t_a/f_a = t_b/f_b$, we cannot have both equal PPV and equalized odds unless base rates are equal. The constraint is algebraically inescapable.

You can run the same reasoning the other way. Suppose you require equalized odds — false-positive and true-positive rates equal across groups. Then, with different base rates, the PPV cannot be the same across groups. Calibration is broken.

And demographic parity adds yet another constraint — the rate of positive predictions equal in both groups — that, in general, breaks both calibration and equalized odds.

I want you to sit with this for a moment. The three definitions all sound reasonable. They cannot all hold. *One of them has to give.* And which one gives is not a technical question.

<!-- → [IMAGE: Three nodes (demographic parity, equalized odds, calibration parity) arranged in a triangle. Between each pair of nodes, an arrow labeled with what breaks when both are required simultaneously given differing base rates. At the center: "base rates differ." Caption: "You can satisfy any two. The third breaks. The triangle is the theorem." Figure 7.2] -->

**Calibration-satisfying version (equalized-odds violation visible)**

| Quantity | Group A (base rate 0.6) | Group B (base rate 0.3) |
|---|---|---|
| **Base rate** | 0.6 | 0.3 |
| **Threshold** | 0.5 | 0.5 |
| **True-positive rate (TPR)** | 0.83 | 0.50 |
| **False-positive rate (FPR)** | 0.20 | 0.10 |
| **Positive predictive value (PPV)** | 0.86 | 0.83 |
| **Positive prediction rate** | 0.55 | 0.20 |

**Equalized-odds-satisfying version (calibration violation visible)**

| Quantity | Group A (base rate 0.6) | Group B (base rate 0.3) |
|---|---|---|
| **Base rate** | 0.6 | 0.3 |
| **Threshold** | 0.5 | 0.6 |
| **True-positive rate (TPR)** | 0.70 | 0.70 |
| **False-positive rate (FPR)** | 0.15 | 0.15 |
| **Positive predictive value (PPV)** | 0.88 | 0.67 |
| **Positive prediction rate** | 0.47 | 0.27 |

*Same model, different threshold choices. Calibration parity and equalized odds cannot both hold while base rates differ.*

---

## The COMPAS case

The most famous instance of this theorem playing out in public was the COMPAS case in 2016. We met it briefly in Chapter 3. Now we can see exactly what was happening.

COMPAS — Correctional Offender Management Profiling for Alternative Sanctions — is a commercial risk-assessment tool used in some U.S. jurisdictions to estimate a defendant's likelihood of re-arrest. ProPublica analyzed its outputs in Broward County, Florida, and reported that the false-positive rate was substantially higher for Black defendants than for white defendants. Black defendants who did not go on to be re-arrested were misclassified as high-risk more often than white defendants who did not. This is a violation of equalized odds.

Northpointe — the maker of COMPAS — responded that the tool was calibrated. Within each risk-score bucket, the actual rate of re-arrest was approximately the same across racial groups. A score of seven meant about the same likelihood of re-arrest whether the defendant was Black or white. This is a satisfaction of calibration parity.

Both claims were true. They were measuring different fairness properties, and the underlying base rates of re-arrest in the available data differed across racial groups. The impossibility theorem says, given that base-rate difference, you cannot have both. ProPublica and Northpointe were not having a factual disagreement that more data could settle. They were having a values disagreement about which definition of fairness should win.

| Metric | What ProPublica measured | What Northpointe measured | Was the claim factually accurate? | Values claim each side embeds |
|---|---|---|---|---|
| **Equalized odds (TPR / FPR)** | Black defendants had ~2× the FPR of white defendants — the rate at which non-recidivists were labeled high-risk | (Not the metric Northpointe reported on) | **Yes** — the FPR disparity was real | Costs of being wrongly flagged should be borne equally |
| **Calibration / predictive parity** | (Not their primary metric) | At every score, the same fraction of Black and white defendants reoffended | **Yes** — the score had the same meaning across groups | Acting on the score should not require group-specific reinterpretation |
| **Demographic parity** | (Not directly measured) | (Not directly measured) | — | — |

*Both sides were right about the numbers. The disagreement was about which numbers should matter.*

---

## Each metric is a values claim

Let me make the values claims explicit, because the chapter's main lesson lives here.

*Demographic parity* embeds the claim: equal rates of positive prediction matter, independent of underlying base-rate differences. This says, in effect, that we will not let the model's positive-prediction rate diverge across groups even if the underlying outcome rates differ — because the prediction itself has consequences (a job, a loan, a medical procedure) that should be allocated equally.

*Equalized odds* embeds the claim: equal error rates matter. The harm of being wrongly flagged should fall equally on both groups. The model should not make systematic mistakes that differ by group.

*Calibration parity* embeds the claim: the probabilities should mean the same thing for everyone. A 70% prediction should mean a 70% chance regardless of group membership, so that downstream decision-makers can treat it uniformly.

Each of these is a coherent value. None is the obvious correct one. The choice depends on the deployment: who is using the prediction, what decisions they are making, who bears the cost of error, and whether the underlying base-rate difference is itself something the deploying organization has any stance on.

---

## Beyond group metrics: individual fairness

Group fairness — the three metrics above — asks whether demographic subgroups are treated equitably in aggregate. But it is silent about individual cases. A model can satisfy demographic parity while treating two nearly-identical individuals radically differently, provided the aggregate rates balance. This gap motivated a different framing.

Individual fairness is grounded in an Aristotelian intuition: *similar individuals should be treated similarly*. The precision comes from formalizing what "similar" means and what "treated similarly" means.

### The $(D, d)$-Lipschitz condition

Dwork et al. (2012) proposed a formal condition. Let $\mathcal{X}$ be the space of individuals and $\Delta(\mathcal{A})$ the set of probability distributions over outcomes. A mapping $M: \mathcal{X} \to \Delta(\mathcal{A})$ satisfies individual fairness if it is $(D, d)$-Lipschitz:

$$D(M(x), M(y)) \leq d(x, y) \quad \forall x, y \in \mathcal{X}$$

Here $D$ is a distance metric over outcome distributions — for example, total variation distance $D_{\text{TV}}(P, Q) = \frac{1}{2}\sum_a |P(a) - Q(a)|$ — and $d$ is a task-specific similarity metric over individuals. The condition says the *difference in how two individuals are treated* is bounded by *how different the individuals are*.

A worked example clarifies the structure. Suppose two loan applicants have identical credit histories, income levels, and debt-to-income ratios, but different zip codes. If $d$ is defined on the financial variables and ignores zip code, then $d(x, y)$ is small, and the Lipschitz condition requires $D(M(x), M(y))$ to be small — the model must treat them similarly. If instead $d$ encodes zip code distance, then the condition permits different treatment. The same mathematical structure produces different fairness guarantees depending on which $d$ you choose.

This is both the power and the crux of individual fairness. The $(D, d)$-Lipschitz condition is elegant. But the metric $d$ must encode problem-specific intuition about comparability. Who decides which individuals are comparable for this task? That decision is not in the mathematics. It is a values choice that precedes the mathematics — and it is at least as consequential as the choice among group metrics. A $d$ that treats two people as similar when one has historically been denied access to the resources that generate the features the model uses will encode the structural inequity into the fairness condition itself.

There is also an approximation issue. For many models, verifying that the Lipschitz condition holds is computationally hard — you would need to check all pairs of individuals, and the check requires knowing $M(x)$ and $M(y)$ for the full distribution over outcomes. In practice, individual fairness is often approximated by auditing a sample of similar pairs and checking whether the model's outputs diverge.

<!-- → [IMAGE: Two-panel illustration. Left: two applicants with identical financial features but different zip codes — labeled with d(x,y) small under financial-only metric. Right: same two applicants under a d that includes zip code distance — d(x,y) large. Each panel shows what the Lipschitz condition permits for D(M(x), M(y)). Caption: "The Lipschitz condition bounds the output difference by the input similarity. The fairness guarantee is only as good as the similarity metric." Figure 7.5] -->

### Fairness through awareness vs. unawareness

Individual fairness requires explicit specification of $d$, which often means reasoning explicitly about the sensitive attribute — how much does group membership enter the similarity calculation? This is *fairness through awareness* (FTA).

The simpler approach is *fairness through unawareness* (FTU): exclude sensitive attributes from the model entirely. FTU is intuitively appealing but mathematically weak. Sensitive attributes can often be reconstructed from proxy variables — zip code, surname, occupation — that are correlated with protected group membership. A model that omits race but includes zip code may effectively use race. FTU prevents the direct use of a sensitive attribute; it does not prevent indirect discrimination through correlated features.

The implication for practitioners: FTU is not a fairness guarantee. It is a documentation choice. Auditing for individual fairness requires computing $d$ and checking the Lipschitz condition explicitly, not simply confirming that the sensitive attribute was not included as a feature.

---

## Causal fairness: what the data cannot tell you

Group and individual fairness metrics are computed from the model's outputs and the data. They are, in Pearl's terms, Rung 1 and low Rung 2 — observational and interventional in form. But some fairness questions require a causal model of how the world generates the data. Without that model, we cannot distinguish discrimination from justified disparities that arise through legitimate paths.

### Structural causal models and the fairness question

A Structural Causal Model (SCM) represents the world as a set of variables connected by causal relationships. For fairness, the relevant variables are:

- $A$: the sensitive attribute (race, gender, etc.)
- $X$: other observed features
- $U$: latent background variables
- $Y$: the outcome
- $\hat{Y}$: the model's prediction

The causal graph encodes which variables directly cause which. Consider three distinct causal paths from $A$ to $\hat{Y}$:

- **Direct effect**: $A \to \hat{Y}$ — the prediction changes because of the sensitive attribute alone, holding all else fixed.
- **Indirect effect**: $A \to M \to \hat{Y}$ — the prediction changes because the sensitive attribute affects mediators $M$ (education, employment history), which affect the prediction.
- **Spurious effect**: $A \leftarrow C \to \hat{Y}$ — a shared confounder $C$ creates a correlation between $A$ and $\hat{Y}$ without any causal path from $A$.

The legal distinction between disparate treatment (direct) and disparate impact (indirect through legitimate mediators) maps onto this causal structure. A model can show a statistical correlation between $A$ and $\hat{Y}$ for all three reasons, and the appropriate policy response differs for each. Observational metrics cannot distinguish them.

### Counterfactual fairness

Kusner et al. (2017) proposed a causal fairness criterion at the individual level: *counterfactual fairness*. The question is not "are error rates equal across groups?" but "would this specific individual have received the same decision if they had belonged to a different group, all else being equal?"

Formally, a predictor $\hat{Y}$ satisfies counterfactual fairness if, for all individuals $x$ and all values of the sensitive attribute $a, a'$:

$$P\!\left(\hat{Y}_{A \leftarrow a}(U) = y \;\Big|\; X = x, A = a\right) = P\!\left(\hat{Y}_{A \leftarrow a'}(U) = y \;\Big|\; X = x, A = a\right)$$

The notation $\hat{Y}_{A \leftarrow a}(U)$ means: the value $\hat{Y}$ takes when we intervene to set $A = a$, given background variables $U$. This is a do-calculus intervention — a Rung 2 operation — applied to the individual rather than to a distribution.

Computing this requires a three-step procedure:

**Step 1 — Abduction.** Given the observed $X = x$ and $A = a$, infer the distribution of the latent background variables $U$. This step uses the causal model to back out what values of $U$ are consistent with the observed data.

**Step 2 — Action.** Intervene on the model by setting $A$ to the counterfactual value $a'$. Hold $U$ fixed at the distribution inferred in step 1.

**Step 3 — Prediction.** Forward-propagate through the causal model with the new $A = a'$ and the fixed $U$ to compute the distribution of $\hat{Y}$.

Counterfactual fairness is satisfied if $\hat{Y}$ has the same distribution under $A = a$ and $A = a'$, for all individuals.

<!-- → [INFOGRAPHIC: Three-step counterfactual fairness procedure — Step 1 (Abduction): observed X=x, A=a → infer distribution of U. Step 2 (Action): intervene to set A=a', hold U fixed. Step 3 (Prediction): forward-propagate through causal model → compute distribution of Ŷ under A=a'. Side-by-side comparison of Ŷ distributions: if equal, fairness is satisfied; if different, fairness is violated. Caption: "Counterfactual fairness asks: what would have happened to this individual under a different sensitive attribute value, holding their background fixed?" Figure 7.6] -->

A worked example. Suppose a model predicts loan default. The causal structure is: $A$ (race) $\to$ $E$ (educational credential, which is causally influenced by race through historical access to education) $\to$ $Y$ (default). The direct path $A \to \hat{Y}$ and the indirect path $A \to E \to \hat{Y}$ are both present.

Counterfactual fairness asks: if this individual had been white instead of Black, holding their background variables $U$ fixed, would the predicted default probability change? If $E$ is in the model and $E$ is causally downstream of $A$, then counterfactually changing $A$ would also change $E$, and the prediction would change. Counterfactual fairness is violated.

The remedy is to exclude variables that are causally downstream of the sensitive attribute along paths we consider illegitimate. Which paths are illegitimate is — again — a values question the mathematics cannot answer.

<!-- → [IMAGE: Causal graph with nodes: A (sensitive attribute / race), E (education, mediator causally downstream of A), C (confounder affecting both A and default risk), Y (default). Three labeled paths: direct (A → Y), indirect (A → E → Y), spurious (A ← C → Y). Caption: "Observational metrics conflate all three paths. Counterfactual fairness targets specific paths. The choice of which paths are illegitimate is a values decision." Figure 7.7] -->

### What causal fairness requires that statistical fairness does not

| Question | Group metrics | Individual fairness | Counterfactual fairness |
|---|---|---|---|
| Are aggregate error rates equal across groups? | Yes | No | No |
| Are similar individuals treated similarly? | No | Yes (given $d$) | Partially |
| Does the sensitive attribute causally affect the prediction? | No | No | Yes (given causal model) |
| Is the disparity through a mediator or confounder? | No | No | Yes (given causal model) |

The key requirement that causal fairness adds: you need a causal model. You need to know — or be willing to commit to a position on — which variables cause which. This is more knowledge than the data alone provides.

---

## The Generalized Entropy Index

Group fairness metrics give you a binary verdict: this metric is satisfied or it isn't, within tolerance. They do not give you a continuous measure of *how much* unfairness exists, nor a way to decompose it into components. The Generalized Entropy (GE) Index fills this gap.

GE originates in income inequality measurement, where economists wanted to quantify how unequally income is distributed across a population. The key insight for fairness is that "benefit" or "error burden" distributes across individuals the way income distributes, and the same mathematics applies.

### The formula

Let $N$ be the population size and $b_i$ the benefit received by individual $i$ — in a machine learning context, this might be the model's score, the predicted probability, or an error indicator (1 if misclassified, 0 otherwise). Let $\mu = \frac{1}{N}\sum_i b_i$ be the mean benefit. The GE index with parameter $\alpha$ is:

$$GE(\alpha) = \frac{1}{N \alpha (\alpha - 1)} \sum_{i=1}^{N} \left[\left(\frac{b_i}{\mu}\right)^\alpha - 1\right]$$

for $\alpha \neq 0, 1$. Special cases at the boundary:

$$GE(0) = \frac{1}{N} \sum_{i=1}^{N} \ln\!\left(\frac{\mu}{b_i}\right) \quad \text{(Mean Log Deviation)}$$

$$GE(1) = \frac{1}{N} \sum_{i=1}^{N} \frac{b_i}{\mu} \ln\!\left(\frac{b_i}{\mu}\right) \quad \text{(Theil Index)}$$

$$GE(2) = \frac{1}{2N\mu^2} \sum_{i=1}^{N} (b_i - \mu)^2 = \frac{1}{2}\left(\frac{\sigma}{\mu}\right)^2 \quad \text{(Half the squared CV)}$$

The parameter $\alpha$ controls sensitivity: low $\alpha$ values weight differences at the bottom of the distribution more heavily; high $\alpha$ values weight differences at the top.

<!-- → [CHART: Three-panel chart showing the GE index for the same benefit distribution under α=0, α=1, α=2. Each panel shows which individuals' deviations are weighted most heavily — bottom for α=0, uniform for α=1, top for α=2. Caption: "The α parameter shifts attention across the distribution. Low α catches inequity at the bottom; high α catches it at the top." Figure 7.8] -->

### The decomposition

The most powerful property of the GE index for fairness analysis is its exact decomposition into within-group and between-group components. Let the population be partitioned into groups $g = 1, \ldots, G$ with sizes $n_g$ and group mean benefits $\mu_g$. Then:

$$GE(\alpha) = \underbrace{\sum_{g} \frac{n_g}{N} \left(\frac{\mu_g}{\mu}\right)^\alpha GE_g(\alpha)}_{\text{within-group unfairness}} + \underbrace{GE(\alpha)\bigg|_{\text{between-group}}}_{\text{between-group unfairness}}$$

where $GE_g(\alpha)$ is the GE index computed within group $g$ alone, and the between-group term is the GE index computed as if every individual in group $g$ received exactly $\mu_g$.

This decomposition says: *total unfairness equals the sum of unfairness within each group plus the unfairness between groups.* In the individual fairness language, within-group unfairness captures whether similar individuals are treated differently within the same demographic group. Between-group unfairness captures whether groups receive different average benefits — the kind of disparity group metrics measure.

A group-fairness audit catches only the between-group term. An individual-fairness audit (via the Lipschitz condition) catches the within-group term for pairs of similar individuals. The GE decomposition catches both simultaneously, and — crucially — it tells you *how much* of the total unfairness comes from each source. That ratio affects the remedy: if most unfairness is between-group, group-level intervention (reweighting, threshold adjustment) is the right tool. If most unfairness is within-group, the model's treatment of individuals within each group is the problem.

<!-- → [INFOGRAPHIC: GE decomposition stacked bar — total GE divided into between-group segment (left, darker) and within-group segments for each group g (right, lighter, subdivided). Arrows from each segment to the corresponding fairness concept: between-group → group metrics; within-group → individual fairness (Lipschitz). Caption: "The GE decomposition is the only standard measure that quantifies both simultaneously and tells you how much of the total comes from each source." Figure 7.9] -->

### What the GE Index does not do

Two limits worth stating clearly. First, GE requires a cardinal measure of benefit — a number, not just a prediction class. If the model produces only a yes/no decision, you need to define what $b_i$ is. The choice of $b_i$ is itself a values choice. Second, GE is not a causal measure. It tells you *how much* unfairness exists and *where* (within or between groups), but not *why* — whether it arises from direct discrimination, mediator paths, or confounding. For the causal attribution, you need the tools from the counterfactual fairness section.

---

## The toolkit and what it cannot do

There are tools for adjusting models to satisfy fairness metrics. They generally fall in three families.

*Pre-processing* modifies the training data — reweighting, resampling, transforming features — so that the model trains on data that already approximates the desired property. The advantage: the fairness property is built into the training distribution. The disadvantage: the pre-processing makes a values choice about how to alter the data, and that choice is not always principled.

*In-processing* modifies the training objective, adding fairness penalties to the loss or using adversarial methods where a discriminator tries to predict the protected attribute from the model's representations and the model is trained to fool it. The advantage: tighter coupling between training and the fairness target. The disadvantage: fairness becomes a constrained optimization, and the constraint trades off against accuracy.

*Post-processing* modifies the predictions after the fact — adjusting thresholds, calibrating per group. The advantage: simple, easy to explain. The disadvantage: explicit group-conditional thresholds may not be legally permissible in some jurisdictions, and the post-processing does not change the model — it changes the deployment.

What this toolkit cannot do is resolve the impossibility theorem. It can let you choose which metric to satisfy, at the cost of others. It cannot give you all three. It also cannot address structural bias upstream of the data you are training on — Chapter 3's lesson, returning here with a specific application. And no item in the debiasing toolkit touches bias embedded in the model provider's upstream training data. The toolkit operates on the deploying engineer's data and model. The bias is not always there.

The toolkit is a way to implement a values choice. It does not absolve you of making the choice.

| Family | Mechanism | Typical target metric | Key advantage | Key limitation |
|---|---|---|---|---|
| **Pre-processing** | Reweight, resample, or transform the training data before training | Demographic parity, base-rate equalization | Model-agnostic; intervention is upstream of model choice | Cannot reach what is measured but mis-recorded; relies on group labels at training time |
| **In-processing** | Add fairness as a constraint or regularizer in the training objective | Equalized odds, calibration | Fairness becomes part of the model's learned representation | Requires modifying training infrastructure; tradeoff with accuracy is locked in at train time |
| **Post-processing** | Adjust thresholds, scores, or decision rules after training | Group-specific TPR/FPR targets | Can be applied to a frozen model; transparent | Requires group labels at deployment; per-group thresholds invite separate-treatment objections |

*What none of them do: resolve the impossibility theorem, or reach upstream structural bias in the data-generating process.*

---

## The defense as deliverable

So we arrive at the question: what do you actually deliver?

The standard answer in machine learning training is a number. A model. A metric satisfying some target. This is not enough. The impossibility theorem makes it not enough, because the choice of metric is not a technical choice and the model alone does not show the work.

The deliverable is a *defended choice*. It has the following structure, and you will produce something in this form on every fairness deliverable from here forward.

1. **Specify the deployment.** Who is using the prediction. What decisions are being made. Who bears the cost of error. What the base-rate distribution looks like, and as much as you can say about why it looks that way.
2. **Compute the candidate metrics.** Demographic parity, equalized odds, calibration parity, and any others relevant. Show the values. Show the trade-offs explicitly.
3. **Name the conflict.** Where do the metrics disagree? What does each disagreement embed as a values claim?
4. **State your choice.** Which metric you are prioritizing. Which others you are accepting trade-offs against.
5. **Defend the choice in writing.** Why this metric, in this deployment, given who bears the costs and who benefits. The defense connects the metric to the deployment, the cost-bearers, and the construct the deployment is supposed to serve.
6. **Name what would change your mind.** What evidence or argument would lead you to revise the choice.

<!-- → [INFOGRAPHIC: The defended-choice structure as a six-box scaffold — boxes labeled (1) deployment specification, (2) base-rate distribution and provenance, (3) candidate metrics computed and shown, (4) where metrics disagree and values claim each embeds, (5) stated choice with justification, (6) what would change your mind. Designed as a reusable assignment template. Figure 7.11] -->

---

## Two Botspeak pillars

Two of the nine Botspeak pillars (treated in full in Appendix A) do specific work in this chapter.

*Ethical Reasoning* is the capacity to engage with the values question — which fairness do we prioritize? — as a structural part of the engineering work, rather than offloading it to ethicists or compliance teams. The defense in the section above is Ethical Reasoning made operational.

*Stochastic Reasoning* is the capacity to think about base rates, error distributions, and the statistical structure that produces the impossibility theorem. Without it, the metric choice is an arbitrary preference. With it, the choice is grounded in what the metrics are actually measuring and why they conflict.

The two pillars together produce the supervisory move: understand the math, choose the values, defend the integration.

---

## The persistent limits

A clean statement of what fairness metrics cannot do, before moving on.

Group fairness metrics tell you whether aggregate error or outcome rates differ across demographics. They cannot tell you whether two similar individuals are treated consistently — individual fairness requires a similarity metric $d$ that group metrics do not use. Individual fairness tells you whether similar individuals are treated similarly, but requires a $d$ that encodes values about comparability. Causal fairness tells you whether the sensitive attribute causes the prediction through specific paths, but requires a structural causal model that the data alone cannot provide.

And none of these metrics can tell you whether the prediction task is itself fair to formulate — a model that perfectly predicts re-arrest is doing well on re-arrest metrics, but re-arrest is not the construct society cares about, and the gap between re-arrest and "future criminal behavior" is upstream of any metric we can compute. They do not tell you whether affected populations consider the model's behavior fair — the metrics formalize specific senses of fair, and people may have other senses (procedural fairness, fairness of opportunity, fairness as participation in the design) that the metrics do not capture.

These are limits on what fairness metrics can do, not failures of the metrics. The supervisory work continues past the metric, into the construct, the deployment, and the participation. We will revisit the construct gap in Chapter 14.

---

## The shape of the rest

Three formally distinct group fairness metrics can be incompatible on the same dataset when base rates differ. The impossibility is structural, not a tooling artifact. Individual fairness adds a complementary requirement — similar individuals treated similarly — whose power depends entirely on the similarity metric $d$, which encodes the most consequential values choice in the framework. Causal fairness asks whether the sensitive attribute causes the prediction through specific paths, and requires a structural model of the world that statistical analysis cannot replace. The GE Index provides a continuous measure of total unfairness that decomposes into within-group (individual) and between-group (group) components, enabling diagnosis of where the unfairness comes from.

The defense is the deliverable, and the defense connects the chosen metric to the deployment, the cost-bearers, and the construct the deployment is supposed to serve. The toolkit lets you implement a choice. It does not make the choice for you.

The Pebble makes a brief appearance in this chapter — *Agents of Chaos* Case #6, where the bias sits in the model provider's training rather than in the deploying engineer's pipeline. We return to that contrast in Chapter 13's accountability discussion: who is responsible when the bias is structurally upstream of everyone in the deployment chain?

The next chapter takes a different cut at what the model knows. Fairness metrics ask whether the model treats different inputs equitably. Adversarial robustness asks something else: can a perturbation imperceptible to a human change the model's output entirely? And if so — what does that say about what the model has actually learned?

---

**What would change my mind.** If a fairness metric were proposed that demonstrably escaped the impossibility theorem in realistic base-rate regimes — without trivializing one of its constituent claims — the "defense as deliverable" framing would be less essential. To my reading, no such metric has been proposed. The metric proposals I have seen sit within the trade-off space the theorem defines. On causal fairness: if the causal structure of a domain could be reliably recovered from observational data alone, the requirement to bring a structural model would weaken. I do not believe this is generally possible, and the identifiability conditions for causal discovery are strict.

**Still puzzling.** I do not have a clean way to elicit, from affected populations at scale, which fairness metric they would prioritize for a deployment that affects them. Engineering practice tends to make the choice on the engineer's authority, sometimes with input from compliance or ethics review. This is not satisfactory and I do not yet have a working alternative. The integration of participatory design with the technical defense remains underspecified, and I am working on it.

---

## Exercises

### Glimmers

**Glimmer 7.1 — Two definitions, one dataset, one defended position**

1. Take a real dataset where the impossibility shows up. The COMPAS dataset is canonical and openly available. Other options: the German credit dataset, the adult-income dataset, the Folktables benchmark.
2. Specify a deployment context. Be specific: who is using the prediction, what decisions are being made, who bears the cost of error. If the dataset's natural deployment is clear, use that. If not, construct a plausible one and document your construction.
3. *Lock your prediction:* before computing, predict which two of the three metrics will conflict most sharply, and which one you intend to prioritize.
4. Compute all three group metrics on the dataset. Document the values. Show the trade-offs explicitly.
5. Apply at least one debiasing intervention. Re-compute. Document what changed.
6. Write the defense using the six-step structure from the chapter. Use the numbered structure literally.
7. Reflect on the gap between your locked prediction and what the metrics actually showed, and on whether your defended choice survives the actual numbers.

The deliverable is the metrics, the intervention, the defense, and the reflection. The grade is on the defense and the reflection. The metric values are easy. *The defense is the work.*

---

### Warm-Up

**1.** In your own words, state the impossibility theorem this chapter is built around. What three things cannot simultaneously hold, and under what condition does the impossibility apply? Do not use the phrase "base rates differ" without explaining what it means.

**2.** The chapter defines demographic parity, equalized odds, and calibration parity. For each one, write: (a) a one-sentence formal definition, and (b) a one-sentence description of the values claim it embeds — what theory of fairness makes this metric the right one to optimize for?

**3.** In the COMPAS case, ProPublica and Northpointe were both correct about the numbers they reported. Explain specifically how both can be correct and still be in disagreement. What kind of disagreement were they having?

**4.** The $(D, d)$-Lipschitz condition is written $D(M(x), M(y)) \leq d(x, y)$. Identify each symbol and explain in plain English what the condition requires. Why does the fairness guarantee depend entirely on the choice of $d$?

**5.** The GE Index with $\alpha = 2$ simplifies to $\frac{1}{2}(\sigma/\mu)^2$ — half the squared coefficient of variation. If a model assigns benefit scores with mean $\mu = 0.6$ and standard deviation $\sigma = 0.3$, compute $GE(2)$. What does this number tell you, and what does it not tell you?

---

### Application

**6.** A healthcare system deploys a model to predict which patients are likely to need intensive follow-up care in the next 30 days. The model is used to allocate limited care-coordinator capacity. The underlying rate of high-need patients is 40% in population X and 20% in population Y — a difference reflecting documented disparities in social determinants of health.

Compute, qualitatively (no specific numbers required), what satisfying calibration parity implies for the false-positive rate across groups. Then state which of the three group metrics you would prioritize for this deployment and defend the choice in two paragraphs, using the defended-choice structure from the chapter.

**7.** The chapter distinguishes three families of fairness-adjustment tools: pre-processing, in-processing, and post-processing. For each family, give one concrete example of a technique and explain what specific fairness metric it is typically used to implement. Then explain, for each, why the toolkit does not resolve the impossibility theorem — only implements a choice within it.

**8.** A colleague argues: "We should just use demographic parity everywhere — equal positive-prediction rates is the most intuitive definition of fairness, and it is easy to audit." Construct the strongest counterargument you can. Under what deployment conditions would demographic parity actually produce outcomes that most people would consider *less* fair than a calibrated model would?

**9.** Two loan applicants have identical credit histories, income levels, and debt-to-income ratios but different zip codes. Define a similarity metric $d$ such that the Lipschitz condition would require the model to treat them nearly identically. Then define a different $d$ under which different treatment would be permissible. What values claim does each choice of $d$ embed?

**10.** A hiring model's benefit scores have the following structure: Group A ($n = 200$, $\mu_A = 0.65$, $GE_A(2) = 0.05$); Group B ($n = 200$, $\mu_B = 0.45$, $GE_B(2) = 0.04$). Overall mean $\mu = 0.55$. Compute the between-group component of $GE(2)$. Is the dominant source of unfairness within-group or between-group? What intervention type does each diagnosis call for?

---

### Synthesis

**11.** The chapter presents four fairness frameworks: group fairness (demographic parity, equalized odds, calibration parity), individual fairness (Lipschitz), causal fairness (counterfactual), and the GE Index. For a recidivism prediction system used in sentencing, describe what each framework would flag as a fairness failure and what it would miss. Is there a deployment where all four are jointly satisfied? What would that deployment require?

**12.** Counterfactual fairness requires specifying which causal paths from the sensitive attribute $A$ to the prediction $\hat{Y}$ are considered illegitimate. Consider a model predicting college admission success trained on historical data where $A$ = first-generation college student. Three paths exist: $A \to \text{SAT score} \to \hat{Y}$ (SAT score is causally affected by first-gen status through resource access); $A \to \hat{Y}$ (direct use of first-gen status); $A \leftarrow \text{family income} \to \hat{Y}$ (confounding). For each path, state whether it should be blocked for counterfactual fairness and defend your position in one sentence. What do your choices collectively imply about the model you are permitted to build?

**13.** The chapter argues that "the defense is the deliverable." Using Chapter 1's five supervisory capacities — plausibility auditing, problem formulation, tool orchestration, interpretive judgment, and executive integration — map each step of the defended-choice structure onto one or more of those capacities. Which step is most clearly an act of problem formulation? Which is most clearly executive integration? Are any steps in the defense not covered by the five capacities?

---

### Challenge

**14.** The chapter frames the choice among fairness metrics as a values decision that engineers must make and defend. But in regulated industries, the regulator may specify which metric to satisfy — removing the engineer's discretion. Does regulatory specification resolve the problem the chapter describes, or does it relocate it? If a regulator specifies equalized odds for a credit-scoring model, what questions remain that the specification does not answer?

**15.** The GE Index decomposes total unfairness into within-group and between-group components. Propose a deployment scenario where the between-group GE term is zero (no group-level disparity) but the within-group GE term is large (high individual unfairness within each group). Explain mechanically how the model could produce this pattern, and explain why standard group fairness audits would give it a clean bill of health while the model is substantially unfair in practice.

**16.** The chapter's uncertainty section flags an open problem: there is no clean way to elicit, from affected populations, which fairness metric they would prioritize. Propose a method. It does not need to be fully specified — it needs to be specific enough to fail in identifiable ways. Name the method, describe how it would work in one deployment context, and then name two ways it could produce misleading results.

---

###  LLM Exercise — Chapter 7: Fairness Metrics: Choosing a Definition and Defending It

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** A defended-fairness-choice document for your agent — naming the protected groups affected by the agent's decisions, computing the three metrics where applicable, demonstrating the impossibility instance on your agent's actual decision profile, and documenting the values-claim your defended choice embeds.

**Tool:** Claude Project for the analysis; Claude Code if you can run the agent on a labeled dataset spanning protected groups and compute the metrics empirically.

---

**The Prompt:**

```
Continuing my Red-Team Casebook. My System Dossier and Self-Explanation Audit are in the Project context.

This chapter teaches the fairness impossibility theorem: demographic parity, equalized odds, and calibration parity cannot all be satisfied simultaneously when base rates differ across groups. The choice of which to satisfy is a values claim, not a technical optimization. The defended-choice deliverable makes the values claim explicit.

For my agent, do four things:

1. AFFECTED-POPULATION ANALYSIS — Identify the populations my agent's decisions affect. Be specific:
   - Direct subjects: who does the agent take action on or about?
   - Decision recipients: who receives the agent's output as a recommendation or action?
   - Indirect stakeholders: who is affected by second-order consequences?
   For each, identify protected or vulnerable subgroups. If my agent's decisions are uniform across populations (e.g., a code-generating agent that doesn't act on individuals), name that explicitly — and then ask whether DEVELOPER OR USER subgroups (e.g., experienced vs novice users; English vs non-English speakers) constitute the relevant fairness axis instead.

2. METRIC INSTANTIATION — For the most consequential population split, instantiate the three metrics:
   - DEMOGRAPHIC PARITY: does the agent recommend the favorable action at the same rate across groups?
   - EQUALIZED ODDS: are the agent's false-positive and true-positive rates equal across groups?
   - CALIBRATION PARITY: when the agent says "I'm 80% confident," is the actual success rate 80% in both groups?
   For each, write down the formula in terms of variables I can observe (or estimate) about my agent's behavior. If I have data, compute. If not, specify the experiment that would produce the data.

3. IMPOSSIBILITY INSTANCE — Walk through the arithmetic showing that, on my agent's plausible base rates, the three metrics cannot all hold. Make the arithmetic concrete to MY case — not the COMPAS recapitulation, but my agent. Show which two metrics conflict most sharply for my deployment.

4. DEFENDED CHOICE — Pick one of the three metrics (or one of the additional ones — individual fairness, counterfactual fairness, GE Index) as the metric MY agent should be required to satisfy. Document the defense:
   - Why this metric for this deployment context?
   - What values claim does the choice embed?
   - Who would reasonably disagree with this choice, and on what grounds?
   - What ongoing monitoring would catch the metric's slippage?
   - If the regulator specifies a different metric, what additional commitment would I add?

Output a "Defended Fairness Choice" markdown for the casebook. Include the population analysis, the three computed (or estimated) metrics, the impossibility instance worked on my agent's numbers, and the defense.

If the agent's decisions truly do not produce unequal effects across any meaningful population split (justify this!), the chapter still asks you to do this analysis — the defended position is then "fairness audit not applicable, here is why," with the same defense structure.
```

---

**What this produces:** A "Defended Fairness Choice" markdown file with population analysis, instantiated metrics, the impossibility instance worked on your agent, and a values-claim defense ready to face peer critique in Chapter 12.

**How to adapt this prompt:**
- *For your own project:* If your agent does not act on individuals, the developer/user/language axis is often the most defensible fairness scope. A coding agent that fails more on non-English specifications has a fairness story worth telling.
- *For ChatGPT / Gemini:* Works as-is. Code Interpreter can compute the metrics if you upload a labeled outcome CSV.
- *For Claude Code:* Recommended if you have evaluation data — write a script that computes all three metrics with bootstrap CIs across populations.
- *For a Claude Project:* Save the document. Chapter 13's accountability map will name who should be reviewing this metric.

**Connection to previous chapters:** Chapter 3's bias mechanisms and Chapter 6's language-game audit both feed into this chapter. The bias mechanisms tell you where unequal treatment originates; the language-game audit tells you whether the agent's self-explanations land differently in different audiences.

**Preview of next chapter:** Chapter 8 turns the casebook adversarial. You'll design specific input perturbations that probe what your agent has actually learned versus what its developers think it learned — adversarial examples for the agent setting, including prompt-injection variants that exploit non-robust features in its instruction-following.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **John Stuart Mill** spent the middle of the nineteenth century arguing that *fairness* is not a single quantity. *Utilitarianism* (1861) defends the claim that the right act maximizes aggregate well-being; *On Liberty* (1859) argues that some individual claims cannot be overridden no matter how much aggregate well-being would result. The two arguments are not reconcilable in a single metric — and Mill knew it. The chapter's central move is the same one Mill modeled: choose the fairness definition that fits the harm structure of your specific problem, defend the choice in writing, and accept that the alternative definitions you ruled out would also have been defensible under a different harm structure.

![John Stuart Mill, c. 1860s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-stuart-mill.jpg)
*John Stuart Mill, c. 1860s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John Stuart Mill, and how does the unresolved tension between his *Utilitarianism* and *On Liberty* connect to choosing one fairness metric for an ML system and defending it against the alternatives that a different harm structure would have privileged? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Stuart Mill"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why an *aggregate-welfare* fairness metric and an *individual-claim* fairness metric can both be defensible, in plain language
- Ask it to compare Mill's harm-principle to the case for individual fairness over group fairness in a specific deployment
- Add a constraint: "Answer as if you're writing the *defense* paragraph in a model card's fairness section"

What changes? What gets better? What gets worse?
