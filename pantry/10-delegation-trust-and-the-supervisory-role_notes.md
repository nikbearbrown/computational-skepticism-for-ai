# Research Notes: Chapter 10 — Delegation, Trust, and the Supervisory Role
**Corresponding chapter:** chapters/10-delegation-trust-and-the-supervisory-role.md · **Editor note:** notes/10-delegation-trust-and-the-supervisory-role.md · **Generated:** 2026-07-01

## Chapter summary
The chapter recasts a delegation not as a partition of labor but as a *contract* whose load-bearing element is a *testable handoff condition* a non-author can verify. It operationalizes the five supervisory capacities into named pipeline artifacts (via a two-teams parable and a Paper Summarizer walkthrough) and argues, on the strength of a trust-calibration triad (under/over/calibrated), that "overtrust is the dominant failure mode in current AI deployments."

## A. Load-bearing claims → sources

- **Claim:** Automation is misused through *overreliance* (misuse) and underused through *disuse*; appropriate reliance depends on trust, workload, and risk. This is the disciplinary frame behind the chapter's under/over/calibrated triad and the "overtrust" claim. · **Source:** Parasuraman, Riley, "Humans and Automation: Use, Misuse, Disuse, Abuse," 1997, *Human Factors* 39(2):230–253, DOI 10.1518/001872097778543886, https://journals.sagepub.com/doi/10.1518/001872097778543886 · primary · **Verdict:** CONFIRMED — defines Use/Misuse/Disuse/Abuse; *misuse = overreliance* (monitoring failures, decision biases); *disuse = underutilization* (often from false alarms). This is the correct anchor for "overtrust." BUT it does NOT assert overtrust is *the dominant* failure mode across "current AI deployments" — see B/D.
- **Claim:** Trust drives reliance on automation; the design goal is *appropriate* reliance / *calibrated* trust (avoiding both overtrust and distrust). · **Source:** Lee, See, "Trust in Automation: Designing for Appropriate Reliance," 2004, *Human Factors* 46(1):50–80, DOI 10.1518/hfes.46.1.50_30392, https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392 · primary · **Verdict:** CONFIRMED — the canonical source for trust *calibration* and "appropriate reliance"; directly grounds the calibrated/over/under triad. Also grounds the "respond to technology socially" premise behind the fluency trap at workflow level.
- **Claim:** Overtrust (misuse) leads to monitoring failures and automation-induced complacency — the mechanism the chapter needs for "the pull toward trusting fluent output and moving on." · **Source:** Parasuraman, Riley 1997 (as above) · primary · **Verdict:** CONFIRMED for the *mechanism* (complacency/monitoring failure). The *prevalence* claim ("dominant failure mode") remains authorial — cite these two papers to license "overtrust is a well-documented and consequential failure mode," not "the dominant one," unless a prevalence study is added.
- **Claim:** Sustained-attention/vigilance decrements are real and were characterized by Broadbent's tradition (the "AI Wayback Machine" section's biographical facts). · **Source:** Broadbent, D. E., *Perception and Communication*, 1958, Pergamon; *Decision and Stress*, 1971, Academic Press; Director of the MRC Applied Psychology Unit (APU) 1958–1974. · primary (books) / secondary (biography: Encyclopedia.com, New World Encyclopedia) · **Verdict:** CONFIRMED — *Perception and Communication* (1958), *Decision and Stress* (1971), and APU directorship 1958–1974 all confirmed. These are the biographical facts the chapter states; now citable.
- **Claim:** A delegation without a testable handoff condition is unsupervised even when it appears to work (the contract framing). · **Source:** Author's framework; grounded in the appropriate-reliance literature (Lee & See 2004; Parasuraman & Riley 1997). · framework/secondary · **Verdict:** CONFIRMED as a defensible synthesis, NOT an externally established finding. Present as the book's operational stance, supported by (not derived from) the trust literature.
- **Claim (Boondoggle Score):** A five-question instrument correctly sorts tasks by delegability. · **Source:** Author's own instrument (self-sourced). · **Verdict:** [UNVERIFIED] — no external validation that the five questions predict real delegation outcomes. Present as a heuristic ("the questions matter more than the score"), not a validated diagnostic. See D.
- **Claim:** Delegation-cue / trust research now extends to LLM agents specifically. · **Source (optional reinforcement):** "Task-Aware Delegation Cues for LLM Agents," 2026, arXiv:2603.11011; "Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents," 2025, arXiv:2502.01390 · primary (recent) · **Verdict:** CONFIRMED these exist and are on-topic; useful to show the 1997/2004 automation-trust findings are being re-tested for LLM agents. Treat as supporting, not load-bearing.

## B. Resolving the editor's [verify] flags
No literal `[verify]` tags in this chapter. The editor flagged three *unsourced-but-load-bearing* assertions:

1. **"Overtrust is the dominant failure mode in current AI deployments"** → PARTIALLY RESOLVED / RECOMMEND REFRAME. The *category* (misuse/overreliance) and its *mechanism* (complacency, monitoring failure) are CONFIRMED and citable to Parasuraman & Riley 1997 and Lee & See 2004. The *"dominant … in current AI deployments"* prevalence claim is [UNVERIFIED] — neither paper (nor any single source located) establishes it as the most common failure mode across contemporary AI systems. **Fix:** either (a) cite Parasuraman & Riley 1997 + Lee & See 2004 and reframe to "overtrust/automation complacency is a well-documented and consequential failure mode," or (b) keep "in my reading" and foreground it explicitly as a working hypothesis. Do not present as an established finding.
2. **Broadbent biographical facts (APU 1958–1974; *Perception and Communication* 1958; *Decision and Stress* 1971)** → RESOLVED. All CONFIRMED. Cite the two books directly and a biographical source (Encyclopedia.com) for the APU directorship dates.
3. **Boondoggle Score presented as validated method** → [UNVERIFIED]. Self-sourced; no external validity evidence. Reframe as a heuristic checklist (the chapter half-concedes "the score is less important than the questions"). See D.

## C. Domain examples / cases (real, cited)
- **Automation misuse (overreliance) → monitoring failure:** Parasuraman & Riley 1997 — the disciplinary precedent for "trusting fluent output and moving on." CONFIRMED.
- **Trust calibration → appropriate reliance:** Lee & See 2004 — the under/over/calibrated regimes plotted against true reliability. CONFIRMED (the Fig 10.4 "three trust-calibration failure modes" should be anchored to this source).
- **Vigilance decrement (human supervisory limit):** Broadbent tradition, *Perception and Communication* (1958) — supports why a human "monitor" degrades over time, motivating testable-handoff design rather than continuous vigilance. CONFIRMED.
- **LLM-agent trust/team performance (contemporary re-test):** "Plan-Then-Execute" 2025 (arXiv:2502.01390) — empirical user-trust/team-performance study with LLM agents; a real, recent example that the classic findings still bind. CONFIRMED as real; use as illustration.
- **Note:** The chapter's two-teams loan-scoring parable is a *constructed* contrast (the editor flags it is not a documented failure). No external citation exists or is needed — present as illustrative, not as a case.

## D. Open flags (still [UNVERIFIED])
- **"Overtrust is THE dominant failure mode in current AI deployments"** — the prevalence/superlative is unsourced. Overtrust-as-a-failure-mode is confirmed (Parasuraman & Riley 1997; Lee & See 2004); "dominant/most-common" is not. **Reframe or flag as hypothesis.**
- **Boondoggle Score validity** — self-sourced instrument; no evidence the five questions predict delegation outcomes. Present as heuristic.
- **"Gru" tool efficacy claims** — any performance/efficacy claim about the author's proprietary tool is [UNVERIFIED] and commercial; not a research citation.
- **Testability-as-objective** — editorial, not a citation gap: the chapter's own gold-standard human steps embed interpretive terms ("domain-specific sense," "would mislead a peer"), so the testable/untestable binary is graded. No source needed; acknowledge in prose.

## Sources
Primary:
- Parasuraman, R., Riley, V. "Humans and Automation: Use, Misuse, Disuse, Abuse." *Human Factors* 39(2):230–253, 1997. DOI 10.1518/001872097778543886 — https://journals.sagepub.com/doi/10.1518/001872097778543886
- Lee, J. D., See, K. A. "Trust in Automation: Designing for Appropriate Reliance." *Human Factors* 46(1):50–80, 2004. DOI 10.1518/hfes.46.1.50_30392 — https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392 ; PubMed 15151155 — https://pubmed.ncbi.nlm.nih.gov/15151155/
- Broadbent, D. E. *Perception and Communication.* London: Pergamon Press, 1958 — https://archive.org/details/in.ernet.dli.2015.139166
- Broadbent, D. E. *Decision and Stress.* London: Academic Press, 1971.

Secondary (biography):
- "Broadbent, Donald Eric." Encyclopedia.com — https://www.encyclopedia.com/science/dictionaries-thesauruses-pictures-and-press-releases/broadbent-donald-eric (confirms APU directorship 1958–1974)

Supporting (contemporary LLM-agent trust, optional):
- "Task-Aware Delegation Cues for LLM Agents." 2026. arXiv:2603.11011 — https://arxiv.org/abs/2603.11011
- "Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant." 2025. arXiv:2502.01390 — https://arxiv.org/abs/2502.01390
