# Agentic Loops: Where Evidence Enters and Action Stops

*An introductory chapter to read after Agents and before The Skeptic's Toolkit.*

An agent fixes three accessibility problems in a ticket form. It runs the scanner again and reports zero findings. It has completed the worklist. Has it made the form accessible?

Perhaps. Or it has disabled the rule that found the problems. Perhaps the scanner checks labels but not the keyboard trap that prevents a person from submitting the form. Perhaps it tested the old page in a cached browser. The final sentence, “all issues resolved,” does not distinguish these possibilities.

This is an illustrative teaching case, not a report of an observed incident. Its point is not that scanners are useless or agents invariably cheat. The point is that an improvement loop can satisfy its own stopping condition while missing the task that justified the loop. Someone must decide what counts as progress, what evidence could contradict it, and what the system is permitted to do next.

In the preceding introduction, the agent became something inspectable: a system with observations, state, tools, decisions, and effects. Here we examine the repeated process connecting those parts. We will learn to draw that process, identify its checks, and put gates where a mistake can become a consequential action. This is preparation for the Skeptic's Toolkit, not a substitute for it. A diagram makes a claim visible. It does not tell us whether the claim is justified.

## What you will be able to do

- Distinguish a reasoning pattern, a workflow pattern, and a pattern for checking progress.
- Identify the observation, proposed action, execution, and feedback in an agentic loop.
- Specify evidence that could reject an agent's claim rather than merely repeat it.
- Place gates before consequential actions and checks after execution.
- Separate a successful task from a stopped, blocked, or inconclusive run.
- Design a bounded evaluation using an authorized sandbox, an observable trace, and a testable acceptance rule.

**Prerequisites:** the preceding Agents chapter. No particular framework is required. The examples use files, forms, and repository changes, but the same questions apply to research agents and service agents.

## A loop is a structure, not a promise

A minimal agentic loop has this shape:

```text
observe current state
       ↓
propose an action
       ↓
check scope and authority ── not allowed ──→ stop or request approval
       ↓ allowed
execute through a tool
       ↓
observe the result and affected state
       ↓
evaluate evidence ── insufficient ──→ bounded next step or escalation
       ↓ sufficient
accept the result and stop
```

Real systems can omit, combine, or distribute these steps. A model may decide the next tool call while a host program enforces an allowlist. A fixed workflow can call a model only at one stage. Several workers can run in parallel. A human can make the acceptance decision. The diagram is an inspection aid, not a requirement that everything happen inside a single model conversation.

We need three distinctions.

**An observation is not automatically trustworthy.** A retrieved page can be stale, a test can run against the wrong version, and an API response can describe an accepted request rather than a completed change. Record where an observation came from and what it actually establishes.

**A proposed action is not an executed action.** Generated code, a plan to send a message, and a tool invocation are different artifacts. A tool invocation may fail or have an uncertain outcome. The trace must preserve those differences.

**Stopping is not succeeding.** The host can end because a task passed, permission was denied, a budget ran out, the user canceled, or no useful next step was available. A responsible result names the reason. “Finished” is too weak a status when someone is relying on the work.

Repeated attempts do not by themselves make a system reliable. They can improve a result when feedback is informative. They can also repeat an incorrect assumption, overfit a test, consume a budget, or multiply a harmful side effect.

## Three kinds of pattern

The companion **Agentic Best Practices** material contains 85 catalog entries grouped into ten checking patterns. Its deck collection also includes five reasoning patterns and five workflow patterns. These are three lenses, not twenty mutually exclusive agent types and not 85 independently validated algorithms.

The catalog is a reading-based synthesis. Some entries are audits, gates, or handoffs rather than repeated improvement loops. A useful classification should help you ask better questions, not make stronger claims than its evidence supports.

### Reasoning patterns: how candidate steps are organized

| Pattern | Working idea | What to inspect |
|---|---|---|
| ReAct | Alternate planning or reasoning with actions and observations. | Does the next action respond to the actual observation, or to an assumption the observation contradicted? |
| Plan-and-Execute | Form a plan, then execute its parts. | Are dependencies and preconditions still true? Who can revise the plan when the world changes? |
| ReWOO | Separate a plan for tool evidence from collection and final synthesis. | Do later evidence requests depend on earlier results? Does the synthesis preserve missing or failed evidence? |
| Reflection | Critique a candidate and revise it against criteria. | Is criticism grounded in a source, test, or rubric? Did revision improve the result or merely its explanation? |
| Tree-of-Thoughts | Explore alternative candidate paths, score them, and select which to extend. | Is the scoring rule valid, and could pruning discard a correct path? What limits search? |

These are useful structural descriptions, not rigid product specifications. Plan-and-Execute implementations can replan. ReWOO does not mean every tool call is independent or safe to run simultaneously. Reflection can help without providing independent verification.

Nor should “inspect reasoning” mean demanding an inaccessible private chain of thought. Students need observable decisions: the selected action, a concise stated rationale, inputs, tool arguments, outputs, artifacts, and checks. A model's written rationale is itself a claim. It can help a reviewer understand a decision, but it is not privileged evidence of the mechanism that produced the decision.

### Workflow patterns: how work is arranged

| Pattern | Working idea | Evidence point or gate |
|---|---|---|
| Prompt chaining | Pass an intermediate result through a fixed sequence. | Validate the intermediate artifact before a later stage treats it as fact. |
| Routing | Select a specialized path for a task. | Record the routing basis; include an uncertain or unsupported route rather than forcing every input into a confident category. |
| Parallelization | Execute independent subtasks concurrently. | Verify independence, common input versions, and the rule for resolving conflicting results. |
| Orchestrator-workers | Decompose a task dynamically and assign bounded work. | Check each worker's scope, evidence, and returned artifact before accepting the combined result. |
| Evaluator-optimizer | Generate, evaluate, revise, and repeat. | Fix the criterion and budget; make rejection possible without allowing the producer to redefine success. |

A fixed chain may not be agentic in the narrow sense of dynamically choosing actions. It can still contain model calls and still require validation. Conversely, an adaptive agent can use a fixed chain as one tool. Naming the pattern does not settle what authority the system should have.

### Checking patterns: why a repetition counts as progress

The ten families below organize the 85 catalog entries by the kind of check they rely on. The examples are applications, not claims of measured effectiveness.

| Checking pattern | Evidence to gather | Gate and characteristic failure |
|---|---|---|
| Measure, change one thing, keep it only if better | Baseline, version, fixed measurement conditions, new result, and guardrails. | Keep a change only when its improvement is meaningful and required behavior remains intact. A moving benchmark or a sacrificed guardrail can create a false win. |
| Burn down a worklist | Initial findings, stable scan scope, each repair, and a comparable rescan. | Accept removal only when the underlying problem is resolved. Suppressing a warning is not the same as fixing it. |
| Change with proof | Reproduced failure or explicit contract, minimal diff, and relevant tests. | Advance the exact candidate supported by the checks. A passing unrelated test is not proof of the requested change. |
| Maker is not the checker | Independent review criteria, source artifacts, objections, and resolution evidence. | Do not accept agreement alone. Different sessions or vendors can still share blind spots and sources. |
| Evidence ledger | Each claim, source, contradiction, scope, and unresolved question. | Block or narrow claims without adequate support. A citation's existence does not establish that it supports the sentence. |
| Replay until clean | Clean starting state, complete scenario, failures, repairs, and fresh replay. | Require the stated scenario to pass without hidden residue. A replay that reuses repaired state may conceal a broken installation or migration. |
| Plan before building | Requirements, assumptions, alternatives, dependencies, and acceptance criteria. | Resolve consequential ambiguity before execution. A detailed plan can still be a plan for the wrong task. |
| Standing watch | Fresh observation time, current authority, last completed action, and changed conditions. | Act only when the trigger and permission still apply. Stale state or an unsafe rerun can repeat a completed action. |
| Audit, gate and handoff | Exact version, verdict, failed checks, unresolved evidence, and restart instructions. | Stop at the authorized boundary. An audit does not silently become permission to deploy or delete. |
| Controlled experiment | Fixed protocol, conditions, repeated observations, and deviations. | Preserve the protocol and report uncertainty. A selected successful run does not establish general reliability. |

One task can combine several families. An agent can plan an accessibility repair, burn down a worklist, submit the result to a different reviewer, and finish with an audit gate. Adding four pattern names does not give four independent guarantees. If every check relies on the same flawed scanner, the apparent layers share one failure mode.

## Where to gather evidence

Draw the boundaries at which information changes status: a request becomes a plan; a plan becomes a tool call; a response becomes a claim; a claim becomes permission to continue.

**At intake**, preserve the user's requested outcome, constraints, authorized targets, and explicit exclusions. Ask what observation would count as completion. “Improve the website” is not a sufficient acceptance condition.

**Before a tool call**, record the intended operation, target, relevant parameters, and authority. A permission check must bind to this action, not to a vague earlier approval. A revised target, expanded scope, or materially changed consequence may require a new decision.

**After a tool call**, distinguish transport success, application success, and the actual postcondition. An HTTP success response can mean that a job was queued. Check its eventual state if completion matters. Preserve error and timeout outcomes rather than letting the narrative overwrite them.

**At a handoff**, carry the source version, scope, evidence references, unresolved issues, and what the next worker is allowed to do. A summary is useful but can lose a critical qualification. The receiving worker should be able to inspect the underlying artifact.

**At acceptance**, test the exact candidate against criteria set before seeing its result. Record failures as well as passes. Confirm that the final artifact or external state is the one evaluated, not an earlier draft.

**After release**, gather evidence that the assumptions still hold: failures, drift, user confusion, repeated interventions, and unexpected side effects. Monitoring is useful only if a finding can lead to a bounded response. It should not be an unbounded license for an agent to repair production however it chooses.

A trace is an instrument, not a confession. Log enough to answer the operational question while minimizing personal data, credentials, and sensitive content. Protect evidence from unauthorized modification, record timestamps and versions, and make retention proportional to the need. More logging is not automatically more useful observability.

### Observability is not evaluation

Observability helps us reconstruct what the running system did. A trace can connect a task to its model calls, retrieved inputs, tool requests, returned errors, and child tasks. Evaluation applies a criterion to that behavior or its result. A complete trace can document a failure beautifully; its completeness does not turn the failure into a success. Conversely, an evaluation score without a usable trace can conceal why the failure happened.

Inspect at several levels. A model may produce a well-formed tool request while the agent selects the wrong tool. Every tool call may complete while the system fails the user's task. A task may complete while violating a permission or creating an unacceptable cost. Keep these separate judgments visible. Production observations can become new evaluation cases, but avoid quietly changing a historical benchmark whenever a new failure appears: retain its version and add a separately identified test.

### Checkpoints are memory, not renewed permission

A checkpoint saves enough state to resume a process. It does not establish that the outside world is unchanged. A resumed agent may hold an old approval, a stale inventory, or an action whose response was lost after execution. Before crossing a consequential boundary after restart, reconcile the external state and recheck authority for the proposed action. Test this deliberately by interrupting a safe fixture between execution and receipt of its result. If the resumed system blindly repeats the operation, the checkpoint preserved progress in the program but not correctness in the world.

## A gate must have a consequence

A warning that the system ignores is not a gate. Specify a gate using five parts:

- **Condition:** the observable facts required to pass.
- **Evidence:** where those facts come from and which version they describe.
- **Decision owner:** code, a qualified reviewer, or both.
- **Allowed transition:** exactly what passing permits.
- **Failure behavior:** stop, gather more evidence, revise within scope, or escalate.

For example: “The proposed repository change may enter review only if the fixed regression tests pass on the candidate commit, no forbidden files changed, and the reviewer can inspect the diff. Failure returns the change to a bounded local revision. Passing does not authorize a production deployment.”

An automated gate is appropriate for many exact checks: schema validation, allowlists, bounded resource use, or whether a test failed. Human review is important where the decision depends on purpose, consequences, or unresolved judgment. Human presence alone is not a guarantee. A rushed reviewer with an unreadable approval screen can become a rubber stamp. Show the proposed action, relevant evidence, uncertainty, and a real option to refuse.

Place permission gates before irreversible or externally consequential actions. Place postcondition checks after execution. One does not replace the other: authorization does not prove success, and a successful action does not retroactively authorize it.

## Worked case: the green scanner and the broken form

The following trace is an invented fixture. It illustrates how to inspect a loop; no performance results are claimed.

**Task:** repair three confirmed accessibility barriers in a local ticket form. Do not publish the page. Preserve its content and existing submission behavior. The permitted edits are limited to the form and its styles.

**Before the run:** save the baseline page, scanner configuration, and tests. Record three acceptance checks: every input has an accessible name, the error message is associated with the invalid field, and a keyboard user can reach and activate Submit without becoming trapped. Automated scanning covers only part of this contract. A keyboard interaction check is also required.

| Step | Observation or action | Evidence-based decision |
|---|---|---|
| Baseline | Scanner identifies missing labels; keyboard test finds a focus trap. | Record distinct failures. Do not assume the scanner has exhausted the problem space. |
| First proposal | Agent adds labels but disables the failing rule in the scanner configuration. | Scope gate rejects the configuration change. The agent cannot redefine its test to claim success. |
| Revision | Agent restores the rule and patches the form. | Inspect the diff and run the unchanged checks on that candidate. |
| Tool result | Scanner reports no findings; keyboard test still fails. | Task is not complete. Preserve both results rather than averaging them into a green verdict. |
| Bounded repair | Agent changes focus handling within the authorized files. | Repeat the full interaction from a clean page state and rerun regression checks. |
| Final review | Required checks pass on the candidate; reviewer records remaining untested screen-reader combinations. | Accept the bounded repair for review. Do not claim universal accessibility or publish the page. |

The loop combines a worklist, change with proof, replay, and a handoff gate. Its value lies in the checks, not the labels. A useful final report would say what passed, on which version, under which conditions, what remains untested, and which action was deliberately not taken.

Now change one detail: the agent has permission to publish. That does not remove the need for a pre-publication gate and a post-publication check. The deployed page may differ from the local candidate. The evidence chain must reach the state people will actually use.

## Budgets, retries, and honest endings

Set limits before the run: elapsed time, tool calls, spending, permitted files, attempted revisions, and a rule for lack of progress. The limits should match the task, not an arbitrary promise of autonomy. A failed test at the budget limit means incomplete work, not permission to lower the test's threshold.

Retries need their own analysis. Repeating a read is often harmless; repeating a payment, message, or record creation may duplicate an effect. After a timeout, first determine whether the earlier action took effect. Use service-supported idempotency keys or stable operation identifiers where available. A bounded retry policy should distinguish a known non-executed attempt from an uncertain outcome.

Use explicit terminal states such as:

- **Accepted:** the stated criteria passed for the verified result.
- **Blocked:** authority, access, or an essential dependency is missing.
- **Inconclusive:** evidence cannot yet establish the result.
- **Budget exhausted:** work stopped before acceptance.
- **Canceled:** the authorized work was stopped by instruction.

These are not grades. They are information the next decision depends on. A safely blocked action can be correct behavior even though the user's broader goal remains unfinished.

## How to evaluate the loop rather than admire the demo

Test more than a happy path. Introduce a stale input, a failed tool, a contradictory observation, an ambiguous timeout, a forbidden action, and an evaluator that returns “unknown.” Predict the system's response before running the fixture. Record whether it actually stopped or narrowed its claim.

Measure both completion and restraint. Useful quantities include task acceptance on a defined test set, prohibited-action attempts, incorrect success reports, failed postconditions, unnecessary escalations, cost, and time. A system that never acts can score well on prevented harm while being useless; a system that always continues can score well on throughput while exceeding its authority. Report the tradeoff instead of hiding one side.

Separate development cases from held-out evaluation cases. Repeatedly changing a prompt against the same cases can teach the system to satisfy that set without improving elsewhere. Keep the evaluator and its configuration versioned. Where judgments are subjective, use a stated rubric, assess reviewer disagreement, and inspect examples rather than presenting a score as a universal truth.

## Practice across the three tracks

All three tracks inspect the same loop and share the same standard of evidence. Their artifacts differ.

**Human-Centered AI and Transparency:** design a supervision screen showing current task, authorized scope, pending action, evidence, uncertainty, and stop controls. Test whether a person can distinguish “request accepted” from “task completed” and identify why a gate failed. A beautiful trace is not enough if the relevant distinction is invisible.

**Statistical and Causal Validation:** compare two checking strategies on a fixed set of safe fixtures. Define the outcome and sampling procedure before the runs. Report variation, failure categories, and limitations. If claiming that a gate caused an improvement, justify the comparison and control changes that could explain the result.

**Agentic Engineering and Reliability:** implement the controller's state transitions, scope checks, retry behavior, and evidence records. Demonstrate that an injected failure cannot fall through to an accepted state. Test restart behavior as well as uninterrupted execution.

## Casebook exercise: instrument one boundary

Choose a sandboxed agent you can inspect, or a documented system for which you can clearly distinguish documented behavior from behavior you have tested. Do not seek production access merely to make the exercise look realistic.

Produce a one-page loop map. Mark the model, controller, tools, observations, state changes, evaluator, and human intervention points. Select one boundary where an incorrect claim could become an action. Write an acceptance rule and a refusal rule for that boundary. Before running, predict what will happen under a normal input and a deliberately misleading or incomplete input.

Your evidence record should contain:

- The request, scope, source versions, and predicted result.
- The proposed action and the gate decision.
- The actual tool result or an explicit statement that execution did not occur.
- A postcondition check independent of the agent's final report where feasible.
- A comparison between the prediction and observation.
- The limits of what this evidence establishes.

If you use AI to help, give it this bounded instruction:

```text
Help me map this agentic workflow and design one falsifiable check.
Do not execute actions, change permissions, or contact external services.
Separate known facts, assumptions, and observations we still need.
Name the exact state transition the gate controls, its evidence source,
and what should happen if evidence is absent or contradictory.
Propose a safe fixture that could demonstrate a failure of the gate.
Do not report a proposed or simulated test as an executed test.
```

Discuss the following questions with another student:

- How could the agent satisfy the metric while failing the user's purpose?
- Which checks share the same source or assumption and therefore are not independent?
- What must be rechecked if the candidate changes after approval?
- Which failure should stop execution, and which permits a bounded repair?
- What evidence would make you revise your own judgment of the loop?

## Bridge to the Skeptic's Toolkit

A loop map tells us where to look. The toolkit tells us how to question what we find. It asks what could falsify a claim, when past performance no longer transfers, and whether we have confused an artifact with the world it represents. Those questions are not an extra review after engineering. They shape the engineering of every observation, check, and gate.

The aim is not to watch an agent's every token. It is to understand enough of the system's behavior to know what it is allowed to do, what evidence it must produce, and what happens when that evidence is not good enough.

## Sources and scope

This chapter synthesizes the local companion materials in `agentic-best-practices/`: `loop-tree.md` (10 checking patterns, 85 catalog entries), `loops-at-a-glance.md` (catalog summaries and stated limitations), `primer.md` (model, controller, tools, and task completion), and `decks/00 - Decks and examples.html` (five reasoning, five workflow, and ten checking-pattern deck pairs). The worked form example and exercise are teaching constructions, not executed studies. The companion's grouping is an editorial judgment, not a universal taxonomy or empirical ranking.

For the original named reasoning and workflow approaches, see Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models* (2022), https://arxiv.org/abs/2210.03629; Xu et al., *ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models* (2023), https://arxiv.org/abs/2305.18323; Yao et al., *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* (2023), https://arxiv.org/abs/2305.10601; and Anthropic, *Building effective agents* (2024), https://www.anthropic.com/research/building-effective-agents. These sources introduce approaches in particular settings; their results do not establish the reliability of a student's deployment.

### Further reading from the course pantry

The instructor-supplied pantry also informed the distinctions above: Sam Bhagwat, *Principles of Building AI Agents*, second edition, section “Observability and Tracing”; Akshay Pachaar and Avi Chawla, *AI Engineering: System Design Patterns for LLMs, RAG and Agents* (2025), “Evaluation vs Observability”; Carmelo Iaria, *The Agentic Architect Playbook*, evaluation layers and human-in-the-loop design; and Anjanava Biswas and Wrick Talukdar, *Building Agentic AI Systems* (Packt, 2025), the chapter on tool use and planning, including graph state and checkpointing. These readings provide implementation perspectives, not evidence that tracing, checkpoints, or a framework automatically ensure reliability. This chapter uses original explanations and examples; it does not reproduce those texts or require students to redistribute pantry copies.
