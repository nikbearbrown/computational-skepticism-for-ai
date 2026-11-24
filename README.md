# Computational Skepticism for AI

## About the book

A practical textbook from **Humanitarians AI Incorporated** on checking AI before people rely on it. Start with the claim, reconstruct what the evidence can support, test what could go wrong, and decide what needs human review.

This is the public working manuscript (2026 edition), not a finished release or a certification standard. You can read the chapters directly on GitHub. Reuse remains subject to the [book license](LICENSE.md).

For students, educators, and practitioners who need to evaluate whether an AI-assisted result is ready to use.

## Learning outcomes

- Turn a model output into testable claims and check the provenance and limits of its evidence.
- Test robustness and compare fairness measures using explicit definitions and denominators.
- Design human review and stop rules for an agent workflow, then communicate the uncertainty that remains.

## Read the book

- [Front matter](chapters/00-frontmatter.md)
- [Introduction](chapters/00-introduction.md)

### Before delegating

- [Agents: Understanding Before Delegating](chapters/00a-agents-understanding-before-delegating.md)
- [Agentic Loops: Where Evidence Enters and Action Stops](chapters/00b-agentic-loops.md)

### Foundations

1. [The Skeptic's Toolkit](chapters/01-the-skeptics-toolkit.md): Turn a confident output into specific claims you can test.
2. [Probability, Uncertainty, and the Confidence Illusion](chapters/02-probability-uncertainty-and-the-confidence-illusion.md): Calibrate confidence and distinguish evidence from a guess.
3. [Data Validation: Reconstructing the Epistemic Frame Behind a Dataset](chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md): Check provenance, missing data, definitions and denominators.

### Model behavior and equity

4. [Robustness: What "Understanding" Means When a Pixel Can Break the Model](chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md): Test whether evidence carries over when inputs change.
5. [Model Explainability: Distinguishing Explanation from the Appearance of Explanation](chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md): Check whether an explanation supports the decision it accompanies.
6. [Bias: Where It Enters and Who Is Responsible](chapters/06-bias-where-it-enters-and-who-is-responsible.md): Trace where unfairness can enter a pipeline.
7. [Fairness Metrics: Choosing a Definition and Defending It](chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md): Choose and justify an equity measure, including its denominator.

### Agents, supervision and communication

8. [Validating Agentic AI: When Autonomous Systems Misbehave](chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md): Distinguish a tool result or a reported success from a verified outcome.
9. [Delegation, Trust, and the Supervisory Role](chapters/09-delegation-trust-and-the-supervisory-role.md): Define who can act, what a human must check and when to stop.
10. [Visualization Under Validation: Honest, Misleading, and the Choices Between](chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md): Check whether a graphic supports the inference it invites.
11. [Communicating Uncertainty: Calibrating Claims to Evidence](chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md): Write claims that match the evidence and state what is unknown.

### Accountability and limits

12. [Accountability: Who Is Responsible When the System Fails?](chapters/12-accountability-who-is-responsible-when-the-system-fails.md): Assign a person to each consequential decision and escalation.
13. [The Limits of AI: What the Tools Cannot Do](chapters/13-the-limits-of-ai-what-the-tools-cannot-do.md): Recognize when the system is not suited to the task.

## Resources

- [Fundamental themes](chapters/97-fundamental-themes.md)
- [Back matter](chapters/99-back-matter.md)

### Evaluating an AI pilot

Start with [the toolkit](chapters/01-the-skeptics-toolkit.md) and [data validation](chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md). Use [bias](chapters/06-bias-where-it-enters-and-who-is-responsible.md) and [fairness metrics](chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md) to choose what to compare, then use [delegation](chapters/09-delegation-trust-and-the-supervisory-role.md) and [accountability](chapters/12-accountability-who-is-responsible-when-the-system-fails.md) to keep approval with a named human. These chapters provide methods and teaching examples; they do not show that any specific pilot has passed.

To apply the book to an evaluation packet, use the separate [Computational Skepticism audit skill](https://github.com/nikbearbrown/computational-skepticism-skill).
