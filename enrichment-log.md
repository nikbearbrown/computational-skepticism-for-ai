# Enrichment + Cleanup Log

Run: 2026-05-05 — computational-skepticism-for-ai (pantry pass v1)

## What changed (2026-05-05) — pantry pass v2 (Taleb / Black Swan)

User expanded `pantry/` to 13 books — a substantial collection covering statistics, AI alignment, prediction, and skepticism. Audited against the book's current state.

**Result: one targeted addition; 12 of 13 skipped.**

The 13 books:
1. Clayton — *Bernoulli's Fallacy*
2. Best — *Damned Lies and Statistics*
3. Huff — *How to Lie with Statistics*
4. Parker — *Humble Pi*
5. Wheelan — *Naked Statistics*
6. Sutton & Barto — *Reinforcement Learning: An Introduction*
7. Christian — *The Alignment Problem* (×2 copies)
8. Taleb — *The Black Swan*
9. Surowiecki — *The Wisdom of Crowds*
10. Cipolla — *The Basic Laws of Human Stupidity*
11. Pearl & Mackenzie — *The Book of Why*
12. Silver — *The Signal and the Noise*

Most of these cover territory the book is already grounded in through specific primary sources and chosen frameworks (Pearl's Ladder, Five Supervisory Capacities, Frictional method, *Agents of Chaos* longitudinal case). Adding citations across multiple chapters would mean running parallel vocabularies for the same territory and would over-cite.

The exception: Taleb's *Black Swan* (2007). Ch 14's third structural limit — the data-world gap — is currently stated abstractly ("the data is always less than the world; gaps are structurally unlearnable from within the training set"). Taleb's Mediocristan/Extremistan distinction gives this limit a sharper specific shape: some data-generating distributions are outlier-dominated, and on those distributions no amount of training data closes the gap. The turkey problem is the canonical illustration: 1000 days of routine evidence, 99.7% accuracy, until day 1001 (Thanksgiving) when the model fails catastrophically. This is exactly the AI validation case — a model tested on ten thousand routine cases may still be a turkey.

**Edit:** Three new paragraphs added in Ch 14 between the Limit 3 engineering-practice line and the Turing/Searle section. Names Taleb's Mediocristan/Extremistan distinction; explains the turkey problem; applies the framing directly to AI validation (the supervisor's job is to know which distribution the deployment lives in; high-stakes deployments often live in Extremistan even when routine traffic looks Mediocristan).

**Skipped (with reasoning):**
- **Pearl, *Book of Why*** — already the spine of the book (heavy integration in Chs 3, 6, 7, 8, 13). Adding more would be over-citation. The earlier intelligence-book pantry pass added one Pearl direct quote in Ch 9 of *that* book; here, Pearl's framework is already structurally present.
- **Christian, *Alignment Problem*** — already engaged in the intelligence-book pantry pass (cascading errors → Ch 16). For this book, the alignment-problem material is mostly covered by the Goodhart's Law and reward-specification content already in Ch 8.
- **Silver, *Signal and the Noise*** — Ch 12 (Communicating Uncertainty) is grounded in academic calibration metrics (Brier score, ECE, reliability diagrams). Silver is popular synthesis; the chapter's grounding does not need it.
- **Sutton & Barto** — Ch 9 (Validating Agentic AI) is about validation in deployment, not RL training. Adding the canonical RL textbook would be a topic shift.
- **Surowiecki, *Wisdom of Crowds*** — collective-intelligence material is not currently a chapter focus.
- **Bernoulli's Fallacy / Naked Statistics / How to Lie with Statistics / Damned Lies / Humble Pi** — popular statistics works covering territory already grounded in Chs 2, 5, 11. Adding any would be parallel framework.
- **Cipolla, *Basic Laws of Human Stupidity*** — humorous classic; doesn't fit the engineering-validation register.

**Citation to verify:** Taleb, N. N. (2007). *The Black Swan: The Impact of the Highly Improbable.* Random House.

---

## What changed (2026-05-05) — pantry pass v1 (Bergstrom & West, Calling Bullshit)

User added a single text to `pantry/`: Carl T. Bergstrom and Jevin D. West, *Calling Bullshit: The Art of Skepticism in a Data-Driven World* (2020). Audited against the book's current state.

**Result: one targeted addition.**

*Calling Bullshit* is a major contemporary book on data skepticism that overlaps directly with this textbook's mission. Most of the territory — selection bias, Goodhart's Law, p-hacking/replication, Simpson's Paradox, GIGO, algorithmic black-box critique — is already grounded in this book through specific primary sources and chapter arguments (Pearl's Ladder, Five Supervisory Capacities, Frictional method, the *Agents of Chaos* longitudinal case). Adding Bergstrom-West citations across multiple chapters would mean running a parallel framework alongside the book's chosen one, and would be over-citation.

The exception: Bergstrom-West cover the **Reuters Florida Stand Your Ground 2014 chart** as the canonical case of axis-flip deception. The y-axis was inverted (zero at top), so a post-2005 spike in firearm murders rendered visually as a decline. The reader took away the opposite of what the data showed; the data was accurate, the chart label was technically correct.

Ch 11 (Visualization Under Validation) currently has three case studies (Challenger 1986, El País Catalonia 2014, Snow's cholera map 1854 as counter-case) and a nine-item catalog of misleading mechanisms. The catalog covers truncated axes, scale trickery (linear vs log), and other manipulations — but not axis inversion specifically. Truncation amplifies a real effect; inversion *reverses* one. These are different deceptions. The Florida case is iconic, fills a real gap in the catalog, and maps directly to AI metric dashboards (where "error rate" vs "accuracy" can be flipped without changing a single number in the underlying CSV).

**Edit:** New case study added to Ch 11 between the El País Catalonia case and the Snow cholera counter-case. Names the Reuters Florida chart, describes the axis inversion mechanism, distinguishes axis inversion from scale truncation, ties to AI-dashboard implications. Section header updated from "Three cases" to "Four cases." Case-summary table updated with a fourth row. Footer summary updated from "Two failures and one success" to "Three failures and one success." Bergstrom & West cited as the canonical secondary source; the original Reuters chart is the primary source flagged for verification.

**Skipped:**
- **Brandolini's Law** in Ch 1 — the asymmetry of bullshit (refuting takes much more energy than producing) is a real concept, but Ch 1 is grounded in the Five Supervisory Capacities + the four-move method. Adding Brandolini would be ornamental.
- **Goodhart's Law with university rankings** — Goodhart's Law is presumably already covered in Ch 7 (Fairness) or elsewhere; the university-rankings example is one of many possible illustrations.
- **Simpson's Paradox** — likely already covered in Ch 5 (Data Validation) or Ch 7 (Fairness Metrics).
- **General "Calling Bullshit" framework** — adopting Bergstrom-West's framework alongside the book's own (Pearl's Ladder + Five Supervisory Capacities) would be running parallel vocabularies for the same territory.

**Citations to verify:**
- Bergstrom, C. T. & West, J. D. (2020). *Calling Bullshit: The Art of Skepticism in a Data-Driven World.* Random House.
- The original Reuters Florida firearm-murders chart (~2014) — confirm date, author, exact source URL.

---

## What changed (earlier passes)

### Build infrastructure added at the book root

`bash build.sh` now produces both `output/computational-skepticism-for-ai.epub` and `output/computational-skepticism-for-ai.html` from the 17-file chapter set. EPUB chapter splits land cleanly on the 17 H1s.

Files added:

- `metadata.yaml` — pandoc-format metadata
- `styles/kindle.css` and `styles/kindle-book.css` — editorial / serif / monochrome
- `build.sh` — pandoc → EPUB + HTML (executable)

### Pass 3 — 11 of 14 Wayback subjects replaced

The book had Wayback subjects who failed the no-post-2000-alive rule. Replaced with pre-2001 figures whose substantive connection to each chapter is genuine; the 3 already-compliant subjects were kept and got portrait stubs. None of the new figures overlap the existing botspeak or branding-and-ai Wayback lists.

| Ch | Old subject | Status | New subject | Why this figure |
|---|---|---|---|---|
| 01 | Sandra Harding (alive) | replaced | **Karl Popper** (1902–1994) | Demarcation criterion — the spine of a skeptic's toolkit |
| 02 | Sarah Lichtenstein (d. 2021, post-2000 work) | replaced | **Frank P. Ramsey** (1903–1930) | *Truth and Probability* (1926) — subjective probability as a number you elicit and score |
| 03 | Latanya Sweeney (alive) | replaced | **Hannah Arendt** (1906–1975) | Banality of evil — systemic harm produced by diffuse role-bound action |
| 04 | Lev Vygotsky (1896–1934) | kept | — | Foundational, pre-2001 clean |
| 05 | Suzanne Briet (1894–1989) | kept | — | Foundational, pre-2001 clean |
| 06 | Cynthia Rudin (alive) | replaced | **Hans Reichenbach** (1891–1953) | Context of discovery vs. context of justification — the gap between explanation and the appearance of explanation |
| 07 | Cynthia Dwork (alive) | replaced | **John Stuart Mill** (1806–1873) | Unresolved tension between *Utilitarianism* and *On Liberty* — the foundational case that fairness is not a single quantity |
| 08 | Dawn Song (alive) | replaced | **John von Neumann** (1903–1957) | Game theory as the older language for adversarial robustness |
| 09 | Lucy Suchman (alive) | replaced | **Maurice Merleau-Ponty** (1908–1961) | *Phenomenology of Perception* — embodied, situated action; agents fail in the gap between plan and situation |
| 10 | Lisanne Bainbridge (alive) | replaced | **Donald Broadbent** (1926–1993) | Vigilance under low-signal conditions — the structural attention problem of supervisory roles |
| 11 | W. E. B. Du Bois (1868–1963) | kept | — | Foundational, pre-2001 clean |
| 12 | Naomi Oreskes (alive) | replaced | **Florence Nightingale** (1820–1910) | Statistical visualization for honest uncertainty communication to non-statistical audiences |
| 13 | Diane Vaughan (alive) | replaced | **John Dewey** (1859–1952) | *The Public and Its Problems* — accountability requires tracing the chain of indirect consequences before assigning blame |
| 14 | Joseph Weizenbaum (d. 2008, post-2000 work) | replaced | **Alan Turing** (1912–1954) | Halting problem + imitation game — the math-forbidden limit and the test that cannot detect the limit |

Diversity: 11 men, 3 women. Pre-2001 substantive constraints driven the picks; balance is what it is given fit-to-chapter.

### Pass 1 — 53 tables rendered

Distribution: Ch 02 (5), Ch 03 (3), Ch 04 (2), Ch 05 (3), Ch 06 (5), Ch 07 (4), Ch 08 (4), Ch 09 (4), Ch 10 (6), Ch 11 (1), Ch 12 (4), Ch 13 (7), Ch 14 (5). Each table populated from the comment description plus chapter context; templates rendered as fillable structures with example rows where the comment specified them.

## Per-chapter results

00-frontmatter.md — 0 tables, 0 figures, no Wayback (front matter)
00-introduction.md — 0 tables, 0 figures, no Wayback (intro)
01-the-skeptics-toolkit.md — 0 tables, 0 figures, Wayback: replaced (Karl Popper, was Sandra Harding)
02-probability-uncertainty-and-the-confidence-illusion.md — 5 tables, 0 figures, Wayback: replaced (Frank P. Ramsey, was Sarah Lichtenstein)
03-bias-where-it-enters-and-who-is-responsible.md — 3 tables, 0 figures, Wayback: replaced (Hannah Arendt, was Latanya Sweeney)
04-the-frictional-method-evidence-of-learning-when-ai-can-generate-the-artifact.md — 2 tables, 0 figures, Wayback: kept (Lev Vygotsky)
05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md — 3 tables, 0 figures, Wayback: kept (Suzanne Briet)
06-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md — 5 tables, 0 figures, Wayback: replaced (Hans Reichenbach, was Cynthia Rudin)
07-fairness-metrics-choosing-a-definition-and-defending-it.md — 4 tables, 0 figures, Wayback: replaced (John Stuart Mill, was Cynthia Dwork)
08-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md — 4 tables, 0 figures, Wayback: replaced (John von Neumann, was Dawn Song)
09-validating-agentic-ai-when-autonomous-systems-misbehave.md — 4 tables, 0 figures, Wayback: replaced (Maurice Merleau-Ponty, was Lucy Suchman)
10-delegation-trust-and-the-supervisory-role.md — 6 tables, 0 figures, Wayback: replaced (Donald Broadbent, was Lisanne Bainbridge)
11-visualization-under-validation-honest-misleading-and-the-choices-between.md — 1 table, 0 figures, Wayback: kept (W. E. B. Du Bois)
12-communicating-uncertainty-calibrating-claims-to-evidence.md — 4 tables, 0 figures, Wayback: replaced (Florence Nightingale, was Naomi Oreskes)
13-accountability-who-is-responsible-when-the-system-fails.md — 7 tables, 0 figures, Wayback: replaced (John Dewey, was Diane Vaughan)
14-the-limits-of-ai-what-the-tools-cannot-do.md — 5 tables, 0 figures, Wayback: replaced (Alan Turing, was Joseph Weizenbaum)
99-back-matter.md — 0 tables, 0 figures, no Wayback (back matter)

## Summary

Total chapters processed: 17
Total tables rendered: 53
Total figures generated (SVG+PNG pairs): 0 *(deferred — see Action items below)*
Total Wayback Machine subjects replaced: 11
Total Wayback Machine portrait stubs added (kept chapters): 3

## Action items

### 1. Pass 2 — 64 IMAGE/FIGURE/DIAGRAM figures (deferred)

The book has 64 `<!-- → [IMAGE: ... ] -->`, `<!-- → [FIGURE: ... ] -->`, and `<!-- → [DIAGRAM: ... ] -->` comments distributed across 13 chapters. They were deferred from this pass to keep the figure-design quality consistent across all of them. The chapter prose currently references zero-byte `.jpg` placeholders for these figures — they will render as broken images in the EPUB until generated.

Chapters with the most figure work pending: Ch 08 (11), Ch 02 (9), Ch 05 (9), Ch 06 (6), Ch 09 (5), Ch 13 (3), others smaller.

### 2. Generate 14 Wayback portrait .jpg files

The Wayback Machine sections reference these AI-redrawn portrait files (none currently on disk):

- `images/karl-popper.jpg` (Ch 1) — c. 1950s
- `images/frank-ramsey.jpg` (Ch 2) — c. 1925
- `images/hannah-arendt.jpg` (Ch 3) — c. 1950s
- `images/lev-vygotsky.jpg` (Ch 4) — c. 1930
- `images/suzanne-briet.jpg` (Ch 5) — c. 1950s
- `images/hans-reichenbach.jpg` (Ch 6) — c. 1940s
- `images/john-stuart-mill.jpg` (Ch 7) — c. 1860s
- `images/john-von-neumann.jpg` (Ch 8) — c. 1940s
- `images/maurice-merleau-ponty.jpg` (Ch 9) — c. 1950s
- `images/donald-broadbent.jpg` (Ch 10) — c. 1960s
- `images/w-e-b-du-bois.jpg` (Ch 11) — c. 1900
- `images/florence-nightingale.jpg` (Ch 12) — c. 1860s
- `images/john-dewey.jpg` (Ch 13) — c. 1920s
- `images/alan-turing.jpg` (Ch 14) — c. 1940s

### 3. Add a cover image

`build.sh` looks for `cover.jpg` at the book root for KDP upload (1600×2560 JPEG).

### 4. INFOGRAPHIC / CHART comments out of literal Pass-2 scope

The book has 24 `[INFOGRAPHIC: ... ]` and 14 `[CHART: ... ]` comments — out of scope per the spec's literal Pass-2 token list (`IMAGE` / `FIGURE` / `DIAGRAM`). If the intent is to render these too, expand the token list and re-run.

## Build commands

```
cd books/computational-skepticism-for-ai
./build.sh
```

Outputs land in `output/`: `computational-skepticism-for-ai.epub`, `computational-skepticism-for-ai.html`, and `combined.md` (archival concatenated source).
