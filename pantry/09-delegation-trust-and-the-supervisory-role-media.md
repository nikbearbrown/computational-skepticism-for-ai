# Media Plan — Chapter 9: Delegation, Trust, and the Supervisory Role

Zones detected: 12 · video 1 · figure 2 · graph 1 · table 0 · served 7 · dropped 1

## Zone index
| # | Concept (one line) | Heuristic | Routed | Priority/Score |
|---|---|---|---|---|
| 1 | Silent-failure asymmetry: missing items 1–4 breaks the pipeline loudly, missing 5–8 fails silently downstream | MC | video (Candidate 03) | 7/10 |
| 2 | The testability refinement loop (write → circle → replace → non-author test → go again) | MC | figure (FIGURE 1) | Important |
| 3 | Hierarchical delegation mapping — documentation dense at the seams, loose in routine interiors | VG | figure (FIGURE 2) | Important |
| 4 | Trust-calibration monitoring readout: HIGH-confidence correction rate over the last 50 papers | PQ | graph (GRAPH 1) | Important |
| 5 | Untestable → testable handoff conditions across three domains | CT | SERVED | — |
| 6 | Five supervisory capacities as pipeline jobs with artifacts | EN | SERVED | — |
| 7 | Five Boondoggle questions and where high risk pushes the delegation | CT | SERVED | — |
| 8 | Eight-item delegation map structure (what "missing" looks like) | EN | SERVED | — |
| 9 | Paper Summarizer happy path + six-step Boondoggle Score | MC | SERVED | — |
| 10 | Three trust-calibration failure modes (undertrust / overtrust / calibrated) | CT | SERVED | — |
| 11 | AI Use Disclosure field anatomy | SP | SERVED | — |
| 12 | Two-teams opening contrast (vague vs contract-grade documentation) | CT | dropped | — |

## Graph cards

```
GRAPH 1 — Trust-calibration readout: HIGH-confidence correction rate over the last 50 papers
Priority: Important
Reader question: Is the researcher's reliance on HIGH-confidence extractions matched to how often those extractions actually turn out to need correction?
Family + first candidate: time series→line (run chart of per-paper correction rate, spot-check rate overlaid as a second series)
Data status: illustrative-only possible — the Paper Summarizer is a constructed worked example; the chapter frames the "last fifty papers" readout as hypothetical. Any rendering must be labeled as a demonstration of what the audit-trail readout WOULD look like, never as findings.
DATA SPEC:
  Unit of observation: one processed paper (its Step 4 disposition record)
  Fields: paper_id : id; date : date; n_high_extractions : int; n_high_corrected : int; n_low_flagged : int; disposition_mix : enum counts (confirmed/corrected/unverifiable); spot_check_rate : float
  Denominator: HIGH-confidence extractions per paper (corrections expressed as a rate of those)
  Expected n: ~50 papers, rolling window
  Likely source: the pipeline's own Step 4 audit trail — the chapter's point is that this data already exists in any mapped deployment and is almost never looked at
Exclusions: the accept/override medical-imaging numbers (they live in Exercise 7 — out of scope); any overtrust-prevalence claim (the chapter explicitly holds "overtrust is dominant" as a working hypothesis, not a finding)
```

## Table cards

None. The chapter's contrast/enumeration zones (capacities, Boondoggle questions, map items, Disclosure fields, handoff examples) are all already served by styled tables.

## Served zones

- SERVED — untestable→testable handoff contrast: the loan/medical/moderation three-domain table ("What interpretation got pinned down").
- SERVED — five supervisory capacities as pipeline jobs: capacity/operational-form/artifact/failure-mode table.
- SERVED — five Boondoggle questions: low-risk/high-risk/delegation-push table.
- SERVED — eight-item delegation map + broken-vs-unsupervised asymmetry: items table with "what missing looks like" column and the italic note. (The asymmetry's temporal mechanism — the silent error propagating — is escalated separately to video Candidate 03; the lookup content itself is served.)
- SERVED — Paper Summarizer happy path and six-step Boondoggle Score: Figures 9.2 and 9.3.
- SERVED — three trust-calibration failure modes: Figure 9.4.
- SERVED — AI Use Disclosure field anatomy: field/what-goes-here/what-vague-looks-like table.

Dropped: two-teams opening contrast — the narrative carries it, and the untestable→testable table generalizes the same lesson; a table here would duplicate.

## Pointers
- Figure cards: pantry/09-delegation-trust-and-the-supervisory-role-cajal.md
- Video candidates from this chapter: vids/video-ideas.md (Candidate 03)
