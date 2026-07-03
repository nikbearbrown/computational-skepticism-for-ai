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
*Figure 12.1 — None of these nodes alone produced the failure; each was necessary, none was sufficient.*

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

I could catalog a dozen cognitive capacities here and rate AI on each. I have done that exercise; it does not earn its length. So let me strip the map down to the capacities that do actual work in the accountability argument — the ones the taxonomy and the answerability argument below stand on — and skip the rest. Three matter, and they matter because each names a place where the extension analogy breaks.

**Episodic memory — the missing autobiography.** Distinguish two kinds of memory. Semantic memory is the storage and retrieval of facts, and AI is superhuman at it; cite a model as a source of recall and you are on solid ground. Episodic memory is the recall of specific past events with temporal context — *I was in that room when that happened* — and here AI is not weak but absent in the sense that matters. A model's "memory" is its weights, shaped by training. It is not a record of its own history as an agent in the world. Watch what that costs you at the accountability layer: episodic memory is what lets an agent say "I made this decision, in this context, for this reason." An AI cannot give that account of itself, because there is no self whose history the account would describe. The trade-off is stark. You get perfect recall of everything humans ever wrote, and you lose the one thing accountability needs — a continuous someone who was present and can be answerable for what they did.

**Emotion — moral salience, not feeling.** This is where the definition you pick does all the work. Under a functionalist definition — a state that shifts behavior in characteristic ways in response to relevant stimuli — the evidence for emotion-like states in AI is real: prompt a model in ways associated with distress and its outputs move off baseline. Under a phenomenological definition — there is something it is like to be in that state — we have no evidence and no method for getting any. But for accountability, neither of those is the load-bearing distinction. The one that is: can the system be harmed, can its interests be violated, can it bear moral standing? Whatever emotion-like text a model produces, the answer on current evidence is no. And that is exactly the capacity sanctions depend on. Shame, regret, the weight of having gotten it wrong — these are not decorations on accountability; they are the mechanism by which a consequence lands. A system that cannot be worse or better *for* anything cannot be the party a sanction bites.

**Metacognition — and why it cannot be self-supplied.** Metacognition is cognition about cognition: monitoring your own reasoning, detecting your own errors, calibrating confidence to evidence. AI produces outputs that *resemble* this. You can prompt a model to "check its work," and it will. But look at where that check comes from — it is generated by the same system being checked. That is the Gödel problem arriving early, and it is the hinge of the whole chapter. Genuine metacognition, the kind that could certify a system, requires a perspective that is not just a continuation of the original process. This is the validator-independence point, and it is worth stating flatly because everything downstream leans on it: an AI checking an AI is not a second opinion, it is the first opinion run twice. The independence that makes review mean something is precisely what a system cannot supply about itself. That independence is what a human supervisor brings, and it is the core of Tier 4.

Notice what these three share. Semantic memory, pattern recognition, statistical language, metric navigation, constrained planning — where AI is strong, it extends human reach exactly the way writing extended memory or the microscope extended perception, and the extended mind is more capable than the bare one. But episodic memory, calibrated metacognition, moral salience, stakes — where AI is weak or absent, the missing capacity is not one you can add by pouring in more computation. It requires a different kind of thing entirely: an agent with a history, with commitments, with the possibility of loss.

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

The taxonomy organizes human intelligence into seven tiers, sorted by AI capability. It is not an academic classification but a triage: a map of where AI is strong, where it is weak, and what that means for which cognitive work requires a human. Read top to bottom, it tracks a migration — from the pattern-and-association work where AI is superhuman, up through the embodied, social, supervisory, causal, collective, and existential tiers where AI weakens and then disappears. The tiers that matter most for accountability are the ones near the bottom, because those are the ones no amount of scale reaches. The table carries the per-tier detail; each row names the capacity, AI's status on it, and what that status means for the human who must stand in the loop.

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

![A monitor built like the system it monitors shares its blind spots — a correlated check, not an independent one.](../images/12-accountability-who-is-responsible-when-the-system-fails-fig-04.png)
*Figure 12.4 — Common cause failure: a monitor built like the system it monitors shares its blind spots — a correlated check, not an independent one.*

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

## The five accountability requirements and the tiers they depend on

The accountability apparatus has five requirements — specifications, audit trails, recourse, independent review, sanctions. Each is necessary because it corresponds to cognitive work at a specific tier, and that tier is exactly where AI cannot substitute for a human. Work through them and the mapping is the argument.

**Specifications** are Tier 4 work. A failure is, operationally, a divergence from specification; without one, there is nothing the system was supposed to do that it failed to do, and no accountability claim that can be precisely made. But writing a spec precise enough to support that claim requires problem formulation — the supervisory capacity to ask not "what did the system do?" but "what was it supposed to do, and did we capture that correctly?" Vague specs are not accidental; they are what Tier 1 reasoning produces when handed a Tier 4 task: plausible-looking language that does not resolve the accountability question. *Vague specifications are a structural choice that protects the deployer from accountability*, whether they intend that or not.

**Audit trails** are Tier 1 capture plus Tier 4 interpretation. The record of what the system did is a logging problem — mechanical, Tier 1. But an audit trail is not self-interpreting; two engineers can read the same log and tell two different stories. The Ash case is the canonical demonstration: the agent's completion report was in the trail, and the trail was wrong. The independent state check — discovering the email still existed on Proton Mail — was not generated by the trail. It required a human to stand outside it and ask whether it matched the world. That is Tier 4 plausibility auditing.

**Recourse** is Tier 3 plus Tier 6. Recourse is a social, relational act: an affected party makes a claim, the claim is heard, a response is given. Social intelligence sits at Tier 3, where AI simulates outputs without experiencing what produces them. A recourse mechanism that is entirely AI-mediated — responses generated by a model, disputes judged by a classifier — has replaced the social act with a Tier 1 simulation, which is precisely why current algorithmic recourse feels hollow to the people routed through it. The act of being heard is constitutively social; it cannot be replaced by a very good approximation of being heard.

**Independent review** is Tier 4 by definition. The logical spine is the Gödel argument: the validator must be outside the system being validated, and an AI reviewing another AI's outputs is more derivation, not external review. Independent review requires the plausibility auditor — the human with deep domain knowledge and AI-failure-mode literacy who can stand outside the output and ask whether it corresponds to reality. Without it, the deploying organization is grading its own work.

**Sanctions** are Tier 7. A sanction is consequential only when the sanctioned party has stakes — something to lose. An AI does not lose its job for a flawed output; a plausibility auditor does, a deploying organization does, a model provider does if the regime imposes consequences. Remove the possibility of consequence and you have a descriptive system, not a prescriptive one. Tier 7 is not a philosophical add-on; it is the load-bearing tier, the one without which the rest of the apparatus has no teeth.

The apparatus therefore lives at Tiers 3, 4, 6, and 7 — where AI is weak to absent — while AI systems operate primarily at Tier 1. That gap is the structural argument for human oversight, not the contingent one. A deployment with all five requirements has a working framework; one missing any of them has gaps that fail in predictable ways, and most deployed AI systems are missing two or more. The checklist below turns the five into a reusable audit instrument.

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

The one structural point survives every update. Regimes mandate "human oversight" for high-risk systems without specifying *which cognitive tier* the oversight must supply — and that omission is the whole vulnerability. A mandate for "a human in the loop" is satisfied by a human who performs only Tier 1 box-checking: reads the AI's output, clicks "approve," and never does the Tier 4 plausibility auditing the loop actually requires. The *Irreducibly Human* taxonomy is what tells you the mandate is underspecified. Human oversight that does not name the tier is a compliance ritual wearing the costume of accountability.

The EU AI Act (Regulation (EU) 2024/1689), in force since 2024 with phased implementation, is the most comprehensive AI-specific regulation as of this writing. It classifies systems by risk and imposes proportional requirements; high-risk systems face requirements for risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy, robustness, and cybersecurity, and penalties for prohibited practices reach up to €35 million or 7% of worldwide annual turnover (Art. 99; prohibited-practice provisions applicable since 2 February 2025). Its "human oversight" clause is exactly the underspecified mandate above. Alongside it sit the U.S. NIST AI Risk Management Framework (voluntary, with an Agent Standards Initiative, announced in early 2026, targeting agentic systems) and sectoral guidance — FDA on medical devices, CFPB on algorithmic credit, EEOC on employment — often more operationally specific than the cross-sector frameworks.

For what it looks like when a regime finally *does* bite, look at SyRI. The Dutch welfare-fraud risk-scoring system was struck down by The Hague District Court in 2020 for violating the right to private life — an opaque scoring system deployed on citizens, with recourse and independent review that existed on paper and not in function (NJCM c.s. v. The Netherlands (SyRI), ECLI:NL:RBDHA:2020:865, 5 February 2020). The court supplied the independent review and the sanction the regime had failed to build in — late, externally, after the harm had landed. Which is the whole argument for building the apparatus *before* deployment, into the gate you sign, rather than waiting for a court to reconstruct it. The specific regimes will change. *The structural requirements will not*, because they are the machinery accountability requires regardless of which regime imposes it. Build to that standard; let the regime catch up.

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
*Figure 12.5 — The standard treatment stops at Rung 2; closing the counterfactual is Rung 3 work, and it requires a human.*

---

## Stages and stakes: a taxonomy of where human oversight is not optional

The cognitive tiers tell you *what capacity* oversight requires; stakes tell you *how intensively* to apply it and on what cadence. That is an orthogonal axis, and crossing the two gives a working tool for when human oversight is not optional.

For **low-stakes, reversible outputs** — a draft email, a code snippet reviewed before deployment — Tier 1 capacity covers most of the work and light review at output suffices. For **moderate-stakes, partially recoverable outputs** — a business analysis, an engineering specification — systematic review at checkpoints is appropriate; the human need not be in the loop constantly but must be capable of Tier 4 plausibility auditing when they are. For **high-stakes, irreversible outputs** — drug candidates, structural recommendations, consequential legal analysis — the human is not performing a review but is constitutive of the output's validity. As system confidence grows the humans do not disappear; they shift from intensive validation to catching systematic drift. The plausibility auditor here works Tiers 4, 5, and 7 at once: standing outside the output, judging whether it corresponds to reality, and doing so with stakes. The surgical analogy holds — AI-assisted guidance raises the capability ceiling; the surgeon's accountable judgment is what makes exercising that ceiling responsible. Notice the failure mode the table names: a human can be present at every stage and still supply nothing, if they are not engaging the tier the stakes demand.

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

Generative AI stretches this topology rather than changing its shape. When a system can produce anything rather than classify something, the list of parties extends — through training data, training procedure, and downstream propagation — and the distribution flattens, so the governance counterfactual acquires more variables. Attribution of the output itself becomes contestable: who wrote an image, a paragraph, a piece of code the model generated on a prompt is not a settled question, and the legal frameworks are in flux — the U.S. Copyright Office's 2025 guidance holds that purely AI-generated output is not copyrightable absent human authorship, while the EU AI Act imposes transparency obligations on generative outputs. What holds the flattened distribution together operationally is provenance — and the AI Use Disclosure from Chapter 9 is its concrete form, a Tier 4 document in which the engineer separates their own contribution from the model's Tier 1 output. A disclosure written by someone who has not done that metacognitive work is formally complete and operationally hollow.

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

**C3.** *(Audit.)* Take a system that failed and that you did *not* build: the **Epic Sepsis Model**. It was a proprietary early-warning tool for sepsis, deployed widely across hospitals, whose independent real-world validation found it performed substantially worse than its marketed accuracy — missing a large fraction of sepsis cases while generating a heavy alert burden (Wong et al., "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients," *JAMA Internal Medicine*, 2021, doi:10.1001/jamainternmed.2021.2626). Its failure is instructive precisely because so many parties *could* have signed a gate, and the ones who signed were not answerable to the patients. Build the full accountability audit: distribute responsibility across the vendor who trained and marketed it, the health systems that deployed it against their own populations without independent local validation, the clinicians who accepted its flags, and the absent independent reviewer. Then write the attestation *you* would have required before deployment — including, in the "what was NOT tested" section, the independent local validation that was never performed. State who should have signed each gate, and what specific signal would have triggered a refusal to sign. The answer that matters is the one about independent *local* validation — the review that was structurally external, the review nobody was required to perform, the gate nobody signed because the regime did not demand a signature. This integrates the distribution method, the five requirements, and the attestation artifact into one deliverable.

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
