[🏠 Roadmap home](../README.md)

---

<a id="practitioner-track"></a>
## 🚀 Practitioner Track (Fast Lane)

> **Read this before you decide the roadmap is too long.** The full curriculum above is a *proof-literate* path: it front-loads mathematics so that by Module 13 you can read a derivation and by Module 26 you can write one. That is the correct path for research, graduate study, and roles where you must invent methods rather than apply them.
>
> It is **not** the only defensible path, and for a large share of 2026 job postings it is not the fastest one. This section is the parallel on-ramp for people whose goal is to be **employed building systems**, not to be able to prove convergence.

> **Citations on this page.** *"video 1 (01:09)"* and similar are resolved in [sources](sources.md#citation-key).

### Why this track exists

Three independent practitioner sources — an [ML Engineer path from a Twitch senior applied scientist](https://www.youtube.com/watch?v=UZ_rK9gzVSc), a [breaking-into-AI/ML account from an Amazon applied scientist](https://www.youtube.com/watch?v=FeQZmQMffzc), and an [AI-Engineer reading list from an ex-Coursera/Amazon engineer](https://www.youtube.com/watch?v=Pr9oRVtAqCM) — converge on the same three claims:

1. **Intuition beats derivation for applied work.** "The math you actually need is way less than people make it sound" (video 1, 01:09). "You need intuition, not derivation skills. Get the concepts down and then move forward" (video 3, 04:47). Both speakers report never hand-deriving a chain rule in years of industry practice.
2. **Shipping beats studying.** Hiring managers "don't need to see that you've *studied*; they need to see that you can do the job" (video 1, 06:23). Repos full of course exercises and Kaggle notebooks with hand-fed data are explicitly called weak signals (video 1, 06:10).
3. **The applied-AI layer is now its own discipline.** "Unlike data scientists or machine learning engineers who train models from scratch, AI engineers build applications using pre-trained models… Their toolkit is mostly prompt engineering, RAG, fine-tuning, and agents" (video 3, 00:53).

**We present both doctrines rather than choosing between them.** The trade-off is explicit and stated at each step below.

### The 6–9 month sequence

Assumes 15–20 hrs/week. Each stage ends with a shipped artifact, not a completion certificate.

| # | Stage | Duration | What you do | Full-track equivalent | What you give up |
|---|---|---|---|---|---|
| **1** | **Python to working fluency** | Weeks 1–14 | [Module 1 Phase 1–3](../curriculum/1-foundations.md#module-1) using the [free-course matrix](../curriculum/1-foundations.md#python-course-matrix); ship a CLI tool and an API-consuming app | M1 (complete) | Nothing — M1 is shared by both tracks |
| **2** | **Math *intuition only*** | Weeks 8–16 (parallel) | [3Blue1Brown Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) + [Essence of Calculus](https://www.3blue1brown.com/topics/calculus) + [StatQuest](https://statquest.org/) + the [Manga Guides](../resources/books.md#practitioner-shelf) | M0, M2, M3, M5 | **Proof literacy.** You will not be able to read PRML/ESL derivations. See the ⚡ callouts in each math module |
| **3** | **Classical ML at sklearn level** | Weeks 14–24 | [Andrew Ng ML Specialization](https://www.coursera.org/specializations/machine-learning-introduction) (free audit) + [Microsoft ML for Beginners](companion-curricula.md#companion-curricula) + StatQuest; concept-level [M9](../curriculum/3-classical-ml.md#module-9)–[M12](../curriculum/3-classical-ml.md#module-12) | M9–M12 with derivations | The ability to derive estimators or diagnose a model from first principles |
| **4** | **From-scratch NumPy implementations** | Weeks 24–28 | Implement **logistic regression, K-Means, and a decision tree** in pure NumPy — the specific three named in video 1 (05:05–05:13) | — | Nothing; this *adds* depth the fast lane would otherwise miss |
| **5** | **AI-Engineer stack** | Weeks 28–40 | Prompt engineering → [M21 RAG](../curriculum/6-frontier-production.md#module-21) → [M22 agents/MCP](../curriculum/6-frontier-production.md#module-22) → evals → fine-tuning basics ([M18](../curriculum/6-frontier-production.md#module-18)) | M18, M21–M23 | Training-from-scratch and alignment-research depth |
| **6** | **Production wrap** | Weeks 36–44 | [M24](../curriculum/6-frontier-production.md#module-24) subset: Docker, CI/CD, MLflow or W&B, monitoring, a real deployment. Meet the [Minimum Production Bar](../curriculum/6-frontier-production.md#production-bar) | M24 (complete) | Platform-scale infrastructure and SLO engineering |

### Stage 4 in detail — the from-scratch discipline

This is the fast lane's substitute for proof work, and it is non-negotiable. Video 1 (05:01–05:15) shows the exact shape expected: a class exposing `__init__`, `sigmoid`, `fit` (containing the gradient-descent loop), and `predict`. Writing that loop yourself is what converts "I watched a video about gradient descent" into "I know what the gradient is doing to the weights."

```
LogisticRegressionScratch
├── __init__(self, lr, n_iters)   # hyperparameters, weights=None, bias=None
├── sigmoid(self, z)              # 1 / (1 + np.exp(-z))
├── fit(self, X, y)               # gradient-descent loop: forward → dw, db → update
└── predict(self, X)              # sigmoid(Xw + b) thresholded at 0.5
```

Do the same for **K-Means** (assignment step / update step / inertia) and a **decision tree** (impurity criterion, best-split search, recursive build, prediction traversal). Then check each against the scikit-learn equivalent on the same data and explain any divergence.

### When you must come back to the math spine

The fast lane is a *loan*, not a discount. Repay it if you:

- want to read or write papers, or enter [M13](../curriculum/4-probabilistic-ml.md#module-13) Bayesian derivations, [M16](../curriculum/5-deep-learning.md#module-16) architecture theory, or [M17](../curriculum/5-deep-learning.md#module-17) RL proofs;
- interview for research scientist, applied scientist, or PhD-track roles;
- need to debug a model whose failure mode is mathematical rather than engineering (identifiability, ill-conditioning, non-convergence);
- find yourself unable to evaluate whether a paper's claim is sound.

At that point return to [M0](../curriculum/1-foundations.md#module-0) → [M2](../curriculum/1-foundations.md#module-2) → [M3](../curriculum/1-foundations.md#module-3) → [M5](../curriculum/1-foundations.md#module-5) in order. The material is unchanged and waiting.

### Honest timeline

| Source | Claim | Conditions |
|---|---|---|
| [Scrimba, *How to Learn Python* (2026)](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) | 9–12 months to entry-level job-ready | Measures *Python* job-readiness (data analyst, junior backend, junior ML), assumes a portfolio, 5–10 hrs/week |
| [Video 2, 04:56](https://www.youtube.com/watch?v=FeQZmQMffzc) | 18 / 24 / 36 months for a career transition | Measures a *career change* into AI/ML from a non-tech background, in a market where juniors compete with laid-off senior engineers |
| This roadmap (full track) | 24–36 months at 20–25 hrs/week | Complete path including the math spine and capstone |

These are not in conflict; they measure different finish lines. Use the shorter figure if you already work in tech and are adding a skill. Use the longer figure if you are changing careers. See [Career Operations](career-operations.md#career-operations) for how to operate inside that window.

---

[🏠 Roadmap home](../README.md)
