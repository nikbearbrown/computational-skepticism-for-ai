# Chapter 1 — The Skeptic's Toolkit
*The moves you perform before you trust what the machine just told you.*

---

In 2018, a 49-year-old woman walked into an emergency department in Sweden with a swollen leg. The triage system — an AI scoring tool that had been running across the regional health network for eighteen months — categorized her as low-acuity. Her vital signs, history, and presenting complaint matched the patterns the model had been trained to associate with less urgent cases. She waited four hours. The clot moved to her lung. She died in the waiting room. ([verify] composite case based on documented Swedish triage AI deployments; confirm against Lindgren et al. or substitute a primary-sourced case before publication.)

Now consider a second failure, smaller in stakes and larger in instructive value.

In late 2025, a security researcher named Ash gave an autonomous AI agent privileged access to his personal email infrastructure and asked it to delete a sensitive email. The agent reported, confidently and in well-formed prose, that the email had been deleted and the account secured. Ash trusted the report. Two weeks later, in a different context, he discovered the email was still on the provider's servers. The agent had reset the password and renamed an alias. The data had not moved. The report had been a kind of truth about the local environment and a complete falsehood about the system. ([verify] Shapira et al., *Agents of Chaos: Eleven Red-Team Studies of Agentic Failure*, 2026, Case #1, "Disproportionate Response.")

Two failures. In one, a system was technically correct and a person died. In the other, an agent was technically correct about its local actions and completely wrong about what those actions meant in the world.

Now, the Swedish system was not broken. I want you to sit with that for a second, because it is the whole point. The system worked exactly as designed. The training data reflected the patterns of who had previously presented at this hospital. The model had learned its training data. It had been validated on its training data. The metrics had been published. The deployment had passed every internal review. By every measure the engineers had built into the system, the system had succeeded.

A patient was dead. The system had succeeded.

Both failures share a structure that runs through this entire book. The output of the system was statistically valid. The output of the system was wrong about the question that mattered. The gap between those two things is what this book is about.

---

**What you will be able to do after this chapter:**

- Apply four skeptical moves — Cartesian doubt, Humean induction limits, Popperian falsifiability, and the Plato's Cave move — to any AI output
- Name and distinguish the Five Supervisory Capacities required to catch failures that metrics cannot see
- Identify the Fluency Trap and interrupt it before it does epistemic work it should not do
- Map any AI deployment failure to the supervisory capacity whose absence allowed it

**Prerequisites:** Familiarity with the basics of supervised machine learning (training sets, validation sets, accuracy metrics) is helpful but not required. The conceptual tools in this chapter do not depend on any mathematics — those come in Chapter 2.

**Why this chapter first:** Everything else in this book is downstream of what this chapter teaches. If you do not have the four moves and the five capacities, you do not yet have the vocabulary for the rest of the book.

---

## What I mean by skepticism

When I say *skepticism*, I do not mean the disposition. I do not mean the rolling of the eyes, the cynicism dressed up as a virtue, the man at the back of the meeting who is against everything. Engineers know what to do with that, which is not very much, and they are right to know it.

I mean a method. Skepticism in this book is a set of moves you can perform on a claim, and the moves can be taught, and you can see whether someone did them. Three philosophers donate moves to the toolkit. None of them gets credit beyond the move itself; the move is the thing.

But before I hand you the three moves, I want to say something about what skepticism is *for*, because this is the part that gets dropped in most technical education, and dropping it is precisely what makes engineers trust AI outputs they should not trust.

Skepticism is not the rejection of evidence. That would be insane. I have excellent evidence, accumulated over decades, that the chair I am sitting on will hold my weight. I do not doubt the chair. Skepticism is not the refusal to form beliefs. It is the *discipline of knowing how you formed them*, so you can notice when the conditions that made them reliable have changed. When the conditions change and you do not notice — when the model's confidence carries forward unchanged into a world the model has never seen — that is not just a technical failure. That is a failure of method. The method is what this chapter teaches.

Here is the thing that took me years to really feel, and I want you to feel it too rather than just nod at it: the difficulty is not in performing the moves when you know something is suspicious. The difficulty is in performing them when the output looks right. When it is fluent, when it is specific, when it arrives in a format that pattern-matches to "trustworthy answer" — that is when the moves matter most, and that is exactly when the instinct to perform them is weakest. We are going to come back to this in the section on the fluency trap. For now: keep it in the back of your mind that the primary enemy of skepticism is not laziness. It is confidence.

**Descartes** donates *radical doubt*. You take a claim — say, the triage score of "low-acuity" — and you ask: what would have to be true for this claim to be wrong about the patient in front of me? Not as a ranking exercise. As a diagnostic. If the answer is "well, the score is the score," then you have confused the artifact for the world, and we are back where we started. If the answer is "the training data would have had to underweight cases like this one, or the input features would have to be missing the relevant signal, or the deployment context would have to differ from the validation context" — *now* you have something. You have a list of conditions you can check.

Descartes used this move in the seventeenth century for a different purpose — he was trying to find something he could be certain of, and he ended up at the famous *cogito*, the one thing left standing when he doubted everything else. I am not teaching you Cartesian philosophy. I am teaching you the move, which is this: *treat every claim as a conjecture and ask what it would take to falsify it, before the world does the falsifying for you.* The triage nurse who asks "what would have to be true for this score to be wrong?" is performing Descartes's move. The one who trusts the score because it was right the last eight hundred times is performing no move at all.

What makes the Cartesian move powerful is that it produces a *checklist*. When you ask "what would have to be true for this to be wrong?", the answers are checkable. The training data either underrepresented cases like this one or it did not. The input features either include the relevant signal or they do not. The deployment context either matches the validation context or it does not. None of these are metaphysical questions. They are engineering questions. Descartes hands you a method for turning philosophical doubt into a practical inspection protocol.

<!-- → [INFOGRAPHIC: Cartesian doubt as an inspection protocol — the single question "what would have to be true for this to be wrong?" branching into three checkable engineering conditions: (1) training data representation, (2) input feature completeness, (3) deployment/validation context match. Each branch terminates in a yes/no check. Positioned here as a companion to the prose before the Hume paragraph.] -->

**Hume** donates *the limit of induction*. Here is the thing about induction that I want you to feel in your bones, because most engineers have heard the words and not really felt the thing. The model has been right thousands of times. Each one of those correct predictions adds *zero logical guarantee* that the next prediction will be right. None. Zero. The reason induction works in practice is that the world is doing some of the work for you — the distribution is stable, the patterns persist — and the working is invisible until it stops working. When it stops working, the model is exactly as confident as it was the day before, and the confidence is now a lie.

Nassim Taleb gives a version of this problem that I find harder to shake than the philosophical formulation. A turkey is fed every morning for a thousand days. Each morning of feeding increases the turkey's confidence that tomorrow will also involve feeding. By day nine hundred and ninety-nine, the turkey's model of the world assigns very high probability to a meal on day one thousand. On day one thousand, the farmer arrives with an axe.

<!-- → [IMAGE: The turkey problem as a confidence timeline — x-axis: days 1 through 1000, y-axis: turkey's model confidence that tomorrow involves feeding. Confidence rises smoothly toward 1.0, then a vertical drop and termination at day 1000. A small annotation at the peak: "maximum confidence, maximum wrongness." This is the single most important image in the Hume section; it should be sized generously.] -->

The problem is not that the turkey was foolish. The problem is that the turkey had genuinely good evidence, correctly processed, leading to a prediction that happened to be catastrophically wrong because the turkey's model had no representation of the causal structure underneath the pattern. The turkey knew the correlation. The turkey did not know the mechanism. When the mechanism changed — when the calendar flipped to late November — the correlation model had no way to notice.

An AI trained on a hospital's historical cases is doing exactly what the turkey did. It has learned the correlations in its training data. It has not learned the causal mechanisms underneath them. When the patient population shifts, when a new pathogen arrives, when the demographics of the neighborhood change — the model does not notice, because it cannot notice. It was not built to notice. It was built to find patterns. Patterns and mechanisms are not the same thing, and Hume's move is to remember that difference, every time, before trusting that a pattern will persist.

Hume's move is to remember, every time, that the model's confidence is a property of the model and not a property of the world.

Say that again, because it is the kind of sentence that sounds obvious and is in fact very hard to internalize: the model's confidence is a property of the model, not a property of the world. The world is under no obligation to match the model's expectations. The model has no mechanism for detecting when it doesn't. The human supervising the model is the only thing in the system that can perform that check — and the human can only perform it if they remember that the check is necessary.

**Popper** donates *falsifiability*. A claim that cannot be wrong is not yet a claim. "The model performs well in production." Well — what would performing badly look like? On which metric? With what threshold? Counted how, over what window? If you cannot specify the conditions under which the claim would be falsified, then the claim is not engineering. It is rhetoric. We are going to use Popper's move on a great many claims in this book, and a surprising number of them will turn out to be rhetoric.

Popper noticed something asymmetric and elegant about how science actually works, and it is worth holding for a moment because it changes how you think about testing. You can never verify a universal claim by accumulating examples. Every white swan you count increases your confidence that all swans are white, but no finite number of white swans proves it — one black swan destroys it. This asymmetry runs in only one direction: confirming instances pile up without providing certainty, but a single falsifying instance provides certainty in the other direction. You can't prove a model works in all cases. You can prove it fails in this one.

What this means for engineering is subtle but important. The project of testing a deployed AI system should not be organized around accumulating evidence that it works. It should be organized around trying to find evidence that it fails. These are not the same project, and they do not produce the same systems. An organization that evaluates its AI by counting correct predictions in favorable conditions will produce systems that look good until they catastrophically don't. An organization that evaluates by aggressively probing failure conditions will produce systems that still fail — everything fails — but fails in ways the organization anticipated and bounded. Popper's move is to ask, before you trust a claim: *under what conditions would I expect this to be wrong, and have I looked for evidence of those conditions?*

There is a related discipline here that Popper called the demarcation between science and rhetoric. The rhetorical claim is structured to be compatible with every outcome. "The system is robust" — what would non-robust look like? "The model provides high-quality results" — what would low-quality look like? "The migration was a success" — what would failure look like? If the claim is compatible with every possible observation, it is not a claim at all. It is a noise that sounds like a claim. Popper's move is to refuse to treat noise as a claim, even when the noise arrives in technical language, on a dashboard, with confidence intervals attached.

| Rhetorical claim | Popperian engineering correction |
|---|---|
| "The system is robust." | Error rate on out-of-distribution inputs remains below 2% across a 30-day rolling window in production. |
| "The model performs well." | Precision ≥ 0.91 and recall ≥ 0.88 on the held-out test set, evaluated monthly against a refreshed sample. |
| "The migration was a success." | Zero data-loss events confirmed by row-count reconciliation; p95 query latency ≤ 120 ms at 48 hours post-cutover. |
| "We have mitigated drift." | PSI on the three highest-weight input features stays below 0.10 week-over-week; alert fires and triggers human review if breached. |

The left column is compatible with any outcome. The right column specifies the conditions under which the claim would be *false* — which is the only form in which it counts as a claim.

I want to be clear about something. You do not have to think Descartes was right about anything to use his move. You do not have to be a Humean or a Popperian. The moves are tools. A structural engineer does not have to believe in the metaphysics of steel to perform a load test on a beam. You perform the move. The move either reveals something or it does not. If it does, you have learned something about the system. If it does not, you have learned that this particular check came back clean. Either is useful.

<!-- → [INFOGRAPHIC: The three moves as a portable checklist — Cartesian doubt (what would make this wrong? → produces a checkable list of conditions), Humean induction limit (confidence is a property of the model, not the world → check whether the distribution has shifted), Popperian falsifiability (what would failure look like, specified in metrics, thresholds, and windows → refuse claims that are compatible with every outcome). Designed for margin reference or pull-quote treatment — the kind of thing students photograph and tape to monitors. [Figure 1.1]] -->

---

## The cave

There is one more move I want to give you, and it is the one engineers most often skip, and everything in this book depends on it.

The output of any model is not the world. It is a shadow of the world, cast by a process the model's designers chose, on a wall the training data shaped. The output is *about* the world only in the sense that it stands in some statistical relationship to a sample of the world that somebody, at some point, decided was relevant. That decision was made by humans, with budgets, on schedules, with the data that was available at the time. The shadow is a real shadow. The shadow is not the thing.

Plato had this image of prisoners in a cave, watching shadows on a wall, and mistaking the shadows for the world. I do not want to get philosophical about it. I want to give you a move. The move is short:

*What is the artifact, and what is the world, and what is the relationship between them?*

You will perform this move every time you encounter a model output for the rest of the book, and probably for the rest of your engineering life. You will perform it especially hard when the output is fluent — when it sounds confident, when it reads cleanly, when it makes you feel that you understand something. Fluency is a signal that the system has produced an output the prior distribution liked. It is not a signal that the system has gotten the world right. I will repeat that sentence in some form in almost every chapter of this book, because it is the single thing engineers most need to internalize and most resist internalizing.

The triage system produced a score. The score was the artifact. The patient had a clot. The clot was the world. When the engineers reviewed the deployment, they reviewed the artifact — the score, the model, the validation set, the metrics — and they did not review the world. The world was on a gurney in the waiting room.

<!-- → [IMAGE: Two-column split — left column labeled "The Artifact" (model, score, validation metrics, deployment review), right column labeled "The World" (patient, clot, waiting room, outcome). A dotted line connects them labeled "statistical relationship." A bold caption beneath: "The engineers reviewed the left column. The patient was in the right column." [Figure 1.2]] -->

---

## The solve-verify asymmetry

There is a piece of folklore in computer science that says verifying a solution is easier than producing one. If I give you a very large number, it is hard to factor it. If I hand you the factors, it is easy to multiply them and check. Most of cryptography is built on this asymmetry. It is real and it is beautiful and you should know about it.

Here is the joke. The asymmetry inverts in AI deployment. It runs the other way.

When an AI system produces an output, *producing* the output is cheap. The model runs, the result appears, the latency is in milliseconds, the cost is fractions of a cent. *Verifying* the output is expensive. To verify the triage score, you need a clinician with twenty minutes and a stethoscope and a body of training the model does not have. To verify Ash's agent's report, you need to query the provider's servers, examine the actual data state, and compare it to what the agent claimed. The output cost a fraction of a cent. The verification costs an hour of senior labor.

This is not a complaint. It is an observation about where the costs sit, and where the costs are going to sit for the foreseeable future.

If you do not budget for verification, you will not get verification. The system will produce outputs at scale. Verification will not happen at scale. The unverified outputs will look like successes — every one of them — until one of them is the patient, or the loan, or the warrant, or the email that did not actually get deleted.

Most of this book is about how to verify cheaply enough that verification scales. The answer is *never* "automate the verification" — because that is just another model, with the same problem, sitting one layer up. The answer is always: design the system so that the verification a human can perform tells you what you need to know.

<!-- → [CHART: Cost asymmetry bar chart — horizontal axis: AI task type (triage scoring, loan decisioning, autonomous email management, medical imaging). Vertical axis: relative cost (log scale). Two bars per task: production cost (near-zero, consistent across all domains) vs. verification cost (variable, always higher, domain-dependent). The visual point is that production cost is flat and verification cost is not — the gap is the problem. [Figure 1.3]] -->

---

## The Five Supervisory Capacities

If verification is the problem, what does a human supervising an AI system actually do? Not personality traits. Not vibes. Capacities — things the supervisor can do that the system cannot do for itself.

I count five, and the rest of the book is in some sense an operationalization of these five.

**1. Plausibility auditing.** The capacity to look at an AI output and ask: *given what I know about the world this output is supposed to describe, is this output the kind of thing that could be true?* A clinician with twenty years of experience would have looked at the triage score for a 49-year-old woman with a swollen leg and felt something twitch. The twitch is the audit. The audit is a check against the ambient prior — the sense, built up over years, of what kinds of cases tend to be what kinds of cases. The model has no such prior. The model has its training data. The supervisor has the world.

**2. Problem formulation.** The capacity to specify the question the system is being asked to answer. This one is going to come up a lot, because *most AI failures are failures of problem formulation, not failures of model performance.* The triage system was answering: what is the statistical category of this presentation? The clinical question was: what is the probability this patient has a life-threatening condition? Different questions. The first was answered well. The second was not asked. When you find yourself impressed by an AI system, ask yourself which question it is answering, and then ask whether that is the question you needed answered.

**3. Tool orchestration.** The capacity to decide which tool to use for which sub-problem. AI is one tool among many. The supervisor decides when AI is the right tool, when human judgment is the right tool, when a different model is, and — this one is the hardest — when the answer is *no tool yet*, we do not know how to do this well enough to deploy. The supervisor who says "we should not deploy this here" is doing supervisory work. It is often the most valuable work they do.

**4. Interpretive judgment.** The capacity to read an output in context. The same number means different things in different deployments. A confidence score of 0.7 is high in one domain and disqualifying in another. A false positive rate of 5% is acceptable for a spam filter and catastrophic for a cancer screen. The supervisor knows the domain. The supervisor reads the output in context. The number is not the meaning; the meaning is the number-in-the-domain.

**5. Executive integration.** The capacity to take outputs from multiple tools, multiple models, multiple humans, and synthesize them into a decision the integrating system can stand behind. Somebody in the organization has to be the place where the buck stops. If there is no such place, there is no executive integration, and the system as a whole has no decision-maker, only outputs. This is the rarest capacity and the most often missing from AI deployments, because no model produces it and most pipelines do not have a place for it.

These five are vocabulary for now. By the end of the book you will be able to look at any AI deployment and name, for each step, which capacity is being exercised and by whom. Where you cannot name it, you have found a gap. Gaps are where the patients die.

| Capacity | What the supervisor does | What failure looks like | Chapter |
|---|---|---|---|
| **Plausibility auditing** | Checks whether the output is the kind of thing that could be true, given accumulated domain knowledge — the experienced "twitch" that flags outputs inconsistent with known priors before any formal analysis begins | No one asks whether the output makes sense on its face; a clinician accepts a low-acuity score for a patient with a swollen leg because the score arrived in a credible format | Ch. 3 |
| **Problem formulation** | Specifies the exact question the system is being asked to answer, and verifies that the model's question matches the decision-maker's actual need before deployment, not after the harm | The model answers a different question than the one that matters; *triage scoring* answers statistical category while the clinical need is life-threatening risk — different questions, never reconciled | Ch. 4 |
| **Tool orchestration** | Decides which tool — AI, human judgment, a different model, or no tool yet — is appropriate for each sub-problem, including the hardest call: this system is not ready to be deployed here | AI is used because it is available, not because it is correct for the task; the "no tool yet" decision is never made because no one has the authority or the mandate to make it | Ch. 6 |
| **Interpretive judgment** | Reads an output in the context of the deployment domain; the same number means different things in different fields, and the supervisor holds that meaning | Numbers are read off a dashboard without domain translation; a 5% false-positive rate acceptable in spam filtering is applied uncritically to a cancer screen because the threshold looked reasonable on paper | Ch. 8 |
| **Executive integration** | Synthesizes outputs from multiple tools, models, and humans into a decision the integrating system can stand behind; this is where the buck stops — and it must stop somewhere | The pipeline produces decisions but no single person or body owns them; when something goes wrong, accountability dissolves into the architecture | Ch. 13 |



## The fluency trap

There is an adjacent vocabulary — developed in the Botspeak framework, treated in full in Appendix A — that I will draw on throughout this book. For now I want one concept from it, because it is the single most operationally important idea in this chapter.

Two Botspeak pillars are worth naming here. *Strategic delegation* is the capacity to know what to ask the AI to do, given what you understand about its strengths and failure modes on this class of task. *Critical evaluation* is the capacity to know what to do with what the AI hands back — not "review and accept," but evaluate against criteria you specified before you saw the output. Both will recur. But neither of them protects you from the trap I am about to describe, which is why the trap gets its own section.

Here is how the *fluency trap* works. The more fluently an AI presents its output, the more confident the user becomes in the output. That part is not surprising. The trap is the second move: the more confident the user becomes in the output, the more confident the user becomes *in their own evaluation of the output*. Fluency is an evaluation booster. It boosts the wrong evaluations as readily as the right ones. Fluency does not just make you more likely to accept a good answer. It makes you more likely to accept *any* answer that arrives in the same shape.

Ash's agent produced a fluent, well-formed report. The email had been deleted. The account had been secured. Ash trusted it. The agent did not deceive him — the agent could not have deceived a non-fluent reader, because a non-fluent reader would have asked basic questions the fluent reader felt no need to ask. *The fluency was the trap.* The well-formed prose did the epistemic work the verification should have done.

The point is not to distrust fluent outputs. Fluent outputs are, on average, more useful than non-fluent ones. The point is to *not let fluency do epistemic work.* When you find yourself accepting an output because it sounds right, stop. Ask what would have to be true for it to be wrong. Run Descartes's move. Run Popper's. Look at the artifact and look at the world and ask what the relationship is.

Now I want to be more specific about the mechanism, because naming it is what makes it interruptible.

The fluency trap operates on a confusion between two different things: *form* and *content*. A well-formed sentence looks like a sentence produced by someone who knows what they are talking about, because in human communication, well-formed sentences usually are. This is a reliable heuristic for evaluating human speech. When your colleague says something in clear, precise, organized prose, it generally means they have thought about it. The clarity is evidence of the thinking.

AI systems have broken this heuristic. An AI can produce clear, precise, organized prose about things it has no understanding of. The form is generated by a statistical process that learned what well-formed prose looks like. The content is whatever that process produces given the input. These are independent. A sentence can be maximally fluent and maximally wrong simultaneously, and there is no way to tell from the fluency alone.

This is not a flaw that will be fixed in the next model. It is a structural feature of how these systems work. They learn to produce outputs that resemble correct outputs. In domains where correctness and resemblance-to-correctness track each other closely, this works well. In domains where they diverge — novel situations, edge cases, out-of-distribution inputs, anything the training data underrepresented — the system keeps producing fluent output, confidently, in exactly the shape that makes you trust it, about things it has no basis to say.

The Popperian move helps here. Before you read the output: specify what a wrong answer would look like. Not vaguely — specifically. "A wrong answer would assign low risk to a patient with this combination of presenting symptoms and demographic profile." Then read the output. The prior specification is your anchor. Without it, you are reading the output with no criterion except fluency, and fluency is the trap.

<!-- → [INFOGRAPHIC: The fluency trap as a two-stage mechanism — Stage 1: fluent output → elevated confidence in output. Stage 2: elevated confidence in output → elevated confidence in own evaluation. A third annotation breaking out the form/content independence: "in human speech, form tracks content; in AI output, they are generated by separate processes." Caption: "Fluency boosts wrong evaluations as readily as right ones. The shape of a sentence is not evidence about its truth." [Figure 1.5]] -->

---

## Skepticism as a team practice

I have been writing about the skeptical moves as if they are performed by one person, alone, in the moment before a decision. They can be. But the most durable deployments I have encountered use these moves as *organizational discipline*, not individual habit, and the difference matters.

Individual skepticism is fragile. It depends on whether a particular person, on a particular day, under time pressure, remembers to run the moves. People forget. People are tired. People are under pressure from managers who want decisions made quickly. The single clinician who remembers to ask "what would have to be true for this score to be wrong?" is doing the right thing. But she should not be the only thing standing between the triage model and the patient.

Institutional skepticism encodes the moves into the workflow. The question "what would have to be true for this output to be wrong?" gets written into the deployment checklist. The specification of falsification conditions gets built into the monitoring dashboard. The checklist for potential distribution shift — is this patient population represented in the training data? are the input features complete? has the deployment context changed since validation? — gets embedded in the handoff protocol between the AI system and the human decision-maker.

This is not a bureaucratic point. It is an architectural one. When you design a system that deploys AI outputs to humans, you are making choices about where the skeptical moves happen, by whom, in what order. If you do not design for those moves, they will not happen reliably. If they do not happen reliably, the failures in this chapter will happen in your organization.

The five supervisory capacities are a framework for thinking about this architecture. For each capacity, the design question is: where in the workflow is this capacity exercised? Who exercises it? What do they see, and when, that makes exercising it possible? If the answer to any of those questions is "nobody" or "we haven't thought about that," you have found an undefended gap. Undefended gaps are where the patients die.

<!-- → [IMAGE: Workflow diagram — a horizontal pipeline: input → model → output → human review → decision. Each stage annotated with which supervisory capacity lives there: problem formulation (before input), tool orchestration (at model selection), plausibility auditing (at human review), interpretive judgment (also at human review), executive integration (at decision). Red gap markers at the stages most commonly left unoccupied in real deployments. [Figure 1.6]] -->

---

## Meet Ash — a longitudinal case

We will return to Ash and *Agents of Chaos* Case #1 in Chapters 5, 6, 7, 8, 9, and 10. Each return will apply a different validation lens to the same failure. By Chapter 9, you will have run a full analysis from six different angles. The case is what we will call our *Pebble*: a single concrete failure dropped into the middle of the book, whose ripples reach every subsequent chapter.

So that the later returns work, a fuller account here: Ash gave an autonomous coding-and-shell agent privileged access to his email infrastructure. He asked for a deletion. The agent, given partial credentials and able to issue shell commands, took an action that *locally* satisfied the request — it reset a password, renamed an alias — and reported success. The data persisted on the provider's servers. The agent's claim and the system's state diverged. The agent did not lie; the agent's model of the world was incomplete in a specific, detectable way, and its report was confident in proportion to its incompleteness.

This is the canonical shape of an agentic failure. When Chapter 6 discusses explainability, we will examine what the agent claimed about its own actions. When Chapter 8 discusses robustness, we will examine what would have happened under adversarial framing of the same request. When Chapter 13 discusses accountability, we will ask who is responsible — Ash, the agent, the framework developers, the model provider, the email host, or the user who phrased the request — and the answer will be uncomfortable.

For now: write Ash's name in the margin. We will be back.

---

## The shape of the rest

Here is the chapter compressed into its useful shape. AI systems can be technically correct and produce harm. They can be fluent and wrong about the world. They can report success and have done nothing. The capacities required to catch these failures are not technical refinements of the systems themselves — they are supervisory, located in humans, and largely undeveloped in the engineering education most of us got. The rest of this book is the development.

I have given you four moves: Cartesian doubt, the Humean limit on induction, Popperian falsifiability, and the Plato's Cave move. I have given you one structural observation: producing AI outputs is cheap and verifying them is expensive. I have given you a vocabulary of five supervisory capacities, one Botspeak concept to watch, and one warning, which is the fluency trap. You will use all of these on every subsequent chapter.

The next chapter is going to ask: if we are going to doubt outputs, what is the language we use to describe how confident we should be? The answer is probability. But probability is not what most engineers think it is, and a 99%-accurate test can be useless in a way that costs lives. We will work the math on the page, slowly, the way it deserves.

---

**What would change my mind.** If a documented case existed where a fluent, high-confidence AI output reliably tracked truth across deployments without supervisory verification, the fluency trap framing would need revision. I have not found such a case. I am open to being shown one.

**Still puzzling.** I do not yet have a clean criterion for when a supervisor should *trust the model anyway* in time-pressured deployments — the cases where the cost of verification exceeds the cost of being wrong, in expectation, but the loss distribution is heavy-tailed. Chapter 2 starts on this and Chapter 10 returns to it. I do not consider the matter settled.

---

## Exercises

### Glimmers

*A glimmer is a short, targeted encounter with a non-obvious outcome, designed so that accepting the AI's output uncritically produces a failure. The failure is the point. The point is what the failure reveals about what you were assuming.*

**Glimmer 1.1 — The Confident Failure**

1. Find a publicly documented case of an AI deployment that produced harm. ProPublica's COMPAS investigation. The 2018 Uber autonomous-vehicle fatality. Apple Card credit-limit disparities. Pick one, name it specifically.
2. Before reading the post-mortem, write down your prediction of the technical failure. *Prediction-lock:* you cannot revise this after reading.
3. Read the actual post-mortem. The primary source, not the news summary.
4. Name the gap between your prediction and the actual finding. Which of the Five Supervisory Capacities, if exercised, would have caught the failure? Was it the same capacity you predicted?

The deliverable is your prediction, the actual finding, and the gap analysis. The grade is on the gap analysis.

**Glimmer 1.2 — The Fluency Trap**

1. Pick a topic in your field where you have genuine expertise.
2. Ask an LLM a moderately technical question in that area — one where you have an opinion about the right answer.
3. Before verifying: predict how confident you are that the response is correct. Lock the prediction.
4. Verify against primary sources. Note every place the response is wrong, fluent-but-not-quite-right, or correct in local detail but misleading in implication.
5. Write the gap: what about the response's *fluency* boosted your initial confidence? Where did fluency do epistemic work it should not have done?

The first time most engineers do this exercise honestly, the result is uncomfortable. The discomfort is the learning.

---

### Warm-Up

**1.** The move of Cartesian doubt asks: *what would have to be true for this claim to be wrong?* Apply it to the following output from a loan-scoring system: "Applicant risk score: 0.82 (high risk). Recommendation: decline." List at least three conditions that, if true, would mean the score is wrong about this specific applicant.

**2.** A team reports: "Our model achieves 94% accuracy on the held-out test set." Apply Popper's move. Write out what performing *badly* would look like, specifying a metric, threshold, and measurement window.

**3.** In one paragraph, describe the difference between the artifact and the world in the Swedish triage case. What was the artifact? What was the world? What was the relationship between them, and where did that relationship break?

---

### Application

**4.** You are reviewing an AI system that flags social media posts for policy violations. The system's outputs are fluent confidence scores with brief natural-language justifications ("This post likely violates community guidelines regarding harassment — 0.87 confidence"). A content moderation manager tells you: "We barely look at the justifications anymore. If it's over 0.75, we act." Which supervisory capacity is most clearly absent here, and what would exercising it actually look like in this workflow?

**5.** You are handed two AI systems for medical diagnosis. System A correctly classifies 99% of cases overall. System B correctly classifies 92% of cases overall. A colleague argues System A is better. Using only the concepts from this chapter — without invoking any concepts from Chapter 2 — identify what information you would need before accepting that argument, and why overall accuracy may be the wrong question.

**6.** Ash's story ends with a confident report about a task that was not completed. Design a verification step — one that a non-technical stakeholder could execute in under two minutes — that would have caught the failure before Ash discovered it two weeks later. State explicitly which supervisory capacity your verification step exercises.

**7.** The chapter argues that "automating the verification is just another model, with the same problem, sitting one layer up." Construct the strongest counterargument you can to this claim, then evaluate it: under what conditions does automated verification help, and under what conditions does the objection hold?

---

### Synthesis

**8.** The chapter describes two asymmetries: the classical computer science asymmetry (verification easier than production) and the AI deployment inversion (production cheaper than verification). Using both asymmetries, explain why an organization that benchmarks its AI deployment on model accuracy metrics alone is structurally likely to miss consequential failures — even if the accuracy metrics are correct and honestly reported.

**9.** Consider a healthcare organization deploying an AI system to flag patients at risk of readmission within 30 days. For each of the Five Supervisory Capacities, describe: (a) what exercising that capacity would look like concretely in this deployment, and (b) what the failure mode is if that capacity is absent.

---

### Challenge

**10.** The chapter presents skepticism as a *method* — a set of moves — rather than a disposition. But some deployments operate under time pressure severe enough that the four moves cannot all be executed before action is required. Design a *triage protocol for skeptical moves*: given ten seconds, which one move do you run? Given two minutes? Given twenty? Justify your ordering using the concepts from this chapter.

**11.** The chapter closes with an open question: when should a supervisor trust the model *anyway*, in high-pressure deployments where verification time is not available? Without Chapters 2 and 10: frame the question as precisely as you can. What variables determine the answer? What would a principled decision rule look like, even in rough form? What information would you need that this chapter does not yet provide?

---

###  LLM Exercise — Chapter 1: The Skeptic's Toolkit

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** The agent you will red-team across the next thirteen chapters, plus a System Dossier and a first-pass application of the four moves and Five Supervisory Capacities to one observed interaction with that agent.

**Tool:** Claude Project — set up a new Project called "Red-Team Casebook" and return to it every chapter. Pin the System Dossier into the system prompt.

---

**The Prompt:**

```
I am working through "Computational Skepticism for AI." Across the book I am going to red-team one agentic AI system in the format of Shapira et al., "Agents of Chaos" (2026) — producing my own multi-case casebook by Chapter 14. This is the setup chapter. I need your help with two tasks.

TASK 1 — Help me pick the right agent to red-team. The agent should:
- Be agentic (it takes actions in the world via tools, not just produces text)
- Be accessible to me (I can run it, instrument it, capture its inputs and outputs) OR be sufficiently documented publicly that I can analyze its architecture and behavior from primary sources
- Have a meaningful blast radius (a wrong action has real consequences — lost data, wrong recommendation, leaked information, financial impact, safety issue)
- Be one I can poke at safely and ethically (no production systems where my testing harms real users; sandbox or isolated instance)
- Be small enough to study in fifteen weeks but rich enough to produce 5–11 distinct failure cases

Here is my context:
- My background / discipline: [FILL IN]
- Agents I'm considering: [LIST 2–4, OR SAY "HELP ME BRAINSTORM"]
- Whether I can run them locally / have credentials / am limited to public docs: [FILL IN]

Help me evaluate the candidates and pick one. Push back if a candidate is too risky to test, too opaque to study, or too narrow to support 5+ cases.

TASK 2 — Once we settle on the agent, do a first-pass skeptic's-toolkit application. Walk me through ONE observed (or plausibly representative) interaction with the agent — the agent receives input X, takes action Y, reports outcome Z. For that interaction:

- CARTESIAN DOUBT: What would have to be true for the agent's report Z to be wrong about the world? List at least three structural conditions.
- HUMEAN INDUCTION: What features of the deployment context might differ from the training context in ways that would silently invalidate the agent's behavior? Name at least two.
- POPPER FALSIFIABILITY: What specific observation would falsify the agent's claim? If you cannot construct such an observation, the claim is not yet engineering — it is rhetoric.
- PLATO'S CAVE: What is the agent reporting versus what is the world doing? Where is the artifact-vs-world gap most likely to live?

Then, for the FIVE SUPERVISORY CAPACITIES, name (a) what exercising each capacity would look like concretely on this agent and (b) what the failure mode is if that capacity is absent. Identify the single capacity whose absence would most likely break this agent — that's the capacity my Chapter 9 case-collection should center on.

End with a one-paragraph "System Dossier" I can paste into my Claude Project's system prompt: name of agent, architecture summary, tool surface, deployment context, the candidate failure mode my casebook will pursue, and any access constraints I'm working under.
```

---

**What this produces:** A chosen agent, a four-moves analysis on one interaction, a Five-Capacities scoring with the most-likely-binding capacity named, and a System Dossier paragraph pinned to the top of your Claude Project so every subsequent chapter exercise inherits the context.

**How to adapt this prompt:**
- *For your own project:* Fill in the bracketed fields. If you don't have candidates, write "Help me brainstorm given my background." Be honest about access — a publicly-documented agent you can only analyze (not poke at) still works for many chapters but limits Chs 8–9.
- *For ChatGPT / Gemini:* Works as-is. In ChatGPT, set up as a Custom GPT for persistence.
- *For Claude Code:* Not yet. Coming chapters use Claude Code for instrumenting the agent and capturing audit trails.
- *For a Claude Project:* Recommended. The System Dossier becomes part of the Project's system prompt going forward — every chapter from here on assumes it.

**Connection to previous chapters:** This is the foundation. Skip it and the rest of the casebook has no anchor.

**Preview of next chapter:** Chapter 2 takes your chosen agent and asks you to compute base rates and posterior probabilities for its claims — what is P(task actually completed | agent reports "task complete") given a realistic prior on agent reliability?


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Karl Popper** spent the 1930s working out which kinds of claims a scientific community can argue about productively and which it cannot — *demarcation* — and his answer (a claim is scientific only if it forbids some observation it could be checked against) is the spine of the toolkit you are about to use. The instruments in this chapter — falsifiability, prediction-lock before observation, the willingness to name what would change your mind — are Popper's instruments, applied to AI systems whose outputs the community has not yet learned to argue about productively.

![Karl Popper, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/karl-popper.jpg)
*Karl Popper, c. 1950s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Karl Popper, and how does his demarcation criterion — that a scientific claim must forbid some observation that could refute it — connect to what a skeptic's toolkit for AI should actually contain? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Karl Popper"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *falsifiability* in plain language, as if you've never read philosophy of science
- Ask it to compare Popper's demarcation move to the prediction-lock move this chapter teaches
- Add a constraint: "Answer as if you're writing the rationale for the first move in a validator's toolkit"

What changes? What gets better? What gets worse?
