# Research Notes: Chapter 05 — Data Validation: Reconstructing the Epistemic Frame Behind a Dataset
**Corresponding chapter:** chapters/05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md · **Editor note:** notes/05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md · **Generated:** 2026-07-01

## Chapter summary
The chapter argues that procedural EDA is necessary but structurally insufficient for deployment-ready validation: it can only see what was written into the dataset, while the load-bearing work is interrogating the epistemic frame — what the recording instrument could and could not see. It opens with a silent-join failure (a 4% drop rate concentrated in one subpopulation), generalizes the blind spot into a taxonomy of structural assumptions (sampling, time-window, label, MNAR, feature-engineering, access-boundary), and supplies a six-step reconstruction procedure. Its central distinction: procedural EDA is evidence of competence; interrogation is evidence of understanding.

## A. Load-bearing claims → sources
- **Claim:** The MCAR / MAR / MNAR taxonomy of missing-data mechanisms is the correct frame for reasoning about why rows/values are absent. · **Source:** Donald B. Rubin, "Inference and Missing Data," *Biometrika* 63(3):581–592, 1976, DOI:10.1093/biomet/63.3.581 · primary · **Verdict:** CONFIRMED — Rubin (1976) is the origin of the missing-data mechanism typology. Nuance worth noting in prose: Rubin formally introduced "Missing at Random" (and "Observed at Random"); the now-standard labels MCAR/MNAR were consolidated by later literature (e.g., Little & Rubin, *Statistical Analysis with Missing Data*, 1987). The chapter's usage is standard and correct.

- **Claim:** A perceptual-effectiveness hierarchy of visual channels (position > length > angle > area > color, etc.) exists and is empirically grounded. · **Source:** William S. Cleveland & Robert McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *Journal of the American Statistical Association* 79(387):531–554, 1984, DOI:10.1080/01621459.1984.10478080 · primary · **Verdict:** CONFIRMED — This is the landmark ranked-accuracy study of elementary perceptual tasks. Promote the Fig 5.7 caption citation into the prose as the editor recommends.

- **Claim:** Perceived magnitude follows a power law of stimulus intensity (invoked as "Stevens' psychophysical power law gives us a framework"). · **Source:** S. S. Stevens, "On the Psychophysical Law," *Psychological Review* 64(3):153–181, 1957, DOI:10.1037/h0046162 · primary · **Verdict:** CONFIRMED as a real, correctly attributed result (S = kI^n). CONTESTED in application: Stevens' power law concerns magnitude estimation of sensory intensity; using it as the theoretical basis for *chart-channel* accuracy is a rhetorical bridge, not a direct finding. Cleveland & McGill is the load-bearing citation for graphical perception; Stevens supports the general psychophysics, not the specific channel ranking. Recommend the chapter cite both and not lean the channel hierarchy on Stevens alone.

- **Claim:** A dataset should be treated as a documented artifact whose provenance, collection process, and intended use must be interrogated — not a neutral recording. · **Source:** Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, Kate Crawford, "Datasheets for Datasets," *Communications of the ACM* 64(12):86–92, 2021, DOI:10.1145/3458723 (preprint arXiv:1803.09010, 2018) · primary · **Verdict:** CONFIRMED — Datasheets propose 57 questions across 7 categories (Motivation, Composition, Collection Process, Preprocessing/Cleaning/Labeling, Uses, Distribution, Maintenance). This is the canonical support for the "artifact, not recording" framing; recommend the chapter cite it explicitly to ground that thesis.

- **Claim:** Naturally occurring data (e.g., email) references the world outside its schema, so a schema-bounded validation misses the true access boundary. · **Source:** Chapter-internal argument; the concrete agent/email case echoes the *Agents of Chaos* study (see below). · secondary/original · **Verdict:** [UNVERIFIED] as a general law — "almost all naturally occurring data is not bounded by its schema" is asserted, not cited. It is defensible for reference-rich data but overreaches to self-contained tabular data (e.g., temperature readings). No single source establishes the universal claim; recommend the chapter narrow it or frame it as a spectrum.

## B. Resolving the editor's [verify] flags
- **[verify] Current scope of Great Expectations, Deequ, and successor tools before publication.** → PARTIALLY RESOLVED. Deequ is real and current: Sebastian Schelter, Dustin Lange, Philipp Schmidt, Meltem Celikel, Felix Biessmann, Andreas Grafberger, "Automating Large-Scale Data Quality Verification," *Proc. VLDB Endowment* 11(12):1781–1794, 2018, https://www.vldb.org/pvldb/vol11/p1781-schelter.pdf (open-source at github.com/awslabs/deequ; AWS Glue Data Quality is built on it). Great Expectations exists as an open-source Python data-validation framework (greatexpectations.io / github.com/great-expectations/great_expectations) but its exact current feature scope was not version-verified here — [UNVERIFIED] on "current scope"; a pre-publication check of the live docs is still needed.

- **Opening join-failure case (4% drop, one subpopulation, malformed IDs) — unsourced, load-bearing.** → [UNVERIFIED]. No public source; consistent with common silent-join pathologies but presented as a remembered war story. Needs an explicit "composite illustration" label or a `[verify]` tag per the editor's priority fix #2. NEVER cite as if sourced.

- **Stevens' power law — uncited.** → RESOLVED as a citation (Stevens 1957, above); flagged CONTESTED as applied to channel ranking.

- **Cleveland & McGill "landmark perceptual studies" — uncited.** → RESOLVED (Cleveland & McGill 1984, above).

- **Email-agent access-boundary story — presented as fact, unattributed.** → RESOLVED to a real source: the "Ash" agent is documented in *Agents of Chaos* (Shapira et al., 2026; see Sources). The chapter should attribute it rather than present it as a bare anecdote. Specific mechanics (Proton persistence, backups) belong to Ch.6's version and should be sourced there.

## C. Domain examples / cases (real, cited)
- **Datasheets for Datasets** (Gebru et al. 2021) — the operational instrument that turns "interrogate the frame" into 57 concrete questions; real, citable, directly supports the chapter's thesis.
- **Deequ** (Schelter et al., VLDB 2018) — real production data-quality-verification system at Amazon scale; supports the "procedural pass" tooling landscape and the [verify] flag.
- **Agents of Chaos / "Ash"** (Shapira et al. 2026) — the real 14-day live red-teaming study behind the email-agent access-boundary story; Ash reportedly blocked 14 consecutive prompt-injection variants. Use to attribute the agent case.
- **Rubin's missing-data mechanisms** (Biometrika 1976) — the canonical MNAR case (missingness depends on the unobserved value itself) that the chapter's "why are there exactly N rows" question operationalizes.

## D. Open flags (still [UNVERIFIED])
1. Opening 4%-join-failure case — no public source; label composite or tag `[verify]`.
2. "Almost all naturally occurring data is not bounded by its schema" — universalizing claim, no citation; narrow or frame as spectrum.
3. Great Expectations *current* feature scope — needs a live-docs check at publication time.
4. Step 5 ("trace one row back to source systems") assumes access that is often absent (inherited/third-party/foundation-model corpora); a limitation, not a citation gap — add the access caveat inline.

## Sources
Primary:
- Rubin, D. B. (1976). Inference and Missing Data. *Biometrika* 63(3):581–592. DOI:10.1093/biomet/63.3.581
- Cleveland, W. S., & McGill, R. (1984). Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods. *JASA* 79(387):531–554. DOI:10.1080/01621459.1984.10478080 · PDF: http://euclid.psych.yorku.ca/www/psy6135/papers/ClevelandMcGill1984.pdf
- Stevens, S. S. (1957). On the Psychophysical Law. *Psychological Review* 64(3):153–181. DOI:10.1037/h0046162
- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for Datasets. *Communications of the ACM* 64(12):86–92. DOI:10.1145/3458723 · preprint arXiv:1803.09010
- Schelter, S., Lange, D., Schmidt, P., Celikel, M., Biessmann, F., & Grafberger, A. (2018). Automating Large-Scale Data Quality Verification. *Proc. VLDB Endowment* 11(12):1781–1794. https://www.vldb.org/pvldb/vol11/p1781-schelter.pdf
- Shapira, N., et al. (2026). Agents of Chaos. https://agentsofchaos.baulab.info/ · arXiv:2602.20021

Secondary / tooling:
- Great Expectations (open-source data validation). https://greatexpectations.io/ · github.com/great-expectations/great_expectations [scope UNVERIFIED at publication]
- Little, R. J. A., & Rubin, D. B. (1987/2019). *Statistical Analysis with Missing Data.* Wiley. (consolidates MCAR/MAR/MNAR labels)
