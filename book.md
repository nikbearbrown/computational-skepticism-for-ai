# Computational Skepticism for AI

*Course textbook · 13 chapters · Masters engineering audience*

---

## One-sentence description

A masters-level engineering textbook on the supervisory and validation capacities required to catch the AI failure that does not announce itself — the plausible answer to the wrong question, the statistically valid output on a causally incoherent claim — built around Pearl's three-rung ladder of causal reasoning, the Five Supervisory Capacities, and a longitudinal red-team casebook the student builds across all 13 chapters, anchored to a recurring model case (Shapira et al., *Agents of Chaos*, 2026, Case #1).

## Audience

Masters engineering students. Mixed subfield (CS, data science, mechanical, EE, interdisciplinary). Probability priors and ML priors vary widely. The book treats this variance as a design constraint: Chapter 2 contains a calibration on-ramp; depth in Chs. 2, 5, and 8 is calibrated for the broadest target, with explicit "skip if you've taken graduate probability" callouts where appropriate.

Open question logged: which engineering subfields are dominant in target adoption? Affects Chs. 2, 5, 8 depth calibration.

## Scope

In: the methodology of computational skepticism applied to AI systems — calibration, bias, data validation, explainability, fairness, robustness, agentic AI validation, delegation, communication, accountability, and the limits of the technical. The Five Supervisory Capacities, Pearl's Ladder (rungs 1–3 across the arc), the Frictional method as a general AI-era pedagogy contribution, and a six-tool ecosystem (Frictional, Gru, CRITIQ, Brutalist, Glimmer, Botspeak) used operationally throughout.

Out: the design of agentic systems (referred to companion volume *Design of Agentic Systems with Case Studies*); deep ML internals beyond what validation requires; pure ethics as separate from validation practice.

## Prerequisites

One graduate-level probability course or equivalent self-study. Comfort reading code in Python. Willingness to predict before observing. No prior philosophy required; the philosophical apparatus is introduced as engineering instruments.

## Voice notes (book-specific)

- **Register: the "Teardown" voice** — Feynman machinery-from-first-principles × design-critic trade-off analysis. Mechanism visible; every mechanism is built up from parts, and every design choice is named with the trade-off it makes. Jargon translated or cut. The voice of someone working through the validation as the reader watches, not lecturing on a settled body of knowledge. First-person, direct, willing to say "I do not yet understand."
- **The reader is supervising AI, not just using it.** Every chapter assumes the reader will deploy AI tools in the course. The chapter teaches the supervision, not the use.
- **First person used to label position-taking.** "I conclude," "my reading is," "I do not yet understand."
- **"You" used to invite the reader to predict, calculate, and test.** Prediction-lock before observation is structural to the method.
- **"We" used when figuring something out together** — particularly in the deep-dive sections.
- **Pearl's Ladder is the spine.** The ladder is sketched and Rung 3 (the counterfactual) is *opened* in Ch. 4 (robustness); Rungs 1 and 2 are developed in detail in Ch. 6 (bias); Rung 3 is *closed* in Ch. 12 (accountability), via the governance counterfactual. Each return is explicit. (Post-renumber mapping — the old Ch3/6/8/13 mapping is stale.)
- **The longitudinal Pebble is the student's own red-team casebook.** Across all 13 chapters, the LLM Exercises build one casebook on an agent the student chooses in Ch. 1 (see CASEBOOK-CHAIN.md). The recurring *model* case is Ash / *Agents of Chaos* Case #1 (the email-server reset), introduced in Ch. 1 and returning where it earns real work: Ch. 5 (explanation), Ch. 8 (its home ground, agentic failure), and Ch. 12 (accountability). Ash anchors the method; the Pebble the reader builds is their own.
- **The forbidden phrases list from CLAUDE.md applies in full.** "Stakeholders" gets cut. "Robust" without qualification gets cut. Engineers use "robust" loosely; this book uses it precisely.

## Structural elements per chapter

Every chapter, in this order:

1. **Narrative opening (cold open) — always first.** The chapter opens in a scene, a concrete failure, or a sharp specific puzzle. NEVER open with bullets, a TL;DR, a learning-objectives list, or a prerequisites block. The reader should be inside a problem by the second sentence. (No TL;DR at all — the cold open does that job. No "two suggested titles." Both were removed 2026-07.)
2. **Prose overview after the cold open.** What the chapter does, what the reader will be able to do by the end, and prerequisites — all written as flowing prose, not lists. Objectives-as-bullets are banned from the chapter opening.
3. Hits all four Teardown moves (hook → unfold the mechanism from first principles → deep-dive on one key mechanism → synthesize and name the trade-off).
4. Includes worked Glimmer exercise(s) with prediction-lock structure.
5. A BUILD/AUDIT pairing, merged into the graduated exercise set (Warm-up → Challenge).
6. LLM Exercise advancing the running casebook (the Pebble). See CASEBOOK-CHAIN.md for the dependency graph.
7. Where it fits: a closing bridge to the actual next chapter (the final chapter closes the book instead).
8. Tags: 5 discoverability tags.

The end-of-chapter apparatus (items 4–8) is separable and read *after* the prose spine; it is not counted in the 4,500–6,000 prose target.

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

Target: **4,500–6,000 words of teaching prose per chapter**, NOT counting the end-of-chapter apparatus (exercises, Glimmers, LLM Exercise, figure prompts), which is separable and meant to be worked *after* the chapter is read. Apparatus typically adds another ~2,000–4,000 words. A finished chapter file therefore lands roughly 6,500–10,000 words, of which the prose spine is 4,500–6,000.

Book body: ~58,000–78,000 words of prose across the 13 chapters; ~90,000–120,000 total with apparatus. Front matter (preface) and the author's-note introduction are separate.

Rationale for the revision (was 2,500–3,500): the old target produced chapters much too short to build a mechanism from first principles, carry a worked example, and land a trade-off — the Teardown moves need room. Prose under ~4,500 words is a warning sign the chapter is asserting rather than deriving; prose over ~6,000 usually means two expositions of the same idea are fighting (the ROUGH MERGE artifact — cut to the Teardown version, don't trim evenly).

## Voice ground truth

Both root `style/` and `books/computational-skepticism-for-ai/style/` are empty as of first drafts. Drafts flagged `voice-unanchored`. The first chapter sets the voice — calibrate Chapter 1 deliberately.
