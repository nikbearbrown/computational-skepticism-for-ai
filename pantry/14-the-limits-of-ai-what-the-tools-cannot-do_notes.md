# Research Notes: Chapter 14 — The Limits of AI: What the Tools Cannot Do
**Corresponding chapter:** chapters/14-the-limits-of-ai-what-the-tools-cannot-do.md · **Editor note:** notes/14-the-limits-of-ai-what-the-tools-cannot-do.md · **Generated:** 2026-07-01

## Chapter summary
The book's final chapter names three structural limits — meaning, intentionality, and the data-world gap — that bound AI regardless of scaling, tying each to its operational form met earlier (Hume, access-boundary, distribution shift). It reframes AI as a "cognitive extremophile" via the extended-mind lineage and lands on the supervisor's authority to *refuse* deployment as the system's most important authority, using Turing/Searle demarcation and Taleb's turkey/Mediocristan-Extremistan as its sharpest instruments.

## A. Load-bearing claims → sources
- **Claim:** Inductive inference (the future will resemble the past) has no non-circular rational justification — the data-world gap / distribution-shift limit at book scale. · **Source:** Hume, D., *An Enquiry Concerning Human Understanding*, 1748, Section IV (and *A Treatise of Human Nature*, 1739, Bk. I, Pt. iii, §6) · primary · **Verdict:** CONFIRMED — Hume's problem of induction; he attributes inductive belief to "custom/habit," not reason. (See also Stanford Encyclopedia of Philosophy, "The Problem of Induction.")
- **Claim:** In Extremistan a single observation can dominate the aggregate; the "turkey problem" shows induction from a long uneventful record can be catastrophically wrong (fed for 1,000 days, killed on day 1,001). · **Source:** Taleb, N.N., *The Black Swan: The Impact of the Highly Improbable*, Random House, 2007 · primary · **Verdict:** CONFIRMED — Mediocristan/Extremistan distinction and the turkey (Russell's chicken, per Taleb) confirmed. Note: Taleb credits Bertrand Russell's inductivist chicken for the original image.
- **Claim:** Symbol manipulation alone is not understanding — the Chinese Room; a program executing syntax lacks semantics/intentionality regardless of behavioral fluency. · **Source:** Searle, J.R., "Minds, Brains, and Programs," *Behavioral and Brain Sciences* 3(3), 1980, pp. 417–457. DOI 10.1017/S0140525X00005756 · primary · **Verdict:** CONFIRMED — directed against functionalism/computationalism; "syntax is not sufficient for semantics." The chapter's careful "what Searle does and doesn't settle" reading is defensible (SEP "The Chinese Room Argument").
- **Claim:** "Can machines think?" is best replaced by the imitation game (Turing Test); Turing brackets metaphysics for behavioral indistinguishability. · **Source:** Turing, A.M., "Computing Machinery and Intelligence," *Mind* 59(236), 1950, pp. 433–460. DOI 10.1093/mind/LIX.236.433 · primary · **Verdict:** CONFIRMED.
- **Claim:** Intelligence = an agent's ability to achieve goals across a wide range of environments (used to argue AI's narrow niche width). · **Source:** Legg, S. & Hutter, M., "Universal Intelligence: A Definition of Machine Intelligence," *Minds and Machines* 17(4), 2007, pp. 391–444. DOI 10.1007/s11023-007-9079-x; arXiv:0712.3329 · primary · **Verdict:** CONFIRMED — the "wide range of environments" definition is theirs; supports the "cognitive extremophile / narrow niche" reframe.
- **Claim:** LLMs produce fluent text without grounding in meaning — "stochastic parrots." · **Source:** Bender, E.M., Gebru, T., McMillan-Major, A. & Shmitchell, S., "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *Proc. FAccT 2021*, pp. 610–623. DOI 10.1145/3442188.3445922 · primary · **Verdict:** CONFIRMED — "stitching together linguistic forms... without any reference to meaning" is the paper's definition; supports the meaning-limit's contestation framing.
- **Claim:** Deep learning is brittle out-of-distribution, data-hungry, and lacks causal/systematic reasoning — the limits-of-current-tools case. · **Source:** Marcus, G., "Deep Learning: A Critical Appraisal," arXiv:1801.00631, 2018 · primary · **Verdict:** CONFIRMED — ten challenges incl. brittleness, poor OOD generalization, absence of causal reasoning, hybrid/neuro-symbolic prescription.
- **Claim:** Whether multimodal grounding could "constitute something more" and close the meaning gap operationally. · **Source:** (chapter cites) Chalmers 2023 on LLMs & consciousness · **Verdict:** [UNVERIFIED here — not searched] — Chalmers, D., "Could a Large Language Model Be Conscious?" (2023, Boston Review / arXiv:2303.07103) is real; confirm exact venue/page. The strong-functionalist counter (grounding closes the gap) is a live position the chapter should engage in-body (editor Priority #4).

## B. Resolving the editor's [verify] flags
- **Bender et al. 2021 (stochastic parrots)** → CONFIRMED. See A.
- **Chalmers 2023 on consciousness and LLMs** → [UNVERIFIED here] — real work exists (arXiv:2303.07103 / Boston Review 2023); confirm exact citation.
- **Searle 1980, *Minds, Brains, and Programs*** → CONFIRMED. *BBS* 3(3): 417–457.
- **Turing 1950, *Computing Machinery and Intelligence*** → CONFIRMED. *Mind* 59(236): 433–460.
- **Taleb, *The Black Swan* (2007), Mediocristan/Extremistan/turkey** → CONFIRMED. Random House, 2007.
- **Legg-Hutter definition** → CONFIRMED. *Minds and Machines* 17(4): 391–444.
- **"Hampton sense" of metacognitive monitoring** → [UNVERIFIED] — likely Robert R. Hampton (e.g., "Rhesus monkeys know when they remember," *PNAS* 2001) on metacognition in animals; confirm the specific attribution.
- **Three calibration-baseline score ranges (0.4–0.6 / 0.6–0.75 / 0.7–0.85, "most students score...")** → [UNVERIFIED] — an empirical claim about learning outcomes with NO data source. Either cite the course's own measured data or reframe as an *expected pattern the student checks against*, not a measured finding.
- **Opening clinical-decision-support case (94% accuracy, three patients harmed, "engineers designed the wrong tests")** → [UNVERIFIED] — no citation; reads as composite/illustrative. Per the book's own standard (and the calibration file's treatment of the analogous Swedish-triage case), it must be sourced or explicitly labeled composite/hypothetical. As written it carries real-case authority without provenance.

## C. Domain examples / cases (real, cited)
- **Chinese Room (Searle 1980):** CONFIRMED philosophical case for the meaning/intentionality limits.
- **Turing Test (Turing 1950):** CONFIRMED; used for the demarcation of what behavioral tests settle.
- **Turkey / Extremistan (Taleb 2007):** CONFIRMED; the best-integrated outside case, giving the data-world gap operational shape.
- **Stochastic Parrots (Bender et al. 2021):** CONFIRMED source for the "fluent without meaning" claim.
- **Marcus 2018 critique:** CONFIRMED source for the concrete brittleness/OOD/causal-reasoning limits.
- **Opening clinical case:** [UNVERIFIED / likely composite] — NOT a citable real case as written.

## D. Open flags (still [UNVERIFIED])
- Opening clinical-decision-support case — uncited; label composite or source it.
- Calibration-baseline score ranges (0.4–0.6 / 0.6–0.75 / 0.7–0.85) — no data source; reframe as expected pattern.
- "Hampton sense" of metacognitive monitoring — confirm Hampton citation.
- Chalmers 2023 exact citation.
- The "binds regardless of the philosophy" move establishing a *categorical* (not merely frequent) limit is an argumentative gap (editor Priority #1), not a citation gap — no external source resolves it; it must be argued in-body.

## Sources
Primary:
- Hume, D. (1748). *An Enquiry Concerning Human Understanding*, §IV. (Also *Treatise*, 1739, I.iii.6.)
- Taleb, N.N. (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House.
- Searle, J.R. (1980). Minds, Brains, and Programs. *Behavioral and Brain Sciences* 3(3): 417–457. https://doi.org/10.1017/S0140525X00005756
- Turing, A.M. (1950). Computing Machinery and Intelligence. *Mind* 59(236): 433–460. https://doi.org/10.1093/mind/LIX.236.433
- Legg, S. & Hutter, M. (2007). Universal Intelligence: A Definition of Machine Intelligence. *Minds and Machines* 17(4): 391–444. https://doi.org/10.1007/s11023-007-9079-x ; arXiv:0712.3329
- Bender, E.M. et al. (2021). On the Dangers of Stochastic Parrots. *FAccT '21*: 610–623. https://doi.org/10.1145/3442188.3445922
- Marcus, G. (2018). Deep Learning: A Critical Appraisal. arXiv:1801.00631.
Secondary / to confirm:
- Chalmers, D. (2023). Could a Large Language Model Be Conscious? arXiv:2303.07103. [confirm venue]
- Hampton, R.R. (2001). Rhesus monkeys know when they remember. *PNAS* 98(9): 5359–5362. [confirm "Hampton sense" attribution]
- Stanford Encyclopedia of Philosophy, "The Problem of Induction" & "The Chinese Room Argument." https://plato.stanford.edu/entries/induction-problem/ ; https://plato.stanford.edu/entries/chinese-room/
