# Editor Calibration — Computational Skepticism for AI

*The spine every chapter's editor note is judged against (per `book-editor`). Derived
from Chapter 1 (The Skeptic's Toolkit) and the book's own framing.*

```
Discipline:          Computational skepticism for AI — validating AI systems, and
                     knowing when a statistically valid output is wrong about the
                     question that matters.

Unifying framework:  The book's connective spine, invoked chapter to chapter —
                     • The FOUR SKEPTICAL MOVES: Cartesian doubt, Humean induction
                       limits, Popperian falsifiability, and the Plato's Cave move.
                     • The FIVE SUPERVISORY CAPACITIES (the human capacities that
                       catch failures metrics cannot see).
                     • The SOLVE–VERIFY ASYMMETRY (generating an artifact is cheap;
                       verifying it is the hard, human part).
                     • The FLUENCY TRAP (well-formed prose read as evidence of truth).

Canonical failure 1: The Epic Sepsis Model — one of the most widely deployed clinical AI
                     tools in the US; trained, validated, published, and cleared through
                     procurement, yet on external validation it missed ~2 of every 3 sepsis
                     cases and alerted on 18% of all patients. "By every measure its builders
                     chose, it succeeded." DOCUMENTED: Wong et al., JAMA Internal Medicine,
                     2021. (Replaced the unverifiable Swedish-triage opening. A labeled
                     composite single-patient scene now illustrates the aggregate finding.)

Canonical failure 2: The autonomous email agent that confidently reported deleting a
                     sensitive email but had only reset a password and renamed an alias
                     — true about its local actions, false about the system.
                     (Shapira et al., *Agents of Chaos*, arXiv:2602.20021, 2026, Case #1.)
```

## Editor targets specific to this book

- **`[verify]` tags.** The manuscript carries inline `[verify]` markers on unsourced
  or composite claims. Every unresolved one is a load-bearing-claim risk — list them
  in each chapter's *Logical gaps* section.
- **Framework anchoring is the house test.** Because the whole book is downstream of
  Ch.1's four moves + five capacities, a chapter that does not explicitly tie its
  content to at least two elements of the spine is *floating* — a finding, not a nit.
- **The book eats its own dog food.** It argues for skepticism about fluent, plausible
  output; the editor holds its *own* prose to that standard — flag any passage that is
  persuasive but under-evidenced (the Fluency Trap, turned inward).
