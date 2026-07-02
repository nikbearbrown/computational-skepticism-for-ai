# Mini-Bio Source — John von Neumann (Chapter 4)

Target: 3–5 minute "mini-bio" Unreal Reels video (see MINIBIO-PROMPT.md).
Extracted from: chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md (AI Wayback Machine section, removed from chapter 2026-07-02).
Status: source material — mini-bio script not yet generated.

---

The ideas in this chapter didn't appear from nowhere. **John von Neumann** co-wrote *Theory of Games and Economic Behavior* in 1944 — the formal account of what happens when a system optimizes against another system that is optimizing against it. Adversarial robustness is a game-theoretic problem before it is an ML problem: a model that aces the clean benchmark and fails on a one-pixel perturbation has not been beaten by random noise. It has been beaten by an adversary that searched the model's input space for the cheapest move that changes the output. Von Neumann's framework is the older language for what the chapter is teaching: the model's accuracy on a held-out set is a strategy that holds up against a non-adversarial nature, not against a player.

![John von Neumann, c. 1940s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](../images/john-von-neumann.jpg)
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

