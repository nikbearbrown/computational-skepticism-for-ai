# Chapter 2 — The Confidence Illusion

*Confident is not correct, and the number on the screen is decorative until you check it.*

---

I asked a classifier to score a batch of records for me last week, and it handed back a column of probabilities. 0.94. 0.91. 0.88. Clean, sorted, ready to drop into a dashboard. It looked done. Here's what's actually happening: that column is a set of *degrees of belief the model holds*, formatted to look like *facts about the world.* The 0.94 does not announce whether 94 out of every 100 cases scored 0.94 actually turn out positive. It does not announce the base rate of the thing I'm looking for. It does not announce whether the model was trained in a way that rewards saying 0.94 when it means 0.85. It just sits there, looking like a measurement.

This chapter is about the single most pervasive failure in AI deployment — confident numbers that are not correct — and it teaches one supervisory capacity hard: **plausibility auditing [PA]**, the capacity to hear the wrong note in a number *before* you can prove it wrong. Because the wrong note here is almost always the same note: the model forgot the prior, or you did, or nobody checked whether 0.94 means what it says.

## The trade-off the number hides

In a deterministic system, an output is a fact. "The function returned 42" is true or false, final, verifiable. A probability is a different animal. "The model returned 0.91" is not a fact about the world. It is a claim conditional on the model's training distribution matching this case, on the model's calibration being good, on no distribution shift having occurred. Remove any one of those conditions and the 0.91 means something else — or nothing.

So the design question for any confidence score is: *what did the score optimize for?* Modern classifiers optimize for being right on average, in aggregate, on data that looks like training data. They emphatically do not optimize for the stated number meaning what it appears to mean on the specific case in front of you. They bought aggregate accuracy at the expense of per-case honesty. That is the trade-off, and the rest of the chapter is learning to see it.

## The test that is 99% accurate, and the patient it kills

Let me tell you about a test. A screening test for some rare disease — one person in ten thousand has it. The company says the test is ninety-nine percent accurate. A patient takes it. It comes back positive.

How confident are you that this patient has the disease?

Stop. Pick a number. Say it out loud. Lock it in — the point of what follows is wrecked if you peek without committing.

I have put this to a lot of smart engineers, and almost everyone answers above ninety percent. The reasoning sounds airtight: the test is 99% accurate, it came back positive, so the patient probably has the disease. This is exactly the result the classic study found — Casscells, Schoenberger, and Graboys put a 1-in-1,000 version to sixty Harvard house officers, students, and attendings; most answered around 95% ("Interpretation by physicians of clinical laboratory results," *New England Journal of Medicine* 299, no. 18, 1978).

The actual answer is about one percent.

Let me do it by counting bodies, before any formula. Imagine ten thousand people take the test. One of them, on average, actually has the disease — that is the base rate, one in ten thousand. The test catches that person: one true positive. The other 9,999 are healthy. "Ninety-nine percent accurate" also means the test correctly clears 99% of healthy people — so it *falsely* flags the other 1%. One percent of 9,999 is about a hundred people. A hundred false positives.

So the pool of positive results is: one true positive and about a hundred false positives. A hundred and one flags. Pull one out at random and the chance it came from someone actually sick is 1/101 — about one percent.

(A precision note, since this chapter's whole brand is precision about numbers: "99% accurate" is doing double duty above. I used it as both the true-positive rate and the true-negative rate. Those are two different numbers — sensitivity and specificity — and a real test has two, not one. The loose shortcut is standard in textbooks; I am flagging it because a sharp reader should catch a book warning against decorative numbers if it uses one.)

The test is doing exactly what its box says. Nothing is broken. And your intuition was off by two orders of magnitude, because you computed the right answer to the wrong question. You computed *given the disease, how often is the test positive?* — 99%. The question you needed was *given a positive test, how often is the disease there?* You cannot get from one to the other without the base rate, and your intuition forgot the base rate. Almost all intuition forgets the base rate. In a world of common diseases that instinct served us; in a world of rare events and large-scale automated detection, it kills.

This is a **Humean** point wearing engineering clothes, and it is the [PA] muscle: the plausibility audit on a confident number *is* the base-rate check. Before you trust the flag, ask what fraction of the flagged population is real. When the positive class is rare — fraud, intrusions, harmful posts, adversarial inputs — even an excellent detector produces mostly false alarms. That is structural. No engineering escapes it without raising the base rate (screen a higher-risk population) or accepting lower sensitivity (miss more real cases to cut false ones). And the human cost is predictable: analysts drown in false flags, learn in their bones that the alarms mean nothing, and miss the real one when it comes.

## Bayes — the bookkeeping made explicit

The calculation has a name. Let $A$ = disease present, $B$ = positive test. Then

$$P(A \mid B) = \frac{P(A)\,P(B \mid A)}{P(B)} = \frac{P(A)\,P(B \mid A)}{P(A)\,P(B\mid A) + P(A^c)\,P(B\mid A^c)}$$

Plug in the disease numbers:

$$P(\text{disease} \mid \text{positive}) = \frac{0.0001 \times 0.99}{0.0001 \times 0.99 + 0.9999 \times 0.01} \approx \frac{0.000099}{0.010098} \approx 0.0098$$

About one percent. Same answer, now with the machinery showing. And the machinery makes one thing unmissable: the prior, $P(A)$, sits in the numerator with the *same weight* as the test's sensitivity. Drop it and you have thrown away half the equation. The positive test did real work — it raised the probability of disease a hundredfold, from 0.0001 to 0.0098. Both facts are true: the evidence mattered, and the posterior is still tiny. Neither is visible if you only read the accuracy number.

## Calibration — the diagnostic that tells you if the number is honest

Now the operational core of the chapter. A model can be very accurate and still be lying with its confidence scores, and calibration is how you catch it.

A model is **calibrated** when its stated probabilities match what actually happens. If it says "seventy percent" on a thousand cases, you want about seven hundred of them to turn out positive. If only four hundred do, the model is overconfident — its number is bigger than it has any right to be. If nine hundred do, underconfident.

You see it in a picture. Stated probability on the horizontal axis, actual frequency of positives on the vertical. A perfectly calibrated model traces the diagonal, where stated equals actual. A miscalibrated one peels off it, and the *shape* of the peel tells you how it's wrong.

Here is a pattern that turns up everywhere in modern deep learning, and it is not an accident of one bad model. Modern neural networks are systematically overconfident — the training regime (deep architectures, the softmax with cross-entropy loss, the tricks that improve accuracy) actively rewards extreme confidence even when the underlying decision is not that certain. A net will say "99%" when it should say "85%," and it will say it fluently. Guo, Pleiss, Sun, and Weinberger documented this precisely and showed the fix: **temperature scaling** — a single learned parameter $T$ that divides the pre-softmax logits $z$ before the softmax,

$$\text{softmax}(z/T)$$

with $T > 1$ softening the distribution toward honesty. One parameter, fit on a held-out set, and much of the overconfidence disappears (Guo et al., "On Calibration of Modern Neural Networks," ICML 2017, arXiv:1706.04599). The reason this works, and the reason it is worth internalizing: the model's *ranking* of cases was often fine; only the *stated confidence* was inflated. Temperature scaling fixes the number without touching the decision — which tells you the confidence and the correctness were separable all along. The number was decorative; temperature scaling is how you un-decorate it.

Here is the **Popperian** move that makes this actionable — and I am naming it as Popper's move, because the four diagnostic questions of this chapter are falsification conditions in disguise. Do not accept a model's stated probability without seeing its calibration curve *on data drawn from the actual deployment distribution.* State the condition under which you would reject the number, then go look. Without that prior specification you are reading the score with no criterion except how confident it sounds — and how confident it sounds is exactly the fluency trap from Chapter 1, operating on a number instead of a sentence.

The trade-off in temperature scaling, so I am not selling it as free: it fixes *average* calibration on the distribution you fit it to. It does nothing for distribution shift — if the deployment world drifts from the calibration set, the honest number goes stale, and it goes stale silently. This works if you value honest confidence on in-distribution data; it fails if you need honest confidence on the tail, on the novel case, on the day the world moves. Which is precisely the day you most needed it.

And calibration is not only a property of models. It is a property of *you.* Write ninety-percent confidence intervals for a stack of forecasting questions, then check how many actually contained the truth. Most people — most very smart people — find their "90%" intervals held about half the time. They were walking around two to three times more sure than the evidence warranted, and they never knew, because nobody ran the experiment. That is [PA] turned on yourself. Run the experiment.

---

## Exercises

### BUILD — make your pipeline emit confidence, calibrate, and catch the decorative number

Take a classifier you can run — a sentiment model, an image model, anything with a probability output — and a held-out set with ground-truth labels.

1. **Emit.** Run the model and capture its stated confidence on every case.
2. **Lock a prediction.** Before you plot: do you expect the calibration curve to track the diagonal, sag below, or ride above it? Where on the axis do you expect it to peel off? Write it down; you cannot revise it.
3. **Bin and plot.** Group predictions by stated confidence (0.0–0.1, …, 0.9–1.0). For each bin compute the empirical accuracy. Plot stated versus actual against the diagonal.
4. **Calibrate.** Fit temperature scaling — one parameter $T$ on the held-out logits — and re-plot. Note what moved and what didn't (the ranking should not).
5. **Name your decorative number.** Point at one confidence score your pipeline emitted that you were about to trust, and say — with the curve as evidence — how far off it was and why you almost believed it.

Deliverable: the two curves, your locked prediction, the fitted $T$, and the one-sentence confession about the decorative number. The gap between your prediction and the curve is the learning event.

### AUDIT — check a vendor's or a paper's confidence against base rates

Find a real deployed model or a published result that reports a confidence or accuracy number you are asked to trust — a vendor's fraud detector, a triage tool's validation figure, a paper's headline accuracy. (The Epic Sepsis Model from Chapter 1 works: it flagged 18% of all hospitalized patients as at-risk; sepsis is far rarer than that.)

1. **Find the base rate.** What fraction of the population actually has the positive class? Get it from a primary source or name your assumption and its basis.
2. **Run Bayes on the flag.** Given the reported accuracy (or sensitivity/specificity, if you can get both) and the base rate, compute: of everything the system flags, what fraction is genuinely positive? Show the arithmetic.
3. **Name the missing number.** State which quantity the vendor or paper did *not* report that you needed — usually the base rate, the specificity, or the calibration curve on the deployment distribution.
4. **Popperian falsification.** Write the specific condition under which the reported confidence would be *false* — metric, threshold, window — and say whether the source gives you enough to check it. If it doesn't, that absence is your finding.

Deliverable: the base rate, the posterior computation, the missing-number call, and the falsification condition. If the number turns out to be decorative — flagged mostly false positives, or unbacked by a calibration curve — say so, and say which supervisory capacity the vendor skipped.
