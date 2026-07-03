# CAJAL Figure Plan — Chapter 13: The Limits of AI: What the Tools Cannot Do

FIGURE 1 — The categorical boundary: the sample cannot contain what the sampling excluded
Heuristic: VG
Priority: Critical
Concept (one sentence): Scaling enlarges the data's covered region of the world, but every enlargement still has a boundary, and the boundary is defined by exactly what the data does not contain — so no amount of added data crosses it.
Reader/audience: reader of Chs. 2–4 (Hume's induction problem, access boundary, distribution shift); no philosophy background needed.
Type: structural schematic
Components (3–8): (1) outer region labeled "the world"; (2) inner region labeled "the data (a sample)"; (3) the boundary line, explicitly labeled "defined by what the sampling excluded"; (4) a second, larger inner region labeled "scaled model — more data" showing the boundary moved but still present; (5) annotation at the boundary: "where deployments fail — the gap lives here"; (6) one-line caption of the complementarity argument: "wider sample and excluded region are complementary by construction (Hume, 1748)".
Exclusions: no Mediocristan/Extremistan panel (Taleb material belongs to the turkey video/graph and TABLE 1); no meaning/intentionality callouts (the inheritance argument stays in prose); no probability-theory formalism; not a Venn diagram of multiple datasets — one sample, one world, one boundary.

FIGURE 2 — The Epic Sepsis Model's circular signal: a model that learned to confirm suspicion, not form it
Heuristic: MC
Priority: Critical (static fallback for video Candidate 02 — build only if the video is not picked)
Concept (one sentence): The early-warning model partly learned to fire on traces of clinicians already suspecting sepsis (e.g., blood-culture orders), so its "prediction" was downstream of the human judgment it was marketed as preceding — a premise flaw invisible to internal validation metrics.
Reader/audience: reader who has met validation metrics (Ch. 2) and data-frame audits (Ch. 4); no clinical background beyond what the labels supply.
Type: cycle
Components (3–8): (1) clinician forms suspicion of sepsis; (2) clinician orders blood culture / responsive workflow trace enters the EHR; (3) model reads the trace as a feature; (4) model fires "sepsis risk" alert; (5) alert lands after/with the suspicion it echoes — arrow back to (1) labeled "confirmatory, not early"; (6) side panel: internal validation scores this loop as high accuracy; (7) the intended (broken) path shown greyed: model warns BEFORE suspicion forms.
Exclusions: no AUC/sensitivity numbers (that is GRAPH 2's job, from Wong et al. 2021); no alert-fatigue subplot; no EHR architecture detail; no vendor-vs-hospital accountability chain (Ch. 12 territory).

FIGURE 3 — Searle's Chinese Room: what the setup is, exactly
Heuristic: VG
Priority: Important
Concept (one sentence): A person who does not understand Chinese follows a rulebook to map incoming symbol slips to outgoing symbol slips, producing behavior indistinguishable from a Chinese speaker's — showing behavior consistent with understanding does not entail understanding.
Reader/audience: no philosophy background; reader has just met Turing's imitation game in the same section.
Type: mechanism cross-section
Components (3–8): (1) the room; (2) the person inside, labeled "does not understand Chinese"; (3) the rulebook (syntactic rules only); (4) input slot with Chinese-symbol slip; (5) output slot with Chinese-symbol slip; (6) observer outside, labeled "cannot distinguish from a Chinese speaker"; (7) caption stating exactly what is settled: "syntax is not sufficient for semantics" — and what is not: whether current systems are ONLY doing this.
Exclusions: no Systems Reply or other counterarguments (Exercise 14 territory); no Turing-test panel (the comparison table already serves that contrast); no claim that the diagram shows current LLMs — the chapter explicitly leaves that contested.

FIGURE 4 — The two-questions gap: the question the system was tested on vs the question the deployment asks
Heuristic: VG
Priority: Important
Concept (one sentence): The clinical system's validation was scoped to "does this presentation match a category in the training data?" while deployment harm arose from "what is going on with this specific patient?" — related questions whose gap no test inside the first question's scope can surface.
Reader/audience: reader of the chapter opening (composite clinical case, explicitly labeled illustrative); the figure must carry the same composite/illustrative label.
Type: comparison panels
Components (3–8): (1) left panel — Question 1: "does this presentation match a training category?" with the validation frame (94% accuracy, fairness, robustness checks) drawn AROUND it; (2) right panel — Question 2: "what is going on with this specific patient?" with no validation frame around it; (3) the gap between panels, labeled "not testable from inside the validation scope"; (4) marker that harms occurred in the gap; (5) supervisor icon positioned at the gap, labeled "the semantic work — mapping outputs to referents"; (6) footer: "composite illustration — the pattern, not a sourced incident".
Exclusions: no patient-level narrative detail; no fabricated harm statistics beyond the chapter's own illustrative framing; no overlap with FIGURE 2 (Epic Sepsis is the real named case, kept separate); no three-limits recap.

FIGURE 5 — The rapid-prototyping loop: testing a load-bearing assumption before deployment
Heuristic: MC
Priority: Supplementary
Concept (one sentence): Six steps — make the assumption explicit, identify falsifying evidence, design a cheap test, pre-register the prediction, run and document the gap, then decide (proceed / modify / defer / refuse) — turn the scientific method into a deployment gate.
Reader/audience: reader who knows the prediction-lock discipline (Ch. 1–2) and Popper's falsification move.
Type: process flowchart
Components (3–8): (1) specify the assumption explicitly; (2) identify what would falsify it; (3) design the cheap, fast test; (4) pre-register the prediction (lock icon); (5) run and document the gap; (6) decide — four labeled exits: proceed / modify / defer / refuse; (7) contrast note: "the validation set is NOT this test — it samples the training distribution".
Exclusions: no example experiment walk-through; no Popper exposition; no repetition of the five-component engineering practice (TABLE 2's job).

FIGURE 6 — The cognitive extremophile: a spiky profile, not a general intelligence
Heuristic: VG / PQ
Priority: Important
Concept (one sentence): Current AI's capacity profile is extreme in one narrow niche (symbolic pattern-matching: retrieval/synthesis, criterion-driven generation, rule application) and weak-to-absent elsewhere (problem formulation, plausibility auditing, judgment under stakes, embodied navigation, causal counterfactuals, metacognitive monitoring, accountability) — a niche specialist, not a general mind.
Reader/audience: reader of this chapter's strengths/weaknesses/absence sections and the Ch. 1 Legg-Hutter definition (intelligence = goal achievement across a WIDE RANGE of environments).
Type: comparison panels (ordinal profile — qualitative bands, explicitly NOT a measured chart)
Components (3–8): (1) horizontal list of capacities grouped in three tiers (strong / structurally weak / absent); (2) ordinal band per capacity: superhuman / strong / weak / absent — labeled "qualitative characterization from the chapter, not measurements"; (3) shaded "niche" region around the three strengths, labeled "symbolic pattern-matching over well-defined inputs"; (4) reference line or note: Legg-Hutter — the RANGE is what intelligence means; (5) caption: "extremophile: superhuman in the niche, category error outside it".
Exclusions: no invented numeric scores or benchmark values; no radar chart with fake magnitudes; no human-baseline series; no seven-tier taxonomy from the author's unpublished work (chapter flags it as uncheckable [verify]).

Recommended: 4–6 figures, Mixed density. (FIGURE 2 only if video Candidate 02 is not picked; FIGURE 1 stands even if video Candidate 01 is picked — the boundary schematic anchors the chapter's central categorical argument on the page, while the video carries the turkey narrative.)
