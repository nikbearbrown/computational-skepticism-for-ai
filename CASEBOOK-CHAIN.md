# The Casebook Exercise Chain — canonical dependency graph

The LLM Exercise in each chapter builds one running deliverable: the student's **Agentic Red-Team Casebook**, red-teaming one agent of their choosing across the book (the Pebble). The exercises were written against the pre-renumber order and were NOT updated during chapterization; this graph is the single source of truth for the fix. Frictional apparatus homed per `FRICTIONAL-DECISION.md`: the **casebook journal + prediction-lock discipline + case template are set up in Chapter 1**; the **AI Use Disclosure is defined in Chapter 9**.

## Production order (new 13-chapter order)

| Ch | Produces | Consumes (must already exist) |
|----|----------|-------------------------------|
| 1 | System Dossier; **casebook journal + prediction-lock discipline + case template** (Frictional apparatus, credited); names the binding capacity for Ch8 | — |
| 2 | Probabilistic Baseline (+ first prediction-lock) | System Dossier |
| 3 | Data Frame Audit + hidden-failure test spec (+ prediction-lock) | System Dossier, Probabilistic Baseline |
| 4 | Robustness Probe Results + `probe-suite.py` + **first ≥2 formal cases** (+ per-probe prediction-locks) | System Dossier, Data Frame Audit, casebook journal |
| 5 | Self-Explanation Audit + case write-up (**adds to** Ch4's cases) | System Dossier, Data Frame Audit, Robustness Probe Results |
| 6 | Bias & Leverage Brief + Mermaid DAG | System Dossier |
| 7 | Defended Fairness Choice | System Dossier, Self-Explanation Audit, Bias & Leverage Brief |
| 8 | casebook-index + case files + failure-statistics table | Data Frame Audit(3), Robustness Probe Results(4), Self-Explanation Audit(5), Bias & Leverage Brief(6), Defended Fairness Choice(7), journal predictions(2–4) |
| 9 | delegation maps (current+proposed) + Boondoggle buckets + **AI Use Disclosure** | case files(8), Bias & Leverage Brief(6), Defended Fairness Choice(7) |
| 10 | two dashboards (honest + misleading) | failure-statistics(8), Defended Fairness Choice(7), Robustness Probe Results(4), prediction-locks(2–4) |
| 11 | verb-audit + calibration metrics (Brier/ECE) + Layer 1 summary + peer-critique request | prediction-locks(2–4), case files(8), dashboards(10), fairness defense(7); AI Use Disclosure(9) into Layer 3 |
| 12 | responsibility-attribution maps + accountability requirements + governance counterfactual (**closes Rung 3 opened in Ch4**) | case taxonomy(8), delegation map(9) |
| 13 | final go/no-go memo + assembled casebook | everything |

## The four validation lenses (used in Ch8)

Data validation = **Ch3**, Robustness = **Ch4**, Explainability = **Ch5**, Fairness = **Ch7**. (Bias/Ch6 feeds the case analysis but is not one of the four "lenses.") Any "four lenses from Chs 5–8" phrasing is old-order and wrong; correct is **Chs 3, 4, 5, and 7**.

## Prediction-locks are made in Ch2, Ch3, Ch4

Every "prediction-locks from Chapters 4, 3, and 4" or "Chapter 4 [verify-xref]" is wrong; correct is **Chapters 2, 3, and 4**, logged in the casebook journal set up in **Chapter 1**.

## Rule for every Connection/Preview block

Connection cites only chapters **before** this one; Preview describes the **immediately next** chapter (13 has none). No `[verify-xref]` flags or editorial notes may remain in student-facing prompt text.
