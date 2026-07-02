# Chapter 1 — Original ↔ New Draft Crosswalk

**Verdict.** The new draft (`_ch1-what-i-mean-by-skepticism.md`) is *not* a new chapter — it is the original chapter's essay body with five documented real-world cases spliced into the moves. It reads like an article because it dropped every piece of chapter scaffolding the original has. So the merge is one-directional: **keep the original chapter whole; pull only the five cases across.** Nothing else in the new draft is net-new.

---

## Section-by-section map

Order follows the original (`01-the-skeptics-toolkit.md`).

| # | Section | Original | New draft | Action |
|---|---|:--:|:--:|---|
| 1 | Title + TL;DR | ✅ | ❌ | Keep original |
| 2 | **Cold open** — Epic Sepsis Model (Wong 2021) + Ash / *Agents of Chaos* | ✅ | ❌ | **Keep — this is the hook.** The chapter's whole "statistically valid, wrong about the question that matters" thesis lives here |
| 3 | Composite patient (49-yo, swollen leg → clot) | ✅ | ❌ | Keep — the labeled illustration the rest of the chapter returns to |
| 4 | Learning objectives / prerequisites / "why this chapter first" | ✅ | ❌ | Keep |
| 5 | "What I mean by skepticism" (intro paras) | ✅ | ✅ | Identical — no change |
| 6 | **Descartes** — radical doubt | ✅ | ✅ + **Knight Capital (2012)** | **Splice case in.** New paragraph: "deployment succeeded" true of the command, false of the running system; $440M/45 min (SEC 2013) |
| 7 | Fig 1.1 (Cartesian inspection protocol) | ✅ | caption only | Keep original image ref |
| 8 | **Hume** — limit of induction (Taleb's turkey) | ✅ | ✅ + **Zillow + Google Flu Trends** | **Splice case in.** New paragraph: two deployed "turkeys" whose correlations held until the distribution moved (Zillow/CNN 2021; Lazer *Science* 2014) |
| 9 | Fig 1.2 (turkey timeline) | ✅ | caption only | Keep original image ref |
| 10 | **Popper** — falsifiability | ✅ | ✅ + **Epic Sepsis falsification callback** | **Splice, but as a CALLBACK.** ⚠️ Epic Sepsis is already the cold open (row 2) — the Popper paragraph must reference it ("the sepsis model we opened with"), not re-introduce it. New draft re-introduces it; fix on merge |
| 11 | Rhetorical-claim → engineering-correction table | ✅ | ✅ | Identical |
| 12 | Fig 1.3 (three moves checklist) | ✅ | caption only | Keep original image ref |
| 13 | **The cave** — Plato / artifact–world | ✅ | ✅ + **DeGrave COVID X-ray + COMPAS** | **Splice case in.** New paragraph: the confident label was a shadow of dataset provenance, not lung pathology (DeGrave *Nat. Mach. Intell.* 2021); COMPAS as second example (ProPublica 2016) |
| 14 | Fig 1.4 (two-column split) | ✅ | caption only | Keep original image ref |
| 15 | The solve-verify asymmetry | ✅ | ✅ | Identical |
| 16 | Fig 1.5 (cost asymmetry) | ✅ | caption only | Keep |
| 17 | The Five Supervisory Capacities + table | ✅ | ✅ | Identical |
| 18 | The fluency trap | ✅ | ✅ | Identical |
| 19 | Fig 1.6 (fluency trap mechanism) | ✅ | caption only | Keep |
| 20 | Skepticism as a team practice | ✅ | ✅ | Identical |
| 21 | Fig 1.7 (workflow diagram) | ✅ | caption only | Keep |
| 22 | **Meet Ash — a longitudinal case** (the "Pebble") | ✅ | ❌ | **Keep** — sets up the returns in Chs 3–9 |
| 23 | The shape of the rest | ✅ | ❌ | Keep |
| 24 | "What would change my mind" / "Still puzzling" | ✅ | ❌ | Keep — the intellectual-honesty coda |
| 25 | Exercises (Glimmers, Warm-Up, Application, Synthesis, Challenge) | ✅ | ❌ | **Keep** — the pedagogical core |
| 26 | LLM Exercise (Red-Team Casebook + paste prompt) | ✅ | ❌ | Keep |
| 27 | AI Wayback Machine (Popper) | ✅ | ❌ | Keep |
| 28 | Prompts (D3 figure generation) | ✅ | ❌ | Keep |

---

## What the new draft actually adds

Only five things — the documented, cited cases that turn abstract moves into engineering history:

| Move | Case added | Load-bearing figures | Citation |
|---|---|---|---|
| Descartes | **Knight Capital** deployment | $440M lost in ~45 min; dead "Power Peg" code reactivated by a reused flag on 1 of 8 servers | SEC administrative proceeding, 2013 |
| Hume | **Zillow Offers** | ~7,000 homes overbought; program shut Nov 2021; >$500M write-down; ~25% of staff cut | Zillow Q3 2021 letter; CNN Business, 2 Nov 2021 |
| Hume | **Google Flu Trends** | Over-predicted flu in 100 of 108 weeks (Aug 2011–Sep 2013); ~2× CDC at the 2012–13 peak | Lazer, Kennedy, King & Vespignani, *Science*, 2014 |
| Popper | **Epic Sepsis Model** (as falsification example) | ~2 in 3 sepsis cases missed; 18% alert rate; 27,697 patients | Wong et al., *JAMA Internal Medicine*, 2021 |
| The cave | **COVID chest-X-ray shortcut** (+ COMPAS) | Models keyed on lead markers / dataset provenance, not lung pathology; failed across hospitals | DeGrave, Janizek & Lee, *Nat. Mach. Intell.*, 2021 |

Every figure above is web-verified.

---

## Why it "reads like an article, not a chapter"

The article-vs-chapter gap is entirely rows 1–4 and 22–28: the original wraps the same argument in a **cold open that states the thesis through two real failures**, **explicit learning objectives**, a **recurring illustration** (the composite patient), a **longitudinal case** that threads through six later chapters, **graduated exercises**, an **LLM red-team project**, and the **Wayback Machine**. Strip those and you get a well-written essay. The new draft stripped them.

One caution the merge must handle: the new draft re-introduces the Epic Sepsis Model inside the Popper section as if the reader hasn't met it — but the original already opens with it. On merge, the Popper paragraph becomes a **callback** ("the sepsis model we opened with was *unrefuted*, not validated"), which is actually stronger: it closes the loop on the cold open.

---

## Recommended merge (one file: `01-the-skeptics-toolkit.md`)

1. Leave the original chapter's structure fully intact (rows 1–28).
2. Insert the **Knight Capital** paragraph into Descartes (after the "inspection protocol" para, before Fig 1.1).
3. Insert the **Zillow + Google Flu** paragraph into Hume (after the "AI trained on a hospital's historical cases" para).
4. Insert the **Epic Sepsis callback** paragraph into Popper (after the "under what conditions would I expect this to be wrong" para) — phrased as a callback to the cold open.
5. Insert the **DeGrave + COMPAS** paragraph into the cave (after the "world was on a gurney" para, before Fig 1.4).
6. Retire `_ch1-what-i-mean-by-skepticism.md` and `_expanded-four-moves.md` — both are now fully absorbed.

Net effect: same chapter, four new documented cases, no lost scaffolding.
