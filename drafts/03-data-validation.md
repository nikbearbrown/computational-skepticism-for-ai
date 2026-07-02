# Chapter 3 — Data Validation

*The histograms are clean. That is not the same as the data being clean.*

You ask an AI to assemble a dataset for you. Pull the customer records from the ticketing system, join them to the CRM on customer ID, drop the columns you don't need, hand me back one clean table. Thirty seconds later there it is: 79,400 rows, tidy dtypes, no obvious garbage. You ask for an exploratory pass — histograms, missing-value counts, a correlation heatmap, outlier flags. The AI writes the pandas, runs it, and reports back. The distributions look reasonable. Missingness is near zero. No wild outliers. The report is, by every visible measure, clean.

Here's what's actually happening. You are holding an artifact that has already made a dozen decisions on your behalf, and the validation pass you just ran was structurally incapable of seeing most of them. The join dropped rows. The dtypes were inferred, not verified. One of those "clean" columns is somebody else's model output wearing the costume of raw data. And the row count — 79,400 — is not a fact about the world. It is the *residue* of a process, and nobody wrote down what N was supposed to be.

The artifact looks done. What it does not announce is the frame it was built inside: what the recording instrument could see, what it silently excluded, and where the boundary of the data actually lives. That frame is the whole chapter. This is where two of the five supervisory capacities have to run at once — **Problem Formulation** (deciding what this dataset is even supposed to represent before you look) and **Plausibility Auditing** (hearing the wrong note in a clean report). The AI is superhuman at producing the histograms. It cannot supply the doubt about what the histograms can't reach. That gap is yours.

---

## The clean dataset that destroyed a deployment

Let me tell you about a failure. I'm going to flag it up front as a composite — it's built from silent-join pathologies I've watched play out more than once, not a single sourced incident — because a book about distrusting fluent, plausible stories cannot open with a fluent, plausible story it asks you to swallow whole. Treat it as an illustration of a mechanism, not as a cited case.

A team ships a model. It keeps underperforming in production. They assume the model is the problem — retrain, tune, regularize, swap architectures. Nothing fixes it. The failures are soft: no crashes, just outputs that, in the field, keep correlating with patterns nobody designed for. Eventually someone rereads the original exploratory analysis. It still looks clean. No missing values worth mentioning. Reasonable distributions. No outliers.

The failure was not in what the analysis looked at. It was in what the analysis *could not* look at.

The dataset had been assembled by joining three source systems on a shared identifier. The join had a four-percent drop rate — rows that didn't match across all three sources got silently excluded. Four percent, spread evenly, would have been harmless. It was not spread evenly. One subpopulation had inconsistent identifier formatting in one of the three systems — a field entered slightly differently, years ago, by whoever maintained that system. Those rows disproportionately failed the join. They never reached the merged table. The model trained beautifully on what was present and, deployed against the full population, performed predictably worse on the subpopulation it had never seen.

The missing-value check ran clean. Of course it did. The rows that failed the join were not "missing" in any sense the check could register — they simply weren't there. **You cannot compute the missingness of rows that never existed.** That single sentence is the crack in procedural EDA that this chapter widens into a doctrine.

So here is the question of the chapter: *Why are there exactly N rows in this dataset?* What was N supposed to be? What is the gap between what came in and what was supposed to come in? Taken seriously, that one question would have surfaced the entire failure in the first hour. Nobody asked it, because the procedure they'd been taught didn't include it. The procedure was histograms, correlations, missingness, outliers. Nothing about the row count. Nothing about the join.

This is the classical move underneath the whole chapter, and I'll name it: it's **Plato's Cave**. A dataset is not the world. It is shadows on the wall — a projection cast by a recording instrument under particular conditions. Procedural EDA describes the shadows with great precision. It tells you nothing about the fire, the objects, or the wall. The interrogation is the work of turning around.

---

## The procedural pass — what it does and what it structurally can't

I want to be fair to procedural EDA before I attack its limits, because the attack only works if you've actually run the procedure. Skip the histograms and you'll invent concerns the histograms would have dismissed and miss things they'd have caught. Run it first. Then ask the harder questions.

The procedural pass is a workflow, and the honest way to teach it is to name what each step *produces* and what it *cannot*.

**Step 0 — classify every column by type before drawing anything.** Continuous numeric (salary, temperature) gets histograms and box plots; means are meaningful. Discrete numeric with a small range behaves categorically — treat floor-count like a category. Categorical nominal (city, blood type) has no order; frequencies matter, ordering doesn't. Categorical ordinal (survey ratings) carries order you must preserve. Temporal data deserves its own axis. Text may hide structure worth surfacing. The dangerous error here is quiet: `zip_code` looks numeric and is categorical — arithmetic on zip codes is nonsense. Read the schema before you classify.

**Step 1 — get the shape.** How many rows, how many columns, do the inferred dtypes match the documentation? A column that should be numeric but reads as string — usually because it contains a sentinel like `"N/A"` — is one of the most common early warnings. Then scan `.describe()`: does the min make sense, does the max, is the mean far from the median (skew or outliers)?

**Step 2 — univariate distributions.** Histograms for continuous data reveal skew, bimodality (two subpopulations), or a spike at one value (often an imputed default). Bar charts for categoricals, sorted by frequency, surface rare categories and misspellings. Box plots compress the summary so you can scan many columns at once.

**Step 3 — missingness, and this is where the theory earns its keep.** Rubin's 1976 taxonomy is the correct frame, and it's worth stating precisely.[^rubin] *Missing completely at random (MCAR)* — the sensor randomly drops readings; safe to impute. *Missing at random (MAR)* — missingness depends on other observed variables (younger respondents skip income more); manageable once you condition on those. *Missing not at random (MNAR)* — missingness depends on the missing value itself (high earners hide income; dead patients stop reporting). MNAR is the hard case: standard imputation produces bias, and the bias points exactly where you can't measure. Procedural EDA does not detect MNAR. You detect it by reasoning about *who would not report this value, and why.* A `missingno` matrix helps you see co-missing columns — but seeing the pattern is not the same as knowing the mechanism.

**Steps 4–6 — bivariate relationships, temporal patterns, outliers.** Scatter plots catch problems invisible to either univariate distribution alone. Correlation heatmaps give an overview, with the caveat that Pearson only sees *linear* structure — two variables can be perfectly dependent ($y = x^2$) and correlate near zero. Record counts over time catch a source system that went down or a methodology that changed. IQR-based outlier detection flags candidates; and the point of outlier detection is never the detection, it's the *decision* that follows — data-entry error, legitimate extreme, or sentinel value.

Here's the trade-off the procedure makes, stated plainly. **It optimized for catching pathologies visible in the data as written, at the expense of everything that was decided before the data was written.** That's a real optimization — the visible pathologies are common and the tools catch them fast. But it means the procedure has one structural blind spot it can never close: it cannot see what was never recorded. It can't see rows dropped in a join. It can't see that a label measures a proxy instead of the thing you care about. It can't see that a feature is someone else's model baked in as input. Those aren't bugs in the tools. They are the definition of what the tools *are*.

[^rubin]: Donald B. Rubin, "Inference and Missing Data," *Biometrika* 63(3):581–592, 1976, DOI:10.1093/biomet/63.3.581. Rubin introduced "Missing at Random"; the now-standard MCAR/MAR/MNAR labels were consolidated in Little & Rubin, *Statistical Analysis with Missing Data* (Wiley, 1987).

---

## Marks and channels — why some plots tell the truth better

You just produced a stack of visualizations. Before the interrogation, understand the grammar underneath them, because reading a chart critically is the same skill as reading a dataset critically.

Every visualization is built from two primitives. A **mark** is a geometric thing that stands for an item — points, lines, areas. In a scatter plot each row is a point. A **channel** is a visual property that encodes information about marks — position, length, size, color, shape, orientation.

Not all channels are equal, and this is empirically established, not a matter of taste. Cleveland and McGill's 1984 study ranked the accuracy with which people read elementary perceptual tasks: position along a common scale is read most accurately, then length, then angle and area, with color intensity well down the list.[^cm] That's why scatter plots (position-only) are the gold standard for bivariate relationships, why bar charts (length) beat pie charts (angle and area) for comparison, and why a correlation heatmap (color intensity) is fine for spotting a screaming correlation but useless for telling 0.43 from 0.51 — verify those numerically. The general psychophysics behind "we perceive some magnitudes accurately and compress others" is Stevens' power law,[^stevens] but I want to be careful: Stevens is about sensory magnitude estimation, and using it as the *theoretical basis* for chart-channel ranking is a rhetorical bridge, not a direct finding. Cleveland and McGill is the load-bearing citation for graphical perception. Stevens supports the mood, not the ranking.

Two principles fall out. The **expressiveness principle**: match the channel to the data type — quantitative data to ordered channels (position, length, size), categorical data to unordered ones (hue, shape). Encode a category with size and you imply a magnitude ordering that isn't there; the data is all correct and the encoding still lies. The **effectiveness principle**: put your most important variable on your most powerful channel.

The transfer to auditing is direct. When you read anyone's EDA output — yours or a colleague's — ask what marks are used, whether the channels match the data types, whether the most important variable got the strongest channel, and, the one that connects to the interrogation: *what is this chart structurally unable to show?* A salary histogram shows nothing about who earned those salaries. A correlation heatmap shows nothing about time.

[^cm]: William S. Cleveland & Robert McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *Journal of the American Statistical Association* 79(387):531–554, 1984, DOI:10.1080/01621459.1984.10478080.
[^stevens]: S. S. Stevens, "On the Psychophysical Law," *Psychological Review* 64(3):153–181, 1957, DOI:10.1037/h0046162.

---

## The six assumptions that hide in plain sight

Once you start asking what the data isn't showing you, a taxonomy of silent failures emerges. Each one has a structural reason procedural EDA misses it.

| Failure mode | What it is | Why EDA misses it |
|---|---|---|
| **Sampling** | Training data drawn from a more reachable subpopulation than the deployment target | EDA sees only what's present; it can't compare present data to the absent target |
| **Time-window** | Training period no longer reflects the deployment environment | EDA has no knowledge of what was true outside the dataset's time range |
| **Label** | The label measures an operational proxy, not the construct of interest | EDA can show a label's distribution, not the gap between label and construct |
| **MNAR** | Values missing because of the value itself | Missingness and data look independent from inside the dataset |
| **Feature-engineering** | An input column is a calculated composite from an upstream model | The column looks like data and has no missing values; its provenance is invisible |
| **Access/boundary** | The effective data universe extends past the schema through references and links | EDA validates records present; it can't follow references to data outside the schema |

Three of these deserve the sharp version. **The label assumption**: re-arrest is not crime, a click is not interest, survival is not health, engagement is not value. The label and the thing you care about are connected by a chain of operational decisions somebody made and didn't write down. This is Hume's induction problem in work clothes — you're inferring the construct from a proxy that happened to correlate in the recorded past, and the correlation carries no guarantee forward. **The feature-engineering assumption**: `customer_lifetime_value` is not a measurement, it's a calculation, with parameters chosen by a human who probably left the company. You inherit the column and treat it like data; it is somebody's model, baked into your input layer, and when their assumptions break so does yours. And **the sampling assumption**: your sample is *available* data, which means it skews toward the easy-to-reach end of every distribution. You train on the convenience sample and deploy against the world, and the world is wider.

The instrument that turns "interrogate the frame" into something operational already exists: Gebru and colleagues' *Datasheets for Datasets* proposes 57 questions across motivation, composition, collection, preprocessing, uses, distribution, and maintenance.[^datasheets] If you want a checklist rather than a doctrine, that's the one to reach for.

[^datasheets]: Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, Kate Crawford, "Datasheets for Datasets," *Communications of the ACM* 64(12):86–92, 2021, DOI:10.1145/3458723 (preprint arXiv:1803.09010, 2018).

---

## The access boundary — where the data universe really ends

The access assumption is the one that breaks deployments most strangely, so it gets its own section.

An autonomous agent is deployed against a corpus of email. The deploying team thought carefully about that corpus, set up access controls, decided what the agent should see. They believe they've drawn the boundary of the agent's data world, and the boundary is the corpus. The agent runs, answers the query, and surfaces from the message bodies things the team never authorized — phone numbers, addresses, fragments of card numbers, references to internal documents not in the corpus, conversation history involving people who never consented to any of this. No access control was violated. This is a documented pattern: it echoes the "Ash" agent case from the *Agents of Chaos* live red-teaming study, which is where I'd send you for the real mechanics.[^chaos]

This is not a model failure. It is a data-validation failure. The team validated *the corpus*. They should have validated *the corpus and everything its contents reference*. Reference-rich data — email, documents, chat logs — carries pointers to data outside its own schema, so the boundary is the schema *plus everything its contents touch*. I want to bound this claim honestly, because the reference chapter overreaches it: this is true of reference-rich data, and it is *not* obviously true of a self-contained table of temperature readings, which doesn't point beyond itself the way an email does. Treat "data isn't bounded by its schema" as a property of a spectrum, sharpest at the email end, near-absent at the sensor-log end — not a universal law.

The validation move: ask *what is the boundary of this data, and how do I know?* — and refuse any answer as thin as "the schema."

[^chaos]: Shapira et al., "Agents of Chaos," 2026, arXiv:2602.20021, https://agentsofchaos.baulab.info/. Chapter 8 returns to this from the agent-validation side.

---

## Reconstructing the epistemic frame — the six-step procedure

If you take this seriously, the procedure for validating a dataset you didn't create changes. Not the procedural EDA — run that as always. The interrogation is what's new.

1. **Read the metadata, lock your prediction.** Before a single histogram, read the schema and any description of how the data was collected. Write down, in your own words, what you predict the frame to be — what it claims to represent, how it was collected, what's excluded, over what period. *Lock it.* The whole exercise depends on this step, because the gap between what you predicted and what you found is the only thing that makes the learning visible. Without the lock, whatever you finally arrive at feels obvious in retrospect and you never notice you learned anything.
2. **Run procedural EDA.** The workflow above is the checklist.
3. **Test the metadata against the data.** Does it look like what the metadata claims? Is the time range consistent? *Why are there exactly N rows?* If you predicted a year and the count is consistent with nine months, that gap is a finding — pursue it.
4. **Ask what is not in the data.** Dropped rows in any join. Fields documented but absent. Populations that should be present. Time periods with suspiciously few records.
5. **Trace at least one row end to end** — *where you have source-system access.* Pick one at random, follow its values back to the sources, document what you find. Doing this once on a real dataset is an education that lasts a career, because almost every trace turns up a surprise. The honest caveat: for inherited, third-party, or foundation-model data the source systems are unreachable, and then this step becomes "document the opacity," which is itself a finding.
6. **Write the frame and compare to your prediction.** What does the dataset actually represent, what's excluded, where does the boundary truly live? The gap from Step 1 is the learning.

This is more work than procedural EDA. For any dataset you'll base a deployed system on, it is the work that decides whether the deployment fails for reasons invisible from inside the data.

---

## What to delegate, what to verify, what to keep

Can you have the AI do some of this? Yes — but the line matters, and the line is not about AI capability. It's about what the work *produces*.

**Delegate freely:** the mechanical pass — plots, summary statistics, missingness tables, outlier flagging, first-pass anomaly detection. These have determinate right answers the AI reaches quickly, and any error is visible the moment you look at the output.

**Verify before trusting:** any AI claim about what the data *means*. Any narrative about why a value is missing. Any assertion that a distribution is "normal for this domain." The AI knows the math, not your domain, and its errors here don't look like errors — they sound plausible.

**Do not delegate at all:** the epistemic-frame reconstruction. Ask the AI to reconstruct the frame and it produces a fluent document based on the same documentation you started with. It will sound thoughtful and look complete. But it cannot trace a row to a source system, and it cannot find what's missing because of a join it never surfaced. The frame reconstruction is a trace of *your* engagement with the data; delegate it and you get a clean document containing no information.

This is the **solve–verify asymmetry** made into a tool. The AI solves — generates the plots, the stats, the fluent prose — faster than you ever could. What stays human is verifying what those artifacts are evidence *of*. The procedural work is evidence of competence. The interrogation is evidence of understanding. Only one of them makes the deployment safe.

The interesting trade-off in this whole discipline: procedural EDA optimizes for speed and coverage of visible pathologies; frame reconstruction optimizes for catching the invisible structural failures that actually break deployments. You need both, and the mistake — the one that has done real harm — is running the fast one, seeing it come back clean, and concluding the data is clean, when what you actually have is a dataset clean *of the things histograms can see.*

---

## Exercises

### BUILD — assemble a dataset with AI, then validate it before you trust it

Fight your own ownership bias. You made this; you want it to be clean.

**B1.** Ask an AI to assemble a dataset from at least two sources joined on a shared key (any real data you can reach; a public dataset is fine). Before running a single plot, **lock a prediction**: how many rows should the merged table have, and why? Then run the procedural pass. Does the actual row count match your prediction? Name the join's drop rate and check whether the dropped rows are spread evenly or concentrated in one subpopulation. *(Tests: row-count interrogation, silent-join failure, prediction-lock.)*

**B2.** For every column in your assembled dataset, classify its type (Step 0) and identify one column that *looks* like raw measurement but is actually a calculated composite or an inherited proxy. Write the three questions you must answer before trusting it as a model input. *(Tests: feature-engineering assumption, type classification.)*

**B3.** Have the AI produce the full EDA report and write the one-paragraph "the data is clean" summary it would hand a review board. Then write the paragraph that report structurally *cannot* contain — the frame it can't see. *(Tests: what the procedural pass cannot see, competence vs understanding.)*

### AUDIT — reconstruct the frame behind a dataset a colleague handed you; block the join failure

You have distance but no provenance. You weren't there for the decisions.

**A1.** Take a dataset a colleague handed you (or any dataset you did not create). Run the six-step reconstruction. For each step record (a) what you predicted before looking, (b) what you found, (c) the gap. The size of the gap isn't graded; the honesty of the prediction-lock is. *(Tests: full interrogation procedure.)*

**A2.** A merged dataset joins a ticketing platform and a CRM on customer ID. The CRM documentation says 85,000 active records; the merged table has 79,400 rows. Write the three questions you'd ask first, and for each, identify which missing-data mechanism (MCAR/MAR/MNAR) it's testing and what outside-the-dataset information you'd need to answer it. Then design the pipeline check that would have flagged the concentrated-drop failure *before* training — specify what it measures, what threshold triggers a flag, and what it still cannot catch even when it passes. *(Tests: block the join failure, MNAR reasoning, validation design.)*

**A3.** An agent is given read access to a corporate Slack workspace: public channels only, no DMs, no files. Describe two ways the agent's actual data universe extends past those boundaries with no access control violated, and name the reconstruction step that would have caught each. *(Tests: access/boundary assumption.)*
