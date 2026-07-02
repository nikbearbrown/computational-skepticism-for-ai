#!/usr/bin/env python3
"""Pass 3 — replace 11 post-2000-failing Wayback subjects, insert portrait stubs in
the 3 kept chapters. All replacements are pre-2001 dead OR foundational work
entirely pre-2001, none overlap the existing botspeak or branding-and-ai lists.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# Replacements: full block rewrite
REPLACEMENTS = {

    "01-the-skeptics-toolkit.md": {
        "old_subject": "Sandra Harding",
        "new_subject": "Karl Popper",
        "stub_filename": "karl-popper.jpg",
        "era": "c. 1950s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Karl Popper** spent the 1930s working out which kinds of claims a scientific community can argue about productively and which it cannot — *demarcation* — and his answer (a claim is scientific only if it forbids some observation it could be checked against) is the spine of the toolkit you are about to use. The instruments in this chapter — falsifiability, prediction-lock before observation, the willingness to name what would change your mind — are Popper's instruments, applied to AI systems whose outputs the community has not yet learned to argue about productively.

![Karl Popper, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/karl-popper.jpg)
*Karl Popper, c. 1950s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Karl Popper, and how does his demarcation criterion — that a scientific claim must forbid some observation that could refute it — connect to what a skeptic's toolkit for AI should actually contain? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Karl Popper"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *falsifiability* in plain language, as if you've never read philosophy of science
- Ask it to compare Popper's demarcation move to the prediction-lock move this chapter teaches
- Add a constraint: "Answer as if you're writing the rationale for the first move in a validator's toolkit"

What changes? What gets better? What gets worse?
""",
    },

    "02-probability-uncertainty-and-the-confidence-illusion.md": {
        "old_subject": "Sarah Lichtenstein",
        "new_subject": "Frank P. Ramsey",
        "stub_filename": "frank-ramsey.jpg",
        "era": "c. 1925",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Frank Ramsey** died at twenty-six, in 1930, having already worked out — in *Truth and Probability* (1926) — the foundational case for treating probability as a property of a *person's* belief rather than a property of the world: a number you can elicit, score, and improve by checking your bets against outcomes. The calibration disciplines this chapter installs are Ramsey's, applied to AI systems whose reported confidence the user has been treating as a property of the world rather than a property of the model's belief.

![Frank P. Ramsey, c. 1925. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/frank-ramsey.jpg)
*Frank P. Ramsey, c. 1925. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Frank Ramsey, and how does his account of *subjective probability* — probability as a coherent number attached to a person's belief, scored by checking bets against outcomes — connect to the problem of an AI that reports high confidence when it should not? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Frank Ramsey philosopher"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *Dutch book arguments* in plain language, as if you've never seen a probability axiom
- Ask it to compare Ramsey's elicit-and-score method to the calibration loop this chapter requires
- Add a constraint: "Answer as if you're writing the rationale for measuring an LLM's calibration with a Brier score"

What changes? What gets better? What gets worse?
""",
    },

    "03-bias-where-it-enters-and-who-is-responsible.md": {
        "old_subject": "Hannah Arendt",
        "new_subject": "Hannah Arendt",
        "stub_filename": "hannah-arendt.jpg",
        "era": "c. 1950s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Hannah Arendt** spent the postwar decades arguing — most famously in *Eichmann in Jerusalem* (1963) — that systemic harm is rarely the work of monstrous individuals. It is the predictable output of a system whose roles, rules, and routines diffuse responsibility across so many actors that no single one feels accountable for the result. The chapter's question — *where bias enters and who is responsible* — is Arendt's question, restated for a pipeline whose participants include data brokers, annotators, modelers, deployers, and a model that is not, itself, a moral agent.

![Hannah Arendt, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/hannah-arendt.jpg)
*Hannah Arendt, c. 1950s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Hannah Arendt, and how does her account of *the banality of evil* — that systemic harm is produced by the diffuse, role-bound action of many people none of whom would do it alone — connect to the question of where bias enters an AI pipeline and who bears responsibility for it? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Hannah Arendt"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *the banality of evil* in plain language, as if you've never read postwar political theory
- Ask it to compare Arendt's analysis of role-bound action to a multi-actor ML pipeline (data brokers, annotators, modelers, deployers)
- Add a constraint: "Answer as if you're writing the accountability section of a model card"

What changes? What gets better? What gets worse?
""",
    },

    "06-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md": {
        "old_subject": "Hans Reichenbach",
        "new_subject": "Hans Reichenbach",
        "stub_filename": "hans-reichenbach.jpg",
        "era": "c. 1940s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Hans Reichenbach** drew the distinction the chapter rests on — between the *context of discovery* (how a model arrived at an output) and the *context of justification* (the reasons that would, post hoc, defend it) — in *Experience and Prediction* (1938). A post-hoc explanation of a black-box model is in the second category dressed up as the first. Reichenbach's argument is that the dressing-up is not innocent: a justification that did not actually drive the conclusion is not the same intellectual object as the process that did, and treating them as the same is how communities convince themselves they understand what they only know how to defend.

![Hans Reichenbach, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/hans-reichenbach.jpg)
*Hans Reichenbach, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Hans Reichenbach, and how does his distinction between the *context of discovery* and the *context of justification* connect to distinguishing genuine model explanation from a post-hoc rationalization that did not actually drive the model's output? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Hans Reichenbach"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *context of discovery vs. context of justification* in plain language, as if you've never read philosophy of science
- Ask it to compare Reichenbach's distinction to the gap between SHAP attributions and the actual computation a deep network ran
- Add a constraint: "Answer as if you're writing the warning label on a post-hoc explanation tool"

What changes? What gets better? What gets worse?
""",
    },

    "07-fairness-metrics-choosing-a-definition-and-defending-it.md": {
        "old_subject": "John Stuart Mill",
        "new_subject": "John Stuart Mill",
        "stub_filename": "john-stuart-mill.jpg",
        "era": "c. 1860s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **John Stuart Mill** spent the middle of the nineteenth century arguing that *fairness* is not a single quantity. *Utilitarianism* (1861) defends the claim that the right act maximizes aggregate well-being; *On Liberty* (1859) argues that some individual claims cannot be overridden no matter how much aggregate well-being would result. The two arguments are not reconcilable in a single metric — and Mill knew it. The chapter's central move is the same one Mill modeled: choose the fairness definition that fits the harm structure of your specific problem, defend the choice in writing, and accept that the alternative definitions you ruled out would also have been defensible under a different harm structure.

![John Stuart Mill, c. 1860s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-stuart-mill.jpg)
*John Stuart Mill, c. 1860s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John Stuart Mill, and how does the unresolved tension between his *Utilitarianism* and *On Liberty* connect to choosing one fairness metric for an ML system and defending it against the alternatives that a different harm structure would have privileged? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Stuart Mill"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why an *aggregate-welfare* fairness metric and an *individual-claim* fairness metric can both be defensible, in plain language
- Ask it to compare Mill's harm-principle to the case for individual fairness over group fairness in a specific deployment
- Add a constraint: "Answer as if you're writing the *defense* paragraph in a model card's fairness section"

What changes? What gets better? What gets worse?
""",
    },

    "08-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md": {
        "old_subject": "John von Neumann",
        "new_subject": "John von Neumann",
        "stub_filename": "john-von-neumann.jpg",
        "era": "c. 1940s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **John von Neumann** co-wrote *Theory of Games and Economic Behavior* in 1944 — the formal account of what happens when a system optimizes against another system that is optimizing against it. Adversarial robustness is a game-theoretic problem before it is an ML problem: a model that aces the clean benchmark and fails on a one-pixel perturbation has not been beaten by random noise. It has been beaten by an adversary that searched the model's input space for the cheapest move that changes the output. Von Neumann's framework is the older language for what the chapter is teaching: the model's accuracy on a held-out set is a strategy that holds up against a non-adversarial nature, not against a player.

![John von Neumann, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-von-neumann.jpg)
*John von Neumann, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John von Neumann, and how does the game-theoretic framing he co-developed in *Theory of Games and Economic Behavior* connect to the idea that a model's accuracy on a clean benchmark is not the same thing as understanding — that it is a strategy against a non-adversarial environment, not against a player? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John von Neumann"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *minimax* in plain language, as if you've never seen game theory
- Ask it to compare a one-pixel adversarial attack to a minimax search in the input space
- Add a constraint: "Answer as if you're writing the threat model for a deployed image classifier"

What changes? What gets better? What gets worse?
""",
    },

    "09-validating-agentic-ai-when-autonomous-systems-misbehave.md": {
        "old_subject": "Maurice Merleau-Ponty",
        "new_subject": "Maurice Merleau-Ponty",
        "stub_filename": "maurice-merleau-ponty.jpg",
        "era": "c. 1950s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Maurice Merleau-Ponty** wrote *Phenomenology of Perception* (1945) to argue that purposive action is not the execution of a pre-computed plan; it is a moment-by-moment adjustment carried out by a body that is already inside the situation, sensing it, responding to it, revising what it is doing. An agent that has no body in the situation — that has only the plan, only the tool calls, only the next-token prediction — fails the way the chapter's case studies fail: not in the plan but in the gap between the plan and the situation the plan did not anticipate.

![Maurice Merleau-Ponty, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/maurice-merleau-ponty.jpg)
*Maurice Merleau-Ponty, c. 1950s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Maurice Merleau-Ponty, and how does his account of *embodied, situated action* — that purposive behavior is moment-by-moment adjustment, not the execution of a pre-computed plan — connect to why agentic AI systems misbehave when deployed outside the conditions their designers imagined? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Maurice Merleau-Ponty"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *situated action* in plain language, as if you've never read phenomenology
- Ask it to compare Merleau-Ponty's account of bodily presence to the absence of bodily presence in a tool-calling agent
- Add a constraint: "Answer as if you're writing a pre-deployment review of a customer-service agent's failure modes"

What changes? What gets better? What gets worse?
""",
    },

    "10-delegation-trust-and-the-supervisory-role.md": {
        "old_subject": "Donald Broadbent",
        "new_subject": "Donald Broadbent",
        "stub_filename": "donald-broadbent.jpg",
        "era": "c. 1960s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Donald Broadbent** ran the Applied Psychology Unit at Cambridge from 1958 to 1974 and produced the foundational work — *Perception and Communication* (1958), *Decision and Stress* (1971) — on how human attention degrades under monotony, low signal rate, and the structural conditions that supervisory roles tend to produce. The paradox of the well-running automated system is, in Broadbent's vocabulary, a vigilance problem: the rare event the supervisor is supposed to catch is rare specifically because the system runs well, and the supervisor's attentional capacity for that rare event has been quietly eroded by the monotony of the long stretches in between.

![Donald Broadbent, c. 1960s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/donald-broadbent.jpg)
*Donald Broadbent, c. 1960s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Donald Broadbent, and how does his work on *vigilance and attention under low-signal conditions* connect to the supervisory role a person actually has when they're delegating to an AI tool that mostly works — and whose rare failures are the ones the supervisor is supposed to catch? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Donald Broadbent"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *vigilance decrement* in plain language, as if you've never read attention research
- Ask it to compare Broadbent's filter model of attention to the supervisor of a 99.5%-correct AI system
- Add a constraint: "Answer as if you're writing the staffing rationale for a human-in-the-loop deployment"

What changes? What gets better? What gets worse?
""",
    },

    "12-communicating-uncertainty-calibrating-claims-to-evidence.md": {
        "old_subject": "Florence Nightingale",
        "new_subject": "Florence Nightingale",
        "stub_filename": "florence-nightingale.jpg",
        "era": "c. 1860s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Florence Nightingale** spent the 1850s building — and the 1860s defending — the first sustained public-policy argument that combined explicit statistical evidence with deliberately legible visual communication. Her *coxcomb* polar-area diagrams of Crimean mortality were not decoration; they were the calibrated visual translation of an uncertain estimate into a claim a Parliament could read at the right level of confidence and act on. The chapter's argument — that communicating uncertainty honestly is itself a craft, distinct from running the analysis — is Nightingale's working method, applied to AI outputs whose audiences are usually less statistically literate than the Parliament she addressed.

![Florence Nightingale, c. 1860s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/florence-nightingale.jpg)
*Florence Nightingale, c. 1860s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Florence Nightingale, and how does her use of statistical visualization to communicate uncertain estimates to non-statistical audiences (Parliament, the War Office) connect to the craft of honestly communicating an AI system's confidence to a non-technical audience? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Florence Nightingale"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why *visual* statistical communication can be either honest or misleading, in plain language
- Ask it to compare Nightingale's coxcomb diagrams to the visualization choices in this chapter for an AI confidence interval
- Add a constraint: "Answer as if you're writing the public-facing summary of a model's uncertainty for a non-technical executive"

What changes? What gets better? What gets worse?
""",
    },

    "13-accountability-who-is-responsible-when-the-system-fails.md": {
        "old_subject": "John Dewey",
        "new_subject": "John Dewey",
        "stub_filename": "john-dewey.jpg",
        "era": "c. 1920s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **John Dewey** spent the 1920s working out — most fully in *The Public and Its Problems* (1927) — what accountability requires when a harm is produced by an extended chain of indirect consequences that no single actor intended or even fully understood. His answer, briefly: a *public* forms whenever the indirect consequences of joint action are recognized and made traceable; a public that has not yet recognized the chain cannot hold anyone accountable; and the work of recognizing the chain is itself prior to the work of assigning responsibility. The chapter's argument that accountability for AI failures is a problem of *making the chain visible* before it is a problem of assigning blame is Dewey's argument, applied a century later.

![John Dewey, c. 1920s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/john-dewey.jpg)
*John Dewey, c. 1920s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was John Dewey, and how does his account of *the public* — formed by tracing the indirect consequences of joint action — connect to the question of who is responsible when an AI system fails after a long, distributed chain of design and deployment decisions? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Dewey"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *indirect consequences as the unit of accountability* in plain language, as if you've never read pragmatist philosophy
- Ask it to compare Dewey's *public* to the multi-stakeholder community that ought to be accountable for an AI deployment's downstream harms
- Add a constraint: "Answer as if you're writing the accountability map for a post-incident review"

What changes? What gets better? What gets worse?
""",
    },

    "14-the-limits-of-ai-what-the-tools-cannot-do.md": {
        "old_subject": "Alan Turing",
        "new_subject": "Alan Turing",
        "stub_filename": "alan-turing.jpg",
        "era": "c. 1940s",
        "block": """## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Alan Turing** named both the proof of fundamental limits and the test that has been most often used to argue past them. The 1936 paper *On Computable Numbers* established that some questions cannot be decided by any algorithmic procedure — there are problems no Turing machine can solve, regardless of speed. The 1950 paper *Computing Machinery and Intelligence* proposed the imitation game, which Turing offered as a *replacement* for the question *can machines think?* — a replacement specifically because Turing thought the original question was too vague to settle. The chapter's argument is in his lineage: there are limits the math forbids, and there are limits the test cannot detect, and the practitioner has to know the difference.

![Alan Turing, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/alan-turing.jpg)
*Alan Turing, c. 1940s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Alan Turing, and how do his two contributions — the halting-problem proof in *On Computable Numbers* (1936) and the imitation game in *Computing Machinery and Intelligence* (1950) — together describe the limits of what AI tools cannot do, even when they appear to be doing it well? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Alan Turing"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain why *the halting problem* is a fundamental limit, in plain language, as if you've never seen a Turing machine
- Ask it to compare a passing imitation-game performance to a system that is genuinely doing the task it appears to be doing
- Add a constraint: "Answer as if you're writing the *out of scope* section for an AI tool's documentation"

What changes? What gets better? What gets worse?
""",
    },
}


# Kept chapters: insert portrait stub only
KEPT = {
    "04-the-frictional-method-evidence-of-learning-when-ai-can-generate-the-artifact.md": (
        "Lev Vygotsky",
        "lev-vygotsky.jpg",
        "c. 1930",
    ),
    "05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md": (
        "Suzanne Briet",
        "suzanne-briet.jpg",
        "c. 1950s",
    ),
    "11-visualization-under-validation-honest-misleading-and-the-choices-between.md": (
        "W. E. B. Du Bois",
        "w-e-b-du-bois.jpg",
        "c. 1900",
    ),
}


PORTRAIT_STUB = '![{name}, {era}. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](images/{filename})\n*{name}, {era}. AI-generated portrait based on a public domain photograph.*'


def replace_block(filename, new_block):
    path = CH / filename
    text = path.read_text()
    m = re.search(r'^## AI Wayback Machine\s*$', text, re.MULTILINE)
    if not m:
        print(f"!!! no Wayback section in {filename}")
        return False
    sec_start = m.start()
    next_h2 = re.search(r'\n## ', text[sec_start + 1:])
    sec_end = sec_start + 1 + next_h2.start() + 1 if next_h2 else len(text)
    new_text = text[:sec_start] + new_block.rstrip() + "\n"
    if sec_end < len(text):
        new_text += text[sec_end:]
    path.write_text(new_text)
    return True


def insert_stub_in_kept(filename, name, fn, era):
    path = CH / filename
    text = path.read_text()
    if PORTRAIT_STUB.split(']')[0][:30] in text and fn in text:
        print(f"  stub already in {filename}")
        return False
    sec_idx = text.index("## AI Wayback Machine")
    run_idx = text.index("**Run this:**", sec_idx)
    stub = PORTRAIT_STUB.format(name=name, era=era, filename=fn)
    before = text[:run_idx].rstrip() + "\n\n" + stub + "\n\n"
    new_text = before + text[run_idx:]
    path.write_text(new_text)
    return True


def main():
    print("=== replacements ===")
    for fn, info in REPLACEMENTS.items():
        ok = replace_block(fn, info["block"])
        if ok:
            print(f"  replaced {info['old_subject']} → {info['new_subject']} in {fn}")

    print("\n=== kept-chapter portrait stubs ===")
    for fn, (name, img, era) in KEPT.items():
        ok = insert_stub_in_kept(fn, name, img, era)
        if ok:
            print(f"  inserted stub for {name} in {fn}")


if __name__ == '__main__':
    main()
