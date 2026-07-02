# Research Notes: Chapter 13 — Accountability: Who Is Responsible When the System Fails?
**Corresponding chapter:** chapters/13-accountability-who-is-responsible-when-the-system-fails.md · **Editor note:** notes/13-accountability-who-is-responsible-when-the-system-fails.md · **Generated:** 2026-07-01

## Chapter summary
The chapter argues responsibility for agentic-AI failures distributes across multiple parties (each necessary, none sufficient), and more strongly that humans must stay in the accountability chain for a *structural* reason — accountability requires cognitive work AI cannot perform. It supports this with a walk-through failure case, two ethics frameworks converging on distribution, a seven-tier taxonomy (author's forthcoming work), a Gödel argument, and the regulatory landscape (EU AI Act, NIST, FDA), closing with Pearl's Rung-3 as a governance counterfactual.

## A. Load-bearing claims → sources
- **Claim:** Learning, autonomous machines create a "responsibility gap": no one can be fairly held responsible because manufacturers/operators cannot predict the machine's learned behavior. · **Source:** Matthias, A., "The responsibility gap: Ascribing responsibility for the actions of learning automata," *Ethics and Information Technology* 6(3), 2004, pp. 175–183. DOI 10.1007/s10676-004-3422-1 · primary · **Verdict:** CONFIRMED — Matthias coined "responsibility gap" in this 2004 paper; framing (unpredictability of learned behavior breaks traditional responsibility ascription) confirmed.
- **Claim:** The responsibility gap is not one problem but at least four (culpability, moral accountability, public accountability, active responsibility), addressable via designing socio-technical systems for meaningful human control. · **Source:** Santoni de Sio, F. & Mecacci, G., "Four Responsibility Gaps with Artificial Intelligence: Why they Matter and How to Address them," *Philosophy & Technology* 34(4), 2021, pp. 1057–1084. DOI 10.1007/s13347-021-00450-x · primary · **Verdict:** CONFIRMED — four-gap taxonomy and meaningful-human-control (reason-responsiveness) solution confirmed.
- **Claim:** Meaningful human control rests on "tracking" (system responds to relevant human reasons) and "tracing" (outcomes traceable to a human). · **Source:** Santoni de Sio, F. & van den Hoven, J., "Meaningful Human Control over Autonomous Systems: A Philosophical Account," *Frontiers in Robotics and AI* 5:15, 2018 (the tracking/tracing conditions); Mecacci & Santoni de Sio, "Meaningful human control as reason-responsiveness" (*Ethics and Information Technology*, 2020) · primary · **Verdict:** [UNVERIFIED here — not directly searched] but these are the standard, real companion papers; the two-condition (tracking/tracing) account is correctly attributed. Cite the 2018 Frontiers paper for the conditions.
- **Claim:** The Gödel argument — that an AI cannot validate its own outputs and structurally needs an external validator — is "logical, not philosophical." · **Source:** Gödel, K. (1931) incompleteness theorems · **Verdict:** CONTESTED / [ANALOGY, NOT PROOF] — Gödel's theorems concern the (in)ability of sufficiently strong consistent formal systems to prove their own consistency / all truths in their language. The leap to "an AI cannot self-validate and needs a human" is an **analogy**, not an entailment: a human validator is not exempt from Gödelian limits, and "recognition/contact with external reality" is undefended philosophical work. FLAG per editor Priority #2 — present as a suggestive structural analogy, strike "not a philosophical objection, it is a logical one." (This matches the task instruction to flag any Gödel/incompleteness claim as analogy.)
- **Claim:** EU AI Act fines for prohibited practices reach up to €35 million or 7% of total worldwide annual turnover, whichever is higher. · **Source:** Regulation (EU) 2024/1689 (AI Act), Article 99 (Penalties); artificialintelligenceact.eu/article/99 · primary (regulation) · **Verdict:** CONFIRMED — Art. 99: prohibited-practice breaches up to €35M or 7% worldwide turnover; high-risk breaches up to €15M or 3%; information violations up to €7.5M or 1%. Prohibited-practices provisions applicable since 2 Feb 2025. (Chapter's "up to 7% of global turnover" is correct.)
- **Claim:** The seven-tier cognitive taxonomy underpinning the structural-impossibility argument. · **Source:** Brown, N.B., *Irreducibly Human*, Bear Brown & Company LLC, Spring 2026 (forthcoming) · primary, author's own, unpublished · **Verdict:** [UNVERIFIED] — forthcoming, author's own work; the reader cannot check it. Legitimate to cite but MUST be flagged prominently as the load-bearing dependency (editor Priority #3). The absolutism ("structurally, not because currently insufficient") should be aligned with the chapter's own "calibrated uncertainty" hedge.

## B. Resolving the editor's [verify] flags
- **Shapira et al., *Agents of Chaos*, 2026, §16.5** (opening case) → [UNVERIFIED] — could not confirm this source exists / is published. Flagged in the book's own calibration file as [verify]. NEEDS confirmation the source is real and the §16.5 case is accurately described; if fictional/composite, mark as such.
- **Nik Bear Brown, *Irreducibly Human*, Spring 2026** → [UNVERIFIED] (forthcoming, author's own). See A.
- **EU AI Act specific articles/effective dates** → CONFIRMED — Reg. (EU) 2024/1689; Art. 5 (prohibited practices), Art. 99 (penalties); prohibited-practices applicable 2 Feb 2025; high-risk obligations phasing to Aug 2026/2027. Cite article numbers.
- **NIST Agent Standards Initiative / AI RMF** → [UNVERIFIED for "Agent Standards Initiative"] — the NIST AI Risk Management Framework (AI RMF 1.0, Jan 2023) is real; a distinct "Agent Standards Initiative" with specific dates/scope was not confirmed. Verify the exact program name and dates.
- **US Copyright Office guidance on generative outputs** → [UNVERIFIED here] — the USCO's "Copyright and Artificial Intelligence" report series (2023–2025) is real; confirm the specific provision cited.
- **SyRI dismissed by Dutch courts 2020** → CONFIRMED as real (The Hague District Court ruled the SyRI welfare-fraud risk-scoring system violated Art. 8 ECHR, judgment 5 Feb 2020). Cite NJCM c.s. v. The Netherlands (SyRI), ECLI:NL:RBDHA:2020:865.
- **Pachocki chain-of-thought monitoring attribution** → [UNVERIFIED] — not confirmed; attributed claim about a specific proposal. Needs a source or should be softened.
- **Mirror self-recognition species list (great apes, dolphins, elephants, possibly magpies)** → largely CONFIRMED in comparative-cognition literature (Gallup MSR test; Reiss & Marino 2001 dolphins; Plotnik/de Waal 2006 elephants; Prior et al. 2008 magpies — magpie result later contested/failed replication). Cite specific studies; note magpie is genuinely "possibly."
- **Bee valence claim** → [UNVERIFIED here] — plausibly refers to Bateson et al. 2011 (*Current Biology*, honeybees show pessimistic cognitive bias). Confirm.
- **EU AI Act "fines up to 7% of global turnover"** → CONFIRMED. See A.

## C. Domain examples / cases (real, cited)
- **SyRI (Netherlands, 2020):** CONFIRMED — court struck down an opaque welfare-fraud risk-scoring system; strong real accountability/recourse case. ECLI:NL:RBDHA:2020:865.
- **EU AI Act (Reg. 2024/1689):** CONFIRMED — real regulatory anchor for the accountability-requirements section; Art. 5 prohibitions, Art. 99 penalties.
- **NIST AI RMF 1.0 (2023):** CONFIRMED as real (verify the specific "Agent Standards" sub-initiative name).
- **Matthias 2004 & Santoni de Sio/Mecacci 2021:** CONFIRMED — the two load-bearing philosophy sources for the responsibility-gap spine.
- **Epic Sepsis / Ash callbacks:** Epic Sepsis is CONFIRMED (see Ch. 12 notes, Wong 2021). "Ash" case is internal to the book — not externally verifiable.

## D. Open flags (still [UNVERIFIED])
- Shapira et al., *Agents of Chaos* §16.5 — existence/accuracy of source unconfirmed.
- *Irreducibly Human* (forthcoming, author's own) — reader cannot check; hedge the impossibility claim.
- Gödel argument — flag as ANALOGY, not proof (per instruction and editor Priority #2).
- NIST "Agent Standards Initiative" exact name/dates.
- Pachocki chain-of-thought-monitoring attribution.
- Bee-valence citation (likely Bateson et al. 2011 — confirm).
- Santoni de Sio & van den Hoven 2018 tracking/tracing conditions (real; cite directly).

## Sources
Primary:
- Matthias, A. (2004). The responsibility gap. *Ethics and Information Technology* 6(3): 175–183. https://doi.org/10.1007/s10676-004-3422-1
- Santoni de Sio, F. & Mecacci, G. (2021). Four Responsibility Gaps with Artificial Intelligence. *Philosophy & Technology* 34(4): 1057–1084. https://doi.org/10.1007/s13347-021-00450-x
- Santoni de Sio, F. & van den Hoven, J. (2018). Meaningful Human Control over Autonomous Systems. *Frontiers in Robotics and AI* 5:15. https://doi.org/10.3389/frobt.2018.00015
- Regulation (EU) 2024/1689 (AI Act), Arts. 5 & 99. https://artificialintelligenceact.eu/article/99/
- The Hague District Court, SyRI judgment, 5 Feb 2020, ECLI:NL:RBDHA:2020:865.
- Gödel, K. (1931). Über formal unentscheidbare Sätze... [cited as analogy only]
- NIST (2023). AI Risk Management Framework (AI RMF 1.0).
Forthcoming / author's own (flagged):
- Brown, N.B. (Spring 2026). *Irreducibly Human*. Bear Brown & Company LLC. [UNVERIFIED — unpublished]
Comparative-cognition support (mirror test):
- Reiss, D. & Marino, L. (2001). Mirror self-recognition in the bottlenose dolphin. *PNAS* 98(10): 5937–5942.
- Plotnik, J., de Waal, F. & Reiss, D. (2006). Self-recognition in an Asian elephant. *PNAS* 103(45): 17053–17057.
- Prior, H., Schwarz, A. & Güntürkün, O. (2008). Mirror-Induced Behavior in the Magpie. *PLoS Biology* 6(8):e202. [magpie result later contested]
