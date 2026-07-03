# CAJAL Figure Plan — Chapter 9: Delegation, Trust, and the Supervisory Role

FIGURE 1 — The testability refinement loop
Heuristic: MC
Priority: Important
Concept (one sentence): A handoff condition becomes testable through an unglamorous loop — write the condition, circle every interpretive word, replace each with a specifiable criterion, hand it to a non-author to verify on a sample case, and if they cannot, go again.
Reader/audience: engineer who knows what a pipeline handoff is; has read the "reasonable result / human reviews" failure example.
Type: cycle
Components (5): (1) draft condition; (2) circle interpretive words (show "reasonable," "reviews" circled); (3) replace with specifiable criteria or pinned-down guidelines; (4) non-author verification test on a sample case; (5) pass → done / fail → arrow looping back to (2).
Exclusions: no tiered-testability caveat (the qualified-reviewer wrinkle stays in prose); no loan/medical/moderation domain examples (the existing three-domain table serves those); no delegation-map eight-item structure.

FIGURE 2 — Hierarchical delegation mapping: dense at the seams, loose in the interior
Heuristic: VG
Priority: Important
Concept (one sentence): At scale the delegation map becomes a layered document — component-level everywhere, step-level only where authority transitions between AI and human, where audit trails cross boundaries, or where decisions commit — with documentation density concentrated at the high-stakes interfaces.
Reader/audience: engineer who has seen the flat eight-item map and is asking how it survives a 1,000-step system.
Type: hierarchy / structural schematic
Components (5): (1) top layer of major components; (2) mid layer of sub-components expanded only at handoffs; (3) routine interior region marked "policy documented, steps not enumerated"; (4) highlighted seams where AI↔human authority transitions; (5) density-gradient legend (tight at seams, light inside settled components).
Exclusions: no multi-agent thousands-of-steps speculation; no map-vs-audit-trail reconciliation problem (that is the chapter's declared open question); no versioning/review workflow detail.

Recommended: 2 figures, Mechanistic density. (The chapter already carries Figures 9.2–9.4; these two fill the only unserved structural zones.)
