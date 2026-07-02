# Reframe — Skepticism for Building Things *with* AI (hands-on)

*A direction proposal, not an edit. Recasts the book so the reader is the builder, the
Five Supervisory Capacities are the spine, chapters are domain-plural, and every chapter
ends in a build the reader made and a failure they caught. Worked examples come from the
ecosystem that already runs this thesis: madison, mycroft, the-reallocation-engine, Gru,
SNICKERDOODLE.*

---

## The reframe in one line

The subject shifts from *"be skeptical of AI systems"* (abstract, third-person) to
**"be skeptical of what *you* build with AI"** (concrete, second-person, hands-on). Same
spine, same four moves, same five capacities — but the reader is now conducting the build,
and the thing they learn to distrust is their own fluent, confident, AI-generated artifact.

Working subtitle: **Validating What You Build with AI.**

## Why this is the right reframe (and branding wasn't)

- **It keeps the book's hard lesson.** The point was never "ads lie." It was *"the system
  succeeded, a patient was dead"* — sincere, valid output that is wrong about the question
  that matters. When you build with AI you generate exactly that on purpose, all day. The
  reader meets the failure in their own hands.
- **It fixes the floating-chapters finding.** Every editor note flagged that chapters don't
  anchor to the spine. Make the **Five Supervisory Capacities** the connective tissue: each
  chapter *is* one capacity, exercised on a real build. Ch.1 already names them; Gru already
  operationalizes them; Snickerdoodle P1 already enforces them.
- **It unifies the ecosystem instead of colonizing one book.** madison stays the branding
  book; this becomes the *builder's* book for which madison/Gru/Snickerdoodle are worked
  cases. Domain-plural, so no chapter wears a costume.

## The spine (state it once, in Ch.1, then never re-explain)

The **solve–verify asymmetry**: AI solves faster than any human and that gap won't close;
what stays human is verification. Verification decomposes into **five capacities** —

- **[PA] Plausibility Auditing** — hearing the wrong note *before* you verify.
- **[PF] Problem Formulation** — deciding what the mission is before the AI sees it.
- **[TO] Tool Orchestration** — which AI task, in what order, with what trust.
- **[IJ] Interpretive Judgment** — supplying meaning and accountability the AI can't.
- **[EI] Executive Integration** — holding all four toward one goal you sign for.

Plus the two hazards: the **Fluency Trap** (well-formed output read as evidence) and the
**Provenance rule** (no number exists that no record produced).

## Chapter map — capacity · ecosystem example · the hands-on build

Every chapter follows one pattern: **you solve with AI → it hands you a confident artifact
→ you apply the chapter's move to catch where it's wrong → you produce the human decision.**

| Ch | Title (current) | Lead capacity | Ecosystem example (homologous) | Hands-on build (what the reader does) |
|----|----|----|----|----|
| 1 | The Skeptic's Toolkit | all five | **Gru** boondoggle score + **the-reallocation-engine** (the reallocation principle: execution→judgment) | Run one real AI task; apply the four moves; name which capacity catches the failure. |
| 2 | Probability & the Confidence Illusion | **PA** | madison competitor-scan confidence scores | Make an AI emit confident probabilities; run a calibration + base-rate check; catch the decorative number. |
| 3 | Bias: Where It Enters, Who's Responsible | **IJ** | madison persona / claims-and-proof | Run a persona-synthesis build; find where bias enters (data / framing / deployment); assign the accountable owner. |
| ~~4~~ | ~~The Frictional Method~~ **— CUT** | — | — | **Move to `friction-measuring-the-learning-struggle`.** Different subject (assessment of *human* learning, not validating a built artifact); it was the manuscript's one **Weak** chapter; its transferable kernel ("a working artifact is not evidence the judgment happened") is already the spine (fluency trap + solve–verify asymmetry). Book tightens 14 → 13. |
| 5 | Data Validation | **PA + PF** | madison `data/raw → data/verified` + DATA_CONTRACT | Take a dataset the AI hands you; reconstruct the epistemic frame that produced it; catch the join/aggregation failure before it enters `verified/`. |
| 6 | Model Explainability | **IJ** | Gru's build rationale / madison claims-and-proof | Get an AI to "explain" a decision; test whether the explanation is about the model or the world; reject the appearance of explanation. |
| 7 | Fairness Metrics | **PF + IJ** | madison two-customers / message across audiences (+ keep COMPAS) | Choose a fairness definition for a real campaign or model and *defend the choice* as a values claim you sign. |
| 8 | Robustness | **PA** | **mycroft / Snickerdoodle** schema-drift → silent-mode revoked | Perturb one field in a working recipe/prompt; watch the confident pipeline break; locate the fragility. |
| 9 | Validating Agentic AI | **TO + EI** | **mycroft** agent recipes (the email-agent case) | Run an agent through a task; catch where it reports success but the world didn't change; write the stop condition that would have caught it. |
| 10 | Delegation, Trust, Supervisory Role | **TO (all five)** | **Gru `/claude`** — the Boondoggle Score | Produce a real Boondoggle Score: assign each step to AI or human, name each human capacity, write the handoff condition between every step. |
| 11 | Visualization Under Validation | **IJ + PA** | madison campaign-performance report + d3 | Have AI generate a chart from real data; catch the misleading axis/encoding; rebuild it honest. |
| 12 | Communicating Uncertainty | **IJ** | madison warranted-verbs / claims-and-proof map | Take an AI's claim; downgrade the verb to what the evidence warrants ("shows" → "suggests"); map every claim to its proof. |
| 13 | Accountability | **IJ + EI** | **SNICKERDOODLE** phase-gate attestation | Write a real attestation record for a build — who cleared which gate, what was tested, what was *not* tested (the mandatory honest list). |
| 14 | The Limits of AI | **EI** | the **Irreducibly Human** frame (Gru's curriculum) | In one of your own builds, find the single decision that is irreducibly human, and say why capability scaling won't reach it. |

Chapters 5, 10, 12, and 13 are the strongest hands-on anchors because the ecosystem gives
the reader a *real artifact to produce* (a verified dataset, a boondoggle score, a
claims-and-proof map, an attestation). Consider opening the book's Part II on Chapter 10 —
the boondoggle score is the most tangible single thing a reader can make.

## The hands-on chapter pattern (the "more hands-on" ask, made concrete)

Replace each chapter's abstract-first opening with a build-first one. The template:

1. **The task.** "You need [X]. You ask the AI. In thirty seconds you have [fluent artifact]."
2. **The trap.** The artifact is confident and *looks* done. Name what it doesn't announce
   (which claim is sourced, which step failed, who's accountable).
3. **The move.** Apply the chapter's capacity + one of the four skeptical moves to *this*
   artifact. Show the wrong note.
4. **The gate.** Produce the human decision — a handoff condition, an attestation row, a
   downgraded verb, a rejected explanation. The reader ends holding an artifact *they* signed.

## Show me — Chapter 10 as the exemplar

**Opening (build-first):** "You ask Claude to build the ingest step for a competitor-scan
pipeline. It returns 120 lines of working-looking Python in one shot. It runs. It even has
a progress bar. You are about to ship it. Stop — you have just been handed the most
dangerous thing in an AI build: fluent code that solves a problem you never formulated."

**The move (Tool Orchestration + the boondoggle):** instead of accepting the monolith, the
reader runs Gru's `/v0` gate ("what are you *proposing to build* — the thing, not the
problem?") and then produces a **Boondoggle Score**: every step tagged CLAUDE TASK or HUMAN
TASK, each human task labeled with its capacity `[PA/PF/TO/IJ/EI]`, and a testable handoff
condition between each step ("every table has a primary key; no column uses a term outside
the domain model"). The chapter's exercise *is* generating that score for a real task.

**The gate they sign:** the reader clears one phase gate with a named attestation — "Ran
sample mode; saw N records in, M rejected for reason R; did *not* test live-write" — and
learns that "looks good" was never a handoff condition. That's the whole book in one build.

## Honest cautions (so the reframe doesn't fail its own test)

- **Not a portfolio tour.** The ecosystem examples must each be *structurally homologous* to
  the capacity they teach (Eddy's decorative-analogy rule), not "here are Nik's five
  projects." The table above is chosen for homology; drop any that starts feeling like a demo.
- **Keep one external, verifiable case per chapter.** All-in-house examples read as
  self-referential and dodge the book's own provenance rule. Keep COMPAS, the Swedish triage,
  Guo-2017 calibration, etc. as the outside anchors alongside the hands-on build.
- **The hands-on builds must actually run.** A book about not trusting fluent artifacts
  cannot ship exercises that only look runnable. Every build in the book should be one the
  author has actually executed (Snickerdoodle attestation discipline, applied to the manuscript).
- **This is a rewrite direction, not a patch.** Fourteen abstract-first openings become
  build-first; that's real work. But it's the same work the editor notes already asked for
  (phenomenon-first, framework-anchored, quantitative-before-qualitative) — now with a spine
  and a source of concrete builds.
