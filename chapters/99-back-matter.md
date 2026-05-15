# Back Matter

---

## Acknowledgments

This book grew out of a course, and the course grew out of students who would not let bad answers stand. The graduate students in INFO 7375 and INFO 7390 at Northeastern University — especially the Humanitarians AI fellows who brought real deployment problems into the room — are the reason the arguments here are as sharp as they are. They found the gaps. They forced the rewrites. The dedication is not rhetorical.

Nina Harris co-taught the branding and AI course with me and sharpened my thinking on communication, design, and what it means to make evidence legible to a non-technical reader. Several of this book's visualization arguments trace directly to her pushback on my first drafts. Charles Fadel read chapters at speed and sent back questions that improved almost every one of them. Sri Sridhar's work on engineering education — and his willingness to argue about pedagogy at length — shaped the framework chapters more than he probably realizes.

The Frictional method in Chapter 4 was developed with students, not for them. They stress-tested every failure mode I documented and found several I had not. The journal format they used is the format that survived.

The material on agentic systems draws on the red-team literature — particularly *Agents of Chaos* — and on documented post-mortems that multiple researchers made publicly available. I am grateful to everyone who writes honest failure reports. The field runs on them.

The textbook is free to read at GitHub. The slide decks and assignment scaffolds are at [bearbrown.co](https://www.bearbrown.co/). The course continues.

---

## About the Author

Nik Bear Brown is Associate Teaching Professor in the Department of Industrial and Systems Engineering at Northeastern University, where they teach graduate courses on artificial intelligence, data science, and engineering practice. Their doctorate is in computer science from UCLA, with a major field in computational and systems biology and minor fields in artificial intelligence and statistics; they completed postdoctoral work at Harvard Medical School. They also hold a Master's in Information Design and Data Visualization and an MBA, both from Northeastern.

Brown is the founder and Executive Director of Humanitarians AI, a 501(c)(3) nonprofit that supports international graduate students in building production-scale AI projects for the public interest. They are the founder of Bear Brown & Company and the creator of the Irreducibly Human curriculum framework, which organizes human cognitive capacities by their replaceability in an AI-augmented world. They are also the architect of the **Brutalist** system for AI-assisted creative production — the renderer-agnostic framework whose AI-deployment-supervision module is this book and whose other modules include *Brutalist After Effects x Claude*, *Brutalist d3 x Claude*, *Brutalist Blender x Claude*, and *Brutalist Remotion x Claude*. The series is at [brutalist.art](https://www.brutalist.art/). Their research spans AI fluency, streaming-platform accountability, adaptive learning systems, and the governance of autonomous AI agents.

They live and work in Boston. More at [bearbrown.co](https://www.bearbrown.co/).

---

## Notes

Notes are grouped by chapter. Items marked **[verify before publication]** are flagged in the main text and require primary-source confirmation before final production.

---

### Chapter 1 — The Skeptic's Toolkit

1. The Swedish triage case is presented as a composite based on documented regional health-network AI deployments in Sweden circa 2018–2020. **[verify before publication]** Confirm against Lindgren et al. or substitute a fully primary-sourced case. The structural failure — a technically functioning system producing preventable harm — is documented across multiple national AI-in-triage audits; the specific death-in-waiting-room framing requires a verifiable primary source or must be recast as an explicit composite.

2. Descartes's method of radical doubt is developed primarily in *Meditations on First Philosophy* (1641), Meditation I. The operational version here — *what would have to be true for this claim to be wrong?* — is an engineering adaptation, not a direct quotation of Descartes's project.

3. Hume's argument against inductive inference is developed in *A Treatise of Human Nature* (1739–40), Book I, Part III, and more accessibly in *An Enquiry Concerning Human Understanding* (1748), Section IV. The framing here follows the "problem of induction" reading standard in philosophy of science rather than Hume's own skeptical conclusions.

4. Popper's criterion of falsifiability is developed in *Logik der Forschung* (1934), published in English as *The Logic of Scientific Discovery* (1959). The application to AI metrics is the author's extension.

5. Plato's cave allegory appears in *The Republic*, Book VII, ~514a–520a.

6. Ash's email-agent case. **[verify before publication]** Attributed to Shapira et al., *Agents of Chaos: Eleven Red-Team Studies of Agentic Failure*, 2026, Case #1, "Disproportionate Response." Confirm publication details, page or case number, and whether the "Ash" pseudonym is used in the source or is introduced here.

---

### Chapter 2 — Probability, Uncertainty, and the Confidence Illusion

7. The disease-screening example — 99% accurate test, 1-in-10,000 base rate, approximately 1% posterior probability — is a standard Bayesian base-rate illustration used in probability pedagogy. The arithmetic is correct. No specific original source is cited; the example appears in multiple statistics and medical-decision-making textbooks.

8. Bayes's theorem originates in Thomas Bayes, "An Essay towards solving a Problem in the Doctrine of Chances," *Philosophical Transactions of the Royal Society of London* 53 (1763): 370–418 (posthumous). The form used here follows standard notation.

9. The pandemic imaging case — models trained pre-2020 experiencing distribution shift in 2021–22 due to COVID-related changes in lung imaging patterns — is documented across several radiology AI audits. **[verify before publication]** Identify and cite at least one primary-source publication before final production.

10. Bjork's desirable difficulties research: the distinction between performance and learning conditions is developed across many papers. A useful primary source is Robert A. Bjork and Elizabeth Ligon Bjork, "A New Theory of Disuse and an Old Theory of Stimulus Fluctuation," in *From Learning Processes to Cognitive Processes: Essays in Honor of William K. Estes*, ed. A. F. Healy, S. M. Kosslyn, and R. M. Shiffrin (Erlbaum, 1992), 35–67. For a more accessible treatment, see Robert Bjork, "Institutional Impediments to Effective Training," in *Learning, Remembering, Believing*, ed. D. Druckman and R. Bjork (National Academy Press, 1994).

11. The Central Limit Theorem: no single original source is appropriate here; the theorem has numerous independent proofs and is standard probability curriculum. The note about Cauchy distributions and power-law exceptions is standard.

---

### Chapter 3 — Bias: Where It Enters and Who Is Responsible

12. The COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) case: the ProPublica analysis is Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner, "Machine Bias," *ProPublica*, May 23, 2016. Northpointe's response is William Dieterich, Christina Mendoza, and Tim Brennan, "COMPAS Risk Scales: Demonstrating Accuracy Equity and Predictive Parity," Northpointe, July 8, 2016.

13. Pearl's causal ladder (association, intervention, counterfactual) is developed in Judea Pearl and Dana Mackenzie, *The Book of Why: The New Science of Cause and Effect* (Basic Books, 2018), especially Chapters 1 and 3. The technical apparatus is in Judea Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed. (Cambridge University Press, 2009).

---

### Chapter 4 — The Frictional Method

14. The Decoupling Problem is the author's framing; no prior source is claimed.

15. Bjork's performance-vs.-learning distinction: see note 10 above.

16. The seven-move Frictional method is the author's original framework, developed for INFO 7375 and INFO 7390 at Northeastern University.

---

### Chapter 5 — Data Validation

17. The join-failure case (four-percent silent drop rate, subpopulation exclusion) is a composite case based on production post-mortems the author has observed or consulted on. It is not attributed to a specific primary-source publication.

18. The agent-and-email-corpus case draws on the agentic failure mode documented in Shapira et al. **[verify before publication]** See note 6.

---

### Chapter 6 — Model Explainability

19. SHAP: Scott M. Lundberg and Su-In Lee, "A Unified Approach to Interpreting Model Predictions," *Advances in Neural Information Processing Systems* 30 (2017). **[verify before publication]** Confirm year and volume.

20. LIME: Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin, "'Why Should I Trust You?': Explaining the Predictions of Any Classifier," *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (2016), 1135–1144. **[verify before publication]** Confirm page range.

21. Counterfactual explanations: Sandra Wachter, Brent Mittelstadt, and Chris Russell, "Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR," *Harvard Journal of Law & Technology* 31, no. 2 (2018): 841–887. **[verify before publication]** The in-text cite says 2017; publication year in the journal is 2018; confirm the correct year to use (the preprint may be 2017).

22. Wittgenstein on language games: Ludwig Wittgenstein, *Philosophical Investigations*, §23, trans. G. E. M. Anscombe, P. M. S. Hacker, and Joachim Schulte, rev. 4th ed. (Wiley-Blackwell, 2009). **[verify before publication]** Confirm that §23 is the most accurate citation for the language-games passage as used here; §7 and §19 may be more directly on point.

23. Ash case: see note 6. Chapter 6 draws on Case #1 for the "language game mismatch" analysis.

24. Causal feature importance: Dominik Janzing, Lenon Minorics, and Patrick Blöbaum, "Feature Relevance Quantification in Explainability: A Causal Problem," *Proceedings of the 23rd International Conference on Artificial Intelligence and Statistics (AISTATS)* (2020). **[verify before publication]** Confirm full citation.

---

### Chapter 7 — Fairness Metrics

25. The fairness impossibility theorem (simultaneous satisfaction of calibration parity, equalized odds, and demographic parity is generally impossible when base rates differ): Jon Kleinberg, Sendhil Mullainathan, and Manish Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," *Proceedings of the 8th Innovations in Theoretical Computer Science Conference (ITCS)* (2017). Alexandra Chouldechova, "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments," *Big Data* 5, no. 2 (2017): 153–163. Both papers were posted as preprints in 2016. **[verify before publication]** Confirm which conference year to use for Kleinberg et al.

26. COMPAS case: see note 12.

---

### Chapter 8 — Robustness

27. The adversarial panda-gibbon example is from Ian J. Goodfellow, Jonathon Shlens, and Christian Szegedy, "Explaining and Harnessing Adversarial Examples," *International Conference on Learning Representations (ICLR)* (2015). **[verify before publication]** Confirm this is the correct source for the specific panda-gibbon illustration.

28. The framing of adversarial perturbations as features rather than bugs draws on Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, and Aleksander Mądry, "Adversarial Examples Are Not Bugs, They Are Features," *Advances in Neural Information Processing Systems* 32 (2019). **[verify before publication]** Confirm citation.

29. Randomized smoothing as certified defense: Jeremy Cohen, Elan Rosenfeld, and J. Zico Kolter, "Certified Adversarial Robustness via Randomized Smoothing," *Proceedings of the 36th International Conference on Machine Learning (ICML)* (2019). **[verify before publication]**.

30. The agent identity-spoofing case draws on Shapira et al. Case #8. **[verify before publication]** See note 6.

---

### Chapter 9 — Validating Agentic AI

31. *Agents of Chaos* is cited throughout this chapter. **[verify before publication]** Full citation: Shapira et al., *Agents of Chaos: Eleven Red-Team Studies of Agentic Failure* (2026). Confirm: publisher, full author list, whether this is a preprint or peer-reviewed publication, and whether §16 is the correct section reference for the taxonomy and the "broke my toy" phrase.

32. The "broke my toy" phrase, attributed to the system owner in §16 of Shapira et al., is the author's interpretive framing of what the paper documents. **[verify before publication]** Confirm that this specific phrase appears in the source or that the paraphrase is clearly identified as such.

---

### Chapter 10 — Delegation, Trust, and the Supervisory Role

33. The Boondoggle Score is an original framework developed by the author for the Gru tool ecosystem deployed in INFO 7375 and INFO 7390 at Northeastern University. No prior publication is claimed.

34. The five supervisory capacities framework (plausibility auditing, problem formulation, tool orchestration, interpretive judgment, executive integration) is the author's original taxonomy, introduced in Chapter 1 and developed throughout the book.

---

### Chapter 11 — Visualization Under Validation

35. McLuhan's "the medium is the message": Marshall McLuhan, *Understanding Media: The Extensions of Man* (McGraw-Hill, 1964), Chapter 1.

36. Tufte on data visualization: Edward R. Tufte, *The Visual Display of Quantitative Information*, 2nd ed. (Graphics Press, 2001). Also relevant: *Envisioning Information* (Graphics Press, 1990) and *Visual Explanations* (Graphics Press, 1997).

37. Cairo on data visualization: Alberto Cairo, *The Functional Art: An Introduction to Information Graphics and Visualization* (New Riders, 2012); *How Charts Lie: Getting Smarter about Visual Information* (Norton, 2019).

38. Research on confidence-interval misinterpretation by readers: a representative source is Geoff Cumming, Fiona Fidler, and David L. Vaux, "Error Bars in Experimental Biology," *Journal of Cell Biology* 177, no. 1 (2007): 7–11. **[verify before publication]** Additional sources in the cognitive-biases-in-statistical-communication literature should be cited if the claim about reader misinterpretation is to be supported robustly.

---

### Chapter 12 — Communicating Uncertainty

39. Grammarly's hedge-language detection capabilities: **[verify before publication]** Confirm current state of the feature and whether a citation to product documentation is appropriate or whether this should be omitted or generalized.

---

### Chapter 13 — Accountability

40. EU AI Act: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence. Official Journal of the European Union, L series, 2024. **[verify before publication]** Confirm OJ citation and phased implementation dates through 2027.

41. NIST AI Risk Management Framework: National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (January 2023). **[verify before publication]** Confirm whether a subsequent version has been published and whether the "Agent Standards Initiative" referenced in the text has a citable document.

42. FDA on AI in medical devices: U.S. Food and Drug Administration, *Artificial Intelligence and Machine Learning (AI/ML)-Based Software as a Medical Device (SaMD) Action Plan* (January 2021). **[verify before publication]** Confirm whether more current FDA guidance supersedes this document.

43. CFPB on algorithmic credit decisions: **[verify before publication]** Identify and cite specific CFPB guidance documents relevant to algorithmic credit scoring as of publication date.

44. EEOC on AI in employment: **[verify before publication]** Identify and cite specific EEOC guidance on AI hiring tools as of publication date.

45. Pearl's Rung 3 closure: the governance counterfactual is the author's original extension of Pearl's framework. See Pearl and Mackenzie, *The Book of Why* (note 13), for the Rung 3 technical apparatus; the application to institutional structure is original here.

---

### Chapter 14 — The Limits of AI

46. Turing's imitation game: Alan M. Turing, "Computing Machinery and Intelligence," *Mind* 59, no. 236 (1950): 433–460.

47. Searle's Chinese Room: John R. Searle, "Minds, Brains, and Programs," *Behavioral and Brain Sciences* 3, no. 3 (1980): 417–424.

48. The Systems Reply to Searle's Chinese Room: discussed in the peer commentary section of Searle (1980); see responses by various authors in the same issue. A useful secondary treatment is Margaret Boden, ed., *The Philosophy of Artificial Intelligence* (Oxford University Press, 1990).

49. The clinical decision-support system case in Chapter 14 is a composite used to illustrate the structural argument. It is not attributed to a specific primary-source publication.

---

## References

Works are listed alphabetically by author. For multi-author works, the first author's surname determines alphabetical position. Works without named authors are listed by institutional name or title.

---

Angwin, Julia, Jeff Larson, Surya Mattu, and Lauren Kirchner. "Machine Bias." *ProPublica*, May 23, 2016. https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing.

Bayes, Thomas. "An Essay towards solving a Problem in the Doctrine of Chances." *Philosophical Transactions of the Royal Society of London* 53 (1763): 370–418.

Bjork, Robert A., and Elizabeth Ligon Bjork. "A New Theory of Disuse and an Old Theory of Stimulus Fluctuation." In *From Learning Processes to Cognitive Processes: Essays in Honor of William K. Estes*, edited by A. F. Healy, S. M. Kosslyn, and R. M. Shiffrin, 35–67. Erlbaum, 1992.

Bjork, Robert A. "Institutional Impediments to Effective Training." In *Learning, Remembering, Believing*, edited by D. Druckman and R. Bjork. National Academy Press, 1994.

Boden, Margaret, ed. *The Philosophy of Artificial Intelligence*. Oxford University Press, 1990.

Cairo, Alberto. *The Functional Art: An Introduction to Information Graphics and Visualization*. New Riders, 2012.

Cairo, Alberto. *How Charts Lie: Getting Smarter about Visual Information*. Norton, 2019.

Chouldechova, Alexandra. "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments." *Big Data* 5, no. 2 (2017): 153–163.

Cohen, Jeremy, Elan Rosenfeld, and J. Zico Kolter. "Certified Adversarial Robustness via Randomized Smoothing." *Proceedings of the 36th International Conference on Machine Learning (ICML)*, 2019. **[verify full citation before publication]**

Cumming, Geoff, Fiona Fidler, and David L. Vaux. "Error Bars in Experimental Biology." *Journal of Cell Biology* 177, no. 1 (2007): 7–11.

Descartes, René. *Meditations on First Philosophy* (1641). Translated by John Cottingham. Cambridge University Press, 1996.

Dieterich, William, Christina Mendoza, and Tim Brennan. "COMPAS Risk Scales: Demonstrating Accuracy Equity and Predictive Parity." Northpointe, July 8, 2016.

European Parliament and Council. Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act). *Official Journal of the European Union*, 2024. **[verify OJ citation before publication]**

Goodfellow, Ian J., Jonathon Shlens, and Christian Szegedy. "Explaining and Harnessing Adversarial Examples." *International Conference on Learning Representations (ICLR)*, 2015.

Hume, David. *A Treatise of Human Nature* (1739–40). Edited by L. A. Selby-Bigge and P. H. Nidditch. Oxford University Press, 1978.

Hume, David. *An Enquiry Concerning Human Understanding* (1748). Edited by Tom L. Beauchamp. Oxford University Press, 1999.

Ilyas, Andrew, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, and Aleksander Mądry. "Adversarial Examples Are Not Bugs, They Are Features." *Advances in Neural Information Processing Systems* 32 (2019). **[verify full citation before publication]**

Janzing, Dominik, Lenon Minorics, and Patrick Blöbaum. "Feature Relevance Quantification in Explainability: A Causal Problem." *Proceedings of the 23rd International Conference on Artificial Intelligence and Statistics (AISTATS)*, 2020. **[verify full citation before publication]**

Kleinberg, Jon, Sendhil Mullainathan, and Manish Raghavan. "Inherent Trade-Offs in the Fair Determination of Risk Scores." *Proceedings of the 8th Innovations in Theoretical Computer Science Conference (ITCS)*, 2017. **[verify conference year; preprint dated 2016]**

Lundberg, Scott M., and Su-In Lee. "A Unified Approach to Interpreting Model Predictions." *Advances in Neural Information Processing Systems* 30 (2017). **[verify volume before publication]**

McLuhan, Marshall. *Understanding Media: The Extensions of Man*. McGraw-Hill, 1964.

National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. January 2023.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press, 2009.

Pearl, Judea, and Dana Mackenzie. *The Book of Why: The New Science of Cause and Effect*. Basic Books, 2018.

Plato. *The Republic*. Translated by G. M. A. Grube, revised by C. D. C. Reeve. Hackett, 1992.

Popper, Karl R. *The Logic of Scientific Discovery*. Hutchinson, 1959. Originally published as *Logik der Forschung*. Springer, 1934.

Ribeiro, Marco Tulio, Sameer Singh, and Carlos Guestrin. "'Why Should I Trust You?': Explaining the Predictions of Any Classifier." *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2016, 1135–1144. **[verify page range before publication]**

Searle, John R. "Minds, Brains, and Programs." *Behavioral and Brain Sciences* 3, no. 3 (1980): 417–424.

Shapira, [first names TK], et al. *Agents of Chaos: Eleven Red-Team Studies of Agentic Failure*. 2026. **[verify before publication: full author list, publisher or venue, page/section numbers for all in-text citations]**

Tufte, Edward R. *The Visual Display of Quantitative Information*. 2nd ed. Graphics Press, 2001.

Tufte, Edward R. *Envisioning Information*. Graphics Press, 1990.

Tufte, Edward R. *Visual Explanations: Images and Quantities, Evidence and Narrative*. Graphics Press, 1997.

Turing, Alan M. "Computing Machinery and Intelligence." *Mind* 59, no. 236 (1950): 433–460.

U.S. Food and Drug Administration. *Artificial Intelligence and Machine Learning (AI/ML)-Based Software as a Medical Device (SaMD) Action Plan*. January 2021. **[verify whether more current guidance supersedes this document before publication]**

Wachter, Sandra, Brent Mittelstadt, and Chris Russell. "Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR." *Harvard Journal of Law & Technology* 31, no. 2 (2018): 841–887. **[verify year: preprint 2017, journal publication 2018]**

Wittgenstein, Ludwig. *Philosophical Investigations*. Translated by G. E. M. Anscombe, P. M. S. Hacker, and Joachim Schulte. Rev. 4th ed. Wiley-Blackwell, 2009.

---

## Glossary

Short definitions of terms used throughout this book. Page-anchor references in the print edition; in the online edition, search by term.

**Agentic system.** An AI system that takes actions in an external environment (sending email, modifying files, calling APIs) rather than only producing predictions or text. Validation requirements differ categorically from those of predictive systems; consequence is the new variable. See Chapter 9.

**Audit (Brutalist phase).** The first phase of the Brutalist framework, in which the supervisor interrogates the data, the problem framing, and the deployment context before any model output is treated as a candidate for use. Chapters 3, 5, and 7 build audits for bias, data, and fairness respectively.

**Base rate.** The unconditional prior probability of an outcome in a population, before any test or evidence is applied. Confusing the base rate for the posterior probability is the most common source of overconfident inference from positive test results. See Chapter 2.

**Brutalist.** The renderer-agnostic framework for AI-assisted production within which this book is the deployment-supervision module. Names five phases (Audit, Schema, Generate, Verify, Handoff) and five supervisory capacities (Plausibility Auditing, Problem Formulation, Tool Orchestration, Interpretive Judgment, Executive Integration). Discussed in the front matter and in the Introduction.

**Calibration.** The property of a probabilistic forecaster whose stated confidences match the empirical frequency of correct predictions. A model that is 80%-confident on a class of cases should be right about 80% of the time on that class. Calibration is necessary for plausibility auditing to function.

**Causal ladder (Pearl).** Three rungs of inferential claim: association (Rung 1), intervention (Rung 2), counterfactual (Rung 3). Used throughout the book to diagnose what kind of claim a calculation is actually making and what evidence could settle it.

**Decoupling Problem.** The framing introduced in Chapter 4 for the way AI tools have decoupled the production of work from the cognitive process the work was supposed to develop. The Frictional Method is the response.

**Delegation map.** The contract — not partition — that names which decisions the model can make, which the human must make, and what the testable handoff conditions are between them. Chapter 10.

**Distribution shift.** The condition in which the data the model is deployed against differs systematically from the data it was trained on. Pre-2020 imaging models meeting 2021–22 imaging is a documented case. Distribution shift is one of the few failure modes that calibration alone cannot detect.

**Equalized odds.** A fairness criterion requiring equal true-positive and false-positive rates across protected groups. One of the three competing definitions in the fairness impossibility theorem. See Chapter 7.

**Executive Integration (EI).** The fifth supervisory capacity. The judgment work of integrating sub-discipline outputs into a single decision about whether to deploy, roll back, or refuse. The capacity that the supervisor's authority to refuse deployment operationalizes.

**Falsifiability (Popper).** The criterion that distinguishes scientific from non-scientific claims: a claim is scientific only if there is some observable outcome that would falsify it. Applied to AI metrics, the move is to ask what model behavior would falsify the performance claim. Chapter 1.

**Fluency trap.** The systematic error in which fluent, well-formed AI output is trusted more than the underlying evidence warrants — and, more dangerously, in which the reader's evaluation of fluent output is itself amplified by the fluency. The canonical Brutalist *Verify*-phase failure mode. Named in Chapter 1; recurs throughout.

**Frictional Method.** The seven-move discipline (predict, lock, work, observe, reflect, trace, calibrate) introduced in Chapter 4 as a counter to the Decoupling Problem. Designed to keep the cognitive process visible when AI tools could otherwise produce the work product without it.

**Generate (Brutalist phase).** The phase in which the model produces a candidate output. The discipline is to treat the candidate as a candidate, not a result.

**Governance counterfactual.** A Rung 3 question about institutional structure: *what would the deployment look like if a different governance regime were in force?* The closure of Pearl's Rung 3 applied to accountability. Chapter 13.

**Handoff (Brutalist phase).** The phase in which the verified result crosses a boundary into a context where someone is going to use it. Includes the supervisor's authority to refuse the handoff. Chapters 11–14.

**Heavy-tailed distribution.** A loss or outcome distribution in which extreme events occur more frequently than a normal distribution would predict. In AI deployment, heavy tails are why average-case performance does not reliably forecast worst-case harm.

**Impossibility theorem (fairness).** The result, demonstrated by Kleinberg et al. and Chouldechova, that calibration parity, equalized odds, and demographic parity cannot in general be simultaneously satisfied when base rates differ across groups. Chapter 7.

**Induction limit (Hume).** The observation that no finite set of past observations logically guarantees a future observation. Applied to AI: training-set performance does not, by itself, license deployment-context predictions. Chapter 1.

**Interpretive Judgment (IJ).** The fourth supervisory capacity. The reading of a result in context, including the recognition of language-game mismatches between the model's output and the user's situation.

**Language game (Wittgenstein).** A use of language whose meaning is determined by the practice in which it is embedded. Two parties using the same word in different language games will appear to communicate while in fact talking past each other. Diagnostic for the Ash case. Chapter 6.

**Plausibility Auditing (PA).** The first supervisory capacity. The discipline of checking whether a result is plausible given everything else the supervisor knows, independently of the model's stated confidence. Chapter 2.

**Posterior probability.** The probability of a hypothesis given the evidence, computed from the prior and the likelihood via Bayes's theorem. Distinct from the test's accuracy; failing to distinguish them is the base-rate fallacy.

**Problem Formulation (PF).** The second supervisory capacity. The discipline of asking whether the question the model is answering is the question that needed to be answered. Chapter 3.

**Robustness.** The property of a model whose performance does not collapse under small input perturbations or moderate distribution shift. The robustness chapter (8) argues that adversarial examples reveal what features the model has actually learned, which is often not the features humans would identify.

**Schema (Brutalist phase).** The contract that names what the system will do, what it will not do, and how the boundary is enforced. In AI deployment, the delegation map is the schema. Chapter 10.

**Stop condition.** A pre-specified, testable condition under which an AI deployment must be halted or rolled back. Without stop conditions, the supervisor's authority to refuse deployment cannot be exercised. Chapters 10 and 14.

**Supervisory capacity.** A category of cognitive work that the human supervisor must do because the system cannot do it for itself. The book names five (PA, PF, TO, IJ, EI), which are the same five Brutalist names across all renderer modules.

**Tool Orchestration (TO).** The third supervisory capacity. Choosing which validation tool to apply when, and recognizing when a tool is being asked to do work it was not designed for. Chapters 6, 8, 9.

**Verb taxonomy.** The framework introduced in Chapter 12 for matching claim verbs (*shows, suggests, proves, indicates, demonstrates, fails to distinguish*) to the evidentiary standard required for each. Reading AI output through the verb taxonomy is one of the book's highest-leverage supervisory moves.

**Verify (Brutalist phase).** The phase in which a candidate output is tested against external referents — calibration data, causal structure, ground truth, the user's actual question — before being treated as a result. The fluency trap is the failure to verify because the candidate looked enough like a result to skip the step.

---

## Index

*Omitted for online release. For print editions, compile after all other content is final using dedicated indexing software or a professional indexer. Key terms suitable for indexing include: adversarial examples, agentic systems, audit trail, base rate, calibration, causal inference, COMPAS, counterfactual, data validation, delegation map, desirable difficulties, distribution shift, equalized odds, explainability, fairness impossibility theorem, falsifiability, fluency trap, Frictional method, governance counterfactual, handoff condition, heavy-tailed distributions, induction, interpretability, label bias, LIME, Pearl's ladder, plausibility auditing, posterior probability, prior probability, robustness, SHAP, structural bias, supervisory capacities, transparency, trust calibration, verb taxonomy.*

