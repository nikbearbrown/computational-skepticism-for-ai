# HANDOFF — Computational Skepticism for AI

Read this file first to continue work on the book. It is a plain status record, not a command list. The repository is the source of truth; when in doubt, read the file and verify with grep rather than trusting any summary — including this one. Everything below is descriptive: what the book is, what has been decided, what the working constraints are, and what remains.

Author: Nik Bear Brown. Publisher: Bear Brown, LLC. Repo: github.com/nikbearbrown/computational-skepticism-for-ai (branch main). A parallel book, *Friction / Measuring the Learning Struggle*, lives at /Users/nik/Documents/Cowork/friction-measuring-the-learning-struggle and is the companion in the *Irreducibly Human* series.

## What the book is

A masters-level engineering textbook on computational skepticism = AI's superhuman speed paired with irreducibly-human doubt. The thesis sentence is "the machine's speed, your doubt." The spine: four classical skeptical moves (Descartes radical doubt, Hume induction limit, Popper falsifiability, Plato's Cave artifact-vs-world), five supervisory capacities ([PA] plausibility auditing, [PF] problem formulation, [TO] tool orchestration, [IJ] interpretive judgment, [EI] executive integration), the solve-verify asymmetry, the fluency trap, and a BUILD/AUDIT exercise pairing per chapter. A running project (the "Pebble") threads all 13 chapters: the student red-teams one agent of their own choosing into a casebook, driven by the end-of-chapter LLM exercises. The recurring model case is Ash / *Agents of Chaos* Case #1, which returns in Chapters 5, 8, and 12.

## Current chapter order (13 chapters, final)

1 The Skeptic's Toolkit · 2 Probability, Uncertainty, and the Confidence Illusion · 3 Data Validation · 4 Robustness · 5 Model Explainability · 6 Bias · 7 Fairness Metrics · 8 Validating Agentic AI · 9 Delegation, Trust, and the Supervisory Role · 10 Visualization Under Validation · 11 Communicating Uncertainty · 12 Accountability · 13 The Limits of AI.

Files are `chapters/NN-slug.md`. Front matter: `00-frontmatter.md` (title/copyright/preface), `00-introduction.md` (the author's-note intro). Back matter: `99-back-matter.md`. Working notes: `97-fundamental-themes.md` (series-level, not part of the book proper), `_ch1-*.md`, `_expanded-four-moves.md`.

## Decisions already made (each has its own doc)

- **Renumbering** to the 13-chapter order — see `RENUMBERING.md`. The old numbering is dead; a stray reference to old numbers is a bug.
- **The "Frictional Method" chapter was cut**, not reinstated. Its apparatus was re-homed: the casebook journal + prediction-lock discipline + case template are set up in **Chapter 1**; the AI Use Disclosure is defined in **Chapter 9**. The Frictional framework itself is credited (it is the subject of the *Friction* book). See `FRICTIONAL-DECISION.md`.
- **The casebook LLM-exercise chain** — canonical dependency graph in `CASEBOOK-CHAIN.md`. Each chapter's LLM exercise Produces/Consumes specific artifacts in a fixed order; the four validation lenses are Ch3/4/5/7; prediction-locks are made in Ch2/3/4.
- **Pearl's Ladder mapping**: sketched and Rung 3 opened in Ch4; Rungs 1–2 developed in Ch6; Rung 3 closed in Ch12.
- **Seven-tier taxonomy** (Ch12) is the canonical *Irreducibly Human* set: 1 Pattern & Association, 2 Embodied & Sensorimotor, 3 Social & Personal, 4 Metacognitive & Supervisory, 5 Causal & Counterfactual, 6 Collective & Distributed, 7 Existential & Wisdom. Requirement→tier map: Specifications→T4, Audit trail→T1 capture+T4 interpretation, Recourse→T3+T6, Independent review→T4, Sanctions→T7. Do not reintroduce the old "Mechanical execution / Moral seriousness" labels.
- **Ch11 verb ladder** is frozen: hypothesize → suggest → observe → find → show → demonstrate → conclude → prove. Every table/prompt conforms; "indicate" is deliberately off-ladder.
- **Voice and length spec** live in `book.md`: the "Teardown" voice (Feynman machinery-from-first-principles × design-critic trade-off analysis, first person); target 4,500–6,000 words of teaching prose per chapter plus separable end-of-chapter apparatus; chapters open with a narrative cold open, never with bullets/TL;DR/objectives.

## Working constraints

- **No fabrication.** Never invent facts, numbers, names, or citations. Uncertain claims are marked `[verify]`. A `[verify]` flag is a promise, not decoration — it stays until a real source confirms the claim.
- **Voice** is first-person Nik ("Teardown"). Chapter 1 (`01-the-skeptics-toolkit.md`) is the hand-written voice benchmark.
- **Git**: pushes happen from Nik's Mac, not from the agent sandbox (no creds there). Work is committed locally and Nik is given exact Terminal paste commands, one per code block. The sandbox sometimes leaves `.git/*.lock` files and `.fuse_hidden*` junk from in-place edits — stage `chapters/*.md` explicitly, never blanket `git add -A`. Never commit mp3/mp4/large media or build trees; a `.gitignore` is in place.
- **Flags**: `[verify]` = fact to confirm; `[verify-xref]` = cross-reference to check (these should all be resolved now — grep to confirm). The line-1 `<!-- CHAPTERIZED ... -->` comments are working notes and are invisible in output.

## State as of this handoff

All seven items from the editorial review (`EDITORIAL-FEEDBACK.md`) have been resolved: Frictional re-homing, casebook-chain regeneration, correctness surgery (Ch7 impossibility tables, Ch11 verb ladder, Ch12 taxonomy), the author's-note intro, voice passes on six survey-middle zones (Ch2/3/6/7/9/12), length cuts (Ch8, Ch12), the mechanical artifact sweep (captions, dual figure numbering, typos, course-scaffolding language), Ch13's ending re-sequence, and citation verification.

Current teaching-prose sizes (words, apparatus excluded): Ch1 ~6,960 · Ch2 ~8,470 · Ch3 ~5,820 · Ch4 ~7,940 · Ch5 ~6,220 · Ch6 ~8,680 · Ch7 ~7,110 · Ch8 ~9,200 · Ch9 ~7,290 · Ch10 ~7,400 · Ch11 ~7,400 · Ch12 ~9,380 · Ch13 ~7,290. Ch2, Ch6, Ch8, Ch12 still run over the 6,000 target; further cutting them is a content decision (which cases / which sections to drop) rather than prose-tightening — see `LENGTH-CUTS-CH8-CH12.md`.

Git note: as of writing, the last commit is `e7314e81` (length cuts). The mechanical sweep, Ch13 re-sequence, and citation verification were done in the working tree but may not be committed/pushed yet — check `git status` and `git log` first.

## Open items (author's own work)

- Three citations could not be verified and stay flagged: Krell et al. 2024 (Ch2, not found), the "Zhang et al. IPS" attribution (Ch4 — the paper exists but its authors are Qin/Wang et al.), and Delattre et al. 2023 (Ch4 — closest real match is Wang & Jordan 2021). These need correct citations or removal.
- The NIST "AI Agent Standards Initiative" claim (Ch12) was confirmed only against a secondary source dated 2026 — worth checking against NIST directly.
- Remaining `[verify]` flags are intentional and should stay: the 2026 *Agents of Chaos* references (a preprint the book leans on), the forthcoming/unpublished *Irreducibly Human*, and the honest "illustrative, not a measured finding" caveats (e.g. calibration ranges in Ch13, ECE rules-of-thumb in Ch11, the composite case in Ch3).
- A final read-through in Nik's own voice — the chapters are cleaned rough drafts, not finished prose.

## The Wayback / mini-bio series

The "AI Wayback Machine" sections were removed from the chapters and moved to `wayback/` as one source file per figure (Popper, Ramsey, Briet, von Neumann, Reichenbach, Arendt, Mill, Merleau-Ponty, Broadbent, Du Bois, Nightingale, Dewey, Turing). Each becomes a 3–5 minute mini-bio video via the Unreal Reels pipeline; `wayback/MINIBIO-PROMPT.md` is the generation script, `wayback/README.md` the manifest.

## Key files

`book.md` (voice + length + structure spec) · `RENUMBERING.md` · `FRICTIONAL-DECISION.md` · `CASEBOOK-CHAIN.md` · `EDITORIAL-FEEDBACK.md` · `LENGTH-CUTS-CH8-CH12.md` · `chapters/` (the manuscript) · `wayback/` (mini-bio sources).
