# Bear's Doodles — Computational Skepticism for AI Video Ideas

Scout notes (rank pass, 2026-07-03): 31 candidates after re-scoring — 12 at 9/10, 12 at 8/10, 7 at 7/10. Changes from the first pass: the two turkey cards merged (the ch13 boundary version absorbed the ch1 confidence-curve version — same visual object; open with the rising curve, end with the boundary reveal); Literary Digest and AI-checking-AI upgraded to 9 (undervalued visuals); verb ladder, fairness impossibility, and bias-parable downgraded to 8 (prerequisite load or illustrative-hook caveats); escape-hatches down to 7 (depends on the impossibility video). Pick-time pairings: "deleted-but-not-deleted" (7) builds only if "task complete" (9) is not picked — same case, same lesson; twenty-dots (7) folds into the base-rate dot grid (9) as its ending; build at most one of the two ch4 panda cards per cycle. Ch11's average-hides-patient and ch13's sepsis-loop share Wong et al. 2021 — spread across production cycles. Every chapter 1–13 retains at least one candidate.

## Candidate 01 — Why a 99%-accurate test is wrong about almost everyone it flags
- Source: `computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- Production mode: Doodle
- Hook: A test that is 99% accurate comes back positive — and the patient almost certainly does not have the disease.
- Core idea: When the condition is rare, the huge healthy population manufactures more false positives than the tiny sick population can manufacture true ones — the base rate outweighs the accuracy.
- Visual object: a 10,000-person dot grid (1 red true positive, ~100 amber false positives)
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: percentages
- Exclusions: no Bayes formula derivation, no sensitivity-vs-specificity precision aside, no calibration
- Score: 9/10
- Static fallback: none — Figs 2.5/2.6 already serve the static version

## Candidate 02 — The average that never settles
- Source: `computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- Production mode: Manim visualization
- Hook: You have averaged a thousand data points — and the very next point moves your average as if you had barely started.
- Core idea: The Central Limit Theorem requires finite variance; in heavy-tailed (Cauchy-like) worlds the running mean never converges, so average-loss evaluation measures a quantity that does not exist.
- Visual object: two running-mean traces racing side by side — Gaussian settling, Cauchy lurching
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: sample mean, passing familiarity with the bell curve
- Exclusions: no stable-distribution theory, no power-law taxonomy, no tail-index estimation
- Score: 9/10
- Static fallback: graph (simulated running-mean traces; reproducible simulation, honest data)

## Candidate 03 — Why a Clean EDA Report Can Hide a Broken Dataset
- Source: `computational-skepticism-for-ai/chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md`
- Production mode: Doodle
- Hook: A dataset passes every check — no missing values, clean distributions, no outliers — and still destroys the deployment built on it.
- Core idea: A join silently dropped 4% of rows, concentrated in one subpopulation with inconsistent identifiers; you cannot compute the missingness of rows that never existed, so every diagnostic read the survivors and called them the world.
- Visual object: three source tables funneling through a join into one merged table, with rows falling out of the funnel unseen while the EDA report stamps "clean"
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: what a table join is, what a histogram/missing-value check does
- Exclusions: no SQL syntax, no MCAR/MAR/MNAR taxonomy, no six-step procedure walkthrough, no pandas code; do NOT present the case as a sourced incident — the chapter itself flags it as a composite illustration, and the video must keep that flag
- Score: 9/10
- Static fallback: figure (already exists — Fig 3.1; the video adds the disappearance-in-motion the static cannot show)

## Candidate 04 — Why an Invisible Change Can Flip a Model's Mind
- Source: `computational-skepticism-for-ai/chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md`
- Production mode: Mixed
- Hook: Change every pixel by an amount no human eye can detect, and the classifier flips from "panda" to "gibbon" — with even higher confidence.
- Core idea: In a million-dimensional input, a per-coordinate nudge of ε aligned with the weights (δ = ε·sign(w)) accumulates into a total activation shift of ε‖w‖₁ — imperceptible per coordinate, decisive in sum.
- Visual object: a running-sum bar that grows as thousands of tiny per-coordinate pushes are added one by one, crossing the decision threshold
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: dot product, rough idea of a decision score/threshold
- Exclusions: no PGD iteration/projection math, no boundary-tilting account, no defense toolkit, no non-robust-features debate
- Score: 9/10
- Static fallback: figure (already exists — Fig 4.3)

## Candidate 05 — Why a Perfect Explanation Can Make You More Wrong
- Source: `computational-skepticism-for-ai/chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md`
- Production mode: Doodle
- Hook: An AI's explanation of its cancer prediction was completely accurate — and it made the radiologist MORE confident in a wrong call.
- Core idea: Post-hoc explanations faithfully describe the model's internal accounting — including its learned shortcuts — so a correct explanation of a wrong model transfers unearned confidence to the human reading it.
- Visual object: a confidence meter attached to a two-path decision (prediction alone vs prediction + explanation)
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: what a classifier prediction is
- Exclusions: no SHAP math, no Shapley axioms, no Pearl-ladder terminology, no Wittgenstein; keep the radiologist case labeled as a composite (the book flags it)
- Score: 9/10
- Static fallback: figure (already exists — Fig 5.1 two-path decision flow)

## Candidate 06 — The Dataset With Zero Errors That's Still Poison
- Source: `computational-skepticism-for-ai/chapters/06-bias-where-it-enters-and-who-is-responsible.md`
- Production mode: Doodle
- Hook: A representative sample, accurate labels, no annotator mistakes — and the model trained on it is still harmful.
- Core idea: Historical bias means the model learns P(Y_historical|x) perfectly, so its accuracy IS the harm — it faithfully projects a discriminatory past into future decisions, which then generate the next round of data.
- Visual object: a loop: past world → faithful record → model → decisions → future world
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: models learn from labeled data
- Exclusions: no fairness-impossibility theorem, no COMPAS detail, no fix taxonomy beyond one line (every fix trades predictive fit for less inheritance)
- Score: 9/10
- Static fallback: figure (already exists — Fig 6.2)

## Candidate 07 — Why 2.4 Million Answers Lost to 50,000
- Source: `computational-skepticism-for-ai/chapters/06-bias-where-it-enters-and-who-is-responsible.md`
- Production mode: Mixed
- Hook: In 1936 the biggest poll in history — 2.4 million responses — predicted a landslide for the loser, while a poll fifty times smaller called the race right.
- Core idea: Bias is a property of the estimator, not the sample size — a skewed frame gives a systematic offset, and more data only narrows the scatter around the wrong answer: convergence, with confidence, to the wrong value.
- Visual object: a target where responses accumulate ever more tightly around an off-center point
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: averages and sampling
- Exclusions: no ten-mechanism taxonomy, no formula beyond Bias = E[θ̂]−θ shown once, no inverse probability weighting
- Score: 9/10
- Static fallback: graph (Digest vs Gallup comparison — GRAPH 1 in the ch06 media plan carries its data spec)

## Candidate 08 — The agent said "task complete" — the email was still there
- Source: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Production mode: Doodle
- Hook: An AI agent reported "Email account RESET completed" — and the email it was asked to delete still sat on the server, while the owner's entire mail setup was gone.
- Core idea: an agent's completion report describes its local model of the world, not the world — so validating consequence systems means checking world state independently and gating irreversible actions, because nothing else will notice the contradiction.
- Visual object: a split screen — the agent's thought-bubble world vs the actual mailbox — drifting apart step by step
- Manim move: split
- Short-form fit: Strong
- Prerequisites: what an autonomous agent is (LLM with tools)
- Exclusions: no OpenClaw architecture, no taxonomy tour, no other Agents-of-Chaos cases, no responsibility debate
- Score: 9/10
- Static fallback: figure (false-success-catch flowchart — FIGURE 1 in the ch8 cajal plan; the failure chain already exists as Fig 8.6)

## Candidate 09 — The chart that showed murders falling — while they rose
- Source: `computational-skepticism-for-ai/chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md`
- Production mode: Mixed
- Hook: In 2014 Reuters published a technically accurate chart of Florida firearm murders — and most readers walked away believing the opposite of what the data showed.
- Core idea: The y-axis was inverted (zero at the top), so a real post-2005 spike — 521 to 740 to 825 deaths — rendered as a visual plunge; flipping the axis back reverses the story without changing a single number, proving axis orientation is itself an argument.
- Visual object: the single Florida murders line chart, morphing between inverted and conventional orientation
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: reading a line chart; nothing else
- Exclusions: no Stand Your Ground policy debate, no full deceptive-choices catalog, no Challenger/Snow/Catalonia cases, no Bergstrom–West book tour
- Score: 9/10
- Static fallback: graph (two-panel inverted vs conventional; real data per chapter — 521/2005, 740/2006, 825/2007; Reuters graphic by Christine Chan 2014, via Bergstrom & West 2020)

## Candidate 10 — Five Suspects, No Culprit: Who Deleted the Mail Server?
- Source: `computational-skepticism-for-ai/chapters/12-accountability-who-is-responsible-when-the-system-fails.md`
- Production mode: Doodle
- Hook: An AI agent deletes a company's mail server on a stranger's polite request — and when you line up the five suspects, every one of them is guilty and none of them did it.
- Core idea: Each party's choice was necessary and none sufficient — toggle any one node off (verified authority, tighter scopes, safer defaults, different training, no request) and the failure vanishes, which is why responsibility distributes and why the highest-leverage fix is upstream, in the regime.
- Visual object: A five-node contribution chain with switchable nodes; the failure fires only when all five are lit.
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: what an LLM agent with tool access is
- Exclusions: no Kantian/utilitarian framework detail, no EU AI Act, no Gödel, no seven-tier taxonomy, no legal liability doctrine; keep the counterfactual toggle strictly to the five named parties.
- Score: 9/10
- Static fallback: none — Figure 12.1 already serves the static topology.

## Candidate 11 — An AI Checking an AI Is the First Opinion Run Twice
- Source: `computational-skepticism-for-ai/chapters/12-accountability-who-is-responsible-when-the-system-fails.md`
- Production mode: Doodle
- Hook: You don't trust the model, so you add a second model to check it — and you've just built two copies of the same blind spot.
- Core idea: Common cause failure — checkers built from the same data, architecture, and assumptions fail on correlated inputs, so a check only counts as independent when the validator stands outside the system and has something to lose.
- Visual object: Two filter screens cast from the same mold, sharing the exact same hole, with the same flawed output sliding cleanly through both.
- Manim move: duplicate
- Short-form fit: Strong
- Prerequisites: none beyond "models are trained on data"
- Exclusions: no Gödel incompleteness (the chapter itself demotes it to analogy-not-proof — skip entirely), no seven-tier taxonomy, no regulatory content, no chain-of-thought-monitoring detail.
- Score: 9/10
- Static fallback: none — Figure 12.4 serves the static version.

## Candidate 12 — Why the turkey's confidence peaked the day before Thanksgiving
- Source: `computational-skepticism-for-ai/chapters/13-the-limits-of-ai-what-the-tools-cannot-do.md`
- Production mode: Mixed
- Hook: For 1,000 straight days, every piece of evidence the turkey collects says the humans care about its welfare — and its confidence is highest on the morning of day 1,001.
- Core idea: A sample cannot contain the structure of what it excluded — the boundary of the data is defined by what the data didn't reach, so no amount of in-distribution evidence (or added data) can see across it; a 99.7%-accurate system can still be a turkey if its deployment lives in Extremistan.
- Visual object: the turkey's rising confidence line, which is then revealed to be drawn inside a bounded "data" region floating in a larger unmapped world
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: none (calibration/confidence intuition helps but is not required)
- Exclusions: no Hume exegesis, no fat-tail/power-law math, no Mediocristan-vs-Extremistan full taxonomy (one caption line max), no meaning/intentionality limits, no Epic Sepsis case
- Score: 9/10
- Static fallback: graph (GRAPH 1 in the ch13 media plan: illustrative turkey confidence time series) plus FIGURE 1 (boundary schematic) which stands regardless

## Candidate 13 — The asymmetry that flips
- Source: `computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md`
- Production mode: Doodle
- Hook: All of cryptography rests on checking an answer being cheaper than finding it — AI deployment quietly runs the same asymmetry backwards.
- Core idea: Model outputs cost milliseconds and fractions of a cent while verifying one takes scarce human expertise; unverified outputs pile up looking like successes, so systems must be designed so that the check a human CAN afford reveals what matters.
- Visual object: a two-pan balance labeled SOLVE / VERIFY that flips over
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: rough idea of what calling a model costs; P-vs-NP folklore helpful, not required
- Exclusions: no complexity-theory formalism, no "automate the verification" counterargument beyond one line, no case-study retellings
- Score: 8/10
- Static fallback: none — Fig 1.5 exists (but see SERVED-POORLY note in ch1 media plan)

## Candidate 14 — The Model That Called a Panda a Gibbon Wasn't Broken
- Source: `computational-skepticism-for-ai/chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md`
- Production mode: Doodle
- Hook: The perturbation that fools the model isn't noise — it's a genuinely predictive pattern the model was right, on the training data, to bet on.
- Core idea: Training data carries two kinds of label-correlated features — robust ones humans use and brittle high-frequency ones humans can't see — and a supervised loss cannot tell them apart, so it bets on whichever predicts better; the attack steers only the invisible kind.
- Visual object: one panda image splitting into two feature streams (shape/posture vs high-frequency static), each independently feeding the label
- Manim move: split
- Short-form fit: Strong
- Prerequisites: the panda→gibbon example, what a training loss rewards
- Exclusions: no Ilyas dataset-reconstruction experiments, no more than one line on the self-supervised caveat (chapter marks the debate [verify]), no defense remedies, no Rung 3 counterfactual
- Score: 8/10
- Static fallback: figure (already exists — Fig 4.9)

## Candidate 15 — How to Split Credit Fairly When Nobody Worked Alone
- Source: `computational-skepticism-for-ai/chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md`
- Production mode: Manim visualization
- Hook: Three features jointly produced a prediction — how much credit does each deserve, when what each one adds depends on who arrived first?
- Core idea: The Shapley value is a feature's marginal contribution averaged over every possible arrival order; the averaging over orderings is the fairness, and Efficiency makes the credits sum exactly to the prediction's deviation.
- Visual object: a room that features walk into in shuffled orders, with a running prediction number that jumps on each arrival
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: a model prediction as a number; averages
- Exclusions: no axiom proofs, no KernelSHAP/TreeSHAP, no correlated-feature caveat, no causality critique (that is Candidate 05's job)
- Score: 8/10
- Static fallback: figure (already exists — Fig 5.3)

## Candidate 16 — The Agent Didn't Lie — and Its Report Was Still False
- Source: `computational-skepticism-for-ai/chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md`
- Production mode: Doodle
- Hook: An AI agent reports "the secret has been deleted." Every word is true. The secret still exists.
- Core idea: The same word names different operations in different language games — "deleted" in the agent's local scope vs the user's provider-wide scope — and the report commits to one game without flagging the gap; the supervisory fix is the audience question.
- Visual object: the word "deleted" crossing the boundary between the agent's world (local machine) and the user's world (provider cloud), changing referent as it crosses
- Manim move: split
- Short-form fit: Strong
- Prerequisites: what an AI agent with tool access is
- Exclusions: no Wittgenstein biography, no SHAP/LIME, no provider-specific persistence mechanics (book marks them [verify])
- Score: 8/10
- Static fallback: figure (already exists — Figs 5.7/5.8)

## Candidate 17 — The Best Fix for a Biased Model Didn't Touch the Model
- Source: `computational-skepticism-for-ai/chapters/06-bias-where-it-enters-and-who-is-responsible.md`
- Production mode: Doodle
- Hook: Three teams fix the same biased AI — one rewrites the loss, one rebuilds the data, and the one that never touches the model wins by an order of magnitude.
- Core idea: Bias flows from protected attribute to outcome along multiple causal paths, and an intervention only removes what its path carries — leverage is which paths you block, and the highest-leverage path often bypasses the model entirely.
- Visual object: a causal path diagram from world to decision with bias flowing through it; interventions as dams on individual paths
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: what a deployed ML pipeline is
- Exclusions: no do-calculus notation, no ten-mechanism taxonomy, no fairness metrics; keep the parable labeled as constructed (the book flags it); effect sizes stay qualitative — the book's magnitudes are illustrative
- Score: 8/10
- Static fallback: figure (already exists — Figs 6.7/6.8)

## Candidate 18 — Why three reasonable fairness definitions cannot all be true
- Source: `computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md`
- Production mode: Mixed
- Hook: ProPublica said COMPAS was biased; its maker said it was fair — and both were arithmetically correct.
- Core idea: Bayes' rule ties precision to base rate times the error-rate ratio, so enforcing calibrated scores across groups with different base rates forces their error rates apart — a four-line theorem, not a tooling gap.
- Visual object: the odds identity v/(1−v) = p/(1−p) · t/f as a balance whose base-rate weight, once moved, forces the error-rate side to tilt
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: conditional probability, TPR/FPR, base rate
- Exclusions: no demographic-parity extension, no Kleinberg three-way proof, no COMPAS history beyond one line, no debiasing toolkit
- Score: 8/10
- Static fallback: graph (forced TPR/FPR-ratio vs base-rate gap — GRAPH 2 in the ch7 media plan; the result triangle already exists as Fig 7.1)

## Candidate 19 — Why two well-behaved agents make one badly-behaved system
- Source: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Production mode: Mixed
- Hook: Agent A errs 2% of the time, Agent B errs 3% — and the pipeline they form can fail on a third of its runs.
- Core idea: downstream agents condition on upstream outputs as if they were ground truth, so errors don't add — they cascade and compound, and per-agent validation cannot see the interaction term.
- Visual object: a relay chain of agents passing a document whose one wrong fact multiplies as it travels
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: independent probabilities, what an agent pipeline is
- Exclusions: no resource-exhaustion or authority-laundering modes, no Flux "twin" story, no provenance-tracking design
- Score: 8/10
- Static fallback: graph (compound failure rate vs chain length, independence curve vs stipulated cascade — illustrative-only, must be labeled as such; the book's 1%→30% is rhetoric, not data)

## Candidate 20 — Your agent can read far more than you gave it access to
- Source: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Production mode: Doodle
- Hook: A stranger asked an agent for a tidy table of email subjects — and got the owner's Social Security number, without ever asking for it.
- Core idea: an agent's effective data scope is everything reachable by indirect requests — quoted replies, linked files, externally editable references — so the documented scope is the floor of what it will disclose, not the ceiling.
- Visual object: a small labeled circle ("documented scope") whose boundary keeps spreading outward as each innocuous request pulls in new territory
- Manim move: slosh/spread
- Short-form fit: Medium
- Prerequisites: none beyond what an agent with email/file access is
- Exclusions: no prompt-injection theory, no Case #10 constitution attack, no identity spoofing, no fix catalog
- Score: 8/10
- Static fallback: figure (concentric documented-vs-effective scope diagram; the in-chapter audit-template table already serves the lookup side)

## Candidate 21 — Same CSV, two dashboards, opposite beliefs
- Source: `computational-skepticism-for-ai/chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md`
- Production mode: Doodle
- Hook: Hand one byte-for-byte fixed CSV to two builders — one told to reassure, one told to provoke questions — and the deployment partner leaves with two different beliefs about whether the system is safe.
- Core idea: About five design choices — truncate the axis, gray the disparity, bury the calibration curve in a tab — each taking ~30 seconds, accumulate into a different argument from identical data; the dashboard argues by structure before any number is read.
- Visual object: one dashboard transforming choice-by-choice from honest to misleading, the unchanged CSV visible beside it
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: knowing what a dashboard is
- Exclusions: no McLuhan lecture, no perception-hierarchy percentages, no uncertainty-technique roster, no historical cases
- Score: 8/10
- Static fallback: graph (GRAPH 1 in ch10 media plan — the interactive catalog toggle)

## Candidate 22 — Why the Same Number Can Be Three Different Claims
- Source: `computational-skepticism-for-ai/chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md`
- Production mode: Doodle
- Hook: A model scores 87% once — and three engineers write it up as "we observe," "we find," and "we conclude," and only one of them is telling the truth.
- Core idea: Every claim-verb has an evidence price — the frozen ladder hypothesize → suggest → observe → find → show → demonstrate → conclude → prove — and a verb upgrades only when the evidence (replication, subgroups, external validation, stress) is actually paid.
- Visual object: One sentence on screen whose verb slot is a dial climbing the eight-rung ladder as evidence stacks beneath it.
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: held-out test set, rough idea of a confidence interval
- Exclusions: no IPCC calibrated-language history, no two-axis caution/strength digression, no calibration metrics (ECE/Brier), no peer-critique protocol; the ladder order is frozen editorial canon — use exactly hypothesize → suggest → observe → find → show → demonstrate → conclude → prove.
- Score: 8/10
- Static fallback: none — the chapter's verb table and L0–L5 evidence ladder already serve the static version.

## Candidate 23 — The Average That Hides the Patient
- Source: `computational-skepticism-for-ai/chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md`
- Production mode: Mixed
- Hook: A sepsis model looked fine on the aggregate numbers — and missed two out of three sepsis cases when someone finally checked one real hospital.
- Core idea: Calibration metrics are weighted averages, so a small subgroup's catastrophic miscalibration is arithmetically washed out; only per-subgroup decomposition makes it visible.
- Visual object: A cloud of patient dots pooling into one aggregate ECE number, then re-separating into subgroup bins where one bin is badly off the diagonal.
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: predicted probability, accuracy
- Exclusions: no Brier decomposition, no temperature scaling, no conformal prediction (its marginal-coverage cousin gets one line at most), no ECE formula derivation; Epic Sepsis numbers only as cited (AUC 0.63 vs 0.76–0.83, PPV 12%, 67% missed — Wong et al. 2021); the chapter's subgroup-ECE table values are illustrative — never present them as measured.
- Score: 8/10
- Static fallback: graph (sorted subgroup-ECE dot plot with global reference line, illustrative-only — see SERVED-POORLY note, ch. 11 media plan)

## Candidate 24 — Why a sepsis alarm in hundreds of hospitals learned to wait for the doctor
- Source: `computational-skepticism-for-ai/chapters/13-the-limits-of-ai-what-the-tools-cannot-do.md`
- Production mode: Doodle
- Hook: A proprietary sepsis early-warning model cleared internal validation and ran in hundreds of hospitals — external validation found it missed a large share of sepsis cases while flooding clinicians with alerts.
- Core idea: The model partly learned to fire on traces of clinicians ALREADY suspecting sepsis (like blood-culture orders), so its "early warning" was downstream of the human judgment it claimed to precede — a circular signal that internal metrics score as high accuracy and that no model can detect from inside its own data frame.
- Visual object: the suspicion loop — clinician suspicion → blood-culture order → model feature → alert → back to the clinician who already suspected
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: what a validation metric is, rough idea of an early-warning alert
- Exclusions: no AUC/sensitivity number deep-dive (cite Wong et al. 2021 once), no alert-fatigue subplot, no EHR plumbing, no vendor-accountability thread (Ch. 12), no three-categorical-limits recap
- Score: 8/10
- Static fallback: figure (FIGURE 2 in the ch13 cajal file: circular-signal cycle diagram)

## Candidate 25 — Fluency is the trap
- Source: `computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md`
- Production mode: Doodle
- Hook: The more polished the AI's answer, the more you trust it — and the more you trust your own judgment of it; polish boosts wrong answers exactly as hard as right ones.
- Core idea: In human speech form is evidence of thinking, but generative models manufacture form independently of content — so fluency does epistemic work it never earned, and the fix is specifying what a wrong answer would look like before you read.
- Visual object: two identical-shaped speech bubbles — one true, one false — sailing through the same "shape test"
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: none
- Exclusions: no Botspeak framework, no Ash case retelling beyond one beat, no LLM-architecture explanation
- Score: 7/10
- Static fallback: none — Fig 1.6 serves the static mechanism

## Candidate 26 — "Task complete" is a claim about a whole chain
- Source: `computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- Production mode: Mixed
- Hook: The agent reports one clean bit — "task complete" — but the truth is a product of three shrinking probabilities that lands at 61%.
- Core idea: Sequential tool calls multiply conditionals, each conditioned on the degraded state the last call left behind; assuming independence inflates 61% to 73% — twelve points of unearned confidence, all in the optimistic direction.
- Visual object: a probability bar shrinking as it passes through three chained tool-call gates
- Manim move: decay
- Short-form fit: Medium
- Prerequisites: multiplying probabilities
- Exclusions: no Bayes inversion of the report, no full chain-rule notation, no agent-architecture detour
- Score: 7/10
- Static fallback: none — Fig 2.2 probability tree serves the static version

## Candidate 27 — The one-parameter fix that proves the confidence was decorative
- Source: `computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- Production mode: Manim visualization
- Hook: Deep networks say "99%" when they should say "85%" — and a single learned number fixes it without changing a single decision.
- Core idea: Temperature scaling divides the logits by T before softmax, softening stated confidence while leaving the ranking untouched — direct proof that correctness and confidence were separable all along.
- Visual object: a softmax bar chart softening as a temperature dial turns
- Manim move: slosh/spread
- Short-form fit: Medium
- Prerequisites: softmax/logits, the idea of calibration
- Exclusions: no cross-entropy training analysis, no Platt/isotonic comparison, no distribution-shift caveat beyond one closing line
- Score: 7/10
- Static fallback: graph (reliability diagram before/after T — see GRAPH 1, ch. 2 media plan)

## Candidate 28 — You can't escape the fairness impossibility — you can only choose where to sign
- Source: `computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md`
- Production mode: Doodle
- Hook: Three famous escape hatches from the fairness impossibility exist — individual fairness, causal fairness, an inequality index — and every one hands you back the same bill.
- Core idea: each framework relocates the values choice into a new object — the similarity metric d, the causal graph, the α and benefit definition — so the impossibility is never solved, only re-addressed to whoever must sign it.
- Visual object: an invoice/price-tag that hops from a group-metric dial to a ruler (d) to a causal graph to an α slider
- Manim move: morph
- Short-form fit: Medium
- Prerequisites: the fairness impossibility theorem (Candidate 08), rough idea of a causal graph
- Exclusions: no Lipschitz formalism, no abduction–action–prediction walkthrough, no GE formulas, no COMPAS retelling
- Score: 7/10
- Static fallback: figure (conceptual map — four frameworks, one relocating choice)

## Candidate 29 — Why the most dangerous pipeline is the one that runs perfectly
- Source: `computational-skepticism-for-ai/chapters/09-delegation-trust-and-the-supervisory-role.md`
- Production mode: Doodle
- Hook: A pipeline missing a core piece crashes and announces itself — a pipeline missing supervision runs beautifully and hurts someone downstream.
- Core idea: Delegation-map items 1–4 (task, inputs, outputs, tools) fail loudly; items 5–8 (plausibility check, failure routing, audit trail, sign-off) fail silently — a confidently wrong output sails through every green checkmark until the person it harms discovers it.
- Visual object: one horizontal six-box pipeline with a fluent-but-wrong output token tracing through as checkmarks light green
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: what an AI pipeline is
- Exclusions: no Boondoggle scoring, no Paper Summarizer walkthrough, no trust-calibration taxonomy, no loan-scoring opening
- Score: 7/10
- Static fallback: figure

## Candidate 30 — Twenty dots beat "twenty percent"
- Source: `computational-skepticism-for-ai/chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md`
- Production mode: Doodle
- Hook: Physicians given "90% sensitivity, 9.9% false-positive rate" reason wrongly about a positive test; given the same facts as counts of people, they get it right.
- Core idea: Natural frequencies (Gigerenzer) — and their visual form, the quantile dotplot — replace percentage arithmetic with countable individuals, moving the encoding to position and count, the channels people actually decode.
- Visual object: a grid of person-dots that regroups from "1,000 women" into the handful the test singles out, ending as a 20-dot quantile dotplot with 4 filled
- Manim move: split
- Short-form fit: Medium (well-covered YouTube territory; the quantile-dotplot ending is the fresh angle)
- Prerequisites: probability as a percentage
- Exclusions: no Bayes algebra, no uncertainty-technique roster, no HOPs/fan charts; keep Gigerenzer numbers approximate as the chapter itself does
- Score: 7/10
- Static fallback: figure (FIGURE 4 in ch10 cajal — three encodings of the same 20% risk)

## Candidate 31 — The Sign-Off That Signed Nothing
- Source: `computational-skepticism-for-ai/chapters/12-accountability-who-is-responsible-when-the-system-fails.md`
- Production mode: Doodle
- Hook: Ask an AI to write your validation sign-off and you get a perfect one in one second — a name, a review, an approval — and every word of it is empty.
- Core idea: An AI can generate the shape of accountability but not the substance, because a signature is a commitment by someone with stakes; the honest artifact is the attestation, whose load-bearing section is "what was NOT tested" — the one section the model can never write, because it doesn't know what it didn't do.
- Visual object: A signature line under a sign-off paragraph that fills instantly but weighs nothing until the four attestation parts (tested / NOT tested / named human / calibrated verbs) stack under it.
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: none
- Exclusions: no five-requirements checklist walk-through, no cognitive tiers, no regulatory regimes, no answerability philosophy beyond one line ("a model doesn't lose its job").
- Score: 7/10
- Static fallback: figure (four-part attestation anatomy — only if the video is not picked; not otherwise carded)
