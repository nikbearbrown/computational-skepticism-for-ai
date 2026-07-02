# AI Wayback Machine — Insertion Report

**Book:** computational-skepticism-for-ai
**Status:** All 14 numbered chapters updated (01-14). Block appended at end-of-file. Frontmatter, introduction, and back-matter were skipped — they have no LLM Exercise block.

---

## Chapter → Figure Map

| # | Chapter | Figure | Anchor Concept |
|---|---|---|---|
| 01 | The Skeptic's Toolkit | Sandra Harding | Standpoint theory / strong objectivity |
| 02 | Probability, Uncertainty, and the Confidence Illusion | Sarah Lichtenstein | Calibration of subjective probability |
| 03 | Bias: Where It Enters and Who Is Responsible | Latanya Sweeney | k-Anonymity / discriminatory ad audits |
| 04 | The Frictional Method | Lev Vygotsky | Zone of Proximal Development / mediated learning |
| 05 | Data Validation | Suzanne Briet | Documentation theory / the antelope example |
| 06 | Model Explainability | Cynthia Rudin | Interpretable ML over post-hoc explanation |
| 07 | Fairness Metrics | Cynthia Dwork | Fairness Through Awareness / individual fairness |
| 08 | Robustness | Dawn Song | Adversarial ML / ML security |
| 09 | Validating Agentic AI | Lucy Suchman | Plans and Situated Actions |
| 10 | Delegation, Trust, and the Supervisory Role | Lisanne Bainbridge | Ironies of Automation |
| 11 | Visualization Under Validation | W. E. B. Du Bois | 1900 Paris Exposition data visualizations |
| 12 | Communicating Uncertainty | Naomi Oreskes | Manufactured doubt / public communication of science |
| 13 | Accountability | Diane Vaughan | Normalization of deviance / Challenger study |
| 14 | The Limits of AI | Joseph Weizenbaum | ELIZA / *Computer Power and Human Reason* |

No figure appears in both this set and the botspeak set.

---

## Diversity Summary

**Figures included:** Sandra Harding, Sarah Lichtenstein, Latanya Sweeney, Lev Vygotsky, Suzanne Briet, Cynthia Rudin, Cynthia Dwork, Dawn Song, Lucy Suchman, Lisanne Bainbridge, W. E. B. Du Bois, Naomi Oreskes, Diane Vaughan, Joseph Weizenbaum.

**Gender breakdown:** 12 women, 2 men.

**Geographic / national breakdown:**
- US-born or US-based: Harding, Lichtenstein, Sweeney, Rudin, Dwork, Suchman, Du Bois, Oreskes, Vaughan
- UK: Bainbridge
- Russia → USSR: Vygotsky
- France: Briet
- China → US: Song
- Germany → US: Weizenbaum

**Era breakdown (active period of cited work):**
- Pre-1950: 2 (Vygotsky d. 1934; Du Bois's Paris Exposition 1900, sociology peaked 1900s–1930s)
- 1950–1990: 4 (Briet 1951; Lichtenstein 1970s–80s; Bainbridge 1983; Suchman 1987; Weizenbaum 1966–1976)
  - That's actually 5 if Suchman is counted here. Boundary case.
- Post-1990: 7 (Harding's later work, Sweeney, Rudin, Dwork, Song, Oreskes, Vaughan)

**Disciplines represented:**
- Philosophy of science: Harding, Oreskes
- Decision research / cognitive psychology: Lichtenstein
- Computer science (privacy, fairness, security): Sweeney, Dwork, Song
- Educational / developmental psychology: Vygotsky
- Library and information science: Briet
- Machine learning interpretability: Rudin
- Anthropology of AI: Suchman
- Automation psychology / ergonomics: Bainbridge
- Sociology / data visualization: Du Bois
- Sociology of organizational accidents: Vaughan
- AI critique / philosophy of computing: Weizenbaum

**Race / ethnicity (separate axis):**
- White European/American: 7 (Harding, Lichtenstein, Rudin, Suchman, Bainbridge, Oreskes, Vaughan; Briet also white European)
- Jewish: 3 (Vygotsky, Dwork, Weizenbaum)
- Black: 2 (Sweeney, Du Bois)
- East Asian: 1 (Song)

**Flags:**
- Heavy female lean (12 of 14). Intentional — the historical record badly under-credits women in these fields, and every figure earns the slot on substance. Worth being aware of, not necessarily worth swapping.
- US-heavy (9 of 14). Latin America, sub-Saharan Africa (beyond Black American), the Arab world, South Asia, and Indigenous traditions are unrepresented. Strong alternates I considered and rejected for fit reasons: Paulo Freire (Brazil) for ch. 4, Humberto Maturana / Francisco Varela (Chile) for ch. 9. If you want a Latin-American swap, Freire for Vygotsky on ch. 4 is the cleanest substitution — Freire's anti-banking model maps to Frictional almost as well as ZPD does.
- Pre-1950 representation is light (2). Vygotsky and Du Bois carry the era. The book's subject is contemporary, so this is somewhat structural.

---

## Verification Suggestions

1. Spot-check Wikipedia titles. The two with non-obvious formatting:
   - **W. E. B. Du Bois** (with periods and spaces, that's the article title)
   - **Lev Vygotsky** (article title; sometimes seen as "Lev Semyonovich Vygotsky" in citations)
2. Run the chapter-3 prompt (Sweeney) yourself — her work is well-documented, so it's a good calibration of what the LLM will produce on a tight, lesser-known figure.
3. Double-check Cynthia Dwork's role in the "Fairness Through Awareness" paper — she's the lead author with Hardt, Pitassi, Reingold, and Zemel. The framing in the block treats her as introducing individual-fairness, which is accurate but slightly compresses the team contribution.

Logged at: `books/computational-skepticism-for-ai/wayback-machine-report.md`
