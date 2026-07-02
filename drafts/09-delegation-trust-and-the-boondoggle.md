# Chapter 9 — Delegation, Trust, and the Boondoggle

Here's a controlled experiment that ran itself, unintentionally, inside two engineering teams. Same data. Same model. Same fairness metrics. Same monitoring infrastructure. Both teams build a validation pipeline for an AI system that scores loan applications. If you diffed their code you'd struggle to tell them apart. Then both go to an adoption committee to get their rollout expanded, and the committee asks each team one question: *who is responsible if a loan decision is challenged?*

Team 1 wrote their delegation like this: "AI scores the application, the loan officer reviews and decides, the system logs both." Clean. Reads well. And when the committee pushes on the word *reviews*, the team can't answer. What does "reviews" mean? What did the loan officer actually check? They go back to reconstruct what their own pipeline was supposed to do, and the committee tables the rollout — not because the pipeline is bad, but because nobody can say what it does.

Team 2 wrote it like this: "The AI computes the score and produces a brief explanation. The loan officer is required to verify that the explanation is consistent with the application data, to check whether any of three named edge-case patterns are present using a checklist embedded in the interface, and to record their decision with one of four documented justification codes. If the AI score is below 0.3 or above 0.7, the loan officer's decision can match the AI without further review. If the score is between 0.3 and 0.7, a second loan officer must independently review before either can record a decision." The committee reads this and knows exactly what happened at each step. They might *still* reject it — but for substantive reasons, not because the documentation is fog.

The only variable was the delegation map. That's the whole chapter. Here's what I want you to be able to build by the end of it: a delegation map with **testable handoff conditions**, a **Boondoggle Score** that sorts your sub-tasks into AI, human, and hybrid buckets, and a signed phase gate that says which capacity you exercised where. This chapter is the operational center of the book. It's where the five supervisory capacities stop being a vocabulary and become jobs with artifacts.

One honest note before we start. The two-teams story proves that a good delegation map survives *review*. It does not prove that Team 2's pipeline makes *better decisions*. Those are different claims, and I'm going to keep them apart. Documentation quality is what we're teaching here — because in AI systems, undocumented delegation is the most common way a working pipeline turns out to be unsupervised.

## The classical move: the contract, not the partition

The mistake almost everyone makes is to treat delegation as a partition of labor — "the AI does this part, I do that part," like slicing a pie. That framing hides the thing that actually matters. A delegation is a **contract**. A contract has boundaries, obligations, and a clause for what happens when one party fails to deliver. The partition framing has none of that. It just names who touches what.

The load-bearing element of the contract is the **handoff condition**: the signal that a step completed correctly, so the next step can proceed. And a handoff condition has exactly one non-negotiable property. It has to be **testable**. Testable means a non-author — someone who didn't build the thing — can read the condition, look at the system, and determine whether it was met.

Watch what fails the test. "The AI produces a reasonable result and the human reviews it." Both *reasonable* and *reviews* are unspecified. Hand this to five loan officers and you get five different behaviors, all of which get called "reviewing." There is no fact of the matter about whether the condition was met, which means there is no fact of the matter about whether the step worked.

Now watch what passes. "The AI produces a score in the interval zero to one with a confidence interval. The human accepts the score, requests re-scoring, or overrides. In the override case, the human records one of four documented justification codes." A stranger can look at the log and tell you, for any case, exactly what happened. That's the standard.

The procedure to convert one into the other is not glamorous, and I want to say that plainly because the un-glamour is the point. Write the condition. Circle every interpretive word. Replace each one with a specifiable criterion, or write a guideline that pins down the interpretation. Then hand it to someone who didn't build it and ask them to determine, for a sample case, whether the condition was met. If they can't, you're not done. This is documentation work. Nobody gets promoted for it. It is also the entire difference between a supervised pipeline and one that merely looks supervised.

| Domain | Untestable | Testable | What got pinned down |
|---|---|---|---|
| Loan scoring | "The model is fair across borrowers." | "False positive rate equalized to within 2 percentage points across the four protected-class groups, on the audit sample drawn from Q3 2025." | *Fair* = equal FPR; *across borrowers* = four named groups; *within* = a stated tolerance |
| Medical triage | "The model handles edge cases responsibly." | "On the held-out 200-case rare-condition set, sensitivity ≥ 0.95, and any false negative is escalated to clinician review within 30 minutes." | *Edge cases* = a named set; *responsibly* = a metric plus an escalation contract |
| Content moderation | "The model respects context." | "On the 500-case context-flip set (same text, different source community), the moderation decision changes ≤ 2% of the time." | *Context* = source community; *respects* = decision invariance under change, with a tolerance |

I'll be honest about a wrinkle here, because the book's whole method is to not let a clean claim smuggle in a mess. Some handoff conditions are only testable by a *qualified* reviewer. "Verify the citation is accurate in the domain-specific sense" is testable — but only by someone who knows the domain, not by any random non-author. That's a narrower guarantee than "anyone can check it," and I'd rather name the gradient than pretend the testable/untestable line is a clean binary. It isn't. It's graded. The standard still holds; it just has tiers.

## The five capacities as jobs, not personality traits

Chapter 1 gave you five supervisory capacities. Here's what's actually happening when they work: each one is not a trait you *have* — good judgment, domain experience — but an operational form the pipeline either contains or doesn't. If the artifact isn't there, the capacity didn't happen.

- **Plausibility Auditing [PA]** — given what I know of the world this output describes, could this be true? Operational form: a checklist embedded in the workflow, verification questions matched to the output type, answered yes/no and recorded. No checklist, no auditing.
- **Problem Formulation [PF]** — before the AI is invoked, specify the question, the evaluation criteria, and the conditions under which AI is even the right tool. Operational form: a written spec of a paragraph or two. No spec, no formulation.
- **Tool Orchestration [TO]** — for each step, decide which tool is responsible, why it's the right one, and what the handoff between tools is. Here's the key move: **[TO] operationalized *is the delegation map itself*.** The map is not a document *about* Tool Orchestration; it is Tool Orchestration made concrete.
- **Interpretive Judgment [IJ]** — read the output in deployment context and interpret what it means for the decision. Operational form: a documented interpretation in the audit trail — "the decision was X because the score was Y in this context, where this context means Z."
- **Executive Integration [EI]** — synthesize outputs from multiple tools, humans, and monitoring signals into a decision the system can stand behind. Operational form: a decision document with named contributors and a clear authority structure.

This chapter's capacity is [TO] — but [TO] pulls the other four in with it, because you can't orchestrate tools without formulating the problem, auditing the outputs, interpreting them, and integrating the result. The delegation map is where all five leave fingerprints.

| Capacity | Operational form | Artifact | Failure mode if absent |
|---|---|---|---|
| Plausibility Auditing | Independent check of output vs. domain ground truth at each step | Plausibility audit log per output batch | Confidently wrong outputs ship; failures surface downstream |
| Problem Formulation | Pre-deployment scoping doc naming question, data scope, anticipated failure modes | Scoping doc + deviation log | The pipeline solves the wrong problem, fluently |
| Tool Orchestration | Per-step tool inventory: tools allowed/forbidden, budgets, rate limits | Tool inventory + per-action log | Resource exhaustion; tool misuse; uncontrolled side effects |
| Interpretive Judgment | Domain reviewer note on every high-stakes output, with disposition | Review log with named reviewers | "The model said so" becomes the audit response |
| Executive Integration | Decision protocol for when capacities conflict — who decides, on what evidence, with what sign-off | Signed decision log | Failure distributes across the team with no accountable human |

## The Boondoggle: five questions that sort the work

So which sub-tasks should the AI do? The instrument I use is a structured assessment I call the **Boondoggle Score** — five questions asked of each sub-task. I want to be precise about what this is and isn't. It's my own instrument. I have no external validation that these five questions predict real delegation outcomes, so treat it as a heuristic, not a diagnostic. The score is less important than the questions. The questions are the thing that survives even if you never compute a number.

1. **Verification cost.** Can a human verify the output cheaply, or does verification cost as much as producing the thing from scratch? This is Chapter 1's solve-verify asymmetry, restored to its original direction: cheap-to-verify tasks — proofreading a summary against its source, sanity-checking a calculation, scanning a candidate list — are *good* AI tasks. Expensive-to-verify tasks are dangerous, because the cost structure itself pushes the supervisor toward accepting rather than checking. That's not a character flaw; it's economics acting on attention.
2. **Stakes.** What does being wrong cost? Low-stakes tasks tolerate higher error. High-stakes tasks demand human review or human-only handling, because the *average* performance is not the relevant statistic when one bad outcome is catastrophic.
3. **Distribution match.** Is the input in-distribution or out-of-distribution? An undertrained region is dangerous regardless of average performance, because the average was computed where the data lived, not where this input sits.
4. **Reversibility.** Can the action be undone? Irreversible actions — deletes, sends, financial transfers — should be gated behind explicit human approval, almost without exception.
5. **Audit trail clarity.** Does the action leave a reviewable trail? If the AI's effect entangles with downstream state so you can't tell what it did versus what propagated, it is not AI-friendly no matter how good the model is.

The five questions sort each sub-task into three buckets: appropriate for AI execution, human-only, or hybrid — AI-assisted with human verification at specified handoff conditions. The output is not a recommendation. It's a documented justification for the delegation choice.

| Question | Low risk | High risk | Where high risk pushes the work |
|---|---|---|---|
| Verification cost | Checkable in seconds; right answer obvious | Needs a domain expert + ≥30 min/item | Toward verify-before-trust, or do-not-delegate |
| Stakes | Wrong wastes team time, harms no one outside | Wrong reaches external parties, regulators, vulnerable users | Toward do-not-delegate without independent review |
| Distribution match | Inputs match training distribution; failures visible | Tail / OOD by construction | Toward verify-before-trust with explicit OOD checks |
| Reversibility | Outputs are discardable drafts | Outputs trigger irreversible action (write, wire, publish) | Toward a hard human-approval gate |
| Audit trail clarity | Every step logged (inputs, outputs, timestamps) | Chain opaque or scattered | Toward do-not-delegate until logging exists |

## The map's eight items — and why four of them are the whole game

Here's the full structure of a delegation map. For each step: (1) step name and purpose, (2) owner — AI, human, or hybrid, (3) inputs, (4) outputs, (5) handoff condition, (6) failure mode and escalation trigger, (7) verification — who verifies, how, (8) audit trail — what's recorded, where, in what format, for how long.

Items 1–4 are standard engineering documentation. Any competent team writes those. Items 5–8 are the supervisory additions, and here is the trade-off that defines the entire field right now: **most deployed AI systems have 1–4 and omit 5–8, and the omission is invisible while the system appears to work.** A pipeline missing any of items 1–4 is *broken* — it won't run. A pipeline missing any of items 5–8 is *unsupervised* — and it runs beautifully, right up until the uncaught error surfaces downstream, usually discovered by the person it harmed.

The completeness test: can an engineer who didn't build the map read it and determine, for any case, whether each step ran correctly? If not, an item is missing or untestable.

## What a real Boondoggle looks like

Let me walk through one. I built a **research-paper summarizer**: you paste in a PDF of an academic paper, and it returns a structured summary — problem, method, key findings, limitations — with every factual claim linked to a specific source passage. A researcher uses it to decide whether a paper is worth reading in full. I built it using a software-design consultant tool of mine, but I want the *method* to stand entirely without the tool, so I'll narrate the method and mention the tool only as one thing that implements it. If you have a whiteboard and discipline, you have everything you need.

**First, formulate the problem — human step, [PF].** The discipline here is to write a single sentence that names the thing being built, not the problem it solves. Not "a tool to help researchers save time" (that names a goal — you can't build a goal), but: "a structured-extraction pipeline inserted between PDF ingestion and researcher review that produces a claim-linked summary with passage citations for each factual assertion." Why is this irreducibly human? Because the AI can generate plausible sentences all day, but it can't decide whether *claim-linked* is the right design for this deployment — whether citations should be sentence-level or paragraph-level, whether "factual assertion" is the right boundary, whether the structure matches how researchers actually read. Those are domain judgments about harm and use. They're mine.

**Then decompose into steps and assign each one.** Here's the map, compressed:

- **Step 1 · human · [PF].** Define the section taxonomy (Introduction, Methods, Results, Limitations, and so on) plus rules for atypical headings and a policy for sections that don't map. *Handoff condition:* a written list of recognized types, mapping rules, and an unmappable-section policy, such that an engineer can predict how any heading gets classified.
- **Step 2 · AI.** A parser that segments the text into named sections using that taxonomy, flags UNMAPPED and SUSPECT sections, and is told: do not infer content, do not fill gaps. *Handoff condition:* the output contains at least one OK section; every original heading appears as recognized, UNMAPPED, or SUSPECT; nothing is silently dropped.
- **Step 3 · AI.** Structured extraction — one core claim per section plus a verbatim 1–3 sentence citation, with explicit NO_CLAIM and NO_CITATION values and a confidence label. *Handoff condition:* every HIGH-confidence citation is found verbatim in the source; nothing is paraphrased or synthesized.
- **Step 4 · human · [PA].** For every LOW-confidence or flagged entry, open the source and verify three things: is the claim accurate *in the domain-specific sense*, is the cited passage the most informative support available, and does the claim omit a qualification that changes its meaning? The example that makes this real: the AI extracted "the model outperformed baselines" when the paper said "on the training set only." Textually faithful, meaningfully false. Spot-check at least one in five HIGH entries too. *Handoff condition:* every flagged entry has a disposition — confirmed, corrected, or unverifiable — the HIGH sample is spot-checked, and the researcher signed off.
- **Step 5 · AI.** Format the verified material into a summary with block-quote citations and an explicit verification-status section. Told: do not add interpretive commentary, do not evaluate whether the paper's methods are sound. *Handoff condition:* every formatted claim traces to Step 3/4 output; no new claims appear.
- **Step 6 · human · [IJ].** Read the summary *as a user, not a QA reviewer.* Does the snapshot accurately characterize the contribution? Are the limitations represented, or does the summary make the paper look stronger than warranted? Sign it with your name and date. This can't be delegated because the AI cannot assess whether its own output would mislead a peer who trusted it.

Count it up: six steps, three AI, three human. And here is what the score reveals, which is the reason I make people build one. The human steps — 1, 4, 6 — are not the steps that *look* like heavy lifting. The AI steps (parse, extract, format) look like work. The human steps look like review. **That's the fluency trap operating at the level of a whole workflow:** the AI's outputs are fluent and specific, and the pull toward trusting them and moving on is strong exactly where you most need to stop. The two highest-risk handoffs are 3→4 (the researcher accepts a HIGH extraction without spot-checking, and a domain-important qualification vanishes) and 5→6 (the researcher treats the final read as proofreading and ships a misleading framing).

Notice something the score does *not* contain: the word "reasonable," the phrase "human reviews," the instruction "check for accuracy." Every human action names what is checked, against what criteria, at what granularity. Step 4 doesn't say "review the extractions." It says: open the source PDF, verify no qualification was dropped, spot-check one in five HIGH entries. **"Looks good" is not a handoff condition.** That's the sentence to tattoo somewhere.

One more thing the map exposes: there's no [EI] step. In a solo build that's fine. But the moment this runs in a team — one person runs the pipeline, another consumes the summary — a documented integration handoff is missing, and you'd add a Step 7 to close it. The map didn't just describe the work. It surfaced the gap.

## Trust calibration: the failure you can't see

Calibrated trust means your reliance matches the AI's *actual* reliability for that kind of input in that deployment context — not trusting the AI "in general," which is not a thing. There are three failure modes.

**Undertrust** is when you systematically discount a reliable AI. The deployment loses its value, and it shows up as "we tried it, it didn't help" — where the real failure was calibration, not accuracy.

**Overtrust** is when you accept an output you shouldn't. The fluency trap is the canonical case. This is the least visible failure mode, because it produces no immediate flag — only uncaught errors, discovered later, usually by the affected user.

Now, I want to be careful here, because this is the chapter that most preaches against mistaking a fluent assertion for evidence, and I'd be a hypocrite to smuggle one in. It is tempting to say overtrust is *the dominant* failure mode in current AI deployments. I'll say instead what the evidence actually supports. Overtrust — automation complacency, over-reliance on an automated aid — is a well-documented and consequential failure mode. That much is established in the human-automation literature: Parasuraman and Riley's taxonomy of use, misuse, disuse, and abuse, and Lee and See's work on designing for appropriate reliance both document the mechanism (complacency, degraded monitoring under low signal rates). What that literature does *not* establish is that overtrust is the *most common* failure across contemporary AI systems. So I'll hold that as a working hypothesis — a load-bearing one for how I design the audit trail — not a finding. If someone runs the prevalence study, I'll update.

**Calibrated trust** is when reliance matches reliability, and it requires two things: knowing the AI's actual reliability (which requires monitoring infrastructure) and acting on it consistently (which requires discipline plus a workflow that supports discipline instead of fighting it). For the summarizer, calibration is a concrete question you can answer from the audit trail: over the last fifty papers, how often did the Step-4 researcher correct a HIGH-confidence extraction? Almost never means the threshold is well-tuned and you can spot-check less. Frequently means you're undertrusting or the threshold is miscalibrated. The data is *right there in the audit trail.* It should be reviewed periodically. It almost never is. That gap — between having the monitoring data and looking at it — is, in my reading, the field's most easily closable failure.

## Where the map scales, and where it doesn't

Ten steps take an afternoon. A hundred take a week. Thousands — a real multi-agent system — cannot be mapped step by step, and pretending otherwise is its own kind of dishonesty. The response is **hierarchical mapping**: map at the level of major components, then within each component map the sub-components that matter most for handoff and stakes, and document a policy for routine sub-components without enumerating every one. Denser at the high-stakes interfaces, looser in routine processing. The framework only requires that the handoff conditions — where authority transitions, where the audit trail crosses a boundary, where a decision is committed — be documented to a testable standard. Everything else can be summarized.

The trade-off I haven't solved: the delegation map is what *should* happen; the audit trail is what *did* happen. There's no clean way to reconcile them automatically at scale. A tool that detected deviations between map and trail would close a major monitoring gap. The general case, across multi-agent systems with thousands of steps, is genuinely hard, and I don't want to hand-wave it.

## Where this leaves you

Delegation is a contract, not a partition. The handoff condition is the load-bearing clause, and testability is its standard — with the honest caveat that some conditions are testable only by a qualified reviewer, which is a narrower guarantee than "anyone can check." The five capacities have operational forms with artifacts; if the artifact is missing, the capacity didn't happen. The Boondoggle's five questions sort your sub-tasks and, more usefully, force you to write down *why*. Items 5–8 of the map are what separate a supervised pipeline from one that merely appears to work. And trust calibration is monitorable from the audit trail — the monitoring is just rarely done.

The summarizer proved the AI/human boundary isn't aesthetic. Steps 1, 4, and 6 are human because domain knowledge, domain judgment, and interpretive responsibility can't be handed to a pattern-completion engine. Steps 2, 3, and 5 are AI because they're cheap to verify, their failures are bounded and detectable, and they're reversible at the next human step. That's not where the *work* looks like it is. It's where the *judgment* is. Next chapter, we take this same discipline to communication — dashboards, where the same data can be encoded to inform or to mislead, and the design choice carries the weight.

## Exercises

### BUILD

**B1 — Produce a Boondoggle Score for your real task.** Take a validation pipeline you're actually building. Decompose it into 8–20 steps. For each step, apply the five Boondoggle questions and assign it to AI, human, or hybrid. Label the supervisory capacity each human step exercises ([PA], [PF], [TO], [IJ], [EI]). Write the handoff condition for every step — and make each one testable: hand it to someone who didn't build it and confirm they can determine, for a sample case, whether it was met. Before you build the map, *lock a prediction*: how many steps will end up Claude, human, and hybrid; which step will be the most contested; and which handoff condition will be hardest to make testable. Then build the full eight-item map (at least 10 steps) and compare the result to your prediction. You are graded on the testability of the handoff conditions and the honesty of the prediction-versus-result gap.

**B2 — Sign a phase gate.** For your map, write a one-page attestation that names, for the highest-stakes handoff in your pipeline: what was checked, against what criterion, by whom, and what would trigger escalation. Sign it. The point is not the signature; it's that a signature you're willing to give forces the handoff condition to be real.

**B3 — Compute a trust-calibration number.** For any AI step in your pipeline with an accept/override log, count how often the human overrode, then audit a sample of the *accepted* outputs against ground truth. Compute the override rate and the estimated AI error rate on accepted outputs. Name which trust-calibration failure mode your deployment exhibits, and cite what in the audit trail would let you monitor it going forward.

### AUDIT

**A1 — Find the missing human decision node.** Take someone else's boondoggle or delegation map (a teammate's, a vendor's, a published system diagram). For each step, ask: is the handoff condition testable by a non-author? Find the step where an irreversible or high-stakes action happens with no explicit human decision node in front of it — the place where "the model said so" is the only available audit response. Write the missing node: what a human must check, against what criterion, at what granularity, before the action commits.

**A2 — Downgrade an untestable handoff.** Take a handoff condition written as "the human reviews the output" (you will not have to look far). Rewrite it to pass the non-author test: name what is checked, against what criterion, at what granularity, with what recorded disposition. Then explain, in two sentences, why the original made overtrust *less visible* than undertrust.

**A3 — Judge the delegation-as-contract framing itself.** In 400–600 words, argue whether "delegation is a contract, not a partition" is a genuinely useful reframing or an obscuring metaphor. Address the strongest version of the opposing view: that for low-stakes, reversible, cheap-to-verify tasks, a partition is exactly the right model and the contract framing is overhead.
