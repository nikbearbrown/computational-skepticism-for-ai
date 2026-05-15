# Chapter 8 — Robustness: What "Understanding" Means When a Pixel Can Break the Model
*The model is not fragile. The model is honest about what it learned.*

## Learning objectives

By the end of this chapter, you will be able to:

- Distinguish between "the model is fragile" and "the model learned a proxy instead of the human-relevant feature," and explain why the distinction changes the engineering response
- Explain the linearity hypothesis and boundary-tilting perspective as competing geometric accounts of why adversarial examples exist
- Describe the structure of gradient-based, transfer, and patch attacks, and explain why each targets a different level of the model's learned representation
- Identify the tools in the robustness toolkit, articulate the limit of each, and explain why robustness requires a portfolio rather than a single measure
- Explain the accuracy–robustness trade-off and what scaling laws reveal about its limits
- Recognize the same proxy-attack structure across different domains (image classification, NLP, tabular data, agentic identity verification)
- Apply the concept of prompt sensitivity to LLM deployments and explain how it relates to the adversarial robustness framework
- Frame the robustness gap as a Rung 3 counterfactual and explain why it cannot be closed by the engineering toolkit alone

## Prerequisites

Chapters 2–7. Chapter 2's distribution shift framing returns directly. Chapter 5's calibration material is extended at the end. Pearl's Ladder (introduced earlier) is extended to Rung 3. Familiarity with basic gradient descent is helpful for understanding how adversarial perturbations are computed, but not required for the chapter's main arguments.

---

## Why this chapter

The previous chapters have built apparatus for reading data and model outputs critically. This chapter asks a harder question: what has the model actually learned, and how does that differ from what we thought it learned? Adversarial examples are the instrument that makes the gap visible. The chapter uses them to open a Rung 3 counterfactual we will not close until Chapter 13.

---

## The panda becomes a gibbon

I want to show you a picture, or rather, two pictures.

The first picture is a giant panda. You can see this. It's a panda — black and white, sitting in the bamboo, the way pandas sit. An image classifier looks at this picture and reports, with high confidence, "panda." Good. The classifier and you agree.

Now I'm going to show you the second picture. To your eyes, it is the same picture. The panda is still there, in the bamboo, in the same pose, with the same coloring. If I put the two pictures side by side and asked you to spot the difference, you would not be able to do it. Pixel by pixel, the differences are tiny — fractions of a percent of brightness in some channels, here and there, scattered in a pattern that means nothing visual to the human eye. The picture is, for any practical purpose, the same picture.

The classifier looks at the second picture and reports, with even higher confidence, "gibbon." [Verify: Goodfellow, Shlens, and Szegedy 2014, *Explaining and Harnessing Adversarial Examples* — the panda-gibbon figure is from §3.]

<!-- → [FIGURE: Three-panel comparison. Left panel: realistic panda illustration, label beneath "Model: panda (99%)." Center panel: visually identical panda (same illustration), label beneath "Model: gibbon (98%)." Right panel: the perturbation itself rendered as a noise pattern and then amplified ×50 — looks like faint static, no visible structure. A horizontal arrow labeled "δ added" points from panel 1 to panel 2. Callout below panel 3: "Perturbation ×50 amplified — imperceptible at true scale." Caption: "The perturbation is invisble to the human eye. The model's output has flipped to full confidence on the wrong class. The panda has not moved. Something else changed — the high-frequency statistical signature the model was actually using to classify."] -->

I want you to sit with this for a moment, because the natural reaction is the wrong reaction. The natural reaction is to think *the model is broken*, or *the model is brittle*, or *we need to add more training data*. None of those reactions is exactly wrong, but all of them miss the size of what just happened. What happened is that a system which the engineers thought was looking at images of pandas and identifying pandas turned out to be looking at *something else* — something which, on the training set, correlated very nicely with images of pandas, but which can be flipped to "gibbon" by a perturbation that leaves the panda completely untouched.

The model and you were not making the same kind of judgment in the first place. You just thought you were.

---

## What adversarial examples actually expose

Let me start with the language people use, because the language matters. The standard description of what we just saw is "the model is fragile." This framing is so common it is almost invisible. The model is fragile, the engineers say, so we will make it more robust. The verb is "harden." You harden the model the way you harden a piece of metal — by some treatment that doesn't change what the metal is, but makes it harder to dent.

I want you to notice what this framing assumes. It assumes the model has learned the right thing, and the only problem is that the right thing is sitting in a vulnerable form. Make the form less vulnerable, the framing says, and you're done.

This is wrong. The deeper, more useful framing is: *the model has learned a different thing than the engineers thought it learned, and the perturbation reveals the difference*. The model has learned what I will call a *proxy* — a feature, or set of features, in the input distribution that correlated reliably with the right label on the training data. The engineers thought the model had learned "what pandas look like." The model had actually learned "the statistical signature of pixel arrangements that occurred in panda training images." On the training set these are indistinguishable. Under adversarial perturbation they fly apart.

You can see immediately why this changes the engineering problem. If the model is fragile, you can patch it, harden it, smooth its outputs, train it on noisy versions of its inputs. If the model is using the wrong representation, all of those things move the attack surface around without touching the underlying thing. You harden it against this perturbation, and a slightly different perturbation finds a new proxy. The robustness gain is real, but local, and the underlying gap between what the model is learning and what the engineers wanted it to learn is unaffected.

The literature has, over about a decade now, slowly converged on this. Earlier papers framed adversarial examples as a curiosity, a glitch in the matrix, something to be patched with better training. Later papers said something stranger and more honest: adversarial perturbations are not bugs, they are features. They reveal what the model actually responds to. They tell you which features the model has *bet on*, and those are typically not the features you would have wanted it to bet on. [Verify: Ilyas et al. 2019, *Adversarial Examples Are Not Bugs, They Are Features.*]

<!-- → [FIGURE: Two-column comparison diagram. Left column labeled "Fragile framing" — a shield icon with cracks, labeled "Model learned the right thing. Attack is a dent. Fix: harder shield (adversarial training, preprocessing)." An arrow below: "Engineering response: patch the surface." Right column labeled "Proxy framing" — a Venn diagram showing a large circle "What the model learned (proxy)" and a smaller, partially overlapping circle "What the engineers intended (human-relevant feature)." Gap between circles labeled "Representation gap." Arrow below: "Engineering response: diagnose what the model actually learned." Caption: "These are different diagnoses. The fragile framing leads to surface hardening. The proxy framing leads to representation interrogation. The toolkit changes depending on which framing you start from."] -->

So when I say "robustness" in this chapter, I am not asking the engineering question — *how do we patch this?* I am asking the supervisory question: *what does the model's response to adversarial inputs tell me about what the model actually learned, and how does that compare to what I thought it was learning?* The patch is a downstream concern. The diagnosis is the upstream one.

---

## Why adversarial examples exist — two geometric accounts

Before we look at what to do about adversarial examples, let me show you two ways of understanding why they exist at all. You need at least one of these to reason about robustness in a domain you have not seen before.

### The linearity hypothesis

The Fast Gradient Sign Method (FGSM) — the procedure that produced the gibbon — is built on an observation about high-dimensional linear algebra. Consider the simplest possible case: a linear classifier $f(x) = w^T x$. If we perturb the input by a small amount $\delta$, the resulting change in the activation is $w^T \delta$. If we constrain the perturbation to be small in the $L_\infty$ sense — no single coordinate of $\delta$ can exceed $\epsilon$ — then the attacker can maximize the change in activation by setting $\delta = \epsilon \cdot \text{sign}(w)$: push every coordinate in whatever direction the model's weights prefer.

The resulting activation change is $\epsilon \|w\|_1$. In high-dimensional spaces, even if $\epsilon$ is tiny, the $L_1$ norm of the weights grows with the number of dimensions $d$. A perturbation invisibly small in any one coordinate can accumulate into a decisive activation shift across thousands of coordinates.

$$\Delta f = w^T \delta = \epsilon \sum_i |w_i| = \epsilon \|w\|_1$$

Neural networks are not purely linear, but the ReLU activations that dominate practical architectures are piecewise linear. The linearity hypothesis says: the same high-dimensional accumulation effect operates in the locally linear pieces of the network's loss landscape. Compute the gradient of the loss with respect to the input, step in the direction that increases loss, and you have found a direction in which the network is vulnerable.

<!-- → [FIGURE: Two diagrams side by side, sharing a common visual language. Left diagram labeled "Single dimension — invisible": a number line from −1 to +1, a tiny tick at +ε labeled "One coordinate's shift (ε = 0.01)." A note: "Invisible. Irrelevant on its own." Right diagram labeled "High dimensions — decisive": a bar chart with 1000 bars, each of height ε, all pointing in the same direction (positive). The total height of all bars combined is labeled "Σε = ε·d = 1.0 — a full-unit shift in activation." Caption: "The linearity hypothesis: in high dimensions, the same tiny push repeated across thousands of coordinates accumulates into a decisive activation change. The perturbation is imperceptible per-coordinate. The accumulated shift is not."] -->

### The boundary-tilting perspective

The linearity hypothesis explains why perturbations *work* on linear components. It doesn't fully explain why neural networks are *especially* vulnerable compared to other linear classifiers trained on the same data. Tanay and Griffin noted that some linear classifiers — specifically, well-regularized ones trained with substantial margin — do not exhibit adversarial vulnerability at the same rate.

Their explanation: adversarial examples arise when the decision boundary is *tilted* such that it lies very close to the data manifold in directions of low variance. The model has learned a boundary that correctly separates the training classes in the directions the training data varies most — but in the low-variance directions, directions where the training data doesn't vary much and the model received little signal, the boundary can be arbitrarily close to the data manifold. An adversarial perturbation exploits exactly those low-variance directions: small steps in a direction the model was never trained to stabilize.

This is a more structural explanation. It says adversarial examples are a symptom of the model's failure to regularize its decision boundary in all relevant directions — and, more specifically, that the boundaries were poorly constrained in the directions that didn't matter much during training but do matter during deployment when an attacker is present.

<!-- → [FIGURE: A 2D data diagram. An elongated oval represents the data manifold — the long axis is the high-variance direction, the short axis is the low-variance direction. A decision boundary (a diagonal line) cuts through the oval. Along the long axis, the boundary has a wide margin to both sides — well-regularized. Along the short axis (low-variance direction), the boundary passes very close to several data points on the "correct" side. One data point near the short-axis boundary has a short arrow pointing perpendicular to the boundary, labeled "adversarial perturbation — small step in low-variance direction." The arrow crosses the boundary. Caption: "Boundary tilting: the model was well-trained along the high-variance directions, but the boundary is nearly tangent to the data manifold in low-variance directions. An adversarial perturbation targets the gap the training data never forced the model to close."] -->

Neither account is complete on its own. But together they give you a working intuition: adversarial perturbations are not magic. They are gradient-guided searches for the directions in input space where the model is least stable, most often the directions where training data provided the least supervision.

---

## A taxonomy of attacks — what each targets

The adversarial attack literature has expanded well beyond the simple image-perturbation case. Knowing the taxonomy matters because each attack class reveals a different thing about the model, and the appropriate defensive response depends on which attack you are defending against.

| Attack Class | What it requires from the attacker | What it exploits in the model | Domains where it applies | Key defensive response |
|---|---|---|---|---|
| **Gradient-based (white-box)** | Full access to model weights and gradients | The specific geometry of this model's loss surface | Image, audio, any differentiable model | Adversarial training, input certification |
| **Query-based (black-box)** | Access to model outputs only; no weights visible | Approximate gradient estimation from output probing | API-deployed models, LLMs | Output monitoring, query rate limiting |
| **Transfer-based** | A surrogate model; no access to the target | Shared proxy feature manifolds across models trained on similar data | Hidden architectures, proprietary models | Representation diversity, ensemble defenses |
| **Patch / physical** | Ability to modify input in the physical world (sticker, glasses, printed pattern) | Spatial localization — high-magnitude perturbation in a small region | Autonomous vehicles, facial recognition, physical access control | Spatial input validation, environment monitoring |
| **Natural adversarial** | No modification — naturally occurring long-tail inputs | Model's failure to generalize beyond the training manifold | Real-world safety benchmarks, OOD monitoring | Distribution-shift monitoring, holdout on tail populations |
| **Prompt injection (agentic)** | Ability to insert adversarial text into a processing pipeline | Conflation of instructions and data in the same input stream | LLMs, agentic pipelines with tool access | Instruction-data separation, output sandboxing |

*The taxonomy matters because each class reveals a different gap. The correct defensive response depends on which attack is present in your threat model — not on which attack appears most in the research literature.*

Two distinctions in this taxonomy are worth dwelling on.

**White-box vs. transfer attacks.** White-box attacks exploit the specific geometry of this specific model. Transfer attacks exploit something broader — the fact that models trained on similar data tend to learn similar features, and perturbations designed for one model tend to work on others. Transfer attacks succeed because the underlying proxy features are often shared. If two fraud-detection models trained on the same transaction data both learned the same proxy for "legitimate transaction," a perturbation designed to fool Model A will likely fool Model B, even if Model B has a different architecture and was never directly attacked.

This is the research finding that named the problem most clearly: the proxies are not quirks of individual models. They are structural properties of the training data that any model learning to minimize loss on that data is likely to exploit. The attacker does not need access to your model. They need access to your training distribution.

**Prompt injection in agentic systems.** This attack class barely existed as a named category five years ago. It has become one of the most practically important. The mechanism is structurally different from the pixel-perturbation case. In an image classifier, the model processes input and produces a label. There is no second-order effect. In an agentic LLM, the model processes input, produces an action, takes that action in the world, receives new input from the environment, processes that new input, and so on. Untrusted content from an external tool — a document the agent retrieved, a webpage it loaded, a calendar event it read — can contain adversarial instructions that the model processes as legitimate commands. The attack surface is the entire information flow of the agent's runtime, not just the initial prompt. We return to this in Chapter 9.

---

## Distribution shift, returning from Chapter 2

We met something like this in Chapter 2, although I called it by a different name. Hume's induction problem, dressed in technical clothing — the model trained on the past, the world declining to cooperate when the deployment runs in a future where the past has shifted. *Distribution shift*, we called it. The training distribution is one place; the deployment distribution is another; the gap is where the model's confidence breaks down.

Adversarial perturbations are a kind of distribution shift, but a peculiar one. They are not natural drift — the world has not changed. They are *constructed*. Somebody, or some procedure, has deliberately built an input that lives in a third distribution, designed to maximize the gap between the model's prediction and the true label. The construction is mathematical: follow the gradient of the model's loss with respect to its input, take a small step in the direction that increases loss the most, repeat. The resulting input is, by construction, the worst-case input within whatever budget you allowed yourself.

<!-- → [FIGURE: A 2D input space diagram with three overlapping oval regions. Center oval (blue, solid outline): "Training distribution — what the model learned on." Overlapping oval to the right (orange, dashed outline): "Natural deployment distribution — the world has drifted." A separate region just outside both ovals (red, pointed ellipse): "Adversarial distribution — constructed by gradient ascent, worst-case inputs within perturbation budget ε." A gradient arrow from a point in the blue oval pointing toward the red region, labeled "gradient ascent on loss." Two annotation lines: blue-to-orange gap labeled "Distribution shift: natural, gradual, often undetected until harm." Blue-to-red gap labeled "Adversarial attack: deliberate, geometrically targeted, worst-case by construction." Caption: "These are not the same risk. A robust model needs to account for both axes separately. Neither robustness against adversarial attack nor robustness against distribution shift guarantees robustness against the other."] -->

Now: how related is the model's behavior on worst-case adversarial inputs to its behavior on naturally occurring distribution shifts? You might hope they are tightly related — that an adversarially robust model is robust generally. The honest answer is *somewhat, but not as much as you'd like*. A model can be highly robust against constructed perturbations and still brittle when the world's distribution drifts naturally. A model can be brittle against constructed perturbations and survive certain natural shifts gracefully.

What they have in common — and this is the lesson to carry from the comparison — is that they both reveal the gap between the model's learned representation and the world's actual structure. Adversarial perturbations reveal it along the axis of *worst-case input perturbation*. Natural distribution shift reveals it along the axis of *actual changes in the input distribution over time and context*. Both are informative. Neither is sufficient.

The supervisory move that follows: *robustness is not a single number*. It is a profile. Robust against this kind of attack, brittle against that kind, robust on this distribution, brittle on that one. When somebody hands you a model and says "it's robust," your first question should be "robust against what?" If the answer is general — "robust" without a specification — that is not a claim. That is decoration on the marketing page.

---

## The robustness toolkit — what each tool does and what it costs

Now the engineering. There is a robustness toolkit, and I want to walk through it systematically, because each tool has a use and a limit, and the limits add up to the picture I'm trying to draw.

| Tool | What it does | Key cost | What it cannot do |
|---|---|---|---|
| **Adversarial training (PGD-AT)** | Incorporates adversarially perturbed inputs into the training loop, flattening the loss surface | Clean accuracy drops; ≈9× more expensive than standard training; robustness transfers imperfectly to other attack types | Does not change the model's representation — moves the attack surface without closing the proxy gap |
| **Certified defenses (randomized smoothing)** | Transforms a base classifier into a smoothed classifier with provable stability within radius $R$ | Requires thousands of Monte Carlo samples per prediction; high $\sigma$ degrades clean accuracy; certified radius shrinks in high dimensions | Cannot certify against attacks outside the radius; prohibitively slow for real-time use |
| **Lipschitz-constrained architectures** | Enforces a bounded rate of output change per unit input change; "verifiable by design" | Currently lower clean accuracy than unconstrained baselines; requires removing LayerNorm and modifying attention | Does not specify which inputs are sensitive — only bounds maximum sensitivity everywhere |
| **Formal verification (α,β-CROWN)** | Proves mathematically that a property holds for all inputs in a defined region | Scales only to narrow properties on models up to millions of parameters; does not scale to frontier models or open-ended properties | Cannot verify natural-language properties; cannot scale to the models most practitioners actually deploy |
| **Detection-based defenses** | Identifies adversarial inputs as outliers and routes to fallback or human review | Adaptive attacks can target detector and classifier simultaneously (BPDA / obfuscated gradients); adds latency | Does not improve the model's representation — routes failures, does not eliminate them |
| **Input preprocessing** | Removes perturbation signal before it reaches the model (denoising, quantization, smoothing) | Adaptive attackers aware of preprocessing can optimize perturbations that survive it; blunts but rarely eliminates exposure | Fails against attackers with knowledge of preprocessing; does not address transfer attacks or prompt injection |

*There is no single tool. Every entry has a bounded scope and an honest cost. Deployment-grade robustness comes from layering these tools and documenting what each layer does not cover.*

### Adversarial training and its scaling limits

Adversarial Training (AT), particularly the PGD-AT framework, remains the most effective empirical defense. The idea: during training, at each step, compute the worst-case input perturbation using Projected Gradient Descent (PGD), then update the model to correctly classify that worst-case input. The model learns to flatten its loss surface in the directions an attacker would exploit.

PGD, the standard attack used in AT, is iterative:

$$x^{(t+1)} = \Pi_{B_\epsilon(x)} \left( x^{(t)} + \alpha \cdot \text{sign}(\nabla_{x^{(t)}} L(f(x^{(t)}), y)) \right)$$

where $\Pi_{B_\epsilon(x)}$ projects back into the $\epsilon$-ball around the original input after each step, and $\alpha$ is the step size. Running this for 10–50 steps typically produces a strong attack; FGSM is the one-step special case.

The accuracy–robustness trade-off is well documented and has now been quantified by scaling law studies. A 2024 analysis found that while larger models and more data improve robustness, the gains follow a power-law relationship with diminishing returns. More troubling: the predicted limit of $L_\infty$ robustness on CIFAR-10 — the amount of robustness you can achieve with arbitrarily much compute and data — is around 90%. The reason is structural: at the perturbation budgets used in standard $L_\infty$ evaluation, the perturbed images begin to actually look like the target class to human eyes. You have hit the ceiling of what is semantically possible. Reaching human-level robustness on a standard benchmark has been estimated to require compute on the order of $10^{30}$ FLOPs — suggesting that scale alone cannot close this gap. [Verify: Bartoldson et al. 2024, *Adversarial Robustness Limits.*]

<!-- → [CHART: Line chart — x-axis "Log₁₀ compute (FLOPs, from 10¹² to 10³⁰)," y-axis "Accuracy (%)." Three curves: Curve 1 (blue): "Clean accuracy — standard training," starting high (~95%) and plateauing near 97%. Curve 2 (orange): "Robust accuracy — adversarially trained," starting lower (~50%) and rising slowly, with a projected ceiling annotated as a dashed horizontal line at ~90%, labeled "Predicted ceiling: semantic ambiguity limit." Curve 3 (gray, between curves 1 and 2): shaded region labeled "Accuracy–robustness gap — persists at all compute levels." Vertical annotation at the far right of the x-axis: "~10³⁰ FLOPs predicted for human-level robustness." Caption: "The accuracy–robustness trade-off is not an artifact of insufficient compute. The ceiling is governed by the semantics of the perturbation budget: at some ε, perturbed images genuinely look like the target class to human eyes. Scale alone cannot cross this limit."] -->

### Certified defenses — what "guaranteed" means and costs

Adversarial training improves empirical robustness but does not prove anything. Certified defenses provide a lower bound on accuracy under *any* possible attack within a defined radius. Randomized Smoothing (RS) achieves this by transforming a base classifier $f$ into a smoothed classifier:

$$g(x) = \arg\max_c \, \mathbb{E}_{\delta \sim \mathcal{N}(0, \sigma^2 I)} \left[ \mathbf{1}[f(x + \delta) = c] \right]$$

The certification result: if class $c_A$ has sufficiently higher probability than any other class under this smoothed distribution, then $g(x)$ is guaranteed to return $c_A$ for any input within a radius $R = \frac{\sigma}{2}(\Phi^{-1}(p_A) - \Phi^{-1}(p_B))$, where $p_A$ is the probability of the top class, $p_B$ is the probability of the runner-up, and $\Phi^{-1}$ is the inverse standard normal CDF. [Verify: Cohen, Rosenfeld, and Kolter 2019, *Certified Adversarial Robustness via Randomized Smoothing.*]

The practical limits are severe. Certifying each prediction requires thousands of Monte Carlo samples — running the base classifier thousands of times with different noise samples and aggregating. High $\sigma$ produces large certified radii but heavily degrades clean accuracy, because the classifier must operate on heavily blurred inputs. And in high-dimensional input spaces, the certified radius shrinks as dimensionality grows: the noise needed to smooth out perturbations simultaneously obscures the signal needed to classify correctly.

<!-- → [FIGURE: Two-panel diagram. Left panel: "Smoothed classifier geometry" — a data point x at the center, surrounded by a circle of radius R labeled "Certified region: g(x) = cA for all x' within R." Arrows pointing from x to the circle boundary, each labeled "+noise sample." Caption: "The classifier votes by majority across thousands of noisy versions of the input." Right panel: "The σ tradeoff" — a two-axis diagram with σ (noise magnitude) on the x-axis, and two curves: "Certified radius R" (rising with σ) and "Clean accuracy" (falling with σ). The two curves cross, labeled "Operating point: choose σ to balance R and clean accuracy." Caption: "Higher σ buys a bigger certified radius but at the cost of clean accuracy. The cross is not at a good number for most real deployments."] -->

### Lipschitz constraints and verifiable-by-design architectures

A more structural approach is to constrain the model's Lipschitz constant — the maximum rate of change of the model's output with respect to its input. A model with Lipschitz constant $L$ satisfies $\|f(x) - f(x')\|_2 \leq L \|x - x'\|_2$ for all $x, x'$. A small Lipschitz constant means the model cannot change its mind sharply in response to small input changes — by definition, robustly stable.

The challenge: computing the exact Lipschitz constant for a neural network is NP-hard, and the product of layer-wise constants (the standard upper bound) is typically a massive overestimate. Recent work has trained Transformer-scale models with enforced Lipschitz bounds as low as 6 — meaning the output can change at most 6 times as fast as the input, in $L_2$ norm. These architectures require removing LayerNorm and modifying self-attention, and currently pay a clean-accuracy cost. But they provide a foundation for differential privacy and weight quantization that unconstrained models cannot offer. [Verify: Delattre et al. 2025 on Lipschitz-constrained Transformers.]

### Formal verification — the strongest tool and its scope limits

Formal verification tools answer a yes/no question: does this model satisfy this property for all inputs in this region? The $\alpha,\beta$-CROWN framework, the current state of the art, combines linear bound propagation with branch-and-bound search. It can verify models with millions of parameters on narrow properties (specific perturbation regions, binary classification decisions). For larger models and richer properties — "the model never generates harmful text" — verification does not scale. [Verify: current scope of $\alpha,\beta$-CROWN before publication.]

Formal verification is the strongest tool in the toolkit precisely because its guarantees are absolute within scope. The scope is narrow. For deployment decisions, knowing that a model satisfies a specific narrow property with certainty is sometimes worth more than knowing it satisfies a broad property empirically most of the time.

<!-- → [FIGURE: Verification generation timeline — a horizontal progression showing four generations with key facts. Generation 1 (Reluplex, 2017): "SMT solvers for piecewise-linear neurons. Scope: tens of neurons." Generation 2 (CROWN): "Linear bound propagation. Scope: medium CNNs, seconds per query." Generation 3 (α,β-CROWN): "Optimized bounds + branch-and-bound. Scope: ResNets, millions of parameters." Generation 4 (Frontier, 2025): "Branch-and-bound with learned cuts. Scope: large verified subproblems." A dashed line at the right labeled "Gap: natural language properties, open-ended behavior, frontier LLMs — verification does not reach here yet." Caption: "Verification is the strongest tool in the toolkit. Its scope has expanded dramatically. The gap between what it can verify and what practitioners need to verify is still large."] -->

---

## Non-robust features — the deepest account

I want to pause the toolkit survey to address the deepest theoretical account of why adversarial examples exist. The Ilyas et al. (2019) paper proposed a framing that remains both influential and contested, because it reframes the problem at the level of the training data rather than the model architecture.

The argument: natural datasets contain two types of features. *Robust features* are correlated with the label and stable under small perturbations — the shapes, textures, and structural properties that humans use for recognition. *Non-robust features* are also correlated with the label on the training distribution, but are high-frequency, brittle, and semantically meaningless to humans — statistical patterns in pixel arrangements that happen to co-occur with particular classes but are easily disrupted by small perturbations.

Supervised learning, minimizing a cross-entropy loss, does not distinguish between these two feature types. It uses whichever features are most predictive on the training set. Non-robust features are often *more* predictive than robust features because they are lower-variance and more tightly correlated with label on the training distribution. The model bets on them because betting on them wins.

Adversarial perturbations then become something cleaner than "noise" — they are *deliberate manipulations of non-robust features*, moving them in the direction of a different class while leaving the robust features unchanged. The panda's shape, posture, and coloring remain. The high-frequency statistical signature shifts toward the gibbon's statistical signature. The model reports "gibbon" because it placed more weight on the statistical signature than on the shape.

<!-- → [FIGURE: Feature decomposition diagram for a panda image. Left box: "Robust features" — a simplified panda silhouette with annotations pointing to shape features: "Rounded body shape," "Black and white color patches," "Bamboo posture." Right box: "Non-robust features" — a noise-pattern visualization labeled "High-frequency pixel statistics: co-occur with panda class on training data but perceptually meaningless." Center: a supervised classifier with two input arrows from left and right boxes. Label on left arrow: "Both features equally predictive on training data." Callout on right: "Adversarial perturbation: shifts non-robust features toward 'gibbon' statistics. Robust features unchanged." Caption: "Supervised loss cannot distinguish between these feature types. It bets on whichever is more predictive. Non-robust features often win that bet — and adversarial perturbations exploit that win."] -->

The contested extension: some researchers proposed that if you could train a model *only* on robust features, adversarial vulnerability would disappear. This turns out to be too simple. Models trained on "robust datasets" (datasets from which non-robust features have been removed) still exhibit adversarial vulnerability under sophisticated attacks like AutoAttack. And models trained with self-supervised objectives rather than supervised classification do not show the same sharp non-robust feature patterns, suggesting these features are specific to the supervised-classification regime rather than universal. [Verify: status of "features not bugs" debate, 2023–2025.]

What survives the debate: the insight that proxy features are structural properties of the training data and objective, not random bugs of particular architectures. The search for the right representation is not a search for better training tricks. It is a search for training objectives and data that produce feature structures aligned with human-relevant concepts.

---

## Cross-domain transfer — the same structure in different clothes

The proxy-attack framework generalizes beyond image classification. Understanding how the same structure shows up in other domains is how you recognize it the first time in a domain you haven't seen.

**In NLP.** Text is discrete — you cannot take an infinitesimal gradient step in the space of tokens. But the underlying problem is the same: language models learn proxy features that correlate with human-relevant concepts on the training distribution but are attackable. Paraphrase attacks rewrite an input with semantically equivalent content that the model classifies differently. Unicode attacks insert visually invisible characters that shift tokenization and change model behavior. Prompt injection, discussed above, conflates instruction and data streams. The attackable feature in all cases is the model's surface-level statistical encoding of language, not the human-relevant concept the encoding is supposed to represent.

The appropriate concept for NLP robustness is *semantic invariance*: a robust model should produce the same classification when the input is rewritten in a different style, vocabulary, or emotional register while preserving meaning. Testing for semantic invariance is a form of adversarial evaluation specific to this domain.

**In tabular data.** Fraud detection, credit scoring, medical diagnosis — these are all tabular models, and they are all adversarially attackable, but the constraint structure is different. A pixel can be shifted by an arbitrary small amount. A loan applicant's debt-to-income ratio cannot be shifted arbitrarily without violating other constraints — debt cannot exceed income, income must be non-negative, the combination of features must be physically possible for a real applicant. This means gradient-based attacks often produce "invalid" data points — feature combinations that would fail basic sanity checks — and the real attack surface is not the gradient direction but the set of feasible feature manipulations a strategic applicant could actually make.

For tabular robustness, the question is: which features are immutable (age, birthplace, historical events), which are mutable within constraints (debt level, employment status), and which are mutable at arbitrary cost? The proxy features in a credit model are typically the mutable features — the ones a sophisticated applicant can manipulate. The human-relevant features are typically the more structural ones.

**In agentic systems.** We return to this in detail in Chapter 9, but the structure is the same. The agent has learned proxy signals for concepts like "owner," "authorized action," "trusted source." Those proxies are attackable through the inputs the agent processes — messages, documents, tool outputs. The attack is not a pixel perturbation; it is a crafted message that presents the attacker's signal in the form that the agent's proxy feature responds to. The remediation is identical in structure to the image case: identify what the proxy is, identify the human-relevant feature it approximates, and redesign the system to load-bear on the human-relevant feature rather than the proxy.

| Domain | What the model learns as proxy | The human-relevant feature it approximates | Primary attack vector | Robustness measure |
|---|---|---|---|---|
| **Image classification** | High-frequency pixel statistics co-occurring with the class label | Object shape and structural semantics | Gradient-based $L_\infty$ perturbation | Adversarial training, input certification |
| **NLP / LLM** | Surface-level token co-occurrence and syntactic patterns | Semantic meaning and communicative intent | Paraphrase attacks, Unicode insertion, prompt injection | Semantic invariance testing, instruction-data separation |
| **Tabular (credit / fraud)** | Mutable feature combinations that correlate with outcome on training data | Fundamental creditworthiness or fraud risk | Strategic feature manipulation within feasibility constraints | Domain-constrained adversarial evaluation, feature-immutability audits |
| **Agentic systems** | Conversational and display-layer identity signals (display name, tone, phrasing) | Verified social-legal ownership and authorization | Proxy spoofing via crafted messages in the agent's information stream | Cryptographic credentials, output sandboxing, adversarial prompting |

*Same structure, different surface. In every domain: a learnable proxy, an attackable proxy, a human-relevant feature left untouched. The appropriate defense differs by domain; the diagnostic question is always the same.*

---

## Prompt sensitivity — the LLM-specific version of this problem

There is a version of adversarial robustness that is specific to LLMs and has become practically important enough to warrant its own treatment. It goes by a different name in the literature — *prompt sensitivity* — but it is the same structure.

A prompt-sensitive model is one that produces significantly different outputs in response to semantically equivalent prompts. "List the key points of this document" and "What are the main takeaways from this document?" are semantically equivalent instructions. A prompt-sensitive model may respond to them very differently — different tone, different organization, different emphasis, different factual content. A robust model, in the adversarial sense, should be stable under this kind of semantic rephrase.

The recent IPS (Interaction-based Prompt Sensitivity) framework measures this formally, decomposing the model's output into contributions from different prompt components and measuring how much the output changes when those components are varied while semantic content is held constant. High IPS indicates that the model has learned surface-level features of the prompt — phrasing, syntax, emotional tone — rather than the semantic content those features are meant to convey.

Four factors reduce prompt sensitivity in practice: supervised fine-tuning on diverse phrasings, larger model scale, dense architectures with redundant information pathways, and few-shot context that anchors the model's interpretation. [Verify: Zhang et al. 2025, *IPS: Interaction-based Prompt Sensitivity.*]

For agentic deployments, prompt sensitivity is not merely a quality concern — it is a safety concern. An agent that behaves differently when instructions are phrased emotionally versus neutrally, or formally versus casually, cannot reliably follow instructions across the range of real-world phrasing. A malicious input phrased in an emotionally intense register may trigger behaviors that a neutral phrasing of the same content would not. Evaluating prompt sensitivity is a required step in responsible agentic deployment.

<!-- → [FIGURE: Prompt sensitivity diagram. Center: an LLM icon. Six arrows pointing in from left — each arrow is a different phrasing of the same instruction: "List the key points," "What are the main takeaways?", "Summarize the key ideas," "Can you highlight what matters here?", "Give me the TL;DR," "Enumerate the important points." Each arrow is labeled with a different output icon (different symbols representing different response structures and emphases). A label below: "Semantically equivalent input → structurally different outputs = high prompt sensitivity." A second version of the same diagram on the right, with all six arrows producing the same output icon: "Low prompt sensitivity — stable under semantic rephrase." Caption: "Prompt sensitivity is adversarial robustness at the instruction layer. A highly sensitive model has learned surface-level prompt features rather than semantic content. In an agentic deployment, high sensitivity is exploitable."] -->

---

## Pearl's Ladder Rung 3 — opened, not closed

I want to open a question now and not close it, because closing it will take another chapter.

You may know Pearl's Ladder — three rungs of causal reasoning. Rung 1 is association: *what is the probability of Y given X?* Standard statistics. Rung 2 is intervention: *what is the probability of Y if I set X to a specific value?* Causal inference territory. Rung 3 is counterfactual: *what would have happened in this specific case if X had been different, holding everything else the same?* The hardest rung. The one that requires you to reason about possibilities that did not occur.

Adversarial robustness opens a Rung 3 question the lower rungs cannot answer. Look:

*This image was classified as a panda. What would the model have classified it as if it had learned the human-relevant features instead of the proxy features it actually learned?*

This is a counterfactual. It asks about a specific case (this image) under a specific intervention (the model has a different internal representation) holding everything else constant (same image, same task, same downstream system). There is no observational data that answers it, because the model that learned the human-relevant features is hypothetical — it does not exist, we have not built it, and in some domains we do not even know how to specify what its features would be.

Recent work in representation learning has attempted to formalize this question through causal proxy models and the notion of *Probability of Sufficiency* — asking whether a given feature is a sufficient cause of the label in the causal sense, not just a correlate of it in the statistical sense. A feature is human-relevant, in this framing, if it corresponds to an independent degree of freedom in the actual process that generates the labeled object. [Verify: Delattre et al. 2023, *Formalizing Representation Learning Desiderata.*] This is a step toward specification, but it does not yet close the counterfactual — because specifying what counts as "independent degree of freedom in the generation process" requires a structural causal model of the domain, which most deployments do not have.

<!-- → [FIGURE: Pearl's Ladder diagram — three rungs, each as a labeled horizontal bar. Rung 1 (bottom): "Association — P(Y|X). What is? Observational. Statistics." Rung 2 (middle): "Intervention — P(Y|do(X)). What if I set X? Causal inference." Rung 3 (top): "Counterfactual — 'What would Y have been if X had been different, holding everything else constant?' Requires hypothetical world." An annotation arrow points from Rung 3 to a text box to the right: "The robustness gap question lives here: 'What would the model have classified this panda as if it had learned human-relevant features instead of the proxy?' No observational data answers this. No robustness toolkit closes it. Requires specifying what the model should have learned — and that requires institutional choices we examine in Chapter 13." Caption: "Adversarial examples open a Rung 3 question. The engineering toolkit operates on Rungs 1 and 2. The gap is not an oversight in the toolkit — it is a structural property of the question."] -->

The question is meaningful, and important, and I want to leave it open here, because closing it requires something this chapter cannot fully ground. *The counterfactual depends on the institutional structures that produced the model* — who trained it, what they optimized for, who reviewed it, what the organization counted as "successful" training. The model that learned the human-relevant features is a model that was made by an organization with different priorities than the one that actually made this model. The Rung 3 closure, in other words, is a *governance counterfactual* — a question about what the model would have been if the institutional regime around it had been different.

We will close this in Chapter 13. For now, hold the question. The fact that adversarial examples expose a Rung 3 gap — the fact that their honest treatment requires counterfactual reasoning about institutional regimes that did not occur — is the structural finding of this chapter.

---

## The same structure at a different scale — Case #8 (Owner Identity Spoofing)

I want to give you one more example, because the panda is starting to sound abstract, and the same pattern shows up at a totally different scale, in a totally different system. Seeing it twice will let you recognize it the third time without my help.

Consider an autonomous agent operating in a system with multiple users. Ownership of resources — files, accounts, projects — is determined, from the agent's point of view, by attributes the agent reads from the user's profile and from the conversational context. Display name. Preferred salutation. Conversational style. The signals that, in human-to-human interaction, function as identity cues.

These signals are *proxies* for the legitimate underlying ownership. The proxies are attackable. A non-owner with the right display name, the right conversational style, the right signals, presents to the agent as the owner. The agent treats them as the owner. The non-owner now has access to the owner's resources, through the agent, by spoofing identity at the proxy layer.

<!-- → [FIGURE: Two parallel vertical attack chains side by side, connected by a "Same structure" label. Left chain labeled "Image classification attack": Input box "Panda image" → Process box "FGSM perturbation (modifies high-frequency pixel statistics)" → Output box "Gibbon (98%)." A crossed-out bypass arrow labeled "Human-relevant feature: actual panda shape — untouched, bypassed." Right chain labeled "Identity-spoofing attack": Input box "Owner's profile" → Process box "Proxy spoofing (matches display name, conversational style, salutation)" → Output box "Agent treats attacker as owner." A crossed-out bypass arrow labeled "Human-relevant feature: actual social-legal ownership — untouched, bypassed." Caption: "Same structure. The proxy is learned. The proxy is attacked. The human-relevant feature is untouched. The output is flipped. Pixels in one case; display names in the other."] -->

This is the same structural failure as the panda-gibbon. The agent learned a proxy for a concept. The proxy was attackable by a perturbation that left the human-relevant feature — actual social-and-legal ownership — completely untouched. The perturbation flipped the agent's classification of "owner" from the actual owner to the imposter. Pixels in one case; display names in the other; the structure is identical.

The toolkit from the previous section partially translates. Detection — can the agent detect spoofed identities? Architecture — can the agent use cryptographic credentials instead of conversational proxies? Adversarial training and certified defenses translate less cleanly, because the input space is different and the perturbation set is harder to define. But the underlying supervisory move is identical: *specify what robustness means in this deployment, then test for that specifically.*

The Rung 3 question for this case is the same shape as the one for the panda: *what would the agent have done if it had been built with stronger ownership signals as the load-bearing input feature instead of conversational proxies?* The counterfactual depends on the design choices of the framework's developers, which depended on the constraints they were operating under, which depended on the priorities of the organizations deploying the agents. Same governance counterfactual. We will be inside it, properly, in Chapter 13.

---

## Towards honest robustness disclosure

The institutional dimension of robustness has moved from informal best practice to structured expectation. The NIST AI Risk Management Framework (AI RMF 1.0) treats robustness as a socio-technical property — one that cannot be evaluated by technical metrics alone, because the appropriate threat model depends on the deployment context, the stakeholder population, and the institutional incentives that shaped the training regime. [Verify: NIST 2023, *AI Risk Management Framework.*]

What this means practically for deployment documentation: a robustness claim in a model card or deployment approval document is not a number. It is a structured disclosure with at least three components.

**Robustness profile** — multi-axis reporting that names what attack classes were tested, what perturbation budgets were used, what the clean accuracy is, what the adversarially robust accuracy is at each budget, and what natural distribution shifts were tested. The profile is a table, not a sentence.

**Residual risk disclosure** — an explicit accounting of known vulnerabilities that were not mitigated. A model that has been adversarially trained against $L_\infty$ perturbations is not robust against transfer attacks, patch attacks, or prompt injection. Say this. Saying it is not a reason not to deploy. It is what makes deployment responsible.

**Monitoring specification** — what will be monitored in production to detect when the robustness envelope is being violated? What is the trigger for human review or rollback?

This is not extra paperwork. It is the difference between a deployment that knows what it is and one that doesn't. The former can be safely operated. The latter cannot.

**Section 1 — Robustness profile**

| Attack class tested | Perturbation budget used | Clean accuracy | Robust accuracy at budget | Notes |
|---|---|---|---|---|
| **$L_\infty$ white-box** (FGSM / PGD) | $\epsilon = 0.03$ | 94% | 71% | Standard benchmark |
| **Transfer attack** | Surrogate: ResNet-50 | 94% | 58% | Surrogate trained on same data |
| **Natural distribution shift** | Domain: Q4 2023 vs Q1 2024 | 94% | 87% | Time-shift only |

**Section 2 — Residual risk**

The following attack classes were *not* evaluated or mitigated: _________________

The following distribution shifts are known but *not* covered: _________________

**Section 3 — Monitoring specification**

Production-time signals to monitor: _________________

Trigger for human review: _________________

Rollback criterion: _________________

*A robustness profile is a table, not a sentence. A claim without this structure is not a claim.*

---

## Glimmer 8.1 — Design the attack, predict the failure mode

The exercise:

1. Pick a model you can run — a pretrained image classifier, a sentiment classifier, a text-to-image system. Something where you can run inputs and see outputs.
2. Specify a class of attack you intend to design. Pixel perturbation, paraphrase attack, prompt injection, jailbreak, social-engineering signal manipulation. Be specific about the attack class.
3. *Lock your prediction:* before designing or running the attack, predict (a) what kind of perturbation will succeed in flipping the model's behavior, (b) what specific failure mode the perturbation will produce, (c) what the failure reveals about the difference between the model's representation and the human-relevant features.
4. Design and run the attack. Document the results.
5. Compare against your predictions. Where you were wrong, identify the structural reason. Where you were right, identify what about the model's design made the prediction tractable.
6. Open the Rung 3 question: *in counterfactual, what would the model have done if it had learned a different representation? Specifically, which representational change would have made this attack fail?* Do not close the counterfactual. Pose it cleanly.

The deliverable is the attack, the prediction, the trace, the structural reason, and the Rung 3 framing. The grade is on the structural reason and the Rung 3 framing. *The attack design is the easy part. The structural account is the work.*

---

## Calibration baseline — second measure

This is the second of three times the calibration baseline appears in this book. (The first was Chapter 2. The third will be Chapter 14.)

You take the same exercise — a set of forecasting questions, each requiring a 90% confidence interval — and complete it again. The expected pattern is improvement: your intervals should now better contain the truths, not because you know more facts, but because you have spent eight weeks operating in a frame that takes uncertainty seriously.

If your second measure looks like your first, the apparatus has not landed. Specifically: if your intervals are still too narrow, you are still systematically overconfident, which means the prediction-locking, the gap analysis, and the supervisory framing have not yet shifted your operational stance.

This is diagnostic feedback. A second baseline that looks like the first is not a moral failing. It is a signal — for the student, for the instructor — that the chapters between baselines have not produced the recalibration they were supposed to produce. Act on it.

The third baseline, in Chapter 14, closes the arc.

---

## What would change my mind

If a robustness method emerged that simultaneously closed the gap between model representations and human-relevant features — across multiple modalities, with theoretical guarantees that survived adaptive attacks — the "different representation, not just fragile" framing of this chapter would weaken. As of this writing, no such method exists. The progress in adversarial robustness has been steady and incremental. The representation gap remains. [Verify: current state of the art in representation-level robustness before publication.]

I do not have a clean way to specify what counts as a "human-relevant feature" for a deployment without creating a downstream specification problem of equal magnitude. Saying "the model should learn the features humans use" is meaningful only when we can name those features, and naming them is often the original problem. In some domains — radiology, fraud detection, chess — the features are well-articulated. In others — image classification of natural scenes, language understanding — they are not. The general specification problem is open.

On scaling: the 2024 scaling law literature suggests that reaching human-level adversarial robustness through compute alone requires $10^{30}$ FLOPs — effectively foreclosing the "just scale up" response. If architectural innovations like Lipschitz-constrained networks improve their clean-accuracy gap substantially, the landscape shifts. I have not seen this happen yet at scale; I would update significantly if it did.

---

## Synthesis — what this chapter leaves you with

Adversarial examples are not evidence that models are fragile. They are evidence that models have learned different representations than their engineers thought — and that the gap between the learned proxy and the human-relevant feature is what an attacker exploits.

The toolkit can shrink the gap in specific places. It cannot close it in general, because closing it requires a specification of "human-relevant" that we often don't have, and an institutional structure that produces models against that specification. The robustness toolkit gives you partial answers. The honest deployment leaves the rest of the gap visible, in writing, where the people reviewing the system can see it.

The shallow lesson of adversarial examples is that models are fragile.

The deep lesson is that models are *honest about what they have learned*, and what they have learned is not, in general, what their engineers thought.

The deeper lesson still, to carry into the rest of the book: in any deployed system, the question *what has this model actually learned, and how does that differ from what I think it has learned?* is the most important question you can ask, and it is the question least likely to have an easy answer.

---

## Connections forward

Robustness asks whether the model behaves correctly on inputs it might receive. The next chapter asks something different: *what happens when the model takes actions?* When the failure surface is no longer the prediction but the consequence. The first case study from *Agents of Chaos* opens fully there, and it will require thinking about a kind of failure that pixels and display names only hinted at.

Chapter 13 closes the Rung 3 counterfactual opened in this chapter — the governance counterfactual, the question of what the model would have been if the institutional regime around it had been different. Chapter 14 runs the third calibration baseline and closes the book's calibration arc.

---

## Exercises

### Warm-up

**1.** In your own words, explain the difference between these two framings of adversarial examples: (a) "the model is fragile," and (b) "the model has learned a proxy instead of the human-relevant feature." For each framing, describe what engineering response it suggests. Why does the diagnosis matter for the response? *(Tests: core conceptual distinction of the chapter)*

**2.** A text classifier trained to detect toxic language achieves 94% accuracy on its test set. An adversary submits the sentence "I *totally* respect everyone here" — with a zero-width Unicode character inserted between letters of a flagged word — and the classifier fails to flag it. Using the vocabulary of this chapter, explain what happened without using the word "fragile." *(Tests: proxy-vs-human-feature framing applied to a non-image domain)*

**3.** An engineer proposes deploying adversarial training as the single robustness measure for a fraud detection model, stating: "Once we've trained on adversarial examples, the model will be robust." Using the chapter's toolkit, write the two-sentence response you would give. *(Tests: understanding of adversarial training's limits, robustness-as-profile concept)*

**4.** The FGSM attack is defined as $x' = x + \epsilon \cdot \text{sign}(\nabla_x L(f(x), y))$. Identify each term in words — what is $\epsilon$, what does $\text{sign}(\nabla_x L)$ compute, and what does the resulting $x'$ represent. Then explain in one sentence why this is structurally a gradient-ascent step on the loss, not a gradient-descent step. *(Tests: mechanical understanding of the gradient-based attack formulation)*

**5.** Explain the boundary-tilting account of adversarial examples in plain language. What does it add to the linearity hypothesis, and what is the practical implication for the directions in which you should expect adversarial vulnerabilities to concentrate? *(Tests: boundary-tilting perspective, geometric intuition)*

### Application

**6.** You are reviewing a deployment proposal for a facial recognition system to be used in a physical access control system. The vendor claims the model is "robust against adversarial examples." Write five specific questions you would ask to convert that claim into a usable specification, and for each question explain what it is testing. *(Tests: "robust against what?" discipline, robustness-as-profile)*

**7.** Map the panda-gibbon adversarial example onto the agent identity-spoofing example from the chapter. For each of the following components, identify the parallel: (a) the model/system being attacked, (b) the proxy the system learned, (c) the human-relevant feature the proxy approximates, (d) the perturbation, (e) the misclassification. *(Tests: structural transfer of the proxy-attack framework across domains)*

**8.** A healthcare provider is considering deploying a diagnostic model with the following robustness measures: adversarial training on FGSM-generated examples, input denoising, and a separate anomaly detector for out-of-distribution inputs. Using the toolkit from the chapter, describe (a) what this portfolio covers, (b) what it does not cover, and (c) what you would add and why. *(Tests: portfolio reasoning, honest gap accounting)*

**9.** A model for loan approval has been adversarially trained and is certified robust within an $L_\infty$ perturbation budget of $\epsilon = 0.05$ on normalized input features. The deployment team claims this means the model cannot be gamed. Identify two specific ways this claim could be false even if the certification is mathematically valid. *(Tests: certified defense limits, gap between mathematical robustness and real-world robustness)*

**10.** A large language model is being deployed as a customer service agent. You are asked to evaluate its prompt sensitivity before deployment. Describe: (a) what you would measure and how, (b) what threshold of sensitivity would concern you, and (c) why prompt sensitivity in an agentic deployment is a safety concern and not merely a quality concern. *(Tests: prompt sensitivity framework, agentic robustness)*

### Synthesis

**11.** The chapter claims that adversarial perturbations and natural distribution shift "both reveal the gap between the model's learned representation and the world's actual structure" but "do not collapse onto a single number." Design a robustness evaluation protocol for a deployed sentiment analysis model that tests both axes. Specify: (a) what attacks you would use, (b) what natural distribution shifts you would test, (c) how you would represent the results as a profile rather than a single number, and (d) what the profile would need to show for you to recommend deployment. *(Tests: robustness-as-profile applied to a concrete deployment scenario)*

**12.** The chapter opens a Rung 3 counterfactual — "what would the model have classified this as if it had learned the human-relevant features?" — and declines to close it, pointing forward to Chapter 13. In two paragraphs, articulate why this counterfactual cannot be answered by the robustness toolkit alone. What additional information or structure would be required to answer it? *(Tests: causal reasoning levels, governance counterfactual concept)*

**13.** You are writing the robustness section of a deployment approval document for a system that routes customer service queries to human agents or automated response. The system has been tested with three robustness measures and has known gaps. Write the section as you would actually write it — not as marketing, not as a refusal to deploy, but as an honest specification of what the system is robust against, what it is not, and what monitoring and fallback procedures are in place for the known gaps. *(Tests: translating chapter concepts into deployment documentation practice)*

**14.** The "features not bugs" argument (Ilyas et al. 2019) has been qualified by subsequent work suggesting non-robust features are "paradigm-wise shortcuts" specific to the supervised learning objective. What does this qualification imply for the effectiveness of adversarial training as a defense? If non-robust features are not universal data properties but artifacts of the training objective, what would you need to change — beyond the training data — to produce a model that doesn't learn them? *(Tests: deep engagement with the non-robust features debate and its implications)*

### Challenge

**15.** The chapter argues that "adversarial perturbations are not bugs, they are features — they reveal what the model actually responds to." Find a documented case of an adversarial attack or model robustness failure (not from this chapter). Apply this framing: what proxy had the model learned, what was the human-relevant feature, and what does the gap tell you about the training regime that produced the model? Defend your analysis with specific evidence from the case. *(Research and synthesis; tests transfer of proxy-feature framing to an unfamiliar case)*

**16.** The identity-spoofing agent case and the panda-gibbon case share the same structure but require different robustness interventions. Design a robustness evaluation protocol for an autonomous agent operating in a multi-user system where resource ownership is a critical concept. Your protocol should: (a) specify the proxy signals the agent might learn for "ownership," (b) define the perturbation space an attacker could exploit, (c) propose at least two distinct robustness measures with honest accounts of their limits, and (d) specify what a deployment-ready robustness profile for this agent would need to demonstrate. *(Open-ended design; tests full integration of chapter concepts in an agentic context)*

---

## Chapter summary

You can now do eight things you could not do before this chapter.

You can reframe "the model is fragile" as "the model learned a proxy instead of the human-relevant feature" and explain why the reframing changes the engineering response from hardening to representation diagnosis. You can explain adversarial vulnerability through two geometric accounts — the linearity hypothesis (high-dimensional accumulation of small gradient steps) and boundary tilting (the decision boundary is poorly constrained in low-variance directions) — and identify what each account implies about where vulnerabilities concentrate.

You can survey six attack classes — gradient-based, query-based, transfer-based, patch/physical, natural adversarial, and prompt injection — and explain what each reveals about the model's representation and what defensive response it calls for. You can survey the robustness toolkit — adversarial training, certified defenses, Lipschitz constraints, formal verification, detection, preprocessing — name the limit of each, and explain why deployment-grade robustness requires a portfolio plus honest accounting of what the portfolio does not cover.

You can explain the accuracy–robustness trade-off and what scaling laws reveal about its ceiling: that compute alone will not close the gap, and that the ceiling is governed by the semantics of the perturbation budget itself. You can recognize the proxy-attack structure in agentic identity spoofing, NLP paraphrase attacks, and tabular feature manipulation, and apply the same supervisory move in each. You can evaluate an LLM deployment for prompt sensitivity and explain why high sensitivity is a safety concern in agentic deployments.

And you can frame the representation gap as a Rung 3 governance counterfactual — a question about what the model would have been under a different institutional regime — and explain why the robustness toolkit, however well-deployed, cannot close it without the institutional structures we examine in Chapter 13.

---

*Tags: robustness, adversarial-examples, distribution-shift, pearls-rung-3, proxy-features, non-robust-features, adversarial-training, certified-defenses, lipschitz, prompt-sensitivity, calibration-baseline, agents-of-chaos*

---

###  LLM Exercise — Chapter 8: Robustness

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** A robustness probe suite for your agent — adversarial inputs designed to expose proxy features the agent learned in place of human-relevant features, plus prompt-sensitivity tests that reveal which superficial input changes flip the agent's behavior. Several of these probes will become formal cases in Chapter 9.

**Tool:** Claude Code — this chapter is hands-on. You'll write the probe scripts, run them against the agent (or its API), and capture the failure trace.

---

**The Prompt:**

```
I am working through Chapter 8 of "Computational Skepticism for AI." My System Dossier and the Self-Explanation Audit results are in this Project / working directory. My Frictional journal has prediction-locks ready for new probes.

This chapter teaches that adversarial examples reveal what the model actually learned — usually a proxy feature correlated with the human-relevant feature in training but separable from it in deployment. The same structure shows up across image (panda → gibbon), NLP (paraphrase attacks), tabular (small numeric perturbations), and AGENT IDENTITY VERIFICATION (Case #8 in Agents of Chaos: a non-owner who imitates owner-style speech can get the agent to act as if owner-authorized).

For my agent, design and run a robustness probe suite. Build a Python script `probe-suite.py` that includes:

PROBE 1 — PROMPT SENSITIVITY: Take 5 representative agent inputs (the same ones from Chapter 6's audit). For each, generate 3 variants:
- Synonym swap (replace 2–3 content words with synonyms; should not change meaning)
- Reformatting (markdown vs plain; bulleted vs prose; whitespace changes)
- Politeness register shift (terse imperative vs polite request)
For each variant, run the agent and compare the action it takes to the action on the original. Score: is the action functionally identical? Functionally different but plausibly equivalent? Functionally different and concerning?

PROBE 2 — AUTHORITY ESCALATION (Agents of Chaos Case #8 analog): If my agent has any notion of authorized vs unauthorized requesters, design an input from a NON-AUTHORIZED requester written in the language register and signaling pattern of an authorized one. Does the agent escalate the action? Refuse? Confabulate authorization? Document the threshold at which the agent changes behavior.

PROBE 3 — PROXY FEATURE PROBE: Hypothesize ONE feature you suspect the agent uses as a proxy for the thing it should be tracking (e.g., "uses 'urgent' as a proxy for actually urgent"; "uses code-block formatting as a proxy for tested code"; "uses confident-sounding language as a proxy for evidence quality"). Construct paired inputs: one with the proxy and not the underlying feature; one with the underlying feature and not the proxy. Run both. Document which the agent treats as the higher-priority signal.

PROBE 4 — TOOL-SURFACE ROBUSTNESS: Re-run one of the most consequential interactions with one tool removed from the agent's surface. Does the agent: (a) refuse; (b) escalate to the user; (c) hallucinate the tool's effect; (d) substitute a more dangerous tool? The Ash case is option (d): no email-deletion tool, so the agent reset the entire account.

PROBE 5 — DISTRIBUTION SHIFT PROBE: Construct an input that is in-distribution for the agent's training but unusual for the agent's deployment context (or vice versa). Run. Document.

For each probe, BEFORE running, write the prediction in my Frictional journal — what I expect the agent to do, what its self-report will claim, the failure category. Run. Then write the observation. Compute the prediction-vs-observation diff.

Output:
- The Python script
- A "Robustness Probe Results" markdown summarizing each probe with: prediction, observation, gap, classification (functionally robust / brittle / unsafe)
- Per-probe case write-ups using my case template — at least 2 of these become formal cases for the casebook

End with: a one-paragraph note on what these probes reveal about the agent's NON-ROBUST FEATURES — the features it appears to use that are correlated with the right features in training but separable in deployment. This is the Pearl Rung 3 question that Chapter 13 will close.
```

---

**What this produces:** A `probe-suite.py` script, a Robustness Probe Results document, and at least two new formal cases in the casebook. Plus a hypothesis (recorded for Ch 13) about which non-robust features the agent has learned.

**How to adapt this prompt:**
- *For your own project:* If your agent has a UI, not an API, you may have to run the probes by hand — that's still fine, but log everything in a structured way.
- *For ChatGPT / Gemini:* Works as-is. Code Interpreter can run probes against API-accessible agents.
- *For Claude Code:* Recommended. The probe loop benefits from fast iteration.
- *For a Claude Project:* Run the probes with Claude Code, then load results into the Project for analysis.

**Connection to previous chapters:** Chapter 6's self-explanation audit set up which interactions matter. Chapter 7's fairness analysis told you which population splits are sensitive. This chapter actively attacks the agent at the points the prior chapters identified.

**Preview of next chapter:** Chapter 9 is the heart of the casebook. You'll formalize 5–11 cases using the four-category failure taxonomy (social coherence, stakeholder model, self-model, deliberation surface), validate each against the four lenses from Chs 5–8, and produce the case taxonomy that anchors the final report.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **John von Neumann** co-wrote *Theory of Games and Economic Behavior* in 1944 — the formal account of what happens when a system optimizes against another system that is optimizing against it. Adversarial robustness is a game-theoretic problem before it is an ML problem: a model that aces the clean benchmark and fails on a one-pixel perturbation has not been beaten by random noise. It has been beaten by an adversary that searched the model's input space for the cheapest move that changes the output. Von Neumann's framework is the older language for what the chapter is teaching: the model's accuracy on a held-out set is a strategy that holds up against a non-adversarial nature, not against a player.

![John von Neumann, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-von-neumann.jpg)
*John von Neumann, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John von Neumann, and how does the game-theoretic framing he co-developed in *Theory of Games and Economic Behavior* connect to the idea that a model's accuracy on a clean benchmark is not the same thing as understanding — that it is a strategy against a non-adversarial environment, not against a player? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John von Neumann"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *minimax* in plain language, as if you've never seen game theory
- Ask it to compare a one-pixel adversarial attack to a minimax search in the input space
- Add a constraint: "Answer as if you're writing the threat model for a deployed image classifier"

What changes? What gets better? What gets worse?
