# Priority Fixes — Computational Skepticism for AI

*One page rolled up from the 14 per-chapter editor notes (`book-editor` pass: bookmap +
ISE + Eddy, calibrated in `_calibration.md`). Ordered so you can work worst-first and
fix patterns once instead of chapter by chapter. Diagnosis only — no chapter was edited.*

---

## Soundness scoreboard (worst first)

| Ch | Title | Soundness |
|----|-------|-----------|
| 04 | The Frictional Method | **Weak** |
| 03 | Bias: Where It Enters and Who Is Responsible | **Moderate** |
| 13 | Accountability: Who Is Responsible When the System Fails | **Moderate** |
| 01 | The Skeptic's Toolkit | Good |
| 02 | Probability, Uncertainty, and the Confidence Illusion | Good |
| 05 | Data Validation | Good |
| 06 | Model Explainability | Good |
| 07 | Fairness Metrics | Good |
| 08 | Robustness | Good |
| 09 | Validating Agentic AI | Good |
| 10 | Delegation, Trust, and the Supervisory Role | Good |
| 11 | Visualization Under Validation | Good |
| 12 | Communicating Uncertainty | Good |
| 14 | The Limits of AI | Good |

No chapter is High. Every one is held below it by the *same three or four wounds* — so the
highest-leverage work is the cross-cutting fixes below, not the per-chapter list.

---

## The five cross-cutting fixes (do these first — each touches many chapters)

**1. Verify the two canonical failure cases and the *Agents of Chaos* citation — now, before more drafting.**
Both anchor cases still sit under `[verify]`: the Swedish triage death (Ch.1) and the Ash / agentic
email case (Ch.1, *Shapira et al., Agents of Chaos*, 2026 — a **forward-dated** source). That one
paper is load-bearing for **Ch.1, 3, 5–13**, and **Ch.9 depends on it entirely**. If it dissolves or
is mis-cited, a third of the book inherits the error. Verify Case names/numbers against the primary
source, or relabel constructed cases as composites (as Ch.1 already does for Ash). *Single highest-leverage
action in the book: one verification protects ~7 chapters.*

**2. Reconcile the self-contradicting reference tables.**
A book preaching evidentiary discipline currently contradicts itself in its own instruments:
- **Ch.11** — the four-case summary table diagnoses different failures/magnitudes for Challenger and Catalonia than the prose.
- **Ch.12** — the verb taxonomy appears in three orderings with two membership lists (`observe`/`find` and `suggest`/`find` invert between tables); the core instrument can't order itself.
- **Ch.13** — Recourse / Independent review / Sanctions each get *different* requirement→tier assignments across prose and two tables; the chapter's central structural claim collapses if the mapping is unstable.
- **Ch.3** — the ten-mechanism taxonomy is contradicted by its own compound-interaction table (which lists non-canonical types).
- **Ch.9** — duplicate "Figure 9.2"/"9.4", captions mismatched to content, and exercises A5/S3 reference **Cases #12–#16 that never appear** (a hard "reader cannot proceed" defect).
These are disqualifying if a reviewer catches them, and reviewers will. Highest-impact class after provenance.

**3. Fix Chapter 4's fluency-trap superstructure — source it or demote it.**
The one **Weak** chapter, and the most serious because it *commits the exact failure the book teaches*:
it names the fluency trap, then builds an elaborate GLP / Y₁–Y₇ measurement apparatus and a
dopamine/BDNF/dendritic-spine neurobiology chain — asserted with zero citations, defining a probability
it never computes, claiming "credible intervals" for an instrument never operationalized. Either cite and
validate it, or explicitly reframe GLP/Y-components as a *conceptual scaffold / research proposal*, not a
measure. Also cite its real anchors (Bjork & Bjork 2011; a spacing-effect meta-analysis) — the strongest
claims are currently the least sourced.

**4. Apply `[verify]` discipline uniformly to unsourced load-bearing claims.**
The provenance rule is applied unevenly. Worst offenders: **Ch.4** (no `[verify]` tags yet the most
unsourced claims), **Ch.8** (8+ tags; the "scale can't close the gap" headline rests on the unsourced
Bartoldson 90% / 10³⁰-FLOPs numbers), **Ch.10/12/14** (clean on *tags* but full of untagged empirical
assertions — "overtrust is the dominant failure mode," ECE 0.02–0.05 ranges, Taleb, the "students score
0.4–0.6" learning-outcome ranges). Also several fluent, unsourced *opening anecdotes* carry whole chapters
(Ch.5 join-failure, Ch.6 radiologist, Ch.14 clinical case) — tag or label them composite. Treat untagged-
but-unsourced the same as `[verify]`: same load-bearing risk.

**5. Name the spine explicitly where chapters already enact it (cheap, high-value).**
The house test — anchor to ≥2 elements of the Ch.1 spine — fails or is thin in **Ch.2, 5, 7, 11, 13**,
even though the reasoning is present. The four skeptical moves in particular fade across the operational
chapters (8–12) while the five-capacities/asymmetry side carries them. Fix is one labeling sentence per
chapter (e.g., "this is the solve–verify asymmetry"; "this is the Plato's Cave move"; pull Ch.7's five-
capacities mapping out of exercise 13 into the body). And in **Ch.13**, add two sentences framing the seven
tiers as *downstream of* the four moves so it doesn't read as a competing framework.

---

## Worst-first, one lead fix per chapter

**Ch.04 (Weak).** Source or demote the GLP/neurobiology apparatus (cross-fix #3) — it discredits a strong first half.
**Ch.03 (Moderate).** Reconcile the ten-mechanism taxonomy with its own compound-interaction table; prove or cite the fairness impossibility instead of asserting "it is a theorem."
**Ch.13 (Moderate).** Reconcile the requirement→tier mappings; downgrade the Gödel claim from "a logical proof" to a structural analogy; flag the unpublished *Irreducibly Human* dependency.
**Ch.01.** Resolve the Swedish triage case to a primary source (or relabel composite); confirm the *Agents of Chaos* citation before Ch.5–13 lean on it.
**Ch.02.** Anchor to ≥2 spine elements explicitly (Popper on the four questions; fluency trap on the "decorative number"); resolve DeGrave 2021 / Guo 2017 / Krell 2024.
**Ch.05.** Name the Plato's-Cave and solve–verify anchors in the body; `[verify]`-tag the opening join-failure war story.
**Ch.06.** Reconcile the Shapley axiom named **Additivity** in prose but **Linearity** in the table; break the honeymoon earlier so SHAP doesn't feel more trustworthy than the thesis allows.
**Ch.07.** Pull the five-capacities mapping from exercise 13 into the body; show the "calibration-satisfying" example table is actually calibrated (or label it schematic).
**Ch.08.** Resolve the eight `[verify]` tags, especially Bartoldson (90% / 10³⁰ FLOPs) on which the headline finding rests; carry the uncertainty into the conclusion rather than dropping it.
**Ch.09.** Verify *Agents of Chaos* + case numbering; add the missing Cases #12–#16 the exercises require; repair duplicate figure numbers.
**Ch.10.** Right-size the proprietary "Gru" walkthrough so the method stands tool-independently; source or reframe "overtrust is the dominant failure mode."
**Ch.11.** Reconcile the four-case narrative with its summary table; cite or downgrade the load-bearing perception percentages.
**Ch.12.** Freeze one canonical verb ordering and one membership list across all tables (and decide whether the taxonomy is 1-D or 2-D).
**Ch.14.** Make the "operational consequence binds regardless of philosophy" argument once, rigorously, up front — and show it establishes a *categorical*, not merely *frequent*, limit.

---

## Book-wide note on figures

Across at least Ch.1–7 the D3/figure-prompt appendices are **identical boilerplate** ("horizontal bar
chart with 5 labeled categories") that contradicts the figure captions — the specs are placeholders. The
per-chapter *High-assertion zones* sections list the figures that actually carry an argument (e.g., Ch.6's
SHAP force plot summing to 0.17, Ch.7's impossibility triangle, Ch.5's join-drop). Those are the ones to
author for real; the rest of the appendix boilerplate should be regenerated or removed.
