# Computational Skepticism for AI

*Course textbook · 14 chapters · Masters engineering audience*

**Author:** Nik Bear Brown

**Folder:** `books/computational-skepticism-for-ai/`

---

## Overview

A masters-level engineering textbook on the supervisory and validation capacities required to catch the AI failure that does not announce itself — the plausible answer to the wrong question, the statistically valid output on a causally incoherent claim — built around Pearl's three-rung ladder of causal reasoning, the Five Supervisory Capacities, and a longitudinal validation case (Shapira et al., *Agents of Chaos*, 2026) threaded through eight chapters.

**Audience.** Masters engineering students. Mixed subfield (CS, data science, mechanical, EE, interdisciplinary). Probability priors and ML priors vary widely. The book treats this variance as a design constraint: Chapter 2 contains a calibration on-ramp; depth in Chs. 2, 5, and 8 is calibrated for the broadest target, with explicit "skip if you've taken graduate probability" callouts where appropriate.

**Scope.** In: the methodology of computational skepticism applied to AI systems — calibration, bias, data validation, explainability, fairness, robustness, agentic AI validation, delegation, communication, accountability, and the limits of the technical. The Five Supervisory Capacities, Pearl's Ladder (rungs 1–3 across the arc), the Frictional method as a general AI-era pedagogy contribution, and a six-tool ecosystem (Frictional, Gru, CRITIQ, Brutalist, Glimmer, Botspeak) used operationally throughout.

---

## Table of Contents

<!-- TOC sourced from `outline.md` -->

## Status

| # | Chapter | Status | Slug |
|---|---------|--------|------|
| 1 | The Skeptic's Toolkit | drafted | skeptics-toolkit |
| 2 | Probability, Uncertainty, and the Confidence Illusion | drafted | probability-uncertainty-confidence |
| 3 | Bias: Where It Enters and Who Is Responsible | drafted | bias-where-it-enters |
| 4 | The Frictional Method | drafted | frictional-method |
| 5 | Data Validation | drafted | data-validation |
| 6 | Model Explainability | drafted | model-explainability |
| 7 | Fairness Metrics | drafted | fairness-metrics |
| 8 | Robustness | drafted | robustness |
| 9 | Validating Agentic AI | drafted | validating-agentic-ai |
| 10 | Delegation, Trust, and the Supervisory Role | drafted | delegation-trust-supervisory |
| 11 | Visualization Under Validation | drafted | visualization-under-validation |
| 12 | Communicating Uncertainty | drafted | communicating-uncertainty |
| 13 | Accountability | drafted | accountability |
| 14 | The Limits of AI | drafted | limits-of-ai |

## Three-act arc

- Act One (Chs. 1–4): establish posture, language of uncertainty, architecture of failure, assessment apparatus
- Act Two (Chs. 5–10): build the validation toolkit
- Act Three (Chs. 11–14): apply — communication, accountability, limits

## Pearl's Ladder thread

- Ch 3: Rungs 1–2 introduced
- Ch 6: Rung 2 deepened
- Ch 8: Rung 3 opened
- Ch 13: Rung 3 closed (governance counterfactual)

## Longitudinal Pebble case

*Agents of Chaos* Case #1 (Ash's email server reset).
- Ch 1: first encounter (also Case #8 Identity Spoofing)
- Ch 5: Case #3 sensitive data
- Ch 6: Case #1 explanation gap
- Ch 7: Case #6 provider values
- Ch 8: Case #8 identity spoofing
- Ch 9: full validation, student picks any case
- Ch 10: Cases #2 and #5 as delegation failures
- Ch 13: §16.5 Responsibility seeds governance counterfactual

---

_Generated overview-and-TOC README. Source files (`book.md`, `outline.md`, etc.) remain the working documents._

---

## What This Book Is

This book is a course in the supervisory capacities that AI deployment requires. Not the engineering of AI systems — the models, the architectures, the training pipelines. Those subjects have excellent books. This book's scope is the supervisor's side of the human-AI boundary: the validation work, the judgment work, the accountability work, the communication work. The work that happens after the model is trained and before the harm is done.

The word *supervisory* is doing real work in that sentence. Supervision is not oversight in the bureaucratic sense. It is a set of *capacities* — things a human can do that the system cannot do for itself, and that the system's deployment depends on. By the end of this book, a reader should be able to audit any AI deployment and name, for each step, which Brutalist phase is in play, which supervisory capacity is being exercised, and by whom. Where that attribution fails, the reader has found a gap.

---

## Who This Book Is For

reader can take any AI deployment and ask, for each Brutalist phase, whether the discipline is in place. Where the answer is no, the reader has found the gap. Gaps are where patients die in waiting rooms.

---

## The five supervisory capacities

Brutalist names five supervisory capacities — five things a human must do that the system cannot do for itself. The five capacities are exactly the five capacities Chapter 1 introduces and the remaining chapters operationalize. The naming is the same be

---

## How to Read It

The fourteen chapters fall into four movements, though the book is designed to be read straight through. Each movement maps onto a Brutalist concern.

**Chapters 1–4 build the framework.** Chapter 1 gives you the Skeptic's Toolkit — four moves (Cartesian doubt, Hume's induction limit, Popperian falsifiability, the Plato's Cave move) that you apply before trusting any model output, and the five supervisory capacities that are the operational form of the book's argument. Chapter 2 confronts the probability intuitions that fail engineers most reliably: base rates, calibration, heavy-tailed loss distributions, and why a 99%-accurate test can be useless in ways that cost lives. Chapter 3 introduces bias through Pearl's causal ladder, distinguishes the three kinds of bias that live at different points in the pipeline, and builds the leverage analysis that tells you where to intervene. Chapter 4 addresses what AI has done to assessment and learning — the Decoupling Problem — and introduces the Frictional Method: predict, lock, work, observe, reflect, trace, calibrate. In Brutalist terms, these chapters are the *Audit* and *Schema* phases as they apply to AI deployment evaluation.

**Chapters 5–9 apply the lenses to specific validation surfaces.** Chapter 5 is data validation as epistemic reconstruction: why EDA is not sufficient, what the interrogation moves are, and what it means to trace a row to its source. Chapter 6 covers explainability — SHAP, LIME, counterfactuals — and the structural critique that these methods explain the model's internal accounting, not the world, and that language-game mismatches are where the practical misleading lives. Chapter 7 works through the fairness impossibility theorem: three reasonable definitions of fair, one dataset, the mathematical proof that they cannot all hold, and the defended-choice deliverable that results. Chapter 8 opens the question of what adversarial examples reveal about what models have actually learned — proxy features, not human-relevant features — and closes a Rung 3 question it opens in earnest. Chapter 9 pivots to agentic systems: the categorical shift from prediction to consequence, a taxonomy of agentic failure modes, the multi-agent patterns that compound them, and the distinction between validating a system and designing one. These chapters are the *Verify* phase, applied to four classes of claim that AI systems make about themselves.

**Chapters 10–12 address the human side of the human-AI system.** Chapter 10 builds the delegation map — a contract, not a partition, with testable handoff conditions — and operationalizes the five supervisory capacities as pipeline jobs rather than personality traits. This is the Brutalist *Schema* in its most explicit form. Chapter 11 makes the case that a dashboard is an argument: the design choices are normative, the catalog of misleading moves is learnable, and building a deliberately misleading version of your own dashboard is the fastest path to seeing what your default dashboards have been doing. Chapter 12 is the verb taxonomy: each verb of a claim has an evidentiary requirement, most engineering writing overstates by one or two verbs, and reading AI output through the taxonomy is one of the highest-leverage supervisory moves available. Chapters 11 and 12 are the *Handoff* phase made teachable.

**Chapters 13–14 close the book's two open arcs.** Chapter 13 addresses accountability — who is responsible when the system fails — through a responsibility-distribution analysis, two ethics frameworks, the five requirements for a working accountability regime, and the governance counterfactual that closes Pearl's Rung 3 opened in Chapter 8. Chapter 14 names the three structural limits that capability scaling cannot fix: meaning, intentionality, and the data-world gap. It distinguishes the deployments where these limits are methodology and the deployments where they are the safety mechanism, and it makes the book's culminating claim, which is also Brutalist's culminating claim: *the supervisor's authority to refuse deployment is the most important authority in any human-AI system, and the practice this book teaches must include that option, or it is not the practice this book is teaching.*

---

---

## Signature Simulations

<!-- TODO: populate from chapter content -->

---

## About the Author

Nik Bear Brown is Associate Teaching Professor in the Department of Industrial and Systems Engineering at Northeastern University, where they teach graduate courses on artificial intelligence, data science, and engineering practice. Their doctorate is in computer science from UCLA, with a major field in computational and systems biology and minor fields in artificial intelligence and statistics; they completed postdoctoral work at Harvard Medical School. They also hold a Master's in Information Design and Data Visualization and an MBA, both from Northeastern.

Brown is the founder and Executive Director of Humanitarians AI, a 501(c)(3) nonprofit that supports international graduate students in building production-scale AI projects for the public interest. They are the founder of Bear Brown & Company and the creator of the Irreducibly Human curriculum framework, which organizes human cognitive capacities by their replaceability in an AI-augmented world. They are also the architect of the **Brutalist** system for AI-assisted creative production — the renderer-agnostic framework whose AI-deployment-supervision module is this book and whose other modules include *Brutalist After Effects x Claude*, *Brutalist d3 x Claude*, *Brutalist Blender x Claude*, and *Brutalist Remotion x Claude*. The series is at [brutalist.art](https://www.brutalist.art/). Their research spans AI fluency, streaming-platform accountability, adaptive learning systems, and the governance of autonomous AI agents.

They live and work in Boston. More at [bearbrown.co](https://www.bearbrown.co/).

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except in the case of brief quotations in critical reviews and certain other noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

[bearbrown.co](https://www.bearbrown.co/)

