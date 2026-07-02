# Renumbering Proposal — 13-Chapter Order

Status: PROPOSAL, not executed. 2026-07-02.

## The decision

Adopt the draft order (the numbering the reframed Teardown drafts already use). It is the order the reframe was written against, the fairness chapter's prerequisites already assume it (bias before fairness, causal ladder from Ch6), and half the in-text cross-references in the merged chapters silently use it. Keeping the old numbering means every merged chapter contradicts its own cross-references.

## Old → new mapping

| New | Title (current) | Current file | Rename? |
|-----|-----------------|--------------|---------|
| 1 | The Skeptic's Toolkit | 01-the-skeptics-toolkit.md | no |
| 2 | Probability, Uncertainty, and the Confidence Illusion | 02-probability-... | no |
| 3 | Data Validation: Reconstructing the Epistemic Frame... | 05-data-validation-... | 05→03 |
| 4 | Robustness: What "Understanding" Means... | 08-robustness-... | 08→04 |
| 5 | Model Explainability: Distinguishing Explanation... | 06-model-explainability-... | 06→05 |
| 6 | Bias: Where It Enters and Who Is Responsible | 03-bias-... | 03→06 |
| 7 | Fairness Metrics: Choosing a Definition and Defending It | 07-fairness-... | no |
| 8 | Validating Agentic AI: When Autonomous Systems Misbehave | 09-validating-agentic-ai-... | 09→08 |
| 9 | Delegation, Trust, and the Supervisory Role | 10-delegation-... | 10→09 |
| 10 | Visualization Under Validation: Honest, Misleading... | 11-visualization-... | 11→10 |
| 11 | Communicating Uncertainty: Calibrating Claims to Evidence | 12-communicating-... | 12→11 |
| 12 | Accountability: Who Is Responsible When the System Fails? | 13-accountability-... | 13→12 |
| 13 | The Limits of AI: What the Tools Cannot Do | 14-the-limits-... | 14→13 |

No filename collisions — slugs all differ, only the number prefix changes.

## Why this order holds up

Part structure it implies: **evidence** (2 probability, 3 data) → **model behavior** (4 robustness, 5 explainability) → **values** (6 bias, 7 fairness) → **autonomy** (8 agents, 9 delegation) → **communication** (10 visualization, 11 uncertainty) → **stakes** (12 accountability, 13 limits).

The one soft spot: robustness at 4, before explainability. Defensible — you establish *what the model actually learned* (proxies, fragility) before asking *whether explanations of it are real* — but if it reads wrong in the hand-rewrite, swapping 4↔5 is a two-file rename with light cross-ref impact. Flagging, not recommending.

## The Frictional Method problem

The intro TOC still lists **Chapter 4 — The Frictional Method**, but no chapter file exists (only `drafts/04-the-frictional-method-...-substack-draft.md`). The reframe's 13-chapter order has no slot for it. **Decision needed:** confirm it's cut (my read of the reframe), park it as an appendix, or reinstate it. The intro TOC must be rewritten in any case.

## Retitle recommendations (apply during hand-rewrite, not now)

- **Ch5:** adopt draft title "Explanation vs. the Appearance of Explanation" — shorter, sharper, same claim. Recommended.
- **Ch7:** adopt draft title "Fairness: Choose a Definition and Defend It" — imperative fits the Teardown voice. Recommended.
- **Ch2:** draft short title "The Confidence Illusion" — good running head; keep the full title as the chapter title. Neutral.
- **Ch9:** draft's "…and the Boondoggle" — keep as in-chapter device, not title. Recommend against.
- **Ch12:** "Who Signs the Gate" subtitle — depends on whether attestation becomes the spine in your rewrite. Defer.

Renaming files twice is churn; renumber now with existing slugs, retitle (and rename once) per chapter as you hand-rewrite.

## Cross-reference problem — the real work

~150 in-text "Chapter N" references across chapters 01–14, in **two mixed numbering frames**: original scaffolding refs use old numbers, woven draft prose uses draft numbers. Example: in the agentic chapter, the draft calls the Human Decision Node "Chapter 9" while original text calls it "Chapter 10" — after renumbering, delegation IS Chapter 9, so the draft refs become correct and the original refs become wrong.

**A mechanical sed is guaranteed to corrupt references.** Each ref must be resolved semantically: read the sentence, identify which chapter it points at by topic, write the new number. Plan: one pass per chapter (parallelizable), resolving every `Chapter \d+` against the new map. Also fixes the stray "Chapter 15" in the limits chapter.

## Execution plan (on approval)

1. `git mv` the ten files (new numbers, same slugs).
2. Update each file's H1 `# Chapter N —` line and the merge comments.
3. Semantic cross-ref pass, chapter by chapter.
4. Rewrite intro TOC (13 chapters, no Frictional Method) and the "How to Read" line.
5. Update anything in `97-fundamental-themes.md` / `99-back-matter.md` that cites chapter numbers.
6. Verify: grep for out-of-range numbers, orphaned refs, old-frame leftovers; diff review.
7. Single commit; hand you the push command.
