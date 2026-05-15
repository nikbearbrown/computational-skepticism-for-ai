# Chapter 10 — Delegation, Trust, and the Supervisory Role
*Write the contract before you trust the handoff.*

---

I want to tell you about two engineering teams.

Both teams have built validation pipelines for an AI system that scores loan applications. The pipelines are close to identical at the technical level. Same data. Same model. Same fairness metrics. Same monitoring infrastructure. They differ in one thing.

The first team's documentation says: *AI scores the application, the loan officer reviews and decides, the system logs both.* On every component, the human and AI roles are described at this level of generality.

The second team's documentation says something different. *The AI computes the score and produces a brief explanation. The loan officer is required to verify that the explanation is consistent with the application data, to check whether any of three named edge-case patterns are present using a checklist embedded in the interface, and to record their decision with one of four documented justification codes. If the AI score is below 0.3 or above 0.7, the loan officer's decision can match the AI without further review. If the score is between 0.3 and 0.7, a second loan officer must independently review before either can record a decision.*

Both pipelines deploy. Both work, in the sense that loans get scored and decided.

Then both teams go to the adoption committee for an expanded rollout. The committee asks the same question of each team: *who is responsible if a loan decision is challenged?*

The first team cannot answer cleanly. The AI produced the score. The loan officer made the decision. The documentation says *the loan officer reviews*, but does not specify what review means. In the case of a particular challenged decision, was review performed? At what depth? Against what criteria? The team has to go back and figure out what their own pipeline was supposed to do. The committee tables the rollout.

The second team produces the documentation. The committee can read, in writing, what the AI did, what each loan officer was required to verify, and what triggered escalation. The committee may still reject the rollout — they have substantive reasons available to them. But they reject it for substantive reasons, not for documentation reasons. They are not waiting on the team to figure out what their own pipeline does.

The difference between the two pipelines is not a difference in the technology. It is a difference in the *delegation map*. And that is what this chapter is about.

I want you to come away holding one idea: a delegation is not "the AI does this part." A delegation is a *contract* with explicit boundaries — what the AI does, what the human does, the testable handoff between them, and what happens when the handoff fails. That formulation sounds dry. It is the difference between a pipeline that passes adoption review and one that does not.

---

**What you will be able to do after this chapter:**

- Construct a delegation map with testable handoff conditions for a multi-step pipeline
- Apply the five Boondoggle questions to sort pipeline sub-tasks into delegation buckets
- Identify which trust-calibration failure mode a deployment is in, given accept/override data
- Operationalize each of the five supervisory capacities as a concrete pipeline job with a documented artifact
- Use Gru to generate a Boondoggle Score for a real project and interpret what it reveals
- Produce an AI Use Disclosure that functions as a supervisory log, not a compliance checkbox

**Prerequisites:** Chapter 1's five supervisory capacities and the solve-verify asymmetry are both required vocabulary. Chapter 4's AI Use Disclosure is extended here. Chapter 7's defended-choice format is structurally related to the delegation map — both are engineering decisions under value pluralism, documented for external review.

**Where this fits:** This chapter is the operational center of the book. The chapters before it built the apparatus. This chapter operationalizes that apparatus into pipeline documentation you can hand to an adoption committee. Chapters 11–14 apply the apparatus to communication, accountability, and the limits of the technical.

---

## The handoff condition

Let me start with the load-bearing piece, because everything else depends on it.

A delegation map describes, for each step in a pipeline, who owns the step (AI, human, or hybrid), what goes in, what comes out, and — crucially — what signals that the step has completed correctly and the next step can proceed. That signal is called the handoff condition. It is the load-bearing element of the entire map, and it has one essential property: *it has to be testable*.

Testable means a non-author of the pipeline can read the condition, observe the system, and determine whether the condition is met. Untestable conditions sound like English but do not survive contact with a reviewer.

Let me show you the contrast.

Untestable handoff condition: *"The AI produces a reasonable result and the human reviews it."* The word "reasonable" is not specified — what counts as reasonable for this kind of output? The word "reviews" is not specified — what does the human do when reviewing? Five different loan officers reading this condition will execute five different behaviors and call all of them reviewing. The pipeline will run. The documentation will say it ran. The audit committee will not be able to tell what actually happened.

Testable handoff condition: *"The AI produces a score in the interval zero to one with a confidence interval. The human accepts the score, requests re-scoring, or overrides. In the override case, the human records one of four documented justification codes."* Every term has a specifiable operational form. Five different loan officers reading this condition execute the same behaviors. An external reviewer can examine a recorded decision and determine whether the condition was met.

The procedure for getting from the first to the second is unromantic. You write your handoff condition in your first attempt. You identify every term in it that requires interpretation. For each interpretive term, you either replace it with a specifiable criterion or you document a guideline that pins down the interpretation. You hand the documentation to someone who did not write it and ask them, for a sample case, to determine whether the condition was met. If they cannot, the condition is not testable, and you go again.

This is documentation work. It is not glamorous. It is the difference between a pipeline that survives adoption review and one that does not.

| Domain | Untestable version | Testable version | What interpretation got pinned down |
|---|---|---|---|
| **Loan scoring** | "The model is fair across borrowers." | "FPR equalized to within 2 pp across the four protected-class groups, on the audit sample drawn from Q3 2025." | *Fair* = equal FPR; *across borrowers* = the four named groups; *within* = tolerance specified |
| **Medical triage** | "The model handles edge cases responsibly." | "On the held-out 200-case rare-condition set, sensitivity ≥ 0.95 and any false negative is escalated to clinician review within 30 min." | *Edge cases* = a named set; *responsibly* = a metric and an escalation contract |
| **Content moderation** | "The model respects context." | "On the 500-case context-flip set (same text, different source community), the moderation decision changes ≤ 2% of the time." | *Context* = the source community; *respects* = decision invariance under that change, with a tolerance |

---

## The Five Supervisory Capacities as pipeline jobs

There are five supervisory capacities I introduced in Chapter 1, and this is the chapter where each becomes a concrete job in the pipeline rather than a personality trait. Engineers sometimes hear "supervisory capacity" and reach for words like *judgment* and *experience* — words that describe a person rather than a task. The reframe of this chapter is that each capacity has an operational form, and the operational form is something the pipeline either has or does not.

*Plausibility auditing* is the capacity that asks: given what I know about the world this output describes, is this output the kind of thing that could be true? Operationalized, it is a checklist embedded in the workflow, with specific verification questions matched to the AI's output type. The audit is not a feeling. It is a series of yes/no questions the supervisor answers and the system records. If the checklist is missing, the auditing did not happen, regardless of what the supervisor felt about the output.

*Problem formulation* is the capacity that, before the AI is invoked, specifies the question being asked, the evaluation criteria for the answer, and the conditions under which the AI is the right tool. Operationalized, it is a written specification — usually a paragraph or two — included in the deployment documentation. An external reviewer can read the specification and either accept or reject it. If the specification is missing, the formulation did not happen.

*Tool orchestration* is the capacity that, for each step in the pipeline, decides which tool is responsible, why that tool is the right one, and what the handoff between tools is. Operationalized, it is the delegation map itself.

*Interpretive judgment* is the capacity that reads the AI's output in the deployment context and interprets what the output means for the decision being made. Operationalized, it is a documented interpretation in the audit trail, with reference to the deployment-specific factors that shaped it. *The decision was X because the score was Y in this context, where this context means Z.*

*Executive integration* is the capacity that synthesizes outputs from multiple tools, multiple humans, and multiple monitoring signals into a decision the integrating system can stand behind. Operationalized, it is a decision document with named contributors and a clear authority structure.

Each of these is a job in a pipeline, with a documented operational form. The first team in the opening had no documented operational forms. The second team had all of them.

| Capacity | Operational form in a pipeline | Artifact that documents it | Failure mode if absent |
|---|---|---|---|
| **Plausibility Auditing** | Independent check of model output against domain ground truth at each step | Plausibility audit log per output batch | Confidently wrong outputs ship; failures only surface downstream |
| **Problem Formulation** | Pre-deployment scoping doc that names the question, the data scope, and the failure modes anticipated | Scoping doc + deviation log | Pipeline solves the wrong problem fluently |
| **Tool Orchestration** | A per-step tool inventory: tools allowed, tools forbidden, budgets, rate limits | Tool inventory + per-action log | Resource exhaustion; tool misuse; uncontrolled side effects |
| **Interpretive Judgment** | Domain reviewer note on every high-stakes output, with disposition | Review log with named reviewers | Ambiguous outputs proceed unchallenged; "the model said so" becomes the audit response |
| **Executive Integration** | Decision protocol when capacities conflict — who decides, on what evidence, with what sign-off | Signed decision log | Failures distribute across the team with no accountable human |

---

## The Boondoggle questions

Now the question that comes before the map: which sub-tasks in your pipeline should the AI do, and which should it not? This is not an aesthetic decision. It is a structured assessment with five questions you ask of each sub-task.

I call the assessment the Boondoggle Score, and it lives inside Gru — the software design consultant tool built on this curriculum, available at [nikbearbrown.com/tools/gru-tool](https://www.nikbearbrown.com/tools/gru-tool) as a Claude Project. The score is less important than the questions, so let me walk through the questions.

The first question is *verification cost*. Can a human verify the AI's output cheaply, or does verification require resources comparable to producing the output from scratch? Tasks that are cheap to verify — proofreading a generated summary against a source document, sanity-checking a numeric calculation, scanning a list of candidates — are good AI tasks. The asymmetry between solving and verifying is what makes the AI useful in the first place (Chapter 1's solve-verify asymmetry, restored to its original direction). Tasks that are expensive to verify are dangerous, because the cost structure quietly pushes the supervisor toward accepting the output rather than checking it.

The second question is *stakes*. What is the cost of being wrong on this sub-task? Low-stakes sub-tasks tolerate higher AI error rates because the downside is bounded. High-stakes sub-tasks require human review or human-only decision-making, even if the AI's average performance is good — because the average is not the relevant statistic when a single bad outcome is catastrophic.

The third question is *distribution match*. Is the input to this sub-task within the AI's training distribution, or is it likely to land in a region of the input space where the AI is undertrained? In-distribution sub-tasks are AI-friendly. Out-of-distribution sub-tasks are dangerous regardless of average performance, because the average was computed on cases that look unlike the case in front of the supervisor right now.

The fourth question is *reversibility*. Can the action be undone if it is wrong? Reversible actions tolerate higher AI error rates. Irreversible actions — deletes, sends, financial transfers, anything that touches the world in a way that cannot be retracted — should be gated behind explicit human approval, almost without exception.

The fifth question is *audit trail clarity*. Does the AI's action leave a trail that can be reviewed after the fact? Actions with clear trails are AI-friendly. Actions whose effects are entangled with downstream state changes — such that you cannot tell, after the fact, what the AI did and what propagated from it — are not.

The five questions sort sub-tasks into three buckets: appropriate for AI execution, human-only, and hybrid (AI-assisted with human verification at specified handoff conditions). The output of the assessment is not a recommendation per se. It is a *documented justification for the delegation choice* that becomes part of the pipeline documentation.

| Question | What low risk looks like | What high risk looks like | Where high risk pushes the delegation |
|---|---|---|---|
| **Verification cost** | Output is checkable in seconds; the right answer is obvious by inspection | Verification requires a domain expert + ≥ 30 min per item | Toward verify-before-trust or do-not-delegate |
| **Stakes** | Wrong answers waste time but harm no one outside the team | Wrong answers reach external parties, regulators, or vulnerable users | Toward do-not-delegate without independent review |
| **Distribution match** | Inputs match the AI's training distribution; failures are visible | Inputs are tail cases or out-of-distribution by construction | Toward verify-before-trust with explicit OOD checks |
| **Reversibility** | Outputs are drafts that can be discarded | Outputs trigger irreversible action (a write, a wire, a publication) | Toward do-not-delegate without a hard human-approval gate |
| **Audit trail clarity** | Every step is logged with inputs, outputs, and timestamps | The chain of decisions is opaque or scattered across systems | Toward do-not-delegate until logging is in place |

---

## The full delegation map structure

A delegation map is a structured document. For each step in the pipeline it specifies:

1. **Step name and purpose.** What is this step trying to accomplish?
2. **Owner.** AI, human, or hybrid?
3. **Inputs.** What does this step consume?
4. **Outputs.** What does this step produce?
5. **Handoff condition.** What signals that the step has completed correctly and the next step can proceed? (The load-bearing element — testable.)
6. **Failure mode.** What does failure of this step look like, and what triggers escalation?
7. **Verification.** Who verifies that the step did what it was supposed to do, and how?
8. **Audit trail.** What is recorded, where, in what format, retained for how long?

Items 1–4 are standard engineering documentation. Items 5–8 are the supervisory additions. Most engineering documentation in current AI deployments contains items 1–4 and omits items 5–8. The omission is the gap.

The test for completeness: can an engineer who did not build the pipeline read the map and determine, for any given case, whether each step was executed correctly? If not, one of the eight items is missing or untestable.

| Item | What 'missing' looks like in practice |
|---|---|
| 1. **Task definition** | The handoff specification is vague; two reviewers reading it would disagree about what the AI is supposed to do |
| 2. **Input contract** | The inputs are unscoped; the AI receives data of types or sources not anticipated at design time |
| 3. **Output contract** | The expected output shape, format, and acceptance criteria are not written down |
| 4. **Tool inventory** | No record of which tools the AI may call; no budget caps or rate limits |
| 5. **Plausibility check** *(supervisory addition)* | No independent check that the output corresponds to the world it represents — a pipeline loses the ability to catch confidently wrong outputs |
| 6. **Failure routing** *(supervisory addition)* | No declared escalation path — failures distribute across the team with no one accountable |
| 7. **Audit trail** *(supervisory addition)* | The chain of inputs, decisions, and outputs cannot be reconstructed after the fact — post-incident review becomes impossible |
| 8. **Sign-off authority** *(supervisory addition)* | No named human is the accountable decision-maker — the pipeline runs but no one can be held to its outputs |

*Items 5–8 are what distinguishes a supervised pipeline from a delegated one. A pipeline missing any of items 1–4 is broken. A pipeline missing any of items 5–8 is unsupervised — even if it appears to be working.*

---

## A worked walkthrough: the Research Paper Summarizer

Everything above is abstract. Let me make it concrete with a system I will build step by step, using Gru as the conductor.

The system is a *Research Paper Summarizer with Citation Verification*. The user pastes a PDF of an academic paper. The system returns a structured summary — problem statement, method, key findings, limitations — with each factual claim linked to a specific passage in the source. A researcher or student uses this to decide whether a paper is worth reading in full.

This system is simple enough to follow but complicated enough that the human-AI boundary is genuinely contested at several steps. By the end of the walkthrough, you will be able to point to exactly where a human must be present and exactly why AI alone will not do.

### Step 1 — Problem formulation with Gru's /v0

Before writing a line of documentation, Gru requires one thing: a sentence that names the thing being built, not the problem it solves. This is the /v0 gate. Skipping it produces documents that look rigorous and describe nothing specific.

Here is what that conversation looks like. I open Gru and type:

```
/v0
```

Gru asks three questions in sequence. The third is the one that matters:

> *In one sentence — not a paragraph, not a list — what are you proposing to ADD? The sentence must name the thing being built, where it sits, and what it produces. FORMAT: "[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]."*

A weak answer: *"A tool to help researchers save time on literature review."*

That names a goal, not a thing. Gru will not move.

A stronger answer: *"The Paper Summarizer is a structured-extraction pipeline inserted between PDF ingestion and researcher review that produces a claim-linked summary with passage citations for each factual assertion."*

Now Gru has something to work with. Notice what the sentence encodes: the word *claim-linked* specifies that each summary claim maps to source text, not just that the summary exists. The word *passage citations* specifies that the link is specific (a passage) not general (the paper). These are not details to figure out later. They are the engineering constraints that determine which steps need human verification.

**Why this is a human step.** Gru asks the question, but the answer requires me. An AI could generate plausible-sounding sentences of this form. It cannot determine whether *claim-linked* is the right specification for my deployment — whether researchers using this tool need sentence-level citations or paragraph-level, whether the summary structure matches how researchers actually read papers in this domain, whether the word *factual assertion* is the right boundary for what gets cited. Those are domain judgments. They determine the correctness criteria for every subsequent step. The problem formulation is not a form to fill in. It is the most consequential decision in the project, and it is irreducibly mine.

<!-- → [IMAGE: Gru /v0 conversation flow — user types /v0, Gru asks three questions in sequence, user provides weak answer (shown with annotation "names a goal, not a thing"), user provides strong answer (shown with annotation "names thing / insertion point / output"). Caption: "The /v0 gate produces one sentence. That sentence is the engineering specification everything else is tested against." Figure 10.5] -->

### Step 2 — Intake with /v1

Once /v0 is confirmed, Gru runs /v1 — a structured intake that produces a problem summary in a canonical form:

> *"This system is [WHAT] for [WHO], that solves [CORE PROBLEM] through [PRIMARY MECHANISM]. It occupies the space between [COMPARABLE A] and [COMPARABLE B], and it succeeds when the user can [SUCCESS CONDITION] without [CURRENT FRICTION]."*

Here is my /v1 prompt to Gru:

```
/v1
```

Gru asks eight questions. The answers I provide:

- **System name:** Paper Summarizer
- **Core problem:** Researchers spend 15–30 minutes skimming a paper to decide whether it warrants full reading; they want that decision to be reliable and fast.
- **Primary user:** A doctoral student or postdoc processing 10–20 papers per week during a literature review.
- **What existing solutions miss:** General-purpose summarizers lose methodological detail and cite nothing. Reading the abstract misses findings buried in results sections.
- **Category of system:** Structured extraction pipeline with human-in-the-loop verification.
- **Deployment target:** Web app, single-user initially.
- **Build scale:** Solo developer, two-week build.
- **Three systems the user relies on:** Zotero (reference management), Google Scholar (discovery), their institution's library PDF access.

Gru produces the problem summary:

> *"The Paper Summarizer is a structured-extraction pipeline for doctoral researchers that solves the reliable-triage problem — deciding whether a paper warrants full reading — through claim-linked extraction with passage citations. It occupies the space between generic AI summarizers (fast but uncited) and full reading (thorough but slow), and it succeeds when a researcher can determine a paper's relevance and credibility in under five minutes without reading beyond the summary."*

**Why the problem summary matters for delegation.** The phrase *claim-linked extraction with passage citations* is now a testable success criterion. Any AI step in the pipeline that produces text without source links has failed, regardless of how fluent the text is. The phrase *determine relevance and credibility* specifies what the summary must enable, which means any summary that is accurate but hides methodological weaknesses has failed. These criteria cannot come from the AI. The AI does not know what researchers in this domain consider methodologically credible. I do. The problem summary crystallizes that knowledge into a form the pipeline can be tested against.

### Step 3 — Architecture principles with /v2

Gru now asks for architecture principles — non-negotiable design commitments that bound every downstream decision. I run:

```
/v2
```

After reviewing the /v1 summary, I commit to three principles:

**Citation fidelity over fluency.** Every claim in the summary must be traceable to a specific passage. A fluent summary with unverifiable claims is worse than a rough summary with exact citations. This principle rules out using AI to "fill in" claims it infers rather than extracts.

**Failure visibility.** When the pipeline cannot reliably extract a section — methods are embedded in a figure caption, findings are in a supplemental file, the PDF is a scanned image — the system must say so explicitly rather than hallucinate a plausible substitute. The output "methods section not parseable" is more useful than a confident fabrication.

**Human authority over scope.** The researcher decides which sections matter for their use case. The system proposes a default structure; the researcher can modify it before extraction runs. The AI's proposed structure is an input to human judgment, not a determination.

**Why principles are a human step.** Gru can generate plausible-sounding principles from the problem summary. It cannot determine which trade-offs are right for this deployment. The "citation fidelity over fluency" principle rules out a large class of AI behavior that users of general-purpose summarizers accept routinely. That ruling-out is a values choice. It encodes my judgment that researchers are better served by honest gaps than confident hallucinations. I have to make that judgment. Gru cannot make it for me, because making it requires knowing what harms researchers in my target domain — and that knowledge is not in the prompt.

| Principle | Design commitment | One decision that honors it | One decision that violates it | Failure state if ignored |
|---|---|---|---|---|
| **Provenance preservation** | Every claim in the output is traceable to a span in the input paper | Each generated sentence carries a citation key linked to a source span | Output mixes paraphrase with synthesis without citation keys | Reviewer cannot tell which claims are summarized vs. fabricated |
| **Bounded autonomy** | The pipeline cannot reach data outside the input PDF | Tools are scoped to the file path; no web fetch | A "supplementary lookup" tool added without scope review | Hallucinated citations from outside the corpus |
| **Independent verification** | A second pass checks the first pass | A separate plausibility-audit step runs against the source spans | The summarization model also self-verifies in the same call | Errors that the model cannot catch about itself ship downstream |
| **Disclosure as default** | Every step the AI did is visible to the reader | Per-step AI Use Disclosure block in the output | The disclosure is opt-in or buried in a footer | Readers cannot calibrate trust in the output |
| **Reversible defaults** | The pipeline produces drafts, not final commitments | Output is a markdown draft, not an autopublished post | Output is auto-pushed to a public surface | A bad summary ships before review |

### Step 4 — Core user flows with /v3

Now the primary flow, written at the interaction level:

```
/v3
```

Gru asks me to define the happy path, the integration flow, and the administrative flow. The happy path:

1. Researcher uploads PDF.
2. System parses the PDF into sections (Introduction, Methods, Results, Discussion, Limitations). *AI task.*
3. System extracts the core claim for each section, with passage citations. *AI task.*
4. System flags any section where citation confidence is below threshold. *AI task.*
5. Researcher reviews the flagged sections and either confirms, corrects, or marks as unverifiable. *Human task.*
6. Researcher reviews the full summary for accuracy and domain coherence. *Human task.*
7. Researcher saves or exports the verified summary.

The integration flow: PDF parsing uses a library (pdfplumber or similar). The AI extraction uses a language model API. The citation confidence scoring uses a second pass over the extracted text.

The administrative flow: I need a way to see which extractions are being flagged most often — which section types, which paper types, which journals — so I can tune the confidence threshold and identify systematic failure modes.

**Why the flow requires human judgment to write.** Step 5 and step 6 are the load-bearing human steps. The reason they are human steps cannot be determined by AI: it requires knowing that researchers cannot rely on AI to evaluate domain-specific methodological quality. A language model may correctly extract the claim "we used a random effects model" and produce a citation. It cannot flag that a random effects model is inappropriate for this study design — that judgment requires domain knowledge the model does not reliably have. That is why step 6 is a human step, and why the handoff condition for step 5 must specify what the researcher is checking, not just that checking occurred.

<!-- → [IMAGE: Happy path flow diagram for the Paper Summarizer — seven steps as labeled boxes in sequence, color-coded by owner: gray for AI steps (2, 3, 4), white with border for human steps (5, 6), neutral for boundary steps (1, 7). Annotations at the two transitions between AI and human ownership: "handoff condition must be testable here." Caption: "The flow shows where authority changes hands. Those transitions are where the delegation map must be tightest." Figure 10.7] -->

### Step 5 — Generating the Boondoggle Score with /claude

Now I have enough: a confirmed problem sentence, a problem summary, three architecture principles, and a core user flow. I run the Boondoggle Score:

```
/claude
```

Gru asks three questions before generating: deployment target (web app), team Claude fluency level (Level I — copy-paste individual prompts), and whether any components are flagged EXPERIMENTAL (the citation confidence scoring is experimental — I have not validated the threshold).

Gru generates the score. I will show you the most important steps in full, because this is where the delegation map becomes concrete.

---

**STEP 1 · PHASE F · HUMAN TASK**

*Supervisory Capacity: [PF] Problem Formulation*

*Action: Define the section taxonomy the parser will use. Write a list of section types the system will recognize (Introduction, Related Work, Methods, Results, Discussion, Limitations, Appendix, References) and the rules for what to do when a section has an atypical heading (e.g., "Experimental Design" maps to Methods, "Future Work" maps to Discussion). This taxonomy is the specification the AI extraction prompt will be built against. It cannot be generated by AI because it requires knowledge of how papers in your target domain are structured — and domain variation is exactly the failure mode you must not silently absorb.*

*Handoff Condition: You have a written list of recognized section types, mapping rules for variant headings, and a policy for sections that cannot be mapped. An engineer reading this list can predict, for any given paper heading, how the system will classify it.*

*Dependency: None. This is the foundation.*

---

**STEP 2 · PHASE F · CLAUDE TASK**

*Context Required: Step 1's section taxonomy (paste directly into prompt). The architecture principle "failure visibility" (paste the one-sentence statement).*

```
You are a document parser assistant. I will give you the text of a PDF academic paper, 
extracted as plain text. Your task is to segment the text into named sections using 
the taxonomy below.

SECTION TAXONOMY:
[paste Step 1 output here]

For each section:
- Output the section name (from the taxonomy)
- Output the full text of that section
- If a heading does not match the taxonomy, apply the mapping rules below
- If a section cannot be mapped, output: UNMAPPED: [original heading text]

MAPPING RULES:
[paste Step 1 mapping rules here]

FAILURE VISIBILITY RULE: If the section text is under 50 words, or if the 
section heading appears to be a figure caption or table note rather than a 
section header, flag it as: SUSPECT: [section name] — [reason].

Do not infer content. Do not fill gaps. Output only what is present in the text.

OUTPUT FORMAT:
Return a JSON array. Each element: 
{"section": "section_name", "text": "full section text", "status": "OK | UNMAPPED | SUSPECT"}

PAPER TEXT:
[paste extracted paper text]
```

*Expected Output: A JSON array where every section is named, every heading is either mapped or flagged UNMAPPED, and every suspect section is flagged. No invented content.*

*Handoff Condition: The JSON array contains at least one section tagged OK. Every heading in the original paper appears somewhere in the output — either as a recognized section, UNMAPPED, or SUSPECT. No section has been silently dropped.*

*Dependency: Step 1 complete.*

---

**STEP 3 · PHASE C · CLAUDE TASK**

*Context Required: Step 2's JSON output. The architecture principle "citation fidelity over fluency." The problem summary's success criterion: "claim-linked extraction with passage citations."*

```
You are a structured extraction assistant. I will give you the segmented text of an 
academic paper in JSON format. For each section, extract the core claim — the single 
most important assertion the section makes — and identify the specific passage that 
best supports it.

EXTRACTION RULES:
1. The claim must be a direct extraction or minimal paraphrase of text present in the 
   section. Do not infer or generalize beyond what the text states.
2. The citation must be a verbatim excerpt of 1–3 sentences from the section text 
   that most directly supports the claim. The excerpt must appear word-for-word in 
   the source text.
3. If you cannot identify a clear core claim — the section contains only procedures, 
   only data tables, or only references — output: NO_CLAIM: [reason]
4. If you cannot find a passage that directly supports a claim you extracted, output 
   the claim and set citation to: NO_CITATION — then flag the section as requiring 
   human review.

OUTPUT FORMAT:
Return a JSON array. Each element:
{
  "section": "section_name",
  "claim": "extracted claim text",
  "citation": "verbatim supporting passage or NO_CITATION",
  "confidence": "HIGH | MEDIUM | LOW",
  "flag": null | "REQUIRES_HUMAN_REVIEW"
}

Set confidence:
- HIGH: claim is a direct quote or minimal paraphrase; citation is verbatim and clearly supports claim
- MEDIUM: claim requires inference across two sentences; citation is present but indirect
- LOW: claim cannot be supported by a single passage; citation is absent or tangential

SEGMENTED PAPER:
[paste Step 2 JSON output]
```

*Expected Output: A JSON array with one entry per section. Every entry has a claim (or NO_CLAIM), a citation (verbatim or NO_CITATION), a confidence level, and a flag if review is needed. No section is silently skipped.*

*Handoff Condition: Every section from Step 2 appears in the output. Every citation tagged HIGH can be found verbatim in the Step 2 source text for that section. No citation has been paraphrased or synthesized — it is extracted or absent.*

*Dependency: Step 2 complete and handoff condition verified.*

---

**STEP 4 · PHASE C · HUMAN TASK**

*Supervisory Capacity: [PA] Plausibility Auditing*

*Action: For every entry tagged LOW confidence or REQUIRES_HUMAN_REVIEW, open the source paper and verify three things: (1) Is the extracted claim an accurate representation of what the section says — not just fluent, but accurate in the domain-specific sense? (2) Is the cited passage the most informative support available, or is there a stronger passage the AI missed? (3) Does the claim omit a qualification that changes its meaning (e.g., the AI extracted "the model outperformed baselines" but the paper said "the model outperformed baselines on the training set only")? For each flagged section: confirm, correct, or mark as unverifiable.*

*Action: For every entry tagged HIGH confidence, spot-check at least one in five by locating the citation in the source PDF and confirming it appears verbatim.*

*This step cannot be delegated because it requires domain judgment about whether a claim is meaningfully accurate — not just textually faithful — and that judgment requires knowledge of the field's conventions for how results and limitations are reported.*

*Handoff Condition: Every LOW and REQUIRES_HUMAN_REVIEW entry has a human disposition: confirmed, corrected, or marked unverifiable. A random sample of HIGH-confidence entries has been spot-checked. The researcher has signed off on the reviewed output.*

*Dependency: Step 3 complete.*

---

**STEP 5 · PHASE C · CLAUDE TASK**

*Context Required: Step 3 JSON (with Step 4 human corrections applied). The problem summary's success criterion: "determine relevance and credibility in under five minutes."*

```
You are a summary formatter. I will give you the extracted claims and citations 
for a research paper in JSON format. Human review has been applied; the data 
has been confirmed or corrected.

Your task is to format the claims into a structured summary for a researcher 
deciding whether to read the full paper. The summary must:

1. Present each section as a short paragraph: the core claim, followed by the 
   verbatim citation in block quote format.
2. At the top, include a PAPER SNAPSHOT: three bullet points — (a) the central 
   research question, extracted from the Introduction claim; (b) the primary 
   method, extracted from the Methods claim; (c) the headline finding, extracted 
   from the Results claim.
3. At the bottom, include a VERIFICATION STATUS section listing: sections reviewed 
   by human (list them), sections marked unverifiable (list them with reason), 
   sections with HIGH-confidence automated extraction only (list them).

DO NOT add interpretive commentary. DO NOT evaluate whether the paper's methods 
are sound. DO NOT add claims that are not in the input JSON. Your job is formatting 
and organization, not evaluation.

INPUT JSON:
[paste Step 3 + Step 4 corrected JSON]
```

*Expected Output: A formatted summary with a PAPER SNAPSHOT at top, section-by-section claims with verbatim block-quote citations, and a VERIFICATION STATUS section at bottom.*

*Handoff Condition: Every claim in the formatted summary appears in the Step 3/4 JSON. The VERIFICATION STATUS section accurately reflects which sections were human-reviewed and which were not. No new claims have been added.*

*Dependency: Step 4 complete.*

---

**STEP 6 · PHASE C · HUMAN TASK**

*Supervisory Capacity: [IJ] Interpretive Judgment*

*Action: Read the formatted summary as a researcher would read it — not as a QA check on the AI's output, but as the intended user of this summary. Ask: Would this summary give a researcher a reliable basis for the triage decision? Specifically:*

- *Does the PAPER SNAPSHOT accurately characterize the paper's contribution?*
- *Are the limitations represented — or does the summary accidentally make the paper look stronger than its own claims warrant?*
- *Is there anything in the VERIFICATION STATUS that should affect how a researcher trusts this summary — and if so, is that clearly communicated?*

*Make any final edits. Sign the summary with your name and the date of review.*

*This step cannot be delegated because it requires the researcher to exercise their own judgment about whether this summary would mislead a peer who trusted it. The AI cannot assess its own misleading — it has no model of what a researcher in this domain would infer from a gap or a hedge.*

*Handoff Condition: The researcher has read the summary as a user, not as a reviewer, and is willing to put their name on it as a reliable triage artifact.*

*Dependency: Step 5 complete.*

---

**SCORE SUMMARY**

Total steps: 6
Claude tasks: 3 (Steps 2, 3, 5) — 50% of steps
Human tasks: 3 (Steps 1, 4, 6) — 50% of steps

Critical path: Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6

Highest-risk handoffs:
- Step 3 → Step 4: AI citation extraction to human plausibility audit. Risk: researcher accepts HIGH-confidence extractions without spot-checking; a domain-important qualification is silently omitted.
- Step 5 → Step 6: Formatted summary to researcher sign-off. Risk: researcher treats this as a proofreading task rather than an interpretive judgment; the summary ships with a framing that misleads peers.

Supervisory capacity distribution:
- [PA] Plausibility Auditing: 1 step (Step 4)
- [PF] Problem Formulation: 1 step (Step 1)
- [TO] Tool Orchestration: implicitly present across all Claude tasks
- [IJ] Interpretive Judgment: 1 step (Step 6)
- [EI] Executive Integration: 0 steps flagged

Flag: No executive integration step is documented. If this system is used in a team setting — where one researcher runs the pipeline and another uses the summary — a documented handoff between them is missing. Add a Step 7 if the context requires it.

---

<!-- → [IMAGE: Boondoggle Score as a visual timeline — six steps arranged horizontally with alternating Claude/Human shading. Claude steps labeled with their task type (parsing, extraction, formatting); Human steps labeled with their supervisory capacity ([PF], [PA], [IJ]). Red flags at the two highest-risk handoffs. A footer bar shows the supervisory capacity distribution with [EI] explicitly flagged as absent. Caption: "Three of six steps are irreducibly human. The AI does the pattern work. The human does the judgment work. The EI gap is the flag." Figure 10.8] -->

### What the Boondoggle Score reveals

Look at where the human steps fall in the score. Step 1 is human because the taxonomy requires domain knowledge. Step 4 is human because citation accuracy requires domain judgment. Step 6 is human because the researcher must exercise interpretive judgment about what the summary will communicate to a peer.

These are not the obvious heavy-lifting steps. The AI steps — parsing, extracting, formatting — are the ones that look like work. The human steps are the ones that look like review. This is the fluency trap operating at the workflow level: the AI's outputs will be fluent and specific, and the pull toward trusting them and moving on will be strong. The Boondoggle Score makes the failure mode explicit *before* the workflow runs, not after the first researcher trusts a hallucinated citation.

Notice also what the score does not contain: the word "reasonable," the phrase "human reviews," the instruction "check for accuracy." Every human action in the score specifies what is being checked, against what criteria, at what granularity. Step 4 does not say "review the extractions." It says: open the source PDF, verify that qualifications haven't been dropped, spot-check one in five HIGH-confidence entries. That specificity is the difference between a handoff condition that can be audited and one that cannot.

---

## Trust calibration

There is a piece of this that is monitorable in deployment, and that most deployments do not monitor.

When a human supervisor and an AI work together on a stream of tasks, the supervisor's reliance on the AI ought to match the AI's actual reliability for that kind of input in that deployment context. This is what *calibrated trust* means in the operational sense. It does not mean trusting the AI in general. It means trusting the AI to about the degree the AI's actual error rate warrants, on this kind of case.

There are three failure modes, and each produces different downstream errors.

*Undertrust* — sometimes called distrust — is when the supervisor systematically discounts AI output, even when the AI is reliable. The deployment loses the value the AI was supposed to add. This often coexists with backlash against AI deployments — *we tried it, it didn't help* — when the failure was not the AI's accuracy but the supervisor's calibration.

*Overtrust* is when the supervisor accepts AI output when they should not. The fluency trap from Chapter 1 is the canonical case: outputs that look right are accepted, and the verification work the supervisor was supposed to do is silently skipped. In my reading, *overtrust is the dominant failure mode in current AI deployments*. It is also the failure mode the documentation makes least visible, because overtrust does not produce immediate flags. It produces uncaught errors that are discovered later, often by the affected user.

*Calibrated trust* is the case where the supervisor's reliance matches the AI's actual reliability. Achieving it requires two things: knowing the AI's actual reliability for this kind of case, which usually requires monitoring infrastructure, and acting on that knowledge consistently, which requires discipline and supportive workflow design.

In the Paper Summarizer, the trust calibration question is specific: over the last fifty papers processed, how often did the researcher in Step 4 find a correction to make in a HIGH-confidence extraction? If the answer is "almost never," the HIGH threshold is probably well-tuned and the researcher can spot-check less aggressively. If the answer is "frequently," the researcher is undertrusting the threshold or the threshold is miscalibrated. The Step 4 disposition data — confirmed / corrected / marked unverifiable — is in the audit trail. It should be reviewed periodically. It almost never is.

<!-- → [CHART: Three-panel trust calibration visualization. Panel 1 (overtrust): researcher correction rate near zero, AI error rate 15% — gap labeled "uncaught errors, discovered later by affected user". Panel 2 (undertrust): researcher correction rate 60%, AI error rate 5% — gap labeled "wasted effort, backlash". Panel 3 (calibrated): correction rate tracks error rate, corrections concentrated in LOW-confidence entries. Horizontal axis: cases processed over time. Caption: "Calibrated trust is a property of the deployment, not the model. It requires monitoring the audit trail, not just running the pipeline." Figure 10.9] -->

---

## The AI Use Disclosure as supervisory log

Chapter 4 introduced the AI Use Disclosure as a required deliverable for every assignment in this course. Here it becomes something larger.

In its course form, the Disclosure asks the student to document what AI was used, on what step, with what verification. The format is structured. The intent is that, read in aggregate, the Disclosure serves as a *supervisory log* — a record of where the student exercised which supervisory capacity.

The same instrument generalizes to professional practice. Engineering teams deploying AI systems will increasingly be required — by adoption committees, by regulators, by clients — to produce documented disclosures of AI use in their work products. The format will vary; the structure will resemble the course form. The professional habit of producing this disclosure is built in the course.

For the Paper Summarizer, the Disclosure for a single processed paper would read:

**Step 2 (PDF parsing):** Tool: GPT-4 API via custom prompt. Step delegated: section segmentation. What I asked for: classification of paper text into taxonomy-defined sections, with UNMAPPED and SUSPECT flags for non-conforming headings. What the tool produced: JSON array with section classifications. What I verified: all headings from original paper appear in output; no section silently dropped. What I changed: none required on this paper.

**Step 3 (claim extraction):** Tool: GPT-4 API. Step delegated: core claim extraction with verbatim citations. What I asked for: one claim per section with supporting passage. What the tool produced: JSON with claims, citations, confidence ratings, and flags. What I verified: all HIGH-confidence citations spot-checked in source PDF (verified 4 of 20); 2 LOW-confidence entries reviewed and corrected (Methods section: AI dropped "on training data only" qualifier; corrected). What I changed: Methods claim corrected; Limitations marked unverifiable.

**Step 5 (formatting):** Tool: GPT-4 API. Step delegated: structured summary formatting. What I asked for: formatted summary with PAPER SNAPSHOT and VERIFICATION STATUS. What the tool produced: formatted markdown. What I verified: VERIFICATION STATUS accurately reflects corrections from Step 4. What I changed: none.

**Step 6 (sign-off):** My judgment. I read the summary as a researcher deciding whether to read this paper. The VERIFICATION STATUS clearly flags the Methods correction. I am comfortable putting my name on this summary as a reliable triage artifact. Signed: [name], [date].

For the Disclosure to function as a supervisory log rather than a compliance checkbox, it has to be four things: granular (per step), honest (documenting corrections and gaps, not just smooth handoffs), time-stamped, and tied to evidence. The Methods correction in Step 3 is not embarrassing. It is the data point that tells you the pipeline caught a domain-critical qualification that would have misled a downstream reader. That is the system working. The Disclosure makes it visible.

| Field | What goes here | What 'missing' or 'vague' looks like |
|---|---|---|
| **Step name** | Specific step identifier (e.g., "Step 3 — extract methods section") | "AI helped" |
| **Tool used** | Named model + version + temperature/sampling settings | "An LLM" |
| **Input** | Exact input passed to the tool, with provenance link | "Some text from the paper" |
| **Output** | Exact output received | A polished paragraph with no diff visible |
| **Verification done** | The named check applied to the output, by whom, with disposition | "Reviewed" |
| **Correction made (if any)** | The specific change, the reason, and the source span the correction relied on | (Field omitted) |

*The correction is not embarrassing. It is the data that proves the pipeline is working.*

---

## Where the map scales — and where it does not

A clean note for the engineer about to deploy this in their own work.

The delegation map scales with the pipeline. A pipeline of ten steps can be mapped in an afternoon. A pipeline of a hundred steps takes a week, and the map is harder to maintain as the pipeline evolves. A pipeline of thousands of steps — multi-agent systems are headed in this direction — cannot be mapped step-by-step at scale.

The response is *hierarchical mapping*. Map the system at the level of major components. For each component, map the sub-components that matter most for handoff and stakes. For sub-components within the bounds of routine operation, document the policy without enumerating every step. The map becomes a layered document, denser at high-stakes interfaces and looser in routine processing.

This is engineering documentation. It looks like the system architecture documents that good infrastructure teams produce. The delegation map is essentially that — system architecture documentation with explicit human-AI handoffs — and the practices that work for system architecture documentation work here: versioning, review, audit, update at change.

The supervisory framework does not require that every step be hand-mapped. It requires that the *handoff conditions* — the places where authority transitions between AI and human, where the audit trail crosses a boundary, where a decision is committed — are documented to a testable standard. Inside a component whose internal authority structure is settled, the documentation can be lighter. At the seams, it has to be tight.

---

## The shape of the rest

Delegation is a contract, not a partition. The handoff condition is the load-bearing element; testability is its standard. The five supervisory capacities have operational forms — checklist audits, written specifications, the delegation map, documented interpretations, decision documents with authority structures — and the pipeline either has them or does not. The Boondoggle questions sort sub-tasks by where the AI can responsibly act and where it cannot. Trust calibration is a monitorable property of the deployment, and the gap between what could be monitored and what is monitored is the field's most easily closable failure.

The Paper Summarizer walkthrough is not a tutorial on how to build a summarizer. It is a demonstration that every step in a pipeline is either an AI step, a human step, or a hybrid — and that the determination is not aesthetic. It follows from the Boondoggle questions applied honestly. Steps 1, 4, and 6 are human steps because domain knowledge, domain judgment, and interpretive responsibility cannot be delegated to a pattern-completion engine. Steps 2, 3, and 5 are AI steps because they are cheap to verify, their failure modes are bounded and detectable, and their outputs are reversible at the next human step.

The two pipelines from the opening are no longer indistinguishable. The second team's pipeline has the contract written down. The first team's pipeline is held together by what the team members happen to remember, and that is not a basis for adoption review.

The next chapter pivots from the pipeline to the *communication* of what the pipeline found. A dashboard tells a visual story. The same data can produce a dashboard that communicates accurately or one that misleads. The design choices are choices, with normative weight. We will treat them that way.

---

**What would change my mind.** If a tool emerged that automated the construction of testable delegation maps from pipeline code — across diverse domains, with handoff conditions an external reviewer could verify without manual work — the framing of *the map is documentation work the engineer must do* would weaken. The closest tools today are workflow-management platforms, which are infrastructure for execution rather than tools for documenting handoff testability. The construction work remains the engineer's.

**Still puzzling.** I do not have a clean way to integrate the delegation map with the audit trail at scale. The map specifies what *should* happen at each step. The audit trail records what *did* happen. Reconciling the two — automatically detecting deviations from the map in the trail — would close a major monitoring gap. Some cases yield to straightforward implementation. The general case, especially across multi-agent systems with thousands of steps, is hard. I do not yet have a working general approach.

---

## Exercises

### Glimmers

**Glimmer 10.1 — Build your delegation map**

1. Take your own research project (Project v2.0, submitted at the midterm milestone). The project is the case.
2. Decompose the project's validation pipeline into discrete steps. Aim for between 8 and 20 steps. Specifically: data ingestion, EDA, model evaluation, fairness analysis, robustness testing, agentic-system validation if applicable, communication, decision.
3. For each step, apply the five Boondoggle questions. Document your assessment and the delegation bucket.
4. *Lock your prediction:* before constructing the delegation map, predict (a) how many steps will be Claude tasks, human tasks, and hybrids; (b) which step will have the most contested delegation; (c) which step's handoff condition will be hardest to make testable.
5. Construct the delegation map using the eight-item structure from this chapter. Ten or more steps. All eight items per step. Testable handoff conditions throughout.
6. Test the map by handing it to a peer. Have the peer attempt to determine, from the map alone, whether each step's handoff condition is met for a sample case. Record where the peer was unable to determine.
7. Revise the map based on the peer's findings. Document what you changed and why.
8. *Optional:* Run your completed pipeline through Gru's /claude command ([nikbearbrown.com/tools/gru-tool](https://www.nikbearbrown.com/tools/gru-tool)) and compare Gru's Boondoggle Score to your hand-built map. Where do they agree? Where do they differ, and why?

The deliverable is the Boondoggle assessments, the prediction, the map, the peer-test results, and the revision. The grade is on the testability of the handoff conditions and the honesty of the prediction-vs-result gap.

---

### Warm-Up

**1.** The chapter defines a delegation map and identifies one load-bearing element. Name the element, state its essential property, and explain in two sentences why that property is load-bearing — what fails specifically if the element is present but the property is not.

**2.** Below are two handoff conditions from a content-moderation pipeline. Identify which is testable and which is not. For the untestable one, name the specific terms that require interpretation and rewrite the condition so a non-author of the pipeline could verify it on a sample case.

- *Condition A:* "The AI flags content for review. The moderator evaluates the flag and takes appropriate action."
- *Condition B:* "The AI assigns one of five severity codes to the content. The moderator confirms or changes the code and, if the code is 4 or 5, must record a policy citation from the documented list before the decision is logged."

**3.** The chapter argues that each of the five supervisory capacities has an "operational form" — something a pipeline either has or does not. For plausibility auditing and executive integration, describe what the operational form is and what artifact documents it in the pipeline.

**4.** In the Paper Summarizer walkthrough, Step 4 is a human step. Apply the five Boondoggle questions to Step 4's task (reviewing LOW-confidence and flagged extractions). For each question, give your assessment and a one-sentence justification. Does the Boondoggle Score confirm that Step 4 is correctly classified as human-only, or does it suggest hybrid is defensible?

**5.** Gru's /v0 gate required a sentence in the format: "[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]." Explain why this sentence format is more useful as a project foundation than a problem statement like "We need a tool to help researchers with literature review." What specific information does the /v0 format encode that the problem statement does not?

---

### Application

**6.** You are assessing a sub-task in a hiring-screen pipeline: the AI ranks the top 20 candidates from a pool of 200 and produces a brief justification for each ranking. Apply the five Boondoggle questions to this sub-task. For each question, state your assessment (low risk / high risk / uncertain) and your reasoning. Then classify the sub-task into one of the three delegation buckets and write the one-paragraph documented justification you would include in the pipeline documentation.

**7.** A deployed medical-imaging pipeline has the following accept/override data from the last 200 cases: the AI's outputs were accepted 186 times and overridden 14 times. A sampled ground-truth audit of 40 randomly selected cases found 6 AI errors. Compute the supervisor's override rate and the estimated AI error rate. Identify which of the three trust-calibration failure modes this deployment is in, and explain what the downstream consequences of this failure mode look like in practice for this specific pipeline.

**8.** You are reviewing the first team's pipeline from the chapter's opening. The documentation says: "AI scores the application, the loan officer reviews and decides, the system logs both." Your job is to rewrite the delegation map so it would pass the adoption committee's challenge. Produce: (a) a testable handoff condition for the AI-to-loan-officer handoff, (b) the operational form of at least two supervisory capacities visible in the documentation, and (c) a specification for when escalation to a second reviewer is triggered.

**9.** The chapter claims that overtrust is the dominant failure mode in current AI deployments, and that it is the failure mode the documentation makes least visible. Why does documentation make overtrust less visible than undertrust? What would documentation designed to surface overtrust actually look like? Use the Paper Summarizer's Step 4 Disclosure entry as a concrete reference.

**10.** The Paper Summarizer Step 3 prompt includes the rule: *"If you cannot find a passage that directly supports a claim you extracted, output the claim and set citation to NO_CITATION — then flag the section as requiring human review."* Explain why this rule is an instance of the architecture principle "failure visibility." What would happen to Step 4 if this rule were omitted from the prompt? Map the failure to one of the five Boondoggle risk dimensions.

---

### Synthesis

**11.** Chapter 1 introduced the five supervisory capacities. Chapter 10 operationalizes each one as a pipeline job with a documented form. Chapter 7 introduced the defended-choice deliverable as the form of an engineering decision under value pluralism. Using all three frameworks, describe what the delegation map and the fairness-defense document have in common — structurally, not just thematically. What is the general form that both are instances of?

**12.** The chapter identifies a monitoring gap: the audit trail records what did happen, but the delegation map specifies what should happen, and most deployments do not reconcile the two. Design a monitoring protocol — at whatever level of specificity is achievable — that would detect, in the Paper Summarizer pipeline, deviations between the delegation map and the actual audit trail. What specific signals would it look for? What would a deviation look like in the data?

**13.** The Boondoggle Score for the Paper Summarizer flagged that no executive integration step is documented, and noted this would matter in a team setting. Design that step. Write it in full Boondoggle format: step name, owner (human), supervisory capacity label, action (specific enough to be a checklist item), handoff condition (testable), and dependency. What makes this step irreducibly human — specifically, what knowledge or authority does it require that the AI cannot supply?

---

### Challenge

**14.** The chapter's uncertainty section flags a genuinely hard problem: reconciling delegation maps with audit trails at scale across multi-agent systems with thousands of steps. The partial solution the chapter gestures toward covers the easy cases. Characterize what makes the hard cases hard. Specifically: what properties of a multi-agent system make delegation-map-to-audit-trail reconciliation difficult in ways that do not appear in a single-agent pipeline? And what would a general solution need to do that a case-by-case solution does not?

**15.** The chapter frames delegation as a contract between the AI and the human supervisor. But contracts require parties with interests, the capacity to make and honor commitments, and accountability when they don't. An AI system has none of these in the ordinary sense. In what sense is "delegation as contract" a useful framing, and in what sense is it a metaphor that obscures the actual engineering problem? Where does the framing do work, and where does it break down?

**16.** The Paper Summarizer walkthrough applies Gru's Boondoggle methodology to a pipeline with a single human user. Extend the analysis: suppose the system is deployed in a research lab where a graduate student runs the pipeline and a faculty supervisor reviews the output before it is used in a paper. How does the delegation map change? What new human steps are required? What new handoff conditions must be testable? What trust-calibration failure modes does the two-person setup introduce that the single-user setup does not?

---

###  LLM Exercise — Chapter 10: Delegation, Trust, and the Supervisory Role

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** A delegation-map-as-it-is and a delegation-map-as-it-should-be for your agent — drawn directly from the failure cases collected in Chapter 9. Each case reveals a missing handoff condition; this chapter writes them. Plus a Boondoggle Score for the agent's deployment using Gru's questions.

**Tool:** Claude Project (continue). Optional Cowork to maintain the delegation-map files.

---

**The Prompt:**

```
Continuing my Red-Team Casebook. My casebook-index, individual case files, and Bias-and-Leverage Brief are in the Project context.

This chapter teaches that DELEGATION IS A CONTRACT — not "the AI does this part." A contract specifies what the AI does, what the human does, the testable handoff between them, and what happens when the handoff fails. The Five Supervisory Capacities are not personality traits — they are pipeline jobs with documented artifacts. The Boondoggle Score (from Gru) sorts pipeline sub-tasks into delegation buckets.

For my agent, do four things:

1. CURRENT DELEGATION MAP — Document the agent's deployment as it currently is. Walk the pipeline:
   - Input: who provides it, in what format, with what quality control
   - Routing / decision: AI or human? Under what conditions does either act?
   - Action: what tool surface does the agent have access to; what guardrails exist
   - Output: what does the user see, what is logged
   - Review: does anyone review? When? Against what criteria?
   - Escalation: when does the agent escalate vs proceed; is there a person on call when it does?
   For each, note whether the documentation in the actual deployment is at the FIRST-TEAM level (vague) or SECOND-TEAM level (specific, testable handoffs).

2. CASE-DERIVED HANDOFF CONDITIONS — For each Chapter 9 case, identify the specific HANDOFF CONDITION that, if it had existed and been enforced, would have caught the failure. Examples:
   - "If the agent is asked to delete data, the agent must produce a list of the specific data items it will delete and require user confirmation before any deletion tool is called" (catches Ash-style cases)
   - "If the request comes from anyone whose authentication is not directly verifiable, the agent must refuse the action and escalate" (catches identity-spoofing cases)
   - "If the agent's confidence in its understanding of the request is below threshold T, the agent must produce three reformulations and ask the user to pick one"
   Each handoff condition must be TESTABLE — written so an evaluator could check whether it triggered correctly.

3. PROPOSED DELEGATION MAP — Rewrite the deployment map with the new handoff conditions in place. Make every supervisory capacity (Plausibility Auditor, Goal Verifier, Frame Setter, Boundary Enforcer, Capability Definer — or whichever names the chapter uses) into a CONCRETE PIPELINE JOB with:
   - The artifact it produces (a checklist, a log, a confirmation, an escalation ticket)
   - The trigger that fires it
   - Who is responsible
   - Where the artifact is stored

4. BOONDOGGLE SCORE — Apply the five Boondoggle questions from the chapter to the agent's deployment. Score each question on the chapter's scale; compute the overall Boondoggle Score; interpret what it reveals about whether this deployment is currently viable, viable with the proposed handoff conditions, or fundamentally a Boondoggle.

Output two files for the casebook folder:
- `delegation-map-current.md` — the current state
- `delegation-map-proposed.md` — the proposed state with handoff conditions and Boondoggle Score

Plus a one-paragraph note on the deployment's TRUST CALIBRATION failure mode: is the deployment currently OVER-trusting the agent (humans not catching failures the chapter suggests they should), UNDER-trusting (humans wasting capacity on checks the agent reliably handles), or properly calibrated for some failure modes and not others?
```

---

**What this produces:** Two delegation-map files (current and proposed), case-derived testable handoff conditions, the Boondoggle Score, and a trust-calibration assessment. This is the document the casebook hands to a deployment-review committee.

**How to adapt this prompt:**
- *For your own project:* If the deployment's actual map is undocumented (as it often is), reconstruct it from observed behavior. The act of reconstruction itself produces a finding.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not the right fit — these documents are policy, not code.
- *For Cowork:* Recommended for maintaining the two map files alongside the casebook.

**Connection to previous chapters:** The cases from Chapter 9 are the evidence base. The bias mechanisms from Chapter 3 tell you which handoff conditions matter most. The fairness defense from Chapter 7 names which handoff conditions affect which populations.

**Preview of next chapter:** Chapter 11 turns the casebook outward — you'll build a dashboard of your findings, in two versions: an honest one and a deliberately misleading one. The misleading version teaches you what the honest one is doing structurally.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Donald Broadbent** ran the Applied Psychology Unit at Cambridge from 1958 to 1974 and produced the foundational work — *Perception and Communication* (1958), *Decision and Stress* (1971) — on how human attention degrades under monotony, low signal rate, and the structural conditions that supervisory roles tend to produce. The paradox of the well-running automated system is, in Broadbent's vocabulary, a vigilance problem: the rare event the supervisor is supposed to catch is rare specifically because the system runs well, and the supervisor's attentional capacity for that rare event has been quietly eroded by the monotony of the long stretches in between.

![Donald Broadbent, c. 1960s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/donald-broadbent.jpg)
*Donald Broadbent, c. 1960s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Donald Broadbent, and how does his work on *vigilance and attention under low-signal conditions* connect to the supervisory role a person actually has when they're delegating to an AI tool that mostly works — and whose rare failures are the ones the supervisor is supposed to catch? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Donald Broadbent"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *vigilance decrement* in plain language, as if you've never read attention research
- Ask it to compare Broadbent's filter model of attention to the supervisor of a 99.5%-correct AI system
- Add a constraint: "Answer as if you're writing the staffing rationale for a human-in-the-loop deployment"

What changes? What gets better? What gets worse?
