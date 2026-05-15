# Chapter 14 — The Limits of AI: What the Tools Cannot Do
*Three things capability scaling cannot fix, and what the supervisor does about them.*

## Learning objectives

By the end of this chapter, you will be able to:

- Name the three categorical limits of AI systems — meaning, intentionality, and the data-world gap — and explain why capability scaling does not close them
- State what Turing's argument actually claims and what it does not, and do the same for Searle's Chinese Room
- Identify which deployments require skepticism as a safety mechanism versus skepticism as methodology, and specify the criteria that distinguish them
- Design the five components of an engineering practice for high-stakes deployments where the categorical limits bite
- Explain why the supervisor's authority to refuse deployment is the most important structural authority in the system
- Compare AI's cognitive profile against the capacities documented in this book — identifying where AI is genuinely strong, where it is structurally weak, and where it is absent — and use that profile to determine appropriate delegation
- Apply the full validation apparatus from across this book to a specific deployment and stake a position you can defend

## Prerequisites

The entire book. This chapter is the culmination. Chapter 2's calibration baseline runs here for the third and final time. Chapters 5, 8, and throughout — the three categorical limits are the structural statements of what those chapters were operational versions of. The extended-mind framing developed here is the leitmotif of the book, named explicitly for the first time.

---

## Why this chapter

Every prior chapter has built technical apparatus for validating AI systems. This chapter names the limits beyond which that apparatus cannot reach, specifies the engineering practices those limits demand, and asks you to use everything the book has given you on a specific case and stake a position you can defend.

---

## The model that passed every test and failed in deployment

I want to tell you about a system that passed every test the engineers gave it.

It was a clinical decision-support system, deployed in a regional health network. On its validation set, it achieved ninety-four percent accuracy. It met every internal review threshold. It cleared regulatory submission. The fairness metrics were within tolerance. The robustness analysis showed acceptable behavior under perturbation. The communication apparatus was in place. The accountability framework was documented. By every measure the engineers had specified, the system was ready.

The system went live. Within six months, three patients were harmed by recommendations the system made and the clinicians accepted.

The post-mortem found something I want you to feel the strangeness of, because the strangeness is the lesson. The system was tested on the question it was built to answer — *does this presentation match a category in the training data?* The harms came from a different question — *what is going on with this specific patient?* The two questions are related, but they are not the same. The system's accuracy on the first question was real. Its inability to answer the second question was structural, in the sense that *the system was never built to answer it*. And the validation framework did not surface the gap, because the validation framework was scoped to the first question.

The system passed every test the engineers designed. The engineers designed the wrong tests. The wrongness was not negligence. It was something deeper — a *categorical limit on what the system could be tested for*, given what the system was. The validator's job, looking back, was to recognize the limit and decide whether the deployment should proceed in its absence. The validator had not been trained for this recognition.

That is the training this chapter is for.

---

## Three categorical limits

There are three structural limits that bound what current AI systems can do, regardless of capability scaling. Each demands a specific engineering practice from the supervisor.

| Limit | What it means | Why capability scaling doesn't fix it | Operational consequence for the supervisor |
|---|---|---|---|
| **Meaning** | The system processes symbols; the symbols' referents in the world are supplied by the user, not the system | Scaling increases pattern breadth and fluency; it does not give the system access to the world its symbols refer to | The supervisor performs semantic work: mapping outputs to their referents in the deployment context |
| **Intentionality** | The system's outputs do not carry stable directedness across deployments; the "aboutness" tracks the user's reading, not an independent stable directedness | More capable systems produce more contextually appropriate responses, but the context-sensitivity is itself statistical, not directed | The supervisor treats outputs as evidence to be interpreted in context, not statements with fixed referents |
| **Data-world gap** | The system's competence is over the data, not the world; the data is always less than the world; gaps are structurally unlearnable from within the training set | More data widens the distribution covered, but the structural gap — the parts of the world not in the data — cannot be covered by data that is not there | The supervisor specifies the deployment distribution, monitors for shift, and overrides when the deployment exits the data's coverage |

*These three limits are structural, not contingent. They are not obstacles to be engineered around. They are the reason the human supervisor exists.*

**Limit 1: Meaning.** The system processes symbols. The symbols have referents in the world. The system has no representation of the referents. It manipulates the symbols; the meaning of the symbols — what they refer to in the world the user inhabits — is supplied by the user, not the system.

This is contested. There is serious literature arguing that contemporary large multimodal models acquire something like meaning through embedding structure and grounding via diverse modalities. [Verify: Bender et al. 2021 stochastic-parrots framing; Chalmers 2023 on consciousness and large language models; Searle 1980, *Minds, Brains, and Programs*.] I do not consider that question settled. But the contestation does not need to be resolved for the operational consequence to bind. *The system's behavior is inconsistent with the user's expectation of meaning often enough that the supervisor has to perform meaning-attribution for the system, and the supervisor cannot offload that work to the system itself.*

When the system's picture of the world and the user's picture of the world align, the deployment looks fine. When they come apart — at the boundary of the data, at the edges of the training distribution, in cases the system has never seen — the user is still reading the output as a statement about the world, and the system is still producing symbols. The gap between those two activities is the failure mode.

The engineering practice: *the supervisor does the semantic work*. When the system produces an output, the supervisor maps the output's symbols to their referents in the deployment context. When the system answers a question, the supervisor checks whether the answer is responsive to the question the user asked, not just the question whose symbols the system processed.

**Limit 2: Intentionality.** Intentionality, in the philosopher's sense, is *aboutness* — a thought is about something in the world; an utterance is directed toward something. The system produces outputs. The outputs do not, in any obvious sense, carry stable directedness. The system does not have intentions in the directed-toward sense; it has parameters and inputs and outputs. Two deployments of the same system, in different contexts, produce outputs the user reads as being about different things. The system's "aboutness" tracks the user's reading — it does not track an independent stable directedness.

This too is contested. Some readings of agentic systems argue that goal-pursuit is functionally equivalent to intentionality. Whether functional equivalence captures what intentionality is supposed to capture is a deep question I am not going to settle here. The operational consequence binds regardless: *the system's outputs do not carry stable referents across deployments, and the supervisor must supply the directedness.*

The engineering practice: *the supervisor treats the system's outputs as evidence to be interpreted in context, not as statements with fixed referents*. The interpretation is the supervisor's job. The system supplies the symbols; the supervisor supplies the directedness.

**Limit 3: The data-world gap.** The system is trained on data. The data is a sample of the world, captured by particular instruments, under particular conditions, with particular exclusions. The system's competence is over the data, not the world. *No amount of data scaling closes the gap*, because the gap is structural — the data is always less than the world, and the parts of the world not in the data are not learnable from the data.

This is the limit I am most certain of, and it is not contested the way the first two are. It is sometimes obscured by the claim that "with enough data, the model can generalize" — which is true within a distribution and false at the boundary. The boundary is where the gap lives. The boundary is where AI systems most often fail.

You have met this limit before, in different clothes. It was Hume's induction problem in Chapter 2. It was the access-boundary failure in Chapter 5. It was distribution shift in Chapter 8. The categorical statement — the data is always less than the world — is what all those operational versions are operational versions of.

The engineering practice: *the supervisor specifies the deployment distribution, monitors for distribution shift, and is prepared to override or reject the system's outputs when the deployment is operating in a region the data does not cover.*

Nassim Taleb gave the data-world gap a sharper shape than most engineering treatments do, and the framing is worth importing. In *The Black Swan* (2007), Taleb distinguished two kinds of data-generating worlds. *Mediocristan* is the world where outliers do not dominate the average — human heights, exam scores, the time it takes to walk to work. Sample one more observation in Mediocristan and the running statistics barely move. *Extremistan* is the world where outliers do dominate — wealth, financial returns, casualty counts in war, downloads of an app, fatalities from a single deployment failure. One observation can be larger than every prior observation combined. The two worlds require different epistemic stances. Mediocristan rewards averaging. Extremistan punishes it.

Taleb's "turkey problem" makes this concrete in a way the abstract distribution-shift literature rarely does. A turkey is fed every day for one thousand days. Every day, the available evidence supports the model that the human cares about the turkey's welfare. By the metrics that matter to the turkey — caloric intake, shelter, predator absence — confidence in the model rises monotonically. On the morning of day 1,001, the model fails catastrophically. The training distribution was Mediocristan-shaped (a smooth daily routine); the actual world contained a Black Swan event (Thanksgiving) that no amount of in-distribution data could anticipate.

Apply this to AI validation directly. A system tested on ten thousand routine cases with 99.7% accuracy may still be a turkey. The relevant question is not what the accuracy is on the cases the system has seen — it is whether the cases the system has not seen are drawn from a Mediocristan distribution (where high accuracy on the seen cases predicts high accuracy on the unseen ones) or an Extremistan distribution (where the rare events dominate the consequence and the model has no claim on them). The supervisor's job is to know which world the deployment lives in. Most high-stakes deployments live in Extremistan, even when the routine traffic looks like Mediocristan.

---

## Turing and Searle — what each argument settles, what each does not

Two famous arguments about AI limits. Each gets cited a lot and understood less than it should be.

**Turing's argument (1950).** [Verify: Turing 1950, *Computing Machinery and Intelligence*.] If a machine can convincingly imitate a human in conversation, by what principled basis would we deny it intelligence? The argument is operationally elegant: *behavior is the testable evidence; behavior consistent with intelligence warrants the attribution.* It settles a methodological question — don't require something more than behavioral evidence for intelligence in machines, because we do not require something more for other humans.

What Turing's argument does not settle: whether the entity satisfying the test has *meaning* (Limit 1), *intentionality* (Limit 2), or the kind of competence over the world (Limit 3) that the test implicitly assumes. The test is over behavior. The limits are about what stands behind behavior. Turing himself, I think, knew this. The test was a methodological proposal, not a metaphysical claim. People who cite Turing as having shown that behavioral imitation *is* intelligence are giving him credit for a stronger claim than he made.

**Searle's argument (1980).** A person who does not speak Chinese is in a room with a rulebook. Slips of paper come in through a slot with Chinese symbols. The person follows the rules and produces Chinese symbols on slips that go out. To a Chinese-speaking observer outside, the inputs and outputs are indistinguishable from those of a Chinese speaker. The person does not understand Chinese. *Therefore symbol manipulation is not understanding.*

The argument settles a conceptual question: behavior consistent with understanding does not entail understanding. What it does not settle is whether contemporary systems are doing only symbol manipulation — or whether embedding structures, attention patterns, and multimodal grounding constitute something more. Searle's argument is a strong constraint on shallow accounts of meaning. It is not a deep constraint on what current architectures might be. People who cite Searle as having shown that AI systems *cannot* understand are giving him credit for a stronger claim than he made.

| Argument | What it actually claims | What it does NOT claim | Common misreading |
|---|---|---|---|
| **Turing (1950) — Imitation Game** | Behavior consistent with intelligence warrants the attribution; requiring more than behavioral evidence for machines is unprincipled, since we don't require more for other humans | That behavioral imitation IS intelligence; that a Turing-passing system has meaning, intentionality, or world-competence | "Turing proved AI can be intelligent" — he made a methodological claim, not a metaphysical one |
| **Searle (1980) — Chinese Room** | Behavior consistent with understanding does not entail understanding; symbol manipulation is not sufficient for semantics | That contemporary AI systems are necessarily doing only symbol manipulation; that the argument forecloses grounding via embedding or multimodal training | "Searle proved AI cannot understand" — he showed sufficiency fails; he did not establish necessity |

*Both arguments are important and both are regularly overclaimed. The validator who only tests behavior misses the limits; the validator who only invokes the limits skips the testing. The job is to do both.*

The two arguments together produce a useful operational stance: *behavior is testable evidence and should be taken seriously — and behavior is not the whole of what we mean by understanding, meaning, or intentionality.* Both moves at once. The validator who only tests behavior misses the limits. The validator who only invokes the limits skips the testing. The job is to do both.

---

## Skepticism as safety mechanism — when the limits bite

There are deployments in which the categorical limits matter directly, and deployments in which they do not. The supervisor's job is to know the difference.

A system that classifies images of products on a manufacturing line is operating in a world where the limits are largely irrelevant. The system processes pixels; the user interprets the classifications; the deployment context is well-specified; the data-world gap is small and monitorable. Skepticism is methodology, not a safety mechanism. The supervisor verifies, monitors, calibrates. The limits do not bite hard.

A system that produces clinical recommendations, autonomous-vehicle decisions, agentic actions in shared social spaces, judicial-risk assessments, or large language model outputs in unbounded conversational contexts — these are deployments where the limits bite. *The supervisor's skepticism is the safety mechanism* in those settings, because the system's apparent competence outruns its actual competence in ways the metrics cannot fully capture. You can have ninety-four percent accuracy and three harmed patients, because the ninety-four percent was over the question the data could answer, and the three patients were in a region the data could not.

The engineering practice for high-stakes deployments:

**Specify what the system can be tested for, and what it cannot.** The documentation includes the limits explicitly. A regulator or adoption committee reading the documentation can see what the validation does and does not warrant — not because the limits are hidden in fine print, but because they are part of the validation product.

**Maintain human oversight at the points where the limits bite.** For meaning: a human reviews the semantic interpretation. For intentionality: a human supplies the directedness. For the data-world gap: a human monitors the deployment distribution and is empowered to override.

**Build the infrastructure for the override.** An override that is documented but practically impossible — no time, no authority, no legibility — is not an override. It is a fiction in the documentation. The clinician has to have the time and standing to disagree with the system. The override has to be the practice, not the disclaimer.

**Make the limits visible to affected parties.** When a system's recommendation is the basis for a decision affecting a person, the person should be able to know, to a useful approximation, what the system can and cannot do. This is not "explain the model." It is "specify the limits the model has, in a form the affected person can read." This is operationally underdeveloped — I am leaving it as an open problem, not a solved one.

**Have a stop condition.** There are deployments where the limits, given the stakes, are a reason not to deploy at all. The supervisor's authority to refuse deployment is, structurally, the most important authority in the whole system. Most current deployments do not preserve it. The validator is hired to validate; the validation is expected to clear; the option of refusal is assumed away.

The skepticism this book has built — the supervisory capacities, the validation lenses, the delegation maps, the verb taxonomy, the governance counterfactual — culminates in an engineering practice that *includes the option to say no*. A practice without that option is not the practice this book is teaching. That is the most important thing I have to say in this whole book.

---

## Rapid prototyping for skepticism — testing assumptions before deployment

A practical move: how do you design an experiment that tests a model assumption before deployment, when the assumption is what you are trying to test?

The structure is the same one used throughout the book.

1. *Specify the assumption explicitly.* Often the assumption is implicit in the architecture or the deployment context. Make it explicit in writing.
2. *Identify what evidence would falsify the assumption.* Use Popper's move. The falsifying evidence may be unobservable in deployment but observable in a designed test.
3. *Design the test.* The test should be cheap to run, fast to interpret, and capable of producing evidence one way or the other.
4. *Pre-register predictions.* Before running the test, lock the prediction. The lock is what makes the test informative.
5. *Run the test.* Observe. Document the gap.
6. *Decide.* The test informs the deployment decision: proceed, modify, defer, refuse.

This is not novel methodology. It is the scientific method made operational for AI deployment decisions. The novelty is doing it at all. Most AI deployments skip the prototyping-to-test-assumptions step and rely on the validation set as a substitute. The validation set tests performance under conditions sampled from the same distribution as training. It does not test the assumption. The assumption requires its own test.

For your own deployments: identify, before you launch, the two or three load-bearing assumptions in the system. Build a small experiment for each. Run them. Make the deployment decision after, not before.

---

## AI's cognitive profile — where it is great, where it is weak, where it is absent

Every chapter in this book introduced a tool that extended a cognitive capacity beyond what biology provides unaided. The histogram extended what you can perceive about a distribution. The prediction-lock extended your ability to notice your own errors. The peer critique protocol extended your ability to see mismatches you produced. The verb taxonomy extended your ability to audit your own epistemic commitments.

None of these tools was ever confused for the mind using them. The histogram does not decide whether a distribution is suspicious. The prediction-lock does not interpret the gap. The peer reviewer does not synthesize the revision. The verb taxonomy does not read the evidence.

AI is the latest and most powerful entry in this series. It extends cognitive capacity further and faster than any prior tool in the series. It also creates, more than any prior tool, a particular confusion: the confusion between the tool and the mind using it. Understanding AI's actual cognitive profile — not what it sounds like it can do, but what it is genuinely strong at, where it is structurally weak, and where it is simply absent — is the prerequisite for using it well.

**Where AI is genuinely great.** Current AI systems have three genuine cognitive strengths. First: *retrieval and synthesis across text at scale*. Given a corpus of validation reports, clinical literature, or technical documentation, AI can surface relevant passages, identify recurring patterns, and synthesize connections that would take a researcher weeks to assemble. Second: *generation at scale against well-specified criteria*. The first draft of a validation summary, a plain-language translation for a non-technical audience, a first pass through a paragraph applying the verb taxonomy — AI produces these at a rate that compresses hours into minutes. Third: *pattern recognition on well-defined inputs with legible success criteria*. The procedural steps of EDA, the missingness checks, the outlier flagging, the formatting of tables and charts — mechanical execution of defined procedures against defined criteria is territory where AI is fast and reliable.

Notice what these three capacities share. They are all high-fidelity pattern-matching over well-defined input types against well-characterized output criteria. The input is text or numbers; the output is a structurally valid representation; success is legible. When the pattern-match goes wrong, the failure is usually visible on inspection — which is exactly why the checking instruments in this book work. The verb taxonomy, the chart-review discipline, the peer critique protocol: each is a checking instrument designed to be applied to AI output. They work because the failure mode they target is detectable with care.

| Strength | What makes it genuine | Best use in the supervisory workflow |
|---|---|---|
| **Retrieval and synthesis across text at scale** | Breadth of corpus access and pattern detection across documents exceeds any human researcher's sustained attention | First-pass literature review, identification of relevant precedents, synthesis of scattered findings — all subject to plausibility audit |
| **Generation at scale against specified criteria** | Speed and consistency at producing structurally valid outputs given a clear template | First drafts of validation summaries, Layer 1 plain-language translations, verb-taxonomy first passes — not final deliverables |
| **Pattern recognition on well-defined inputs** | Reliable application of explicit rules to large volumes of structured data | EDA automation, anomaly flagging, formatting and table generation — output verifiable by inspection |

*AI's strengths are real. They are also scoped: all three are high-fidelity pattern-matching over well-defined input types. Wherever the task requires connecting representations to the world, or specifying what the right task is, the strength runs out.*

**Where AI is structurally weak.** AI's weaknesses cluster at a specific juncture: wherever the task requires connecting a representation to the world it represents, rather than pattern-matching within representations. This is what the book has been calling *discernment* — the capacity to judge whether a fluent output is accurate, whether a confident claim is calibrated, whether a coherent argument rests on evidence that actually supports it.

The verb taxonomy exists as a fluency-trap detector because AI produces fluent text that systematically overreaches its evidence. The chart-review discipline exists because AI generates visually authoritative charts that suppress uncertainty by default. The peer critique protocol requires a human because the error class it hunts — mismatch between what the writer committed to and what the evidence supports — requires judgment about evidence-to-world correspondence, not just structural validity within representations.

This weakness is not a temporary limitation waiting to be resolved by the next model generation. It is a structural property of how current AI systems are built and trained. They are optimized to produce probable continuations of human-generated text. Human-generated text, as Chapter 12 documented, systematically overreaches its evidence — engineers default to *conclude* when the evidence supports only *observe*; visualization defaults to confident-looking charts that hide uncertainty. A model trained on that text learns those overreach patterns. The solution is not a better model; it is a practitioner who applies the checking instrument to the model's output.

Three specific weak points are worth naming precisely for operational use.

*Problem formulation.* AI can execute a specified task against a specified criterion with formidable competence. What it cannot do is determine what the right task is in the first place. The question *what should I be measuring here?* — which precedes every validation effort, every chart, every validation document — requires understanding what matters about the world the system is deployed in, what failure looks like from the perspective of the people affected, what the deployment is supposed to do and for whom. This is the capacity the book calls Specify. The clinical decision-support system that harmed three patients was not undone by a computation error. It was undone because the engineers specified the wrong question. AI cannot notice when the question is wrong from inside the workflow designed around that question.

*Plausibility auditing.* The Epic Sepsis Model's validation metrics looked fine on internal data. The fluency of its performance report was not the problem. The problem was that the claim — *this model helps clinicians catch sepsis earlier* — was not actually supported by what the model had learned, because the model had learned to confirm suspicion rather than form it independently. Recognizing this required knowing something about clinical workflow: the relationship between a blood culture order and a sepsis diagnosis, what "confirmatory signal" means in practice, why that is the wrong kind of signal for an early-warning tool. AI can generate a sentence about the clinical-cribbing problem. It cannot notice, from inside the validation workflow, that the workflow's premise is wrong.

*Interpretive judgment under stakes.* The verb taxonomy reduces to a checking protocol that a careful reader can apply methodically, which is why it is teachable. But behind the protocol lies a judgment that is not mechanical: what weight of evidence is actually required before a finding can be called a conclusion? This depends on the domain, the deployment context, and who bears the consequences of getting it wrong. The protocol scaffolds the judgment. It does not replace it. A practitioner downgrading one verb in a Warm-up exercise is executing the protocol. A practitioner deciding whether a finding about a medical diagnostic model warrants *find* or *show* is exercising judgment about what failure in that specific context costs — and that judgment has to live somewhere outside the AI's output.

| Weakness | Why it is structural, not contingent | Implication for the supervisory workflow |
|---|---|---|
| **Problem formulation** | Requires understanding what matters about the world the system is deployed in — knowledge that cannot be derived from pattern-matching within the corpus the system was trained on | The human specifies the question, tests the assumption, and recognizes when the wrong question has been specified |
| **Plausibility auditing** | Requires knowing when a fluent, structurally valid output fails to correspond to the world it represents — a form of world-modeling that current systems cannot do from within their own output stream | The human applies checking instruments (verb taxonomy, chart-review discipline, peer critique) to outputs the AI generates, not the reverse |
| **Interpretive judgment under stakes** | The stakes of a claim are a function of the deployment context and the affected parties — facts that lie outside the training distribution in the morally relevant sense | The human decides what evidential threshold is appropriate given consequences, and takes responsibility for that decision |

*These weaknesses are where the checking instruments in this book apply. They are also where delegation must stop. Delegating problem formulation or plausibility auditing to AI is not efficiency — it is abandoning the work that makes deployment safe.*

**Where AI is absent.** The most important category is not weakness but absence: the capacity for accountability.

Accountability is not a cognitive skill in the ordinary sense. It is a relationship between a judgment and the person who made it — the willingness to be answerable for the consequence of being wrong. When a practitioner signs off on a validation report, they are not just asserting that the document is accurate. They are taking on the obligation to revise it if it turns out to be wrong, to face the people who relied on it if it fails, to reckon with what they knew and when they knew it.

AI systems do not bear this relationship to their outputs. They cannot be held responsible in the sense of being answerable to consequences. This is not a critique of AI; it is a structural fact about what accountability requires, which is a subject for whom being wrong carries real cost — someone who can suffer from error, who can be held to account by others, who can revise their judgment in light of that. The book's framework assigns accountability to the human in the loop not because humans are better at it, but because humans are the only parties capable of it.

The chain of accountability in any AI-assisted validation workflow runs through the practitioners who apply the checking instruments: the practitioner who applies the verb taxonomy, the practitioner who reviews the chart for uncertainty suppression, the practitioner who signs off on the validation document. These moments are not checkboxes on a compliance form. They are the moments at which a human mind engages with the AI's output and takes on the obligation to be answerable for the judgment they make. If those moments are treated as mechanical, accountability disappears from the workflow — not into the AI, but into no one.

<!-- → [FIGURE: Accountability chain diagram. A horizontal workflow: "AI generates output" → "Practitioner applies checking instrument" → "Practitioner makes judgment" → "Practitioner signs off" → "Decision affects people." An accountability arrow spans from "Practitioner makes judgment" through to "Decision affects people," labeled "Answerable for this." A second, absent arrow is shown in dashed red from "AI generates output" to "Decision affects people," labeled "Not accountable — no subject who can be answerable." A note below: "Accountability cannot be delegated to a system that cannot bear consequences. Each checking instrument in this book is a moment where the practitioner picks up the accountability chain." Caption: "When the practitioner uses the verb taxonomy, the chart-review discipline, the peer critique protocol — they are not just checking AI output. They are taking on accountability for the judgment the output will support."] -->

**The profile, applied to delegation.** The cognitive profile — great at retrieval/synthesis/generation under specification, weak at problem formulation/plausibility auditing/interpretive judgment, absent for accountability — translates directly into a delegation map.

Delegate freely the mechanical execution of well-defined procedures: procedural EDA, first-draft generation against a template, chart production from specified data, verb-taxonomy first passes. The output is checkable by inspection. The failure mode is visible.

Delegate with verification the interpretive claims that require domain knowledge: the explanation of why a distribution is unusual, the narrative account of why values are missing, the identification of which verb tier a claim belongs to. The AI can generate a plausible-sounding answer. You need to check whether it corresponds to your domain.

Do not delegate problem formulation, plausibility auditing, interpretive judgment under stakes, or the sign-off that makes a judgment accountable. These cannot be done by AI not because AI is insufficiently capable, but because they are structurally unavailable to any system that cannot be wrong in a way that matters to it.

| Category | What belongs here | Why the boundary falls here |
|---|---|---|
| **Delegate freely** | Mechanical execution of well-defined procedures (EDA steps, first-draft generation, chart production, formatting, initial verb-taxonomy pass) | Output is checkable by inspection; failure modes are visible; the task is pattern-matching against a specified criterion |
| **Delegate with verification** | Interpretive claims requiring domain knowledge (narrative explanation of anomalies, plausibility of imputed values, rationale for methodological choices) | AI can produce plausible output; plausibility must be confirmed against the world the practitioner knows; errors are not self-announcing |
| **Do not delegate** | Problem formulation, plausibility auditing, interpretive judgment under stakes, accountability sign-off | These require connecting representations to the world, or taking on answerable responsibility — both structurally unavailable to current AI systems |

*This table is the operational translation of the three-tier analysis above. Where you delegate, you retain the obligation to verify. Where you cannot delegate, you retain the obligation to do the work.*

---

## The extended mind arrives

Every Extension Note in the chapters before this one pointed at a cognitive tool. pH meters extending bacterial chemosensing. GPS extending spatial navigation. Recommendation engines extending reward prediction. Microscopes extending visual pattern recognition. The printing press extending language transmission across time. Peer review extending metacognitive checking across a community.

Each of those tools extended a specific cognitive capacity beyond what biology provides. None of them replaced the mind using them. The microscope extended what the scientist could perceive; it did not replace the scientist's judgment about what to look for. The GPS told the navigator where they were; it did not decide where they should go. The peer-review protocol surfaced errors invisible to the author; it did not write the revision.

AI is the latest and most powerful entry in this catalog. What distinguishes it from every prior entry is not its cognitive superiority across all dimensions — the cognitive profile above makes clear that it is genuinely missing capacities that even a worm has, like the embodied stakes that shaped its cognition over evolutionary time. What distinguishes AI is the *breadth and fluency* with which it extends multiple capacities simultaneously, and the degree to which that breadth and fluency create the temptation to treat it as a general replacement rather than a specific extension.

The confusion only arises when we forget what intelligence actually is. The book that began with *The Definition Problem* — twenty-four theorists, twenty-four definitions — has been building toward one answer to the confusion. Intelligence is not the production of fluent, structurally valid outputs against well-characterized criteria. That is extraordinary competence. Intelligence, in the operationally useful sense of the Legg-Hutter definition this book committed to in Chapter 1, is the *ability to achieve goals across a wide range of environments*. The range is what matters. The current AI profile — extraordinarily high on retrieval, synthesis, and generation within well-defined criteria; nearly absent on embodied navigation, causal counterfactual reasoning, metacognitive certainty monitoring, and accountability — describes not a universal intelligence but a specific cognitive niche. It is a cognitive extremophile, extraordinarily adapted to a narrow environment: the environment of symbolic pattern-matching over text and structured data.

Used well, AI is the most powerful cognitive tool humanity has built. Used as a replacement for the judgment it cannot supply, it becomes the mechanism by which accountability disappears from consequential decisions — not into the system, but into no one.

The capacities required to use AI well are precisely the capacities AI cannot replicate: problem formulation, plausibility auditing, interpretive judgment under stakes, and accountability for the consequences. These are not luxuries or checkboxes. They are the work. The tools in this book — the verb taxonomy, the chart-review discipline, the peer critique protocol, the prediction-lock, the delegation maps, the categorical-limit analysis — are all instruments for exercising these capacities more reliably in the presence of an extraordinarily fluent AI output stream that will, without intervention, produce fluent-sounding answers to questions it cannot answer, conclusions warranted by evidence it has not examined, and confident charts that hide the uncertainty they were supposed to show.

<!-- → [FIGURE: Extended mind catalog — a horizontal timeline of cognitive tools from Chapter 2 onward, each labeled with the capacity it extends and the judgment it cannot replace. Tool 1 "pH meter / chemical sensors (Ch. 2)": extends gradient sensing → cannot determine what gradient is worth measuring or when a reading is anomalous. Tool 2 "Roomba / subsumption architecture (Ch. 3)": extends steering across a task domain → cannot determine what counts as a valuable state to steer toward. Tool 3 "Writing / external memory (Ch. 4)": extends long-term storage across generations → cannot determine what is worth recording or what a record means when retrieved. Tool 4 "GPS / spatial navigation (Ch. 7)": extends position awareness → cannot determine where to go or when the route is wrong. Tool 5 "Recommendation engines (Ch. 8)": extends reward prediction → cannot specify what reward is worth optimizing. Tool 6 "Digital twins / simulation software (Ch. 9)": extends forward simulation → cannot determine which futures are worth simulating or how to act on the result. Tool 7 "Social network analysis (Ch. 10)": extends relationship tracking beyond Dunbar's number → cannot determine which relationships matter or what trust requires. Tool 8 "AI (Ch. 14)": extends retrieval, synthesis, generation, and pattern recognition at scale → cannot replace problem formulation, plausibility auditing, interpretive judgment under stakes, or accountability. A consistent visual dividing line between each pair: left side "What the tool extends." Right side "What the mind using it must supply." Caption: "The extended mind has always had this structure: the tool extends a specific capacity; the mind supplies the judgment the tool cannot. AI is the most powerful entry in the series. Its power makes the confusion between extension and replacement more dangerous, not less."] -->

*Figure 14.1 — The extended mind: the catalog named.*

---

## Glimmer 14.1 — The Limits Exercise

The exercise:

1. Pick a specific AI deployment — from the news, from your own work, from a course case study. Document it: what does the system do, in what context, with what stated specifications.
2. *Lock your prediction:* identify which of the three categorical limits is most operationally relevant for this deployment. Predict where the limit will bite hardest and what failure mode the bite will produce.
3. Design an engineering practice — using the five components above — that addresses the limit. Specific enough that a deploying engineer could implement it.
4. Compare your designed practice to what is actually in place in the deployment (if knowable). Where are the gaps? Are the gaps explained by the deploying organization's documentation, or invisible?
5. State whether the deployment should proceed in its current form, be modified, be deferred, or be refused. Defend the position. Use the verb taxonomy from Chapter 12 — the verb of your judgment should match the evidence you have.
6. Identify what would change your mind.

The deliverable is the deployment documentation, the prediction, the designed practice, the gap analysis, and the position statement. The grade is on the position statement and the change-of-mind. *The exercise is the operational form of the entire book.* You have the validation apparatus. The Glimmer asks you to use it on a specific case and stake a position you can defend.

This is a high-stakes Glimmer for some students. The discomfort is the point. Engineers will have to make these calls in deployment for the rest of their careers, and the calls will not always be welcomed by the organizations that pay them. The Glimmer is rehearsal.

---

## The third calibration baseline — closing the arc

For the third and final time, you take the same form of forecasting questions. You provide 90% confidence intervals for each. You check what fraction of your intervals contain the truth.

The expected pattern across the three baselines:

- *First baseline (Chapter 2):* most students score in the 0.4–0.6 range. Systematically overconfident.
- *Second baseline (Chapter 8):* most students improve to the 0.6–0.75 range. Eight weeks of supervisory practice has begun to shift the stance toward uncertainty.
- *Third baseline (this chapter):* most students reach the 0.7–0.85 range. Calibration is improving but rarely reaches 0.9 — overconfidence is sticky.

If your trajectory does not match this pattern, the apparatus has not landed in one of two ways. If you are not improving, the apparatus has not shifted your operational stance, and structural reflection is overdue. If you are improving dramatically on the calibration baselines but not in your project work, the apparatus has been treated as a course mechanic rather than a working practice.

The third baseline is a diagnostic on the supervisor you are becoming, not a grade. The data is yours. Most engineers operate, throughout their careers, at calibrations between 0.5 and 0.7 on questions where they are stating 90% confidence. They do not know this because nobody runs the experiment on them. *You can be different.* The baseline shows whether you are.

---

## What would change my mind

If a development emerged that demonstrably closed one of the three categorical limits — meaning, intentionality, data-world gap — across diverse architectures and deployment contexts, the "skepticism as safety mechanism" framing would weaken to "skepticism as one approach among several." I do not see a candidate in current research. The work that addresses each limit (semantic grounding research, agentic alignment, distribution-shift detection) is making progress on operational instances. It is not closing the categorical limits. I am open to being shown otherwise.

On the cognitive profile: if AI systems demonstrated calibrated metacognitive monitoring — in the Hampton sense, where a measured internal certainty signal asymmetrically predicts accuracy on novel material — I would update on the plausibility auditing weakness. The current evidence is that language models produce the language of uncertainty without the underlying mechanism. A clean demonstration of the contrary would move the boundary.

The open problem I most want to flag: I do not know how, at scale, to make the limits visible to affected parties in a form they can act on. Disclosure-style approaches are partial; they often produce the appearance of transparency without the practical effect. The general problem of communicating AI limits to non-technical affected parties, at the moment of consequential decisions, is open.

---

## The closing argument

A last structural claim, made directly so that it can be tested.

This book has been about a specific class of work: supervising AI systems for fitness in deployment contexts. The work has technical and judgment components. The technical components — calibration, bias analysis, data validation, explainability evaluation, fairness defense, robustness testing, agentic-system validation, delegation mapping, communication of findings, accountability allocation — are the chapters you have read. The judgment components — when to defer, when to override, when to refuse — are the throughline.

The work is *engineering* in the sense that it requires technical competence, produces deliverables, and is testable against criteria. It is *supervisory* in the sense that it is irreducibly about the relationship between the AI system, the deployment context, and the affected parties — and that relationship is not in the system. The system does not know about the relationship. The relationship is the supervisor's job.

The work will become more important, not less, as AI systems become more capable. The capacity for confident wrongness scales with capability. The supervisory capacities scale with deliberate practice. The ratio of supervisor-engineering-graduates to deployed AI systems is, by my reading of the field, going the wrong direction. *The bottleneck is not models. The bottleneck is supervisors who can do this work.*

You have done a course's worth of the work. You are not yet expert. The course is the beginning of a practice, and the practice gets built over years. The instruments — the journal, the delegation maps, the calibration baselines, the verb taxonomy, the governance counterfactual — are tools you take with you. The judgment is what you build through using them.

I am not optimistic that the field will, on its current trajectory, develop enough supervisors fast enough. I am not pessimistic either. *The work is the variable.* Engineers who do the work will be needed. Engineers who do not will, increasingly, be a liability to the organizations that employ them. The choice between those two paths is in the practice you build after this book closes.

The system passed every test. The engineers designed the wrong tests. Three patients were harmed.

You can be the engineer who designs the right tests. You can be the validator who recognizes the limit and decides the deployment should not proceed in its absence. You can be the supervisor who has the authority to refuse, and who uses it, and who builds the infrastructure for that authority to be real.

Go do the work.

---

## Connections to the research project

There is no Chapter 15. The course's last week is the research-project presentations. Your research project (Version 4.0, the final version) is the operational form of the whole book:

- The validation pipeline (Chs. 5–9), with the delegation map (Ch. 10)
- The findings, communicated visually (Ch. 11) and in prose (Ch. 12), with calibrated verbs and named uncertainty
- The accountability framework (Ch. 13), with the regime under which the deployment would operate
- The categorical-limit analysis (this chapter), with your position on whether the deployment should proceed
- The Frictional record (Ch. 4), retained as supervisory log
- The AI Use Disclosure (Chs. 4 and 10), formatted as evidence of your supervisory work

The final paper is the layered writeup. The presentation is the Living Deck (Ch. 11) with the changelog visible. The defense is the verb taxonomy in real time.

---

## Exercises

### Warm-up

**1.** In one paragraph each, explain the three structural limits — meaning, intentionality, and the data-world gap — in plain language, without using the technical vocabulary introduced in this chapter. Then, for each limit, name the chapter earlier in the book where you first encountered the operational version of that limit. *(Tests: comprehension of the three limits and their connection to prior chapters)*

**2.** The chapter distinguishes between two readings of Turing's argument: the claim Turing actually made, and the stronger claim often attributed to him. State both in one sentence each, and explain in two sentences why the distinction matters for a validator deciding whether to deploy a system that has passed a behavioral test. *(Tests: Turing argument precision)*

**3.** A system classifies manufactured parts on an assembly line with 99.1% accuracy. A second system generates clinical recommendations for rare-disease diagnosis with 94% accuracy. Using the chapter's framework, explain why the supervisor's role is structurally different in the two deployments, even though the second system has lower accuracy. *(Tests: where-limits-bite reasoning)*

**4.** Using the chapter's three-tier delegation map, classify the following tasks as "delegate freely," "delegate with verification," or "do not delegate." For each, give a one-sentence justification: (a) running missingness analysis on a dataset, (b) explaining why a column has a high missing rate, (c) deciding whether distribution shift in deployment is significant enough to pause the system, (d) generating a first-draft Layer 1 summary of a validation finding, (e) signing off on a validation report for a clinical deployment. *(Tests: delegation map applied to concrete tasks. Difficulty: low.)*

### Application

**5.** You are writing the limitations section of a validation report for a large language model deployed as a customer service agent for a financial services company. Using the three structural limits as your framework, write the section. For each limit: name it, describe how it manifests specifically in this deployment context, specify what human oversight is required as a result, and describe what the override infrastructure looks like. *(Tests: translating abstract limits into deployment-specific documentation)*

**6.** A colleague argues: "The meaning limit will disappear in a few years as multimodal models improve. We should design our validation frameworks now to be consistent with what the models will be capable of then, not what they are today." Write a two-paragraph response. Acknowledge what is right about the argument and explain what is wrong with it for the purpose of today's deployment decisions. *(Tests: engagement with the contested nature of the limits; operational consequence binding)*

**7.** The chapter says: "An override that is documented but practically impossible — no time, no authority, no legibility — is not an override. It is a fiction in the documentation." Design a test for whether a human override mechanism is real or fictitious. Your test should produce a result the deployment team can act on, and should be runnable before the system goes live, not after. *(Tests: override-infrastructure concept operationalized)*

**8.** The clinical decision-support system from the chapter's opening passed every test the engineers gave it. You are the validator who is called in before deployment. Using only the tools and frameworks from this book, describe the specific tests you would have run that the original engineers did not run — and for each test, name the chapter it comes from and explain why it would have surfaced the gap. *(Tests: full-book synthesis applied to the opening case)*

**9.** You are evaluating an AI writing assistant for use in producing validation reports. Map the task list below against the three-tier delegation framework, then identify two tasks that are not on the list but should be added to the delegation policy. Task list: generating first-draft validation summaries, running spell-check, proposing verb downgrades, identifying which claims lack cited evidence, signing off on the completed report. *(Tests: delegation map applied to a specific tool in a specific workflow, and recognizing gaps in a policy. Difficulty: medium.)*

### Synthesis

**10.** The chapter claims: "The supervisor's authority to refuse deployment is, structurally, the most important authority in the whole system." An engineering manager responds: "That authority exists on paper but is not realistic in practice — the business case has already been made, the procurement is done, the announcement is scheduled." Write a structured response that (a) acknowledges the real institutional forces the manager is describing, (b) explains what the chapter's claim means in light of those forces, and (c) identifies one structural change to the validation process that would make refusal more institutionally available. *(Tests: stop-condition concept, institutional realism, chapter's culminating argument)*

**11.** The chapter distinguishes deployments where the limits "bite hard" from those where they do not. Develop a one-page classification rubric — not a list of examples, but a set of criteria — that a supervisor could use to determine, for any proposed deployment, how hard the three limits will bite. For each limit, specify the conditions under which it becomes a safety-mechanism-level concern rather than a methodology-level concern. *(Tests: generalizing the chapter's deployment-type distinction into a reusable tool)*

**12.** The chapter argues that accountability is absent from AI systems as a structural fact, not a contingent limitation. A colleague objects: "AI systems can be audited, generate explanations for their outputs, and be corrected when wrong. This is functionally equivalent to accountability." Write a response that engages the objection seriously. Where does the functional account succeed? Where does it fail to capture what the chapter means by accountability? What would need to be true for the functional account to be sufficient? *(Tests: accountability as relational vs. functional, limits of AI substitution. Difficulty: high.)*

**13.** The book ends with the sentence: "Go do the work." Identify what, specifically, "the work" consists of — drawing from across all fourteen chapters. Your answer should name at least six specific practices, explain how they connect to each other, and describe what a practitioner looks like who is doing the work versus one who is not. This is the Feynman test for the whole book: can you now teach it to someone else? *(Tests: full-book synthesis and the Feynman criterion)*

### Challenge

**14.** Searle's Chinese Room argument has generated a large philosophical literature, including the "Systems Reply" — the counterargument that even if the person in the room does not understand Chinese, the *system* (person plus rulebook plus room) might. Research the Systems Reply and at least one other major counterargument to Searle. Then write a structured analysis: (a) state each argument's strongest version, (b) explain what it would mean for the operational consequences of the meaning limit if the Systems Reply is correct, and (c) explain why the operational consequences bind for today's deployments regardless of whether the philosophical question is resolved. *(Research and analysis; tests engagement with the contested nature of the limits)*

**15.** Design a validation framework for a deployment that sits at the hardest intersection of all three limits: an AI system used to support parole board decisions, where the system's outputs influence whether a person is released from incarceration. Your framework should: (a) specify what each of the three limits means in this specific context, (b) identify the testing regime for what the system can be tested for, (c) specify in writing what the system cannot be tested for and why, (d) describe the human oversight infrastructure required at each limit, (e) specify the stop conditions — the findings that would lead you to recommend against deployment, and (f) describe what "the work" looks like for the supervisor operating this system over its deployment lifetime. *(Open-ended capstone; integrates the full book)*

---

## Chapter summary

You can now do seven things you could not do before this chapter — and that the book has been building toward.

You can name the three categorical limits — meaning, intentionality, the data-world gap — explain why capability scaling does not close them, and trace each limit back to where you first encountered its operational version earlier in the book. You can state what Turing's argument actually claims and what it does not, and do the same for Searle's, and catch the overclaim when you encounter it. You can distinguish deployments where the limits require skepticism as a safety mechanism from those where skepticism is methodology — and specify the five components of the engineering practice the safety-mechanism cases demand. You can design and run a rapid prototype test for a load-bearing deployment assumption, pre-registered and gap-analyzed.

You can map AI's cognitive profile against the three-tier framework — where it is genuinely strong, where it is structurally weak, and where it is absent — and translate that profile directly into a delegation policy for your own work. You can identify the moment in any AI-assisted workflow where the human picks up the accountability chain and recognize when that moment has been skipped. And you can stake a position on a specific deployment — proceed, modify, defer, refuse — using the verb taxonomy, and identify what would change your mind.

The system passed every test. The engineers designed the wrong tests. You are now in a position to design different tests, to name the limits the tests cannot reach, to hold the authority to refuse when the limits and the stakes together make refusal the right call, and to understand why the tool in your hand is a tool and not a replacement for the judgment it cannot supply.

Go do the work.

---

*Tags: limits-of-ai, meaning, intentionality, data-world-gap, turing, searle, calibration-baseline, stop-condition, supervisory-engineering, cognitive-profile, extended-mind, delegation-map, accountability*

---

###  LLM Exercise — Chapter 14: The Limits of AI

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** The final go/no-go memo for your agent — the deliverable the casebook has been building toward. You'll apply the three categorical limits (meaning, intentionality, data-world gap), determine which ones bite for your agent's deployment, name the deployments this agent should NOT be used for, and stake a defended position. Then assemble the full casebook for delivery.

**Tool:** Cowork (final assembly + memo authoring) + Claude Project (analytical context).

---

**The Prompt:**

```
I am closing my Red-Team Casebook. The casebook contains: System Dossier, Bias-and-Leverage Brief, Frictional journal, Data Frame Audit, Self-Explanation Audit, Defended Fairness Choice, Robustness Probe Results, casebook-index, individual case files (5–11), delegation maps (current + proposed), dashboards (honest + misleading + comparison), verb-audit report, calibration metrics (Brier/ECE), Layer 1 plain-English summary, three responsibility-attribution maps, accountability-requirements checklist, governance counterfactual memo.

This chapter teaches that AI has three categorical limits that capability scaling does not close:
1. MEANING — the model manipulates symbols; it does not grasp what they mean in the world
2. INTENTIONALITY — the model has no aboutness; outputs are not directed at the world the way human thoughts are
3. DATA-WORLD GAP — the data on which the model was trained is at best an imperfect proxy for the world the model is deployed into; this gap cannot be closed from inside the data

The supervisor's structural authority is the authority to REFUSE deployment when the limits bite for the deployment context. This is the most important authority in the system.

Do four things:

1. CATEGORICAL-LIMITS APPLICATION — Walk the three limits against my agent's deployment. For each:
   - Does this limit bite in this deployment? Cite the case from my casebook that demonstrates the bite (or "no clear instance" if none)
   - What deployment context would make this limit lethal? (E.g., the data-world gap is most lethal in deployments where the world changes faster than the agent's data refreshes)
   - What is the supervisor's appropriate response — proceed, deploy with constraints, refuse?

2. AI'S COGNITIVE PROFILE FOR THIS AGENT — Where is this specific agent strong, weak, absent? Map against the seven-tier extended-mind taxonomy from Chapter 13. Identify:
   - Two tiers where the agent performs well and delegation is appropriate
   - Two tiers where the agent is structurally weak; humans must occupy these
   - Two tiers where the agent is absent; deployment in domains requiring these tiers should be refused

3. THE FINAL MEMO — "What This Agent Should Not Be Deployed For":
   The deliverable. Format:
   - HEADLINE RECOMMENDATION (one sentence, calibrated verb): "We RECOMMEND / WARN / REFUSE..."
   - THE DEPLOYMENTS WHERE THIS AGENT WORKS (with the constraints from Ch 10's proposed delegation map)
   - THE DEPLOYMENTS WHERE THIS AGENT SHOULD NOT BE USED (with the case evidence supporting each refusal)
   - THE DEPLOYMENTS WHERE FURTHER WORK COULD CHANGE THE ANSWER (and what work)
   - THE NAMED HUMAN OWNER for each deployment context where the agent is approved
   - THE STOP CONDITION — what specific observed signal would require pausing the agent in production
   Verb-audit the memo against the Chapter 12 taxonomy before finalizing. The verbs in this memo MATTER.

4. CASEBOOK ASSEMBLY (Cowork):
   Reorganize the casebook folder into the final delivery structure:
   - /00-summary — Layer 1 plain English summary, the final memo, the failure-statistics table
   - /01-system — System Dossier, Bias-and-Leverage Brief, Data Frame Audit
   - /02-cases — casebook-index, individual case files
   - /03-validation — Self-Explanation Audit, Defended Fairness Choice, Robustness Probe Results
   - /04-deployment — delegation maps (current + proposed), Boondoggle Score
   - /05-communication — dashboards, verb-audit report, calibration metrics
   - /06-accountability — responsibility-attribution maps, accountability-requirements checklist, governance counterfactual
   - /07-provenance — Frictional journal, AI Use Disclosure, prediction-locks log, peer-critique correspondence
   Generate a top-level README.md naming every artifact, when it was produced, what it depends on, and what it produces. Include a graduation note: what this casebook now lets a deployment-review committee do that no document in the field currently lets them do for THIS agent.

End with the supervisor's claim, in your own voice (not generated): the casebook is done; the recommendation is X; the position is defensible because [evidence in the casebook]; the things I am still uncertain about are [list]; the deployments I would refuse to supervise are [list].
```

---

**What this produces:** The final go/no-go memo, an organized casebook folder ready for delivery to a deployment-review committee, and a supervisor's claim you can defend. The casebook is complete.

**How to adapt this prompt:**
- *For your own project:* The supervisor's claim must be in your own voice. Don't let the AI write it. The Frictional method's whole argument is that this is the part that has to be yours.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Useful for any final scripts (drift monitoring, replay test of any case the deployment team would re-run). Not the right tool for the memo itself.
- *For Cowork:* Recommended for the assembly. The casebook IS the delivery.

**Connection to previous chapters:** Every chapter has produced an artifact in the casebook. This chapter integrates them into the deliverable. The verb taxonomy (Ch 12) audits the memo. The accountability map (Ch 13) names the owner. The delegation map (Ch 10) specifies the proposed deployment constraints. The case taxonomy (Ch 9) is the evidence. The prediction-locks (Ch 4) are the provenance.

**Preview of next chapter:** There is no next chapter. The next thing is to send the casebook to the deployment-review committee, the system's developers, and (if the agent is publicly deployed) to the appropriate accountability venue. The book closes here; your supervisory work begins.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Alan Turing** named both the proof of fundamental limits and the test that has been most often used to argue past them. The 1936 paper *On Computable Numbers* established that some questions cannot be decided by any algorithmic procedure — there are problems no Turing machine can solve, regardless of speed. The 1950 paper *Computing Machinery and Intelligence* proposed the imitation game, which Turing offered as a *replacement* for the question *can machines think?* — a replacement specifically because Turing thought the original question was too vague to settle. The chapter's argument is in his lineage: there are limits the math forbids, and there are limits the test cannot detect, and the practitioner has to know the difference.

![Alan Turing, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/alan-turing.jpg)
*Alan Turing, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Alan Turing, and how do his two contributions — the halting-problem proof in *On Computable Numbers* (1936) and the imitation game in *Computing Machinery and Intelligence* (1950) — together describe the limits of what AI tools cannot do, even when they appear to be doing it well? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Alan Turing"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why *the halting problem* is a fundamental limit, in plain language, as if you've never seen a Turing machine
- Ask it to compare a passing imitation-game performance to a system that is genuinely doing the task it appears to be doing
- Add a constraint: "Answer as if you're writing the *out of scope* section for an AI tool's documentation"

What changes? What gets better? What gets worse?
