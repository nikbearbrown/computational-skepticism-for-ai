# Computational Skepticism for AI

*Course textbook · 14 chapters · Masters engineering audience*

---

## One-sentence description

A masters-level engineering textbook on the supervisory and validation capacities required to catch the AI failure that does not announce itself — the plausible answer to the wrong question, the statistically valid output on a causally incoherent claim — built around Pearl's three-rung ladder of causal reasoning, the Five Supervisory Capacities, and a longitudinal validation case (Shapira et al., *Agents of Chaos*, 2026) threaded through eight chapters.

## Audience

Masters engineering students. Mixed subfield (CS, data science, mechanical, EE, interdisciplinary). Probability priors and ML priors vary widely. The book treats this variance as a design constraint: Chapter 2 contains a calibration on-ramp; depth in Chs. 2, 5, and 8 is calibrated for the broadest target, with explicit "skip if you've taken graduate probability" callouts where appropriate.

Open question logged: which engineering subfields are dominant in target adoption? Affects Chs. 2, 5, 8 depth calibration.

## Scope

In: the methodology of computational skepticism applied to AI systems — calibration, bias, data validation, explainability, fairness, robustness, agentic AI validation, delegation, communication, accountability, and the limits of the technical. The Five Supervisory Capacities, Pearl's Ladder (rungs 1–3 across the arc), the Frictional method as a general AI-era pedagogy contribution, and a six-tool ecosystem (Frictional, Gru, CRITIQ, Brutalist, Glimmer, Botspeak) used operationally throughout.

Out: the design of agentic systems (referred to companion volume *Design of Agentic Systems with Case Studies*); deep ML internals beyond what validation requires; pure ethics as separate from validation practice.

## Prerequisites

One graduate-level probability course or equivalent self-study. Comfort reading code in Python. Willingness to predict before observing. No prior philosophy required; the philosophical apparatus is introduced as engineering instruments.

## Voice notes (book-specific)

- **Register:** Feynman-flavored engineering pedagogy. Mechanism visible. Jargon translated or cut. The voice of someone working through the validation as the reader watches, not lecturing on a settled body of knowledge.
- **The reader is supervising AI, not just using it.** Every chapter assumes the reader will deploy AI tools in the course. The chapter teaches the supervision, not the use.
- **First person used to label position-taking.** "I conclude," "my reading is," "I do not yet understand."
- **"You" used to invite the reader to predict, calculate, and test.** Prediction-lock before observation is structural to the method.
- **"We" used when figuring something out together** — particularly in the deep-dive sections.
- **Pearl's Ladder is the spine.** Rung 1 introduced in Ch. 3. Rung 2 in Ch. 6. Rung 3 opened in Ch. 8 and closed in Ch. 13. Each return is explicit.
- **The longitudinal Pebble** is *Agents of Chaos* Case #1 (Ash's email server reset). Introduced in Ch. 1, returned to in Chs. 5, 6, 7, 8, 9, 10. Each return adds a new validation lens.
- **The forbidden phrases list from CLAUDE.md applies in full.** "Stakeholders" gets cut. "Robust" without qualification gets cut. Engineers use "robust" loosely; this book uses it precisely.

## Structural elements per chapter

Every chapter:

1. Opens in scene or sharp specific puzzle.
2. Two suggested titles at the top.
3. TL;DR (2 sentences) before the hook.
4. Hits all four moves (hook, unfold, deep-dive, synthesize).
5. Includes worked Glimmer exercise(s) with prediction-lock structure.
6. Closes with "What would change my mind" + "Still puzzling."
7. Tags: 5 discoverability tags.

## Spine source

*Agents of Chaos: Eleven Red-Team Studies of Agentic Failure* (Shapira et al., 2026). The book treats this as the longitudinal case material — the Pebble. Specific case recurrences are mapped in the TOC.

Aging risk noted: tools cited in the paper (OpenClaw, specific model versions) will obsolete within 2–3 years. The cases and the failure-mode taxonomy will not. Frame chapter prose around failure structure, not tools.

## Six-tool ecosystem

The book is accompanied by six tools, all running inside Claude as Claude Projects:

- **Frictional** — the learning journal. Prediction-lock, reflection, gap analysis.
- **Gru** — software design document consultant. Boondoggle Score, delegation maps.
- **CRITIQ** — peer review and paper development.
- **Brutalist** — instructional design engine for living presentations.
- **Glimmer Exercise Tool** — designs and evaluates exercises against the anti-substitution requirement.
- **Botspeak** — the conceptual framework (Nine Pillars) the other five instantiate.

Tools are referenced in chapter prose; the chapter teaches the supervision, not the tool's UI.

## Hero image direction

Diagnostic, not decorative. Calibration curves, causal DAGs, adversarial perturbation pairs, dashboards in two registers (honest/misleading), agent failure case schematics. Avoid stylized AI iconography (glowing networks, humanoid robots).

## Approximate length

Target: 2,500–3,500 words per chapter for rough drafts. 35,000–50,000 words for the book body. Front matter (preface) is separate.

## Voice ground truth

Both root `style/` and `books/computational-skepticism-for-ai/style/` are empty as of first drafts. Drafts flagged `voice-unanchored`. The first chapter sets the voice — calibrate Chapter 1 deliberately.
