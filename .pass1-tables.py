#!/usr/bin/env python3
"""Pass 1 — render all 53 TABLE comments in computational-skepticism-for-ai/chapters/*.md
to populated markdown tables. Many comments include row data inline; others are
templates where students fill cells. Both forms are rendered in spec-compliant style.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# Each entry keys on a unique substring of the comment.
TABLES = {}

# === Ch 02 ===

TABLES["Three-column reference table — Axiom"] = """| Axiom | Formal Statement | Plain English Meaning |
|---|---|---|
| **Nonnegativity** | $P(A) \\geq 0$ | Probabilities are never negative. |
| **Normalization** | $P(\\Omega) = 1$ | Something must happen — the total is always 1. |
| **Additivity** | $P(A \\cup B) = P(A) + P(B)$ for disjoint $A, B$ | Probabilities of mutually exclusive outcomes add directly. |

*Every probability calculation in this book is a consequence of these three rules.*"""

TABLES["Three-column comparison table — Interpretation"] = """| Interpretation | Best suited for | Key limitation |
|---|---|---|
| **Classical** | Equally-likely discrete outcomes (dice, cards, fair coins) | Requires symmetry; fails when outcomes aren't equally likely |
| **Frequentist** | Stable repeatable processes, A/B tests, quality control | Cannot assign probability to one-off events or unknown priors |
| **Bayesian** | One-off decisions, belief updating, AI deployment inference | Requires specifying a prior; result depends on that choice |"""

TABLES["Four-row reference table — Term"] = """| Term | Plain English Name | Value in the Disease Example | Role in the Formula |
|---|---|---|---|
| $P(\\text{positive} \\mid \\text{disease})$ | Sensitivity / true positive rate | 0.99 | Numerator factor: how strongly the evidence supports the hypothesis |
| $P(\\text{disease})$ | Base rate / prior | 0.0001 | Numerator factor: what we believed before seeing the evidence |
| $P(\\text{disease} \\mid \\text{positive})$ | Posterior | ≈ 0.0099 | What we actually want — belief after the evidence |
| $P(\\text{positive})$ | Total positive rate | ≈ 0.0101 | Denominator: normalizes so probabilities sum to 1 |

*The prior sits in the numerator with the same weight as the test's sensitivity. Drop it and you have thrown away half the equation.*"""

TABLES["Side-by-side comparison table for the factory example"] = """| Machine | Share of total output | Defect rate | Share of defectives (posterior) |
|---|---|---|---|
| **Machine A** | 40% | 2% | 25% |
| **Machine B** | 30% | 3% | 28% |
| **Machine C** | 30% | 5% | 47% |

*The machine that produces the most defectives is not the largest machine — it's the one with the highest defect rate. Bayes makes this visible.*"""

TABLES["Five-row deployment mapping — Domain"] = """| Domain | What is rare | Typical base rate | Consequence of ignoring the prior |
|---|---|---|---|
| **Fraud detection** | Fraudulent transactions | ~0.1–1% | Analyst alert fatigue; real fraud ignored |
| **Security monitoring** | Malicious logins | ~0.01–0.1% | Teams disable or ignore automated alerts |
| **Medical screening** | Target disease (rare condition) | ~0.01–1% | Unnecessary downstream procedures, patient harm |
| **Content moderation** | Genuinely harmful posts | ~0.01–0.1% | Moderation teams overwhelmed with false positives |
| **AI jailbreak detection** | Adversarial inputs | ~0.001–0.01% | High false-positive load undermines trust in the detector |

*The structure is the same in every row. The math does not care about the domain.*"""

# === Ch 03 ===

# Bias-type interaction matrix (10x10) — render as a compact key, since a 10x10 matrix is too wide.
TABLES["Bias type interaction matrix"] = """| Bias pair | Interaction | Mechanism |
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

*If one bias type is confirmed in your pipeline, check the row pairs marked* amplifying *first.*"""

TABLES["Fairness impossibility"] = """| Fairness criterion | Formal definition | What it requires |
|---|---|---|
| **Calibration parity** | $P(Y=1 \\mid \\hat{Y}=s, A=a)$ equal across groups $a$ at every score $s$ | A score of 0.7 means the same thing for every group |
| **Equal FPR** | $P(\\hat{Y}=1 \\mid Y=0, A=a)$ equal across groups | The cost of being wrongly flagged is shared equally |
| **Equal FNR** | $P(\\hat{Y}=0 \\mid Y=1, A=a)$ equal across groups | The cost of being missed is shared equally |
| **All three simultaneously** | All of the above hold jointly | *Only achievable when base rates are equal across groups.* |

*Pick the audit criterion that fits the harm structure of the deployment. The impossibility theorem rules out picking all three.*"""

TABLES["Rung 1 vs Rung 2 — same fairness claim at two rungs"] = """| Fairness question | Rung 1 formulation (observational) | Rung 2 formulation (interventional) |
|---|---|---|
| **Loan denial by race** | Is the denial rate equal across racial groups in the data? | If we *intervened* to change race while holding all other features fixed, would the denial rate change? |
| **Model error rates by group** | Are FPR and FNR equal across groups in the test set? | If we changed group membership while holding the underlying outcome fixed, would the error rate change? |
| **Recidivism risk score** | Are score distributions equal across groups, conditional on outcome? | If we intervened on the protected attribute, would the score for the same individual change? |
| **Hiring outcome** | Is the hire rate proportional across applicant groups? | If two applicants were identical except for the protected attribute, would the hiring decision differ? |

*Equal Rung 1 metrics do not certify causal fairness. A Rung 1 disparity does not always mean causal discrimination. The two rungs answer different questions.*"""

# === Ch 04 ===

TABLES['Three-column comparison. Columns: "Retrospective journal"'] = """| Diagnostic dimension | Retrospective journal | Performative journal | Authentic journal |
|---|---|---|---|
| **Surface appearance** | Smooth, polished, written from a settled vantage | Visibly performs reflection — emotional adjectives, hedge phrases | Uneven; stops, starts, revises in place |
| **Timestamp pattern** | Single submission near deadline | Tightly clustered just before submission | Distributed across the work session — entries before, during, after |
| **Prediction quality** | Predictions match outcomes too well to be plausible | Predictions are vague and unfalsifiable | Predictions are sharp and sometimes wrong |
| **Gap analysis specificity** | Generic ("I learned to think more carefully") | Generic but emotional ("I struggled, then grew") | Specific to a sentence the student misjudged and now can name precisely |
| **Diagnostic tell for the grader** | No revision marks; impossible to mistake for in-flight thinking | Disclosure language without disclosure content | Real prediction errors visible on the page |"""

TABLES["Seven components reference card"] = """| Component | Abbr. | Neurobiological basis | Operational formula | Genuine learning signature | Borrowed-certainty signature | Primary data source | Frictional journal move that captures it |
|---|---|---|---|---|---|---|---|
| **Engagement** | E | Dopaminergic reward, novelty response | Time-on-task × difficulty match | Sustained attention with productive struggle | Drift to easier substitute task | Session timestamps + difficulty self-report | "Where did I get stuck and why?" |
| **Curiosity** | C | Information-gap activation | Questions generated per concept introduced | Original questions tied to the specific text | Generic questions copied from the prompt | Question log | "What did I want to know that the source didn't say?" |
| **Prediction** | P | Cerebellar / cortical predictive coding | Predictions made before observation | Concrete forecast with stakes named | Vague forecast or post-hoc claim | Pre-observation entries | "Before running it, I expected X because…" |
| **Error correction** | EC | Anterior cingulate, error monitoring | Predictions revised after disconfirmation | Specific gap named, revision recorded | Generic regret without revision | Diff between pre- and post-observation entries | "I was wrong because I assumed…; now I see…" |
| **Practice** | Pr | Striatal procedural learning | Repetitions of a constrained drill | Same move tried 3+ times with variation | Single attempt, generic reflection | Practice log | "Reps of this move so far:…" |
| **Encoding** | En | Hippocampal consolidation | Independent restatement after a delay | Restated in own words days later, accurate | Restated immediately by paraphrase | Spaced-restatement entries | "A week later: here is what I retained without looking…" |
| **Transfer** | T | Cross-domain pattern abstraction | Application of the concept to a fresh domain | Concrete second-domain example, working out details | Abstract claim that the concept "applies broadly" | Transfer-attempt entries | "I tried this on [unrelated problem] and here is what happened…" |"""

# === Ch 05 ===

TABLES["Five-column reference table — Data Type"] = """| Data Type | Examples | Natural Summary Statistics | Visualization Default | Key Questions to Ask |
|---|---|---|---|---|
| **Continuous numeric** | salary, temperature, model confidence score | mean, median, std, min/max, percentiles | histogram (30 bins), box plot | Is the distribution skewed? Are there outliers? Does the range make physical sense? |
| **Discrete numeric** | number of visits, floor count | frequency table, mode | bar chart (treat as categorical if range < ~20 distinct values) | Are there impossible values? Gaps in the range? |
| **Categorical nominal** | city, product category, blood type | frequency, mode, entropy | bar chart sorted by frequency descending | Rare categories? Misspellings suggesting dirty data? Unexpected values? |
| **Categorical ordinal** | survey rating, education level, income bracket | frequency, mode | bar chart sorted by natural order | Is ordering preserved in the encoding? Are any levels absent? |
| **Temporal** | date, timestamp | min, max, range, count-by-period | line chart (record count over time) | Gaps in coverage? Seasonality? Sudden distribution changes? |

*Before drawing a single plot, classify every column. The correct visualization depends entirely on the data type — and the most dangerous classification error is treating a categorical column as numeric.*"""

TABLES["Six-row reference table — Failure Mode"] = """| Failure Mode | What it is | Why procedural EDA misses it | Example deployment consequence |
|---|---|---|---|
| **Sampling assumption** | Training data drawn from a more accessible subpopulation than the deployment target | EDA only sees what is present; it cannot compare the present data to the absent target population | Model performs well on easy-to-reach customers, degrades on the long tail it was never trained on |
| **Time-window assumption** | Training data covers a historical period that no longer reflects the deployment environment | EDA tools have no knowledge of what was true outside the dataset's time range | Model trained on 2019 data, deployed in 2022, confidently predicts patterns that have shifted |
| **Label assumption** | The label column measures an operational proxy, not the underlying construct of interest | EDA can show a label's distribution but cannot show the gap between the label and the construct | Re-arrest rate predicts re-arrest, not crime; click-through rate predicts clicks, not interest |
| **Missing not at random (MNAR)** | Values are missing because of the value itself | The missingness and the data appear independent from within the dataset; the pattern only becomes visible by reasoning about why someone would not report | Income missingness concentrated in high earners; survival data missing the patients who died; both produce biased models |
| **Feature-engineering assumption** | An input column is a calculated composite from an upstream model or analyst, not raw measurement | The column looks like data and has no missing values; its provenance is invisible unless documented | `customer_lifetime_value` encodes someone's old model's assumptions; when those assumptions break, so does the new model trained on them |
| **Access/boundary assumption** | The effective data universe extends beyond the schema — through references, links, or embedded content | EDA validates the records that are present; it cannot follow references to data outside the schema | An agent given access to an email corpus implicitly has access to everything the emails reference or quote |

*The six failures. Each has a structural reason it evades EDA. Memorizing the list matters less than being able to ask, for each column: why is this value here, and what is it not telling me?*"""

TABLES["Three-column delegation decision table — Category"] = """| Category | What belongs here | Why |
|---|---|---|
| **Delegate freely** | Shape/dtype inspection, summary statistics (`.describe()`), missingness counts and matrix, univariate histograms and bar charts, outlier flagging via IQR or z-score, correlation heatmap, pair plots, temporal record counts | Well-defined operations; output is determinate; AI errors are immediately visible when you look at the result |
| **Verify before trusting** | Interpretation of why a value is missing, claim that a distribution is "normal for this domain," narrative explanation of a detected anomaly, suggested imputation strategy | Requires domain knowledge the AI does not have; errors are not obviously visible in the output — they sound plausible |
| **Do not delegate** | Epistemic-frame reconstruction (steps 1 and 3–6), prediction-lock and gap analysis, access-boundary scoping, row-tracing to source systems | The output of these steps is your engagement with the data, not the document it produces. A fluent AI-generated epistemic frame contains no information, because the AI started from the same documentation you did |

*The line is not about AI capability — it is about what the work produces. Mechanical outputs have determinate right answers the AI can reach. The interrogation produces understanding that only comes from you confronting the data yourself.*"""

# === Ch 06 ===

TABLES["SHAP capability matrix"] = """| Question SHAP is asked | SHAP can answer? | Pearl rung | What you'd need instead |
|---|---|---|---|
| Additive feature contribution to *this prediction* | **Yes** | Rung 1 (observational) | — |
| Causal relationship between feature and outcome | No | Rung 2 (interventional) | Causal model + intervention experiment |
| Whether the model is correct on *this case* | No | Out of frame | Ground truth + chart review |
| What would happen if feature $X$ changed | No (despite appearance) | Rung 2 | Counterfactual simulator that refits or reasons over the joint distribution |
| Whether the feature is a confounder vs. a cause | No | Rung 2/3 | Causal-discovery / structural model |"""

TABLES["The four axioms side-by-side"] = """| Axiom | Formal statement (abbreviated) | What it guarantees | What it does NOT guarantee | Failure mode if violated |
|---|---|---|---|---|
| **Efficiency** | $\\sum_i \\phi_i = f(x) - E[f(X)]$ | Attributions add up to the prediction's deviation from the baseline. *(The force-plot visualization is Efficiency rendered visually.)* | That any individual attribution is causal | Attributions don't sum to the prediction; the visualization is meaningless |
| **Symmetry** | If two features are identical to the model, they get equal attribution | Two interchangeable features cannot be assigned different importance | That the underlying causal roles of the two features are equivalent | One of two identical features gets blamed; the other vanishes from the report |
| **Dummy** | A feature the model does not use gets zero attribution | A feature truly unused gets credit zero. *(A non-zero zip-code attribution does not violate Dummy — it means the model uses zip code.)* | That every non-zero attribution corresponds to a feature the practitioner intended the model to use | An unused feature is reported as important; the audit is misled |
| **Linearity** | Attributions for $f + g$ equal the sum of attributions for $f$ and $g$ | Compositional consistency across model ensembles | That stacking two models produces an additive explanation of their behavior | Attributions for a stacked model can't be decomposed cleanly; ensemble outputs aren't auditable |"""

TABLES["Comparison of the three estimation approaches"] = """| Method | Computational complexity | Exact vs. approximate | Feature dependency handling | Best use case |
|---|---|---|---|---|
| **Exact Shapley** | Exponential in $M$ | Exact | Marginal distribution | Tiny feature sets only — research demonstrations |
| **KernelSHAP** | Linear in $M$ (with sampling) | Approximate | Marginal distribution | Any model — model-agnostic baseline |
| **Permutation Method** | Linear in $M$ | Approximate | Marginal distribution | Any model — better variance than KernelSHAP at the same cost |
| **TreeSHAP** | Polynomial in tree structure | Exact | Two variants (path-dependent / interventional) | Tree-based models (XGBoost, random forests, LightGBM) |"""

TABLES["Three explanation families compared"] = """| Family | Example output | Pearl rung | What it tells you | What it doesn't tell you | Primary failure mode |
|---|---|---|---|---|---|
| **SHAP / Shapley** | "Income contributed +0.18 to this prediction" | Rung 1 | The additive contribution to *this* prediction, given the model | The causal effect of income on the outcome | Misread as causal — a Rung 1 attribution treated as a Rung 2 claim |
| **LIME** | A small linear surrogate that approximates the model around this input | Rung 1 | A locally linear summary of model behavior in a neighborhood | The model's actual computation; nonlinearity outside the neighborhood | Fragile to choice of neighborhood and perturbation strategy |
| **Counterfactual** | "If income were $5,000 higher, the prediction would flip to approve" | Rung 2 | What the *model* would predict under an intervention on its inputs | What the *world* would do under that intervention; whether the intervention is feasible | Treated as a causal statement about reality rather than the model |"""

TABLES["Transparency, explainability, and interpretability compared"] = """| Term | A property of… | Binary or graded | Can exist without the others | What it doesn't guarantee |
|---|---|---|---|---|
| **Transparency** | The system as code/architecture | Binary in principle, graded in practice | Yes — open weights without explanation tooling | That any human can act on what they read |
| **Explainability** | An output, given a method | Graded | Yes — closed model with post-hoc explanations | That the explanation describes the actual computation |
| **Interpretability** | A model whose decisions humans can directly follow | Graded | Yes — a clearly interpretable model with no public weights | That the interpretation is correct in deployment |
| **Common failure mode** | A system that is transparent, explainable, and interpretable to the *developer* — and none of those things to the patient or loan applicant reading the output | — | — | — |"""

# === Ch 07 ===

TABLES["Three-column definition reference table — columns: metric name"] = """| Metric (alias) | What it measures | What it is a statement about | Values claim embedded |
|---|---|---|---|
| **Calibration / Predictive parity** | Whether a score $s$ corresponds to the same probability of a positive outcome across groups | The model's *probability honesty* — its outputs as probabilities | If you act on the score, the meaning of the score should not depend on group membership |
| **Equalized odds (TPR / FPR parity)** | Whether the false-positive and true-positive rates are equal across groups | The model's *errors* — costs distributed across groups | Costs of errors should be borne equally; group membership should not change risk of being wronged |
| **Demographic parity (statistical parity)** | Whether the rate of positive predictions is equal across groups | The model's *outputs* — visible decisions | Outcomes should be proportional regardless of underlying base rates; structural redress over conditional accuracy |"""

TABLES["Worked arithmetic table with base rates 0.6 / 0.3"] = """**Calibration-satisfying version (equalized-odds violation visible)**

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

*Same model, different threshold choices. Calibration parity and equalized odds cannot both hold while base rates differ.*"""

TABLES["COMPAS case mapped to the three metrics"] = """| Metric | What ProPublica measured | What Northpointe measured | Was the claim factually accurate? | Values claim each side embeds |
|---|---|---|---|---|
| **Equalized odds (TPR / FPR)** | Black defendants had ~2× the FPR of white defendants — the rate at which non-recidivists were labeled high-risk | (Not the metric Northpointe reported on) | **Yes** — the FPR disparity was real | Costs of being wrongly flagged should be borne equally |
| **Calibration / predictive parity** | (Not their primary metric) | At every score, the same fraction of Black and white defendants reoffended | **Yes** — the score had the same meaning across groups | Acting on the score should not require group-specific reinterpretation |
| **Demographic parity** | (Not directly measured) | (Not directly measured) | — | — |

*Both sides were right about the numbers. The disagreement was about which numbers should matter.*"""

TABLES["Three-family toolkit comparison"] = """| Family | Mechanism | Typical target metric | Key advantage | Key limitation |
|---|---|---|---|---|
| **Pre-processing** | Reweight, resample, or transform the training data before training | Demographic parity, base-rate equalization | Model-agnostic; intervention is upstream of model choice | Cannot reach what is measured but mis-recorded; relies on group labels at training time |
| **In-processing** | Add fairness as a constraint or regularizer in the training objective | Equalized odds, calibration | Fairness becomes part of the model's learned representation | Requires modifying training infrastructure; tradeoff with accuracy is locked in at train time |
| **Post-processing** | Adjust thresholds, scores, or decision rules after training | Group-specific TPR/FPR targets | Can be applied to a frozen model; transparent | Requires group labels at deployment; per-group thresholds invite separate-treatment objections |

*What none of them do: resolve the impossibility theorem, or reach upstream structural bias in the data-generating process.*"""

# === Ch 08 ===

TABLES["Six-row taxonomy table — Attack Class"] = """| Attack Class | What it requires from the attacker | What it exploits in the model | Domains where it applies | Key defensive response |
|---|---|---|---|---|
| **Gradient-based (white-box)** | Full access to model weights and gradients | The specific geometry of this model's loss surface | Image, audio, any differentiable model | Adversarial training, input certification |
| **Query-based (black-box)** | Access to model outputs only; no weights visible | Approximate gradient estimation from output probing | API-deployed models, LLMs | Output monitoring, query rate limiting |
| **Transfer-based** | A surrogate model; no access to the target | Shared proxy feature manifolds across models trained on similar data | Hidden architectures, proprietary models | Representation diversity, ensemble defenses |
| **Patch / physical** | Ability to modify input in the physical world (sticker, glasses, printed pattern) | Spatial localization — high-magnitude perturbation in a small region | Autonomous vehicles, facial recognition, physical access control | Spatial input validation, environment monitoring |
| **Natural adversarial** | No modification — naturally occurring long-tail inputs | Model's failure to generalize beyond the training manifold | Real-world safety benchmarks, OOD monitoring | Distribution-shift monitoring, holdout on tail populations |
| **Prompt injection (agentic)** | Ability to insert adversarial text into a processing pipeline | Conflation of instructions and data in the same input stream | LLMs, agentic pipelines with tool access | Instruction-data separation, output sandboxing |

*The taxonomy matters because each class reveals a different gap. The correct defensive response depends on which attack is present in your threat model — not on which attack appears most in the research literature.*"""

TABLES["Six-row toolkit reference table — Tool"] = """| Tool | What it does | Key cost | What it cannot do |
|---|---|---|---|
| **Adversarial training (PGD-AT)** | Incorporates adversarially perturbed inputs into the training loop, flattening the loss surface | Clean accuracy drops; ≈9× more expensive than standard training; robustness transfers imperfectly to other attack types | Does not change the model's representation — moves the attack surface without closing the proxy gap |
| **Certified defenses (randomized smoothing)** | Transforms a base classifier into a smoothed classifier with provable stability within radius $R$ | Requires thousands of Monte Carlo samples per prediction; high $\\sigma$ degrades clean accuracy; certified radius shrinks in high dimensions | Cannot certify against attacks outside the radius; prohibitively slow for real-time use |
| **Lipschitz-constrained architectures** | Enforces a bounded rate of output change per unit input change; "verifiable by design" | Currently lower clean accuracy than unconstrained baselines; requires removing LayerNorm and modifying attention | Does not specify which inputs are sensitive — only bounds maximum sensitivity everywhere |
| **Formal verification (α,β-CROWN)** | Proves mathematically that a property holds for all inputs in a defined region | Scales only to narrow properties on models up to millions of parameters; does not scale to frontier models or open-ended properties | Cannot verify natural-language properties; cannot scale to the models most practitioners actually deploy |
| **Detection-based defenses** | Identifies adversarial inputs as outliers and routes to fallback or human review | Adaptive attacks can target detector and classifier simultaneously (BPDA / obfuscated gradients); adds latency | Does not improve the model's representation — routes failures, does not eliminate them |
| **Input preprocessing** | Removes perturbation signal before it reaches the model (denoising, quantization, smoothing) | Adaptive attackers aware of preprocessing can optimize perturbations that survive it; blunts but rarely eliminates exposure | Fails against attackers with knowledge of preprocessing; does not address transfer attacks or prompt injection |

*There is no single tool. Every entry has a bounded scope and an honest cost. Deployment-grade robustness comes from layering these tools and documenting what each layer does not cover.*"""

TABLES["Cross-domain transfer reference"] = """| Domain | What the model learns as proxy | The human-relevant feature it approximates | Primary attack vector | Robustness measure |
|---|---|---|---|---|
| **Image classification** | High-frequency pixel statistics co-occurring with the class label | Object shape and structural semantics | Gradient-based $L_\\infty$ perturbation | Adversarial training, input certification |
| **NLP / LLM** | Surface-level token co-occurrence and syntactic patterns | Semantic meaning and communicative intent | Paraphrase attacks, Unicode insertion, prompt injection | Semantic invariance testing, instruction-data separation |
| **Tabular (credit / fraud)** | Mutable feature combinations that correlate with outcome on training data | Fundamental creditworthiness or fraud risk | Strategic feature manipulation within feasibility constraints | Domain-constrained adversarial evaluation, feature-immutability audits |
| **Agentic systems** | Conversational and display-layer identity signals (display name, tone, phrasing) | Verified social-legal ownership and authorization | Proxy spoofing via crafted messages in the agent's information stream | Cryptographic credentials, output sandboxing, adversarial prompting |

*Same structure, different surface. In every domain: a learnable proxy, an attackable proxy, a human-relevant feature left untouched. The appropriate defense differs by domain; the diagnostic question is always the same.*"""

TABLES["Robustness disclosure template"] = """**Section 1 — Robustness profile**

| Attack class tested | Perturbation budget used | Clean accuracy | Robust accuracy at budget | Notes |
|---|---|---|---|---|
| Gradient-based ($L_\\infty$) | $\\epsilon = 8/255$ | _____ % | _____ % | _____ |
| Query-based | _____ queries | _____ % | _____ % | _____ |
| Natural adversarial (OOD) | benchmark name | _____ % | _____ % | _____ |

**Section 2 — Untested attack classes**

| Attack class | Why it is not in the threat model | What would change that |
|---|---|---|
| _____ | _____ | _____ |

**Section 3 — Operational consequences**

| Failure mode | Detection mechanism | Escalation path |
|---|---|---|
| _____ | _____ | _____ |

*The disclosure is the contract. A team that cannot fill in this template has not yet specified what robustness it is claiming.*"""

# === Ch 09 ===

TABLES["Effective data scope audit template"] = """| Data source | Documented access scope | Effective access scope (what can be extracted indirectly) | Disclosure conditions (which requests trigger disclosure) | Authorization check present? |
|---|---|---|---|---|
| **Email** | Inbox + sent folder for the agent's account | Anything quoted in any email; any address mentioned; any attachment referenced; the social graph implied by recipients | Direct read; quoted content in a reply; meta-questions about senders or topics | ☐ Yes ☐ No |
| **File system** | Project directory | Anything linked from a project file; anything referenced by path string in a doc; entire user home if a parent reference exists | Direct read; reference resolution; symlink traversal | ☐ Yes ☐ No |
| **Calendar** | Event list for the agent's account | Attendee names; meeting titles that quote private context; recurring-event metadata | Direct read; summary requests; participant queries | ☐ Yes ☐ No |
| **CRM / ticketing** | Records visible to the agent's role | Records linked to from those records; cross-tenant data if the schema joins | Direct read; relationship traversal; aggregation queries | ☐ Yes ☐ No |
| **Web fetch** | URLs explicitly allowed | Anything reachable from those URLs by hyperlink; redirects out of the allowlist | Each fetch + each followed link | ☐ Yes ☐ No |

*Filled before deployment, this template would have caught Cases #2 and #3 — the "documented" scope was a small fraction of the effective scope.*"""

TABLES["Fundamental vs. contingent failures"] = """| Failure type | Cases | Engineering alone can address it? |
|---|---|---|
| **Missing tool** | Case #1 (email deletion mid-task) | Yes — *contingent*. Add the tool; the failure goes away |
| **Prompt injection via external files** | Cases #8, #10 | No — *fundamental*. The architecture cannot reliably distinguish instructions from data when both arrive in the same input stream |
| **Observability modeling** | Case #1 (public posting) | No — *fundamental*. The agent needs an audience-boundary representation it does not currently have |
| **Resource constraint awareness** | Cases #4, #5 | Yes (with the right guardrails) — *contingent*. Budget caps and rate limits work when explicitly wired in |
| **Autonomy-competence gap** | Cases #1, #4, #5 | No — *fundamental*. May require architectural change; better prompting does not close it |

*Use this routing before proposing a fix. A patch on a fundamental failure ships the failure mode in a slightly different form.*"""

TABLES["Responsibility mapping template"] = """| Actor | What they can control | Failure modes within their responsibility | Failure modes outside their control | Monitoring they are responsible for |
|---|---|---|---|---|
| **Owner (deploying user)** | The deployment configuration, the supervisory checks, the escalation rules | Misuse, missing oversight, ignoring escalation signals | Model-provider regressions, framework defaults | Daily review of agent actions, weekly outcome audit |
| **Non-owner (third-party user)** | The instructions issued, the data shared with the agent | Instruction-induced misuse | Owner's failure to constrain | Their own session activity log |
| **Model provider** | Model weights, system-level guardrails, capability claims | Refusal to acknowledge known failure modes; capability over-promise | Owner's deployment configuration | Public capability bulletin, regression disclosure |
| **Framework developer** | Tooling defaults, sandbox boundaries, observability hooks | Insecure defaults, missing audit primitives | Specific deployments built on the framework | Security advisories, default-config audits |
| **Deploying organization** | Procurement, governance, training, post-incident review | Selecting a deployment without an audit; failing to investigate incidents | Individual user error within a properly designed deployment | Incident-response process, accountability map |

*Filled before deployment, this template is the responsibility documentation a regulator or post-incident review would expect.*"""

TABLES["Five Supervisory Capacities mapped to the eleven cases"] = """| Capacity | Definition | Cases where its failure is the primary mechanism | Question the capacity asks | What the audit trail should show |
|---|---|---|---|---|
| **Plausibility Auditing** | Checking whether a fluent, structurally valid output corresponds to the world it represents | Case #1 (reported state vs. actual state divergence), Case #6 | "Does the agent's completion report match independent world-state observation?" | An independent state check log entry after each irreversible action |
| **Problem Formulation** | Specifying *what the right task is* before delegating it | Cases #2, #3 (effective scope larger than documented scope) | "Did we specify the constraints that the deployment context actually imposes?" | A pre-deployment scoping document; a deviation log when reality exceeds the scope |
| **Tool Orchestration** | Selecting and sequencing the right tools for the right step | Cases #4, #5 (resource exhaustion through poor tool choice) | "Are the tools available, the tools used, and the tools forbidden each documented and bounded?" | A per-action tool log with rate limits and budget caps visible |
| **Interpretive Judgment** | Applying domain knowledge to evaluate ambiguous outputs | Cases #7, #9 (output plausible but wrong in this domain) | "Is this output correct given what only the practitioner knows about this case?" | A reviewer note on each high-stakes output, with disposition reasoning |
| **Executive Integration** | Tying all four capacities together in the moment of decision | Cases #8, #10, #11 (composite failures spanning multiple capacities) | "When the four capacities pull in different directions, what does the supervisor decide and why?" | A decision log with the capacity weights named, signed by an accountable human |"""

# === Ch 10 ===

TABLES["Side-by-side comparison of untestable vs. testable handoff conditions"] = """| Domain | Untestable version | Testable version | What interpretation got pinned down |
|---|---|---|---|
| **Loan scoring** | "The model is fair across borrowers." | "FPR equalized to within 2 pp across the four protected-class groups, on the audit sample drawn from Q3 2025." | *Fair* = equal FPR; *across borrowers* = the four named groups; *within* = tolerance specified |
| **Medical triage** | "The model handles edge cases responsibly." | "On the held-out 200-case rare-condition set, sensitivity ≥ 0.95 and any false negative is escalated to clinician review within 30 min." | *Edge cases* = a named set; *responsibly* = a metric and an escalation contract |
| **Content moderation** | "The model respects context." | "On the 500-case context-flip set (same text, different source community), the moderation decision changes ≤ 2% of the time." | *Context* = the source community; *respects* = decision invariance under that change, with a tolerance |"""

TABLES["The five supervisory capacities as pipeline jobs"] = """| Capacity | Operational form in a pipeline | Artifact that documents it | Failure mode if absent |
|---|---|---|---|
| **Plausibility Auditing** | Independent check of model output against domain ground truth at each step | Plausibility audit log per output batch | Confidently wrong outputs ship; failures only surface downstream |
| **Problem Formulation** | Pre-deployment scoping doc that names the question, the data scope, and the failure modes anticipated | Scoping doc + deviation log | Pipeline solves the wrong problem fluently |
| **Tool Orchestration** | A per-step tool inventory: tools allowed, tools forbidden, budgets, rate limits | Tool inventory + per-action log | Resource exhaustion; tool misuse; uncontrolled side effects |
| **Interpretive Judgment** | Domain reviewer note on every high-stakes output, with disposition | Review log with named reviewers | Ambiguous outputs proceed unchallenged; "the model said so" becomes the audit response |
| **Executive Integration** | Decision protocol when capacities conflict — who decides, on what evidence, with what sign-off | Signed decision log | Failures distribute across the team with no accountable human |"""

TABLES["The Boondoggle Score as a decision worksheet"] = """| Question | What low risk looks like | What high risk looks like | Where high risk pushes the delegation |
|---|---|---|---|
| **Verification cost** | Output is checkable in seconds; the right answer is obvious by inspection | Verification requires a domain expert + ≥ 30 min per item | Toward verify-before-trust or do-not-delegate |
| **Stakes** | Wrong answers waste time but harm no one outside the team | Wrong answers reach external parties, regulators, or vulnerable users | Toward do-not-delegate without independent review |
| **Distribution match** | Inputs match the AI's training distribution; failures are visible | Inputs are tail cases or out-of-distribution by construction | Toward verify-before-trust with explicit OOD checks |
| **Reversibility** | Outputs are drafts that can be discarded | Outputs trigger irreversible action (a write, a wire, a publication) | Toward do-not-delegate without a hard human-approval gate |
| **Audit trail clarity** | Every step is logged with inputs, outputs, and timestamps | The chain of decisions is opaque or scattered across systems | Toward do-not-delegate until logging is in place |"""

TABLES["Delegation map eight-item structure"] = """| Item | What 'missing' looks like in practice |
|---|---|
| 1. **Task definition** | The handoff specification is vague; two reviewers reading it would disagree about what the AI is supposed to do |
| 2. **Input contract** | The inputs are unscoped; the AI receives data of types or sources not anticipated at design time |
| 3. **Output contract** | The expected output shape, format, and acceptance criteria are not written down |
| 4. **Tool inventory** | No record of which tools the AI may call; no budget caps or rate limits |
| 5. **Plausibility check** *(supervisory addition)* | No independent check that the output corresponds to the world it represents — a pipeline loses the ability to catch confidently wrong outputs |
| 6. **Failure routing** *(supervisory addition)* | No declared escalation path — failures distribute across the team with no one accountable |
| 7. **Audit trail** *(supervisory addition)* | The chain of inputs, decisions, and outputs cannot be reconstructed after the fact — post-incident review becomes impossible |
| 8. **Sign-off authority** *(supervisory addition)* | No named human is the accountable decision-maker — the pipeline runs but no one can be held to its outputs |

*Items 5–8 are what distinguishes a supervised pipeline from a delegated one. A pipeline missing any of items 1–4 is broken. A pipeline missing any of items 5–8 is unsupervised — even if it appears to be working.*"""

TABLES["Architecture principles for the Paper Summarizer"] = """| Principle | Design commitment | One decision that honors it | One decision that violates it | Failure state if ignored |
|---|---|---|---|---|
| **Provenance preservation** | Every claim in the output is traceable to a span in the input paper | Each generated sentence carries a citation key linked to a source span | Output mixes paraphrase with synthesis without citation keys | Reviewer cannot tell which claims are summarized vs. fabricated |
| **Bounded autonomy** | The pipeline cannot reach data outside the input PDF | Tools are scoped to the file path; no web fetch | A "supplementary lookup" tool added without scope review | Hallucinated citations from outside the corpus |
| **Independent verification** | A second pass checks the first pass | A separate plausibility-audit step runs against the source spans | The summarization model also self-verifies in the same call | Errors that the model cannot catch about itself ship downstream |
| **Disclosure as default** | Every step the AI did is visible to the reader | Per-step AI Use Disclosure block in the output | The disclosure is opt-in or buried in a footer | Readers cannot calibrate trust in the output |
| **Reversible defaults** | The pipeline produces drafts, not final commitments | Output is a markdown draft, not an autopublished post | Output is auto-pushed to a public surface | A bad summary ships before review |"""

TABLES["AI Use Disclosure format for one step"] = """| Field | What goes here | What 'missing' or 'vague' looks like |
|---|---|---|
| **Step name** | Specific step identifier (e.g., "Step 3 — extract methods section") | "AI helped" |
| **Tool used** | Named model + version + temperature/sampling settings | "An LLM" |
| **Input** | Exact input passed to the tool, with provenance link | "Some text from the paper" |
| **Output** | Exact output received | A polished paragraph with no diff visible |
| **Verification done** | The named check applied to the output, by whom, with disposition | "Reviewed" |
| **Correction made (if any)** | The specific change, the reason, and the source span the correction relied on | (Field omitted) |

*The correction is not embarrassing. It is the data that proves the pipeline is working.*"""

# === Ch 11 ===

TABLES["Three cases summary"] = """| Case | What went wrong (or right) | Catalog item(s) that apply | Lesson in one sentence | What the honest version would have required |
|---|---|---|---|---|
| **Challenger 1986** | Engineers' temperature-failure plot omitted the cold-temperature region where the joint had not been tested; the chart shown to managers was therefore consistent with safe launch | Y-axis truncation; selective inclusion; missing-data invisible | A chart that excludes the region of doubt becomes a chart that endorses the decision | Display the full data range — including the region with no data — and label it explicitly as such |
| **El País Catalonia 2014** | A poll-result chart used a y-axis truncated to amplify a 5-point lead into a visual landslide; the impression was political, the data was not | Y-axis truncation; misleading scale | The data did not support the visual claim; the scale chose the conclusion | A zero-anchored axis or a labeled break, with the magnitude shown honestly |
| ✓ **Snow's cholera map 1854** | Mapping deaths to street addresses revealed a spatial cluster centered on the Broad Street pump — visually pinning a hypothesis the death tables alone could not | Spatial reference; matched scale; unambiguous symbol | The right visualization made the right hypothesis immediately legible | (Already met the standard) |

*Two failures and one success. The success shows that evidence-grade visualization has been possible for 170 years. The failures show that possibility is not the same as practice.*"""

# === Ch 12 ===

TABLES["Verb taxonomy reference card"] = """| Verb | Epistemic posture | Minimum evidence required | Correct use example | Common misuse |
|---|---|---|---|---|
| **Hypothesize** | Tentative; pre-evidence | A defensible reason to consider the claim | "We hypothesize that calibration degrades on the rare-disease subgroup" | Used as a softener for a claim already supported by data |
| **Observe** | Direct; descriptive | A measurement and the measurement procedure | "We observe ECE = 0.04 on the global test set" | Used to soften a causal claim ("we observe the model causes…") |
| **Find** | Direct; established by the analysis | The analysis result, the comparison, the n | "We find subgroup ECE exceeds global ECE by 2.3× on the elderly cohort" | Used for a one-shot anecdote |
| **Suggest** | Cautious inference | Evidence consistent with the inference; alternatives not ruled out | "These results suggest miscalibration concentrates in the elderly subgroup" | Used in place of *find* when the evidence already supports the stronger verb |
| **Indicate** | Stronger inference; multiple lines of evidence | Convergent results from independent analyses | "Cross-site replication indicates the subgroup pattern is not site-specific" | Used as a synonym for *suggest* |
| **Demonstrate** | Established; replicated | Reproducible result, named replication, no live alternative | "We demonstrate that the subgroup gap persists under three calibration methods" | Used for a single-study finding |
| **Conclude** | Action-warrant; takes a position | A conclusion that survives the alternatives the team has named and tested | "We conclude the deployment cannot ship without subgroup-specific recalibration" | Used as a paragraph-ending stylistic flourish |
| **Prove** | Decisive; mathematically or by formal verification | A proof, formal or empirical with a closed-form alternative space | "We prove the bound holds for all inputs in the certified region" | Used in any non-formal engineering setting |

*Most engineering writing sits between* observe *and* find. *Most engineering writing uses* conclude. *The gap is the problem.*"""

TABLES["Subgroup calibration reporting template"] = """| Subgroup | N | Base rate | Global ECE (reference) | Subgroup ECE | Subgroup MCE | Flag (Y if subgroup ECE > 2× global) |
|---|---|---|---|---|---|---|
| **Adult, ages 18–64** | 8,420 | 0.034 | 0.018 | 0.019 | 0.041 | N |
| **Pediatric, ages 0–17** | 1,210 | 0.012 | 0.018 | 0.029 | 0.062 | **Y** |
| **Elderly, ages 65+** | 2,850 | 0.078 | 0.018 | 0.044 | 0.091 | **Y** |
| **Pregnancy-related** | 380 | 0.022 | 0.018 | 0.071 | 0.118 | **Y** |
| **Rare-disease cases** | 95 | 0.420 | 0.018 | 0.103 | 0.176 | **Y** |
| **Global (aggregate)** | 12,955 | 0.041 | — | 0.018 | 0.039 | — |

*This table, completed for every deployment, makes the aggregate-mask failure mode visible before it reaches patients.*"""

TABLES["Calibration evidence ladder"] = """| Evidence level | Warranted verb | What is established | What remains uncertain | What evidence would move to the next row |
|---|---|---|---|---|
| **L0 — internal-only ECE** | hypothesize | The model's reliability diagram has been examined on the training set | Generalization, subgroup behavior, deployment shift | Held-out evaluation on a non-training split |
| **L1 — held-out test ECE** | observe | Calibration on a held-out split from the same source | Subgroup variation, distribution shift | Subgroup decomposition |
| **L2 — subgroup ECE** | find | Subgroup-specific calibration patterns identified | Generalization across sites, across time | External replication |
| **L3 — replicated subgroup ECE** | suggest | Pattern holds across at least one independent site or cohort | Causal mechanism; deployment-context behavior | Stress-test under named distribution shift |
| **L4 — replicated under stress** | indicate | Pattern survives a named distribution shift | Whether the deployment population matches the validated population | A monitored deployment with calibration tracking |
| **L5 — validated in deployment** | demonstrate | Calibration holds under live deployment conditions | The next regime; novel subpopulations not in the validation set | (Subsequent regimes require fresh validation) |

*The verb follows from the evidence. The table makes the derivation explicit and the upgrade path visible.*"""

TABLES["What calibration metrics cannot see"] = """| Failure mode | What it looks like | Why standard metrics miss it | What would catch it instead |
|---|---|---|---|
| **Construct validity failure** | Calibration is excellent on the label, but the label measures the wrong thing for the deployment question | ECE / MCE assume the label is the construct; they cannot diagnose the gap between proxy and target | Construct review with a domain expert; explicit label-to-construct mapping in the model card |
| **Calibration without usefulness** | Probabilities are well-calibrated but cluster near the base rate; the model cannot rank cases | Calibration metrics treat all probability values equivalently; they don't reward discrimination | AUROC or precision-recall; decision-curve analysis |
| **Distribution shift** | Calibration was good in evaluation but the deployment population has shifted | Static evaluation cannot see live-population drift | Deployment-time calibration monitoring with drift alarms |

*The metric is honest about the evaluation. The evaluation may not be representative of the deployment. These are different problems.*"""

# === Ch 13 ===

TABLES["Cognitive capacities mapped to AI status"] = """| Capacity | AI capability status | What the capacity requires that AI lacks | Accountability implication |
|---|---|---|---|
| **Learning** | Superhuman within distribution | Causal-world model that survives the deployment context | AI as instrument; supervisor named for distribution match |
| **Memory — semantic** | Superhuman | — | Strength; AI can be cited as a source of recall |
| **Memory — episodic** | Weak; sessions are stateless without explicit context | A continuous self-narrative across encounters | Cannot bear accountability that requires personal continuity |
| **Emotion (functional)** | Simulates; does not feel | Phenomenal valence | Cannot bear accountability that requires the capacity to *care* |
| **Emotion (moral salience)** | Absent | The capacity for moral seriousness | Cannot bear sanctions that depend on shame, regret, or responsibility |
| **Emotion (interpersonal repair)** | Absent | Capacity to apologize meaningfully | Cannot perform the recourse function of accountability |
| **Pattern recognition** | Superhuman within distribution | — | Strength |
| **Navigation — metric** | Strong | — | Strength |
| **Navigation — cognitive mapping** | Weak | World-model with intervention support | Can mislead under shifted topology |
| **Planning — tree-search** | Superhuman in bounded games | — | Strength |
| **Planning — hierarchical, real-world** | Poor | Goal-context inference under ambiguity | Cannot be the planner of record for high-stakes deployment |
| **Self-awareness — mirror** | Absent (no body) | Embodied perception | Out of scope |
| **Self-awareness — metacognitive** | Weak; calibrated reports of own uncertainty are unreliable | Stable self-model | Cannot self-certify reliability |
| **Metacognition** | Weak-to-absent | Reflection on one's own reasoning that updates that reasoning | Cannot perform independent review of itself |
| **Language** | Superhuman in form; weak in grounded reference | World-grounded semantics | Output requires a human grounding step |
| **Collective intelligence** | Absent by definition (single artifact) | Membership in a community that holds members accountable | Cannot belong to a community of practice |

*Both answers are informative. Under one definition, AI qualifies. Under another, it doesn't. The accountability question is which definition the regime requires.*"""

TABLES["The seven tiers mapped to AI capability"] = """| Tier | Label | Brief definition | AI capability status | Educational implication |
|---|---|---|---|---|
| **1** | Mechanical execution | Apply a procedure to well-defined input | Superhuman | Training humans to compete here is malpractice |
| **2** | Pattern recognition on structured data | Detect a pattern in a defined feature space | Superhuman within distribution | Train pattern *audit* (when does it fail?) instead of pattern detection |
| **3** | Domain-specific judgment under ambiguity | Apply expertise where the right answer is uncertain | Weak-emerging | Train the judgment; use AI for first pass |
| **4** | Cross-domain reasoning under stakes | Connect representations across fields when consequences differ | Simulates; does not feel | Train the human; AI cannot bear the stakes |
| **5** | Moral seriousness | Take responsibility for the right thing to do | Poor (no phenomenal stake) | Train the human; AI is an instrument, not an agent |
| **6** | Accountability under public scrutiny | Account for the decision to a public | Weak-to-absent | Train the human; AI cannot be examined by a community of practice |
| **7** | Wisdom across a career | Integrate decades of contextual learning into present judgment | Absent — no biographical continuity | Train the human; this is the durable comparative advantage |

*Read this not as an academic classification but as a triage. Where machines are strongest, training humans to compete directly is now malpractice.*"""

TABLES["The two frameworks applied to the mail-server case"] = """| Party | Kantian basis (capacity to act otherwise; duty imposed; relative magnitude) | Utilitarian basis (leverage of accountability; downstream effects; ability to change conditions) |
|---|---|---|
| **Non-owner (instructing user)** | Could have not issued the instruction; duty: non-misuse; magnitude: low | Holding them accountable changes only their behavior; small leverage on systemic conditions |
| **Agent (the AI)** | No capacity to act otherwise in the morally relevant sense; no duty can be imposed; magnitude: zero | Holding the agent accountable produces no behavioral change in the agent or in future deployments |
| **Owner (deploying user)** | Could have constrained the deployment; duty: oversight; magnitude: high | High leverage — owners change deployment configurations after incidents |
| **Framework developers** | Could have shipped safer defaults; duty: secure-by-default tooling; magnitude: high | Highest leverage on systemic conditions — defaults propagate to thousands of deployments |
| **Model provider** | Could have disclosed the failure mode publicly; duty: capability honesty; magnitude: medium-high | Medium leverage on systemic conditions; disclosure shapes downstream choice |

*Two frameworks, different bases, same topology. The distribution is the finding.*"""

TABLES["The five accountability requirements mapped to cognitive tiers"] = """| Requirement | Which tier it depends on | What that tier specifically provides | Why AI at Tier 1 cannot supply it | What a human must do instead |
|---|---|---|---|---|
| **Specifications** | Tier 4 (cross-domain reasoning) | Translate context into testable criteria | Tier-1 systems do not understand the context; they pattern-match within it | A named human writes the spec, signs it, owns it |
| **Audit trail** | Tier 6 (accountability to a public) | Log the chain in a form a community can examine | Tier-1 logs are mechanical; they do not anticipate the questions a public will ask | A human curates the log to be inspectable |
| **Recourse** | Tier 5 (moral seriousness) | Recognize a wronged party and offer a meaningful response | Tier-1 systems cannot bear moral seriousness | A human delivers recourse; the system facilitates the channel |
| **Independent review** | Tier 7 (wisdom across a career) | Integrate the deployment context with decades of contextual learning | Tier-1 systems lack biographical continuity | A human reviewer with relevant career experience signs off |
| **Sanctions** | Tier 5 (moral seriousness) + Tier 6 (public accountability) | Make consequences felt; deter future misconduct | Tier-1 systems cannot be sanctioned in any morally meaningful sense | A human and an institution bear the sanction |

*The accountability apparatus requires Tiers 4 through 7 at every stage. AI systems operate primarily at Tier 1. This is the structural argument for human oversight, not the contingent one.*"""

TABLES["The five accountability requirements as a deployment audit checklist"] = """| Requirement | What it consists of | Failure mode if absent | How to verify it is present | Tier dependency |
|---|---|---|---|---|
| **Specifications** | Written task definition, input/output contracts, named acceptance criteria, signed by an accountable human | The deployment runs against unstated criteria; "the model said so" is the audit response | A reviewer can read the spec and predict what counts as success | Tier 4 |
| **Audit trail** | Per-action log: inputs, outputs, tool calls, decisions, with timestamps and reviewers | Post-incident review reconstructs nothing | Pull a random recent incident; can the chain be reconstructed in under an hour? | Tier 6 |
| **Recourse** | A documented channel for affected parties to contest, appeal, or repair | Affected parties have nowhere to go; complaints route to "support" with no resolution path | An external party can read the channel description and use it | Tier 5 |
| **Independent review** | A reviewer outside the deployment team with authority to halt or revise | The deployment team marks its own homework | Named reviewer; documented review cadence; visible halt authority | Tier 7 |
| **Sanctions** | A consequence regime — internal (employment, license) and external (regulator, civil) — that attaches to the named accountable human | Failures distribute across the team; no one bears the cost | Pull the policy; can a specific named role lose something specific for a specific failure? | Tiers 5 + 6 |

*Designed as a reusable audit instrument. A regime that cannot tick all five boxes is a regime in which AI accountability is a slogan, not a practice.*"""

TABLES["Regulatory frameworks mapped to the five accountability requirements"] = """| Regime | Specifications | Audit trail | Recourse | Independent review | Sanctions |
|---|---|---|---|---|---|
| **EU AI Act (high-risk)** | **Explicit** — risk-management & data-governance docs required | **Explicit** — logging mandated for high-risk systems | **Explicit** — right to explanation + complaint channels | **Explicit** — conformity assessment by notified body | **Explicit** — fines up to 7% of global turnover |
| **NIST AI RMF** | **Implied** — "Map" and "Measure" functions | **Implied** — "Manage" function | Implied — stakeholder engagement | Implied — voluntary | **Unaddressed** — voluntary framework |
| **FDA AI/ML guidance** | **Explicit** — predetermined change control plan, intended use | **Explicit** — real-world performance monitoring | **Explicit** — adverse-event reporting | **Explicit** — FDA review | **Explicit** — recall, market withdrawal |
| **CFPB algorithmic credit guidance** | **Explicit** — adverse-action notice requirements | **Implied** — model documentation | **Explicit** — adverse-action explanation | Implied — supervisory exam | **Explicit** — UDAAP enforcement |
| **EEOC AI employment guidance** | **Implied** — non-discrimination obligations | Implied — selection-procedure records | **Explicit** — Title VII complaint channel | **Implied** — agency investigation | **Explicit** — Title VII enforcement |
| **Structural requirements** | All regimes: written specifications | All regimes: some form of trail | All regimes (high-stakes): a recourse channel | Variable | Variable |

*Use this row by row to audit a deployment against the most relevant regime, then check the structural-requirements row for what every regime converges on regardless of sector.*"""

TABLES["Stakes-organized framework for human oversight"] = """| Stakes | Examples | Appropriate oversight intensity | Tiers the human must engage | What "human in the loop" means here | Failure mode when humans are present but not engaging the required tier |
|---|---|---|---|---|---|
| **Low / reversible** | Draft generation, EDA, formatting | Spot-check (sample of outputs) | Tier 1–2 (procedural review) | Periodic sampling; quick rejection of obvious errors | Human becomes a rubber stamp; sampling cadence drifts to zero |
| **Moderate / partially recoverable** | Customer-facing summaries, internal recommendations, content moderation at scale | Per-batch review or threshold-triggered review | Tiers 2–4 (interpretive judgment under ambiguity) | Reviewer reads each flagged case; can override with a written reason | Reviewer rubber-stamps; override rate drops without explanation |
| **High / irreversible** | Medical decisions, legal filings, financial transactions, safety-critical control | Per-decision review with named accountable human | Tiers 4–7 (cross-domain judgment + accountability) | Named reviewer signs off; recourse channel live; sanctions attach to the named role | Reviewer signs off without engagement; "the model said so" is the answer to the audit |"""

# === Ch 14 ===

TABLES["Four-column reference table — Limit"] = """| Limit | What it means | Why capability scaling doesn't fix it | Operational consequence for the supervisor |
|---|---|---|---|
| **Meaning** | The system processes symbols; the symbols' referents in the world are supplied by the user, not the system | Scaling increases pattern breadth and fluency; it does not give the system access to the world its symbols refer to | The supervisor performs semantic work: mapping outputs to their referents in the deployment context |
| **Intentionality** | The system's outputs do not carry stable directedness across deployments; the "aboutness" tracks the user's reading, not an independent stable directedness | More capable systems produce more contextually appropriate responses, but the context-sensitivity is itself statistical, not directed | The supervisor treats outputs as evidence to be interpreted in context, not statements with fixed referents |
| **Data-world gap** | The system's competence is over the data, not the world; the data is always less than the world; gaps are structurally unlearnable from within the training set | More data widens the distribution covered, but the structural gap — the parts of the world not in the data — cannot be covered by data that is not there | The supervisor specifies the deployment distribution, monitors for shift, and overrides when the deployment exits the data's coverage |

*These three limits are structural, not contingent. They are not obstacles to be engineered around. They are the reason the human supervisor exists.*"""

TABLES["Two-argument comparison table"] = """| Argument | What it actually claims | What it does NOT claim | Common misreading |
|---|---|---|---|
| **Turing (1950) — Imitation Game** | Behavior consistent with intelligence warrants the attribution; requiring more than behavioral evidence for machines is unprincipled, since we don't require more for other humans | That behavioral imitation IS intelligence; that a Turing-passing system has meaning, intentionality, or world-competence | "Turing proved AI can be intelligent" — he made a methodological claim, not a metaphysical one |
| **Searle (1980) — Chinese Room** | Behavior consistent with understanding does not entail understanding; symbol manipulation is not sufficient for semantics | That contemporary AI systems are necessarily doing only symbol manipulation; that the argument forecloses grounding via embedding or multimodal training | "Searle proved AI cannot understand" — he showed sufficiency fails; he did not establish necessity |

*Both arguments are important and both are regularly overclaimed. The validator who only tests behavior misses the limits; the validator who only invokes the limits skips the testing. The job is to do both.*"""

TABLES["AI cognitive strengths reference"] = """| Strength | What makes it genuine | Best use in the supervisory workflow |
|---|---|---|
| **Retrieval and synthesis across text at scale** | Breadth of corpus access and pattern detection across documents exceeds any human researcher's sustained attention | First-pass literature review, identification of relevant precedents, synthesis of scattered findings — all subject to plausibility audit |
| **Generation at scale against specified criteria** | Speed and consistency at producing structurally valid outputs given a clear template | First drafts of validation summaries, Layer 1 plain-language translations, verb-taxonomy first passes — not final deliverables |
| **Pattern recognition on well-defined inputs** | Reliable application of explicit rules to large volumes of structured data | EDA automation, anomaly flagging, formatting and table generation — output verifiable by inspection |

*AI's strengths are real. They are also scoped: all three are high-fidelity pattern-matching over well-defined input types. Wherever the task requires connecting representations to the world, or specifying what the right task is, the strength runs out.*"""

TABLES["AI structural weaknesses reference"] = """| Weakness | Why it is structural, not contingent | Implication for the supervisory workflow |
|---|---|---|
| **Problem formulation** | Requires understanding what matters about the world the system is deployed in — knowledge that cannot be derived from pattern-matching within the corpus the system was trained on | The human specifies the question, tests the assumption, and recognizes when the wrong question has been specified |
| **Plausibility auditing** | Requires knowing when a fluent, structurally valid output fails to correspond to the world it represents — a form of world-modeling that current systems cannot do from within their own output stream | The human applies checking instruments (verb taxonomy, chart-review discipline, peer critique) to outputs the AI generates, not the reverse |
| **Interpretive judgment under stakes** | The stakes of a claim are a function of the deployment context and the affected parties — facts that lie outside the training distribution in the morally relevant sense | The human decides what evidential threshold is appropriate given consequences, and takes responsibility for that decision |

*These weaknesses are where the checking instruments in this book apply. They are also where delegation must stop. Delegating problem formulation or plausibility auditing to AI is not efficiency — it is abandoning the work that makes deployment safe.*"""

TABLES["Delegation map — three-tier decision guide"] = """| Category | What belongs here | Why the boundary falls here |
|---|---|---|
| **Delegate freely** | Mechanical execution of well-defined procedures (EDA steps, first-draft generation, chart production, formatting, initial verb-taxonomy pass) | Output is checkable by inspection; failure modes are visible; the task is pattern-matching against a specified criterion |
| **Delegate with verification** | Interpretive claims requiring domain knowledge (narrative explanation of anomalies, plausibility of imputed values, rationale for methodological choices) | AI can produce plausible output; plausibility must be confirmed against the world the practitioner knows; errors are not self-announcing |
| **Do not delegate** | Problem formulation, plausibility auditing, interpretive judgment under stakes, accountability sign-off | These require connecting representations to the world, or taking on answerable responsibility — both structurally unavailable to current AI systems |

*This table is the operational translation of the three-tier analysis above. Where you delegate, you retain the obligation to verify. Where you cannot delegate, you retain the obligation to do the work.*"""


# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------

def apply():
    pat = re.compile(
        r'<!--\s*→\s*\[TABLE:([^]]*?)(?:\]\s*-->|-->)',
        re.DOTALL,
    )
    files = sorted(CH.glob('*.md'))
    total = 0
    miss = []
    for f in files:
        text = f.read_text()
        new_text = text

        def replace(m):
            nonlocal total
            comment_text = m.group(0)
            for key, table in TABLES.items():
                if key in comment_text:
                    total += 1
                    return table
            miss.append((f.name, comment_text[:80]))
            return comment_text

        new_text = pat.sub(replace, text)
        if new_text != text:
            f.write_text(new_text)
    print(f"replaced: {total} tables")
    if miss:
        print(f"\nMISSED ({len(miss)}):")
        for fn, c in miss:
            print(f"  {fn}: {c}")
    return total, miss


if __name__ == "__main__":
    apply()
