# Chapter 11 — Visualization Under Validation: Honest, Misleading, and the Choices Between
*The dashboard is an argument. The design choices are yours.*

## Learning objectives

By the end of this chapter, you will be able to:

- Explain why visualization is an argument made through structural choices, not a transparent transmission of facts
- Identify the nine misleading visualization choices in the catalog, distinguish honest from dishonest uses of each, and apply the catalog to audit your own dashboards
- Use the perception hierarchy to choose the right visual channel for quantitative precision
- Apply the FT question taxonomy to match chart type to the question being answered
- Distinguish aleatoric from epistemic uncertainty and select an appropriate visualization technique for each
- Design an uncertainty visualization that makes the uncertainty visually equal in weight to the central estimate
- Build both an honest and a deliberately misleading version of a dashboard from the same data, and identify which design choices did the misleading work
- Explain why a dashboard that visualizes findings unfaithfully is a validation failure at the output layer, not merely a communication problem
- Apply the living-deck principle to communicate provisional analysis honestly

## Prerequisites

Chapters 2–10. Chapter 2's calibration material returns — calibration visualization is one of the cases examined. The validation methodology built across the book is what this chapter asks you to communicate faithfully.

---

## Why this chapter

Every prior chapter in this book has asked you to produce honest analysis. This chapter asks how you communicate it — and establishes that the communication is itself part of the validation. A dashboard that misrepresents valid findings is not a downstream problem. It is a validation failure at the output layer, and it is the supervisor's responsibility.

---

## Two dashboards built from one CSV

I want to tell you about two dashboards.

A team has finished a validation analysis on a deployed recommendation system. The findings are mixed. The system performs well on the typical user. It performs poorly on three specific subgroups. And the high-confidence outputs — the cases where the system is most certain — turn out, when you look at the calibration curve, to be overconfident at the top of the probability range. A complicated picture. A picture that needs to be communicated to a deployment partner who is non-technical, time-pressured, and going to make decisions based on what they understand.

Two team members each build a dashboard. They use the same CSV. The numbers are identical, byte for byte.

The first dashboard opens with a single, large, bold metric — *94% accuracy*. Underneath, smaller charts show the subgroup performance, but on truncated y-axes that visually compress the disparity. The calibration curve is over in a sub-tab labeled "advanced metrics," where most readers will not click. The color scheme is green for "good" and gray for "needs attention" — the disparity charts are gray.

The second dashboard opens with a panel showing performance on the overall user base alongside the subgroup performance, on consistent axes, with the disparity visible at first read. The calibration curve sits in the main view, with a banner noting that calibration is overconfident at high probabilities. The color scheme is uniform; the design does not redirect attention.

Same data. Same CSV. The first dashboard is misleading. The second is honest. And — here is the part you have to feel in your bones to understand the rest of this chapter — the deployment partner's response to the two dashboards is *predictably different*. They will leave the first dashboard reassured. They will leave the second dashboard with questions. The questions are appropriate. The reassurance is not.

I want to spend this chapter on what is happening between those two dashboards, because most engineers do not realize they are making this choice every time they build one.

---

## The medium is the message — McLuhan applied to the dashboard

There is a famous claim from Marshall McLuhan that gets quoted constantly and understood rarely: *the medium is the message*. \[Verify: McLuhan 1964, *Understanding Media.*\] McLuhan's idea, in working form, was that the *form* of a communication shapes its meaning before any specific content arrives. A spoken story is not a written story is not a televised story, and the differences are not because the words have changed but because the medium structures the encounter.

A dashboard is a medium. Its structure shapes what the reader takes from the data before the reader reads any specific number.

A dashboard that opens with a single bold headline metric communicates, by its structure, that the headline metric is the answer. The reader scans it, decides whether the answer is acceptable, and may not reach the supporting detail. The dashboard is *implicitly arguing*, by its form, that the headline is sufficient. The argument is made before the data is read.

A dashboard that opens with a panel of equally weighted views communicates, by its structure, that the picture is composite, that no single number suffices, that the reader is being asked to integrate. The reader's pace slows. They may take the time to read the calibration curve. The dashboard *implicitly argues*, again by form, that integration is required.

These are different arguments. The data is identical. The choice between forms is a choice about which argument to make.

This is the most important conceptual move in the chapter. *Visualization is not transparent communication of facts.* It is an argument, made through structural choices, about what the facts mean and how the reader should weight them. Engineers undercredit this. Engineers also produce many of the most misleading dashboards in deployment — often without intending to mislead, often building exactly the kind of dashboard their training would predict — because they do not realize that their structural choices are arguments.

---

## Step one: the question the chart is answering

A chart is not a way to display data. A chart is a way to answer one question with data. If you cannot state the question in a sentence, you do not yet know which chart to draw. This sounds obvious. It is violated in most dashboard builds, where the sequence is *here is a table of numbers, what should I do with it* rather than *here is the question, what data answers it*.

The Financial Times' *Visual Vocabulary* (Alan Smith and team) makes the connection concrete by sorting every chart type into nine question-families. \[Verify: FT Visual Vocabulary, available at ft.com/vocabulary.\] State the question, locate the family, pick from the charts within it.

<!-- FIGURE 11.0: Table — columns: Question family | What it answers | Chart types that belong here | Validation-context examples. Rows: Deviation (how far from a reference?), Correlation (how does one variable move with another?), Ranking (what is the order?), Distribution (how often does each value occur?), Change over time (what is the trend?), Part-to-whole (what proportion of the total?), Magnitude (how big, in absolute terms?), Spatial (where?), Flow (what moves where?). Designed as a chart-selection reference the student can pin above their workstation. -->

The nine families in brief:

**Deviation** — how far from a reference point (zero, a target, a baseline, a comparison group)? Bullet charts and diverging bars belong here. When you want to show that subgroup A performs 12 points below the overall average, this is the family.

**Correlation** — how does one variable move with another? Scatterplots. When you want to show that calibration error rises with predicted probability, this is the family.

**Ranking** — what is the order? Ordered bar charts, dot plots. When you want to show which features the model relies on most, this is the family.

**Distribution** — how often does each value occur? Histograms, box plots, violin plots, strip plots. When you want to show the spread of prediction confidence scores, this is the family.

**Change over time** — what is the trend? Line charts. When you want to show how accuracy has shifted over deployment months, this is the family.

**Part-to-whole** — what proportion of the total? Stacked bars, treemaps. Use cautiously; pie charts belong here but rarely communicate as clearly as their popularity suggests.

**Magnitude** — how big, in absolute terms? Bar charts with a zero baseline. When you want to show raw counts of model failures by category, this is the family.

**Spatial** — where? Maps. When the geography matters — when you need to show that failures cluster in specific deployment regions — this is the family.

**Flow** — what moves from where to where? Sankov and alluvial diagrams. When you want to show how users reclassified by the new model compare to the old, this is the family.

Andrew Abela's older decision tree (*Choosing a Good Chart*, 2009) collapses these into four — comparison, composition, distribution, relationship — and walks through binary choices. Either framework works. The point is the same: the chart is a function of the question. Pick the question first.

The mistake to avoid: starting from the data shape ("I have a table with three columns and twelve rows") and reaching for the default chart Excel offers. Excel does not know what you are trying to say.

---

## Step two: the perception hierarchy

Once you know the question and the chart family, you choose the *visual variable* — position, length, angle, area, color, volume — that encodes the answer. This is not a matter of taste. It is empirical. Some variables transmit quantitative information more accurately than others.

The hierarchy, established by Cleveland and McGill (1984) and reinforced in subsequent perception research, runs roughly from most accurate to least:

1. **Position along a common scale** — most accurate. Humans judge it with roughly 2% error. A dot plot where every point shares an x-axis is using this channel.
2. **Length** — 2–3% error. Bars on a shared baseline use this channel. Reliable.
3. **Angle and slope** — worse. Pie slices encode quantity as angle. Radar chart arms encode quantity as slope. Both are harder to read precisely than bars.
4. **Area** — 10–20% error. Bubbles and treemap rectangles encode quantity as area. Useful when relative magnitude is all that matters; unreliable when the reader needs to compare closely.
5. **Volume** — even worse. Avoid.
6. **Color saturation and hue** — weakest for quantity; fine for category. Color is excellent for distinguishing groups, poor for encoding "how much."

The implication for picking charts: when the answer is quantitative and precision matters, encode it as position or length. Reach for area, angle, or color only when precision does not matter, or when no other channel fits. This hierarchy has a sharp implication for uncertainty visualization, which we address in the next two sections.

<!-- FIGURE 11.A: The Cleveland-McGill perception hierarchy displayed as a ranked scale. Left axis: visual variable (position → length → angle → area → volume → color). Right axis: approximate error rate. A worked example for each: dot plot (position), bar chart (length), pie chart (angle), bubble chart (area). Caption: "When the answer is quantitative, choose the channel at the top of this list. The channel choice is not aesthetic — it determines how accurately the reader reads the number." -->

---

## Uncertainty has two faces

The standard visualization literature names one kind of uncertainty — the spread of the data — and stops. This is aleatoric uncertainty: the irreducible variability arising from sampling, natural variation, and stochastic processes. Error bars and confidence intervals are tools for it. It is what most guides mean when they say "show your uncertainty."

But there is a second kind. *Epistemic uncertainty* is the gap between what you know and what is true — uncertainty that arises from the limits of your data, your instruments, your proxies. \[Verify: Cairo, *Uncertainty and Graphicacy*; Bonneau et al. 2014.\] It is reducible in principle: better data, more sources, less biased instruments would close it. Most charts hide it entirely.

A poll showing 45.3% versus 44.5% with a margin of error of ±2.95% has aleatoric uncertainty *larger than the effect being reported*. A bar chart of "kidnapping rates" built from a database of news mentions has epistemic uncertainty that *swamps the data entirely* — the proxy is not the thing it claims to measure. Both kinds can wreck a chart. The tools for showing them differ.

A useful third source: the *visualization process itself* introduces uncertainty. How you bin a histogram, where you start the y-axis, what you call "high" — these are choices, and choices are sources of distortion the reader cannot see unless you surface them.

The chapter divides its remaining treatment across both faces. Sections below address each in turn.

---

## Showing the range — techniques for aleatoric uncertainty

Pick the technique by asking how the reader will use the answer, not by what is conventional in your field.

**Error bars (point estimate ± standard deviation or confidence interval).** Use when you are showing point estimates from samples, side by side, and the reader needs a quick visual check on overlap. Watch for: widely misinterpreted. Most readers think the true value is *somewhere inside the bar with equal probability*, which is not what either a standard deviation or a 95% CI means. Label what the bar actually is, every time. "Error bar = 95% CI" is not optional metadata.

**Confidence interval bands (shaded area behind a line).** Use when the trend is the message and uncertainty grows or shrinks across it — climate projections, fitted regressions, model drift estimates. Watch for: you have just encoded the most important number — the *amount* of uncertainty — in color saturation, one of the weakest perceptual channels. Readers cannot easily judge how wide the band is at any given x-value. Mitigate with explicit labels at key points, especially where the band widens.

**Fan charts (forecast widening into the future).** Use when projecting forward and the uncertainty grows with the horizon. Standard in central-bank inflation forecasts, hurricane forecasts, economic outlook reports. Watch for: the "cone of uncertainty" in hurricane forecasts contains 66% of past forecast errors, not 95%. The public frequently reads the cone as the physical size of the storm, or as a hard wall outside which it is "safe." \[Verify: Cairo's treatment of the hurricane cone backfire effect.\] Solution: pair with explicit text and consider gradient-line alternatives showing many possible paths individually.

**Box plot.** Use when comparing several distributions side by side and you care about median, spread, and outliers more than shape. Watch for: a box plot can hide bimodality. Two distributions with identical quartiles can look identical and behave nothing alike. If distribution shape matters, add a strip plot underneath.

**Violin plot.** Use when distribution *shape* matters — multimodal data, skewed distributions, anything unusual. Shows the kernel density on each side of a spine. Watch for: non-experts read it as a decorative vase rather than a probability density. Annotate the key features or pair it with a box plot inside.

**Strip plot / jittered dot plot.** Use when n is small enough to show every point. Position-based, perceptually honest — it sits at the top of the Cleveland-McGill hierarchy. Watch for: large n turns it into an illegible smear. Add transparency, or add summary marks (mean, median) on top.

**Quantile dotplot.** This is the technique most guides skip, and it is one of the most effective for communicating uncertainty to lay audiences. Twenty dots, of which four are filled, beats "20% chance" every time. The underlying principle comes from Gerd Gigerenzer's work on natural frequencies: "9 out of 10 women with breast cancer test positive; 99 out of 1,000 women without breast cancer also test positive" produces correct reasoning where "90% sensitivity, 9.9% false-positive rate" does not — even among physicians who should know better. \[Verify: Gigerenzer, *Natural Frequencies* research program.\] The quantile dotplot applies the same logic visually: position-based (best perceptual channel), count-based (natural frequencies), avoids percentage arithmetic that confuses most readers. Use for risk communication, lay audiences, any situation where the probability has to *land* with the reader rather than merely be reported.

**Hypothetical Outcome Plots (HOPs).** Animated frames, each showing one plausible draw from the distribution. Lets the reader *feel* the variability across frames rather than inferring it from a static shape. Watch for: static publication — they do not work on paper. Effective in interactive dashboards, unsuitable for reports.

**Gradient line plots (many paths, opacity scaled by likelihood).** Show that the future is many futures, weighted by probability. Watch for: Cairo's warning that overlaying possible storm sizes on possible paths in hurricane graphics produced a backfire effect, with some viewers concluding that scientists "knew nothing." More information made trust worse. Test with actual audiences before deploying.

A useful default for most real situations: the **quantile dotplot with a sentence of natural-frequency narration underneath** is the strongest combination available for communicating uncertainty to mixed or lay audiences. Position channel for perception, counts for cognition, narration for the reader who skims.

<!-- FIGURE 11.2: Side-by-side comparison of two uncertainty visualizations for the same data. Left: large bold central estimate with a thin error bar — headline reads "94.3% accuracy." Right: a range chart showing the full confidence interval at equal visual weight to the point estimate — headline reads "91–97% accuracy (95% CI)." Student should see how the visual hierarchy in the left version demotes the uncertainty to decoration. Anchor to the paragraph below on visual weighting. -->

**Make the uncertainty visually equal in weight to the central estimate.** A small error bar on a big bold number says: *this is the answer, with a quibble*. A central estimate displayed at the same visual weight as the uncertainty range says: *the uncertainty is part of the finding*. When the margin of error is large relative to the effect, the visual hierarchy must reflect that — which means the uncertainty must be as prominent as the estimate, not smaller and grayer.

**Avoid false precision.** A reported metric of 0.847291 with a confidence interval of ±0.05 is not a 0.847291 metric. It is a 0.85 metric. Round the central estimate to a precision the uncertainty actually supports. Reporting more decimal places than the data justifies is itself a small act of dishonesty — it implies certainty that does not exist.

**Test the visualization on a non-author reader.** Show the chart to someone who did not produce it. Ask them what they think it says. If their interpretation does not match the data, the visualization is not yet doing its job, no matter how much you like the design. This step is almost always skipped because it is uncomfortable. It is also the single most useful item on this list.

---

## Showing the trust — techniques for epistemic uncertainty

This is where guides go quiet, and where most published charts fail. Aleatoric uncertainty has standard visual tools. Epistemic uncertainty mostly has *practices*, not tools. But the practices are as important as the tools, and skipping them produces charts that look authoritative while being built on rotten data.

**Validate before you visualize.** Cairo's clearest rule, drawn from a FiveThirtyEight map of Nigeria "kidnapping rates" that turned out to be a map of *news stories about kidnappings*. The database was GDELT — the Global Database of Events, Language, and Tone — which counts media mentions, not events. The spike correlated with Boko Haram media coverage, not kidnapping rates. No disclosure of the proxy appeared anywhere in the chart. \[Verify: Cairo, *Ethical Infographics*, treatment of the GDELT Nigeria case.\] The chart conveyed the full visual authority of a chart built from ground truth, because it looked like all other charts, because charts do not carry labels that say "this proxy may not measure what the question asks."

The lesson: a chart based on a proxy you have never examined will mislead with the full visual authority of a chart based on truth. You have to check first whether the proxy carries the signal at all. A sticky note from the journalist Erin Simpson, quoted by Cairo, deserves to be above every dashboard build: *"Validate your own data. It's not true just because it's on a goddamn map."*

**Disclose the source, inside the chart.** Title is the question. Subtitle is the answer. Source line is the warrant. Treat the source line as part of the chart, not as footer decoration. Move it inside the chart frame. Make it specific: dataset name, year, URL or identifier. "World Bank data" is not a source; "World Bank Development Indicators, GDP per capita, 2023, data.worldbank.org/indicator/NY.GDP.PCAP.CD" is. \[Verify: Stephanie Evergreen and Ann K. Emery, *Data Visualization Checklist*.\]

**Disclose the methodology choices that affected the picture.** Did you bin? Did you smooth? Did you exclude? Did you normalize? A short methods note adjacent to the chart — three sentences, not a paper — separates a chart that survives a hostile read from one that does not. The choices are yours; the reader deserves to know what they were.

**Disclose what the data does not measure.** The Nigeria chart was titled as a chart of kidnappings. It was a chart of news stories about kidnappings. The reader had no way to see the gap. A title that names the proxy honestly — "News-story counts about kidnappings, 1985–2014" — would have changed the reading. Less compelling. More true.

**When uncertainty is too large, do not visualize.** The 2014 El País Catalonia poll: 45.3% no, 44.5% yes, ±2.95% margin of error. The difference is 0.8; the margin is 2.95. This is a tie. A bar chart showing two bars, one a hair taller than the other, is a lie of composition — the visual encodes a difference that is not there. The honest move is text, or a chart that makes the confidence interval visually larger than the effect. Sometimes the right chart is no chart.

**Hierarchy of disclosure.** Cairo's resolution of the "show everything / show what's necessary" tension:

- *Prominent in the chart* — when the uncertainty materially affects the answer. The Catalonia poll. A hurricane forecast for an evacuation decision. Your calibration curve when calibration failure is the finding.
- *In a clearly visible caption or footnote* — when the uncertainty does not change the conclusion but a serious reader needs it. A 60% vs. 30% finding with a ±3% margin.
- *In a methodology appendix* — when the uncertainty is small, the conclusion is robust, and the audience is general.

Hierarchy is not hiding. The test is whether a hostile reader could arrive at a different conclusion by knowing the uncertainty. If yes, the uncertainty belongs prominently in the chart.

<!-- FIGURE 11.B: A decision tree for uncertainty disclosure. Entry: "Does knowing the uncertainty materially change the conclusion?" Branch yes → show prominently in the chart. Branch no → second branch: "Would a serious reader need it to evaluate the work?" Branch yes → caption or footnote. Branch no → methodology appendix. Caption: "Hierarchy of uncertainty disclosure is not concealment. The test is the hostile reader." -->

---

## The deceptive visualization catalog

Let me make the catalog of choices visible, because once you see them named you will not unsee them.

<!-- FIGURE 11.1: Table — columns: Move | Honest use | Dishonest use | How to tell the difference. Rows: Truncated axis, Inconsistent axes across panels, Aggregation hiding distribution, Color asymmetry, Cherry-picked time windows, Scale trickery, Chartjunk/3D effects, Missing baseline, Labels that prejudge, Selective uncertainty visualization. Students should use this as a checklist when auditing dashboards. Insert via Datawrapper or image after authoring table content. -->

**Truncated axes.** A bar chart with the y-axis starting at 80 instead of 0 makes a small difference look large. Legitimate uses: when the relevant range really is narrow, when zero is not meaningful for the quantity being displayed (stock prices are routinely shown on truncated axes for good reason). Illegitimate uses: when the visual amplification implies a larger effect than the data supports. The chart looks the same in both cases. The choice is the difference.

**Inconsistent axes across panels.** Two charts side by side look comparable. They are not — because their y-axis ranges differ and the reader's visual comparison is invalid. This is one of the most common mistakes in dashboards built without intent to deceive: the engineer did not ask whether the visual comparison their layout was inviting was a valid one.

**Aggregation that hides distribution.** A single number — a mean, a median — that conceals a heavy-tailed or multimodal distribution. "Median performance is good" communicates the median and hides the tail. If the tail contains the catastrophic cases, hiding it is not summarization; it is concealment. The aggregation is doing rhetorical work.

**Color asymmetry.** Categorical data displayed with colors of unequal salience guides the eye toward where the designer wants attention and away from where they do not. The data has not changed. The salience has. The reader's gaze has been directed without their awareness.

**Cherry-picked time windows.** A trend chart over a window that begins at a local minimum and ends at a local maximum exaggerates the trend. The same data over a longer window may show a different story, or no story at all. This is why the living-deck principle (addressed below) requires the changelog to include the date range rationale.

**Scale trickery.** Linear axes for data that is naturally logarithmic; log axes for data that is naturally linear. Each compresses or expands different regions of the data. The choice can serve clarity or its opposite.

**Chartjunk and 3D effects.** Decorative elements that distort the perception of magnitude. 3D bar charts whose foreshortening makes near bars look bigger than far ones; pie charts with exploded slices; busy backgrounds that interfere with the data signal. Often introduced for aesthetic reasons; their effect is often to obscure. Tufte's term "chartjunk" names the category: any element of the display that does not transmit information about the data. \[Verify: Tufte 2001, *The Visual Display of Quantitative Information*.\]

**Missing baselines.** A chart showing a metric without showing the comparison metric — accuracy without random-baseline accuracy, performance without prior-system performance, a finding without the null. The reader cannot tell whether the finding is large or small. Without the baseline, everything looks like a finding. The Snow cholera map succeeded because it showed *all the pumps*, not just the Broad Street pump — the comparison was what made it evidence.

**Labels that prejudge.** Axis labels, legend entries, and headlines that frame the interpretation before the reader sees the data. "Accuracy boost from new model" on a chart comparing two models is a label that prejudges. "Accuracy: model A vs model B" is a label that does not. The data should make the argument; the label should name the variables.

**Selective uncertainty visualization.** Showing confidence intervals where they support the argument and omitting them where they would weaken it. Common, hard to detect, structurally the most dishonest of the bunch — because the data on uncertainty exists, and the choice to display it selectively is precisely the rhetorical move the engineer is making while telling themselves they are merely "presenting the data."

This is not a complete list. Tufte and Cairo each have longer ones, and both are worth reading. \[Verify: Tufte 2001, *The Visual Display of Quantitative Information*; Cairo 2019, *How Charts Lie*.\] The pattern across all of them is consistent: each is a *choice* that shifts the reader's interpretation. The engineer's job is to know which choices are being made and why.

---

## Four cases that teach the catalog

The rules are best learned from failures. Four cases, all real, all instructive.

**Challenger, January 1986.** Engineers had thirteen charts showing O-ring erosion data. The data contained a pattern — erosion was worse at lower launch temperatures — but it was not displayed in a way that made the pattern visible. Charts mixed qualitative text with quantitative displays, did not show the temperature-erosion relationship in a single visualization, and emphasized reassuring findings without presenting the overall risk profile. The chart that should have made the causal chain legible — cold temperature → harder rubber → longer seating time → blow-by → failure — was never drawn. The evidence existed. The visualization did not make it visible to a decision-maker under pressure. Management approved the launch. Seven astronauts died. \[Verify: Tufte, *Visual and Statistical Thinking: Displays of Evidence for Making Decisions*.\]

**Lesson:** when a decision is high-stakes and contested, the visualization must make the causal chain visible and the uncertainty salient enough that a manager cannot honestly read it as inconclusive.

**El País Catalonia poll, December 2014.** Headline: "Catalan public opinion swings toward 'no' for independence." Data: 45.3% vs 44.5%, ±2.95% margin of error. Effect smaller than the uncertainty. The chart showed two bars of different heights, encoding a difference that the data could not distinguish from noise. A reader leaving the chart believed one side was leading. A reader who knew the margin knew the chart was showing a tie.

**Lesson:** when uncertainty exceeds effect size, the chart is a story about noise. The honest story is "tie." Either visualize the confidence intervals so their overlap is obvious, or replace the chart with a sentence.

**Reuters, Florida Stand Your Ground, 2014.** A line chart showed firearm-related murders in Florida from 1990 to 2012, with the state's 2005 Stand Your Ground law marked as the inflection point. At first glance the chart appeared to show murders rising through the 1990s, leveling off, and then dropping precipitously after 2005 — apparently strong visual evidence that the law worked as advertised. The y-axis was inverted. Zero was at the top of the chart and high values were at the bottom, so the post-2005 *spike* in firearm murders rendered visually as a *decline*. Bergstrom and West, in *Calling Bullshit* (2020), use this as the canonical case for axis-flip deception: the data is accurate, the chart label is technically correct, the reader takes away the opposite of what the data shows. The mechanism is not in the catalog above as a named item — it is a relative of "scale trickery" but operates differently. Truncation amplifies a real effect. Inversion reverses one. The two are different deceptions. Both are available to anyone building an AI metric dashboard, where the orientation of "error rate" versus "accuracy" can be flipped without changing a single number in the underlying CSV. \[Verify: Bergstrom & West 2020, *Calling Bullshit*, ch. 7; the original chart was a Reuters news graphic.\]

**Lesson:** the orientation of the axis is itself a structural argument about which direction is "good." When the axis runs against convention, the chart can communicate the inverse of the data while remaining technically accurate. Honest practice: zero at the bottom for quantities where larger values mean more, with the direction-of-better stated explicitly in the title or caption.

**Snow's cholera map, 1854. (Counter-case.)** The reason this case is famous is that the map did three things simultaneously: showed spatial clustering of deaths, marked the Broad Street pump as the spatial center, and *included all other pumps for comparison*. The third move is what made it evidence rather than illustration. Snow let the reader rule out alternative explanations by making the comparisons visible inside the chart. The other pumps were not mentioned — they were shown. The visualization did the work.

**Lesson:** evidence-grade visualization shows what would have to be true for the conclusion to be wrong, not just what supports the conclusion.

| Case | What went wrong (or right) | Catalog item(s) that apply | Lesson in one sentence | What the honest version would have required |
|---|---|---|---|---|
| **Challenger 1986** | Engineers' temperature-failure plot omitted the cold-temperature region where the joint had not been tested; the chart shown to managers was therefore consistent with safe launch | Y-axis truncation; selective inclusion; missing-data invisible | A chart that excludes the region of doubt becomes a chart that endorses the decision | Display the full data range — including the region with no data — and label it explicitly as such |
| **El País Catalonia 2014** | A poll-result chart used a y-axis truncated to amplify a 5-point lead into a visual landslide; the impression was political, the data was not | Y-axis truncation; misleading scale | The data did not support the visual claim; the scale chose the conclusion | A zero-anchored axis or a labeled break, with the magnitude shown honestly |
| **Reuters Florida 2014** | A firearm-murder line chart with an inverted y-axis (zero at top) rendered a post–Stand Your Ground spike as a visual decline; the reader took away the opposite of what the data showed | Axis inversion (relative of "scale trickery"); convention violation | An inverted axis can communicate the inverse of the data while remaining technically accurate | Conventional orientation (zero at bottom for "more is more"), with the direction-of-better stated explicitly in the title |
| ✓ **Snow's cholera map 1854** | Mapping deaths to street addresses revealed a spatial cluster centered on the Broad Street pump — visually pinning a hypothesis the death tables alone could not | Spatial reference; matched scale; unambiguous symbol | The right visualization made the right hypothesis immediately legible | (Already met the standard) |

*Three failures and one success. The success shows that evidence-grade visualization has been possible for 170 years. The failures show that possibility is not the same as practice.*

---

## The Living Deck — provisionality as a visible argument

Validation analyses are usually presented as if they were finished. The dashboard, the deck, the report — they look polished, single-version, authoritative. This finished-looking form is itself a structural argument: *the analysis is complete; what you are reading is the answer*. Most validation analyses are not, in fact, complete. They are the current state of an ongoing process. The polished form misrepresents the analysis it presents.

A more honest form is the *living deck* — a presentation that exposes its own version history. Each version is dated. Each version has a changelog slide documenting what changed since the prior version and why. Old slides that have been superseded are retained, in a "previously" section, with a note about what they used to claim and what changed.

The structural argument the living deck makes, by form: *this analysis is provisional, the version you are reading is the latest state of an ongoing process, and the changes are themselves part of the work.*

This argument is not always welcome. Some adoption committees and procurement processes prefer the polished single artifact that hides the work. They are arguably wrong about what they prefer, because the polished artifact looks finished and is therefore harder to revise as new evidence comes in. The living deck, by exposing its own changelog, makes revision easier and more honest. The cherry-picked time window in the deceptive visualization catalog is, at the process level, addressed by the living deck: the changelog records when the time window changed and why.

The medium of provisional analysis is provisional itself. A finished-looking artifact misrepresents the analysis. This is a small operational point with a large structural implication: when the work is provisional, the form should say so.

The course's research project uses the living deck format throughout. The final presentation includes the changelog as the second-to-last slide. The changelog is evidence of the work — the visible track of how the analysis evolved. Removing it before final submission would erase the supervisory log.

<!-- → [IMAGE: A mock living-deck changelog slide. Title: "Changelog." Three rows with version dates (v1: [date], v2: [date], v3: [date]), a one-sentence description of what changed in each version, and a one-sentence reason why. Below the changelog: a "Previously" thumbnail showing an old claim that was superseded, struck through, with a note explaining what changed. The slide looks like a real slide from a validation deck — not a diagram about the concept, but an example artifact the student can copy. Caption: "The changelog slide is the second-to-last slide in every living deck. It is evidence of the supervisory process, not a confession of uncertainty. A deck without it is pretending to be finished."] -->

---

## A working sequence for picking and showing

Pulling the frameworks together into a single operational pass:

**1. State the question in one sentence.** Not "chart the database." "How has model calibration changed across six months of deployment?" Name the answer you need before touching the data.

**2. Locate the question in the FT taxonomy.** Change over time? Correlation? Distribution? If the question spans more than one family, the chart is probably answering more than one question, which is often a sign to split it.

**3. Check the data against the question.** Does the dataset measure what the question asks? If the database measures proxy behavior rather than the underlying phenomenon, either find a different dataset, change the question, or disclose the proxy prominently. Do not change the title to match the data and proceed as if nothing happened.

**4. Identify the aleatoric uncertainty.** Sampling error, distributional spread, forecast variance. Choose a technique from the range above, scaled to the audience: quantile dotplot for lay readers; confidence interval bands for domain experts who know how to read them; box plots for comparing distributions across groups.

**5. Identify the epistemic uncertainty.** Where did the data come from, what does it not measure, what proxies did it ride on, what choices did you make in cleaning and transforming it? Determine where in the hierarchy the disclosure belongs — prominent in the chart, caption, or appendix — and write it.

**6. Apply the perception hierarchy to encoding.** Position and length for quantitative precision. Color for category. Area only when magnitude, not precision, is what matters. Volume never.

**7. Test the chart against a hostile read.** Give it to someone who did not produce it. Ask them what they think it says. If their interpretation does not match the data, the visualization is not yet doing its job. This step is almost always skipped because it is uncomfortable. It is the most useful thing on this list.

<!-- → [INFOGRAPHIC: The seven-step working sequence as a vertical flowchart. Each step is a box with a short label and a decision fork where relevant. Step 1: State the question → Step 2: Locate in FT taxonomy → Step 3: Check data against question (decision: does data measure what question asks? No → change dataset, change question, or disclose prominently. Yes → continue) → Step 4: Identify aleatoric uncertainty → choose technique by audience type (lay: quantile dotplot; expert: CI band; group comparison: box plot) → Step 5: Identify epistemic uncertainty → place in disclosure hierarchy → Step 6: Apply perception hierarchy to encoding → Step 7: Hostile read test (decision: does non-author interpretation match data? No → redesign. Yes → ship). Caption: "This is the sequence, not a checklist. The decision forks at steps 3 and 7 are where most published charts quietly fail."] -->

---

## Glimmer 11.1 — Build the honest version, build the misleading version

I want to make a recommendation that some students find uncomfortable, and I want to make it anyway.

Take a finding from your work — a real result you have produced and would communicate to a deployment partner. Build the *honest version* first: a dashboard or static visualization that communicates the finding accurately, including uncertainty, including subgroup variation, including the limits of the analysis.

Then, using only the same data — no fabricated numbers, nothing invented — build the *misleading version*. Make the finding look better than it is, or worse than it is, or different in shape. Pick a direction. Lean into it. Use the choices from the catalog above. Truncate axes. Pick favorable color salience. Hide the calibration in a sub-tab. Make the central estimate bold and the error bars thin. Build it the way you'd build it if you were trying to mislead.

*Lock your prediction before building the misleading version:* (a) which design choices will you make to mislead? (b) which will be hardest, because the data refuses to be obscured? (c) which choices do you suspect you have already made unintentionally in earlier dashboards?

Then put the two side by side.

What you will see, if you do this honestly, is that the misleading version is *not difficult to build*. It is a small number of choices away from the honest one. Some of those choices you may have already made, unintentionally, in earlier work. The discomfort that comes when you recognize your own previous dashboards in the misleading version — that is the learning.

The deliverable is both versions, the prediction, the design-choice documentation, and the reflection. The *grade is on the reflection*. Specifically: which choices were the high-leverage ones? Which choices were almost invisible to a casual reader but had large effects on interpretation? Which choices, if reversed, would substantially reduce the misleadingness? A student who builds technically excellent dashboards but cannot identify which design choices did the misleading work has done the easier half of the assignment. The structural recognition is the harder half.

Building a misleading dashboard with intent is the most efficient way to learn what your default dashboards have been doing without intent. After you've done this once, you do not see dashboards the same way. You see the choices. You see the arguments the structures are making. You catch yourself about to truncate an axis for entirely defensible reasons, and you stop and ask whether the truncation is doing rhetorical work you did not intend.

<!-- → [IMAGE: Side-by-side thumbnail of the two-dashboard opening example. Left panel (misleading): large bold "94% accuracy" headline, truncated y-axis bar charts in gray, calibration curve labeled "Advanced Metrics" in a sub-tab the reader would not click. Right panel (honest): headline panel showing overall + subgroup performance on consistent axes at equal visual weight, calibration curve in the main view with a banner noting overconfidence above 0.85, uniform color scheme. An annotation layer labels the specific misleading choices on the left panel and the specific honest choices on the right. Caption: "Same data. Same CSV. The difference is five design choices, each taking about thirty seconds to make in either direction. The Glimmer asks you to make those choices deliberately, then name them." Intended to anchor the Glimmer for students who learn best from a visual anchor of the deliverable they are building.] -->

---

## Why this chapter is load-bearing

A note for the reader wondering whether this belongs in a curriculum that already includes a technical-writing course.

Engineering programs typically train students to write and present clearly. They typically do not connect that training to the validation methodology the engineer is operating under. The connection is the load-bearing claim of this chapter.

A technical-writing course teaches students to write clearly. A presentation course teaches students to present effectively. Neither typically teaches that the design choices in a dashboard are themselves arguments about what the data means, and that the validation methodology of this book extends through the visualization layer to the reader's interpretation.

This chapter's contribution: *the visualization is part of the validation*. A dashboard that visualizes findings unfaithfully is not a communication failure downstream of valid analysis — it is a validation failure that happens at the output layer. The supervisor's job extends to the visualization. The student who has taken a technical-writing course and this chapter produces dashboards that survive validation review. The student who has only the writing course produces dashboards that look polished and may, undetectably, mislead.

---

## What would change my mind

If a visualization standard emerged with strong empirical evidence that readers' interpretations matched the data — across diverse readers, audiences, and finding types — without bespoke-design work, the "every dashboard is an argument" framing would weaken to "most dashboards are arguments unless they conform to the standard." As of this writing, no such standard exists. The closest are domain-specific guidelines (e.g., FDA guidance for clinical trial visualizations), which are partial and not generalizable. \[Verify current scope of domain-specific visualization standards before publication.\]

If lay audiences turned out to read confidence interval bands as accurately as quantile dotplots in well-controlled studies, the uncertainty-technique rankings above would shift toward bands for the obvious convenience of static publication. The current evidence, from Hullman, Kay, and the HOPs literature, runs the other way; that is why dotplots rank above bands for lay communication here. \[Verify: Hullman 2020 review on uncertainty visualization.\]

I do not have a clean way to automatically detect deceptive design choices in a dashboard the way accessibility tools detect contrast issues. Some patterns — truncated axes, inconsistent scales — are mechanical and could be flagged by tooling. Others — color asymmetry, label prejudgment, selective uncertainty, cherry-picked time windows — require contextual judgment about whether the choice is honest. The general detection problem is open.

---

## Synthesis — the design choices are validation choices

*Every dashboard is making an argument, by structure, about what the data means.* The argument is made before any specific number is read. The choices that compose the argument are normative — they reflect a stance about what matters and how the reader should weight things. The engineer who treats those choices as neutral is mistaken about what they are doing.

The chart family narrows to one when the question is clear. The encoding channel follows the perception hierarchy. The uncertainty technique follows from who is reading and how consequential the answer is. The epistemic disclosures belong inside the chart, not in a footnote that hides in a methodology appendix, whenever the uncertainty could materially change the reader's conclusion.

This is not a counsel of despair. It is a counsel of *deliberation*. Make the choices on purpose. Document them. Invite revision. Build versions that test the boundaries of honesty by deliberately crossing them, so you know where the lines are.

A dashboard that visualizes findings unfaithfully is not a communication failure downstream of valid analysis. It is a validation failure that happens at the output layer. The validation methodology of this whole book — the prediction-locking, the gap analysis, the supervisory frame, the honest specification of what is robust and what is not — extends through the visualization layer to the reader's interpretation. The supervisor's job extends to the visualization. The design choices are validation choices. Make them on purpose.

The choices are normative. There is no neutral.

---

## Connections forward

The next chapter takes the same problem in writing. A dashboard tells a visual story. Validation findings also get communicated in writing, in proposals, in meetings, in conversations with people who will not look at any chart. There the question is harder, because there is no axis to truncate, no color to choose. How do you say what you don't know without losing the room? That is the next chapter's work.

The living-deck format introduced here recurs in the research project throughout the course. Chapter 14 closes the calibration arc and the book's supervisory thread.

---

## Exercises

### Warm-up

**1.** A colleague shows you a bar chart comparing two model versions. The y-axis runs from 91% to 96%. Model B's bar appears roughly three times the height of Model A's. The actual accuracy values are Model A: 92.1%, Model B: 94.3%. Calculate the ratio of the visual difference to the actual difference, and name the misleading choice in the catalog. What would the chart look like on a zero-baseline axis? *(Tests: truncated axis identification and quantification)*

**2.** You are reviewing a validation report that presents median latency as the headline performance metric. The distribution of latency values is right-skewed, with a long tail extending to 8 seconds for roughly 3% of requests. Write two sentences: one explaining what the median communicates accurately, and one explaining what it conceals and why that matters for deployment. *(Tests: aggregation-hiding-distribution)*

**3.** A dashboard shows three subgroup accuracy charts side by side. Group A: y-axis 70–100%. Group B: y-axis 85–100%. Group C: y-axis 60–100%. A reviewer says "the three groups look about the same." Name the misleading choice and describe the single change that would make the comparison valid. *(Tests: inconsistent axes identification and fix)*

**4.** A chart shows model accuracy over six months using a linear y-axis. The accuracy values range from 0.001% to 78%, with most of the action occurring between 1% and 78% across the first few weeks of deployment. Explain what a linear axis communicates about the early period of rapid improvement versus what a logarithmic axis would communicate. Which axis is more honest for this dataset, and why? *(Tests: scale trickery and the log-vs-linear judgment)*

**5.** You need to communicate a 20% probability of model failure to a hospital committee with no statistical training. Design two displays of this probability: one using a percentage figure with a confidence interval bar, and one using a quantile dotplot with natural-frequency narration. Explain which would produce more accurate comprehension and why, drawing on the perception hierarchy and Gigerenzer's natural-frequencies research. *(Tests: quantile dotplot and natural-frequency concepts, uncertainty technique selection)*

### Application

**6.** You are handed a dashboard built by another team to support a deployment decision. Using the nine-item catalog from the chapter, conduct a structured audit. For each item: note whether it is present, assess whether its use is honest or misleading in this context, and flag the two highest-risk choices for the deployment partner's decision. Submit your audit as a structured table. *(Tests: full catalog application to a real artifact)*

**7.** A model's accuracy on the majority subgroup is 93% ± 2% (95% CI). On the minority subgroup it is 81% ± 9%. Build — on paper or in a tool of your choice — two versions of a single chart that shows both results. Version 1: maximize the impression that the model performs consistently. Version 2: make the disparity and the uncertainty fully visible. Annotate each design choice you made in each version and identify which catalog item each one corresponds to. *(Tests: deliberate honest/misleading construction exercise)*

**8.** You have presented a validation analysis to a deployment partner. They respond: "The 94% accuracy looks great — we're ready to proceed." You know from your analysis that the calibration is overconfident above 0.85 probability and that one subgroup underperforms by 12 points. The partner did not ask about either issue. Describe the visualization and communication changes you would make before the next meeting, and explain why the current dashboard, though factually accurate, has produced a misleading interpretation. *(Tests: visualization-as-validation-failure concept, practical redesign reasoning)*

**9.** A trend chart shows model accuracy improving steadily over 6 months. The chart's x-axis begins in April. You know the model was retrained in March after a significant performance drop. The April-to-October window shows only the recovery, not the drop. Name the misleading choice, explain what a reader would infer versus what the full data shows, and describe what the honest version of the chart would look like. *(Tests: cherry-picked time window, living-deck concept)*

**10.** A colleague argues: "My dashboard is accurate. Every number in it is true. If the reader draws wrong conclusions, that's a communication problem, not a data problem." Write a two-paragraph response that addresses this argument directly, using the McLuhan frame from the chapter and at least one specific example from the deceptive visualization catalog. *(Tests: dashboard-as-argument and McLuhan concepts)*

### Synthesis

**11.** The chapter claims: "A dashboard that visualizes findings unfaithfully is a validation failure at the output layer, not a communication failure downstream of valid analysis." Write a two-paragraph argument defending this claim to an engineer who believes that visualization is a separate concern from analysis — that as long as the numbers are right, the presentation is a communication problem, not a validation problem. Your argument should connect to at least two concepts from earlier chapters. *(Tests: chapter's load-bearing claim, cross-chapter integration)*

**12.** You are designing a dashboard to communicate ongoing model monitoring results to a non-technical governance board that meets quarterly. The model has: overall accuracy 91%, three-subgroup breakdown (89%, 90%, 78%), a calibration curve that is overconfident above 0.8, and a distribution shift metric that has been slowly increasing for two quarters. Design the dashboard layout — not the implementation, the layout and the structural argument it makes. Specify: (a) what appears in the main view and why, (b) what appears in secondary views, (c) how uncertainty is displayed, including which technique from the chapter you would use and why, (d) how the living-deck principle is applied, and (e) what structural argument your layout makes before a single number is read. *(Tests: full chapter integration applied to a realistic governance communication problem)*

**13.** The chapter recommends building a deliberately misleading version of your own dashboard as a learning exercise. A student objects: "This feels like practicing deception." Write a response that addresses the objection directly, explains the actual learning objective of the exercise, and connects it to the chapter's central claim about what engineers fail to see in their own default dashboards. *(Tests: understanding of the exercise's purpose and the chapter's central claim)*

### Challenge

**14.** Find a published data visualization — from a news outlet, a research paper, a company report, or a government publication — that uses at least three of the nine misleading choices from the catalog. Annotate it: identify each misleading choice, explain what a reader would infer versus what the underlying data supports (you may need to find the underlying data), and build a sketch of the honest version. This exercise is not about finding a dishonest actor; many misleading visualizations are built without intent to deceive. The goal is to identify the structural choices, not to assign blame. *(Research and analysis; tests catalog application to real-world artifacts)*

**15.** The chapter ends by saying "the choices are normative — there is no neutral." Write a short essay (600–800 words) arguing either for or against this claim. If you argue for it, your essay should address the strongest objection: that some visualization choices are purely technical (e.g., choosing a bar chart over a pie chart for categorical data) and carry no normative content. If you argue against it, your essay should address the strongest evidence for the claim: that structural choices have predictable, measurable effects on reader interpretation regardless of intent. *(Open-ended; tests philosophical engagement with the chapter's central claim)*

---

## Chapter summary

You can now do six things you could not do before this chapter.

You can name the mechanism by which a dashboard makes an argument before any specific number is read — the McLuhan move applied to the dashboard as medium — and explain why structural choices are normative, not neutral. You can state the question a chart is answering, locate it in the FT question taxonomy, and use that location to choose among chart families before touching the data. You can apply the perception hierarchy to choose the encoding channel that best serves quantitative precision. You can distinguish aleatoric from epistemic uncertainty and select the visualization technique appropriate to each — quantile dotplots for lay audiences, confidence bands for expert ones, natural-frequency narration for both — with the disclosure hierarchy guiding where the uncertainty appears in the display. You can audit a dashboard using the nine-item catalog and identify which choices are being made and whether they are honest. And you can build both an honest and a deliberately misleading version of a visualization from the same data, then identify the high-leverage choices that made the difference — the exercise that makes visible what your default dashboards have been doing without your awareness.

The chapter's central claim: the dashboard is part of the validation. The design choices are validation choices. Make them on purpose.

---

*Tags: visualization, mcluhan, uncertainty-visualization, living-deck, dashboard-as-argument, deceptive-visualization, perception-hierarchy, FT-question-taxonomy, aleatoric-uncertainty, epistemic-uncertainty, quantile-dotplot, natural-frequencies*

---

###  LLM Exercise — Chapter 11: Visualization Under Validation

**Project:** The Agentic Red-Team Casebook

**What you're building this chapter:** Two dashboards of your casebook findings, built from the SAME failure-statistics data: an honest one that gives the agent a fair hearing, and a deliberately misleading one that makes the agent look better than the evidence supports. Comparing them surfaces which design choices did the misleading work — exactly the move the chapter teaches.

**Tool:** Claude Code (for chart generation) + Cowork (for the dashboard files). Or the artifact pattern in claude.ai if you want HTML/React dashboards rendered live.

---

**The Prompt:**

```
I am working through Chapter 11 of "Computational Skepticism for AI." My casebook contains 5–11 failure cases with classifications and the failure-statistics table from Chapter 9.

This chapter teaches that a dashboard is an argument. The design choices are normative — choice of axis range, color, channel, ordering, what gets foregrounded vs sub-tabbed, what shows uncertainty vs hides it. The nine-item catalog of misleading choices includes truncated axes, dual-axis tricks, cherry-picked windows, area-instead-of-position encoding, color-as-judgment, etc. Aleatoric uncertainty (irreducible variability) and epistemic uncertainty (incomplete knowledge) require different visualization techniques.

Build TWO dashboards from my casebook's failure statistics. They use IDENTICAL underlying data.

DASHBOARD A — HONEST:
Design choices:
- Failure rate (cases per N tasks tested) shown on a position-encoded chart (bar or dot plot), with a y-axis starting at 0
- Severity classification (fundamental vs contingent) shown alongside, not buried
- Per-category breakdown (the four taxonomy categories) shown with consistent ordering
- The two prediction-locks from Chapter 4 that resolved badly are visible — calibration of the casebook itself is on the dashboard
- Aleatoric uncertainty around each rate shown via confidence intervals (use Wilson or bootstrap CI for small N)
- Epistemic uncertainty (sources of structural unknown — opacity of training data, untested deployment contexts) shown via a "what we cannot say" panel
- Color used for category, not for judgment

DASHBOARD B — DELIBERATELY MISLEADING:
Design choices to deploy (each violates one of the catalog items):
- Truncated y-axis on the failure rate chart so the bars look small
- "Successful interactions" headline metric in large green type at top; failure cases in small gray sub-tab
- Per-category breakdown ordered by FREQUENCY, with the most damaging failure type buried at the bottom
- Confidence intervals omitted; central estimate only
- The fundamental/contingent classification quietly relabeled "addressable" so all failures look fixable
- Color: green for "successful interactions," gray for everything that suggests caution
- Cherry-picked time window if the agent has improved over time — show only the last week
- Dual-axis trick: failure count on one axis, "successful interactions" on the other, scaled so the failures look minor

For each dashboard, output:
- A description of every design choice and what it does to the reader's interpretation
- Either the actual chart code (if I'm using Claude Code with matplotlib / plotly / d3) or the rendered artifact (if I'm using the artifact pattern with Recharts)
- The catalog-item label for each misleading choice in Dashboard B

Then write the COMPARISON: a one-page note titled "What the design choices did" that walks through each pairing of choices (honest vs misleading) and names exactly what the misleading choice obscured.

Finally — the LIVING DECK move — add a provisionality note to Dashboard A. Some of the casebook's findings are still under collection; some prediction-locks are still open. Show what is settled and what is provisional.
```

---

**What this produces:** Two dashboards (HTML, image, or interactive artifact), a per-dashboard design-choice explanation, a side-by-side comparison note titled "What the design choices did," and a provisionality annotation on the honest version. The misleading version is for your eyes — DO NOT include it in the final external-facing report; include the comparison analysis instead.

**How to adapt this prompt:**
- *For your own project:* If you can render dashboards directly in claude.ai's artifact pattern, do — it's the fastest way to see the design choices working live.
- *For ChatGPT / Gemini:* Works as-is. ChatGPT's Code Interpreter handles matplotlib well; Gemini's renders Plotly cleanly.
- *For Claude Code:* Recommended for the matplotlib / plotly version. Claude Code can iterate on the design fast.
- *For Cowork:* Save both dashboards plus the comparison note to the casebook folder.

**Connection to previous chapters:** The Chapter 9 failure statistics are the data; the Chapter 7 fairness defense is one of the cells; the Chapter 8 robustness probe results are visible too. The dashboard is the casebook's findings made legible.

**Preview of next chapter:** Chapter 12 audits the casebook's WRITING — every claim against the verb taxonomy, every confidence number against actual calibration metrics computed on your prediction-locks. This is where the casebook's internal honesty is checked before it goes to peer critique.


---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **W. E. B. Du Bois** designed some of the most original data visualizations in history for the 1900 Paris Exposition — explicit, deliberate choices about what to show and how, with the politics of each choice fully visible. Here's a prompt to find out more — and then make it better.

![W. E. B. Du Bois, c. 1900. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/w-e-b-du-bois.jpg)
*W. E. B. Du Bois, c. 1900. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was W. E. B. Du Bois, and how do his 1900 Paris Exposition visualizations connect to the choices behind making a chart that is honest rather than merely persuasive? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"W. E. B. Du Bois"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe one specific Du Bois Paris chart in plain language, as if you've never seen 19th-century data viz
- Ask it to compare a Du Bois choice (his polar-area or step-chart designs) to a modern misleading-vs-honest version of the same data
- Add a constraint: "Answer as if you're writing the opening case for a chapter on visualization under validation"

What changes? What gets better? What gets worse?

