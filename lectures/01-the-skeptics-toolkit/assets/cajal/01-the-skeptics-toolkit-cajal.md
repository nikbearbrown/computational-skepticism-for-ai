# Figure intelligence — Chapter 1, The Skeptic's Toolkit

Cajal-style scan: the figures that *should* exist for this chapter, what each states
(SCOPE), and what it must NOT try to say (exclusions). One idea per figure.

The book ships fig-01…fig-09, but figs 01–07 are **generic stub bars** — the chapter's
`## Prompts` generated every figure from the same "horizontal bar chart, 5 categories,
values 0–100" template, so "Cartesian doubt as an inspection protocol" and "the turkey
confidence timeline" both came out as meaningless bar charts (title words used as bar
labels). Those are flagged `placeholder` in the manifest; the real figures below were
authored to replace them.

---

## Authored (in the pool)

### F1 · four-moves-checklist.svg — the chapter's spine
- **States:** the four moves (Descartes/Hume/Popper/Plato) as a portable checklist,
  each with the checkable question it hands you.
- **Excludes:** philosophical biography; ranking the moves; any claim they're a strict
  sequence (they're independent tools).
- **Replaces:** stub fig-03 ("three moves as a portable checklist").

### F2 · artifact-vs-world.svg — the cave move, concrete
- **States:** two columns — the artifact the engineers reviewed vs the world they did
  not — joined by a "statistical shadow" that broke at deployment (Swedish triage).
- **Excludes:** blame narrative; clinical detail beyond the one case; any suggestion the
  model malfunctioned (it succeeded — that's the point).
- **Replaces:** stub fig-04 ("two-column split").

### F3 · turkey-confidence-timeline.drawer.js — the induction limit (LIVE D3)
- **States:** confidence rising with each fed day, then collapsing at day 1000. One red
  break. The visual claim: confidence peaks the instant before catastrophe.
- **Excludes:** a real probability model; exact Taleb numbers; any y-axis implying the
  world's actual risk (it's the turkey's *belief*, a model property).
- **Chart, not bar:** this is genuinely a time series — the stub bar version was wrong.

### F4 · cost-asymmetry.drawer.js — the solve-verify inversion (LIVE D3)
- **States:** produce ≈ $0.0001 vs verify ≈ $75, on a **log axis** (≈7 orders of
  magnitude) so the gap is honest, not exaggerated. Red = the cost that doesn't scale.
- **Excludes:** precise dollar figures as fact (labeled as illustrative orders of
  magnitude); a linear axis (would either flatten or mislead).
- **Replaces:** stub fig-05 ("cost asymmetry bar chart") — same idea, honest encoding.

### F5 · five-supervisory-capacities.svg — the core vocabulary
- **States:** the five capacities, what the supervisor does, and what each absence looks
  like (one row per capacity).
- **Excludes:** the per-capacity chapter cross-refs (deck can add); personality framing
  ("good engineers are skeptical") — these are capacities, not traits.

### F6 · fluency-trap-mechanism.svg — the most operational idea
- **States:** the two-stage mechanism (fluency → confidence in output → confidence in
  your own evaluation) + the form/content independence and the interrupt (specify the
  wrong answer first).
- **Excludes:** "distrust fluent output" (wrong lesson — fluent output is usually more
  useful); any claim the next model fixes it (structural).
- **Replaces:** stub fig-06.

## Considered, excluded from the pool
- **Rhetoric → engineering table** (the four "robust/performs well/success/drift"
  corrections): strong content, but reads as a table, not a figure — leave it as a deck
  `concept`/table slide, don't force an SVG.
- **Popper swan asymmetry** as its own figure: covered well enough by doodle D5;
  a static figure would duplicate the four-moves card. Kept as a doodle candidate only.
- **Karl Popper portrait** (`images/karl-popper.jpg`): a book asset, not a concept
  figure — belongs to the Wayback-Machine sidebar, not the lecture pool.
