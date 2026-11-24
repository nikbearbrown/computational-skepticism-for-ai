# Computational Skepticism for AI

A practical textbook from **Humanitarians AI Incorporated** on checking AI before people rely on it. Start with the claim, reconstruct what the evidence can support, test what could go wrong, and decide what needs human review.

This is the public working manuscript (2026 edition), not a finished release or a certification standard. You can read the chapters directly on GitHub. Reuse remains subject to the [book license](LICENSE.md).

## Read the book

- [Front matter](chapters/00-frontmatter.md)
- [Introduction](chapters/00-introduction.md)

### Before delegating

- [Agents: Understanding Before Delegating](chapters/00a-agents-understanding-before-delegating.md)
- [Agentic Loops: Where Evidence Enters and Action Stops](chapters/00b-agentic-loops.md)

### Foundations

- [Chapter 1 — The Skeptic's Toolkit](chapters/01-the-skeptics-toolkit.md): Turn a confident output into specific claims you can test.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/02-probability-uncertainty-and-the-confidence-illusion.md): Calibrate confidence and distinguish evidence from a guess.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md): Check provenance, missing data, definitions and denominators.

### Model behavior and equity

- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md): Test whether evidence carries over when inputs change.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md): Check whether an explanation supports the decision it accompanies.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/06-bias-where-it-enters-and-who-is-responsible.md): Trace where unfairness can enter a pipeline.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md): Choose and justify an equity measure, including its denominator.

### Agents, supervision and communication

- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md): Distinguish a tool result or a reported success from a verified outcome.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/09-delegation-trust-and-the-supervisory-role.md): Define who can act, what a human must check and when to stop.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md): Check whether a graphic supports the inference it invites.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md): Write claims that match the evidence and state what is unknown.

### Accountability and limits

- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/12-accountability-who-is-responsible-when-the-system-fails.md): Assign a person to each consequential decision and escalation.
- [<!-- CHAPTERIZED 2026-07-02: TL;DR removed, exercises merged, bridges/prereqs updated to 13-chapter order. Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved. -->](chapters/13-the-limits-of-ai-what-the-tools-cannot-do.md): Recognize when the system is not suited to the task.

- [Back matter](chapters/99-back-matter.md)

## For readers evaluating an AI pilot

Start with [the toolkit](chapters/01-the-skeptics-toolkit.md) and [data validation](chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md). Use [bias](chapters/06-bias-where-it-enters-and-who-is-responsible.md) and [fairness metrics](chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md) to choose what to compare, then use [delegation](chapters/09-delegation-trust-and-the-supervisory-role.md) and [accountability](chapters/12-accountability-who-is-responsible-when-the-system-fails.md) to keep approval with a named human. These chapters provide methods and teaching examples; they do not show that any specific pilot has passed.
