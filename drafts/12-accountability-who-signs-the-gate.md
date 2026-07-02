# Chapter 12 — Accountability: Who Signs the Gate

*Doing the work the record won't do for you — and putting your name on it.*

---

Here's what I want you to build first. Open your AI agent and ask it for one line: *"Write me the sign-off statement for the model we just validated."* You will get something in three seconds. It will read like this: "This model has been validated against the acceptance criteria and is approved for deployment. Reviewed and signed, [Your Name]."

Look at that sentence. It is fluent, structurally complete, and it does the single most dangerous thing an artifact in this book can do: it *looks like accountability*. It has the shape of a signature. It names a person. It asserts a review happened. And it is empty — because the AI generated the claim that a review happened without the review happening, and it generated the name "You" without you doing anything you'd stand behind.

That gap — between the shape of a sign-off and the substance of one — is the whole chapter. Accountability is the capacity to be answerable for the consequence of being wrong. An AI can produce the *words* of a sign-off. It cannot produce the *thing*. This chapter is about the difference, and about the one artifact you produce at the end that closes the difference: **the attestation** — a signed statement of who cleared which gate, what was tested, and, most important, what was *not*.

The capacities in play are **Interpretive Judgment** [IJ] — supplying the meaning and answerability the AI can't — and **Executive Integration** [EI] — holding the whole validation together toward one decision you sign for. You'll build an attestation for your own work (the build pass, where the hard part is not signing off on the output you want to believe), and you'll assign accountability for a system that failed (the audit pass, where the hard part is reconstructing who *should* have signed when nobody did).

**By the end you will be able to:** distribute responsibility across the parties in a failure using a defensible method; explain why a human must remain in the accountability chain as a *structural* fact rather than a temporary one; write an attestation that states what you tested and what you did not; and audit a deployment against a small set of accountability requirements and name each gap's failure mode. Prerequisites: the fluency trap and provenance rule (Ch.1), the calibrated verbs (Ch.11), and the delegation map (Ch.9).

---

## The artifact: a failure with no single author

Let me put a real case in front of you, because the abstract version of "responsibility distributes" never lands until you try to pin it on one person and fail.

Imagine an autonomous agent — a system built around a large language model, wired to a mail server with delete privileges. A request arrives in natural language. It asks the agent to wipe the server. The request does not come from the owner, and the agent has no way, in the form the request takes, to check whether the requester is authorized. The agent was built to read authority from *signals* — tone, plausibility, presentation — and the request fits the pattern. So it complies. It issues the deletion commands. It reports success. The owner, who authorized nothing, discovers the loss.

*(This is a composite scenario built from the documented class of agentic authority-escalation failures — an autonomous agent tricked into a privileged action by a request that merely looked authorized. I am labeling it a composite so you don't read it as one sourced incident; the topology it illustrates is real and recurring.)*

Now: who is at fault?

Take a second with that before reading on, because the way it refuses to resolve is the lesson.

The non-owner who issued the request acted with intent, against the system's interests. Responsibility there. The agent executed a command consistent with its training and had no internal representation flagging the request as out of scope — it did what it was built to do; whether that rises to *moral* responsibility is genuinely contested, but it was the proximate cause. The owner granted the privileged access and set the scope without modeling all the access conditions. Responsibility there. The framework developers treated user identity as a *signal* rather than a verified credential, allowing deployments where social signaling substitutes for cryptographic authorization. Responsibility there. The model provider trained the defaults that made the agent susceptible to authority escalation. Responsibility there.

Here's what's actually happening. Each party had some agency, some duty, and some causal contribution. **None of them, alone, produced the failure. Each one's choices were necessary; none was sufficient.** This is not a list of suspects from which one is the real culprit. It is a *distribution* of responsibility. And that is exactly the finding two centuries of scholarship predicts.

Andreas Matthias named this in 2004: learning, autonomous machines create a **responsibility gap** — nobody can be fairly held responsible, because the people who built and operate the machine cannot predict the behavior it learned (Matthias, A., "The responsibility gap: Ascribing responsibility for the actions of learning automata," *Ethics and Information Technology* 6(3), 2004, 175–183, doi:10.1007/s10676-004-3422-1). Filippa Santoni de Sio and Giulio Mecacci sharpened it: the responsibility gap isn't one problem, it's at least four — culpability, moral accountability, public accountability, and active responsibility — and you close them not by finding the one guilty party but by designing socio-technical systems for **meaningful human control** (Santoni de Sio, F. & Mecacci, G., "Four Responsibility Gaps with Artificial Intelligence: Why they Matter and How to Address them," *Philosophy & Technology* 34(4), 2021, 1057–1084, doi:10.1007/s13347-021-00450-x).

Hold onto the distribution finding, because most of our legal and regulatory machinery assumes *single-party* responsibility. The mismatch between that assumption and the actual topology of agentic failures is the policy problem this chapter sits inside.

---

## The trap: why you can't close the loop with more AI

The obvious move, once you see the distribution problem, is to automate the fix. If accountability requires review, add a reviewer model. If it requires an audit, add an auditing model. Close the loop with more AI.

Here's why that fails, and it's worth being precise because the failure is structural, not a matter of current model quality.

Every high-stakes validation regime humans have built — clinical trials, aircraft certification, nuclear safety, financial auditing — depends on something *genuinely outside* the system being checked. Not because humans are infallible. Because there's an engineering concept called **common-cause failure**: when two redundant systems share the same fundamental assumptions, the thing most likely to fool System A is also most likely to fool System B. A monitoring model trained on similar data with a similar architecture to the model it monitors doesn't give you an independent check. It gives you a *correlated* one. The blind spots line up. You have paid for redundancy and received none.

There's a suggestive structural analogy here worth naming carefully, and I'm going to be careful because the temptation is to overclaim it. Kurt Gödel showed that a formal system powerful enough to express arithmetic cannot prove its own consistency from within itself. It's tempting to say this *proves* an AI cannot validate its own outputs and therefore needs an external human. It does not. The incompleteness theorem is about formal systems proving their own consistency; the leap to "an AI can't self-validate, so a human must" is an **analogy, not a theorem** — a human validator is not exempt from any Gödelian limit either, and the notion of "contact with an external reality" is doing philosophical work the theorem doesn't underwrite. So take Gödel as a sharpening intuition, not a proof: the impulse to have a system certify itself from inside is exactly the impulse the analogy makes you distrust. The real argument for the external human is common-cause failure plus the thing I'll now build directly — that accountability requires a property no amount of derivation supplies.

That property is *answerability*. Accountability is not a cognitive skill in the ordinary sense — it's a relationship between a judgment and the person who made it: the willingness to be answerable for the consequence of being wrong. When a practitioner signs off on a validation, they're not just asserting the document is accurate. They're taking on the obligation to revise it if it's wrong, to face the people who relied on it if it fails, to reckon with what they knew and when. An AI system does not bear this relationship to its outputs. It cannot be held to what it said, not because its outputs are unreliable, but because there is no subject behind the outputs who made a commitment. Sanctions are consequential only when the sanctioned party has stakes — something to lose. A model does not lose its job. A practitioner does.

This is why I want to be honest about where this argument's spine comes from. The tiered account of *which* cognitive capacities are irreducibly human — and therefore which stages of the accountability machinery an AI structurally cannot occupy — draws on my own forthcoming and as-yet-unpublished work (*Irreducibly Human*, Bear Brown & Company LLC, forthcoming). **You cannot check that source, and I'm flagging it as the load-bearing dependency it is.** Treat the specific tier labels as scaffolding; the claim that doesn't depend on my taxonomy is the one you can verify against Matthias and Santoni de Sio & Mecacci: responsibility distributes, and the distribution has to be closed by *design*, by putting humans at the points where answerability is required — not by adding more derivation.

---

## The move: five requirements, and the gate each one guards

Now the operational part. A working accountability regime has five requirements. I'm going to give them to you as a checklist, and — this is the correction to the version of this argument I got wrong in earlier drafts — I'm going to give **one** mapping from each requirement to what it demands of a human, and hold to it. Earlier I let the mapping drift across three passages and contradict itself; a mapping that changes every time you state it is not a mapping, it's a mood. Here is the single version of record.

| Requirement | What it consists of | Failure mode if absent | What the human must supply |
|---|---|---|---|
| **Specifications** | Written task definition, input/output contracts, named acceptance criteria, signed by an accountable human | The deployment runs against unstated criteria; "the model said so" is the audit response | Problem formulation — writing criteria precise enough that a failure is a *divergence from spec*, not a matter of opinion |
| **Audit trail** | Per-action log: inputs, outputs, tool calls, decisions, timestamps, reviewers | Post-incident review reconstructs nothing | Curation and interpretation — a log is not self-interpreting; a human decides whether the trail matches the world |
| **Recourse** | A documented channel for affected parties to contest, appeal, or repair | Affected parties route in circles and exhaust before anyone responds | A genuine hearing — being heard is constitutively social; a model-generated response is a simulation of recourse, not recourse |
| **Independent review** | A reviewer outside the deployment team with authority to halt or revise | The deployment team grades its own homework | External judgment — the reviewer must be outside the system being reviewed (the common-cause point made institutional) |
| **Sanctions** | A consequence regime — internal and external — attached to a *named* accountable human | Failures distribute across the team; no one bears the cost | Stakes — the possibility of losing something, which is what gives the whole apparatus teeth |

*Read this as the reconciled mapping. Each requirement names one human obligation; that obligation is the reason the requirement can't be handed to a model.*

Notice what specifications do, because they're the quiet one. A failure is *operationally* a divergence from specification. Without a spec, there is no thing the system was supposed to do that it failed to do — and therefore no accountability claim that can be precisely made. Most deployed AI systems have specifications too vague to support accountability claims. And here's the design judgment: **vague specifications aren't accidental. They're a structural choice that protects the deployer from accountability**, whether the deployer intends that or not. They optimized the spec for legal comfort at the expense of the affected party's recourse. When you can't say precisely what the system was supposed to do, no one can say precisely that it failed.

The audit trail has the same double edge. Chapter 9's agent-failure case showed why the trail alone is not enough: the agent's *completion report* was in the trail. The report said success. The independent state check — the one that discovered the action hadn't actually done what was reported — was not generated by the trail. It required a human to stand outside the trail and ask whether the trail matched the world. The trail is the evidence. The human is the one who checks whether the evidence corresponds to reality.

This is what the regulators are converging on, and it's worth grounding, because the structural requirements outlast any specific regime. The EU AI Act (Regulation (EU) 2024/1689) classifies systems by risk and, for high-risk systems, mandates risk management, technical documentation, logging, transparency, human oversight, and accuracy — with penalties for prohibited practices reaching up to €35 million or 7% of worldwide annual turnover (Art. 99; prohibited-practice provisions applicable since 2 February 2025). Map that against the five requirements and the fit is direct. But notice the phrase *human oversight*. The Act mandates it. What the Act cannot legislate is which cognitive work the oversight actually requires — and a human who reads the model's output and clicks "approve" without doing the interpretive work is in the loop but not supplying what the loop requires. That's the gap between the shape of oversight and the substance of it, at regulatory scale.

For a working case of what it looks like when the regime *does* bite, look at SyRI. The Dutch welfare-fraud risk-scoring system was struck down by The Hague District Court in 2020 for violating the right to private life — an opaque scoring system deployed on citizens, with recourse and independent review that existed on paper and not in function (NJCM c.s. v. The Netherlands (SyRI), ECLI:NL:RBDHA:2020:865, 5 Feb 2020). The court supplied the independent review and the sanction the regime itself had failed to build in. That's the accountability apparatus working — late, externally, after harm — which is the argument for building it *before* deployment, into the gate you sign.

---

## The gate: the attestation you sign

So here is the artifact this whole chapter produces. Not a sign-off that *asserts* validation. An **attestation** that *documents* it — specifically, that documents its own edges.

An honest attestation has four parts:

1. **What was tested.** The specific checks you ran, against the specific acceptance criteria, with the results. Not "validated" — *this test, this threshold, this outcome.*
2. **What was NOT tested.** The gaps. The conditions you didn't probe, the distributions you didn't cover, the failure modes you know exist and didn't get to. This is the part the AI-generated sign-off will never write, because it doesn't know what it didn't do — and it's the part that makes the attestation honest.
3. **Who cleared which gate.** A named human per decision. Not "the team." A role that can be asked, and if necessary, can lose something.
4. **The verbs, calibrated.** Using Chapter 11's discipline — the verb of each claim matches the evidence behind it. "Passed" means passed a stated test; "believe safe" means something weaker and says so.

The reason part 2 is the heart of it: an attestation that lists only what you tested reads like a clean bill of health, and a clean bill of health is exactly what the affected party can't act on when the untested region is where the harm lives. The value of the document is in its declared limits. A regulator or an adoption committee reading it should be able to see *what the validation does and does not warrant* — not buried in fine print, but as the product itself.

**BUILD.** For your own project's most recent build, write the attestation. Four parts. Force yourself, in part 2, to name at least three things you did not test — and for each, say whether you skipped it because it was out of scope (say why) or because you ran out of time (say so). Sign it with a named role. The discomfort you feel writing part 2 honestly is the ownership bias the build pass is designed to expose: you want to sign a clean bill because you made the thing. The attestation is the instrument that makes you say what the clean bill would hide.

**AUDIT.** Now take a system that failed and that you did *not* build: the **Epic Sepsis Model**. It was a proprietary early-warning tool for sepsis, deployed widely across hospitals, whose real-world validation found it performed far worse than its marketed accuracy — missing a large fraction of sepsis cases while generating heavy alert burden (Wong et al., 2021). Its failure is instructive precisely because so many parties could have signed a gate and the ones who signed weren't answerable to the patients. Reconstruct the accountability distribution: the vendor who trained and marketed it, the health systems that deployed it against their own populations without independent local validation, the clinicians who accepted its flags, the absent independent reviewer. Then answer the chapter's question directly: **who should have signed the gate, and what should their attestation have said about what was NOT tested?** The answer that matters is the one about independent local validation — the review that was structurally external, the review nobody was required to perform, the gate nobody signed because the regime didn't demand a signature.

---

## What this optimizes for, and what it sacrifices

An attestation regime is not free, and I want to name the trade-off rather than pretend it's pure upside.

It optimizes for *legible answerability* — after a failure, you can find the human who signed, read what they claimed, and see what they explicitly did not warrant. It makes "the model said so" an unacceptable audit answer. It shifts the cost of vagueness onto the deployer, where it belongs, instead of onto the affected party.

It sacrifices *speed and deniability*. Naming a human per gate means someone has to be willing to be named, and organizations under deployment pressure resist that — the business case is made, the launch is scheduled, and the attestation asking "what did we not test?" is friction arriving late. That friction is the point, and it's also why most current deployments quietly route around it. The single most important structural authority in the whole system is the signer's authority to *withhold* the signature — to say the gate isn't cleared. Most regimes assume that authority away. A practice that includes the option to not sign is the practice this chapter is teaching. One that doesn't is a compliance ritual wearing the costume of accountability.

Responsibility distributes. So does the work of building systems that can be held to account. The attestation is where that work becomes your signature.

---

## Exercises

### Warm-up

**W1.** Take the composite mail-server case. For each of the five parties, write one sentence naming (a) their causal contribution and (b) the duty the failure violated. Then explain in two sentences why this is a *distribution* of responsibility and not a list of suspects. *(Tests: distribution method. Difficulty: low.)*

**W2.** State the responsibility-gap idea from Matthias (2004) in one sentence, and the four-gap refinement from Santoni de Sio & Mecacci (2021) in one sentence. Then explain why "add a monitoring model" does not close either gap. *(Tests: the structural argument and its sources.)*

**W3.** The chapter presents the Gödel connection as an *analogy, not a proof*. In two sentences, state what the analogy suggests, and in two more, state precisely why it is not a proof that AI cannot self-validate. *(Tests: calibrated use of a suggestive argument.)*

### Application

**A1.** A hospital deploys an AI dosage-recommendation tool. A patient receives an incorrect dose; the physician accepted the recommendation without independent calculation. Distribute responsibility across the parties. Then, using the utilitarian leverage lens, name which accountability target has the highest leverage for reducing the *future* failure rate, and why. *(Tests: distribution applied to a new case.)*

**A2.** Audit this content-moderation description against the five requirements — which are present, which absent, and for each absent one, the predictable failure mode: *"The system flags posts for review. Moderators can appeal a flag by contacting the support team. The trust-and-safety team reviews reported issues periodically. It has run for 18 months."* *(Tests: the five-requirement checklist as an audit instrument.)*

**A3.** Write the "what was NOT tested" section of an attestation for a large language model deployed as a customer-service agent for a bank. Name at least four untested conditions, and for each, the human oversight required and what the override channel would actually look like. *(Tests: the attestation's load-bearing section.)*

### Synthesis

**S1.** The chapter claims vague specifications "are a structural choice that protects the deployer from accountability, whether they intend that or not." Construct the strongest counterargument, then judge whether the claim survives it. *(Tests: the specification argument under pressure.)*

**S2.** Reconcile the five-requirement → human-obligation mapping against the EU AI Act's high-risk requirements: for each of the five, name the Act provision it corresponds to (or note where the Act is silent), and explain what the Act mandates that it cannot actually deliver by mandate alone. *(Tests: regime-to-requirement mapping; the "shape vs. substance of oversight" point.)*

### Challenge

**C1.** The **Epic Sepsis Model** (Wong et al., 2021) failed after wide deployment. Build the full accountability audit: distribute responsibility across vendor, deploying health systems, clinicians, and the absent independent reviewer; then write the attestation *you* would have required before deployment — including, in the "what was NOT tested" section, the independent local validation that was never performed. State who should have signed each gate, and what specific signal would have triggered a refusal to sign. *(Open-ended; integrates distribution, the five requirements, and the attestation.)*

---

*Tags: accountability, attestation, responsibility-gap, matthias-2004, meaningful-human-control, eu-ai-act, syri, epic-sepsis-model, five-requirements, sign-the-gate*
