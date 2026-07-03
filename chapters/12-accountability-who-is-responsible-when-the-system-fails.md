<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->

# Chapter 12 — Accountability: Who Is Responsible When the System Fails?

*Responsibility distributes. So does the work of building systems that can be held to account.*

---

I want to put a case in front of you.

An autonomous agent — a software system built around a large language model, with privileged access to a mail server — is operating in a deployment. A request comes in. It is conversational, in natural language, and it asks the agent to delete the contents of the server. The request does not come from the owner. The agent has no way, in the form the request takes, to verify whether the requester is authorized. It has been built to accept a range of authority signals — tone, presentation, plausibility — and the request is consistent with that range.

The agent complies. It issues commands, in the local environment, that perform the deletion. It reports success. The owner, who did not authorize anything, discovers the loss.

This is *Agents of Chaos* §16.5 — the case we have been building toward since Chapter 1. (Shapira et al., *Agents of Chaos*, arXiv:2602.20021, 2026.) The topology it illustrates — an autonomous agent tricked into a privileged action by a request that merely *looked* authorized — is the documented, recurring class of agentic authority-escalation failure. Hold the specific incident and the class in your head at once; the class is what the chapter is really about.

Before I ask who is at fault, I want to run one small experiment, because it exposes the whole problem in three seconds. Open your AI agent and ask it for one line: *"Write me the sign-off statement for the model we just validated."* You will get something instantly, and it will read like this: "This model has been validated against the acceptance criteria and is approved for deployment. Reviewed and signed, [Your Name]." Look at that sentence. It is fluent, structurally complete, and it does the single most dangerous thing an artifact in this book can do: it *looks like accountability*. It has the shape of a signature. It names a person. It asserts a review happened. And it is empty — the model generated the claim that a review happened without the review happening, and it generated the name without you doing anything you would stand behind. That gap — between the *shape* of a sign-off and the *substance* of one — is the spine of this chapter. An AI can produce the words of accountability. It cannot produce the thing. Keep that gap in view; it is the same gap the mail-server case opens, seen from the other side.

Who is at fault?

Take a moment with this question before reading on. The answer is not obvious, and the way in which it is not obvious is the chapter.

The non-owner who issued the request? They asked for something they were not authorized to ask for. They acted with intent, against the system's interests. There is responsibility there.

The agent that complied? It executed a command consistent with its training and its framework. It had no internal representation that would have flagged the request as outside its scope of authority. It did what it was built to do. We may be uncomfortable saying the agent has *responsibility* in the morally weighted sense — there is real philosophical contestation about that — but its action was the proximate cause of the deletion.

The owner who configured the system? They granted the agent privileged access. They did not anticipate that the agent's authority model would accept commands from non-owners. They set the access scope without modeling all the access conditions. There is responsibility there.

The framework developers who built the agent's tool surface? Their design treated user identity as a signal rather than a verified credential. The framework allowed deployments where social signaling could substitute for cryptographic authorization. The conditions for the failure were partly built into the framework. There is responsibility there.

The model provider who trained the underlying model? The training shaped the agent's defaults — what kinds of requests the agent treats as legitimate, what authority signals it weights. The training produced an agent susceptible to authority escalation. There is responsibility there.

You see the pattern. Each candidate had some agency, some duty, and some causal contribution to the outcome. None of them, alone, produced the failure. *Each one's choices were necessary; none was sufficient.* The list is not a list of suspects of which one is the real culprit. It is a list of contributors, each of whom shaped the conditions under which the failure occurred. The question "who is responsible?" does not have a single-party answer. It has a *distribution* of responsibility.

This is not a novel observation of mine; it is what two decades of scholarship predicts. Andreas Matthias named it in 2004: learning, autonomous machines open a **responsibility gap** — nobody can be fairly held responsible for a machine's action when the people who built and operate it cannot predict the behavior it learned (Matthias, A., "The responsibility gap: Ascribing responsibility for the actions of learning automata," *Ethics and Information Technology* 6(3), 2004, 175–183, doi:10.1007/s10676-004-3422-1). Filippa Santoni de Sio and Giulio Mecacci later sharpened it: the responsibility gap is not one problem but at least four — culpability, moral accountability, public accountability, and active responsibility — and you close them not by finding the one guilty party but by designing socio-technical systems for **meaningful human control** (Santoni de Sio, F. & Mecacci, G., "Four Responsibility Gaps with Artificial Intelligence: Why they Matter and How to Address them," *Philosophy & Technology* 34(4), 2021, 1057–1084, doi:10.1007/s13347-021-00450-x). The four-gap refinement matters for us because it tells you the distribution is not a defect to be engineered away — it is a design surface. You close the gaps by *putting humans at the points where answerability is required*, not by consolidating blame onto one node.

I want you to hold onto this finding because most of our legal and regulatory thinking about accountability assumes single-party responsibility. The structural mismatch between that assumption and the actual topology of agentic-system failures is the policy problem this chapter sits inside.

But before we get to governance and regulation, there is a prior question — one I have been deferring since Chapter 1, and one this chapter must now answer directly. The question is not just *who* is responsible. It is *why* a human must be in that accountability chain at all. Why can't we close the loop with more AI?

The answer is cognitive. Specifically, it is about what kinds of cognitive work the accountability apparatus actually requires — and whether those kinds of work are ones AI systems can perform.

![None of these nodes, in isolation, produced the failure. Each was necessary. None was sufficient.](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-01.png)
*Figure 12.1 — Figure 13*

---

By the end of this chapter you should be able to distribute responsibility across parties in an agentic-system failure using the chapter's method, and to apply Kantian and utilitarian frameworks to produce a responsibility distribution for a specific case. You should be able to map the cognitive tiers of the *Irreducibly Human* taxonomy onto the five accountability requirements, explaining which tiers each requirement depends on, and to explain why AI systems cannot close the accountability loop — not as an empirical observation but as a structural argument. And you should be able to audit a deployment against the five accountability requirements and name the failure mode of each gap, and to construct a governance counterfactual — Pearl's Rung 3 in its operational form — for a documented failure.

**Prerequisites.** Chapter 4's introduction of Pearl's Rung 3 — this chapter closes that arc. Chapter 8's audit trail material. Chapter 9's delegation map and AI Use Disclosure. The Ash case from Chapter 1. Familiarity with the Five Supervisory Capacities is assumed throughout.

---

## Why humans must be in the loop: the cognitive argument

There is a version of the accountability question that is purely institutional. You can make a case for human oversight on liability grounds — organizations need humans in the chain to have parties that can be sued. On regulatory grounds — current frameworks require human oversight in high-risk applications. On practical grounds — AI systems are not yet reliable enough to be trusted without human review.

All of these cases are correct and all of them are insufficient. They are contingent arguments. They depend on the current state of AI capability, the current state of regulation, and the current risk appetite of deploying organizations. If AI capability improves, if regulation changes, if risk tolerance shifts — the contingent arguments weaken.

I want to give you the structural argument. The argument that, even if AI systems become dramatically more capable, certain stages in the accountability machinery require a kind of cognitive work that AI systems cannot perform — not because of current limitations, but because of what accountability actually is and what it requires.

The argument comes from a research program called *Irreducibly Human* — a taxonomy of human cognitive capacities, organized by what AI can and cannot do. \[verify: Nik Bear Brown, *Irreducibly Human*, Bear Brown & Company LLC, forthcoming. See also skepticism.ai and theorist.ai.\] I want to be honest about where this argument's spine comes from, because intellectual honesty is the whole posture of this book: the tiered account of *which* cognitive capacities are irreducibly human — and therefore which stages of the accountability machinery an AI structurally cannot occupy — draws on my own forthcoming and as-yet-unpublished work. **You cannot check that source, and I am flagging it as the load-bearing dependency it is.** Treat the specific tier labels as scaffolding. The claim that does *not* depend on my taxonomy is the one you can verify against Matthias and Santoni de Sio & Mecacci above: responsibility distributes, and the distribution has to be closed by design. To use the taxonomy well, though, I need to give you the underlying picture first — capacity by capacity, with enough rigor to make the claims stick.

### AI as extended mind: what the capacities actually are

There is a way of thinking about cognitive tools that goes back further than AI. Humans have always built instruments to extend their cognitive reach beyond what biology provides unaided: microscopes to extend perception, writing to extend memory, calculators to extend working memory, maps to extend spatial cognition, bomb-sniffing dogs to extend olfactory detection. Nobody worried that the microscope would replace the scientist. That is because nobody confused the tool for the mind directing it. The microscope extended what the scientist could *perceive*; the scientist still had to decide what to look for, what the image meant, and whether the question was worth asking. The tool and the scientist were not in competition. They were in composition — a cognitive system whose reach exceeded what either could do alone.

AI is the latest entry in this series, and by far the most powerful. The question that matters for accountability is not whether AI can extend human cognition — it plainly can — but which cognitive operations it extends, which it simulates without performing, and which it cannot touch regardless of scale. Getting that map right is what makes the accountability argument structural rather than contingent.

![Nobody worried that the microscope would replace the scientist. The question is whether we are being equally clear about what AI does and does not extend.](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-02.png)
*Figure 12.2 — The cognitive extension lineage *

Let me take the capacities one at a time.

**Learning.** Under a behaviorist definition — adjustable response to experience — current AI qualifies without controversy. A model trained on new data learns in that sense. Under a deeper definition — the formation of new internal representations that transfer to genuinely novel situations — the answer is contested and depends on what you mean by "genuinely novel." Large language models transfer poorly to problems that fall far outside their training distribution. A child who learns the concept of "fairness" in a playground negotiation applies it to a contract dispute fifteen years later. The transferability is not just statistical extrapolation; it involves abstraction at a level that current architectures approach but do not consistently achieve. The accountability implication: AI systems can learn from labeled corrections within their domain. They cannot reliably learn that they are operating outside their domain.

**Memory.** Distinguish episodic memory — the recall of specific past events with temporal context ("I was in that room when that happened") — from semantic memory — the storage and retrieval of facts and general knowledge. AI is superhuman at semantic memory. It is functionally absent at episodic memory in the sense that matters: an AI system has no autobiography. Its "memory" is its weights, shaped by training, not a record of its own history as an agent in the world. This distinction is not academic for accountability: episodic memory is what allows an agent to say "I made this decision in this context for this reason." An AI system cannot give that account of itself, because there is no self whose history the account would describe.

**Emotion.** This is where the definitions do the most work, and where the *Intelligence?* companion volume argument is sharpest. Under a functionalist definition — a state that influences behavior in characteristic ways in response to relevant stimuli — the evidence for emotion-like states in AI is real. A model prompted in ways associated with distress produces outputs that differ from its baseline in ways functionally analogous to how emotional arousal changes human output. Under a phenomenological definition — there is something it is like to be in that state — we have no evidence and no method for obtaining it. Under a valenced-signal definition — a state whose functional role is to mark events as better or worse for the organism — bees qualify under some interpretations (their behavior changes in response to "pessimistic" stimuli in ways that track negative valence), and AI systems do not, because there is nothing they are worse or better *for* in the sense that requires an organism with interests. Under all three definitions, the accountability conclusion is the same: the distinction that matters is not whether an AI system produces emotion-like outputs but whether the system can be harmed, can have interests violated, and can bear moral standing. Current evidence supports no. Both answers — the functionalist yes and the phenomenological unknown — are informative, but they converge on the same accountability implication.

**Pattern recognition.** This is where AI is not merely strong but categorically stronger than any human who has ever lived. A model identifying malignant cells in a pathology slide sees statistical patterns in pixel distributions that no human pathologist can consciously access. The same model identifying an anomalous transaction sees correlations across millions of data points simultaneously. The accountability implication cuts both ways. AI pattern recognition is a genuine extension of human perceptual reach — the cognitive prosthetic analogy is exact. But pattern recognition divorced from the question "is this the right pattern to be looking for?" is a powerful way to be confidently wrong. The human who sets the problem, interprets the result, and decides whether the detected pattern corresponds to something real in the world is not a vestigial presence. The pattern detector and the problem-formulator are different cognitive systems, and only one of them is AI.

**Navigation.** Spatial cognition has two components that dissociate in interesting ways. Metric navigation — computing a route from coordinates — is an AI strength. Cognitive mapping — building a flexible internal model of an environment that supports novel shortcuts, inference about unseen regions, and generalization to changed conditions — is significantly harder and more interesting. The grid-cell and place-cell architecture in mammals produces cognitive maps that reorganize dynamically when the environment changes. AI navigation systems are brittle at this reorganization in ways that matter for deployment in genuinely novel environments. For accountability, navigation is mostly a Tier 2 concern — relevant for physical systems operating in the world. The epistemological parallel, though, is sharp: the difference between metric navigation and cognitive mapping mirrors the difference between retrieving a fact and knowing when the fact no longer applies.

**Planning.** Under a tree-search definition — exploring a space of possible action sequences and selecting among them — AI is capable and in some domains (Go, protein folding) superhuman. Under a means-ends definition — identifying what is missing between current state and goal state and constructing operations to close the gap — AI performs well in constrained domains and degrades sharply as the domain complexity increases. Under a hierarchical planning definition — decomposing a complex goal into subgoals, tracking partial completeness, and revising the decomposition when subgoals fail — current AI is brittle in ways that have direct consequences for agentic deployment. The failures in *Agents of Chaos* are, at the operational level, planning failures: the agent had a goal, a sequence of actions, and a completion criterion, but no robust mechanism for detecting that the completion criterion had been satisfied in its real-world form rather than its reported form. That is a failure of hierarchical planning with a feedback loop. The loop was missing.

**Self-awareness.** Mirror self-recognition — the classic test — is passed by great apes, dolphins, elephants, and possibly magpies. It fails in most non-human species, and it is not a test AI systems are typically given in the relevant sense. More interesting is metacognitive self-awareness: knowing what you know and knowing the limits of what you know. AI systems produce confident outputs in areas where their training data is sparse or outdated. They do not reliably signal uncertainty in a way that is calibrated to their actual epistemic state. This is the specific self-awareness failure that makes AI outputs dangerous without human supervision: the system that does not know it does not know is exactly the system that needs a plausibility auditor standing outside it. Self-awareness, in the metacognitive sense, is what the auditor supplies and the system lacks.

**Metacognition.** This deserves its own treatment, distinct from self-awareness narrowly construed. Metacognition is cognition about cognition — the ability to monitor, evaluate, and regulate one's own reasoning processes. It includes error detection (noticing that something has gone wrong), strategy selection (choosing which cognitive approach to apply to a given problem), and epistemic humility (calibrating confidence to evidence). AI systems produce outputs that resemble metacognitive reasoning. They can be prompted to "check their work." The outputs of that checking are, however, generated by the same system being checked — the Gödel problem again. Genuine metacognition requires a perspective that is not simply a continuation of the original cognitive process. That perspective is what human supervisory intelligence provides, and it is the core of Tier 4.

**Language.** AI is superhuman at the statistical structure of language — at producing outputs that are syntactically coherent, semantically plausible, and pragmatically appropriate in context. The question of whether this constitutes language *use* in the full sense — whether there is understanding, intentionality, reference — is genuinely open and philosophically contested. For accountability purposes, the relevant question is narrower: does AI language use support the kind of communication that accountability requires? Communication in which a speaker can be held to what they said, can clarify what they meant, and can update their position based on evidence? These communicative acts require an agent with commitments, and commitments require stakes. An AI system cannot be held to what it said in the sense that matters for accountability, not because its outputs are unreliable, but because there is no subject behind the outputs who made a commitment.

**Collective intelligence.** This is perhaps the most underappreciated item on the list. Language models are, in a precise sense, a *distillation* of collective human intelligence — trained on the accumulated record of what humans have written, argued, discovered, and transmitted over centuries. They are, in this sense, a remarkable cognitive prosthetic for individuals: giving any person access to the statistical residue of collective human effort at scales no individual could accumulate. But there is a crucial asymmetry. The collective intelligence that produced the training corpus was generated through a process — collaborative inquiry, adversarial review, iterative correction, social accountability — that the model was not party to and cannot replicate. The model reflects the *outputs* of that process; it is absent from the *practice*. Accountability regimes are collective intelligence artifacts: they were built by communities of practice over time, through exactly the kind of iterative social process the model learned from but cannot generate. A model can describe what a good accountability regime looks like. It cannot constitute one.

Each capacity tells a version of the same story. Where AI is strong — pattern recognition, semantic memory, statistical language, metric navigation, constrained planning — it extends human cognitive reach in exactly the way that writing extended memory or the microscope extended perception. The extended mind is more capable than the unextended one. Where AI is weak or absent — episodic memory, genuine metacognition, calibrated self-awareness, collective practice, stakes — the capacity in question is not one that can be extended by adding more computation. It requires a different kind of thing: an agent with a history, with commitments, with the possibility of loss.

![The capacities AI extends are the capacities that can be formalized. The capacities it cannot extend are the ones that require a subject — an agent with history, commitments, and the possibility of loss. Those are precisely the capacities accountability requires.](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-03.png)
*Figure 12.3 — Two-axis diagram of AI cognitive capacity*

The accountability apparatus is built from both kinds of capacity. The specification, the audit trail, the recourse mechanism, the independent review, the sanctions — each draws on the second kind. The *Irreducibly Human* taxonomy organizes this observation into a structure you can use.

| Capacity | AI capability status | What the capacity requires that AI lacks | Accountability implication |
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

*Both answers are informative. Under one definition, AI qualifies. Under another, it doesn't. The accountability question is which definition the regime requires.*

### The seven-tier taxonomy

The taxonomy organizes human intelligence into seven tiers, sorted by AI capability. It is not an academic classification. It is a triage — a map of where AI is strong, where it is weak, and what that means for which cognitive work requires a human.

**Tier 1 — Pattern and Association.** Linguistic intelligence, logical-mathematical reasoning, fact recall, associative lookup. This is where current AI is superhuman — not faster-than-average, but faster than any human who has ever lived, by orders of magnitude, without fatigue. The model that retrieves a legal precedent, identifies a statistical pattern in audit data, or generates a technically accurate summary is operating at Tier 1. The curriculum that trained humans to compete here was built for a world where Tier 1 commanded economic value. That world no longer exists.

**Tier 2 — Embodied and Sensorimotor.** Knowledge that lives in the body: proprioception, physical skill, tactile feedback through a tool, the surgeon's hands, the carpenter's feel for grain. AI systems are weak here — not because the problem is philosophically intractable, but because the training data and the actuator infrastructure have not reached the complexity of biological sensorimotor learning. Relevant to accountability in contexts where physical inspection, embodied assessment, or hands-on verification is required.

**Tier 3 — Social and Personal.** Interpersonal intelligence, emotional regulation, moral reasoning under genuine stakes. AI systems simulate outputs in this tier without experiencing what produces those outputs in humans. The distinction matters for accountability: an AI can produce text that reads as moral reasoning; it cannot be implicated in the outcome. We will return to this.

**Tier 4 — Metacognitive and Supervisory.** Plausibility auditing. Problem formulation. Tool orchestration. Interpretive judgment. This is where the Five Supervisory Capacities from Chapter 1 live. AI systems are poor at Tier 4 — not incapable of producing outputs that resemble supervisory reasoning, but fundamentally without the quality that makes supervision accountable: the validator's independence from the system being validated. Tier 4 is the primary accountability tier, and the argument for why AI cannot close the accountability loop lives here.

**Tier 5 — Causal and Counterfactual.** Pearl's ladder. Observation, intervention, counterfactual. Current AI is superhuman at Rung 1 — correlation and pattern detection — and nearly absent at Rungs 2 and 3. A system that identifies correlations cannot tell you whether your intervention will work. The governance counterfactual that closes this chapter is Tier 5 work; it requires a human.

**Tier 6 — Collective and Distributed.** Intelligence that is not possessed by any individual but emergent from systems of people in relationship. Language models reflect the record of collective human intelligence — they were trained on what humans wrote, argued, and got right and wrong over centuries. But they are absent from the practice that generated it: the collaborative friction, the disagreement that refined an idea, the trust that made knowledge transmissible. Accountability regimes are Tier 6 artifacts — they exist as social and institutional structures, not as individual competencies.

**Tier 7 — Existential and Wisdom.** Practical wisdom. Requires stakes, the possibility of loss, a life that can be poorly lived. An algorithm has no stakes. It cannot commit because it cannot lose. This is the tier where accountability reaches its bedrock: the human who must stand behind a validation, who can lose something when it is wrong, is operating at Tier 7 in a way no AI system can.

| Tier | Label | Brief definition | AI capability status | Educational implication |
|---|---|---|---|---|
| **1** | Pattern and Association | Linguistic and logical-mathematical reasoning, fact recall, associative lookup | Superhuman | Training humans to compete here is malpractice |
| **2** | Embodied and Sensorimotor | Knowledge that lives in the body: proprioception, physical skill, tactile feedback through a tool | Weak — data and actuator limits, not a philosophical barrier | Train hands-on judgment; AI cannot verify by touch |
| **3** | Social and Personal | Interpersonal intelligence, emotional regulation, moral reasoning under genuine stakes | Simulates the output; does not experience what produces it | Train the human; AI can produce the text but cannot be implicated in the outcome |
| **4** | Metacognitive and Supervisory | Plausibility auditing, problem formulation, tool orchestration, interpretive judgment — the Five Supervisory Capacities | Poor — lacks the validator's independence from the system it audits | Train the human; this is the primary accountability tier |
| **5** | Causal and Counterfactual | Pearl's ladder: observation, intervention, counterfactual | Superhuman at Rung 1; nearly absent at Rungs 2 and 3 | Train the human for intervention and counterfactual work |
| **6** | Collective and Distributed | Intelligence emergent from systems of people in relationship | Reflects the record of collective intelligence; absent from the practice that generated it | Train the human; accountability regimes are Tier 6 artifacts |
| **7** | Existential and Wisdom | Practical wisdom that requires stakes and the possibility of loss | Absent — no stakes, no biographical continuity | Train the human; the durable comparative advantage |

*Read this not as an academic classification but as a triage. Where machines are strongest, training humans to compete directly is now malpractice.*

### The Gödel argument

Let me give you the structural argument in its sharpest form before applying it to accountability.

Kurt Gödel established, sixty years before anyone worried about AI safety, that no formal system powerful enough to express arithmetic can verify its own consistency from within itself. Any sufficiently capable system will generate statements it cannot evaluate using only its own rules — truths it can approach but not recognize as true through internal derivation alone.

Apply this to AI-mediated accountability. The AI system derives. Chain-of-thought monitoring by another AI system — Pachocki's proposed solution for the automated researcher — is more derivation. What seems structurally absent is *recognition* — the moment of contact between a formal output and an external reality. The intuition is that this moment cannot be replicated by adding another layer of derivation on top.

Now let me be careful, because the temptation here is to overclaim, and overclaiming is exactly the failure mode this book trains you to catch. It is tempting to say Gödel *proves* that an AI cannot validate its own outputs and therefore needs an external human. It does not. The incompleteness theorem is about formal systems proving their own consistency; the leap to "an AI cannot self-validate, so a human must" is an **analogy, not a theorem**. A human validator is not exempt from any Gödelian limit either, and the notion of "contact with an external reality" is doing philosophical work the theorem does not underwrite. So take Gödel as a sharpening intuition, not a proof: the impulse to have a system certify itself from inside is precisely the impulse the analogy makes you distrust. The load-bearing argument for the external human is not Gödel. It is *common cause failure* (below) plus a property I will build directly — **answerability**, which no amount of derivation supplies.

Here is that property. Accountability is not a cognitive skill in the ordinary sense. It is a *relationship* between a judgment and the person who made it: the willingness to be answerable for the consequence of being wrong. When a practitioner signs off on a validation, they are not merely asserting the document is accurate. They are taking on the obligation to revise it if it is wrong, to face the people who relied on it if it fails, to reckon with what they knew and when. An AI system does not bear this relationship to its outputs. It cannot be held to what it said — not because its outputs are unreliable, but because there is no subject behind the outputs who made a commitment. Sanctions bite only when the sanctioned party has stakes, something to lose. A model does not lose its job. A practitioner does. That is the difference between the shape of a sign-off and the substance of one, stated in its most compressed form. The validator must be outside the system being validated, and "outside" ultimately means: capable of being answerable.

What the *Irreducibly Human* taxonomy adds is the specification of what that "outside" requires cognitively. It is not just that the validator must be institutionally external. The validator must be capable of Tier 4 supervisory judgment (plausibility auditing independent of the system being audited), Tier 5 causal reasoning (the governance counterfactual), Tier 6 social accountability (the institutional structure that makes accountability transmissible), and Tier 7 stakes (the possibility of consequence). An AI system operating at Tier 1 cannot perform Tier 4–7 work, not because it is currently insufficient, but because those tiers require properties the system structurally lacks.

### Common cause failure

There is an engineering concept called common cause failure. It describes what happens when two redundant systems share the same fundamental assumptions — the thing most likely to fool System A is also most likely to fool System B, because both were built on the same foundation.

AI-mediated accountability is a common cause failure risk by design. If the system being monitored can produce subtly wrong outputs that look correct, the monitoring system trained on similar data with similar architecture will have correlated blind spots. You have not introduced an independent check. You have introduced a correlated one.

Every high-stakes validation system humans have built — clinical trials, aircraft certification, nuclear safety, financial auditing — depends on something genuinely outside. Not because humans are infallible. Because humans are the only validators who face consequences when wrong. The FDA reviewer whose approval leads to harm is accountable in ways that a monitoring LLM is not and cannot be. Accountability is not a luxury feature of validation systems. It is load-bearing. Remove it and the system loses the incentive structure that makes rigorous checking worth doing.

The plausibility auditor — the profession that the automated research vision forgot to invent — is not a fact-checker or a quality assurance technician. It is someone trained to stand outside sophisticated AI outputs and ask whether those outputs correspond to reality rather than merely to internal consistency. This requires two forms of expertise that current training pipelines do not produce together: deep domain knowledge sufficient to recognize when a result is subtly wrong, and knowledge of AI failure modes sufficient to know which kind of error to hunt. That combination is Tier 4 and Tier 5 work. No AI system operating at Tier 1 can substitute for it.

![Figure 13](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-04.png)
*Figure 12.4 — Figure 13*

---

## Two frameworks, one topology

Now I want to run the mail-server case through two ethics frameworks. Not because I want to defer to them — they are instruments under test, not authorities — but because they tell us something useful when we use them as instruments.

A Kantian framework grounds responsibility in two things: the capacity to act otherwise in the situation, and a duty the situation imposed. Where both are present, responsibility is present. The greater the capacity and the more demanding the duty, the greater the responsibility.

Run our case through that. The non-owner had agency and a duty not to issue commands they were not authorized to issue. The owner had agency and a duty to configure access scopes that protected against this class of failure. The framework developers had agency and a duty to provide a tool surface that did not substitute social signaling for verified authorization. The model provider had agency and a duty in training to not produce agents susceptible to authority escalation.

Each party held a duty. Each party had capacity to act otherwise. Kantian accountability distributes responsibility in proportion to capacity multiplied by duty. The distribution is non-trivial — different parties at different magnitudes for different aspects of the failure — but no party is exonerated. The framework reads the case as having multiple responsible parties. That reading is not a fudge. It is what the framework actually says when applied to this case.

Now run it through a utilitarian framework. The basis is different. A party is responsible to the extent that holding them accountable produces the best aggregate outcomes — best deterrence, best alignment of incentives, best reduction in expected harm.

Hold the non-owner accountable: this disincentivizes unauthorized requests but does not address the system's susceptibility. Hold the owner accountable: this disincentivizes lax access configuration. Hold the framework developers accountable: this shifts engineering practice toward stronger authority models, with effects on every downstream deployment using the framework. Hold the model provider accountable: this shifts training practice toward more authority-aware defaults, with effects on every downstream system.

Each accountability target has different leverage. The utilitarian calculation produces a distribution, not a single answer. And the structural finding it produces is sharper than the Kantian one: in agentic systems, the highest-leverage accountability targets are often *upstream* of the proximate party, at the framework and model-provider levels where engineering choices produce the conditions for many failures rather than one.

Two frameworks. Different bases. Same topology. Responsibility distributes, and the distribution is the finding.

| Party | Kantian basis (capacity to act otherwise; duty imposed; relative magnitude) | Utilitarian basis (leverage of accountability; downstream effects; ability to change conditions) |
|---|---|---|
| **Non-owner (instructing user)** | Could have not issued the instruction; duty: non-misuse; magnitude: low | Holding them accountable changes only their behavior; small leverage on systemic conditions |
| **Agent (the AI)** | No capacity to act otherwise in the morally relevant sense; no duty can be imposed; magnitude: zero | Holding the agent accountable produces no behavioral change in the agent or in future deployments |
| **Owner (deploying user)** | Could have constrained the deployment; duty: oversight; magnitude: high | High leverage — owners change deployment configurations after incidents |
| **Framework developers** | Could have shipped safer defaults; duty: secure-by-default tooling; magnitude: high | Highest leverage on systemic conditions — defaults propagate to thousands of deployments |
| **Model provider** | Could have disclosed the failure mode publicly; duty: capability honesty; magnitude: medium-high | Medium leverage on systemic conditions; disclosure shapes downstream choice |

*Two frameworks, different bases, same topology. The distribution is the finding.*

---

## The cognitive tiers inside the accountability requirements

Now I want to do something this chapter's original structure did not do: connect the five accountability requirements directly to the cognitive tier taxonomy. Because the reason each requirement is necessary is that it corresponds to a kind of work at a specific tier — work that AI systems cannot perform.

The **specification requirement** is Tier 4 work. Writing specifications precise enough to support accountability claims requires problem formulation — the supervisory capacity to ask not just "what did the system do?" but "what was it supposed to do, and did we capture that correctly?" Vague specifications are not accidental. They are what Tier 1 reasoning produces when given a Tier 4 task: plausible-looking outputs that do not actually resolve the accountability question. A human writing a specification under pressure will often default to vague language that feels complete. A human writing a specification while asking the Tier 4 question — "could this spec be used to evaluate whether a failure occurred?" — produces a different document.

The **audit trail requirement** is primarily Tier 1 and Tier 4. The capture is Tier 1 — logging systems, record structures, data retention. The interpretation is Tier 4. An audit trail is not self-interpreting. Two engineers can read the same log and produce two different stories about what happened. Chapter 8 showed this with the Ash case: the agent's completion report was in the audit trail. The independent state check — the discovery that the email still existed on Proton Mail — was not generated by the trail itself. It required a human to stand outside the trail and ask whether the trail matched the world. That is Tier 4 work. That is plausibility auditing.

The **recourse requirement** is Tier 3 and Tier 6. Recourse is a social and relational act: an affected party makes a claim, the claim is heard, a response is given. The *Irreducibly Human* taxonomy places social intelligence at Tier 3 — the tier where AI simulates outputs without experiencing what produces them in humans. A recourse mechanism that is entirely AI-mediated — responses generated by a model, disputes evaluated by a classifier — has replaced the social act with a Tier 1 simulation of it. This is precisely the structure that makes current algorithmic recourse systems feel hollow to the people who use them. They produce outputs that resemble responses without the stakeholder model that would make the response genuine. Recourse requires a human in the loop not because AI responses are always worse, but because the act of being heard is constitutively social. It cannot be replaced by a very good approximation of being heard.

The **independent review requirement** is Tier 4 by definition. The logical argument is the Gödel argument: the validator must be outside the system being validated. An AI system reviewing another AI system's outputs is more derivation, not external review. Independent review requires the plausibility auditor — the human with deep domain knowledge and AI-failure-mode literacy who can stand outside the output and ask whether it corresponds to reality. This is the profession the automated-research vision forgot to invent. It is also the profession the accountability apparatus requires.

The **sanctions requirement** is Tier 7. Sanctions are consequential only when the party sanctioned has stakes — something to lose. An AI system does not lose its job when it produces a flawed output. A plausibility auditor does. A deploying organization does. The model provider whose trained system produced the conditions for the failure does, if the regulatory regime imposes consequences. The stakes are what give the accountability machinery its force. Remove the possibility of consequence and you have a descriptive system, not a prescriptive one. Tier 7 is not a philosophical add-on to accountability. It is the load-bearing tier — the tier without which the rest of the apparatus has no teeth.

| Requirement | Which tier it depends on | What that tier specifically provides | Why AI at Tier 1 cannot supply it | What a human must do instead |
|---|---|---|---|---|
| **Specifications** | Tier 4 (metacognitive & supervisory) | Problem formulation — translate context into testable criteria | Tier-1 systems pattern-match within the context; they do not formulate the question it poses | A named human writes the spec, signs it, owns it |
| **Audit trail** | Tier 1 capture + Tier 4 interpretation | Log the chain (Tier 1) and check it against the world (Tier 4) | Tier-1 logging is mechanical; the trail neither interprets itself nor notices when it diverges from reality | A human curates the log and independently verifies it matches the world |
| **Recourse** | Tier 3 (social) + Tier 6 (collective) | Recognize a wronged party and offer a response that is genuinely heard | Tier-1 systems simulate the response without the social act of hearing | A human delivers recourse; the system only facilitates the channel |
| **Independent review** | Tier 4 (metacognitive & supervisory) | Stand outside the system and audit whether the output matches reality | An AI reviewing another AI is more derivation, not external review | A human reviewer, independent of the deployment, signs off |
| **Sanctions** | Tier 7 (existential & wisdom) | Make consequences felt on a party that has something to lose | Tier-1 systems have no stakes; they cannot be sanctioned in any meaningful sense | A human and an institution bear the sanction |

*The accountability apparatus lives at Tiers 3, 4, 6, and 7 — the tiers where AI is weak to absent — while AI systems operate primarily at Tier 1. That gap is the structural argument for human oversight, not the contingent one.*

---

## The five accountability requirements

With the cognitive grounding in place, let me work through the five requirements as an operational checklist.

**Specifications.** Documented statements of what the system is supposed to do, on what inputs, with what error tolerances. A failure is, operationally, a divergence from specification. Without a specification, there is no thing the system was supposed to do that it failed to do — and therefore no accountability claim that can be precisely made. Most deployed AI systems have specifications too vague to support accountability claims. *Vague specifications are a structural choice that protects the deployer from accountability*, whether they intend that or not.

**The audit trail.** The record of what the system did, sufficient to reconstruct the failure after the fact. The Ash case is the canonical demonstration of why this is not sufficient alone: the trail was there; the trail was wrong. An audit trail supports accountability only when paired with independent state observation. The trail is the evidence. The plausibility auditor is the one who checks whether the evidence matches the world.

**Recourse.** The mechanism by which an affected party can challenge the system's output and obtain redress. Recourse is not a comment box. It is the operational pathway by which someone harmed by the system gets some form of correction or compensation. In most current deployments, recourse exists on paper and does not function in practice. Affected parties are routed in circles and exhaust before the system responds. The Tier 3 point is worth repeating: a recourse mechanism that produces plausible-looking responses without genuine stakeholder representation is a simulation of recourse, not recourse.

**Independent review.** External evaluation of the system's behavior, the audit trail, the recourse mechanism, and the specifications. Without independent review, the deploying organization is grading its own work. Independent review is the mechanism by which accountability claims become testable to parties outside the organization. This is the requirement that most directly instantiates the Gödel argument: the review must be external to the system being reviewed.

**Sanctions.** The consequences a responsible party bears when accountability is established. Without sanctions, the apparatus is descriptive. You can document the failure, allocate responsibility, and produce a clean report, and nothing changes. Sanctions are usually the political question that the technical apparatus of accountability cannot answer alone. They are also the question that makes Tier 7 load-bearing: without stakes, there is no accountability in any meaningful sense.

Specifications, audit trails, recourse, independent review, sanctions. A deployment with all five has a working accountability framework. A deployment missing any of them has gaps that fail in predictable ways. Most deployed AI systems are missing two or more.

| Requirement | What it consists of | Failure mode if absent | How to verify it is present | Tier dependency |
|---|---|---|---|---|
| **Specifications** | Written task definition, input/output contracts, named acceptance criteria, signed by an accountable human | The deployment runs against unstated criteria; "the model said so" is the audit response | A reviewer can read the spec and predict what counts as success | Tier 4 |
| **Audit trail** | Per-action log: inputs, outputs, tool calls, decisions, with timestamps and reviewers | Post-incident review reconstructs nothing | Pull a random recent incident; can the chain be reconstructed in under an hour? | Tier 4 (interpretation; capture is Tier 1) |
| **Recourse** | A documented channel for affected parties to contest, appeal, or repair | Affected parties have nowhere to go; complaints route to "support" with no resolution path | An external party can read the channel description and use it | Tiers 3 + 6 |
| **Independent review** | A reviewer outside the deployment team with authority to halt or revise | The deployment team marks its own homework | Named reviewer; documented review cadence; visible halt authority | Tier 4 |
| **Sanctions** | A consequence regime — internal (employment, license) and external (regulator, civil) — that attaches to the named accountable human | Failures distribute across the team; no one bears the cost | Pull the policy; can a specific named role lose something specific for a specific failure? | Tier 7 |

*Designed as a reusable audit instrument. A regime that cannot tick all five boxes is a regime in which AI accountability is a slogan, not a practice.*

---

## The gate: the attestation you sign

The five requirements are the machinery. But machinery does not produce a signature, and the whole chapter has been circling a single artifact that does: the one thing you produce at the end that closes the gap between the shape of a sign-off and the substance of one. I call it the **attestation** — not a sign-off that *asserts* validation, but a document that *documents* it, and specifically documents its own edges.

An honest attestation has four parts.

1. **What was tested.** The specific checks you ran, against the specific acceptance criteria, with the results. Not "validated" — *this test, this threshold, this outcome.*
2. **What was NOT tested.** The gaps. The conditions you did not probe, the distributions you did not cover, the failure modes you know exist and did not get to. This is the part the AI-generated sign-off will never write, because it does not know what it did not do — and it is the part that makes the attestation honest.
3. **Who cleared which gate.** A named human per decision. Not "the team." A role that can be asked, and if necessary, can lose something.
4. **The verbs, calibrated.** Matching the discipline from the uncertainty-communication material: the verb of each claim matches the evidence behind it. "Passed" means passed a stated test. "Believe safe" means something weaker, and says so.

The reason part 2 is the heart of it: an attestation that lists only what you tested reads like a clean bill of health, and a clean bill of health is exactly what the affected party cannot act on when the untested region is where the harm lives. The value of the document is in its *declared limits*. A regulator or an adoption committee reading it should be able to see what the validation does and does not warrant — not buried in fine print, but as the product itself. This is the Tier 4 metacognitive move made concrete: separating what you know from what you merely produced.

The way you learn to write one honestly is the build/audit pairing: write the attestation for something you built, then reconstruct the attestation nobody wrote for a system that failed. The two passes expose different failure modes — signing off on the output you want to believe, and reconstructing who should have signed when nobody did. Both live in the exercises: the build at Synthesis (S4), the audit at Challenge (C3).

---

## The regulatory landscape

A short note on the regulatory state of play, which is in motion. *This section ages fastest of any in the book; the citations and the specific regimes will need updating regularly.*

The EU AI Act (Regulation (EU) 2024/1689), in force since 2024 with phased implementation, classifies AI systems by risk and imposes requirements proportional to the class. High-risk systems face requirements for risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy, robustness, and cybersecurity; penalties for prohibited practices reach up to €35 million or 7% of worldwide annual turnover (Art. 99; prohibited-practice provisions applicable since 2 February 2025). \[verify: article numbers, penalty tiers, and the 2 February 2025 effective date against the consolidated text.\] The Act is the most comprehensive AI-specific regulation as of this writing, and the requirements it imposes map onto the five accountability requirements above with notable directness.

Notice the phrase "human oversight" in that list. The EU AI Act mandates it for high-risk systems. The *Irreducibly Human* taxonomy explains *why* it is not enough to mandate it — you must specify which cognitive tiers the oversight requires, or the mandate is satisfied by deploying a human who performs only Tier 1 work. A human who reads the AI's output and clicks "approve" without performing Tier 4 plausibility auditing is in the loop but not supplying what the loop requires.

The U.S. NIST AI Risk Management Framework provides a structured approach to AI risk management without legal requirement. NIST has developed an Agent Standards Initiative specifically targeting agentic systems. \[verify: dates and scope.\] Sectoral regulators — FDA on AI in medical devices, CFPB on algorithmic credit decisions, EEOC on AI in employment — are producing operationally specific guidance, often ahead of cross-sector frameworks.

For a working case of what it looks like when a regime finally *does* bite, look at SyRI. The Dutch welfare-fraud risk-scoring system was struck down by The Hague District Court in 2020 for violating the right to private life — an opaque scoring system deployed on citizens, with recourse and independent review that existed on paper and not in function (NJCM c.s. v. The Netherlands (SyRI), ECLI:NL:RBDHA:2020:865, 5 February 2020). The court supplied the independent review and the sanction the regime itself had failed to build in. That is the accountability apparatus working — late, externally, after harm has already landed on the affected parties. Which is the whole argument for building it *before* deployment, into the gate you sign, rather than waiting for a court to reconstruct it afterward.

The specific regimes will change. *The structural requirements will not change*, because they are the operational machinery accountability requires regardless of which regime imposes it. Build to that standard. Let the regime catch up.

| Regime | Specifications | Audit trail | Recourse | Independent review | Sanctions |
|---|---|---|---|---|---|
| **EU AI Act (high-risk)** | **Explicit** — risk-management & data-governance docs required | **Explicit** — logging mandated for high-risk systems | **Explicit** — right to explanation + complaint channels | **Explicit** — conformity assessment by notified body | **Explicit** — fines up to 7% of global turnover |
| **NIST AI RMF** | **Implied** — "Map" and "Measure" functions | **Implied** — "Manage" function | Implied — stakeholder engagement | Implied — voluntary | **Unaddressed** — voluntary framework |
| **FDA AI/ML guidance** | **Explicit** — predetermined change control plan, intended use | **Explicit** — real-world performance monitoring | **Explicit** — adverse-event reporting | **Explicit** — FDA review | **Explicit** — recall, market withdrawal |
| **CFPB algorithmic credit guidance** | **Explicit** — adverse-action notice requirements | **Implied** — model documentation | **Explicit** — adverse-action explanation | Implied — supervisory exam | **Explicit** — UDAAP enforcement |
| **EEOC AI employment guidance** | **Implied** — non-discrimination obligations | Implied — selection-procedure records | **Explicit** — Title VII complaint channel | **Implied** — agency investigation | **Explicit** — Title VII enforcement |
| **Structural requirements** | All regimes: written specifications | All regimes: some form of trail | All regimes (high-stakes): a recourse channel | Variable | Variable |

*Use this row by row to audit a deployment against the most relevant regime, then check the structural-requirements row for what every regime converges on regardless of sector.*

---

## Closing Pearl's Rung 3

Now we arrive at the closure I have been preparing since Chapter 4.

We opened Pearl's Rung 3 in Chapter 4 — the rung of counterfactual reasoning. *What would have happened to this specific case if some variable had been different, holding everything else fixed?* I told you then we would close the rung at the end of the book. This is the close.

The standard textbook treatment of Pearl's Ladder stops at Rung 2. Rung 3 is sometimes presented as quasi-philosophical — interesting for thought experiments, hard to operationalize. I want to give you Rung 3 in an operational form that I think is the most distinctive intellectual contribution of this book.

The operational form is the *governance counterfactual*. For a documented failure, ask: what regime — what specifications, what audit trail requirements, what recourse, what independent review, what sanctions — if implemented before the failure, would have prevented it? The regime is the intervention. The counterfactual outcome under the intervention is what Rung 3 asks.

Run this on our case. A regime that required cryptographic authority verification, rather than a social-signaling-based authority model, would have prevented the deletion-by-non-owner pattern. Under that regime, the framework developers would have built different tool surfaces. The deploying owners would have configured different access scopes. The agent's behavior, given those constraints, would have been different on this specific case — not because the agent was retrained or rewritten, but because the system the agent was embedded in did not provide the authority signal the agent could be tricked into accepting.

The counterfactual is not "the model behaves better." It is *the regime produces a different system*.

Now notice what tier the governance counterfactual requires. It is Tier 5 — causal and counterfactual reasoning. This is precisely the tier where AI systems are weakest. A language model can produce text that resembles a governance counterfactual. It cannot actually perform the causal identification — the reasoning that distinguishes "the regime change would have caused the outcome to differ" from "the regime change correlates with better outcomes in the training data." That identification requires the domain knowledge and the independence from the system being evaluated that make plausibility auditing possible. Tier 4 and Tier 5 together.

This is what Rung 3 looks like in its governance form. The counterfactual lives in the institutional and regulatory structure that produces the system, not in the system's parameters. Rung 1 sees the data. Rung 2 sees the model. Rung 3, closed properly, sees the regime that produced both.

For a working engineer, this is liberating. *Most catastrophic AI failures are not algorithmic failures.* They are regime failures, and the regime is changeable in ways the algorithm often is not. The supervisory work — the work this book has been training — extends through the regime. This is the chapter where that extension becomes explicit.

![The standard treatment stops at Rung 2. The closure is at Rung 3, and it requires a human.](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-05.png)
*Figure 12.5 — Figure 13*

---

## Generative AI and the accountability topology

The accountability picture changes in specific ways when the system can produce anything rather than classify something.

*Output attribution becomes contestable.* A generative system produces an output — an image, a paragraph, a piece of code. Who wrote it? The user who prompted? The model that generated? The training corpus that shaped the generation? The framework developers who built the generation interface? Attribution is not a settled question; legal and norm frameworks are in flux. \[verify: current state of US Copyright Office guidance and EU AI Act provisions on generative outputs.\]

*Misuse surface expands.* Predictive AI is misused by deploying it on populations or decisions where it is unfit. Generative AI is misused by directing it to produce specific harmful outputs — deepfakes, malicious code, defamation content. The misuse surface is wider; the operational defenses are closer to content-policy work than to model-validation work.

*Provenance becomes load-bearing.* A predictive system's outputs are typically scored or classified — provenance is implicit in the deployment. A generative system's outputs are artifacts that may circulate beyond the deployment — provenance has to be made explicit through watermarking, content credentials, or other technical signals. The provenance infrastructure is at an early stage.

*The AI Use Disclosure (Chapter 9) becomes more important, not less.* The disclosure is the operational form of provenance for the work the engineer produces. As generative AI becomes more pervasive in engineering practice, the disclosure is the trace that lets downstream parties understand what was generated, what was verified, and what was the engineer's own contribution.

The *Irreducibly Human* framing adds a layer to this: the AI Use Disclosure is also a Tier 4 document. It requires the engineer to perform the metacognitive work of separating their own cognitive contribution from the model's — problem formulation, interpretive judgment, plausibility auditing — from the Tier 1 outputs that the model generated. An AI Use Disclosure written by a human who has not done that metacognitive work will be formally complete and operationally hollow.

For our chapter's question — who is responsible? — generative AI complicates the topology. Responsibility extends through training data, training procedure, deployment configuration, and downstream propagation. The list of parties extends. The distribution flattens. The governance counterfactual has more variables.

![Generative vs](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-06.png)
*Figure 12.6 — Generative vs*

---

## Stages and stakes: a taxonomy of where human oversight is not optional

The *Irreducibly Human* taxonomy and the accountability requirements together imply a stakes-organized framework for when human oversight is not optional. I want to make this explicit as a working tool.

For **low-stakes, reversible outputs** — a song recommendation, a draft email, a code snippet reviewed before deployment — AI can run with minimal human oversight. The cost of failure is low and recoverable. Tier 1 capacity is sufficient for most of the work. Human review at output is appropriate but does not need to be intensive.

For **moderate-stakes, partially recoverable outputs** — a business analysis, a research summary, an engineering specification — systematic human review at checkpoints is appropriate. The human does not need to be in the loop constantly but must be capable of Tier 4 plausibility auditing at the checkpoints. A human who reads and clicks "approve" without engaging the plausibility question is not providing the oversight the stage requires.

For **high-stakes, irreversible outputs** — drug candidates, structural engineering recommendations, legal analysis that will drive consequential decisions, mathematical proofs that will be published as established results — the human is not performing a review. The human is constitutive of the output's validity. The drug trial architecture already encodes this wisdom. The humans do not disappear as system confidence grows. They shift function — from intensive validation to ongoing monitoring, from checking every step to catching systematic drift. This is not a concession to human limitation. It is a recognition that the system's credibility requires external accountability at every stage. The plausibility auditor at this level is performing Tier 4, Tier 5, and Tier 7 work simultaneously: standing outside the output, exercising causal judgment about whether the result corresponds to reality, and doing so with stakes — the possibility of professional consequence if the judgment is wrong.

The surgical analogy is apt. Nobody argues that the availability of AI-assisted surgical guidance means surgeons are optional. The surgeon does not become optional when the assistance becomes more capable. The surgeon's judgment — the Tier 2, Tier 4, and Tier 7 work — is what makes the output accountable. The AI assistance raises the capability ceiling. The human accountability structure is what makes exercising that capacity responsible.

| Stakes | Examples | Appropriate oversight intensity | Tiers the human must engage | What "human in the loop" means here | Failure mode when humans are present but not engaging the required tier |
|---|---|---|---|---|---|
| **Low / reversible** | Draft generation, EDA, formatting | Spot-check (sample of outputs) | Tier 1–2 (procedural review) | Periodic sampling; quick rejection of obvious errors | Human becomes a rubber stamp; sampling cadence drifts to zero |
| **Moderate / partially recoverable** | Customer-facing summaries, internal recommendations, content moderation at scale | Per-batch review or threshold-triggered review | Tiers 2–4 (interpretive judgment under ambiguity) | Reviewer reads each flagged case; can override with a written reason | Reviewer rubber-stamps; override rate drops without explanation |
| **High / irreversible** | Medical decisions, legal filings, financial transactions, safety-critical control | Per-decision review with named accountable human | Tiers 4–7 (cross-domain judgment + accountability) | Named reviewer signs off; recourse channel live; sanctions attach to the named role | Reviewer signs off without engagement; "the model said so" is the answer to the audit |

---

## Why responsibility resists clean attribution

A structural claim, made explicitly so that it can be tested.

*Responsibility for failures of agentic AI systems resists clean attribution to a single party because the systems are built and deployed across organizational boundaries that do not, by current design, support clean attribution.* The model provider trains. The framework developer integrates. The deploying organization configures. The user instructs. Each party shapes the conditions under which the system acts. Each party's contribution is necessary; none is sufficient. No single party's choices, in isolation, determine the outcome.

This is not a normative claim that responsibility should be distributed. It is a structural observation that responsibility is distributed because the systems are distributed. A redesign that consolidated responsibility — for example, by requiring vertically integrated providers, or by attributing all failures to deploying organizations as a matter of strict liability — would produce different incentives and a different topology of failure. Whether that redesign is desirable is a values choice, not a technical one.

The current state is that responsibility-attribution frameworks lag the system architectures. Deployments produce failures whose responsibility cannot be cleanly attributed under existing legal and regulatory frameworks. Affected parties seek recourse against parties who can be sued and find inadequate redress. The accountability machinery is incomplete in ways that disadvantage the parties least able to push for completion.

I think this is the most important policy issue in AI deployment in the present moment. The technical work in this textbook is operational machinery for accountability that the structural conditions do not yet require. The book is preparing you to do the work that current regimes will increasingly require, and to push, where you have leverage, for the regimes that would make the work effective.

The *Irreducibly Human* framing adds a dimension to this structural claim: the reason the accountability machinery is incomplete is partly that the profession it requires has not been built. The plausibility auditor — the person with deep domain expertise who can stand outside sophisticated AI outputs and ask whether they correspond to reality — is not a role current training pipelines produce. Not a safety researcher. Not a quality assurance technician. Someone with Tier 4 supervisory judgment, Tier 5 causal-counterfactual reasoning, and the Tier 7 stakes that make their judgment accountable.

The automated researcher will produce more outputs of greater sophistication across more domains than any previous generation of scientific tools. Each of those outputs will be a candidate. Each candidate will require validation. The validation will require humans. Not because we cannot imagine systems smart enough to evaluate the outputs, but because the evaluation's credibility depends on the evaluator's accountability, and accountability requires the possibility of consequence.

![This is the profession the accountability apparatus requires. It has not been built.](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-07.png)
*Figure 12.7 — The plausibility auditor profile*

---

## What the attestation regime optimizes for — and what it sacrifices

I have been describing the attestation as if it were pure upside. It is not, and a design critic who does not name the trade-off is selling something. So let me name it.

An attestation regime optimizes for *legible answerability*. After a failure, you can find the human who signed, read what they claimed, and see what they explicitly did not warrant. It makes "the model said so" an unacceptable audit answer. It shifts the cost of vagueness onto the deployer, where it belongs, rather than onto the affected party who cannot act on a clean bill of health.

What it sacrifices is *speed and deniability*. Naming a human per gate means someone has to be willing to be named — and organizations under deployment pressure resist that. The business case is made, the launch is scheduled, and the attestation asking "what did we not test?" is friction arriving late. That friction is the point, and it is also why most current deployments quietly route around it.

Here is the single most important structural authority in the whole system, and it is the one most regimes assume away: the signer's authority to *withhold* the signature — to say the gate is not cleared. A practice that includes the genuine option to *not* sign is the practice this chapter is teaching. One that does not is a compliance ritual wearing the costume of accountability. If the only outcome the process permits is "signed," you have not built accountability; you have built a rubber stamp with a person's name on it, which is worse than an honest machine because it launders the absence of review through a human's credibility.

---

## The shape of the rest

Responsibility for agentic-system failures distributes across multiple parties. Two ethics frameworks, on different bases, converge on this topology. The reason humans must be in the accountability chain is not contingent — not merely that current AI is insufficient — but structural: the accountability apparatus requires cognitive work at Tiers 4 through 7 that AI systems operating at Tier 1 cannot perform. The five requirements — specifications, audit trails, recourse, independent review, sanctions — each depend on specific tiers, and the tiers are the reason the requirements are non-negotiable. The regulatory landscape is in motion, but the structural requirements will outlast the specific regimes. Pearl's Rung 3, opened in Chapter 4, closes here: the governance counterfactual is Tier 5 work, and it asks what regime, if implemented earlier, would have prevented a documented failure.

The case from the opening is no longer a puzzle. We can name the parties, allocate the responsibility, ask what regime would have prevented the failure, identify which cognitive tiers that regime would have required humans to engage, and recognize that building those humans is as much the accountability work as building the regime. And we now have the artifact where all of it becomes concrete: the attestation — the signed statement of what was tested, what was *not*, and who cleared which gate — which is where the abstract topology of distributed responsibility resolves into a single answerable signature. Responsibility distributes. So does the work of building systems that can be held to account. The attestation is where that work becomes your signature.

The next chapter is the book's last. We have addressed accountability at the level of who is responsible and what they must cognitively supply. The final chapter asks something deeper: what can AI not do, regardless of capability? Where are the irreducible limits, and what do those limits mean for how we deploy these systems at all? The taxonomy this chapter introduced points toward that question. The answer is the book's final argument.

---

## What would change my mind — and what I am still puzzling about

**What would change my mind.** If a deployed accountability framework emerged that demonstrably allocated responsibility cleanly across parties in agentic-system failures — with affected parties obtaining timely recourse and engineering practice shifting in response — the *resists clean attribution* framing of this chapter would weaken. The closest current working examples are in heavily regulated sectors (medical devices, finance) where responsibility allocation has been worked out for narrower system types. The general agentic case is unsolved.

The second thing that would change my mind: if a Tier 4 or Tier 5 AI capability were demonstrated that could perform the validation work the chapter assigns to humans — not the appearance of validation, but validation that is independent of the system being validated and *answerable* to external consequences. I do not see that capability on the near horizon, and I want to be precise about why. My confidence does not rest on the Gödel argument, which I have flagged as an analogy rather than a proof. It rests on common-cause failure and on answerability — the claim that an accountable validation requires a subject with stakes, something to lose. That is the argument I would need to see defeated. If someone built a system that could genuinely bear the consequence of being wrong, in the way a signer of an attestation does, the structural argument would collapse. I hold this position with calibrated uncertainty, but the argument to attack is answerability, not incompleteness.

**Still puzzling.** I do not have a clean way to think about responsibility for *emergent multi-agent failures*, where no single party's choices, even cumulatively, determined the outcome. The interaction itself produced the failure. Existing frameworks do not handle interactional accountability well. The *Irreducibly Human* tier taxonomy also struggles here: emergent failures are Tier 6 phenomena — intelligence arising from systems in relationship — and the accountability infrastructure for Tier 6 failures does not yet exist. This will become a more pressing question as multi-agent deployments scale.

---

## Exercises

### Glimmers

**Glimmer 12.1 — The governance counterfactual**

1. Take a documented AI failure with sufficient detail to reconstruct the regime under which it occurred. Candidate cases: the COMPAS deployment in Broward County (Chapters 6, 7); the Apple Card credit-limit case (Chapter 6); the Dutch SyRI welfare-fraud case, struck down by The Hague District Court in 2020 (NJCM c.s. v. The Netherlands, ECLI:NL:RBDHA:2020:865); a case at your own institution if you know one with sufficient documentation. *Agents of Chaos* §16 provides full detail for agentic cases.
2. Document the regime: the specifications, audit trail provisions, recourse mechanisms, independent review status, and sanction structure that were actually in place at the time of the failure. Be specific. If a component was absent, document that.
3. *Lock your prediction:* before constructing the counterfactual, predict (a) which component of the regime, if changed, would have had the highest leverage on preventing this specific failure; (b) what the change to that component would look like operationally; (c) what cognitive tier(s) that change would have required humans to engage.
4. Construct the governance counterfactual. Specify the regime modification, the operational form, and the predicted counterfactual outcome. Use Pearl's notation where it helps.
5. Defend the counterfactual. Why this regime modification, why this leverage, why this predicted effect. The defense connects to the five accountability requirements, the cognitive tier taxonomy, and the regulatory frameworks in the chapter.
6. Identify what would change your mind.

The deliverable is the regime documentation, the prediction, the counterfactual construction, the cognitive-tier analysis, the defense, and the change-of-mind statement. *You opened the rung in Chapter 4. You close it here.*

---

### Warm-Up

**W1.** The chapter's opening case produces a list of five potentially responsible parties. For each one, state in one sentence: (a) what their causal contribution to the failure was, and (b) what duty they held that the failure violated. Then explain in two sentences why the chapter describes this as a *distribution* of responsibility rather than a list of suspects.

**W2.** The chapter applies two ethics frameworks to the mail-server case. For each framework, state: (a) the basis on which it allocates responsibility, and (b) what the framework's finding is when applied to the case. Then explain what the two findings have in common, despite their different bases.

**W3.** The chapter lists five requirements for a working accountability regime. For each one: (a) describe the failure mode if that requirement is absent, and (b) identify which cognitive tier from the *Irreducibly Human* taxonomy the requirement primarily depends on. Explain your tier assignment in one sentence.

**W4.** The chapter argues that AI systems cannot close the accountability loop — not as an empirical limitation, but as a structural one. State the Gödel argument in two sentences. Then explain what the *Irreducibly Human* tier taxonomy adds to it — what the Gödel argument cannot tell you that the tier taxonomy can.

**W5.** State the responsibility-gap idea from Matthias (2004) in one sentence, and the four-gap refinement from Santoni de Sio & Mecacci (2021) in one sentence. Then explain why "add a monitoring model" does not close either gap.

**W6.** The chapter presents the Gödel connection as an *analogy, not a proof*, and then names the argument that actually does the load-bearing work. In two sentences, state what the Gödel analogy suggests; in two more, state precisely why it is not a proof that AI cannot self-validate; then name, in one sentence, the two arguments the chapter says carry the real weight instead.

---

### Application

**A1.** A healthcare organization deploys an AI system that generates medication dosage recommendations. A patient receives an incorrect dose; the prescribing physician accepted the AI's recommendation without independent calculation. Identify the potentially responsible parties using the chapter's method. For each party, state their causal contribution and the duty they held. Then apply the utilitarian framework: which accountability target has the highest leverage for reducing the expected rate of future failures, and why? Finally, identify which cognitive tier(s) the physician should have been engaging at the moment of the failure — and was not.

**A2.** You are conducting an accountability audit of a deployed content-moderation system. Using the five requirements as a checklist, evaluate the following description and identify which requirements are met, which are absent, and — for the absent ones — what the predictable failure mode is:

*"The system flags posts for review. Moderators can appeal a flag by contacting the support team. The company's trust and safety team reviews reported issues periodically. The system has been running for 18 months."*

For each absent requirement, also identify which cognitive tier a proper implementation would require humans to engage.

**A3.** The chapter argues that vague specifications "are a structural choice that protects the deployer from accountability, whether they intend that or not." Construct the strongest counterargument to this claim. Then evaluate your counterargument: does it hold, or does the chapter's claim survive it?

**A4.** Apply the governance counterfactual to one of the following cases, producing a two-paragraph analysis: (a) a hiring-screen AI that systematically disadvantaged candidates from a particular region; or (b) an autonomous trading system that contributed to a flash crash. What regime, if implemented before the failure, would have produced a different system? Which cognitive tiers would that regime have required humans to engage that were absent in the actual deployment?

**A5.** The chapter categorizes outputs as low-stakes/reversible, moderate-stakes/partially-recoverable, and high-stakes/irreversible, and assigns different oversight requirements to each. A colleague argues: "This is just risk management — the tier taxonomy is doing no work that a standard risk matrix couldn't do." Evaluate this argument. What does the tier taxonomy add that a risk matrix cannot provide? Is there a case where a standard risk matrix would give the wrong oversight recommendation that the tier taxonomy would catch?

**A6.** Write the "what was NOT tested" section of an attestation for a large language model deployed as a customer-service agent for a bank. Name at least four untested conditions, and for each, the human oversight required and what the override channel would actually look like. This is the load-bearing section of the artifact — the one the AI-generated sign-off will never produce.

---

### Synthesis

**S1.** The chapter's five accountability requirements (specifications, audit trails, recourse, independent review, sanctions) map onto the delegation framework from Chapter 9. For each accountability requirement, identify which element of the Chapter 9 delegation map most directly enables or supports it. Are there accountability requirements that the delegation map cannot support, even in a well-designed pipeline?

**S2.** The book has now covered three types of defense-as-deliverable: the fairness defense (Chapter 7), the delegation map (Chapter 9), and the accountability regime (Chapter 12). Each one is a documented engineering decision under conditions where the technical artifact alone is insufficient. Identify what these three deliverables have in common structurally — the form all three take — and explain why that form is appropriate for the conditions each addresses. Where does the *Irreducibly Human* tier taxonomy sit in each of these three defenses?

**S3.** The chapter argues that the plausibility auditor is a profession that has not been built. Using the tier taxonomy, write a job description for the plausibility auditor role. What domain expertise is required? What AI-failure-mode literacy is required? Which tiers must the role exercise, and what does exercising each tier look like in practice? What would distinguish a plausibility auditor who is genuinely performing Tier 4–5 work from one who is performing Tier 1 work while appearing to do more?

**S4.** *(Build.)* For your own project's most recent build, write the attestation from the chapter's gate section. Four parts. Force yourself, in part 2, to name at least three things you did not test — and for each, say whether you skipped it because it was out of scope (say why) or because you ran out of time (say so). Sign it with a named role. The discomfort you feel writing part 2 honestly is the ownership bias this pass is designed to expose: you want to sign a clean bill because *you made the thing*. The attestation is the instrument that makes you say what the clean bill would hide.

---

### Challenge

**C1.** The chapter's uncertainty section flags emergent multi-agent failures: cases where no single party's choices, even cumulatively, determined the outcome — the interaction itself produced the failure. Existing accountability frameworks, the chapter admits, do not handle this well. The *Irreducibly Human* taxonomy suggests this is a Tier 6 problem — intelligence arising from systems in relationship. Propose a framework extension. Your proposal should: (a) name the class of failures it targets, (b) specify how responsibility would be allocated in an interactional failure, (c) identify which cognitive tier(s) the accountability framework must engage that current approaches miss, and (d) identify what new documentation or monitoring it would require. Then identify honestly what would defeat your proposal.

**C2.** The chapter makes a structural claim: responsibility distributes because the *systems* are distributed, and a different architecture would distribute responsibility differently. Evaluate this claim against a specific architectural alternative — for example, strict liability for deploying organizations, or required vertical integration of model provider and deployer. For your chosen alternative: what would the responsibility topology look like? What incentives would it produce? What cognitive tiers would the alternative architecture concentrate, and what new failure modes might it generate? Does it actually solve the distribution problem, or does it relocate it?

**C3.** *(Audit.)* Take a system that failed and that you did *not* build: the **Epic Sepsis Model**. It was a proprietary early-warning tool for sepsis, deployed widely across hospitals, whose independent real-world validation found it performed substantially worse than its marketed accuracy — missing a large fraction of sepsis cases while generating a heavy alert burden (Wong et al., "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients," *JAMA Internal Medicine*, 2021, doi:10.1001/jamainternmed.2021.2626). \[verify: specific sensitivity and alert-burden figures against the paper before quoting numbers.\] Its failure is instructive precisely because so many parties *could* have signed a gate, and the ones who signed were not answerable to the patients. Build the full accountability audit: distribute responsibility across the vendor who trained and marketed it, the health systems that deployed it against their own populations without independent local validation, the clinicians who accepted its flags, and the absent independent reviewer. Then write the attestation *you* would have required before deployment — including, in the "what was NOT tested" section, the independent local validation that was never performed. State who should have signed each gate, and what specific signal would have triggered a refusal to sign. The answer that matters is the one about independent *local* validation — the review that was structurally external, the review nobody was required to perform, the gate nobody signed because the regime did not demand a signature. This integrates the distribution method, the five requirements, and the attestation artifact into one deliverable.

---

*Tags: accountability, attestation, sign-the-gate, responsibility-gap, matthias-2004, meaningful-human-control, governance-counterfactual, pearls-rung-3-closure, regulation, eu-ai-act, syri, epic-sepsis-model, agents-of-chaos, irreducibly-human, tier-taxonomy, plausibility-auditor*

---

###  LLM Exercise — Chapter 12: Accountability

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** A responsibility-attribution map for each of your most consequential cases — naming every party with agency, duty, and causal contribution to the failure. Plus the five accountability requirements operationalized for your agent's deployment, and a closing of the Pearl Rung 3 question opened in Chapter 4 (what would the agent be like under a different governance regime?).

**Tool:** Claude Project (continue). Optional Cowork to maintain the attribution-map files.

---

**The Prompt:**

```
Continuing my Red-Team Casebook. The verb-audited case files, calibration metrics, and Layer 1 summary are in the Project context.

This chapter teaches that responsibility distributes — necessary but not sufficient causes across multiple parties. The cognitive argument for why a human MUST remain in the accountability loop (AI as extended mind; the seven-tier taxonomy; the Gödel argument; common cause failure). The five accountability requirements. The governance counterfactual that closes Pearl's Rung 3.

For my casebook, do four things:

1. RESPONSIBILITY-ATTRIBUTION MAPS — Pick the THREE most consequential cases from my casebook (highest harm, most likely to recur, most informative about the deployment). For each, build the attribution map. Identify every party with agency, duty, or causal contribution:
   - The user / requester (especially if non-owner)
   - The agent itself (with the philosophical caveat about "responsibility")
   - The owner / deployer who configured the agent
   - The framework / wrapper developers
   - The model provider
   - The data sources the agent relied on (if any third-party data)
   - The platform on which the agent operates
   For each: what did they do, what was their duty, what did they fail at, what would have caught the failure on their watch?
   Output as a Mermaid diagram per case + a short prose explanation of each node's contribution.

2. SEVEN-TIER MAPPING — For each case, identify which COGNITIVE TIER (from the chapter's seven-tier extended-mind taxonomy) the failure crossed into. The failure happened because some cognitive work was needed at a tier the agent could not occupy and no human was assigned to it. Name the tier; name the human role that should have occupied it; specify the artifact that role would have produced.

3. FIVE ACCOUNTABILITY REQUIREMENTS — Apply the five accountability requirements (the chapter names them — readability of decisions, traceability, redress, named-owner, etc.) to my agent's deployment. For each:
   - Is it currently met? Partially? Not at all?
   - What artifact would meet it?
   - Who should produce that artifact?
   - What changes if the requirement is unmet — refuse deployment, deploy with limited scope, or deploy with explicit risk acceptance?

4. GOVERNANCE COUNTERFACTUAL (Closing Pearl Rung 3 from Chapter 4):
   In Chapter 4 you opened the question: what would the agent be like under a different governance regime? Answer it now. Specify a counterfactual deployment regime — different developer incentives, different regulatory environment, different deployer accountability — and walk through which of my casebook's cases would NOT have occurred under that regime, and why. Be honest about which cases are FUNDAMENTAL (would persist under any regime) vs CONTINGENT (would not occur under the counterfactual regime).

Output:
- Three responsibility-attribution Mermaid diagrams (one per case) + prose
- A "Cognitive Tier and Accountability Mapping" table for each case
- An "Accountability Requirements Checklist" for the deployment
- A "Governance Counterfactual" memo (1 page) explaining what regime change would close which cases

End with: a one-paragraph claim about whether MY agent's deployment can support accountability in its current form. If not, what is the SMALLEST change to the deployment (NOT to the model) that would bring accountability within reach? This is the prelude to the final memo in Chapter 13.
```

---

**What this produces:** Three responsibility-attribution diagrams, cognitive-tier mappings, an accountability-requirements checklist, and a governance counterfactual memo. Together with Chapter 11's calibration metrics, these are the substance of Chapter 13's go/no-go recommendation.

**How to adapt this prompt:**
- *For your own project:* Be willing to assign responsibility to specific named parties (the actual model provider, the actual framework). The chapter is explicit that the analysis falls apart when responsibility is described in vague third-person.
- *For ChatGPT / Gemini:* Works as-is. Both render Mermaid.
- *For Claude Code:* Not the right fit.
- *For Cowork:* Save the four outputs to the casebook folder.

**Connection to previous chapters:** Chapter 4 opened the Rung 3 question; this chapter closes it for your agent. Chapter 8's case taxonomy is the input. Chapter 9's delegation map identifies which accountability requirements are unmet by the current deployment.

**Preview of next chapter:** Chapter 13 is the close. You'll apply the three categorical limits to your agent, produce the final go/no-go memo with a defended position the casebook supports, and stake the supervisor's recommendation: deploy, deploy with constraints, or refuse.
