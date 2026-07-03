# Editorial Feedback — Computational Skepticism for AI

Full-manuscript developmental edit, 2026-07-02. Four independent reviewers (intro+1–2, 3–5, 6–9, 10–13+end matter), benchmarked against Chapter 1's voice. Feedback only — nothing in the manuscript was changed.

## Executive summary

The architecture is sound. The four verified long arcs all work: Pearl Rung 3 (opened Ch4, explicitly closed Ch12), the calibration baseline (Ch2 → Ch4 → Ch13), the Ash case (1 → 5 → 8 → 12), and the casebook's convergence into Ch13's final memo. The voice, where it's yours, is a real instrument — every reviewer independently flagged the same phenomenon: chapters are bimodal, with benchmark-grade frames wrapped around survey-textbook middles from the second draft.

But the manuscript currently contains **falsifiable errors a reviewer with a calculator will find**, and three of them sit in flagship material: Ch7's impossibility tables don't compute, Ch11's frozen verb ladder appears in four contradictory orderings in a chapter whose thesis is "freeze exactly one ordering," and Ch12 ships two incompatible seven-tier taxonomies with three mutually contradictory requirement→tier mappings. These are not polish; they are the book failing its own test.

**Grades:** Intro/frontmatter: non-viable, replace. Ch1 A · Ch2 B · Ch3 B− · Ch4 B · Ch5 A− · Ch6 B · Ch7 B · Ch8 B+ · Ch9 B− · Ch10 A− · Ch11 B · Ch12 C+ · Ch13 B+.

---

## The seven systemic issues (ranked by leverage)

### 1. The Frictional Method cut is the manuscript's open wound

One decision unlocks ~20 fixes. The casebook's core artifacts — the prediction-lock journal, the Frictional journal, the AI Use Disclosure, the case template — are homed in a chapter that no longer exists. Chapters 3, 5, 6, 8, 9, 10, 11, 12, 13 all reference them (every `[verify-xref: Frictional Method chapter cut]` flag). Ch9's fourth deliverable dangles from it; Ch13's final-memo assembly requires a "/07-provenance — Frictional journal" that has no source chapter. **Decide where prediction-locking, the journal, and the Disclosure now live (Ch1 is the natural home for the lock discipline; the Disclosure could move to Ch9), then do one global fix.**

### 2. The casebook exercise chain was written for the dead chapter order

The chapterization pass fixed chapter bodies but the LLM exercises still encode the old sequence. Evidence assembled across reviewers: Ch4's exercise treats Ch5 and Ch7 as *previous* chapters and previews "Chapter 8" as next; Ch5's exercise requires Ch6's Bias-and-Leverage Brief (not yet built) and calls its output "the first formal case" after Ch4 produced two; Ch6's exercise targets "your Chapter 4 robustness probes" as future work; Ch8's paste-ready prompt says "probes you ran in Chs 5, 6, 8" and its connection note contradicts the body's own lens mapping on the same page; Ch9's prompt **fabricates capacity names** ("Goal Verifier, Frame Setter, Boundary Enforcer, Capability Definer — or whichever names the chapter uses") and demands a Boondoggle *scale* the chapter never defines. A student running the casebook in book order hits a wall in week 4. **Fix: draw the Dossier → Data Frame Audit → probe suite → self-explanation audit → brief → cases → map dependency graph once, then regenerate every exercise's Connection/Preview block from it.**

### 3. Correctness surgery (the do-not-ship list)

- **Ch7 (L110–128):** the impossibility tables are arithmetically wrong. Group B: prediction rate computes to 0.22 (table: 0.20), PPV to 0.68 (table: **0.83**) — the calibration-satisfying illustration is a counterexample to its own caption. Also: the theorem is framed over {demographic parity, equalized odds, calibration} but proved over {calibration, equalized odds}; neither cited paper proves the stated triple.
- **Ch11:** the frozen verb ladder (L39) is contradicted by the misuse table (L67–76), the evidence-ladder table (L239–248), and the LLM prompt (L501) — four orderings, one chapter, thesis = "one ordering." Plus the MCE claim (L150) is false as stated (MCE does not avoid bin-dependence), and "Chapters 4, 3, and 4" (L489, L517) is a raw merge artifact.
- **Ch12:** two incompatible seven-tier taxonomies (prose L127–139 vs table L141–149), three conflicting requirement→tier mappings, a corrupted table cell ("Simulates; does not feel" pasted into a reasoning tier), and exercises (W3, LLM) that are unanswerable until one taxonomy wins. `97-fundamental-themes.md` contains a *third* variant.
- **Ch13:** three false claims about the book's own structure sitting in the climax — "Every Extension Note in the chapters before this one" (none exist), "the book that began with The Definition Problem" (it began with Epic Sepsis), "the Legg-Hutter definition this book committed to in Chapter 1" (Ch1 contains no Legg-Hutter). Residue from another manuscript.
- **Ch6 ↔ Ch7:** Ch6 promises the proof to Ch7 (L236) then delivers it in full (L242–248), kneecapping Ch7's centerpiece; and counterfactuals are Rung 3 in Ch6 (L289) but "a Rung 2 operation" in Ch7 (L233).
- **Ch4:** the 10³⁰ FLOPs figure is honestly un-confirmed at L158 and then asserted flat at L373. One must go. Also "eight weeks" (L357) belongs to a dead course pacing.
- **Ch10:** Challenger is diagnosed two incompatible ways (prose L217 rules encoding-failure; table L235 says omission); the catalog is called "nine" but lists ten; "**Sankov** diagrams" should be Sankey (L78).
- **Ch5:** TreeSHAP complexity O(TLD) should be O(TLD²) (L186); M means "features" and "samples" in adjacent table rows.
- **Ch2:** Exercise 6's givens contradict each other (97% accuracy can't flag 0.5% at that base rate) — in the chapter that warns about exactly this; the calibration baseline exercise references a question set that doesn't exist.
- **Ch1:** Descartes's move as defined (L47) *is* Popper's move (L77) — the four-move toolkit is currently two moves in four coats; and the move count wobbles 3 ↔ 4 across the chapter (L25, 37, 225, Figure 1.3 caption).

### 4. The intro and frontmatter cannot ship

Unanimous and blunt: template prose with the title mail-merged in ("the gap between knowing the name of Computational Skepticism for AI's subject"), a bullet TOC leaking truncated learning-objective strings, a claimed theme ("transfer") that appears nowhere in the book, and zero mention of the four moves, five capacities, Ash, the casebook, or the fluency trap. **Replace with a 2–3 page author's note in the Ch1 voice**: thesis in one paragraph, the reader's contract (BUILD/AUDIT + the casebook named as the Pebble), Ash in two sentences, and the 13-chapter map told as an argument, not a list. Bonus: this houses the book's best six-word thesis — "the machine's speed, your doubt" — which chapters 2–13 attribute to Chapter 1 but which Chapter 1 never actually says.

### 5. The Pebble and the thesis phrase are homeless

"The Pebble" is defined in Ch1 (the casebook), but Ch5 (L351) uses it with a different apparent referent, and Ch7 (L400) misattributes it to *Agents of Chaos* Case #6 and claims an in-chapter appearance that doesn't exist. The [PA][PF][TO][IJ][EI] bracket codes appear in the spine documents but nowhere in the manuscript — if they're the book's shorthand, Ch1's capacity table must mint them. And the "pairing Chapter 1 committed us to" callback appears in near-identical words in Chs 3, 4, 5 — a macro, not a spine. Vary it; and put the actual sentence in Ch1.

### 6. Voice: the bimodal chapters have bounded rewrite zones

The second-draft register breaks are locatable, not diffuse: Ch2 lines 109–229 (statics/dice/cards/Alice — imported course problems with no world), Ch3 lines 59–257 (pandas tutorial + marks-and-channels module), Ch6 lines 59–163 (the ten-mechanism plateau, "X bias occurs when..."), Ch7 lines 170–312 (the survey half), Ch9 lines 154–497 (the Gru product walkthrough, with undefined "PHASE F/C" jargon), Ch12 lines 64–151 (the imported capacity catalog — bees, magpies, dolphins). Each needs either repatriation into the book's world (agents, triage, fraud) or compression.

### 7. Mechanical artifact sweep (one pass, book-wide)

Truncated figure captions in nearly every chapter ("Figure 6.1 — Biased vs", "Figure 2.5 — Population grid... arranged as a"); dual figure-numbering systems alive in Chs 6, 8, 10, 12 (numbers assigned twice to different objects); three Ch12 figures captioned "**Figure 13**"; a stray metadata/tags line shipped in Ch8's body (L569); revision-history language in reader-facing prose ("Chapter 6 (bias) now comes later in the book," "earlier drafts of this chapter"); "invisble" (Ch4 L19); visible [verify-xref] editorial notes inside student-facing prompt text (Ch6 L552, Ch8 L621); course scaffolding leaking into book text ("fifteen weeks," "Project v2.0, submitted at the midterm milestone").

---

## Chapter verdicts (condensed)

**Intro/frontmatter — replace.** No sentence worth keeping. See systemic #4.

**Ch1 — A.** The benchmark; cold open and load-bearing sentences most textbooks never achieve. Fix: differentiate Descartes from Popper (premises/provenance vs falsification conditions — the raw material is already on the page), enforce one move count, resolve the Botspeak provenance muddle (L167–169), and either verify or label the *Agents of Chaos* citation the whole book leans on.

**Ch2 — B.** Disease-test sequence and calibration section are exactly the book's promise. Fix zone is bounded: the double opening (L14–22), the imported course-problem middle, Exercise 6's numbers, the DeGrave case misdescribed as temporal drift (contradicting Ch1's correct telling), and an empty calibration question bank anchoring a three-chapter arc.

**Ch3 — B−.** The interrogation doctrine ("why are there exactly N rows," prediction-lock, access boundary) is original curriculum. But the chapter forks: three competing assumption taxonomies (table, prose, LLM exercise) and two different "six-step procedures" under one name. Merge the stacked cold opens (composite disclaimer currently kills the story before it starts — copy Ch5's story-first pattern); cut or relocate marks-and-channels.

**Ch4 — B.** The fragile-vs-proxy reframe and the chapter's willingness to attack its own title and headline statistic are the thesis performed. Fix: the LLM exercise belongs to the dead order (worst instance), the 10³⁰ contradiction, "Rung 3" invoked 225 lines before the ladder exists, Tanay & Griffin uncited, and the robustness-profile numbers need an "illustrative" label.

**Ch5 — A−.** Closest to benchmark; the Shapley math checks at every computed point, and the deflationary sentence placed *before* the impressive derivation (L169) is the book in two sentences. Fix: TreeSHAP exponent, the two Ash narrations with inconsistent hedging (fact vs "possibly"; Proton named here but not in Ch1), the Pebble orphan at L351, exercise forward-references.

**Ch6 — B.** The three-teams parable and leverage analysis are a genuinely original organizing device. Fix: the proof leak into Ch7's territory, the ten-mechanism register plateau (group the minor five, spend the space on selection/historical/implicit), the compound table's undefined primitives, dual figure numbering, stale exercise refs.

**Ch7 — B.** Lines 9–166 are the best sustained Teardown in the mid-book — and the flagship tables under them don't compute. Fix the arithmetic first, restate the theorem over its true triple, then give the survey half (individual/causal/GE) the first-person mechanism treatment and label the promised BUILD/AUDIT exercises.

**Ch8 — B+.** Best cold open after Ch1; the case-driven architecture pays the book's method off. Fix: the promised BUILD/AUDIT exercises **don't exist** (the intro specifies their content — write them), the LLM exercise's old numbering, duplicated weld sentences (L15/17, L66/71), the Case #2 taxonomy contradiction, and the highest verification burden in the book (names, quotes, dates, "NIST's AI Agent Standards Initiative").

**Ch9 — B−.** The handoff-condition doctrine and items-5–8 distinction are the most operationally useful 150 lines in the book. Fix: cut the 340-line Gru walkthrough to one worked handoff, purge undigested internals (Phase F/C, fabricated capacity names, undefined score), label the two-teams composite (the book's own standard), and reconcile Exercise 9 with the body's careful overtrust hedge — the exercise asserts exactly the claim the body declines to make. The body paragraph is right; fix the exercise.

**Ch10 — A−.** Best structure of the back half and the book's best bridge. Fix: Challenger double-diagnosis, nine-vs-ten catalog, figure numbering collision, Sankov→Sankey, triple-stated objectives.

**Ch11 — B.** The verb taxonomy is the most original pedagogical device in the back half — and the chapter currently disproves itself. Reconcile the ladder everywhere, fix the MCE claim, de-duplicate the conflicting evidence→verb tables, check the Brier decomposition labeling, authored transition into the metrics half.

**Ch12 — C+.** The attestation-as-artifact idea and the three-second sign-off experiment are A-grade; the Rung 3 closure genuinely lands. But the load-bearing tier apparatus disagrees with itself everywhere it's used, three figures carry another chapter's captions, the capacity catalog is an unintegrated import, and two referents (the *Intelligence?* volume, Pachocki) are never introduced. Structural surgery, not polish.

**Ch13 — B+.** The categorical-limits argument is the finest philosophical writing in the book, and the casebook convergence into the final memo is a satisfying payoff. Two fixes: purge the other-book residue from the climax, and re-sequence the ending — "Go do the work" currently fires twice and the book's last page is an LLM prompt. End the body at L321; let "There is no Chapter 14" sit next to "Go do the work," where it belongs.

**97-fundamental-themes — harvest and cut.** Series-level marketing in manifesto register, plus a third incompatible tier taxonomy. Its one treasure: the cleanest statement of the five capacities anywhere in the manuscript (L418–426) — harvest into Ch1.

**99-back-matter — fix before ship.** The author page must name Nik Bear Brown (an authorless author page contradicts the accountability chapter's own thesis), and "References may be added in future editions" is untenable for a book whose central skill is calibrating claims to evidence — the [verify] flags are promissory notes and this is where they're redeemed.

---

## Passages the hand-rewrite must protect (reviewers' consensus picks)

- Ch1: "It missed two of every three septic patients. The system had succeeded." / "Each was a turkey with a spreadsheet."
- Ch2: "a set of degrees of belief the model holds, formatted to look like facts about the world." / the self-audit note on decorative numbers.
- Ch3: "You cannot compute the missingness of rows that never existed." / "79,400 is not a fact about the world. It is the residue of a process."
- Ch4: "This is the fluency trap wearing a lab coat."
- Ch5: "A correct explanation made a wrong decision feel right." / "precision about the model, and the model is not the world."
- Ch6: the "someone else's house" paragraph; "conference papers and persistent disparities."
- Ch7: "I want to hand you a problem, prove to you that it has no clean solution..." / "smuggled in as a modeling default."
- Ch8: "The agent's phenomenology is the task is complete. The owner's phenomenology is my toy is broken." / "Looks-fine-from-here is not a defense."
- Ch9: "'Looks good' is not a handoff condition." / the overtrust-as-working-hypothesis paragraph.
- Ch10: "It is a lens, ground to a prescription." / the Erin Simpson sticky note.
- Ch11: "The numbers never changed. What changed was the verb." / "It also survives reading."
- Ch12: the three-second sign-off experiment; "launders the absence of review through a human's credibility."
- Ch13: "You cannot scale your way across a boundary defined by what the scaling did not reach." / "cognitive extremophile" / "Go do the work."

---

## Recommended fix order

1. **Decide the Frictional apparatus home** (one decision; unlocks the casebook, nine chapters of xrefs, and Ch9/Ch13 deliverables).
2. **Regenerate the casebook exercise chain** from a single dependency graph (mechanical once #1 is decided).
3. **Correctness surgery** — the do-not-ship list in systemic #3, starting with Ch7's tables, Ch11's ladder, Ch12's taxonomy.
4. **Write the author's note** replacing intro/frontmatter (houses the thesis sentence and the Pebble contract — three book-level fixes in one move).
5. **Voice passes** on the six bounded zones (systemic #6), in hand-rewrite order.
6. **Mechanical artifact sweep** (captions, dual numbering, metadata, revision-history language) — one pass, scriptable in part.
7. **Ch13 ending re-sequence; 97 harvest-and-cut; 99 author + references.**

The three things no reviewer would let ship under any circumstances: Ch7's inconsistent arithmetic, Ch9's fabricated capacity names in a student-facing prompt, and Ch13's false claims about the book's own structure.
