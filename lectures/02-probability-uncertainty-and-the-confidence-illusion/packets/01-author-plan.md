# AGENT SLOT 1 — author the deck plan

**Chapter:** `/sessions/loving-youthful-hawking/mnt/Cowork/computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
**Starter:** `deck_plan.starter.json` (156 TODOs)
**Write:** `deck_plan.json` in this folder with every `TODO:` replaced. No TODO may remain.

The starter has the correct slide SKELETON (title, section dividers, concept/equation/
figure slides, close). Your job is the judgement a regex can't do:
- headlines that make a claim, not restate the heading
- speaker_notes that will become the narration seed (2-4 sentences, teach don't recite)
- bind figure/chart slides to a pool asset id from `assets/assets.json` where one fits
- drop slides that shouldn't be in a lecture; merge thin ones

Read the chapter and the starter, then emit the finished `deck_plan.json`.
When done, re-run: `silent_run.py <book> --chapter 02-probability-uncertainty-and-the-confidence-illusion --from deck`
