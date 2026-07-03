# The Logic for Making a Chart or Graph

The decision sequence, in order. Skipping a step is how a Venn diagram ships
as a bar chart.

## 0 · Never fabricate

A chart is a set of quantitative claims. If there is no data, there is no
chart — write the data spec (fields, unit of observation, denominators,
expected n, likely source) and either find the data or generate illustrative
data carrying a visible "ILLUSTRATIVE — not a measured finding" label inside
the image. Placeholder values that look real (88/74/61/47/34) are worse than
no figure, because a reader cannot tell them from findings.

## 1 · Start with the reader question

One sentence, before anything else: what should a reader be able to answer
after looking at this? "Visualize the data" and a caption pasted as a title
are not questions. If the question cannot be stated, the figure is not ready.

## 2 · Triage the medium — is it even a chart?

- Reader must **look up exact values** → a table.
- Reader must **see structure** — sets, mechanisms, cycles, hierarchies,
  boundaries → a diagram/figure (SVG), not a data chart. A Venn diagram is a
  set-relationship *figure*; it contains no bars because it contains no
  magnitudes.
- Reader must **compare magnitudes or see a shape** — trend, distribution,
  proportion → a chart. Only now does charting machinery start.

## 3 · Audit the data

Classify every field (categorical / ordinal / quantitative / temporal /
geographic / hierarchical / network). State the unit of observation. State
the denominator behind every rate or percentage. Note missing values,
outliers, transformations. Ask Cairo's question: *compared with what?* No
chart until the audit exists.

## 4 · Choose the family by reader task, not data shape

| Reader task | Family | First candidate |
|---|---|---|
| Compare categories | Comparison | Sorted bar (horizontal if labels are long) |
| Change over time | Time series | Line |
| See a distribution | Distribution | Histogram or box plot |
| See a relationship | Relationship | Scatterplot |
| Parts of a whole | Part-to-whole | Stacked bar or waffle; pie only for 2–5 slices |
| Nested structure | Hierarchy | Treemap |
| Movement between states | Flow | Sankey |
| Where | Spatial | Choropleth (rates) / bubble map (counts) |

The message can override the data shape: 100%-sum data with a "which is
biggest?" question is a comparison chart, not a pie.

## 5 · Schema before code

Write down, before generating: mark types; which channel encodes which
variable (position and length carry the quantitative truth — color supports);
sort order; scale types; zero-baseline decision; one color role per series
(one red emphasis series, neutral grays for the rest, ochre never encodes
data); titles, axis labels, direct labels, accessibility text.

## 6 · Honesty constraints (non-negotiable)

Bars and areas start at zero. Ink proportional to value; bubble radius via
square root. Gaps shown, never silently interpolated. Trend lines only with
the model named. No dual y-axes, no 3D, no rainbow palettes. Every figure
must survive the grayscale test.

## 7 · Verify against the question

Open it. Read it against the data and the schema. If the chart does not let
the reader answer the stated question faster, more accurately, and with less
ambiguity than a table would — it is not finished. A title is not a caption;
a caption is not a subtitle; production metadata never renders in the image.

---

*Why the current book images fail: they came from a placeholder generator
(`graphs.sh`) that skips every step above — it fabricates values (step 0),
has no reader question (1), ignores the medium (2 — the "Venn diagram" bars),
never audits (3), defaults to one family regardless of task (4), and renders
caption text and metadata into the image (7). It was scaffolding for layout
iteration that shipped as final art. The remedy is a remake pass: route each
existing image through step 2 — most are figures (SVG diagrams), a few are
real graphs that need real data found first.*
