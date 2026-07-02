# Wayback — Mini-Bio Video Series

The "AI Wayback Machine" sections were removed from all 13 chapters on 2026-07-02.
Each becomes a 3–5 minute **mini-bio** video produced with the Unreal Reels pipeline
(`/Users/nik/Documents/Cowork/unreal-reels`).

## Files

| File | Figure | Chapter |
|------|--------|---------|
| 01-karl-popper.md | Karl Popper | 1 — The Skeptic's Toolkit |
| 02-frank-ramsey.md | Frank Ramsey | 2 — Probability, Uncertainty, and the Confidence Illusion |
| 03-suzanne-briet.md | Suzanne Briet | 3 — Data Validation |
| 04-john-von-neumann.md | John von Neumann | 4 — Robustness |
| 05-hans-reichenbach.md | Hans Reichenbach | 5 — Model Explainability |
| 06-hannah-arendt.md | Hannah Arendt | 6 — Bias |
| 07-john-stuart-mill.md | John Stuart Mill | 7 — Fairness Metrics |
| 08-maurice-merleau-ponty.md | Maurice Merleau-Ponty | 8 — Validating Agentic AI |
| 09-donald-broadbent.md | Donald Broadbent | 9 — Delegation, Trust, and the Supervisory Role |
| 10-w-e-b-du-bois.md | W. E. B. Du Bois | 10 — Visualization Under Validation |
| 11-florence-nightingale.md | Florence Nightingale | 11 — Communicating Uncertainty |
| 12-john-dewey.md | John Dewey | 12 — Accountability |
| 13-alan-turing.md | Alan Turing | 13 — The Limits of AI |

Each source file contains the verbatim removed section: the chapter-connection paragraph
(the video's thesis — why this figure anchors this chapter), the portrait reference, and
the "Run this" student prompt (reusable as an end-card or companion exercise).

`MINIBIO-PROMPT.md` is the generation script: run it once per figure to produce the
narration script + beat sheet that Unreal Reels consumes.

`computational-skepticism-for-ai-wayback.md` is the old whole-book extraction (pre-removal,
old chapter numbering). Superseded by the per-figure files; kept as an archive.

## Workflow per figure

1. Generate the mini-bio script: paste MINIBIO-PROMPT.md + the figure's source file into the writing session (or run the `unreal-reels` skill with both).
2. Review the script — anything marked [verify] gets checked before audio.
3. Hand the approved script to the Unreal Reels pipeline (audio-first: narration is the master clock).
4. Park finished videos as `wayback/NN-figure-slug/` build folders or link them here. No mp3/mp4 in this repo — builds live in the unreal-reels workspace; only scripts and beat sheets get committed here.
