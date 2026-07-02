# Chapter 10 — Visualization Under Validation

Here's an experiment you can run this afternoon. Take one CSV — a real validation result, byte for byte fixed — and hand it to two people with instructions to build a dashboard. One of them wants to reassure a nervous deployment partner. The other wants that partner to ask the right questions. Watch what comes back.

The first dashboard opens with a single large number: **94% accuracy**, bold, alone. The subgroup charts underneath sit on truncated y-axes that squeeze the disparities down to nothing. The calibration curve — which happens to be the finding that matters — is tucked into a sub-tab labeled "advanced metrics." Green means good, gray means needs-attention, and the disparity charts are gray.

The second dashboard opens with a panel: overall performance *and* subgroup performance, on the same axes, so the gap between them is visible at first read. The calibration curve is in the main view with a banner noting the model is overconfident at high probabilities. One color. Nothing pulling your eye anywhere in particular.

Same data. Same CSV. And the deployment partner walks away from the two dashboards with two different beliefs about whether the system is safe. Here's what I want you to be able to do by the end of this chapter: get an AI to chart your data, then **catch and fix your own misleading encoding** before it ships — and catch someone else's when a chart lands on your desk. That's the [IJ] and [PA] combination, applied to the output layer, where a chart persuades before anyone checks it.

The claim underneath the whole chapter is this: a dashboard's structural choices *are an argument* about what the data means, and that argument is made before any single number is read. Which means a dashboard that misrepresents a valid finding is not a downstream communication problem. It's a validation failure at the output layer, and it's the supervisor's responsibility. The dashboard is an argument. The design choices are yours.

## The classical move: the medium is the message

Marshall McLuhan gave us the sentence in *Understanding Media* (1964): the medium is the message. The form shapes meaning before the content arrives. Apply it to a dashboard and the abstraction turns concrete. A dashboard that opens with one bold headline metric argues, by its structure, that the headline *is* the answer. A dashboard that opens with a panel of equally weighted views argues that the picture is composite and you have to integrate it yourself. Same numbers. Different arguments — and the argument is carried by layout, not by data.

Engineers are the worst offenders here, and not from malice. They think of a chart as a transparent pane of glass through which the data is simply seen. It isn't. It's a lens, ground to a prescription, and if you don't choose the prescription deliberately, you've chosen one by default — usually your plotting library's default, which was optimized for looking finished, not for being honest. The most important conceptual move in this chapter is to stop treating visualization as transmission and start treating it as argument.

## Step one: name the question the chart answers

A chart answers *one* question with data. Before you pick a chart type, write the question as a sentence. This sounds trivial and it's the step everyone skips, which is why so many charts answer a question nobody asked.

The Financial Times *Visual Vocabulary* (Alan Smith and the FT graphics team) sorts chart types by the question they answer, into families like: **deviation** (how far from a reference?), **correlation** (how does one variable move with another?), **ranking** (what's the order?), **distribution** (how often does each value occur?), **change over time** (what's the trend?), **part-to-whole** (what proportion?), **magnitude** (how big, in absolute terms?), **spatial** (where?), and **flow** (what moves where?). Andrew Abela's decision tree (*Choosing a Good Chart*, 2009) collapses the same idea to four: comparison, composition, distribution, relationship. Either way, the discipline is identical: start from the question, not from the shape of your data reaching for the nearest default.

<!-- → [TABLE: chart-selection reference — columns: Question family | What it answers | Chart types that belong here | Validation-context example. One row per FT family. Meant to be pinned above the reader's workstation.] -->

## Step two: encode where the eye is accurate

Once you know the question, you have to choose how to encode the answer, and human perception is not uniformly accurate across encodings. Cleveland and McGill established the ordering in 1984, and it's held up as one of the durable results in the field. Ranked from most to least accurate for reading a quantity:

1. **Position along a common scale** — the most accurate (a dot plot).
2. **Length** — nearly as good (bars on a shared baseline).
3. **Angle and slope** — worse (pie slices, radar arms).
4. **Area** — considerably worse (bubbles, treemap rectangles).
5. **Volume** — worse still; avoid.
6. **Color saturation and hue** — weakest for quantity, fine for category.

Cleveland and McGill measured the error rates that produce this ranking, and people often quote specific figures — position around a couple percent, area in the low tens of percent. I'll give you the ordering as solid and the exact percentages as approximate: the specific error figures I've seen attributed to this paper are [UNVERIFIED] against a page in the original, so treat them as "roughly, from Cleveland-McGill's measured rates," not as citable constants. The *ordering* is the tool. The implication is clean: encode quantitative answers as position or length; reserve area, angle, and color for cases where precision doesn't matter. When someone hands you a pie chart of five nearly equal slices, they've chosen the third-worst channel to answer a question that demanded the first.

<!-- → [CHART: the Cleveland-McGill hierarchy as a ranked scale — visual variable on the left (position → length → angle → area → volume → color), approximate error rate on the right, with a worked example per rung (dot plot, bar chart, pie, bubble). Caption: the channel choice determines how accurately the reader reads the number.] -->

## Uncertainty has two faces

Before we get to the deception catalog, one distinction that most charts erase. **Aleatoric uncertainty** is irreducible variability — sampling noise, natural variation, stochastic processes. That's what most people mean by "show your error bars." **Epistemic uncertainty** is the gap between what you know and what's true — it comes from the limits of your data, your instruments, your proxies, and in principle it's *reducible* if you go get more or better information. Most charts hide the epistemic kind entirely, which is dangerous, because the epistemic kind is often the larger one.

For aleatoric uncertainty, you have tools. **Error bars** for side-by-side point estimates — but label them, always, because readers misread an error bar as "the true value is uniformly somewhere in this interval," which is not what a 95% CI means. **Confidence bands** for trends where uncertainty grows or shrinks over the range — though a shaded band encodes the *amount* of uncertainty in color saturation, the weakest channel, so add explicit labels where the band widens. **Fan charts** for forecasts widening into the future.

That last one has a famous failure. The hurricane forecast "cone of uncertainty" contains roughly **66% of past forecast track errors — not 95%.** (That's confirmed against the National Hurricane Center's methodology: the cone is a two-thirds likelihood region sized from the prior five years of forecast errors.) The public reads the cone as the physical size of the storm, or as a hard wall between safe and unsafe. Neither is what it means. The fix is explicit text plus alternative encodings — because the default encoding was so intuitive it was intuited *wrong.*

And the single most effective technique for a lay audience is the one most guides skip: the **quantile dotplot** paired with a sentence of natural-frequency narration. Twenty dots, four of them filled, beats "20% chance" every time. This is grounded in Gerd Gigerenzer's work on natural frequencies — "9 out of 10 women with breast cancer test positive; 99 out of 1,000 women without it also test positive" produces correct reasoning where "90% sensitivity, 9.9% false-positive rate" produces confusion, even in physicians. (The canonical Gigerenzer numbers use roughly an 8-in-1,000 base rate and land near an 8% posterior; the specific phrasing varies, but the finding — that natural frequencies beat percentages for comprehension — is well established.)

Two rules that carry most of the weight. **Make the uncertainty visually equal in weight to the central estimate.** A small error bar hung off a big bold number reads as "the answer, with a quibble." And **avoid false precision** — 0.847291 ± 0.05 is a 0.85 metric, and every extra decimal is a small act of dishonesty. The most useful step of all, the one almost everyone skips: test the chart on a reader who didn't build it, and watch what they conclude.

## Showing the trust: epistemic uncertainty has practices, not tools

Epistemic uncertainty doesn't get a chart type. It gets practices. The first is Alberto Cairo's rule, and it comes from a real map: a FiveThirtyEight visualization of "kidnapping rates" in Nigeria that was actually a map of GDELT data — media *mentions* of kidnappings. The spike tracked Boko Haram press coverage, not kidnapping rates, and nothing on the map disclosed the proxy. Erin Simpson's line, which Cairo quotes, is the whole lesson: *"Validate your own data. It's not true just because it's on a goddamn map."* Validate before you visualize. Disclose the source inside the chart. Disclose your methodology choices — binning, smoothing, exclusion — in three sentences. Disclose what the data doesn't measure, in the title if that's where the honesty lives.

And sometimes the honest move is to not visualize at all. Cairo's hierarchy of disclosure: put uncertainty *prominently in the chart* when it materially changes the answer; in a *caption or footnote* when a serious reader needs it but the conclusion holds; in a *methodology appendix* when it's small and the conclusion is robust. The hierarchy is not hiding. The test is whether a *hostile* reader could arrive at a different conclusion. If they could, the uncertainty belongs up front.

## The deception catalog

Here's the catalog of moves that mislead — nine structural choices plus one about uncertainty itself. Every one of them has an honest use, which is exactly why they're dangerous: the chart looks the same whether the choice was honest or not, and the choice is the difference.

1. **Truncated axes** — a y-axis starting at 80 instead of 0 amplifies a small difference. Legitimate when the range is genuinely narrow and zero isn't meaningful (stock prices). Dishonest when it manufactures a gap.
2. **Inconsistent axes across panels** — side-by-side charts that look comparable but sit on different y-ranges. The most common *unintentional* dashboard mistake.
3. **Aggregation that hides distribution** — a mean or median concealing a heavy tail or a bimodal split. If the tail holds the catastrophic cases, hiding it is concealment.
4. **Color asymmetry** — unequal salience steers the gaze without the reader noticing.
5. **Cherry-picked time windows** — a window running from local minimum to local maximum exaggerates a trend.
6. **Scale trickery** — linear axes for log-natural data, or the reverse.
7. **Chartjunk and 3D effects** — Tufte's term; foreshortening and exploded pies distort the very quantities they display.
8. **Missing baselines** — accuracy with no random baseline, performance with no prior system. John Snow's 1854 cholera map worked precisely because it showed *all* the pumps, not just Broad Street.
9. **Labels that prejudge** — "Accuracy boost from new model" versus the neutral "Accuracy: model A vs model B."

And the tenth, which is structurally the most dishonest of the set: **selective uncertainty visualization** — showing confidence intervals where they help your story and omitting them where they'd hurt it.

<!-- → [TABLE: the deception catalog — columns: Move | Honest use | Dishonest use | How to tell the difference. Ten rows, one per move above. Meant as an audit checklist.] -->

## Four charts that made history

Three failures and one success. I'm going to be careful with two of these, because the source record isn't equally solid across all four, and a chapter about visual honesty cannot ship with a sloppy case.

**Challenger, January 1986.** The engineers had thirteen charts of O-ring erosion data the night before launch. The pattern was *in the data* — erosion was worse at lower temperatures — but it was never displayed in a way that made the pattern visible. The charts mixed qualitative text with quantitative displays, never plotted temperature against erosion in a single view, and emphasized reassuring findings over the overall risk profile. The chart that would have made the causal chain legible — cold → harder rubber → longer seating time → blow-by → failure — was never drawn. This is Edward Tufte's reading (*Visual Explanations*, 1997), and I want to flag it precisely because an earlier version of this material described the failure two different ways — as poor *encoding* of present data in one place and as *omission* of the cold-temperature region in another. Those are different diagnoses, and I'm going with the one the literature supports: the evidence existed; the visualization failed to make it visible to a decision-maker under pressure. Management approved the launch. Seven astronauts died. **Lesson:** when a decision is high-stakes and contested, the visualization has to make the causal chain visible and the uncertainty salient enough that a manager cannot honestly read it as inconclusive.

**Reuters, Florida "Stand Your Ground," 2014.** A line chart of firearm murders in Florida from 1990 to 2012, with the 2005 law marked. At a glance it looked like murders *dropped* after 2005 — the law worked. But the y-axis was **inverted**: zero at the top, high values at the bottom. So the post-2005 *spike* (deaths rose from 521 in 2005 to 740 in 2006 to 825 in 2007) rendered visually as a *decline*. Bergstrom and West use it in *Calling Bullshit* (2020) as the canonical axis-flip. The distinction worth keeping: truncation *amplifies* a real effect; inversion *reverses* one. **Lesson:** the orientation of an axis is itself a structural argument about which direction is "good." Honest practice: zero at the bottom for quantities where more means more, with the direction-of-better stated explicitly in the title.

**El País, Catalonia poll, 2014 — flagged.** This case is meant to illustrate uncertainty exceeding effect size: a poll reporting 45.3% "no" versus 44.5% "yes" with a ±2.95% margin — a 0.8-point difference inside a 2.95-point margin, which is a statistical tie — allegedly rendered as two bars of visibly different height, a lie of composition. I'm keeping it in the text only with a warning attached, because **I could not find the primary source** — the actual El País graphic and its date. Worse, an earlier version of this material described the same case two incompatible ways: the prose called it a 0.8-point tie misrepresented by two bars, while a summary table called it a *truncated axis* amplifying a "5-point lead." Those are different charts, different magnitudes, different sins. Until the original graphic surfaces, treat "Catalonia" as an *illustrative construction* of a real and important failure mode — uncertainty larger than the effect — not as a documented case. The failure mode is real regardless: when the margin swamps the difference, two bars of unequal height is a story about noise, and the honest move is a sentence — "it's a tie" — or a chart that makes the confidence interval visually larger than the effect. Sometimes the right chart is no chart.

**Snow's cholera map, 1854 — the counter-case.** John Snow's map did three things: it showed the spatial clustering of deaths, it marked the Broad Street pump at the center, and — the move that made it *evidence* rather than illustration — it showed *all the other pumps too*. The other pumps weren't mentioned in a caption. They were *shown*, which let a reader rule out the alternatives. (Historical footnote for honesty: the map was drawn after Snow reached his conclusion, by C. F. Cheffins, so it's better understood as a compelling argument than as the instrument of discovery the myth suggests.) **Lesson:** evidence-grade visualization shows what would have to be true for the conclusion to be *wrong*, not just what supports it.

Here's the summary, reconciled so the prose and the table finally agree:

| Case | What happened | Catalog item | Lesson |
|---|---|---|---|
| Challenger 1986 | The temperature-erosion pattern existed in the data but was never plotted legibly; the charts shown to managers read as consistent with a safe launch | Aggregation / missing causal display (per Tufte, *Visual Explanations* 1997) | A chart that fails to make the region of doubt visible ends up endorsing the decision |
| Reuters Florida 2014 | An inverted y-axis rendered a post-2005 murder *spike* as a visual *decline*; readers took away the opposite of the data | Axis inversion (relative of scale trickery) | An inverted axis can communicate the inverse of the data while staying technically accurate |
| El País Catalonia 2014 **[source unverified]** | A 0.8-point difference inside a ±2.95% margin — a tie — allegedly shown as two unequal bars | Uncertainty exceeding effect size (illustrative; primary source not found) | When the margin swamps the effect, the honest chart is a sentence, or no chart |
| ✓ Snow's cholera map 1854 | Mapping deaths to addresses *and showing all the pumps* pinned a hypothesis the death tables alone could not | Spatial reference; matched scale; alternatives shown | The right visualization makes the right hypothesis legible — and rules out the wrong ones |

*Three failures and one success. The success shows evidence-grade visualization has been possible for 170 years. The failures show possibility is not the same as practice.*

## The trade-off, stated plainly

A misleading chart is faster to build than an honest one, and it is more persuasive on first contact. That's the trade-off the whole field lives inside. The misleading dashboard from the opening was not *harder* to make than the honest one — it was a handful of choices away: truncate here, gray there, bury the calibration curve in a tab. Each choice took about thirty seconds and each one shifted the argument. If you optimize a chart for looking finished and reassuring, you sacrifice the reader's ability to reach a different conclusion than the one you wanted. That works if you value persuasion. It fails — catastrophically, at the Challenger level — if you need a decision-maker to see the region of doubt.

The choices are normative. There is no neutral.

## Exercises

### BUILD

**B1 — Chart your data, then catch your own misleading encoding.** Take a real finding from your own work. First build the *honest* version — accurate encoding, uncertainty shown at equal weight, subgroups on consistent axes, limits stated. Then, using only the same data, build a *misleading* version: truncate the axes, tilt the color salience, bury the inconvenient curve, put a bold central estimate over a thin error bar. **Lock a prediction before you build the misleading one:** which choices will you reach for to mislead, which will be hardest because the data refuses to be obscured, and which of these choices do you suspect you *already made unintentionally* in the honest version. Put the two side by side. You are graded on the reflection — which choices were high-leverage, which were nearly invisible yet high-impact, and which, if reversed, would most reduce the misleadingness.

**B2 — Fix the encoding you caught.** Take the unintentional misleading choice you found in B1 and fix it. Document what changed, name the catalog item it fell under, and state in one sentence how a reader's conclusion changes between the two versions.

### AUDIT

**A1 — Catch the misleading axis in a chart you were shown.** Take a chart handed to you — a dashboard, a paper figure, a slide. Run it against the ten-item catalog: for each move, note whether it's present and, if present, whether the use is honest or misleading. Flag the two highest-risk choices. For the worst one, state the reader's likely inference versus what the data actually supports, and sketch the honest version. Then answer the specific question this chapter is built around: is there a *truncated or inverted axis*, and if so, what conclusion does it manufacture?

**A2 — Answer the accuracy-versus-communication objection.** A colleague argues: "My dashboard is accurate. If people draw the wrong conclusion, that's a communication problem, not a validation problem." Respond in two paragraphs, using McLuhan's medium-is-the-message and one specific item from the catalog, to defend the claim that unfaithful visualization is a validation failure at the output layer.
