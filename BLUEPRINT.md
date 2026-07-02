# BLUEPRINT.md — Computational Skepticism for AI
### Validating What Gets Built with AI — Yours and Everyone Else's

**Author:** Nik Bear Brown · Humanitarians AI
**Status:** Reframed plan of record (2026-07-01). The 13 chapters below are the target; the
current manuscript in `chapters/` is *reference material for the rewrite*, not the finished
book. Grew out of INFO 7375 and the Snickerdoodle / Irreducibly Human ecosystem.

---

## Concept — the reframe

**What computational skepticism is (the definition — this is Chapter 1).** The term is the
thesis. **Computational**: the AI does the fast things — writes code, gathers data, retrieves
patterns, drafts prose — and is *superhuman* at them (the forklift). **Skepticism**: the
irreducibly-human capacity for doubt — the supervisory judgment that decides what is worth
building, hears the wrong note before recomputing, interprets what an output *means*, and signs
for it. **Computational Skepticism is the discipline of pairing the two:** using the machine's
speed while supplying the doubt no tool can supply. The combination beats either alone — *Tier 1
without Tier 4 is a very efficient way to be confidently wrong at scale.*

This places the book in the **Irreducibly Human** series: it is the applied text for **Tier 4 —
the metacognitive / supervisory layer** (plausibility auditing, problem formulation, tool
orchestration, interpretive judgment, executive integration — the five capacities), the same
ground as *Conducting AI (Book 5)*. Gru's boondoggle *is* conducting AI; this book is the
skepticism half of the combo, taught hands-on.

Old framing: *be skeptical of AI systems* (abstract, third-person, a survey of ML-validation
topics). New framing: **be skeptical of what gets built with AI — yours and everyone else's**
(concrete, second-person, hands-on). The reader learns to distrust the fluent, confident,
AI-generated artifact whether they conducted it or someone handed it to them — the dataset
that looks clean, the code that runs, the agent that reports success, the chart that persuades,
the vendor model that scores you, the deployed system that just failed.

**Two stances, one discipline.** The same five capacities run in two directions:
- **Building** *(proactive)* — you conduct the AI and control the process. Hardest problem:
  the fluency trap runs strongest on your *own* output, because you want to believe what you
  just made (ownership bias).
- **Auditing** *(forensic)* — an AI-built artifact you didn't control lands on your desk: a
  colleague's AI-drafted code, a vendor's model, a paper's results, a chart, a deployed system.
  Hardest problem: you have *distance* but little *provenance* — you weren't there for the
  decisions and must reconstruct a frame you never saw.

A third seat matters in the high-stakes chapters: you are often the **subject** of a system
others built (the patient triaged, the applicant scored) — accountability, fairness, and limits
are argued from that seat. The book trains all three: responsible builder, sharp reviewer,
and clear-eyed subject.

**Every chapter runs both directions.** Each chapter has the reader *build something and audit
something* — the same capacity exercised twice: once on an artifact you conducted (where the
hard part is not believing your own fluent output), once on one that landed on your desk (where
the hard part is reconstructing a process you never saw). The pairing is the through-line; by
the end the reader has done both, thirteen times.

The book is the theory text for a working ecosystem that already runs one claim —
**AI made execution cheap; it did not make judgment cheap.** Its worked examples come from
that ecosystem: **madison** (branding pipelines, verified data contract), **mycroft** (the
agent operating system), **the-reallocation-engine** (the reallocation principle), **Gru**
(the boondoggle / SDD consultant), and **SNICKERDOODLE** (the constitution with phase gates,
provenance, attestation). Chapters are **domain-plural** — each grabs the example that is
*structurally homologous* to its move, never one costume across the whole book.

## The spine — stated once in Chapter 1, never re-explained

The **solve–verify asymmetry**: AI solves faster than any human and that gap will not close;
what stays human is verification. Verification decomposes into **five supervisory capacities**,
and every chapter is one of them, exercised on a real build:

- **[PA] Plausibility Auditing** — hearing the wrong note *before* you verify.
- **[PF] Problem Formulation** — deciding what the mission is before the AI sees it.
- **[TO] Tool Orchestration** — which AI task, in what order, with what trust.
- **[IJ] Interpretive Judgment** — supplying meaning and accountability the AI can't.
- **[EI] Executive Integration** — holding all four toward one goal you sign for.

Two hazards ride alongside: the **Fluency Trap** (well-formed output read as evidence) and
the **Provenance rule** (no number exists that no record produced). The four classical moves
— Cartesian doubt, Humean induction, Popperian falsifiability, Plato's Cave — are the
sharpening tools, introduced in Ch.1 and *named explicitly* wherever a chapter uses one.

## The house rule — build-first, every chapter

Each chapter runs one pattern **twice** — once building, once auditing (replacing the current
abstract-first openings):

1. **The artifact** — an AI-built thing. *Build pass:* you ask the AI and get it in seconds.
   *Audit pass:* a vendor / colleague / paper / deployed system hands you one.
2. **The trap** — it looks done. Name what it does not announce (which claim is sourced, which
   step failed, who is accountable). On the build pass, name *why you want to believe it*
   (ownership bias); on the audit pass, name *what provenance you're missing*.
3. **The move** — apply the chapter's capacity + one classical move to *this* artifact; show
   the wrong note; do the math before the qualitative verdict.
4. **The gate** — produce the human decision the reader signs: a handoff condition, an
   attestation row, a downgraded verb, a rejected explanation, a defended definition.

The two passes teach different muscles — building fights self-trust, auditing fights the
provenance gap — and the reader finishes each chapter having exercised the capacity both ways.

Every hands-on build must actually run — a book about distrusting fluent artifacts cannot
ship exercises that only *look* runnable (Snickerdoodle attestation discipline, applied to
the manuscript itself). Each chapter also keeps **one external, verifiable case** (COMPAS,
the Epic Sepsis Model (Wong 2021), Guo-2017 calibration) so the book is not a portfolio tour of in-house work.

---

## The arc — the flow, and why it's this order

The book follows the **builder's own journey**, and responsibility widens as it goes: from a
single output you distrust → a pipeline you validate → a build you conduct → results you own.

**Part I — The Asymmetry** *(define the discipline; install the most common wrong note)*
Ch.1 **defines computational skepticism** — the Computational + Skepticism combo, the Irreducibly
Human / Tier-4 grounding, the solve–verify asymmetry, the fluency trap, provenance, and the four
classical moves (Descartes / Hume / Popper / Plato) as the *lineage and tools* of human doubt.
Ch.2 installs the single most pervasive failure — confident numbers that aren't correct —
because calibration underlies every later judgment.

**Part II — Validating What You Build** *(the pipeline: inputs → fragility → output → harms)*
You build in an order, so you validate in that order: the data you feed it, the fragility of
what it produces, whether its "explanation" explains, and whether its output is biased or
unfair. This is the [PA]→[IJ] heart of the book.

**Part III — Conducting the Build** *(orchestration and delegation)*
Having learned to distrust a single output, you now orchestrate many. Agents that report
false success, and the boondoggle — conducting AI through a build with explicit human decision
nodes. This is [TO]/[EI] and the most hands-on part (Gru's `/v0` + Boondoggle Score).

**Part IV — Report, Own, and the Limit** *(communicate honestly, sign for it, know the edge)*
Honest visualization, warranted verbs, the attestation you sign, and the close: **The Limits of
AI** — the decision that is irreducibly human, regardless of capability scaling. The book opens
by *defining* the human half of the combo (Ch.1) and closes by *bounding* it (Ch.13); the
philosophy is the frame, not a late chapter.

## Chapter-by-chapter (13)

Every chapter exercises its capacity **twice** — a **Build** pass (you conduct the AI) and an
**Audit** pass (an artifact lands on your desk). Both use the four classical moves; the split
is who made the thing.

| # | Chapter | Cap. | BUILD — you conduct (fight self-trust) | AUDIT — handed to you (fight the provenance gap) | Ref. |
|---|---------|------|-----------------------------------------|--------------------------------------------------|------|
| **I** | **The Asymmetry** | | | | |
| 1 | What Is Computational Skepticism? | all five | Conduct one AI task (a Gru boondoggle); catch where computational speed handed you something only human doubt catches | Apply the four moves to the Epic Sepsis Model case; name the missing supervisory capacity | old 1 |
| 2 | The Confidence Illusion | PA | Make your pipeline emit confidence scores; calibrate; catch your decorative number | Check a vendor model's / a paper's confidence against base rates | old 2 |
| **II** | **Validating What Gets Built** | | | | |
| 3 | Data Validation | PA+PF | Assemble a dataset with AI; validate it before it enters `verified/` | Reconstruct the frame behind a dataset a colleague handed you; block the join failure | old 5 |
| 4 | Robustness | PA | Perturb your own pipeline's input; find where it breaks | Probe a deployed model / others' recipe for a fragility you didn't design | old 8 |
| 5 | Explanation vs. the Appearance of Explanation | IJ | Get AI to explain *your* model's decision; test if it explains the world | Falsify a vendor's SHAP/rationale you were handed | old 6 |
| 6 | Bias: Where It Enters, Who's Responsible | IJ | Run your persona/data build; find where you let bias in | Trace where bias entered a deployed system; assign the accountable owner | old 3 |
| 7 | Fairness: Choose a Definition and Defend It | PF+IJ | Choose and defend a fairness definition for a system you're building | Judge COMPAS's definition; prove the impossibility; name who should have decided | old 7 |
| **III** | **Conducting the Build** | | | | |
| 8 | Validating Agentic AI | TO+EI | Run your own agent; catch its false success report; write the stop condition | Catch a false success report from an agent someone else configured | old 9 |
| 9 | Delegation, Trust, and the Boondoggle | TO (all five) | Produce a Boondoggle Score for your real task; sign a phase gate | Review someone else's boondoggle/handoffs; find the missing human decision node | old 10 |
| **IV** | **Report, Own, and the Limit** | | | | |
| 10 | Visualization Under Validation | IJ+PA | Have AI chart your data; catch and fix your own misleading encoding | Catch the misleading axis in a chart you were shown | old 11 |
| 11 | Communicating Uncertainty | IJ | Calibrate the verbs in a report you write; map each claim to its proof | Downgrade the verbs in an AI-written claim someone sent you | old 12 |
| 12 | Accountability: Who Signs the Gate | IJ+EI | Write an attestation for your build (what you tested, what you did *not*) | Assign accountability for a system that failed (Epic Sepsis Model): who should have signed? | old 13 |
| 13 | The Limits of AI | EI | Name the irreducibly-human decision in your own build | Name it in a system others deployed; say why scaling won't reach it | old 14 |

Every capacity owns real estate ([IJ] richest, Ch.5–7 and 10–12; [PF] across Ch.1, 3, 7, 9),
and every chapter ends with the reader having *built one thing and audited one thing*. The book
**opens by defining the human half of the combo (Ch.1)** and **closes by bounding it (Ch.13)** —
the philosophy is the frame, not a late chapter. The Boondoggle Score (Ch.9) is the single most
tangible thing a reader makes — a good marketing hook.

## What changed from the current manuscript

- **Ch.4 (The Frictional Method) is cut** → ported to `friction-measuring-the-learning-struggle`.
  It was a different subject (assessment of *human learning*), the manuscript's one **Weak**
  chapter, and its transferable kernel is already the spine. (See `_cut-to-friction-book/`.)
- **Resequenced** from a topic list into the builder's-journey arc above (14 → cut Ch.4 →
  **13 chapters**).
- **Ch.1 reframed to "What Is Computational Skepticism?"** — the *definition* chapter. It names
  the Computational + Skepticism combo, grounds the book in the **Irreducibly Human** series at
  **Tier 4** (the five supervisory capacities), and carries the philosophy of skepticism *as the
  definition and the lineage of the four moves* (Descartes / Hume / Popper / Plato) — not as a
  separate late chapter. The book opens by defining the human half and closes (Ch.13) by bounding
  it; philosophy is the frame. Keep Ch.1 phenomenon-first even as it does definitional work.
- **Reframed subject**: "validate AI systems" → "validate what gets built with AI, **yours and
  everyone else's**"; every chapter goes **artifact-first** and **hands-on**, with an explicit
  **build ↔ audit** stance so the book teaches both conducting your own work *and* auditing
  what others hand you (and being the subject of what others deploy).
- **The five capacities become the explicit spine** (fixes the editor finding that chapters
  floated free of the framework), and the four classical moves get **named in the body** where
  used, not left implicit.
- **the-reallocation-engine** re-homed from the (forced) friction slot to **Ch.1**, where the
  reallocation principle actually belongs.

## Prerequisites

The reader can talk to an AI agent and run the commands it hands them; not necessarily a
programmer. Helpful but not required: the basics of supervised ML (train/validation/accuracy).
Foundations before genres: a reader who tries the boondoggle (Ch.9) without the toolkit (Ch.1)
and the confidence illusion (Ch.2) will not feel why a fluent artifact is dangerous.

## Positioning (one line)

Computational speed + irreducibly-human doubt: the field manual for pairing the two. Not "how AI
works" and not "how to prompt," but how to catch the confident, fluent, wrong artifact — whether
you conducted it or someone handed it to you — before it ships or reaches a customer. The Tier-4
"skepticism" text of the Irreducibly Human series; the practice for which madison, Gru, and
Snickerdoodle are the tooling.

## Open questions / next

- **Part IV — Viz + Uncertainty** could collapse into one "Honest Reporting" chapter if the
  book wants 12; kept separate for now (both are hands-on).
- **A standalone Problem-Formulation chapter?** PF is currently distributed (Ch.1/3/7/9). If it
  proves under-taught in the rewrite, promote Gru's `/v0` gate into its own early chapter.
- **Rewrite order:** draft **Ch.9 (the boondoggle)** first as the exemplar hands-on chapter —
  it's the most concrete and sets the build-first pattern for the rest.
