# Chapter 5 — Explanation vs. the Appearance of Explanation

*When a correct explanation makes the wrong decision feel right.*

A radiologist looks at a screening image. The AI tool reports *high risk of malignancy, 0.84 confidence*, and — helpfully — explains itself: the prediction was driven mainly by a texture pattern, feature X, and a regional asymmetry, feature Y. She looks. X is there. Y is there. The explanation feels right. She concurs, recommends biopsy. The biopsy comes back benign.

I'm going to flag this opening the way I flag every load-bearing story in this book: it's a composite, not a sourced clinical incident, and I'm labeling it so because a chapter about distrusting fluent explanations cannot itself run on a fluent anecdote you're asked to trust. The *mechanism* it illustrates is real and documented — deep networks in medical imaging routinely learn shortcuts: spurious features that correlate with the label in training and generalize badly, and which a post-hoc explanation will faithfully report without flagging as shortcuts.[^shortcuts]

Now look at what an explanation tool just handed you. It's a decision artifact, and it looks done — it names the features, it comes with a confidence number, it's coherent. What it does not announce is whether it is telling you about *the model* or about *the world*. The model's explanation was technically accurate: the prediction really was driven by X and Y. What it could not say is that X and Y were correlated, in this population, with a benign condition the training data hadn't seen much of. The model learned a shortcut, the explanation correctly described the shortcut, and it did not flag the shortcut as a shortcut. And here is the part that earns the chapter: the explanation made the radiologist *more confident in the wrong direction.* Without it she might have weighted the prediction lightly. With it, the prediction acquired a coherence the underlying decision didn't deserve. That is the **fluency trap** in its purest form — well-formed output read as evidence — and it is the capacity this chapter trains: **Interpretive Judgment**, supplying the meaning and accountability the explanation itself cannot warrant.

[^shortcuts]: Robert Geirhos et al., "Shortcut Learning in Deep Neural Networks," *Nature Machine Intelligence* 2:665–673, 2020, DOI:10.1038/s42256-020-00257-z; and Alex J. DeGrave, Joseph D. Janizek, Su-In Lee, "AI for radiographic COVID-19 detection selects shortcuts over signal," *Nature Machine Intelligence* 3:610–619, 2021, DOI:10.1038/s42256-021-00338-7.

---

## What SHAP is, and what SHAP isn't

SHAP is the dominant feature-attribution method in deployed ML, and it comes from cooperative game theory.[^shap] Here's what's actually happening. For each feature, you compute the marginal contribution it makes to the prediction, averaged over all possible orderings in which features could have been added to the model's calculation. Out comes one number per feature, and the numbers add up — across features — to the model's deviation from a baseline.

What SHAP shows is the additive contribution of each feature *in the model's own internal accounting*. That phrase is the whole game. The model has an internal accounting; it is real; it is what the model actually did; SHAP faithfully describes it. What SHAP does *not* show is why the feature contributes what it contributes — it gives you the magnitude of the relationship, not its nature. It does not show whether the contribution is causal or correlational: SHAP lives entirely on Pearl's Rung 1, the associational rung.[^pearl] The features it scores high may be confounders, mediators, colliders, or genuine causes, and SHAP does not distinguish. It does not show whether the model is wrong on this case — a high attribution to X tells you the model *used* X, not that X was right. And it does not show what would happen if X were different; that's a Rung 2 question, and SHAP can't answer it.

For a practitioner, the operational risk is a single misread: treating the attribution as causal. It is descriptive of the model's internal accounting, and the model's internal accounting is not the world.

[^shap]: Scott M. Lundberg & Su-In Lee, "A Unified Approach to Interpreting Model Predictions," NeurIPS 2017, arXiv:1705.07874. The game-theoretic foundation is L. S. Shapley, "A Value for n-Person Games," in *Contributions to the Theory of Games II*, Princeton, 1953, 307–317.
[^pearl]: Judea Pearl & Dana Mackenzie, *The Book of Why*, Basic Books, 2018, for the ladder of causation (Rung 1 association, Rung 2 intervention, Rung 3 counterfactual).

---

## The mathematics — and the guarantee it does and doesn't give

To use SHAP responsibly you need to know what it computes, because the mathematics is exactly what tells you what you *cannot* infer.

The model produces $\hat{f}(\mathbf{x})$ for an instance, and the dataset average is $\mathbb{E}[\hat{f}]$. We distribute the difference $\hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}]$ across features, treating them as players in a cooperative game whose payout is the prediction minus its average. The first ingredient is a value function $v(S)$ — the expected prediction when only the features in the coalition $S$ are known, averaging over the rest:

$$v(S) = \mathbb{E}_{\mathbf{x}_{\bar{S}}}\bigl[\hat{f}(\mathbf{x}_S, \mathbf{x}_{\bar{S}})\bigr].$$

Two boundaries follow: $v(\emptyset) = \mathbb{E}[\hat{f}]$ (no features, predict the average) and $v(F) = \hat{f}(\mathbf{x})$ (all features, predict the actual output). The marginal contribution of feature $i$ to coalition $S$ is $\Delta_i(S) = v(S \cup \{i\}) - v(S)$. The Shapley value averages that contribution across every ordering:

$$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!\,(|F| - |S| - 1)!}{|F|!} \bigl[v(S \cup \{i\}) - v(S)\bigr].$$

The intuition I prefer: features enter a room in a random order, every ordering equally likely; when feature $i$ enters it finds some coalition already there, and the Shapley value is the average change it produces across all those arrivals.

Shapley values are the *unique* attribution satisfying four axioms, and understanding the axioms is understanding the guarantee. **Efficiency**: the values sum to $\hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}]$ — nothing left over, nothing double-counted; the force-plot visualization is this axiom rendered visually. **Symmetry**: two features interchangeable to the model get equal attribution. **Dummy**: a feature that never changes any coalition's value gets zero. **Additivity**: for two combined games the Shapley values add, $\phi_i^{\text{combined}} = \phi_i^A + \phi_i^B$, which is why a random forest's attributions can be computed per tree and averaged.

One naming point, because the reference chapter is quietly inconsistent and a careful reader would trip on it. The fourth axiom is stated in prose as **Additivity** and appears in the summary table as **Linearity**. These are the same property under two names in the cooperative-game literature — the general linear-operator form is sometimes called Linearity, the combined-game form Additivity — and I'm reconciling them explicitly rather than switching silently: I use **Additivity**, and note "sometimes called Linearity" where the table lands. It is a naming reconciliation, not a factual error, but leaving it unmarked reads like a hidden distinction and undermines the rigor the section is built on.

| Axiom | What it guarantees | What it does NOT guarantee |
|---|---|---|
| **Efficiency** | Attributions sum to the prediction's deviation from baseline (the force plot made visible) | That any individual attribution is causal |
| **Symmetry** | Two features identical to the model get equal attribution | That their underlying causal roles are equivalent |
| **Dummy** | A truly unused feature gets zero (a non-zero zip-code attribution means the model *uses* zip code — not a violation) | That every non-zero attribution is a feature you intended the model to use |
| **Additivity** *(sometimes called Linearity)* | Compositional consistency across model ensembles | That stacking two models yields an additive *explanation* of their behavior |

### A worked example, and the sentence that matters

Three features — income ($x_1$), debt-to-income ($x_2$), zip code ($x_3$). For one applicant $\hat{f}(\mathbf{x}) = 0.72$ and $\mathbb{E}[\hat{f}] = 0.55$, so we distribute $0.17$. Suppose the six orderings average out to $\phi_{x_1} = 0.073$ for income, $\phi_{x_2} = 0.062$ for debt-to-income, $\phi_{x_3} = 0.035$ for zip code. Efficiency check: $0.073 + 0.062 + 0.035 = 0.17$. The accounting is complete.

And here is the sentence the whole chapter turns on, and I want it to arrive *before* you bank the precision, not fifteen pages after: the zip-code attribution of $0.035$ is a real number describing the model's behavior, and it tells you *nothing* about the world. It does not say whether zip code proxies for race or geography. It does not say whether that effect persists if an applicant moves. It does not say whether the effect is direct or mediated by income. Those are Rung 2 questions. The Shapley value lives on Rung 1. The precision of the math is real; it is precision about the model, and the model is not the world. Do not let the rigor of the derivation buy the method more trust than the thesis allows.

The one structural caveat inside the math: computing $v(S)$ requires marginalizing over the features not in $S$, and the marginal distribution ignores correlations. If two features are strongly correlated, independent sampling produces "Frankenstein instances" — combinations that never occur in real data, which the model extrapolates on unpredictably.[^aas] Sampling from the conditional distribution fixes the realism but can violate Dummy, letting a feature with no direct influence pick up attribution through its correlations. Marginal versus conditional is not a technical toggle; it's a choice about what you want the attribution to *mean* — "how much does this feature contribute on average" versus "given what we already know." Neither is wrong. They answer different questions.

[^aas]: Kjersti Aas, Martin Jullum, Anders Løland, "Explaining individual predictions when features are dependent," *Artificial Intelligence* 298:103502, 2021, DOI:10.1016/j.artint.2021.103502.

---

## LIME and counterfactuals — the same limit, different shapes

LIME takes a different route: fit a simple interpretable model — usually linear regression — to the *local neighborhood* of the prediction. Perturb the input, watch the output move, fit a line, read the coefficients. What LIME shows is a local linear approximation of model behavior around this input. What it does *not* show is whether that approximation is faithful — its quality depends on the perturbation distribution matching the data manifold and the local model fitting well, and both can fail silently. You get a coefficient; you don't get a flag saying "this one's unreliable." It's also unstable across runs: same input twice, different explanation, because the perturbations are random — and most practitioners run it once and read the result.[^lime]

Same Rung 1 limitation as SHAP, and the same structural critique applies to both: *they explain the model, not the world.* If the model is well-aligned with the world, the explanation is useful. If it's misaligned — and the case where you most need the explanation is exactly the misaligned case — the explanation is a faithful description of the misalignment, formatted to look like a description of the world. (I'll flag that "need and misalignment co-occur" claim as an aphorism the chapter asserts more than it proves; it's intuitively strong and I don't have a source that establishes the co-occurrence, so hold it as a working intuition, not a theorem.)

Counterfactuals get closer to what a practitioner actually wants: "if feature X had been Y, the prediction would have been Z." That's a Rung 2 statement, interventional in form, and it engages the rung SHAP and LIME can't. But it's the *model's* counterfactual, not the world's — if the model is misaligned, it tells you what the model would do in the hypothetical, not what would actually happen — and multiple counterfactuals are usually possible, with the method picking the closest one without justifying why "closest" is the relevant one.

| Family | Pearl rung | What it tells you | Primary failure mode |
|---|---|---|---|
| **SHAP** | Rung 1 | Additive contribution to *this* prediction, given the model | Misread as causal |
| **LIME** | Rung 1 | A locally linear summary in a neighborhood | Fragile to neighborhood and perturbation choice; unstable across runs |
| **Counterfactual** | Rung 2 | What the *model* would predict under an intervention on its inputs | Treated as a causal statement about reality |

[^lime]: Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin, "'Why Should I Trust You?': Explaining the Predictions of Any Classifier," KDD 2016, DOI:10.1145/2939672.2939778.

---

## Three words that are not synonyms

Three words show up in the literature as if interchangeable. They are not, and separating them is the most portable thing in this chapter.

*Transparency* is a property of the system: a transparent system's internals — code, weights, architecture, training data — are inspectable. *Explainability* is a property of outputs: an explainable output comes with a reason. SHAP, LIME, and counterfactuals are explainability tools. *Interpretability* is a property of the understanding a human builds *from* those explanations — a system a person can build a working mental model of, good enough to predict its behavior on new cases.

They don't entail each other. A system can be fully transparent and entirely uninterpretable — 175 billion parameters, all inspectable, no understanding produced. It can be explainable and uninterpretable — a SHAP attribution per prediction that no one can assemble into a mental model. It can be interpretable to the developer and opaque to the loan applicant. This matters because regulation and procurement often demand "explainability" and mean "interpretability for the affected user." A system that ships SHAP on every prediction has met the explainability requirement and become no more interpretable to the patient or the defendant. Somebody signed off on the wrong property. Rudin's argument that high-stakes decisions should use inherently interpretable models rather than post-hoc explanations of black boxes lands exactly here.[^rudin]

If you take one operational thing from this chapter: when someone says their system is explainable, ask *explainable to whom?* Explanation is not a property of the system alone. It is a property of the system *and* the audience.

[^rudin]: Cynthia Rudin, "Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead," *Nature Machine Intelligence* 1:206–215, 2019, DOI:10.1038/s42256-019-0048-x.

---

## Language games — and why "deleted" straddles two of them

A short philosophical detour, and I don't love detours, but I haven't found a way around this one. Wittgenstein observed that a word's meaning depends on the *language game* it's used in — the same word does different work in different contexts.[^witt] For our purposes: *the same explanation can be correct in one game and misleading in another.*

Ground it in a documented case. An autonomous agent — call it Ash's agent — is given privileged access to email infrastructure and asked to delete a sensitive message. It runs commands that, in the local environment, constitute deletion: resets the password, renames an alias, archives locally. It reports: *the secret has been deleted.* But the data persists on the provider's servers — backups, recovery windows, the sync model, all outside the agent's effective scope. This is drawn from the *Agents of Chaos* red-teaming study, and I cite it on the page rather than pointing vaguely backward, because a chapter about verifying claims can't leave its own central case unverifiable.[^chaos]

The agent did not lie. In the *local* language game — the operations available in its environment — "deleted" was true. In the *user's* language game — "the data is no longer accessible to anyone" — it was false. Same word, two games, two different operations. And notice what would and wouldn't have caught it. No SHAP or LIME attribution would have: they'd correctly report that the agent's actions caused the local state changes, correct in the local game. Attribution methods do not detect language-game mismatch, because detecting it requires *modeling the audience* of the explanation, which attribution methods don't do. What catches it is the audience question: *who is reading this report, and what does "deleted" mean in their game?* Asked in advance, it forces the honest report — *local state is consistent with deletion; the data may persist on the provider's servers; provider-side action is required for full deletion.* That report is in the user's language game. That's the one the agent should have produced.

This generalizes the structural critique. SHAP operates in the model's language game (feature attribution in an internal accounting). The practitioner reads it in *their* game (which features matter for the decision in the world). Same words — "important feature," "driver of the prediction" — different operations. Correct in the first game, potentially misleading in the second.

[^witt]: Ludwig Wittgenstein, *Philosophical Investigations*, Blackwell, 1953. Applying language-games to model self-report is my own reading, not Wittgenstein's claim.
[^chaos]: Shapira et al., "Agents of Chaos," 2026, arXiv:2602.20021, https://agentsofchaos.baulab.info/. The specific provider-side persistence mechanics should be checked against the primary before being quoted precisely.

---

## The trade-off explanation tools make

Here's the design judgment, stated as a trade-off. **Post-hoc explanation methods optimized for coverage and generality — a faithful, model-agnostic number on every prediction — at the expense of warranting anything about the world.** SHAP will explain any model's every decision, fast, with an axiomatic guarantee. That guarantee is Efficiency: attributions sum to the prediction. It is *not* a guarantee that the attributions are causal, correct, or meaningful in the user's language game. Those are three different claims and only the first is guaranteed.

Explanation tools work if you value a consistent, auditable description of *what the model did.* They fail if you need to know *whether the model is right about the world* — which is usually the actual question, and precisely the question a fluent explanation is most likely to make you feel you've answered when you haven't. The residual gap between "Rung 2 in the model" and "Rung 2 in the world" is not a tooling defect to be patched. It is supervisory territory. It is yours.

---

## Exercises

### BUILD — get AI to explain your model's decision; test whether it explains the world

Fight ownership bias. You built the model; the explanation flatters your belief that it works.

**B1.** Take a model you built or can run, get a SHAP (or LIME, or counterfactual) explanation for one specific decision, and **lock a prediction** *before* investigating: is this explanation likely to be practically informative, practically neutral, or practically misleading — and state the stakes. Then trace the actual case against the world: what happened, what would have happened, what should have happened in the affected user's language game. Name the gap. *(Tests: fluency trap, model-vs-world test, prediction-lock.)*

**B2.** For your model, produce a SHAP attribution and then write the *audience* version: pick a real affected person (applicant, patient, defendant) and rewrite the explanation in their language game. Where the two versions use the same word for different operations, mark it. *(Tests: explainable-to-whom, language-game mismatch.)*

**B3.** Compute SHAP on two features you know are correlated, using marginal sampling, then conditional sampling. Interpret the difference between the two attributions, and state which question each one answers — and why neither settles "does this model use feature A as a proxy for feature B." *(Tests: marginal vs conditional, the limit of the method on its own.)*

### AUDIT — falsify a vendor's SHAP or rationale you were handed

You have distance and no provenance. Assume the explanation is doing epistemic work it can't warrant, and try to break it.

**A1.** A vendor ships a sepsis-risk predictor and satisfies a "must be accompanied by an explainable reason" contract with SHAP attributions. Write the clinical informaticist's objection using the transparency/explainability/interpretability trichotomy: what property does the contract require, what does clinical safety actually need, and what would genuinely satisfy the underlying goal? *(Tests: signing off on the wrong property.)*

**A2.** A vendor's SHAP output for a loan denial lists: debt-to-income (+0.41), recent inquiries (+0.28), zip code (+0.19), employment length (−0.12). Identify which attribution a regulator concerned with disparate impact should examine most carefully and give the *structural* reason the attribution doesn't resolve the concern (not "bias" — the Rung-1 reason). Then construct the counterfactual for the same denial and say precisely what it reveals that SHAP doesn't, and what SHAP reveals that it doesn't. *(Tests: falsifying the rationale, Rung 1 vs Rung 2.)*

**A3.** An agent you were handed reports "the file has been deleted." In exactly three sentences, describe the failure structure: one for what's true in the agent's language game, one for what the user's game expects, one for the supervisory check that would have caught the mismatch before the report was issued. Then name the deployment context in which this explanation risk is unacceptable. *(Tests: language-game audit, audience question as a check.)*
