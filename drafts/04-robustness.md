# Chapter 4 — Robustness

*The model is not fragile. It is honest about what it learned.*

Here are two pictures. The first is a giant panda — black and white, sitting in bamboo, the way pandas sit. An image classifier looks at it and reports "panda" with high confidence. You and the model agree.

The second picture, to your eye, is the same picture. Same panda, same pose, same coloring. Put them side by side and you cannot find the difference — the changes are fractions of a percent of brightness, scattered in a pattern that means nothing visual to a human. The classifier looks at the second picture and reports "gibbon," with *even higher* confidence.[^goodfellow]

Someone hands you a model with a benchmark score of 94% and calls it robust. The score looks done. What it does not announce is which 94% — robust against what, measured how, at what perturbation budget — and, underneath that, the thing the panda just revealed: the model and you were never making the same kind of judgment. You just thought you were. This chapter is one supervisory capacity, **Plausibility Auditing**, pointed at exactly that gap: hearing the wrong note in a model that scores well, and locating the fragility before it locates you.

[^goodfellow]: Ian Goodfellow, Jonathon Shlens, Christian Szegedy, "Explaining and Harnessing Adversarial Examples," ICLR 2015, arXiv:1412.6572. The panda→gibbon example is Figure 1. (The arXiv preprint is dated December 2014; the canonical ICLR publication is 2015 — cite it as 2014/2015 if you need both.)

---

## What the perturbation actually exposes

The standard description of what you just saw is "the model is fragile," and the standard fix is to *harden* it — treat the model like metal, apply some process that doesn't change what it is but makes it harder to dent. Notice what that framing assumes: that the model learned the right thing, and the right thing is just sitting in a vulnerable form.

That assumption is wrong, and the wrongness is the whole point of the chapter. Here's what's actually happening. The model learned a *proxy* — a feature, or a set of features, in the input distribution that correlated reliably with the right label on the training data. The engineers thought the model learned "what pandas look like." It actually learned "the statistical signature of pixel arrangements that occurred in panda training images." On the training set those two things are indistinguishable. Under an adversarial perturbation they fly apart: the perturbation moves the statistical signature toward "gibbon" while leaving the panda's shape, pose, and color completely untouched.

This is not a rhetorical flourish, and it changes the engineering problem entirely. If the model is fragile, you patch it, harden it, train it on noisy inputs. If the model is using the wrong representation, all of those move the attack surface around without touching the underlying thing — you harden against this perturbation and a slightly different one finds a new proxy. The robustness gain is real but local; the gap between what the model learned and what you wanted it to learn is unaffected.

The literature converged on this over about a decade. Early papers treated adversarial examples as a glitch to be patched. Ilyas and colleagues in 2019 said something stranger and more honest: adversarial perturbations are not bugs, they are *features* — genuinely predictive, statistically real patterns that happen to be imperceptible and meaningless to humans.[^ilyas] The model bet on them because, on the training distribution, betting on them wins.

I want to be honest about a tension the reference chapter glosses. Calling the model "honest about what it learned" is a great line, and it quietly smuggles in a fact-of-the-matter about "what the model learned" that the non-robust-features debate has not settled. If non-robust features are partly artifacts of the *supervised* training objective — and models trained with self-supervised objectives show weaker versions of these patterns — then "what the model learned" is partly a property of the training regime, not a fixed thing the model is being honest about. So read the metaphor precisely: the model is honest about *what this training produced*, not about a stable truth of the world. That distinction matters when you get to the trade-off at the end.

[^ilyas]: Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, Aleksander Mądry, "Adversarial Examples Are Not Bugs, They Are Features," NeurIPS 2019, arXiv:1905.02175. The debate is documented in "A Discussion of 'Adversarial Examples Are Not Bugs, They Are Features,'" *Distill*, 2019.

---

## Why they exist — two geometric accounts

You need at least one working account of *why* adversarial examples exist to reason about robustness in a domain you haven't seen.

**The linearity hypothesis.** Take the simplest classifier, $f(x) = w^\top x$. Perturb the input by $\delta$ and the activation changes by $w^\top \delta$. Constrain the perturbation so no single coordinate exceeds $\epsilon$, and the attacker maximizes the change by pushing every coordinate in the direction the weights prefer: $\delta = \epsilon \cdot \text{sign}(w)$. The resulting shift is

$$\Delta f = w^\top \delta = \epsilon \sum_i |w_i| = \epsilon \|w\|_1.$$

In high dimensions this is the whole trick. Even with $\epsilon$ tiny, $\|w\|_1$ grows with the number of dimensions. A perturbation invisible in any one coordinate accumulates across thousands of coordinates into a decisive shift. Neural nets aren't purely linear, but ReLU networks are piecewise linear, and the same accumulation operates inside each locally linear piece. That's what the Fast Gradient Sign Method exploits: compute the gradient of the loss with respect to the input, step in the direction that increases it.

**The boundary-tilting account.** Linearity explains why the trick works but not why neural nets are *especially* vulnerable, since well-regularized linear classifiers with large margin aren't as vulnerable. The structural explanation: adversarial examples appear when the decision boundary sits very close to the data manifold in *low-variance directions* — directions the training data barely explored, where the model got little signal and left the boundary poorly constrained. An adversarial perturbation is a gradient-guided search for exactly those directions: the ones training never forced the model to stabilize.

Neither account is complete alone. Together they give you the intuition that adversarial perturbations aren't magic — they're a search for the directions where the model is least stable, which are usually the directions where the training data gave the least supervision.

---

## Robustness is a profile, not a number

Adversarial perturbations are a kind of distribution shift — a peculiar one. Natural distribution shift is the world declining to stay put: you trained on the past and deployed into a shifted present. That's Hume's induction problem in technical dress, and we met it as distribution shift earlier. An adversarial input lives in a *third* distribution — not natural drift but a constructed worst case, built by following the gradient to the input that maximizes the gap between prediction and truth within a budget.

How related are the two? Somewhat, but not as much as you'd like. A model can be robust against constructed perturbations and brittle under natural drift, or the reverse. What they share is that both reveal the gap between the model's learned representation and the world's actual structure — one along the worst-case axis, the other along the actual-change-over-time axis. Both are informative; neither is sufficient.

Which forces the supervisory move: **robustness is not a single number, it is a profile.** Robust against this attack, brittle against that one; robust on this distribution, brittle on that one. When someone hands you a model and says "it's robust," the only correct first question is *robust against what?* An unqualified "robust" is not a claim — it's decoration on a marketing page. This is the fluency trap wearing a lab coat: a confident, well-formed word standing in for evidence it doesn't carry.

---

## The toolkit — what each tool does and what it costs

Here's the engineering, and the honest way to present it is to name the limit of each tool alongside what it buys, because the limits are the point.

| Tool | What it does | Key cost | What it cannot do |
|---|---|---|---|
| **Adversarial training (PGD-AT)** | Trains on worst-case perturbed inputs, flattening the loss surface | Clean accuracy drops; substantially more expensive than standard training;[^ninex] transfers imperfectly across attack types | Doesn't change the representation — moves the attack surface without closing the proxy gap |
| **Certified defenses (randomized smoothing)** | Turns a base classifier into a smoothed one provably stable within radius $R$ | Thousands of Monte Carlo samples per prediction; certified radius shrinks in high dimensions | Cannot certify outside the radius; too slow for real-time use |
| **Lipschitz-constrained architectures** | Bounds how fast the output can change per unit input change | Lower clean accuracy; requires removing LayerNorm and modifying attention | Bounds maximum sensitivity everywhere; doesn't say *which* inputs are sensitive |
| **Formal verification (α,β-CROWN)** | Proves a property holds for all inputs in a defined region | Scales only to narrow properties on bounded network sizes | Cannot verify natural-language properties; doesn't reach frontier-scale models |
| **Detection-based defenses** | Flags adversarial inputs as outliers, routes to fallback | Adaptive attacks target detector and classifier together | Routes failures; doesn't improve the representation |
| **Input preprocessing** | Strips perturbation signal before it reaches the model | Attackers aware of it optimize perturbations that survive | Fails against adaptive attackers; doesn't touch transfer or prompt injection |

There is no single tool. Every entry has a bounded scope and an honest cost, and deployment-grade robustness comes from layering them and *writing down what each layer doesn't cover.*

**Adversarial training** (PGD-AT) is the strongest empirical defense.[^madry] At each step you compute the worst-case perturbation with projected gradient descent and update the model to classify it correctly:

$$x^{(t+1)} = \Pi_{B_\epsilon(x)}\left( x^{(t)} + \alpha \cdot \text{sign}(\nabla_{x^{(t)}} L(f(x^{(t)}), y)) \right),$$

projecting back into the $\epsilon$-ball after each step. FGSM is the one-step special case.

Now the load-bearing claim, and I'm going to be careful with it because the chapter's headline conclusion rests on it. A 2024 scaling-law study by Bartoldson and colleagues found that on CIFAR-10, $L_\infty$ robustness slowly grows and then plateaus around **90%** — and, crucially, that human accuracy on the fooling set *also* plateaus near 90%, because at the perturbation budgets used in standard $L_\infty$ evaluation the perturbed images begin to genuinely look like the target class or become invalid for their label.[^bartoldson] That 90% ceiling, and the semantic reason for it, is confirmed in the source. The reference chapter also cites a figure of $10^{30}$ FLOPs to reach human-level robustness by scale alone — I could not confirm that specific number in the paper's abstract, so I'm hedging it rather than printing it as fact: the study's scaling extrapolation implies the compute required is astronomically large, effectively foreclosing "just scale up," but the exact figure should be located in the paper body before anyone quotes it. The structural conclusion survives the hedge: the ceiling is governed by the *semantics of the perturbation budget*, and scale alone cannot cross a semantic limit.

**Certified defenses** give a lower bound under *any* attack within a radius. Randomized smoothing builds a smoothed classifier

$$g(x) = \arg\max_c \, \mathbb{E}_{\delta \sim \mathcal{N}(0, \sigma^2 I)}\left[ \mathbf{1}[f(x + \delta) = c] \right],$$

and certifies a radius $R = \frac{\sigma}{2}(\Phi^{-1}(p_A) - \Phi^{-1}(p_B))$ from the top two class probabilities.[^cohen] The cost is severe: thousands of samples per prediction, clean accuracy degrading as $\sigma$ rises, and the radius shrinking as dimensionality grows. **Lipschitz constraints** bound $\|f(x)-f(x')\|_2 \le L\|x-x'\|_2$ so the model can't change its mind sharply — but the exact constant is NP-hard to compute and enforced-Lipschitz transformers currently pay a real clean-accuracy price. (The reference chapter cites a Lipschitz constant "as low as 6"; I couldn't verify that specific figure, and the nearest confirmed 2025 results report a 10-Lipschitz transformer reaching only ~21% accuracy — treat "as low as 6" as unverified.)[^lip] **Formal verification** (α,β-CROWN) is the strongest tool precisely because its guarantees are absolute — within a scope that stays narrow.[^crown]

[^ninex]: The reference chapter states adversarial training is "≈9× more expensive than standard training." I could not source that specific multiple; the per-step cost multiple of PGD training is real but the exact 9× is unverified — read it as "several times to an order of magnitude more expensive."
[^madry]: Aleksander Mądry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, Adrian Vladu, "Towards Deep Learning Models Resistant to Adversarial Attacks," ICLR 2018, arXiv:1706.06083. The accuracy–robustness tension is established in Dimitris Tsipras et al., "Robustness May Be at Odds with Accuracy," ICLR 2019, arXiv:1805.12152.
[^bartoldson]: Brian Bartoldson, James Diffenderfer, Konstantinos Parasyris, Bhavya Kailkhura, "Adversarial Robustness Limits via Scaling-Law and Human-Alignment Studies," ICML 2024, arXiv:2404.09349. The 90% plateau and its semantic cause are confirmed in the abstract; the $10^{30}$-FLOPs figure is not, and is hedged here accordingly.
[^cohen]: Jeremy Cohen, Elan Rosenfeld, J. Zico Kolter, "Certified Adversarial Robustness via Randomized Smoothing," ICML 2019 (PMLR v97, 1310–1320).
[^lip]: Compare Newhouse et al., "Training Transformers with Enforced Lipschitz Constants," 2025, arXiv:2507.13338, which reports a 10-Lipschitz transformer at ~21% accuracy.
[^crown]: α,β-CROWN, Verified-Intelligence; winner of VNN-COMP 2021–2025 (VNN-COMP 2025 summary, arXiv:2512.19007). Complete verification remains bounded to modest network sizes and specifications.

---

## The same structure in different clothes

The proxy-attack framework generalizes, and recognizing it in a new domain is the transferable skill.

**In NLP**, text is discrete — no infinitesimal gradient step in token space — but the structure holds: language models learn surface-level statistical encodings that proxy for meaning and are attackable through paraphrase, invisible Unicode insertion, or prompt injection. The right robustness notion here is *semantic invariance*: same classification under a meaning-preserving rewrite. **In tabular data** — credit, fraud, diagnosis — the attacker is constraint-bound: a debt-to-income ratio can't move arbitrarily without violating other constraints, so the real attack surface is the set of *feasible* manipulations a strategic applicant could actually make, and the proxy features are usually the mutable ones. **In agentic systems**, the agent learns proxies for "owner," "authorized," "trusted source," and those are attackable through crafted messages that present the attacker's signal in the form the proxy responds to.

I want to bound the "same structure" claim, because the reference chapter overstates it. The image case is a continuous, unconstrained, gradient-guided perturbation. The tabular and agentic cases are discrete, feasibility-constrained, strategic attacks. That is a genuinely different threat structure, not the same mechanism in a costume. What is shared is the *diagnostic question* — a learnable proxy, an attackable proxy, a human-relevant feature left untouched — not the attack machinery. "Same structure" is an analogy that pays off in the diagnostic, and it should be read as analogy, not identity.

There's a version specific to LLMs worth naming: **prompt sensitivity** — producing meaningfully different outputs for semantically equivalent prompts ("list the key points" vs. "what are the main takeaways?"). High sensitivity means the model learned surface features of the prompt rather than its content, and in an agentic deployment that's a safety concern, not a quality one: an agent that behaves differently when instructions are phrased emotionally versus neutrally can be steered by phrasing alone.

---

## The question the toolkit can't answer

Adversarial robustness opens a counterfactual the engineering can't close, and the honest move is to open it and *leave it open.*

*This image was classified as a panda. What would the model have classified it as if it had learned the human-relevant features instead of the proxy it actually learned?*

There's no observational data that answers this, because the model that learned the human-relevant features is hypothetical — it doesn't exist, and in many domains we can't even specify what its features would be. That's the deepest limit of the whole framework, and the reference chapter is admirably honest that it applies to exactly the flagship examples: I do not have a clean way to say what counts as a "human-relevant feature" for natural-scene images or language, and saying "the model should learn the features humans use" is only meaningful when you can name them — which is often the original problem.

The counterfactual depends on the institutional structure that produced the model: who trained it, what they optimized for, who reviewed it, what the organization counted as success. The model that learned the human-relevant features is a model made by an organization with different priorities. So the closure is a *governance* question, not an engineering one, and I'll leave it open here — Chapter 12 returns to it. The structural finding of this chapter is exactly that: the honest treatment of adversarial examples requires reasoning about institutional regimes that did not occur.

Which is where the trade-off finally lands. **The robustness toolkit optimized for shrinking the proxy gap in specific, measurable places at the expense of ever closing it in general** — because closing it in general requires a specification of "human-relevant" we usually don't have and an institution built to train against that specification. The toolkit works if you value bounded, documentable guarantees on named attack classes. It fails if you need a general promise that the model learned what you meant. The honest deployment shrinks the gap where it can and leaves the rest of it visible, in writing, where the people reviewing the system can see it.

The shallow lesson of adversarial examples: models are fragile. The deep lesson: models are honest about what this training produced, and what it produced is usually not what the engineers thought.

---

## Exercises

### BUILD — perturb your own pipeline's input; find where it breaks

Fight self-trust. You built this pipeline; you want to believe it holds.

**B1.** Take a model you can run — a pretrained image classifier, a sentiment model, a small LLM. Pick a specific attack class (pixel perturbation, paraphrase, prompt-register shift) and **lock a prediction** *before* running it: what perturbation will flip the behavior, what failure mode it produces, and what the failure reveals about the difference between the model's representation and the human-relevant feature. Then run it, document the result, and where you were wrong name the structural reason. *(Tests: proxy-vs-human-feature diagnosis, prediction-lock.)*

**B2.** For your own pipeline, hypothesize one feature you suspect it uses as a *proxy* for the thing it should track ("uses code-block formatting as a proxy for tested code"; "uses confident phrasing as a proxy for evidence quality"). Build paired inputs — one with the proxy and not the underlying feature, one with the feature and not the proxy — run both, and document which signal the model prioritizes. *(Tests: locating the fragility you designed in.)*

**B3.** Write the robustness profile for your pipeline as a table, not a sentence: attack classes tested, perturbation budgets, clean accuracy, robust accuracy at each budget, and an explicit residual-risk row naming what you did *not* test. *(Tests: robustness-as-profile, honest disclosure.)*

### AUDIT — probe a deployed model or someone's recipe for a fragility you didn't design

You have distance but didn't make the design choices. Reconstruct the threat model you were never told.

**A1.** A vendor claims a facial-recognition model for physical access control is "robust against adversarial examples." Write five specific questions that convert that claim into a usable specification, and for each say what it's testing. *(Tests: "robust against what?" discipline.)*

**A2.** Map the panda→gibbon case onto an agentic owner-identity-spoofing case (a non-owner imitating an owner's display name and register). For each component — the system attacked, the proxy learned, the human-relevant feature, the perturbation, the misclassification — identify the parallel, and then name where the analogy *breaks* (what's genuinely different between a continuous pixel perturbation and a discrete identity spoof). *(Tests: structural transfer plus its honest limits.)*

**A3.** A loan model has been adversarially trained and certified robust within an $L_\infty$ budget of $\epsilon = 0.05$; the deployment team says it "cannot be gamed." Identify two specific ways that claim is false even if the certification is mathematically valid — then articulate, in two paragraphs, why the "what would this model have done under a different representation" counterfactual cannot be answered by the toolkit alone, and what structure would be required to answer it. *(Tests: certified-defense limits, the governance counterfactual.)*
