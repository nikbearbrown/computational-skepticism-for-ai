# MINIBIO-PROMPT — generate one mini-bio script per Wayback figure

Use this prompt once per figure file in `wayback/`. Output goes to
`wayback/NN-figure-slug-SCRIPT.md`, ready for the Unreal Reels pipeline
(audio-first: one beat = one narrated line over one generated clip).

---

## The prompt (paste everything below, then paste the figure's source file)

You are writing the narration script for a 3–5 minute "mini-bio" video in the
Wayback series for the book *Computational Skepticism for AI* by Nik Bear Brown.
Voice: first person Nik — Feynman machinery-from-first-principles × design-critic
trade-off analysis. Direct address, no academic hedging, no documentary-narrator
pomposity.

INPUT: the source file below contains (a) the thesis paragraph connecting this
figure to one chapter of the book, (b) a portrait reference, (c) a student prompt.

HARD RULES
- NO FABRICATION. Every biographical fact — dates, titles, institutions, quotes —
  must be either present in the source file, or a widely documented fact you are
  confident of. Anything less than certain gets marked [verify] inline. Never
  invent quotes. Never invent scenes presented as fact; a reconstructed scene must
  be labeled as reconstruction in the narration itself ("Picture..." / "Imagine...").
- The chapter connection is the spine, not a footnote. This is not a generic
  biography: the video exists to show why this figure's move anchors this chapter.
  The source file's thesis paragraph states that connection — the script builds to
  it and lands on it.
- Length: 450–700 narration words total (≈ 3–5 min at speaking pace).

STRUCTURE — 8 to 12 beats. For each beat give:
- **Beat N** — one narrated sentence or two (the exact words to be spoken)
- **Scene** — one image/video prompt for the visual (period-appropriate, may
  reference the AI-portrait style used in the book; no text-in-image)
- **On-screen text** (optional) — max 6 words, only when a date/title earns it

Beat arc: (1) cold open — a concrete moment or problem, not "X was born in...";
(2–4) the life compressed: who, where, what pressed on them; (5–8) the idea —
build the figure's core move from first principles, the way the book would;
(9–11) the turn to now — the chapter connection from the source thesis paragraph,
AI systems named plainly; (12) close — one sentence that hands the viewer the
move, plus the surprising fact the source's student prompt asks for (marked
[verify] if not certain).

OUTPUT FORMAT
```
# Mini-Bio Script — {Figure} ({N} of 13, Chapter {N})
Runtime target: 3–5 min. Word count: {n}.
Source: wayback/{NN-figure-slug}.md

## Beats
[beats as specified above]

## End card
[the "Run this" student prompt from the source file, verbatim]

## Verify list
[every [verify] item, one line each, so they can be checked before audio]
```

---

## Run order (all 13)

- [ ] 01 Karl Popper
- [ ] 02 Frank Ramsey
- [ ] 03 Suzanne Briet
- [ ] 04 John von Neumann
- [ ] 05 Hans Reichenbach
- [ ] 06 Hannah Arendt
- [ ] 07 John Stuart Mill
- [ ] 08 Maurice Merleau-Ponty
- [ ] 09 Donald Broadbent
- [ ] 10 W. E. B. Du Bois
- [ ] 11 Florence Nightingale
- [ ] 12 John Dewey
- [ ] 13 Alan Turing
