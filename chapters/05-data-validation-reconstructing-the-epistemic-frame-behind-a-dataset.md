# Chapter 5 — Data Validation: Reconstructing the Epistemic Frame Behind a Dataset
*What the histograms can see, and the failures that live in everything else.*

## Learning objectives

By the end of this chapter, you will be able to:

- Explain why procedural EDA is necessary but not sufficient for deployment-ready data validation, and describe what the interrogation approach adds
- Execute the core procedural EDA workflow — distributions, missingness, correlations, outliers — and identify what each diagnostic does and does not reveal
- Choose appropriate marks and channels when constructing or reading a data visualization, and explain why position outranks color for quantitative data
- Identify at least six structural assumption categories that fail silently and are invisible to standard EDA
- Apply the six-step epistemic-frame reconstruction procedure to a dataset you did not create, including the prediction-lock
- Explain the access/boundary assumption and why the effective scope of a dataset is rarely identical to its schema
- Identify which validation work to delegate to AI tools, which to verify before trusting, and which to not delegate at all
- Trace a dataset failure backward to the structural assumption that produced it

## Prerequisites

Chapters 2–4. Chapter 3 (bias) is directly referenced — the bias-as-hidden-failure pattern returns in Glimmer 5.1. Familiarity with basic SQL join semantics is helpful but not required. No programming language is assumed; code examples use Python/pandas idioms, but the concepts transfer directly.

---

## Why this chapter

We have spent several chapters building apparatus for reading model outputs critically. This chapter steps earlier in the pipeline. Before the model, there is data. Before the data, there are choices — about what to record, what to include, how to join, where to stop. Those choices are the epistemic frame of the dataset, and they are almost never written down.

This chapter teaches you two things. First: how to actually do EDA — the mechanics of the procedural pass, the visualizations that matter, the code patterns that produce them, and most importantly what each diagnostic does and does not reveal. Second: how to do the work that comes after EDA, the work that determines whether a deployment will fail in production for reasons invisible from inside the data. We cannot do the second without doing the first, so we start there.

---

## The clean dataset that destroyed a deployment

I want to tell you about a dataset that destroyed a deployment.

The team that built the deployment didn't know the dataset destroyed it. They thought the model destroyed it. They retrained, tuned, regularized, tried different architectures. The deployment kept failing. The failures were soft — not crashes, not errors — just outputs that, in production, kept correlating with patterns nobody had designed for. The senior engineers got pulled in. They reread the original exploratory data analysis. The analysis still looked clean. No missing values to speak of. Distributions reasonable. No outliers. Nothing in the dataset, looked at by itself, explained the failure.

The failure was not in what the EDA looked at. The failure was in what the EDA didn't look at.

The dataset had been assembled from three source systems by joining them on a shared identifier. The join had a four-percent drop rate — rows that didn't match across all three sources got silently excluded. Four percent doesn't sound like a lot, and if it had been spread evenly across the population, it wouldn't have been. But it wasn't spread evenly. One specific subpopulation had inconsistent identifier formatting in one of the three source systems — a field entered slightly differently by the people who originally maintained that system years ago. Those rows disproportionately failed the join. They never made it into the merged dataset. The training set was systematically missing them. The model, trained on what was present, performed beautifully on what was present. Deployed against the full population, it performed predictably worse on the subpopulation it had never seen.

The EDA report had every plot it was supposed to have. The histograms were drawn. The summary statistics were tabulated. The missing-values check ran clean — because the rows that had failed the join were not "missing" in any sense the EDA could see. They simply weren't there. You cannot compute the missingness of rows that never existed.

<!-- → [FIGURE: Two-panel diagram. Left panel labeled "What EDA sees" — a single clean merged dataframe, histogram shapes, green checkmarks on missingness and outlier checks. Right panel labeled "What actually happened" — three labeled source system boxes (System A, System B, System C) with arrows converging into a merge operation; a gap is shown between the merge output and a dashed "expected full population" outline, annotated "4% dropped at join — never written, never visible." A callout bridging both panels: "EDA tools cannot detect rows that were never written." Placed immediately after the paragraph ending "you cannot compute the missingness of rows that never existed."] -->

So I want to ask you a question that is the question of this whole chapter. *Why are there exactly N rows in this dataset?* What was N supposed to be? What is the difference between what was supposed to be there and what is?

That single question, taken seriously, would have surfaced this entire failure mode in the first hour of working with the data. Nobody asked it. Why not? Because the procedure they had been taught for EDA didn't include it. The procedure was: histograms, correlations, missing-value analysis, summary statistics, outliers. Nothing about the row count. Nothing about the join. Nothing about *what came in versus what was supposed to come in*.

This is the gap I want to spend this chapter on. EDA is not a procedure. Or rather: EDA includes a procedure, and the procedure is fine, and you should run it. But the procedure is not the *work*. The work is interrogation. The dataset is being interviewed by a skeptical reader who wants to know what the recording instrument was, who deployed it, what it could see and what it couldn't see, and what choices were made before any data was written down.

Here is the move I am asking you to make. Treat every dataset as a recording made by a particular instrument under particular conditions. Then ask the questions you would ask of any recording. *What was recorded? What was not? Why? By whom? Under what assumptions about what was worth recording?*

---

## The procedural EDA pass — what it does, how to do it, and what it misses

Before we can interrogate the dataset, we need to look at it. The procedural pass is how we look. It is not optional. You cannot skip the histograms and go straight to the epistemic frame — you will miss things the histograms would have caught, and you will invent concerns the histograms would have dismissed. Run the procedure first. Then ask the harder questions.

I am going to walk through the procedural pass as a workflow, naming what each step produces and what it cannot produce. The goal is not a tutorial on any specific tool — tools rotate every few years and the concepts don't — but a principled understanding of the diagnostic logic that any tool is implementing.

### Step 0 — Understand the data type of each column

Before drawing anything, know what kind of data each column contains. This matters because the right visualization for a column depends entirely on its type.

**Numeric continuous** data (temperatures, salaries, ages, model confidence scores) can take any value in a range. Distributions are meaningful. Means and standard deviations are meaningful. Scatter plots and histograms are natural.

**Numeric discrete** data (counts, integers with a bounded range) looks numeric but behaves categorically when the range is small. The number of floors in a building is discrete. Treat small-range discrete columns like categorical for visualization purposes.

**Categorical nominal** data has no natural ordering — city names, product categories, blood types. Frequencies and proportions are meaningful. Ordering is not.

**Categorical ordinal** data has a natural ordering — survey ratings (Unsatisfied / Neutral / Satisfied), education levels, income brackets. The order carries information and should be preserved in any visualization.

**Temporal** data has an inherent ordering that is meaningful and often the most important thing about the column. Date and time deserve their own axis.

**Text** data is unstructured. It may contain embedded structure (phone numbers, identifiers, addresses) that is worth surfacing before treating the column as a text blob.

This classification is not always obvious. A column called `zip_code` looks numeric but is categorical nominal — arithmetic on zip codes is meaningless. A column called `score` may be continuous, ordinal, or a calculated composite depending on how it was produced. Read the schema documentation before classifying.

| Data Type | Examples | Natural Summary Statistics | Visualization Default | Key Questions to Ask |
|---|---|---|---|---|
| **Continuous numeric** | salary, temperature, model confidence score | mean, median, std, min/max, percentiles | histogram (30 bins), box plot | Is the distribution skewed? Are there outliers? Does the range make physical sense? |
| **Discrete numeric** | number of visits, floor count | frequency table, mode | bar chart (treat as categorical if range < ~20 distinct values) | Are there impossible values? Gaps in the range? |
| **Categorical nominal** | city, product category, blood type | frequency, mode, entropy | bar chart sorted by frequency descending | Rare categories? Misspellings suggesting dirty data? Unexpected values? |
| **Categorical ordinal** | survey rating, education level, income bracket | frequency, mode | bar chart sorted by natural order | Is ordering preserved in the encoding? Are any levels absent? |
| **Temporal** | date, timestamp | min, max, range, count-by-period | line chart (record count over time) | Gaps in coverage? Seasonality? Sudden distribution changes? |

*Before drawing a single plot, classify every column. The correct visualization depends entirely on the data type — and the most dangerous classification error is treating a categorical column as numeric.*

### Step 1 — Get the shape of the dataset

To start an EDA pass, ask an AI assistant:

> *"I'm loading a CSV file called [filename] into a pandas dataframe. Give me a Python snippet that prints the shape, inferred dtypes for all columns, the non-null counts via .info(), and a .describe() of all numeric columns. Add a brief comment after each call explaining what I'm looking for."*

The first question is always: how many rows, how many columns, and do the inferred types match what the documentation says? Type mismatches — a column that should be numeric but is read as string, usually because it contains a sentinel value like `"N/A"` — are one of the most common early warnings.

The `.describe()` output gives you, for each numeric column: count (non-missing rows), mean, standard deviation, minimum, 25th percentile, median, 75th percentile, maximum. Before you draw a single histogram, scan this table. Does the minimum make sense? Does the maximum? Is the mean close to the median, or are they far apart (suggesting skew or outliers)?

### Step 2 — Examine univariate distributions

For each column, you want to see the shape of its distribution. The right visualization depends on the data type.

**Histogram** for numeric continuous data. A histogram bins the values and shows counts per bin. The shape tells you whether the distribution is roughly symmetric, skewed, bimodal (two humps, suggesting two subpopulations), or contains a spike at a particular value (often a sentinel or default). The choice of bin count matters — too few bins hides structure, too many creates noise. Start with 20–30 bins and adjust.

To generate this with an AI assistant:

> *"Write a Python function using matplotlib that takes a dataframe and a list of numeric column names and produces one histogram per column with 30 bins, labeled axes, and a title showing the column name. Add a horizontal line at the mean and a vertical annotation showing the median."*

**Bar chart** for categorical data, sorted by frequency descending. Sorting by frequency makes it easy to spot rare categories that may warrant investigation.

> *"Write a Python snippet using pandas and matplotlib that plots a horizontal bar chart of value counts for the column [column_name], sorted by frequency descending, with count labels on each bar."*

**Box plot** as a complement to the histogram for numeric data. A box plot shows the median (center line), the interquartile range (the box), the whiskers (typically extending to 1.5× the IQR), and outliers beyond the whiskers as individual dots. The value of the box plot is that it compresses the distribution summary into a small space, making it easy to compare many columns side by side.

> *"Write a Python snippet that produces a side-by-side box plot for columns [col1, col2, col3] from a pandas dataframe, with each box labeled with its column name and a horizontal reference line at zero."*

What you are looking for: spikes at round numbers (often imputed defaults); impossible values (negative ages, salaries above what is physically plausible); bimodal distributions suggesting subpopulations the documentation doesn't mention.

### Step 3 — Examine missingness

Missing data is not a single thing. There are (at minimum) three structurally different reasons a value can be missing:

**Missing completely at random (MCAR):** The probability of a value being missing is independent of both the observed and unobserved data. A sensor failure that randomly drops readings. Safe to impute; unlikely to introduce bias.

**Missing at random (MAR):** The probability of being missing depends on other observed variables, but not on the missing value itself. Younger respondents in a survey skip the income question at higher rates. Conditional on age, the missingness is random. More complex to handle, but manageable.

**Missing not at random (MNAR):** The probability of being missing depends on the value itself. High earners are less likely to report their income. Sick patients leave a study before the final measurement. MNAR is the hard case — standard imputation produces biased estimates, and the bias is exactly in the direction you cannot measure. Standard EDA does not detect MNAR; you detect it by thinking carefully about who would not report this value and why.

To compute missingness by column and produce a sortable summary:

> *"Write a Python snippet that computes the number and percentage of missing values per column in a pandas dataframe, sorts by percentage descending, and prints only columns with at least one missing value."*

For a visual overview of missingness patterns across columns:

> *"Write a Python snippet using the missingno library that produces a matrix plot of missing values across all columns of a pandas dataframe, with a title and figure size of 12×6. Add a comment explaining what co-missing column patterns mean and what I should look for."*

The `missingno` matrix plot shows each row as a horizontal line and each column as a vertical stripe — white where a value is present, black where it is missing. The critical diagnostic is whether missingness in one column tends to co-occur with missingness in another column. If columns A and B are missing together in the same rows, either there is a structural data-collection reason (both come from the same source that sometimes fails) or there is a meaningful subpopulation that systematically does not have these values recorded.

<!-- → [FIGURE: missingno-style matrix visualization. A rectangular grid — rows on y-axis (each row is one dataset record), columns on x-axis (each column is one feature). Most cells are white (present). Two columns — call them "income" and "employment_status" — have heavy black vertical stripes (missing). Crucially, those stripes align: the same rows are missing in both columns. A callout box: "Co-missing: income and employment_status are absent in the same rows. This is structural — probably a shared data source that fails together, or a subpopulation that reports neither." A second column nearby has scattered individual black cells (random missingness). Caption: "Aligned stripes = structural missing pattern. Scattered dots = random missingness. The difference is the question: does missingness depend on something we can see, or something we can't?"] -->

### Step 4 — Examine bivariate relationships

A univariate distribution tells you about one column in isolation. A bivariate plot tells you how two columns relate. This matters for two reasons: understanding the data, and catching data-quality problems that only become visible when two variables are plotted together (a relationship that should exist but doesn't, or shouldn't exist but does).

**Scatter plot** for two numeric continuous variables. Each row in the dataset becomes a point; x-position encodes one variable, y-position encodes the other. If 10,000 rows overplot into an uninformative blob, add transparency or use a 2D density plot instead.

> *"Write a Python snippet using pandas and matplotlib that produces a scatter plot of [col_x] versus [col_y] with alpha=0.3 to handle overplotting. Add axis labels, a title, and a best-fit line using numpy.polyfit."*

**Correlation heatmap** for a high-level view of pairwise relationships across all numeric columns. Pearson correlation measures linear relationships; values near +1 or -1 indicate strong linear association, values near 0 indicate little linear relationship. Note the important caveat: Pearson correlation misses nonlinear relationships entirely. Two variables can be perfectly dependent (say, $y = x^2$) and have a Pearson correlation near zero.

> *"Write a Python snippet using seaborn that produces a correlation heatmap for all numeric columns in a pandas dataframe. Use the coolwarm colormap centered at 0, annotate each cell with the correlation value to 2 decimal places, and add a caption in the title noting that Pearson correlation only captures linear relationships."*

**Pair plot** for simultaneous pairwise visualization across multiple numeric columns. Each off-diagonal cell is a scatter plot; the diagonal shows the univariate distribution. Useful for small-to-medium column sets (up to about 8–10 columns before it becomes unreadable).

> *"Write a Python snippet using seaborn.pairplot for columns [col1, col2, col3, col4], with histograms on the diagonal and alpha=0.3 on scatter plots. Color the points by [categorical_column] if present."*

**Cross-tabulation** for two categorical columns:

> *"Write a Python one-liner using pandas that produces a normalized cross-tabulation of [col1] versus [col2], expressed as row percentages."*

<!-- → [FIGURE: Annotated scatter plot — x-axis "Age," y-axis "Salary." The main mass of points forms a loose upward-trending cloud (realistic age-salary relationship). Two isolated points are far upper-right (very high age and very high salary). A tight cluster of ~40 points sits at x=0 (age encoded as 0 to mean "unknown"). Three annotation callouts: pointing at the age=0 cluster: "Sentinel value — age=0 means 'not recorded,' not newborn. Not visible in the age histogram alone." Pointing at the two upper-right outliers: "Plausible outliers — verify against source data before removing." Pointing at the main cluster: "Expected pattern — positive age-salary relationship." Caption: "A scatter plot catches problems invisible to either univariate distribution alone. The age histogram showed no spike at zero because 40 points in a dataset of 10,000 is too small to flag there — but it's a structurally meaningful cluster."] -->

### Step 5 — Examine temporal patterns

If the dataset has a date or timestamp column, plot counts over time as the first temporal diagnostic. This catches: time periods with unusually few records (a source system was down, a batch job failed, a collection methodology changed); sudden distribution shifts (the product changed, the data schema changed, the population changed); seasonality that you need to account for in modeling.

> *"Write a Python snippet that converts [date_column] to datetime, resamples the dataframe to weekly record counts, and plots the result as a line chart with a title, axis labels, and a horizontal dashed line at the mean weekly count. Add a comment explaining what a sharp drop would mean."*

A sharp drop in record counts is always a finding. It may be benign (a holiday, a weekend effect in a business dataset). It may be critical (the system was down; the subpopulation affected by the downtime is now underrepresented).

<!-- → [FIGURE: Time-series line chart — x-axis "Week," y-axis "Records per week." The line runs roughly flat at ~800 records/week from early 2018 through February 2020. A sharp drop to ~200 records/week begins in March 2020 and persists through June 2020. The line recovers in July 2020 but settles at a slightly different level (~850/week) with a changed slope. Three annotations: "Drop: possible data collection disruption — what changed here?"; "Recovery: data resumes, but is the population the same?"; "Mean weekly count" marked as a dashed horizontal line. Caption: "Record counts over time are the first temporal diagnostic. A drop that aligns with a known external event (pandemic, system migration, policy change) is a finding — the subpopulation that stopped generating data during the gap may be systematically absent from your training set."] -->

### Step 6 — Examine outliers formally

The histogram and box plot will surface obvious outliers visually. Formal outlier detection uses either the IQR method or the Z-score method.

**IQR method:** A value is an outlier if it falls below $Q_1 - 1.5 \times IQR$ or above $Q_3 + 1.5 \times IQR$. This is the criterion the box plot's whiskers implement. It is robust to the presence of outliers because the IQR itself is not affected by extreme values.

**Z-score method:** A value is an outlier if its Z-score — the number of standard deviations from the mean — exceeds a threshold, typically $|z| > 3$. This method is sensitive to the presence of outliers in the mean and standard deviation calculation, which makes it less reliable when the dataset is already contaminated.

> *"Write a Python function that takes a dataframe and a column name and returns a dataframe of outlier rows using the IQR method (Q1 - 1.5×IQR and Q3 + 1.5×IQR as bounds). Print the count and percentage of outliers. Add a comment explaining why the IQR method is preferred over Z-score when the data may already contain outliers."*

The most important thing about outlier detection is not the detection — it is what you do next. Every identified outlier needs a decision: is this a data-entry error (a salary of $1,200,000 when typical salaries are $50,000–$200,000 might be a decimal-point error)? A legitimate extreme value (a CEO salary is legitimately high)? A sentinel value used to encode "unknown" or "not applicable"? The decision determines whether you remove, impute, cap, or retain the value.

<!-- → [FIGURE: Annotated box plot for a single "salary" column. Box spans Q1 to Q3. Whiskers extend to 1.5×IQR above and below. Three individual points lie above the upper whisker. Each point has a callout: Point at ~$1,200,000: "Verify: possible data-entry error — is this $120,000 with a misplaced decimal? Check source record." Point at $9,999,999: "Verify: likely sentinel — $9,999,999 is a common 'not applicable' encoding." Point at ~$750,000: "Plausible: C-suite compensation. Verify before removing." A fourth label on the box itself: "IQR — the box's height is the interquartile range, not affected by the outliers above it." Caption: "Outlier detection is triage, not removal. The IQR method flags the candidates. Domain knowledge makes the call."] -->

### What the procedural pass cannot see

The procedural pass is designed to surface pathologies visible in the data as written. It has a structural blind spot: it cannot see what was never written.

It cannot see rows that were dropped in a join before the dataset reached you. It cannot see the label's relationship to the construct it claims to measure. It cannot see features that are other people's model outputs baked in as inputs. It cannot see who could not generate data in this dataset. These are not failures of EDA tools — they are structural properties of what EDA is.

The next section gives you the theory for reading the visual output you have just produced. After that, the interrogation gives you the tools for what comes next.

---

## Marks and channels — the grammar of what EDA plots are doing

You have just run a procedural EDA pass. You have histograms, scatter plots, heatmaps, box plots. Now I want to step back and explain the visual logic underneath all of these — why certain representations work well and others mislead, and why knowing this matters for both reading and designing visualizations.

Every data visualization is built from two primitives: **marks** and **channels**.

A **mark** is a geometric primitive that represents an item or a relationship. Points, lines, and areas are the three fundamental mark types. In a scatter plot, each row in the dataset is a point. In a line chart, the relationship between consecutive measurements is encoded as a line. In an area chart, a quantitative amount is encoded as a filled region.

A **channel** is a visual property that encodes information about marks. Position (horizontal and vertical), size, color, shape, and orientation are channels. When you place a dot at a particular x and y position, both x and y are channels. When you color the dots by category, color is a channel. When you size the dots by a third numeric variable, size is a channel.

<!-- → [FIGURE: Two-panel illustration. Left panel labeled "The three mark types" — three clearly distinct geometric shapes with labels: a small solid circle labeled "Point (one item = one mark)"; a diagonal line segment labeled "Line (relationship between items)"; a filled irregular shape labeled "Area (magnitude as region)." Right panel labeled "Channels applied to a scatter plot" — a scatter plot of ~20 dots, with four annotation callouts using brackets and lines: one bracket spanning the x-axis: "Channel: x-position encodes a numeric variable"; one bracket spanning the y-axis: "Channel: y-position encodes a second numeric variable"; an arrow pointing at differently-colored dots: "Channel: hue encodes a categorical variable (no size ordering implied)"; an arrow pointing at differently-sized dots: "Channel: size encodes a third numeric variable (larger = more)." Caption: "Every visualization is marks + channels. Understanding which channels are active — and whether they are matched to the right data types — is how you evaluate whether a chart is telling the truth."] -->

### Why some channels are stronger than others

Not all channels are equal. Position is the most powerful channel for encoding quantitative data — human perception of position along a common scale is extremely accurate. Length is the next most powerful, which is why bar charts (where length encodes value) work well for comparing quantities. Area and color intensity are weaker: we perceive them inaccurately, especially when comparing non-adjacent elements.

Stevens' psychophysical power law gives us a framework for why. For length, perceived magnitude tracks physical magnitude almost exactly — your eye correctly judges that one bar is twice as long as another. For area, perceived magnitude is systematically compressed — you underestimate how much larger a big circle is compared to a small one. This is why pie charts and bubble charts require more cognitive effort than bar charts to read accurately: they rely on area rather than position or length.

<!-- → [CHART: Two-column ranked list — left column "For quantitative data (rank 1 = most accurate):" listing (1) Position on common aligned scale, (2) Position on non-aligned scales, (3) Length, (4) Angle / slope, (5) Area, (6) Color intensity / luminance, (7) Color hue — least accurate for quantities. Right column "For categorical data (rank 1 = best separation):" listing (1) Position, (2) Hue, (3) Shape, (4) Texture, (5) Size — weakest (implies ordering). Below both columns, a note: "Use the highest-ranked channel for your most important variable. The hierarchy is not arbitrary — it reflects measured perceptual accuracy." Caption: "Channel effectiveness hierarchy, based on Cleveland & McGill's landmark perceptual studies. Encode the variable that matters most with the channel people read most accurately."] -->

This ranking has direct consequences for EDA:

**Histograms use position and length.** The x-axis position of a bar encodes the value range; the height (length) of the bar encodes the count. This is why histograms are easy to read accurately — both active channels are high in the hierarchy.

**Scatter plots use position.** Two variables, two axes, position-only encoding. This is the gold standard for showing bivariate relationships. The reason scatter plots are so legible is that position is the best channel we have.

**Correlation heatmaps use color intensity.** Color intensity (luminance) is a weaker channel. This means heatmaps are better for quickly spotting extreme correlations than for judging whether a correlation of 0.43 is meaningfully different from 0.51. The heatmap is an overview tool; verify the specific values numerically.

**Pie charts use angle and area.** Both are weaker channels than position and length. This is why pie charts are less accurate than bar charts for comparing parts. A bar chart of the same data, with bars sorted by value, lets you compare parts much more precisely. The rule of thumb: use a pie chart only when there are two or three parts and the goal is to communicate a rough proportion, not to support precise comparison.

### The expressiveness principle and the effectiveness principle

There are two principles worth knowing by name.

The **expressiveness principle** says: match the channel to the data type. Quantitative data should use channels with a natural ordering (position, length, size, luminance). Categorical data should use channels without a natural ordering (hue, shape). Using size to encode a categorical variable — making one category's dots larger than another's with no quantitative meaning — implies an ordering that isn't there. This misleads the reader.

The **effectiveness principle** says: encode the most important variable with the most powerful channel. If your visualization encodes three variables, the variable that matters most to the reader's question should get position. A secondary variable can get color hue if it is categorical, or size if it is quantitative. The tertiary variable gets whatever is left.

<!-- → [FIGURE: Two side-by-side scatter plots — identical dataset (age on x, salary on y, department as a third variable). Left plot labeled "Expressiveness principle: satisfied." Dots colored by department hue (categorical → hue is a match). Legend shows department names, no implied ordering. Right plot labeled "Expressiveness principle: violated." Dots sized by department (categorical → size is a mismatch). Caption note: "Size implies 'Finance > Marketing > Engineering' — but there is no such ordering. The reader infers a quantity relationship that does not exist in the data." Overall caption: "Using size for a categorical variable is the single most common expressiveness violation. It misleads without lying — the data is all there, but the encoding creates a false impression of magnitude differences."] -->

### Applying this to EDA output

When you are reading your own EDA output — or someone else's — ask these questions:

What marks are being used? What does each mark represent? Is there a row-to-mark correspondence (one data point per mark) or an aggregation (each mark represents a group)?

What channels are being used? Are they matched to the data types they encode? Is the most important variable on the highest-ranked channel?

What is the chart not showing? Every visualization encodes some variables and omits others. A histogram of salary shows nothing about who earned those salaries. A correlation heatmap shows nothing about the temporal structure of the relationships.

The last question is the one that connects the procedural pass to the interrogation. The procedural pass tells you what the data looks like from the inside. The interrogation asks what the data is not showing you, and why.

---

## Hidden assumptions that hide in plain sight

Once you start asking these questions, a list of structural failures begins to emerge — failures that almost never get surfaced by procedural EDA, and almost always show up in deployment.

| Failure Mode | What it is | Why procedural EDA misses it | Example deployment consequence |
|---|---|---|---|
| **Sampling assumption** | Training data drawn from a more accessible subpopulation than the deployment target | EDA only sees what is present; it cannot compare the present data to the absent target population | Model performs well on easy-to-reach customers, degrades on the long tail it was never trained on |
| **Time-window assumption** | Training data covers a historical period that no longer reflects the deployment environment | EDA tools have no knowledge of what was true outside the dataset's time range | Model trained on 2019 data, deployed in 2022, confidently predicts patterns that have shifted |
| **Label assumption** | The label column measures an operational proxy, not the underlying construct of interest | EDA can show a label's distribution but cannot show the gap between the label and the construct | Re-arrest rate predicts re-arrest, not crime; click-through rate predicts clicks, not interest |
| **Missing not at random (MNAR)** | Values are missing because of the value itself | The missingness and the data appear independent from within the dataset; the pattern only becomes visible by reasoning about why someone would not report | Income missingness concentrated in high earners; survival data missing the patients who died; both produce biased models |
| **Feature-engineering assumption** | An input column is a calculated composite from an upstream model or analyst, not raw measurement | The column looks like data and has no missing values; its provenance is invisible unless documented | `customer_lifetime_value` encodes someone's old model's assumptions; when those assumptions break, so does the new model trained on them |
| **Access/boundary assumption** | The effective data universe extends beyond the schema — through references, links, or embedded content | EDA validates the records that are present; it cannot follow references to data outside the schema | An agent given access to an email corpus implicitly has access to everything the emails reference or quote |

*The six failures. Each has a structural reason it evades EDA. Memorizing the list matters less than being able to ask, for each column: why is this value here, and what is it not telling me?*

There is the **sampling assumption**. Was this sample drawn from the population the model is going to be deployed against? Often, no. The sample is *available* data — meaning the data that was easiest to collect, which means it skews toward the easy-to-reach end of every distribution it was drawn from. You train on convenience samples and deploy against the world. The world is wider than the convenience sample, and you find this out slowly.

There is the **time-window assumption**. What time period does the data cover? Is the deployment going to run in the same period? Almost never. AI deployments routinely train on historical data and deploy in a present that has shifted. The shift can be invisible if you're not watching for it.

There is the **label assumption**. What does the label actually measure? Re-arrest is not crime. A click is not interest. Survival is not health. Engagement is not value. The label and the construct you actually care about are usually different things, connected by a chain of operational decisions that somebody made long ago and didn't write down.

There is the **missing-data assumption**. Why is a value missing? Was it not recorded? Did it fail a join? The textbook hard case is *missing not at random* — where the reason a value is missing is correlated with the value itself. This is exactly the case standard EDA does not detect, because the procedural tools assume the missingness and the data are independent.

There is the **feature-engineering assumption**. The column called `customer_lifetime_value` is somebody's calculation. The calculation has parameters chosen by a human who is probably no longer at the company. You inherit the column and treat it like data, but it is not data. It is *somebody's model*, baked into your input layer.

There is the **schema-and-provenance assumption**. What was the source schema? What got renamed, recast, truncated, or merged in the pipeline that produced this dataset? Schema documentation, where it exists, is often out of date — written when the pipeline was built and never updated as the pipeline evolved.

And then there is the assumption that connects all the others and breaks deployments most strangely: the **access assumption**.

---

## The access assumption — and where the boundary really lives

I want to tell you a story about an agent.

An autonomous agent is deployed in an environment. The environment contains a corpus of email messages. The agent is instructed to perform a task that involves reading the email corpus to answer a query. The deploying team has thought carefully about the corpus. They have set up access controls. They have decided what data the agent should see. They have, they believe, drawn the boundary of the agent's data world, and the boundary is the corpus.

The agent runs. The agent answers the query. The answer contains, surfaced from the bodies of the messages, things the team did not authorize the agent to surface — phone numbers, addresses, fragments of credit-card numbers, references to internal documents that aren't in the corpus, conversation history that includes parties who never consented to be part of any of this in the first place.

This is not a model failure. This is a data-validation failure. The team thought they were validating *the corpus*. What they should have been validating was *the corpus and everything the corpus's contents reference*. Email messages, like almost all naturally occurring data, are not bounded by their schema. They contain, embedded in their content, references to data outside the schema. The boundary of the dataset is not the schema. The boundary is the schema *plus everything its contents touch*.

<!-- → [FIGURE: Concentric boundary diagram. A solid circle in the center labeled "Validated schema boundary — the email corpus (rows × columns the team inspected)." A larger dotted-circle surrounding it labeled "Actual data universe." Between the two circles, six labeled arrows point outward from the inner circle: "Referenced internal documents (linked by URL in message body)," "Embedded phone numbers and addresses (in message text)," "Fragment of a credit card number (quoted in reply chain)," "Third-party identities (people CC'd who never consented)," "Conversation history (prior thread quoted in each message)," "External attachments referenced by filename." The gap between the two circles is shaded and labeled "Validation blind spot — present in the data, invisible to schema-level validation." Caption: "The access boundary is not the schema. Naturally occurring data always references the world outside itself. Validating only what is formally in scope means the agent was given access to far more than the team intended — and no access control was violated."] -->

The validation move that catches this — the move I want you to make on every dataset you ingest — is to ask: *what is the boundary of this data, and how do I know?* And to insist on an answer more rigorous than "the schema." The boundary is the union of the schema and everything the schema's contents reference, link to, or imply.

---

## Reconstructing the epistemic frame — a working procedure

If you take what I have argued seriously, the procedure for validation changes. Not the procedural EDA — that part is fine, run it as you have always run it. The interrogation is what changes.

<!-- → [FIGURE: Six-step linear workflow diagram with labeled boxes connected by arrows. Box 1: "Read metadata → lock prediction" — annotation: "Catches surprises that later feel obvious." Box 2: "Run procedural EDA" — annotation: "Catches what is visible in the data as written." Box 3: "Test metadata against data" — annotation: "Catches gaps between claimed and actual scope, row counts, units." Box 4: "Ask what is NOT in the data" — annotation: "Catches dropped rows, absent populations, time gaps." Box 5: "Trace one row end-to-end" — annotation: "Catches pipeline surprises invisible at the aggregate level." Box 6: "Write epistemic frame, compare to prediction" — annotation: "The gap between prediction and finding is the learning event." A horizontal bracket under all six boxes: "The procedural EDA (box 2) reveals what is present. Steps 1 and 3–6 reveal what is absent, assumed, or beyond the schema." Caption: "Keep this as a checklist. Steps 3–6 are the work that EDA alone does not do."] -->

**Step 1 — Read the metadata, lock your prediction.** Before you run a single histogram on a dataset you did not create, read the metadata, the schema documentation, and any published description of how the data was collected. Write down, in your own words, what you predict the dataset's epistemic frame to be — what it claims to represent, how it was collected, what is excluded, and over what time period. *Lock your prediction.* The whole exercise depends on this.

**Step 2 — Run procedural EDA.** Histograms, correlations, missingness, outliers, temporal patterns. Note what shows up. The workflow from earlier in this chapter is the checklist.

**Step 3 — Test the metadata against the data.** Does the data look like what the metadata claims? Is the time range consistent? Are the units consistent? Does the row count match what the documentation implies? *Why are there exactly N rows?* If your prediction was that the dataset would contain a year of records, and the row count is consistent with maybe nine months, that gap is a finding. Pursue it.

**Step 4 — Ask what is not in the data.** Look for dropped rows in any join or merge. Look for fields documented but absent. Look for populations the documentation suggests should be present but aren't. Look for time periods with suspiciously few records.

**Step 5 — Trace at least one row, end to end.** Pick one at random. Follow its values back to the source systems. Document what you find. Doing this once, on a real dataset, is an education that survives the rest of your career — because almost every dataset you trace this way will turn up at least one surprise.

**Step 6 — Write the epistemic frame and compare to your prediction.** Write the frame as you now understand it — what the dataset actually represents, what is excluded, where the boundary truly lives. Then compare to your Step 1 prediction. The gap between what you thought before and what you found is the learning. Without the prediction-lock at the start, the gap doesn't exist; you only ever see what you finally arrived at, which feels obvious in retrospect, and you don't notice you've learned anything.

This is more work than procedural EDA. It is also, for any dataset you intend to base a deployed system on, the work that determines whether the deployment will fail in production for reasons invisible from inside the data.

---

## Strategic delegation in EDA

Now, you may be wondering: can I have an AI do some of this? You can, and you should — but only some of it, and the line matters.

**Delegate freely:** the mechanical work — procedural plots, summary statistics, missingness tables, outlier flagging, first-pass anomaly detection. These are well-defined and the AI will do them quickly and reasonably correctly. There is no reason to be precious about it.

**Verify before trusting:** any AI claim about what the data *means*. Any narrative about why a value is missing. Any assertion that a distribution is "normal" for this domain. The AI does not know your domain. It knows the math. The interpretation requires knowledge the AI does not have.

**Do not delegate at all:** the epistemic-frame reconstruction. The AI will produce a fluent reconstruction based on the documentation it can read, which is the same documentation you started with. It will sound thoughtful. It will look complete. But it cannot trace a row to its source system. It cannot identify what is missing because of a join issue you have not yet surfaced. The frame reconstruction is a trace of *your* engagement with the dataset. Delegating it produces a clean document that contains no information.

The procedural work is evidence of competence. The interrogation is evidence of understanding. The two are not the same, and only one of them is what makes the deployment safe.

| Category | What belongs here | Why |
|---|---|---|
| **Delegate freely** | Shape/dtype inspection, summary statistics (`.describe()`), missingness counts and matrix, univariate histograms and bar charts, outlier flagging via IQR or z-score, correlation heatmap, pair plots, temporal record counts | Well-defined operations; output is determinate; AI errors are immediately visible when you look at the result |
| **Verify before trusting** | Interpretation of why a value is missing, claim that a distribution is "normal for this domain," narrative explanation of a detected anomaly, suggested imputation strategy | Requires domain knowledge the AI does not have; errors are not obviously visible in the output — they sound plausible |
| **Do not delegate** | Epistemic-frame reconstruction (steps 1 and 3–6), prediction-lock and gap analysis, access-boundary scoping, row-tracing to source systems | The output of these steps is your engagement with the data, not the document it produces. A fluent AI-generated epistemic frame contains no information, because the AI started from the same documentation you did |

*The line is not about AI capability — it is about what the work produces. Mechanical outputs have determinate right answers the AI can reach. The interrogation produces understanding that only comes from you confronting the data yourself.*

---

## Glimmer 5.1 — The hidden-failure EDA

The exercise is intentionally adversarial. You are given a dataset designed to look clean — procedural EDA produces no flags — but containing at least three structural failures the procedural EDA does not surface. The course materials provide such a dataset; if you are reading this outside the course, construct one yourself by introducing a non-random missingness mechanism, a silent join failure, or an embedded label-process failure.

The exercise:

1. Run the procedural EDA workflow from this chapter. Produce the standard artifacts. Note that nothing flags.
2. *Lock your prediction:* given that the dataset was designed with hidden failures, what kind of failure do you predict? Where in the data? As specifically as you can name it.
3. Apply the six-step procedure. Find at least two of the failures.
4. Document the trace of how you found each one. What question did you ask that the procedural EDA did not?
5. Compare to the answer key (provided after submission). Note any failure you missed.
6. Write the gap analysis: what about your initial procedural pass made you not see the failure that the procedure surfaced?

The deliverable is the artifacts, the prediction, the trace, and the gap analysis. The grade is on the trace and the gap, not the count of failures found. A student who finds one failure and explains the structural reason their procedural pass missed it has shown more learning than a student who finds three by mechanical pattern-matching.

The bias callback: at least one of the hidden failures is a bias artifact in the Chapter 3 sense — a pattern that systematically affects one subgroup. Naming it requires the leverage analysis from Chapter 3, applied to the data layer.

---

## A note on tooling, and the aging risk

Every concrete EDA tool I might name in this chapter — for data-quality monitoring, missingness analysis, ETL pipelines, schema validation — every one of them will be partly obsolete within three years. pandas will still be there. The specific libraries above pandas will rotate. The cloud frameworks will rotate.

The tools rotate. The questions don't. This chapter is written around the questions, not the tools, on purpose. When you pick up the next-generation data-validation framework, the questions from the structural assumptions section and the six-step procedure transfer directly. The framework is the implementation. The questions are the methodology.

If you are reading this two years from now and the named tools are gone, do not panic. Ask the same questions in the new tools. The procedural EDA will be easier. The interrogation will be the same.

---

## What would change my mind

If a fully automated EDA pipeline emerged that reliably surfaced the kinds of structural failures described in this chapter — across diverse data sources, without per-dataset tuning — the "interrogation requires human engagement" framing would weaken. Current automated tools catch a subset of these failures (schema validation, statistical anomalies). They do not catch the access-boundary failures that animate the agent case. [Verify: current scope of Great Expectations, Deequ, and successor tools before publication.]

I do not have a clean diagnostic for unconsented data leakage through a corpus's boundary at scale. The email-agent pattern shows up easily in small examples and is hard to surface in large corpora without targeted search. The agentic deployment surface is making this worse, not better. I do not yet have a procedure that would find these reliably without some form of red-teaming. Chapter 9 returns to this from the agent-validation side.

---

## Synthesis — the artifact and its frame

A dataset is not a faithful recording of the world. It is an artifact — produced by someone, for some purpose, under some constraints, with some assumptions, and shaped at every step by what the recording instrument could and couldn't see.

Standard EDA produces artifacts. The work of validation produces *understanding of what those artifacts are evidence of*. The two are separate, and a great deal of harm has been done by people who confused one for the other — people who looked at clean histograms and concluded the data was clean, when what they really had was a dataset that was clean *of the things histograms can see*.

The marks-and-channels framework gives you the vocabulary to read visualizations critically: to ask whether the channel matches the data type, whether the most important variable got the most powerful channel, and what the visualization is structurally unable to show. The procedural EDA workflow gives you the mechanics to produce those visualizations systematically. The six-step interrogation gives you the discipline to ask what neither the visualizations nor the statistics can answer.

---

## Connections forward

We have validated the data. The model trained on the data produces outputs. Some of those outputs come with explanations. The question for the next chapter is: do the explanations tell us what the model is doing? Or do they make us feel like they do?

The most familiar version of explanation-that-feels-right-but-is-misleading is an autonomous agent reporting "deletion successful" — and when you ask what that report is actually evidence of, you find you have wandered into the same kind of question this chapter has been asking about data, only one layer up. Chapter 9 returns to this chapter's access-boundary problem from the agent-validation side. Chapter 14 closes the loop on the interrogation discipline as a whole.

---

## Exercises

### Warm-up

**1.** A dataset contains records of customer support tickets joined from two source systems — a ticketing platform and a CRM — on a shared customer ID. The documentation says the CRM contains 85,000 active customer records. The merged dataset has 79,400 rows. Write the three questions you would ask first to explain the gap, and identify which type of missing-data assumption each question is testing. *(Tests: row-count interrogation, missing-data taxonomy)*

**2.** You inherit a feature column called `risk_score` in a training dataset. The column has no missing values and a clean, plausible distribution. List three questions you must answer before using this column as a model input, and explain why each matters for deployment. *(Tests: feature-engineering assumption)*

**3.** Match each label to the construct it fails to measure directly, and in one sentence explain what operational decision creates the gap: re-arrest / crime; click-through rate / interest; 30-day hospital readmission / recovery; content engagement time / value. *(Tests: label assumption)*

**4.** A scatter plot shows age on the x-axis and salary on the y-axis, with dots colored by department. Identify the marks and the channels in this visualization. Then explain: (a) why position is used for age and salary rather than color, and (b) what would go wrong if you encoded department using dot size instead of hue. *(Tests: marks-and-channels framework, expressiveness principle)*

**5.** You examine a correlation heatmap of 12 numeric columns. Two pairs of columns show correlations above 0.85. A colleague says "those columns are highly related — we should drop one from the model." What additional information would you need before agreeing, and what does the heatmap not tell you that matters? *(Tests: understanding correlation heatmap limitations, distinguishing linear from nonlinear relationships)*

### Application

**6.** You are validating a dataset of medical imaging records intended for training a diagnostic model. The documentation says records span January 2018 through December 2022. When you plot record counts by month, you find a sharp drop in March 2020 that persists through June 2020, then a recovery with a different distribution pattern. Write a structured paragraph: (a) what hypotheses this pattern generates, (b) what you would check to test each hypothesis, and (c) what deployment implication each hypothesis would carry if confirmed. *(Tests: time-window assumption, distribution shift, interrogation procedure)*

**7.** An autonomous agent is given read access to a corporate Slack workspace to answer queries about project history. The access control policy specifies: public channels only, no direct messages, no files. Describe two ways in which the agent's actual data universe could extend beyond these boundaries without any access control being violated. For each, identify the validation step from the six-step procedure that would have caught it. *(Tests: access/boundary assumption, schema-content gap)*

**8.** A dataset has a column `income` with 18% missing values. You produce a missingno matrix and notice that `income` missingness co-occurs strongly with the `age < 25` subgroup. (a) Which missingness type — MCAR, MAR, or MNAR — is most consistent with this pattern? (b) What imputation approach would be appropriate, and what approach would introduce bias? (c) What additional investigation would you do to rule out the MNAR possibility? *(Tests: missing-data taxonomy, MCAR/MAR/MNAR distinctions, imputation reasoning)*

**9.** Apply the six-step interrogation procedure to a dataset you have access to — any real dataset will do, including a publicly available one. For each step, record (a) what you predicted before looking, (b) what you found, and (c) the gap. Submit your gap analysis. The size of the gap is not graded; the honesty of the prediction-lock is. *(Tests: full interrogation procedure, prediction-lock discipline)*

### Synthesis

**10.** The chapter distinguishes three categories of validation work: mechanical/procedural (delegate freely), interpretive (verify before trusting), and epistemic-frame reconstruction (do not delegate). A colleague argues that a sufficiently capable AI, given access to the source systems, could perform all three. Write a structured response: where do you agree, where do you disagree, and what is the crux of the disagreement? *(Tests: AI-delegation reasoning, understanding of what the interrogation actually produces)*

**11.** You are presenting a data validation report to a deployment review board. The procedural EDA is clean — no missing values, reasonable distributions, no outliers. But your interrogation identified one high-risk assumption: the training data covers only customers who completed onboarding, and the deployment will include customers who abandoned onboarding partway through. The board asks whether the clean EDA report is sufficient for approval. Write the response you would give. *(Tests: integrating procedural and interrogation findings, sampling assumption, deployment consequences)*

**12.** The chapter opens with a join-failure case where a four-percent drop rate caused systematic subpopulation exclusion. Design a data pipeline validation check that would have caught this before training began. Specify: (a) what the check measures, (b) what threshold would trigger a flag, (c) what information you need from outside the merged dataset to run it, and (d) what the check cannot catch even if it passes. *(Tests: translating interrogation concepts into concrete validation design)*

**13.** A data visualization colleague shows you a bubble chart where x-position encodes year, y-position encodes country GDP, bubble size encodes population, and bubble color hue encodes continent. Evaluate this visualization against the expressiveness and effectiveness principles. Identify one channel choice that is well-matched and one that is questionable. Suggest a specific alternative encoding for the questionable choice and explain why it would be more effective. *(Tests: marks-and-channels analysis, expressiveness and effectiveness principles)*

### Challenge

**14.** Choose a publicly documented AI deployment failure (not the examples from this chapter or Chapter 2). Reconstruct the epistemic frame of the dataset involved as best you can from public sources. Identify which of the six structural failure modes from the chapter best explains the failure. Argue your case with specific evidence, and identify what validation step, if run before deployment, would have surfaced the risk. *(Research and synthesis; tests ability to apply the chapter's framework to an unfamiliar case)*

**15.** The chapter claims: "A dataset is not a faithful recording of the world. It is an artifact." Write a two-page argument for why this framing matters for AI governance and regulatory compliance — specifically, for the question of who is responsible when a model trained on a flawed dataset causes harm. You do not need to take a legal position; you need to show how the artifact framing changes the question of where to look for accountability. *(Open-ended; tests conceptual transfer from technical to governance context)*

---

## Chapter summary

You can now do six things you could not do before this chapter.

You can execute the procedural EDA workflow — shape inspection, univariate distributions, missingness analysis, bivariate relationships, temporal patterns, outlier detection — and explain what each diagnostic does and does not reveal. You can read a data visualization through the marks-and-channels framework, identifying whether the channel encoding matches the data types and whether the most important variable received the highest-ranked channel. You can explain why position outranks color for quantitative data, and why using size to encode a categorical variable misleads the reader.

You can ask the question that procedural EDA does not ask — *why are there exactly N rows?* — and trace the answer into the source systems and join logic that produced the dataset. You can name the six structural assumption categories that fail silently and explain why each one is invisible to histograms and missingness checks. You can apply the six-step epistemic-frame reconstruction procedure, including the prediction-lock that makes the gap visible. And you can identify the boundary of a dataset — the union of the schema and everything its contents reference — and explain why that boundary is almost never the same as the schema alone.

The chapter's central distinction — procedural EDA as evidence of competence, interrogation as evidence of understanding — is not a methodological nicety. It is the difference between a validation report that tells you the data is clean of the things histograms can see, and a validation report that tells you what the data is actually evidence of.

---

*Tags: data-validation, eda, marks-and-channels, epistemic-frame, missing-data, distribution-shift, access-boundary, strategic-delegation*

---

###  LLM Exercise — Chapter 5: Data Validation: Reconstructing the Epistemic Frame Behind a Dataset

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** An epistemic-frame reconstruction of every dataset your agent depends on — training corpus, retrieval corpus, system-prompt examples, tool documentation it learned from — and one hidden-failure test designed to expose a structural assumption the agent's developers almost certainly made and never wrote down. The test, when run in Chapter 9, may produce one of your first formal cases.

**Tool:** Claude Project for the reconstruction. Claude Code if you have access to a real dataset (system prompt, retrieval corpus, fine-tuning examples) and want to run the procedural EDA pass on it.

---

**The Prompt:**

```
Continuing my Red-Team Casebook. My System Dossier and Bias-and-Leverage Brief are in the Project context. My Frictional journal infrastructure is set up.

This chapter teaches that procedural EDA (distributions, missingness, correlations, outliers) is necessary but not sufficient for deployment-ready validation. The structural failures live in the assumptions EDA cannot see — assumptions about scope, access, definition, joining, sampling. The six-step epistemic-frame reconstruction is the supplement.

For my agent, do four things:

1. DATA INVENTORY — List every dataset the agent depends on. Most agents depend on more than one; the inventory should cover:
   - Training data of the underlying model (usually opaque — name what you can infer about it)
   - Fine-tuning or RLHF data (if applicable)
   - Retrieval corpus (vector store, document base) if the agent does RAG
   - System prompt and few-shot examples
   - Tool documentation that shapes when the agent uses which tool
   - Logs of past interactions if the agent learns from them
   For each: what is it claimed to represent, who built it, what is its access scope?

2. EPISTEMIC-FRAME RECONSTRUCTION (six steps):
   For the most consequential dataset on the inventory, walk the six steps:
   - Step 1: What is this dataset claimed to represent?
   - Step 2: What does it actually represent (after looking at its construction)?
   - Step 3: What does it exclude — by sampling, by definition, by access boundary?
   - Step 4: What structural assumptions does its use embed?
   - Step 5: What hidden failures could each assumption produce in deployment?
   - Step 6: PREDICTION-LOCK: predict the failure pattern that would result if assumption #N breaks. Confidence?

3. STRUCTURAL ASSUMPTIONS AUDIT — Walk through the six categories of structural assumption that fail silently (the chapter names them — scope, sampling, definition, joining, time, access). For each, name the specific assumption your agent's most consequential dataset embeds, and rate how plausible the failure is.

4. HIDDEN-FAILURE TEST DESIGN — Pick the structural assumption you're most suspicious of. Design a test that would expose its failure if it is failing. The test should:
   - Construct an input that lies just outside the dataset's effective scope (the access/boundary assumption from the chapter)
   - Specify what the agent should do (refuse, escalate, ask) and what you predict it will actually do (proceed, hallucinate, confabulate a tool call)
   - Be runnable in Chapter 9 when you formally collect cases
   - Lock the prediction in your Frictional journal

Output a "Data Frame Audit" markdown file for my casebook with: the inventory, the six-step reconstruction, the assumption audit table, and the hidden-failure test specification (ready to run in Ch 9).

If I have access to the agent's system prompt or retrieval corpus, ALSO walk through the procedural EDA pass on it — distributions of token length, topical distribution of retrieved documents, missingness in metadata, etc. — and note where the procedural pass would have missed the structural failure.
```

---

**What this produces:** A "Data Frame Audit" file in your casebook folder, including a dataset inventory, a six-step epistemic-frame reconstruction, a structural-assumption audit, and a hidden-failure test ready to run.

**How to adapt this prompt:**
- *For your own project:* If you have zero access to the underlying training data (most foundation-model agents), the audit is still valuable — it documents the opacity itself, which is part of the validation finding.
- *For ChatGPT / Gemini:* Works as-is. Code Interpreter can run the procedural EDA on a system prompt or document corpus you upload.
- *For Claude Code:* Recommended if you have a system prompt file, RAG corpus, or finetuning JSONL — Claude Code will install pandas, run the EDA, and produce the diagnostic plots.
- *For a Claude Project:* Save the Data Frame Audit into the casebook folder.

**Connection to previous chapters:** Chapter 3 located bias in the pipeline. This chapter audits the data layer of that pipeline. Together they identify where the agent's beliefs about the world come from — and where those beliefs are most likely to be wrong.

**Preview of next chapter:** Chapter 6 probes what the agent says about its own actions. You'll apply explainability methods to the agent's natural-language self-reports and identify language-game mismatches between what the agent claims to have done and what the world actually shows — the technically-accurate-practically-misleading pattern that defines the Ash case.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Suzanne Briet** was asking what counts as evidence and how an object becomes a document — including her famous example of an antelope in a zoo — decades before anyone worried about how a dataset selects, frames, and silences. Here's a prompt to find out more — and then make it better.

![Suzanne Briet, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/suzanne-briet.jpg)
*Suzanne Briet, c. 1950s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Suzanne Briet, and how does her claim that documents are made by social context — not by inherent properties — connect to reconstructing the epistemic frame behind an AI training dataset? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Suzanne Briet"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain Briet's "antelope" example in plain language, as if you've never thought about what makes something a document
- Ask it to compare her account of how documents are made to how a modern training dataset selects and excludes
- Add a constraint: "Answer as if you're writing a chapter epigraph for a textbook on data validation"

What changes? What gets better? What gets worse?

