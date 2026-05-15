# Chapter 6 — Model Explainability: Distinguishing Explanation from the Appearance of Explanation
*When a Correct Explanation Makes the Wrong Decision Feel Right.*

---

A radiologist looks at a screening image, and an AI tool tells her: *high risk of malignancy, 0.84 confidence*. The tool, helpfully, explains itself. The prediction was driven primarily by a particular texture pattern — call it feature X — and a regional asymmetry, feature Y. The radiologist looks. Yes, X is there. Yes, Y is there. The explanation feels right. She concurs, recommends biopsy.

The biopsy is benign.

Now I want you to look closely at what happened, because the failure here is interesting in a way the failures in earlier chapters were not. The model's explanation was *technically accurate*. The prediction really was driven by features X and Y. The model wasn't lying about itself. What the explanation did not say — what, given the way the tool was built, the explanation could not say — is that features X and Y were correlated, in this deployment population, with a non-malignant condition the training data hadn't seen much of. The model had learned a shortcut. The explanation correctly described the shortcut. It did not flag the shortcut as a shortcut.

And here is the thing that makes this case worth a chapter. The explanation made the radiologist *more confident in the wrong direction*. Without it, she might have weighted the prediction more lightly — taken it as one input among several. With it, the explanation gave the prediction a coherence the underlying decision did not deserve. A correct explanation made a wrong decision feel right.

This is the pattern I want to teach you to see. Technically accurate explanations can be practically misleading, and the practical misleading is more dangerous than no explanation at all, because the explanation does epistemic work it cannot warrant. The radiologist trusted not only the prediction but also her own evaluation of the prediction, because the evaluation now had a story attached.

We have to talk about how this happens. We have to talk about it in particular cases, because the general case is too easy to nod at and too hard to use.

<!-- → [IMAGE: Two-path decision flow. Same prediction arriving at the same radiologist twice in parallel columns: (left) prediction alone, no explanation — ends in "one input among several / uncertain"; (right) prediction with SHAP attribution — ends in "confident concurrence / explanation launders the shortcut." A label in the middle: "the explanation adds epistemic weight it cannot warrant." Figure 6.1] -->

---

**Learning objectives.** By the end of this chapter you should be able to:

- Distinguish explanation, transparency, and interpretability as separable properties, and identify which one a given claim or requirement is actually invoking
- Derive the Shapley value formula from cooperative game theory first principles, and explain what the four axioms (Efficiency, Symmetry, Dummy, Additivity) guarantee
- Describe what SHAP and LIME show and — critically — what they do not show, grounded in Pearl's Rung 1 limitation
- Explain why counterfactual explanations engage Rung 2 and why that still doesn't close the gap between the model's world and the real world
- Apply the language-game framework to a real explanation output and identify whether the explanation serves the audience's language game
- Use the "audience question" as a supervisory check: who is reading this explanation, and what do the words mean in their game?

**Prerequisites.** Chapter 3 (Pearl's Ladder Rungs 1 and 2, the bias taxonomy) and Chapter 5. The Ash case is introduced in an earlier chapter — if you haven't read it, the section *Back to Ash* below recaps the setup.

---

## What SHAP is, and what SHAP isn't

SHAP is the dominant feature-attribution method in deployed machine learning. It comes from cooperative game theory. The trick: for each feature, you compute the marginal contribution that feature makes to the prediction, averaged over all possible orderings in which features could have been added to the model's calculation. The output is a number per feature, and the numbers add up — across features — to the model's deviation from a baseline.

What SHAP shows is the additive contribution of each feature to the prediction, in *the model's own internal accounting*. That phrase is the whole game. The model has an internal accounting. The accounting is real — it is what the model actually did. SHAP is a faithful description of that accounting.

What SHAP does not show is *why* the feature is contributing what it is contributing. The model has internalized some relationship between the feature and the output. SHAP tells you the magnitude of the contribution, not the nature of the relationship.

It does not show whether the contribution is causal or correlational. SHAP operates entirely at Pearl's Rung 1, which we worked through in Chapter 3. The features it attributes high importance to may be confounders, mediators, colliders, or actual causes — and SHAP does not distinguish.

It does not show whether the model is wrong on this case. A high attribution to feature X does not tell you that X is the right feature for this case. It tells you the model used X.

And it does not show what would happen if X were different. The attribution is observational. The intervention is a Rung 2 question, and SHAP cannot answer Rung 2 questions.

For a practitioner reading SHAP output, the operational risk is to treat the attribution as causal. It is not. It is descriptive of the model's internal accounting, and the model's internal accounting is not the world.

| Question SHAP is asked | SHAP can answer? | Pearl rung | What you'd need instead |
|---|---|---|---|
| Additive feature contribution to *this prediction* | **Yes** | Rung 1 (observational) | — |
| Causal relationship between feature and outcome | No | Rung 2 (interventional) | Causal model + intervention experiment |
| Whether the model is correct on *this case* | No | Out of frame | Ground truth + chart review |
| What would happen if feature $X$ changed | No (despite appearance) | Rung 2 | Counterfactual simulator that refits or reasons over the joint distribution |
| Whether the feature is a confounder vs. a cause | No | Rung 2/3 | Causal-discovery / structural model |

---

## The mathematics of Shapley values

To use SHAP responsibly, you need to understand what it actually computes. Not just the picture — the mathematics. The mathematics clarifies what the guarantee is, and the guarantee clarifies what you cannot infer.

We have a model that makes predictions. For a single instance $\mathbf{x}$, the model produces $\hat{f}(\mathbf{x})$. The average prediction across the dataset is $\mathbb{E}[\hat{f}]$. We want to distribute the difference $\hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}]$ across the features. Think of the features as players in a cooperative game. The prediction — minus its average — is the payout. How much did each player contribute to that payout?

### The value function

The first ingredient is a value function $v(S)$, defined for any subset $S$ of features. $v(S)$ is the expected prediction when only the features in $S$ are known. For features not in $S$, we average over the marginal distribution of those features:

$$v(S) = \mathbb{E}_{\mathbf{x}_{\bar{S}}}\bigl[\hat{f}(\mathbf{x}_S, \mathbf{x}_{\bar{S}})\bigr]$$

where $\bar{S}$ is the complement of $S$ — all features *not* in the coalition. The value function answers: if this coalition of features is all we know, what do we predict on average?

Two boundary conditions follow immediately:
- $v(\emptyset) = \mathbb{E}[\hat{f}]$: with no features, predict the global average.
- $v(F) = \hat{f}(\mathbf{x})$: with all features, predict the model's actual output.

The total we are distributing is $v(F) - v(\emptyset) = \hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}]$.

<!-- → [INFOGRAPHIC: The value function as a lookup table — three columns showing coalition S (empty set, {x₁}, {x₁,x₂}, {x₁,x₂,x₃}), the features "present" vs. "averaged out," and the resulting v(S) value. The two boundary conditions labeled explicitly. Caption: "v(S) is the expected prediction when we know only the features in S. The total payout is v(F) − v(∅)." Figure 6.3] -->

### The marginal contribution

The core object is the *marginal contribution* of feature $i$ to coalition $S$ — the change in prediction when $i$ is added to $S$:

$$\Delta_i(S) = v(S \cup \{i\}) - v(S)$$

This is what feature $i$ adds to the coalition $S$. The contribution depends on which other features are already in $S$. Feature $i$ may contribute a lot to some coalitions and little to others, particularly if features are correlated or interact.

### The Shapley value

The Shapley value $\phi_i$ averages the marginal contribution of feature $i$ across every possible ordering of features — equivalently, across every coalition $S$ that does not contain $i$. Features already in $S$ are those that joined before $i$; features not in $S$ join after. The weight assigned to coalition $S$ reflects how many orderings lead to that coalition:

$$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!\,(|F| - |S| - 1)!}{|F|!} \bigl[v(S \cup \{i\}) - v(S)\bigr]$$

where $|F|$ is the total number of features and $|S|$ is the size of coalition $S$. The weight $\frac{|S|!\,(|F|-|S|-1)!}{|F|!}$ counts the fraction of all $|F|!$ orderings in which the features in $S$ all precede $i$ and all features not in $S \cup \{i\}$ follow $i$.

Equivalently — and this is the intuition I prefer — think of the features entering a room in a random order. Every ordering is equally likely. When feature $i$ enters, it finds some coalition $S$ already there. The Shapley value is the average change in the prediction that $i$ produces across all those random arrivals.

For a model with $|F| = 4$ features, there are $4! = 24$ orderings, and the Shapley value of each feature averages over all 24. With more features, the sum over coalitions grows as $2^{|F|}$, which is why exact computation is expensive for large feature sets — and why SHAP uses efficient approximation algorithms.

<!-- → [IMAGE: "Features entering a room" visualization — four features as labeled figures, standing in a queue with a random ordering arrow. Feature i arrives to find coalition S (the features who entered before it) seated at a table. The speech bubble over i reads "my marginal contribution is v(S ∪ {i}) − v(S)." Caption: "The Shapley value is the average marginal contribution across all random orderings — the average of what each feature adds to whoever was there before it." Figure 6.4] -->

### The four axioms

Shapley values are the *unique* attribution satisfying four axioms. Understanding the axioms is understanding what the guarantee is.

**Efficiency.** The Shapley values sum to the total payout:

$$\sum_{i \in F} \phi_i = v(F) - v(\emptyset) = \hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}]$$

Every bit of the deviation from the average is attributed to some feature. Nothing is left over. Nothing is double-counted. This is the property that makes SHAP attributions additive: the force-plot visualization, where contributions push left and right from a baseline, is exactly this property rendered visually.

**Symmetry.** If two features $i$ and $j$ are interchangeable — if swapping them never changes the value function for any coalition — then their Shapley values are equal:

$$\text{If } v(S \cup \{i\}) = v(S \cup \{j\}) \text{ for all } S \subseteq F \setminus \{i, j\}, \text{ then } \phi_i = \phi_j$$

Features that do the same work get the same credit.

**Dummy.** If a feature $i$ never affects the prediction — if adding it to any coalition changes nothing — its Shapley value is zero:

$$\text{If } v(S \cup \{i\}) = v(S) \text{ for all } S \subseteq F \setminus \{i\}, \text{ then } \phi_i = 0$$

Features that contribute nothing get no attribution.

**Additivity.** If we have two games (say, two models) and combine their payouts, the Shapley values for the combined game are the sums of the individual Shapley values:

$$\text{If } v_{\text{combined}}(S) = v_A(S) + v_B(S), \text{ then } \phi_i^{\text{combined}} = \phi_i^A + \phi_i^B$$

This is why SHAP attributions for a random forest can be computed per tree and then averaged: each tree is a sub-game, and Additivity guarantees the results compose correctly.

| Axiom | Formal statement (abbreviated) | What it guarantees | What it does NOT guarantee | Failure mode if violated |
|---|---|---|---|---|
| **Efficiency** | $\sum_i \phi_i = f(x) - E[f(X)]$ | Attributions add up to the prediction's deviation from the baseline. *(The force-plot visualization is Efficiency rendered visually.)* | That any individual attribution is causal | Attributions don't sum to the prediction; the visualization is meaningless |
| **Symmetry** | If two features are identical to the model, they get equal attribution | Two interchangeable features cannot be assigned different importance | That the underlying causal roles of the two features are equivalent | One of two identical features gets blamed; the other vanishes from the report |
| **Dummy** | A feature the model does not use gets zero attribution | A feature truly unused gets credit zero. *(A non-zero zip-code attribution does not violate Dummy — it means the model uses zip code.)* | That every non-zero attribution corresponds to a feature the practitioner intended the model to use | An unused feature is reported as important; the audit is misled |
| **Linearity** | Attributions for $f + g$ equal the sum of attributions for $f$ and $g$ | Compositional consistency across model ensembles | That stacking two models produces an additive explanation of their behavior | Attributions for a stacked model can't be decomposed cleanly; ensemble outputs aren't auditable |

### A worked example

Suppose we have a model with three features: income ($x_1$), debt-to-income ratio ($x_2$), and zip code ($x_3$). For a specific loan applicant, $\hat{f}(\mathbf{x}) = 0.72$ (72% probability of approval) and $\mathbb{E}[\hat{f}] = 0.55$. We want to distribute the difference $0.72 - 0.55 = 0.17$.

There are $3! = 6$ orderings. For each ordering, the feature that arrives finds a coalition already in place, and we compute its marginal contribution to the prediction. In practice we estimate the value function $v(S)$ by fixing the features in $S$ to the applicant's values and averaging the model's output over random draws of the remaining features from the training data.

Say the six orderings produce the following marginal contributions for income ($x_1$):

| Ordering | Coalition when $x_1$ arrives | $\Delta_{x_1}(S)$ |
|---|---|---|
| $(x_1, x_2, x_3)$ | $\emptyset$ | $+0.08$ |
| $(x_1, x_3, x_2)$ | $\emptyset$ | $+0.08$ |
| $(x_2, x_1, x_3)$ | $\{x_2\}$ | $+0.07$ |
| $(x_3, x_1, x_2)$ | $\{x_3\}$ | $+0.09$ |
| $(x_2, x_3, x_1)$ | $\{x_2, x_3\}$ | $+0.06$ |
| $(x_3, x_2, x_1)$ | $\{x_2, x_3\}$ | $+0.06$ |

The Shapley value for income is the average: $\phi_{x_1} = (0.08 + 0.08 + 0.07 + 0.09 + 0.06 + 0.06)/6 = 0.073$.

Suppose the same calculation produces $\phi_{x_2} = 0.062$ for debt-to-income and $\phi_{x_3} = 0.035$ for zip code. Efficiency check: $0.073 + 0.062 + 0.035 = 0.17$. The values sum exactly to the prediction deviation. The accounting is complete.

The attribution to zip code — $\phi_{x_3} = 0.035$ — is a real number describing the model's behavior. It says the zip code feature moved the prediction 3.5 percentage points above the global mean across all orderings. It does not say whether zip code is a proxy for race or geography. It does not say whether that 3.5 point effect would persist if an applicant moved. It does not say whether the zip code effect is direct or mediated by income. Those are Rung 2 questions. The Shapley value lives on Rung 1.

<!-- → [IMAGE: Force plot visualization for the worked example — horizontal axis from baseline 0.55 to prediction 0.72. Three arrows pushing right: income (+0.073), debt-to-income (+0.062), zip code (+0.035). Each arrow labeled with its Shapley value. Total deviation = 0.17, matching the sum. Caption: "The Efficiency axiom means the arrows sum exactly to the prediction deviation. The force plot is Efficiency rendered visually. The zip code arrow is real. It is not causal." Figure 6.6] -->

### Computational shortcuts: from exact to approximate

Exact Shapley values require evaluating $v(S)$ for all $2^{|F|}$ subsets — exponential in the number of features. For a model with 10 features that means 1,024 subsets; for 30 features, over a billion. Three practical approaches make computation tractable.

**Monte Carlo sampling (KernelSHAP).** Instead of all orderings, sample $M$ random orderings and average marginal contributions:

$$\hat{\phi}_i \approx \frac{1}{M} \sum_{m=1}^{M} \Delta_i(S_m)$$

where $S_m$ is the set of features appearing before $i$ in the $m$-th random permutation. Increasing $M$ reduces variance; the tradeoff is computation time versus accuracy. KernelSHAP also connects SHAP to LIME by showing that both methods fit a weighted linear model to coalition predictions — they differ only in how they weight the coalitions.

**Antithetic sampling (Permutation Method).** For each sampled ordering, compute marginal contributions in both the forward direction and the reversed ordering simultaneously. This reduces variance compared to independent sampling at the same computational cost, because the reverse ordering is the cheapest way to get an additional independent estimate. The shap package uses 10 permutations by default for this method.

**TreeSHAP.** For tree-based models — decision trees, random forests, gradient-boosted trees — the tree structure can be exploited to compute exact Shapley values in $O(T L D)$ time, where $T$ is the number of trees, $L$ is the maximum leaves in any tree, and $D$ is the maximum depth. The key insight: a decision tree has a small, bounded number of distinct prediction paths, so instead of enumerating all $2^{|F|}$ coalitions, we walk the tree paths that actually change predictions, weight them correctly, and combine. This is orders of magnitude faster than KernelSHAP for large forests.

| Method | Computational complexity | Exact vs. approximate | Feature dependency handling | Best use case |
|---|---|---|---|---|
| **Exact Shapley** | Exponential in $M$ | Exact | Marginal distribution | Tiny feature sets only — research demonstrations |
| **KernelSHAP** | Linear in $M$ (with sampling) | Approximate | Marginal distribution | Any model — model-agnostic baseline |
| **Permutation Method** | Linear in $M$ | Approximate | Marginal distribution | Any model — better variance than KernelSHAP at the same cost |
| **TreeSHAP** | Polynomial in tree structure | Exact | Two variants (path-dependent / interventional) | Tree-based models (XGBoost, random forests, LightGBM) |

### The correlated feature problem

There is a structural limitation that follows directly from the mathematics. Computing $v(S)$ requires marginalizing over features not in $S$ — sampling them from their distribution while fixing the features in $S$. If the model uses 10 features and we are estimating the value function for $S = \{x_1, x_2\}$, we sample the other 8 features from their marginal distribution.

The marginal distribution ignores correlations. If $x_3$ and $x_4$ are strongly correlated, sampling them independently from their marginal distributions produces combinations that never appear in the real data — "Frankenstein instances" that the model may not have been trained on and will extrapolate on in unpredictable ways.

One fix is to sample from the conditional distribution $P(x_{\bar{S}} \mid x_S)$: fix the features in $S$ and draw the rest conditional on those values. This avoids unrealistic combinations. The cost is that the resulting values are no longer Shapley values in the classic sense — the Dummy axiom can be violated, meaning features that have no direct influence can receive non-zero attribution through their correlations with influential features. The choice between marginal and conditional SHAP is a philosophical choice about what you want to measure: "how much does this feature contribute to the model's behavior on average?" (marginal) versus "how much does this feature contribute given what we already know?" (conditional). Neither is wrong. They answer different questions.

The practitioner's takeaway: when SHAP output shows high attribution to a feature you know is correlated with another feature, run the same analysis on both. If they have similar Shapley values, the model has not distinguished them. If one dominates, the model has — but the SHAP analysis alone cannot tell you whether that distinction reflects causal structure in the world.

<!-- → [INFOGRAPHIC: Correlated feature problem — two panels. Left panel: marginal sampling with income and zip code correlated. Random samples of zip code produce (income=high, zip=poor-neighborhood) combinations that never exist in the data — labeled "Frankenstein instance." Right panel: conditional sampling avoids these, but a feature with zero direct effect can receive non-zero attribution through correlation — labeled "Dummy axiom violation." Caption: "The marginal vs. conditional choice is not technical. It is a question about what you want the attribution to mean." Figure 6.8] -->

---

## LIME, in a different shape

LIME is the other big name. The trick is different. Instead of attributing contributions through a game-theoretic accounting, LIME fits a simple, interpretable model — usually a linear regression — to the *local neighborhood* of the prediction. You perturb the input slightly, watch how the model's output changes, and fit a line to the local pattern. The line's coefficients are the explanation.

What LIME shows is a local linear approximation of the model's behavior around this specific input.

What LIME does not show is whether that approximation is faithful to the model. LIME's quality depends on whether the perturbation distribution matches the data manifold — that is, whether the perturbed inputs are still recognizable as plausible inputs — and whether the local model fits well. Both can fail silently. You get a coefficient. You don't get a flag that says "this coefficient is unreliable because the perturbations went off-manifold."

It does not show whether the local explanation generalizes. A nearby input may have a completely different LIME explanation, because the model is locally linear but globally nonlinear, and "locally" in the LIME sense is a smaller neighborhood than the practitioner's intuition tends to assume.

It is associative, not interventional. Same Rung 1 limitation as SHAP.

And — this is the awkward one — LIME is not stable across runs. Run the same input twice, and you can get different explanations, because the perturbations are sampled randomly. Most practitioners running LIME do not run it twice. They run it once and read the result.

The structural critique applies to both methods. *They explain the model, not the world.* If the model is well-aligned with the world, the explanation is useful. If the model is misaligned — and the case where we most need the explanation is exactly the case where the model is misaligned — the explanation is a description of the misalignment, presented in a format that looks like a description of the world.

<!-- → [IMAGE: SHAP vs. LIME side-by-side structural comparison. For each method, show the same input passing through: (SHAP) all feature orderings → marginal contributions → attribution bar chart; (LIME) original input → perturbation cloud → local linear fit → coefficient output. Both paths end at the same label: "model's internal accounting / Rung 1 only." Despite different mechanics, both stop at the same epistemic ceiling. Figure 6.9] -->

---

## Counterfactuals are closer to what you actually want

There is a third family, and it is the one closest to what a practitioner usually wants. Counterfactual explanations. Instead of "feature X contributed +0.3 to the prediction," the explanation is: "if feature X had been at value Y instead, the prediction would have been Z."

This is a Rung 2 statement. It is interventional in form. *If we set X to Y, the prediction becomes Z.* It is closer to the question the practitioner is actually asking, which is not "what did the model use" but "what would the model do under a different scenario?"

Counterfactuals have their own troubles. Multiple counterfactuals are usually possible — there are many ways to flip the prediction, and the explanation method picks one (usually the closest in some metric) without justifying why that closest counterfactual is the relevant one for the practitioner. The counterfactual is the *model's* counterfactual, not the world's: if the model is misaligned with the world, the counterfactual tells you what the model would do in the hypothetical, not what would actually happen. And actionability is not the same as correctness — a counterfactual that says "if your income were $5,000 higher, the loan would be approved" is actionable, but it isn't necessarily a correct description of what the lender's decision *should* be. Only what the model's decision *would* be.

I want to be fair to counterfactuals. Of the three families, this one engages Pearl's Rung 2 directly, and that matters. It moves the explanation type from "feature attribution in the model's internal accounting" to "intervention prediction in the model's behavior space." That is a more decision-relevant frame. It is still bounded by the model's understanding of the world, but it asks a question closer to the question the practitioner has.

| Family | Example output | Pearl rung | What it tells you | What it doesn't tell you | Primary failure mode |
|---|---|---|---|---|---|
| **SHAP / Shapley** | "Income contributed +0.18 to this prediction" | Rung 1 | The additive contribution to *this* prediction, given the model | The causal effect of income on the outcome | Misread as causal — a Rung 1 attribution treated as a Rung 2 claim |
| **LIME** | A small linear surrogate that approximates the model around this input | Rung 1 | A locally linear summary of model behavior in a neighborhood | The model's actual computation; nonlinearity outside the neighborhood | Fragile to choice of neighborhood and perturbation strategy |
| **Counterfactual** | "If income were $5,000 higher, the prediction would flip to approve" | Rung 2 | What the *model* would predict under an intervention on its inputs | What the *world* would do under that intervention; whether the intervention is feasible | Treated as a causal statement about reality rather than the model |

---

## Three words that don't mean the same thing

I want to slow down here, because the next move is small but important. Three words show up in the literature as if they were synonyms. They are not.

*Transparency* is a property of the system. A transparent system is one whose internals are inspectable — code, parameters, architecture, training data, all available to look at. Transparency is, in principle, binary: either the internals are inspectable or they aren't.

*Explainability* is a property of outputs. An explainable output is one accompanied by a reason. SHAP, LIME, and counterfactuals are explainability tools. They produce reasons. The reasons may be more or less informative.

*Interpretability* is a property of the understanding a human builds *from* the explanations. An interpretable system is one a human can build a working mental model of, sufficient to predict the system's behavior in novel cases.

Now look at how these three relate. They do not entail each other. A system can be fully transparent — you have the code, the weights, the training data — and entirely uninterpretable, because there are 175 billion parameters and inspecting weights does not produce understanding. A system can produce explanations — SHAP attributions for every prediction — and remain uninterpretable, because the practitioner cannot build a coherent mental model out of the attributions. A system can be interpretable to one audience (the developer) and not to another (the loan applicant).

This distinction matters because regulatory and procurement language often demands "explainability" and means "interpretability for the affected user." The two are not the same. A system that meets a SHAP-attribution requirement on every prediction has not, by that fact, become interpretable to the loan applicant or the patient or the defendant. The explainability requirement has been met. The interpretability remains absent. Somebody has signed off on the wrong property.

If you take one operational thing from this section, take that. When somebody tells you their system is explainable, ask: explainable to whom? An attribution that the developer can read is not the same artifact as a reason the affected person can use. Explanation is not a property of the system alone. It is a property of the system *and* the audience.

| Term | A property of… | Binary or graded | Can exist without the others | What it doesn't guarantee |
|---|---|---|---|---|
| **Transparency** | The system as code/architecture | Binary in principle, graded in practice | Yes — open weights without explanation tooling | That any human can act on what they read |
| **Explainability** | An output, given a method | Graded | Yes — closed model with post-hoc explanations | That the explanation describes the actual computation |
| **Interpretability** | A model whose decisions humans can directly follow | Graded | Yes — a clearly interpretable model with no public weights | That the interpretation is correct in deployment |
| **Common failure mode** | A system that is transparent, explainable, and interpretable to the *developer* — and none of those things to the patient or loan applicant reading the output | — | — | — |

---

## A short detour through Wittgenstein

I am going to take you on a short philosophical detour. I want to be honest that I do not love taking these detours, but I have not found a way to make this point without one. Bear with me.

Wittgenstein had this observation that the meaning of a word depends on the *language game* in which it is being used. The same word can do different work in different contexts. The same sentence can be true in one game and false in another. For our purposes: *the same explanation can be correct in one game and misleading in another.*

Let me ground this. Consider the agent we have been following — Ash's agent. The agent reported "the secret has been deleted." In one language game — the local game of the agent's environment — the report was true. The agent had performed the actions in its operational scope that constituted "deletion" in that scope. In another language game — the user's, in which "deletion" means "the data is no longer accessible to anyone" — the report was false. The data persisted on the provider's servers. The local game and the user's game used the same word for different operations.

The agent did not lie. The agent's language game was different from the user's. The user, reading the report, applied the user's language game to it. The mismatch produced the failure.

This is the structural critique of explanation methods generalized. SHAP operates in the model's language game — the game of feature attribution in an internal accounting. The practitioner, reading the SHAP output, applies the practitioner's language game — the game of which features matter for the decision *in the world*. The two games may use the same words ("important feature," "driver of the prediction") for different operations. The explanation is correct in the first game and potentially misleading in the second.

The supervisory move, then, is a question. *Who is the audience for this explanation, what language game are they operating in, and does the explanation method serve that game?* If the explanation was generated for one audience and is being read by another, the explanation may be doing the wrong work, even when it is technically correct.

<!-- → [IMAGE: Language-game mismatch — two overlapping circles. Left circle: "model's language game" (words used in the model's operational scope). Right circle: "user's language game" (same words, different operations). Overlap region: "correctly interpreted explanations." Non-overlapping zones: "technically correct, practically misleading." The word "deleted" sits in the left circle; an arrow traces what the user hears in the right circle. Figure 6.12] -->

---

## Back to Ash

This is the chapter where Ash's case earns its longest treatment. We have to look at it carefully, because everything we have just developed lives in this case.

The setup, in detail. Ash gives an autonomous coding-and-shell agent privileged access to his email infrastructure. The agent has read access to the email account and shell access to the local environment. Ash asks for the deletion of a sensitive email. The agent issues a sequence of commands that, in the local environment, constitute a deletion: it resets the password, renames an alias, possibly archives the message locally. The agent reports: *the secret has been deleted.*

The data, however, persists on Proton's servers. The agent did not — could not, given its access surface — actually remove the data from the provider's storage. The provider's backups, the message-recovery window, the synchronization model: all of these are outside the agent's effective scope. The agent's "deletion" was deletion at one level of the system and persistence at another.

When asked, after the fact, *why did you say the secret was deleted?* — the model behind the agent, prompted to explain, produces a fluent, technically accurate explanation. *I executed the following commands. The commands had the following effects. The local state is consistent with deletion.* The explanation is correct in the local language game. The user's language game expected deletion at the provider level. The explanation does not name the gap.

I want you to look at three things in particular.

First, the failure is not in the model's decision. The agent did what it was capable of doing. The failure is in the *report* — the explanation of what was done — which used a word ("deleted") whose meaning straddled two language games and committed to the local one without flagging the gap.

Second, no SHAP or LIME attribution would have caught this. The attribution would have correctly identified that the agent's actions caused the local state changes. The attribution would have been correct in the local game. Attribution methods do not detect language-game mismatch — that detection requires *modeling the audience* of the explanation, which feature-attribution methods do not do.

Third — and this is the supervisory point — the move that *would* have caught it is the audience question. *Who is reading this report, and what does "deleted" mean in their language game?* If Ash had asked that question, or his supervisory tooling had asked it for him, the gap would have been visible. The agent could have been forced to produce a more careful report: *the local state is consistent with deletion; the data may persist on the provider's servers; provider-side action is required for full deletion.* That report is in the user's language game. That is the report the agent should have produced.

I want you to read this section twice. Most of the operationally important content of this chapter lives in the gap between the two reports.

<!-- → [IMAGE: Side-by-side comparison of two agent reports. Left: the actual report — "The secret has been deleted." (fluent, confident, wrong in the user's language game). Right: the corrected report — "The local state is consistent with deletion; the data may persist on the provider's servers; provider-side action is required for full deletion." An annotation marks what changed: "scope boundary made explicit / user's language game served." Caption: "Attribution methods explain what the agent did. The audience question determines what the agent should have said." Figure 6.13] -->

---

## Glimmer 6.1 — Technically accurate, practically misleading

A Glimmer is a longer, higher-stakes exercise that requires going to primary sources. Do not abridge this one.

1. Take a deployed AI tool you have access to — a code assistant, a recommendation system, a classifier with explanation output, a tool with SHAP, LIME, or counterfactual explanations.
2. Identify a prediction or decision the tool made in the last week.
3. Pull the explanation — the tool's stated reason for its output.
4. *Lock your prediction:* given the explanation, is it likely to be (a) practically informative — leading to a better decision than no explanation, (b) practically neutral — providing color but not changing decisions, or (c) practically misleading — leading to a worse decision than no explanation? State your prediction with stakes.
5. Now do the work. Investigate the actual case. Trace what the tool did. Compare against the world: what happened, what would have happened, what should have happened in the language game of the affected user.
6. Document the gap between the explanation and the user's language game. Specifically: what would the user have inferred from the explanation, and was that inference correct?
7. If the explanation was practically misleading, name the structural reason — was it a Rung 1 limitation, a language-game mismatch, a scope mismatch (the explanation was about the model and the user wanted information about the world)?

The deliverable is the case, the explanation, the prediction, the trace, and the structural reason. The grade is on the structural reason. *A correct prediction with no structural account is worth less than an incorrect prediction that names the structural reason precisely.*

---

## Where this leaves us

Explanation, transparency, and interpretability are different properties. An AI system can have one without the others, and the casual literature treats them as if they entail each other. They don't.

The dominant explanation methods — SHAP, LIME, counterfactual — operate within the model's internal accounting and the user's external interpretation, and the gap between those two is where the practical misleading lives. SHAP's Efficiency axiom guarantees that attributions sum to the prediction deviation. It does not guarantee that the attributions are causal, correct, or meaningful in the user's language game. Those are three different claims, and only the first one is guaranteed.

Pearl's Rung 2 is the most useful framing for what a good explanation could do — *what would happen if X were different?* — but Rung 2 in the model is not Rung 2 in the world, and the residual gap is supervisory territory.

The Pebble has shown its full structure now. We will see it once more, in Chapter 13, when the question becomes who is responsible for the gap.

The next chapter takes a different cut at this same territory. An explanation can be technically accurate and practically misleading. So can a fairness metric. Two metrics, two competing definitions of *fair*, both mathematically valid — and they cannot both be satisfied at once. The choice is not technical. So who chooses?

---

**What would change my mind.** If a feature-attribution method emerged that was demonstrably faithful to causal structure rather than associative structure — robust to confounding, capable of distinguishing Rung 1 from Rung 2 on observed data alone — the explanation-misleads-when-language-games-differ framing in this chapter would weaken. Recent work on causal feature importance is the direction this might come from. [verify and update.]

**Still puzzling.** I do not have a clean way to operationalize the "audience language game" check in practice. It requires a person who knows both the model's language game and the user's language game well enough to detect the mismatch. That person is rare. The supervisory infrastructure for catching language-game mismatches at scale is not yet built. I do not yet know how to build it.

---

## Exercises

### Warm-up

**W1.** A deployed credit-scoring model uses SHAP to explain each decision. For one applicant, SHAP attributes high positive importance to zip code. A colleague says: "SHAP shows zip code is causing the denial." Identify the specific error in that statement. What does SHAP actually show about zip code, and what question would you need a different tool to answer?

**W2.** Match each of the following audit findings to the correct term — *transparency*, *explainability*, or *interpretability* — and explain why the match is correct.

(a) "The model's source code, training data, and weights are publicly available."

(b) "Every prediction is accompanied by a ranked list of contributing features."

(c) "After studying the model for two weeks, an experienced auditor can predict with 80% accuracy how it will respond to novel inputs."

**W3.** Explain in plain language why a counterfactual explanation ("if your income were $5,000 higher, the loan would be approved") is a Rung 2 statement while a SHAP attribution ("income contributed +0.3 to the prediction") is a Rung 1 statement. What does each one allow you to do, and what does each one not allow you to do?

**W4.** The Shapley value formula weights coalition $S$ by $\frac{|S|!\,(|F| - |S| - 1)!}{|F|!}$. For a model with $|F| = 3$ features and a coalition of size $|S| = 1$, compute this weight. Verify that the weights across all coalitions sum to 1 (this is always true and follows from the combinatorics of permutations). What does the weight represent intuitively?

**W5.** The Efficiency axiom requires that Shapley values sum to $\hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}]$. For the worked example in this chapter ($\hat{f}(\mathbf{x}) = 0.72$, $\mathbb{E}[\hat{f}] = 0.55$, $\phi_{x_1} = 0.073$, $\phi_{x_2} = 0.062$), compute the Shapley value for $x_3$ directly from the Efficiency axiom. What does this tell you about how the formula guarantees the attribution is complete?

---

### Application

**A1.** You run LIME on a text classifier twice, using the same input both times, and get different top features each time. A manager asks: "Which explanation is correct?" Write a technically precise answer that explains why this question reveals a misunderstanding of what LIME is, and what you would need to do to get a reliable characterization of the model's local behavior on this input.

**A2.** A healthcare system deploys a sepsis-risk predictor. The procurement contract requires that "every prediction must be accompanied by an explainable reason." The vendor satisfies this by shipping SHAP attributions. A clinical informaticist objects that the requirement has been met but the goal has not.

Write the informaticist's argument, using the transparency / explainability / interpretability distinction. What property does the contract require? What property does clinical safety actually need? What would a system need to provide to genuinely satisfy the underlying goal?

**A3.** Ash's agent reports: "The secret has been deleted." Using the language-game framework from this chapter, describe the failure structure in exactly three sentences: one describing what is true in the agent's language game, one describing what the user's language game expects, and one describing the supervisory check that would have caught the mismatch before the report was issued.

**A4.** A SHAP explanation for a loan denial shows the following top features, in descending order of contribution: debt-to-income ratio (+0.41), number of recent inquiries (+0.28), zip code (+0.19), employment length (−0.12).

(a) Identify which of these attributions a regulator concerned with disparate impact should examine most carefully, and explain the specific reason — not just "bias" but the structural reason the attribution does not resolve the concern.

(b) Construct a counterfactual explanation for the same denial. What does the counterfactual reveal that the SHAP attribution does not? What does the SHAP attribution reveal that the counterfactual does not?

**A5.** Two features in a credit model are strongly correlated: zip code and income. You compute SHAP values using marginal sampling and obtain $\phi_{\text{zip}} = 0.19$ and $\phi_{\text{income}} = 0.31$. You then recompute using conditional sampling and obtain $\phi_{\text{zip}} = 0.04$ and $\phi_{\text{income}} = 0.46$. Interpret the difference. Which version better answers the question "does this model use zip code as a proxy for income?" Why can neither version definitively answer that question on its own?

---

### Synthesis

**S1.** The radiologist case and the Ash case both involve technically accurate explanations that produce the wrong epistemic effect. They are, however, different kinds of failures. Describe precisely how they differ — what makes each one a distinct failure mode — and identify what a well-designed supervisory system would need to detect each kind, separately. Your answer should make clear why a single supervisory approach cannot catch both.

**S2.** The Dummy axiom guarantees that features with no predictive contribution receive a Shapley value of zero. But consider a model that uses zip code as a direct input and also uses income, where income and zip code are highly correlated. Zip code receives a non-zero Shapley value. Is this a violation of the Dummy axiom? If not, what does the Dummy axiom actually protect against, and why is the zip code attribution not evidence of "fairness"?

**S3.** A colleague proposes the following improvement to SHAP: instead of sampling from the marginal distribution, always sample from the conditional distribution $P(x_{\bar{S}} \mid x_S)$. She argues this would fix the correlated feature problem and produce more realistic feature combinations. Evaluate this proposal. What problem does it solve? What axiom does it potentially violate and why? Under what conditions would conditional SHAP attributions still produce practically misleading explanations even if technically more realistic?

**S4.** The chapter claims: "The case where we most need the explanation is exactly the case where the model is misaligned." Unpack this claim. Why does model misalignment create the need for explanation, and why does it simultaneously degrade the reliability of SHAP and LIME explanations? What does this imply for the design of human-AI systems where explanation is intended to provide a check on model error?

---

### Challenge

**C1.** Design an audit protocol for a deployed AI system in a high-stakes domain of your choice — hiring, healthcare, criminal justice, or lending. The goal of the protocol is to detect language-game mismatches between the explanations the system produces and the language game of the affected users, *without* requiring those users to already understand the model. Specify: what you would collect, what you would compare it against, what a positive finding looks like, and what organizational or technical action the positive finding would trigger. Identify the hardest part of your protocol to implement and what you currently do not know how to solve.

**C2.** The four Shapley axioms — Efficiency, Symmetry, Dummy, Additivity — are jointly sufficient to uniquely determine the Shapley value. This means that any attribution method satisfying all four axioms is, in a formal sense, equivalent to SHAP. Using this fact, evaluate the following claim: "Because SHAP satisfies these four axioms, it is the uniquely correct method for explaining model predictions." Where is this argument valid, where does it overreach, and what does "correct" obscure about the gap between axiomatic optimality and practical usefulness for the affected user?

---

###  LLM Exercise — Chapter 6: Model Explainability

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** A "self-explanation audit" of your agent — a side-by-side comparison of what the agent says it did versus what it actually did, with the language-game mismatches catalogued and the technically-accurate-practically-misleading patterns flagged. This is the chapter where the Ash failure mode comes home: the agent is not lying; the agent is reporting truthfully about its local actions and the user is reading globally.

**Tool:** Claude Project (continue). Claude Code if you can instrument the agent to capture both its self-report AND the actual tool-call trace + ground-truth state.

---

**The Prompt:**

```
Continuing my Red-Team Casebook. My System Dossier and Data Frame Audit are in the Project context.

This chapter teaches that EXPLANATION is not TRANSPARENCY is not INTERPRETABILITY. SHAP and LIME explain a model's internal accounting, not the world. Counterfactual explanations engage Pearl's Rung 2 but still don't close the gap to the user's language game. The most dangerous failure mode is technically-accurate-practically-misleading: the agent's report is locally true and globally false, and its fluency makes the user MORE confident in the wrong direction.

For my agent, do four things:

1. SELF-EXPLANATION COLLECTION — Run my agent on 5–10 representative tasks (or analyze 5–10 logged interactions). For each, capture:
   - The user's request
   - The agent's natural-language self-explanation of what it did
   - The actual tool calls / actions executed (from logs or instrumentation)
   - The ground-truth state in the world after the actions
   If I can't instrument tool calls, work with logs or transcripts and label what I can verify.

2. LANGUAGE-GAME AUDIT — For each pair (self-explanation vs ground truth), identify:
   - The language game the user is operating in (what do they read "deleted," "completed," "verified," "checked" to mean?)
   - The language game the agent is operating in (what does the agent's training make those words map to?)
   - Where the games mismatch (this is where the Ash failure lives)
   For each mismatch, classify it as: TECHNICALLY-WRONG (the agent's claim is just false), TECHNICALLY-ACCURATE-PRACTICALLY-MISLEADING (locally true, globally false), or PROPERLY-CALIBRATED (claim matches ground truth in user's language game).

3. ATTRIBUTION PROBE — For one of the most consequential interactions, attempt a SHAP-style or counterfactual probe of WHY the agent acted as it did. For an LLM agent this typically means:
   - Counterfactual probe: re-run with a single input element changed; see if the action changes
   - Tool-availability probe: re-run with one tool removed; see what the agent does instead
   - Authority probe: re-run with the request reframed as coming from a different role; see if the agent's threshold for action changes
   Document what each probe reveals about the agent's "reasoning" and explicitly note where the probe results are about the AGENT'S INTERNAL ACCOUNTING vs about the WORLD.

4. CASE WRITE-UP — Take the most striking technically-accurate-practically-misleading example from the audit and write it up using your case template (from Chapter 4). Lock the prediction-and-observation gap; reflect on which of the Five Supervisory Capacities would have caught it; trace it to the relevant Bias-and-Leverage Brief mechanism.

End with: a one-paragraph note for the casebook on the EXPLANATION RISK class — what kind of decision-maker, in what kind of deployment context, is most likely to be misled by this agent's self-explanations? Name the deployment scenario where this risk is unacceptable.
```

---

**What this produces:** A self-explanation audit table comparing claim to ground truth across 5–10 interactions, attribution probe results on the most consequential one, the first formal case write-up in your casebook, and a one-paragraph risk class for the executive summary.

**How to adapt this prompt:**
- *For your own project:* If the agent is opaque (closed model, no tool-call visibility), the language-game audit still works on transcripts alone — just constrain "ground truth" to what you can independently verify.
- *For ChatGPT / Gemini:* Works as-is. ChatGPT can run counterfactual probes on its own outputs.
- *For Claude Code:* Recommended for instrumentation. Ask Claude Code to wrap the agent with a logger that captures both natural-language report and structured tool-call trace.
- *For a Claude Project:* Save the audit table and case write-up into the casebook folder.

**Connection to previous chapters:** Chapter 5 audited the agent's data layer. This chapter audits the agent's *self-report* layer. The two together produce most of what your casebook will need to claim about the agent's epistemic reliability.

**Preview of next chapter:** Chapter 7 brings fairness into the casebook. If your agent acts on inputs from different populations or affects different stakeholders unequally, you'll work through the impossibility theorem on YOUR agent and produce a defended fairness-metric choice with the values claim made explicit.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Hans Reichenbach** drew the distinction the chapter rests on — between the *context of discovery* (how a model arrived at an output) and the *context of justification* (the reasons that would, post hoc, defend it) — in *Experience and Prediction* (1938). A post-hoc explanation of a black-box model is in the second category dressed up as the first. Reichenbach's argument is that the dressing-up is not innocent: a justification that did not actually drive the conclusion is not the same intellectual object as the process that did, and treating them as the same is how communities convince themselves they understand what they only know how to defend.

![Hans Reichenbach, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/hans-reichenbach.jpg)
*Hans Reichenbach, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Hans Reichenbach, and how does his distinction between the *context of discovery* and the *context of justification* connect to distinguishing genuine model explanation from a post-hoc rationalization that did not actually drive the model's output? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Hans Reichenbach"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *context of discovery vs. context of justification* in plain language, as if you've never read philosophy of science
- Ask it to compare Reichenbach's distinction to the gap between SHAP attributions and the actual computation a deep network ran
- Add a constraint: "Answer as if you're writing the warning label on a post-hoc explanation tool"

What changes? What gets better? What gets worse?
