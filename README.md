<div align="center">

<img src="assets/hero-banner.jpg" alt="Data Science and AI Roadmap - foundations to production AI" width="100%">

# Data Science & AI Roadmap

### A rigorous, free-first path from foundations to production AI

[![Version](https://img.shields.io/badge/version-2026.3%20Practitioner's%20Pass-blue)](#refresh-log)
[![Modules](https://img.shields.io/badge/modules-27-6f42c1)](#roadmap)
[![Level](https://img.shields.io/badge/level-beginner%20to%20advanced-0969da)](#who-this-is-for)
[![Resources](https://img.shields.io/badge/resources-free--first-1a7f37)](#how-to-use-this-roadmap)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-lightgrey)](LICENSE.md)

**Mathematics · Statistics · Machine Learning · Data Engineering · Deep Learning · LLMs · Production AI**

[Start here](#start-here) · [Fast lane](#practitioner-track) · [Choose a track](#choose-your-track) · [Browse modules](#roadmap) · [Companion curricula](#companion-curricula) · [Books](#books) · [Toolchain](#toolchain) · [Career ops](#career-operations) · [Progress tracker](#progress-tracker)

</div>

---

## Goal

This roadmap turns high-quality university syllabi and open learning resources into one prerequisite-aware curriculum. It is designed to help you:

- build strong mathematical, statistical, and programming foundations;
- learn classical machine learning before jumping to frontier models;
- ship real systems with data engineering, MLOps, RAG, agents, and evaluation;
- finish with a portfolio-ready research, systems, or applied capstone.

The curriculum is detailed by design, but the navigation is intentionally simple: **choose a track, follow the modules in order, and build as you learn.**

## Who this is for

- **Beginners** who want a complete path and are willing to fill prerequisite gaps.
- **Data analysts and data scientists** strengthening statistics, experimentation, and modelling.
- **ML and AI engineers** building production-grade model and LLM systems.
- **Experienced practitioners** using individual modules for focused study or interview review.
- **Research-oriented learners** preparing for graduate-level machine learning work.

> **Expected commitment:** roughly 24–36 months at 20–25 hours per week for the complete path. You do not need to complete every module for a role-focused track.

## How to use this roadmap

1. **Take the [math diagnostic](#math-diagnostic).** Complete Module 0 if any foundation is weak.
2. **Choose a destination** in the role-track table below instead of studying everything by default.
3. **Respect prerequisites.** Each module states what you should know before starting.
4. **Use one primary course and one primary book.** Treat the remaining links as alternatives or references.
5. **Build every mandatory project.** Passive course completion is not enough.
6. **Track your work** with the [progress checklist](#progress-tracker).
7. **Finish with a capstone** that matches your intended role.

<a id="start-here"></a>
## Start here

Use the shortest entry point that matches your current experience. You can return to the full curriculum whenever you need more depth.

| If you are... | Start with | Then continue to |
|---|---|---|
| **New to programming and data** | [Microsoft Data Science for Beginners](#companion-curricula), then [M1](#module-1) | [M5](#module-5) → [M6](#module-6) → [M7](#module-7) → [M8a](#module-8a) |
| **Comfortable with Python, new to ML** | [Microsoft ML for Beginners](#companion-curricula) alongside [M9](#module-9) | M9 → [M10](#module-10) → [M11](#module-11) → [M12](#module-12) |
| **An analyst moving into data science** | [M5](#module-5) → [M6](#module-6) → [M7](#module-7) | [M9](#module-9) → [M14](#module-14) → [M25](#module-25) |
| **An ML practitioner moving into production AI** | [M8b](#module-8b) and [M24](#module-24) | [M18](#module-18) → [M21](#module-21) → [M22](#module-22) → [M23](#module-23) |
| **Preparing for research** | [Math diagnostic](#math-diagnostic) | Follow M0–M18 in order, then [M23](#module-23) and the [research capstone](#module-26) |

> **First milestone:** complete one small project before collecting more resources. The Microsoft companion courses below supply guided lessons, quizzes, assignments, and solutions; this roadmap supplies the deeper prerequisite and production sequence.

<a id="practitioner-track"></a>
## 🚀 Practitioner Track (Fast Lane)

> **Read this before you decide the roadmap is too long.** The full curriculum above is a *proof-literate* path: it front-loads mathematics so that by Module 13 you can read a derivation and by Module 26 you can write one. That is the correct path for research, graduate study, and roles where you must invent methods rather than apply them.
>
> It is **not** the only defensible path, and for a large share of 2026 job postings it is not the fastest one. This section is the parallel on-ramp for people whose goal is to be **employed building systems**, not to be able to prove convergence.

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
| **1** | **Python to working fluency** | Weeks 1–14 | [Module 1 Phase 1–3](#module-1) using the [free-course matrix](#python-course-matrix); ship a CLI tool and an API-consuming app | M1 (complete) | Nothing — M1 is shared by both tracks |
| **2** | **Math *intuition only*** | Weeks 8–16 (parallel) | [3Blue1Brown Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) + [Essence of Calculus](https://www.3blue1brown.com/topics/calculus) + [StatQuest](https://statquest.org/) + the [Manga Guides](#practitioner-shelf) | M0, M2, M3, M5 | **Proof literacy.** You will not be able to read PRML/ESL derivations. See the ⚡ callouts in each math module |
| **3** | **Classical ML at sklearn level** | Weeks 14–24 | [Andrew Ng ML Specialization](https://www.coursera.org/specializations/machine-learning-introduction) (free audit) + [Microsoft ML for Beginners](#companion-curricula) + StatQuest; concept-level [M9](#module-9)–[M12](#module-12) | M9–M12 with derivations | The ability to derive estimators or diagnose a model from first principles |
| **4** | **From-scratch NumPy implementations** | Weeks 24–28 | Implement **logistic regression, K-Means, and a decision tree** in pure NumPy — the specific three named in video 1 (05:05–05:13) | — | Nothing; this *adds* depth the fast lane would otherwise miss |
| **5** | **AI-Engineer stack** | Weeks 28–40 | Prompt engineering → [M21 RAG](#module-21) → [M22 agents/MCP](#module-22) → evals → fine-tuning basics ([M18](#module-18)) | M18, M21–M23 | Training-from-scratch and alignment-research depth |
| **6** | **Production wrap** | Weeks 36–44 | [M24](#module-24) subset: Docker, CI/CD, MLflow or W&B, monitoring, a real deployment. Meet the [Minimum Production Bar](#production-bar) | M24 (complete) | Platform-scale infrastructure and SLO engineering |

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

- want to read or write papers, or enter [M13](#module-13) Bayesian derivations, [M16](#module-16) architecture theory, or [M17](#module-17) RL proofs;
- interview for research scientist, applied scientist, or PhD-track roles;
- need to debug a model whose failure mode is mathematical rather than engineering (identifiability, ill-conditioning, non-convergence);
- find yourself unable to evaluate whether a paper's claim is sound.

At that point return to [M0](#module-0) → [M2](#module-2) → [M3](#module-3) → [M5](#module-5) in order. The material is unchanged and waiting.

### Honest timeline

| Source | Claim | Conditions |
|---|---|---|
| [Scrimba, *How to Learn Python* (2026)](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) | 9–12 months to entry-level job-ready | Measures *Python* job-readiness (data analyst, junior backend, junior ML), assumes a portfolio, 5–10 hrs/week |
| [Video 2, 04:56](https://www.youtube.com/watch?v=FeQZmQMffzc) | 18 / 24 / 36 months for a career transition | Measures a *career change* into AI/ML from a non-tech background, in a market where juniors compete with laid-off senior engineers |
| This roadmap (full track) | 24–36 months at 20–25 hrs/week | Complete path including the math spine and capstone |

These are not in conflict; they measure different finish lines. Use the shorter figure if you already work in tech and are adding a skill. Use the longer figure if you are changing careers. See [Career Operations](#career-operations) for how to operate inside that window.

## Choose your track

| Track | Recommended modules | Portfolio outcome |
|---|---|---|
| **Data Analyst** | M1 → M6 → M7 → M8a → M25 → M26 | Reproducible analysis, dashboard, and stakeholder memo |
| **Data Scientist** | M1–M7 → M9–M14 → M25 → M26 | Validated model plus causal or experimental evaluation |
| **Data Engineer** | M1 → M4 → M7 → M8a → M8b → M24 → M26 | Tested batch/streaming data platform with observability |
| **ML Engineer** | M1–M12 → M15–M17 → M24 → M26 | Model served behind an API with CI, monitoring, and SLOs |
| **AI Engineer (Applications)** | [Fast lane](#practitioner-track): M1 → M7 → M8a → intuition-level M2/M3/M5 → M18 → M21–M24 → M26 | Deployed product built **on** a foundation model: RAG or agent system with an eval suite, tracing, guardrails, and a cost/latency budget |
| **AI Engineer (Systems/Research-adjacent)** | M1 → M8a → M15–M18 → M21–M24 → M26 | Evaluated RAG or agent system with tracing and guardrails, plus architecture-level understanding of the models it serves |
| **Research / PhD prep** | M0–M18 → M23 → M26 Research Track | Reproducible paper, ablations, and public research artifact |

> **Reading the two AI Engineer rows.** They are different jobs, not seniority levels. The **Applications** row matches the role as defined in [video 3, 00:53](https://www.youtube.com/watch?v=Pr9oRVtAqCM): a software engineer who turns GPT/Claude/Llama into products via prompting, RAG, fine-tuning, and agents, and who does *not* train models from scratch. Its primary text is **Chip Huyen, _AI Engineering: Building Applications with Foundation Models_** (O'Reilly, Jan 2025 — see the [Practitioner Shelf](#practitioner-shelf)). The **Systems** row keeps the deep-learning spine (M15–M17) for people who must also reason about the model internals, not just the API surface. In our [survey of 16 live 2026 postings](#skills-checklist), titles for the Applications row appear as "AI Engineer", "Applied AI Architect", and "Forward Deployed Engineer (GenAI)".

## Roadmap

### Tracks and pacing

- [🚀 Practitioner Track (fast lane, 6–9 months)](#practitioner-track)
- [Choose your track](#choose-your-track)
- [Module projects — the enforcement rule](#module-projects)

### Foundations

- [Math diagnostic and remediation](#math-diagnostic)
- [M0 — Mathematical maturity: pre-calculus, logic, and proof](#module-0)
- [M1 — Programming foundations and computational thinking](#module-1)
- [M2 — Calculus, matrix calculus, and convex optimisation](#module-2)
- [M3 — Linear algebra](#module-3)
- [M4 — Discrete mathematics, algorithms, and data structures](#module-4)
- [M5 — Probability theory](#module-5)

### Statistics and data systems

- [M6 — Statistical inference](#module-6)
- [M6½ — Causal inference and experimentation](#module-6-half)
- [M7 — Data wrangling, EDA, and visualisation](#module-7)
- [M8a — Databases, SQL, and warehouses](#module-8a)
- [M8b — Distributed data and streaming systems](#module-8b)

### Classical machine learning

- [M9 — Regression](#module-9)
- [M10 — Classification and kernel methods](#module-10)
- [M11 — Unsupervised learning and dimensionality reduction](#module-11)
- [M12 — Trees, ensembles, and boosting](#module-12)

### Probabilistic and deep learning

- [M13 — Bayesian inference, graphical models, and MCMC](#module-13)
- [M14 — Sequence modelling and time series](#module-14)
- [M15 — Deep learning foundations](#module-15)
- [M16 — Representation learning, transformers, and generative models](#module-16)
- [M17 — Reinforcement learning and decision-making](#module-17)

### Frontier and production AI

- [M18 — Large language models, RLHF, and alignment](#module-18)
- [M21 — RAG, vector databases, and retrieval](#module-21)
- [M22 — Agentic AI, MCP, and A2A](#module-22)
- [M23 — AI safety, interpretability, evaluations, and policy](#module-23)
- [M24 — MLOps, LLMOps, and AgentOps](#module-24)
- [M25 — Product data science and communication](#module-25)
- [M26 — Capstone: research, systems, or applied](#module-26)

### Reference sections

- [Core textbook list](#books) · [🧰 Practitioner Shelf](#practitioner-shelf)
- [Production toolchain](#toolchain) · [🏁 Minimum Production Bar](#production-bar)
- [🐍 Free Python course matrix](#python-course-matrix)
- [⚖️ Prompting vs RAG vs fine-tuning](#module-21)
- [🧭 Career Operations](#career-operations) · [Skills ↔ job-description mapping](#skills-checklist)
- [Progress tracker](#progress-tracker)
- [🗓️ Refresh log](#refresh-log)
- [Acknowledgements and sources](#acknowledgements)
- [Verification and audit trail](audit/FINAL_AUDIT.md) · [v2026.3 pass](audit/AUDIT_v2026.3.md)

## Curriculum at a glance

<div align="center">

<img src="assets/roadmap-overview.jpg" alt="The six curriculum strata as a left-to-right learning path, from Foundations (M0-M5) to Production AI (M18-M26)" width="100%">

</div>

| Stage | Modules | Main outcome |
|---|---|---|
| **Foundations** | M0–M5 | Proof literacy, Python, calculus, linear algebra, algorithms, probability |
| **Statistics & data** | M6–M8b | Inference, experimentation, EDA, SQL, warehouses, distributed systems |
| **Classical ML** | M9–M12 | Regression, classification, unsupervised learning, ensembles |
| **Probabilistic & deep learning** | M13–M17 | Bayesian modelling, time series, neural networks, transformers, RL |
| **Frontier & production** | M18, M21–M25 | LLMs, RAG, agents, safety, evaluation, MLOps, product thinking |
| **Capstone** | M26 | A public, reproducible portfolio project |

<a id="companion-curricula"></a>
## Guided companion curricula

The two Microsoft curricula below are strong, actively maintained beginner companions. They use the lesson-table navigation, short projects, quizzes, assignments, and solution folders that make a large subject easier to enter. Use their repository root links to follow the newest default-branch content; the reviewed commits provide a dated audit trail.

| Curriculum | Best for | Current scope | Reviewed upstream snapshot |
|---|---|---|---|
| [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | A gentle, project-based introduction before the statistics and data modules | 10 weeks · 20 lessons · data ethics, SQL/NoSQL, Python, preparation, visualisation, lifecycle, cloud, and communication | [`4d2ac42`](https://github.com/microsoft/Data-Science-For-Beginners/commit/4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f), reviewed 2026-07-24 |
| [Microsoft ML for Beginners](https://github.com/microsoft/ML-For-Beginners) | Hands-on classical ML practice alongside M9–M14 and M17 | 12 weeks · 26 lessons · regression, classification, clustering, NLP, time series, reinforcement learning, and responsible ML | [`d0d0ea2`](https://github.com/microsoft/ML-For-Beginners/commit/d0d0ea2b2d22cddca31f9c6d108df7daa87a1b46), reviewed 2026-07-24 |

### Where the Microsoft lessons fit

| This roadmap | Guided lesson groups | How to use them |
|---|---|---|
| [M1 Programming](#module-1), [M5 Probability](#module-5), [M6 Statistics](#module-6) | [Defining data science and introductory statistics](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction) | Use as an accessible first pass; keep this roadmap's exercises for mathematical depth. |
| [M7 Wrangling, EDA, and visualisation](#module-7) | [Working with data](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data) and [data visualisation](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/3-Data-Visualization) | Complete the guided notebooks, then rebuild one analysis with validation and a reproducible pipeline. |
| [M8a Databases and SQL](#module-8a) | [Relational and NoSQL lessons](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data) | Use lessons 5–6 for practice before advanced SQL, query plans, warehousing, and dbt. |
| [M9 Regression](#module-9) | [Regression lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression) and [model web app](https://github.com/microsoft/ML-For-Beginners/tree/main/3-Web-App) | Pair the projects with this roadmap's derivations, diagnostics, regularisation, and cross-validation. |
| [M10 Classification](#module-10) | [Classification lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification) | Practise model comparison, then add calibration, leakage checks, and error analysis. |
| [M11 Unsupervised learning](#module-11) | [Clustering lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering) | Use for a visual K-means project before PCA, mixture models, and manifold learning. |
| [M14 Time series](#module-14) | [Time-series lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/7-TimeSeries) | Start with ARIMA and SVR, then continue to probabilistic forecasting and foundation models. |
| [M16 Representation learning](#module-16) | [Introductory NLP lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP) | Treat these as classical NLP prerequisites before transformers and generative models. |
| [M17 Reinforcement learning](#module-17) | [Reinforcement-learning lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/8-Reinforcement) | Use the Q-learning projects as the practical on-ramp to modern deep and offline RL. |
| [M23 Safety](#module-23), [M24 Operations](#module-24), [M25 Product DS](#module-25) | [ML in the wild](https://github.com/microsoft/ML-For-Beginners/tree/main/9-Real-World), [data-science lifecycle](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle), and [cloud lessons](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud) | Use for case studies; follow this roadmap for current evaluation, governance, MLOps, and communication depth. |

> **Selection rule:** use the Microsoft courses when you want a guided beginner lesson or a small practice project. Use the primary university courses and books in each module when you need formal depth. The companion courses supplement this roadmap; they do not replace its mathematics, deep learning, data engineering, or production-AI modules.

### Suggested study rhythm

For each module, use a simple four-step loop:

1. **Learn** — complete the primary course or lecture sequence.
2. **Read** — work through the listed primary text and exercises.
3. **Implement** — reproduce core algorithms without relying only on high-level APIs.
4. **Ship** — complete the module project with tests, documentation, and a short results memo.

> **Resource policy:** free and open resources are preferred. Some books are listed as optional references when no equivalent open source is as strong.

<a id="module-projects"></a>
### Module projects — the enforcement rule

Every module from [M1](#module-1) to [M25](#module-25) carries a **📦 Module Project (mandatory)** or **📋 Mandatory mini-projects** block. The rule is simple and it is not negotiable: **you do not advance to the next module until the current module's project is pushed to a public repository.** Passing a course's quizzes is not evidence; a repository is.

Each project block states three things in the same shape:

| Field | What it means |
| :--- | :--- |
| **Deliverable** | The concrete artefact. Specific enough that you cannot talk yourself into having finished. |
| **Definition of done** | Three fixed requirements every time: a **test suite**, a **`README.md`** a stranger can follow, and a short **results memo** stating what you found and what you are unsure about. The memo is the part everyone skips and the part that reads as senior. |
| **Stretch goal** | Adds exactly **one production element** — a Dockerfile, a CI workflow, a deployment, a monitoring hook. Stretch goals accumulate; by [M24](#module-24) you will have met the full [Minimum Production Bar](#production-bar). |

> **Ship it before it is good.** A messy project on the internet beats a perfect project on your laptop. An unfinished public repository with an honest README is a stronger signal than a polished notebook nobody can see — and it is the only version of the work that can get you a job, feedback, or a collaborator. Video 2 (11:30) goes one step further: prefer projects built **for a real person or organisation** over generic dataset projects, because a stakeholder who wanted the result is what makes the project a story rather than a screenshot.
>
> **Where the archetypes come from.** The project set is deliberately drawn from the archetypes named in the [source videos](#refresh-log) — churn-prediction dashboard, constraint-based meal planner, weather CLI, Reddit scraper, Discord bot, Flask blog with authentication, Hugging Face sentiment analyser, stock dashboard, RAG chatbot over your own notes — mapped to the module that actually teaches the underlying skill, and hardened with the definition-of-done requirements above.

---

# 🟩 FOUNDATION STRATUM — Modules 0–5

<img src="assets/stratum-1-foundations.jpg" alt="Foundation stratum, modules 0 to 5" width="100%">

> These six modules establish the non-negotiable mathematical and programming substrate. **A weakness in any one will cause silent failure later** — e.g., a shaky grasp of eigenvalues cripples PCA, a shaky grasp of chain rule cripples backprop, a shaky grasp of `∀ / ∃ / ⟹` cripples your ability to read a single PRML proof.

---

<a id="math-diagnostic"></a>
## 🩺 Math-Foundations Diagnostic & Remediation Map

> **Why this section exists:** Most self-learners fail at Modules 9–17 not because ML is hard, but because they skipped (or mis-sequenced) one of *six* prerequisite skills. Below is a **15-question, 60-minute diagnostic** plus a **remediation table** so you can fix the weakness *before* it metastasises.

### Step 1 — Take the 15-question self-diagnostic (free, 60 min)

Pick **one** of these freely-available diagnostic instruments — each maps cleanly to the 6 strands you must master:

| # | Strand | Diagnostic instrument | Pass bar | Remediation if you fail → |
|---|---|---|---|---|
| 1 | **Pre-calculus & algebra** | [MIT 18.01A diagnostic (Q1–Q10)](https://ocw.mit.edu/courses/18-01a-calculus-fall-2005/resources/exam_a/) | 8/10 | Module **0a** (Khan Academy Pre-Calc) |
| 2 | **Trigonometry & complex numbers** | [Paul's Online Trig diagnostic](https://tutorial.math.lamar.edu/) | 7/10 | Module **0a** (Khan Academy Trig + Euler's formula) |
| 3 | **Proof writing & logic** | [Velleman *How To Prove It* §1.5 exercises](https://www.cambridge.org/core/books/how-to-prove-it/) | 4/5 | Module **0b** (Hammack *Book of Proof* + Velleman + Lean tutorial) |
| 4 | **Single-variable calculus** | [MIT 18.01 Final Exam](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/final-exam/) | 70 % | Module **2** (full) |
| 5 | **Linear algebra (computational)** | [MIT 18.06 Quiz 1](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/exams/) | 70 % | Module **3** (full) |
| 6 | **Probability sense** | [Harvard Stat 110 Practice Strategic Practice 1–3](https://stat110.hsites.harvard.edu/) | 70 % | Module **5** (full) |

### Step 2 — Use the remediation paths

* **Score < 50 %:** Do **Module 0** end-to-end (≈ 6–10 weeks at 10 hrs/week) before touching Module 2.
* **Score 50–70 %:** Spot-fix using the per-topic links inside Module 0a / 0b.
* **Score > 70 %:** Skip Module 0; you are ready for Module 1 + 2 in parallel.

### Step 3 — Adopt the **Math Maturity Operating Manual**

Independent of *which* topic, every elite programme (MIT, Cambridge, Harvard) implicitly assumes you have these **seven habits**:

1. **Quantifier discipline** — when you read "for every / there exists", you can write it as `∀ / ∃` and negate it correctly.
2. **Definition-unfolding** — given a theorem, you can rewrite each term to its primitive definition before reasoning.
3. **Counter-example reflex** — when you doubt a claim, you immediately try `n=0`, `n=1`, the empty set, the singleton, and the constant function.
4. **Proof-template recall** — induction, contradiction, contrapositive, direct, construction, pigeonhole — each as a *template* you can fill in.
5. **Notation hygiene** — distinguish `=` (equal), `:=` (defined-as), `≡` (congruent / identical), `≈` (approximately), `∼` (asymptotic), `∝` (proportional).
6. **Computational verification** — every symbolic claim you make is sanity-checked in **SymPy** (algebra) or **NumPy** (numerical) within 5 minutes.
7. **Lean / proof-assistant exposure** — *not required*, but doing one chapter of [Velleman's *How To Prove It With Lean*](https://djvelleman.github.io/HTPIwL/) **changes how you read every subsequent definition** for the rest of your career.

> **Cited source for habits 1–6:** Cambridge IB Discrete Mathematics + Harvard Math 22a "Reasoning, Proof, and Linear Algebra" course handbooks (2025–26).

---

<a id="module-0"></a>
## Module 0: Mathematical Maturity Bridge — Pre-Calculus, Logic & Proof

> **Status:** Optional **only** if you scored > 70 % on every diagnostic above. Otherwise: **mandatory**.

* **The Tutor's "Why":** No university teaches *the leap* from procedural high-school math to definition-driven university math — they assume you already made it. The result: 60 %+ of self-learners stall at Module 5 (probability proofs) or Module 9 (regression assumptions). Cambridge's IB CST course explicitly assumes "Mathematics for Natural Sciences" maturity; MIT 6.7960 assumes 18.05 + a proof course; Harvard CS 1810 assumes Math 22a (linear algebra **with proofs**). **This module IS that proof course, compressed and free.**

* **Strict Prerequisites:** Working knowledge of high-school algebra (solve linear and quadratic equations).

### Sub-module 0a — Pre-Calculus & Trigonometry Refresher (≈ 2–4 weeks)

* **Exhaustive Topic List:**
  * **Numbers:** ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ; absolute value as distance; intervals; surds and rationalising.
  * **Algebra:** factorisation (difference of squares, sum/difference of cubes), polynomial long division, partial fractions, exponent and log laws, change-of-base formula, **completing the square** (the single most-cited identity in regression).
  * **Functions:** domain/range, composition, invertibility, even/odd, increasing/decreasing, piecewise, absolute value, floor/ceiling.
  * **Conic sections:** circle, ellipse, parabola, hyperbola — equations and parametrisations (you'll see them again in Gaussians and SVMs).
  * **Trigonometry:** unit circle, radian measure, six trig functions, identities (Pythagorean, sum/difference, double-angle, half-angle, product-to-sum), inverse trig, polar coordinates.
  * **Complex numbers:** Cartesian and polar form, **Euler's formula `eⁱᶿ = cos θ + i sin θ`** (the bridge to Fourier transforms in M3), De Moivre's theorem, roots of unity.
  * **Sequences & series:** arithmetic and geometric, sum formulas (you will re-derive these in MGFs in M5).
  * **Limits — informal:** ε-δ intuition, one-sided limits, infinite limits, limits at infinity.

* **2026 Resources:**
  * **Primary (free):** [Khan Academy Precalculus](https://www.khanacademy.org/math/precalculus) — 10 units, ≈ 40 hours, includes mastery quizzes.
  * **Alternative (free, MIT-quality):** [MIT 18.01A Calculus with Pre-Calc](https://ocw.mit.edu/courses/18-01a-calculus-fall-2005/) — combines refresher with calculus, ideal if you have 6+ weeks.
  * **Reading:** Stewart *Calculus, Early Transcendentals* (9th ed.) — Appendix A (numbers), Appendix B (coordinate geometry), Appendix C (graphs), §1.1–§1.5 (functions and models).
  * **Computational verification:** every identity must be checked in **SymPy** within 1 line (e.g., `sympy.simplify(sin(x)**2 + cos(x)**2 - 1)`).

### Sub-module 0b — Logic, Proof & Mathematical Vernacular (≈ 4–6 weeks · CORE)

* **Exhaustive Topic List:**
  * **Propositional logic:** truth tables, conjunction `∧`, disjunction `∨`, negation `¬`, implication `⟹`, biconditional `⟺`, **converse / contrapositive / inverse** (and which are logically equivalent).
  * **Predicate logic:** universal `∀`, existential `∃`, **negating quantified statements** (`¬∀x P(x) ≡ ∃x ¬P(x)` — the single most error-prone identity in undergraduate maths).
  * **Sets:** ∅, ∈, ⊆, ⊊, ∪, ∩, complement, Cartesian product, power set, Russell's paradox (and why ZFC patches it).
  * **Functions formally:** as relations satisfying functional dependence; injection, surjection, bijection; image and pre-image; composition; inverse function theorem (statement only).
  * **Relations:** reflexive, symmetric, transitive, equivalence relations, partitions, partial and total orders.
  * **Cardinality:** finite, countably infinite (ℕ ∼ ℤ ∼ ℚ), uncountable (ℝ via Cantor's diagonal); pigeonhole as a corollary.
  * **Proof techniques (with at least 3 worked examples each):**
    1. **Direct proof** — e.g., sum of two evens is even.
    2. **Proof by contradiction** — e.g., √2 is irrational; there are infinitely many primes.
    3. **Proof by contrapositive** — e.g., if `n²` is even then `n` is even.
    4. **Proof by mathematical induction** (weak and strong) — e.g., `Σk=1ⁿ k = n(n+1)/2`; well-ordering principle.
    5. **Proof by construction** — e.g., explicitly construct a bijection ℕ → ℤ.
    6. **Proof by cases** — e.g., triangle inequality.
    7. **Pigeonhole principle** — e.g., among any 13 people, two share a birth-month.
  * **Number theory primer:** divisibility, gcd, Euclidean algorithm (with extended version), Bezout's identity, modular arithmetic, Fermat's little theorem, Chinese Remainder Theorem (used in cryptography and hashing).
  * **Combinatorial identities:** Pascal's rule, hockey-stick identity, Vandermonde's identity (you will re-encounter all three in Stat 110 Lec 1–2).
  * **(Optional) Lean 4 first contact:** prove `∀ n : ℕ, n + 0 = n` interactively. *Not required for the curriculum but a 10× force-multiplier on every later module's confidence.*

* **2026 Resources:**
  * **Primary text (free, CC-BY):** [_Book of Proof_ (Hammack, **3rd Edition, 2018; revised 2025**)](https://richardhammack.github.io/BookOfProof/) — chapters 1–10. Open Textbook Initiative-approved; used at 50+ universities.
  * **Companion text:** [_How to Prove It: A Structured Approach_ (Velleman, **3rd Edition, Cambridge 2019**)](https://www.cambridge.org/core/books/how-to-prove-it/) — chapters 1–6 + the new **[*How to Prove It With Lean* (Velleman, 2024)](https://djvelleman.github.io/HTPIwL/)** companion (free, browser-based).
  * **Discrete-math companion:** [_Mathematics for Computer Science_ (Lehman, Leighton, Meyer — MIT 6.042J, **2024 edition free PDF**)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook/) — chapters 1–5 (Proofs, Induction, Number Theory).
  * **Video course:** [Stanford CS103 Mathematical Foundations of Computing — full lecture notes](https://web.stanford.edu/class/cs103/) (publicly mirrored).
  * **Free online interactive course:** [_Introduction to Mathematical Thinking_ (Keith Devlin — Coursera, evergreen)](https://www.coursera.org/learn/mathematical-thinking) — Stanford-led, free audit.
  * **Practical implementation:** **SymPy 1.13+** for symbolic verification; **Lean 4 + Mathlib** (optional) — `lean4-web` runs in browser, no install needed.

* **Outcome:** When you finish Module 0b you can **read any theorem statement in Stat 110 / 18.06 / CS 1810 and re-state it formally before attempting the proof.** That single skill is the difference between a frustrated learner and an MIT-track one.

* **Suggested Pace:** 6 weeks at 10 hrs/week = 60 hrs total; or 12 weeks at 5 hrs/week. **Do not skip the exercises** — Hammack provides 600+ with hints, and *doing 200 of them* is the entire point of this module.

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The route:** Skip Module 0 entirely. Go straight to [M1](#module-1), and pick up mathematical vocabulary as it appears via [StatQuest](https://statquest.org/) and the [Manga Guides](#practitioner-shelf). Return here only if you later hit the wall described below.
>
> **The argument for it:** Video 3 (04:47) — *"You need intuition, not derivation skills. Get the concepts down and then move forward."* Video 1 (00:44–01:09) reports that months spent on manual derivations "took years longer than it needed to" and did not yield "great intuition for why models behave the way they do in practice."
>
> **What you give up — stated plainly:** Module 0 is not a maths course, it is a *reading* course. Without it you cannot parse `∀ / ∃`, negate a quantified statement, or unfold a definition — which means every theorem statement in Stat 110, ESL, PRML, and Murphy remains opaque. You will be able to *use* methods and unable to *check* them.
>
> **Come back when:** you enter [M13](#module-13) (Bayesian derivations), any research-track work, or you find yourself unable to tell whether a paper's claim is actually supported. Module 0 is 60 hours; it does not expire.

---

<a id="module-1"></a>
## Module 1: Programming Foundations & Computational Thinking

* **The Tutor's "Why":** All 2026 data-science work is Python-first (with selective Polars/R/Julia). You cannot derive a gradient if you cannot write a loop. This module is the gateway — master it, or every subsequent module becomes guesswork.

* **Strict Prerequisites:** High-school algebra. A working laptop with VS Code installed.

* **Exhaustive Topic List:**
  * **[Harvard CS50P · Week 0]**: Functions, variables, types (int/float/str), `print`, formatted strings, conditionals, boolean expressions.
  * **[Harvard CS50P · Week 1]**: Conditionals, `match` statement, flow control, truthy/falsy semantics.
  * **[Harvard CS50P · Week 2]**: Loops (`for`, `while`), iterables, `break`/`continue`, `enumerate`, `zip`.
  * **[Harvard CS50P · Week 3]**: Exceptions, `try/except/else/finally`, raising custom exceptions, `assert`.
  * **[Harvard CS50P · Week 4]**: Libraries, `import`, `pip`, standard library tour (`random`, `statistics`, `sys`, `pathlib`).
  * **[Harvard CS50P · Week 5]**: Unit testing, `pytest`, test-driven development, fixtures, parametrise.
  * **[Harvard CS50P · Week 6]**: File I/O, CSV, JSON, binary files, context managers (`with`), PIL/Pillow basics.
  * **[Harvard CS50P · Week 7]**: Regular expressions, `re.search/match/sub/findall`, character classes, anchors, lookaheads.
  * **[Harvard CS50P · Week 8]**: Object-Oriented Programming: classes, `__init__`, attributes, methods, `@classmethod`, `@staticmethod`, `@property`, inheritance, `super()`, dunder methods (`__str__`, `__repr__`, `__eq__`).
  * **[Harvard CS50P · Week 9]**: `et cetera` — set/dict comprehensions, generators (`yield`), decorators, `*args`/`**kwargs`, type hints (`typing` module, 2026 `|` syntax).
  * **[IITM BSCS1001 — Computational Thinking]**: Algorithmic decomposition, state machines, invariants, correctness proofs (loop invariants), complexity intuition (counting ops).
  * **[IITM BSCS1002 — Programming in Python]**: Python interpreter model, memory model (reference semantics), mutability vs immutability, scope (LEGB), closures, iterators vs generators vs async generators.
  * **[MIT 6.0001 (archived edX)]**: Branching, iteration, string manipulation, recursion (factorial, Fibonacci, Towers of Hanoi), debugging methodology, efficiency (big-O informal intro), tuples, lists, aliasing, cloning, mutating, dictionaries.
  * **[MIT 6.0002]**: Optimisation problems, knapsack, graph-theoretic models, dynamic programming motivation, random walks, Monte Carlo simulation, sampling + confidence, experimental data curve-fitting, statistical myths.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS50P — 2024 edition](https://cs50.harvard.edu/python/) · [MIT 6.0001 on OCW](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)
  * **Required Reading (Latest 2026 Editions):**
    * _Fluent Python_ (**2nd Edition, 2022** — the current edition; [fluentpython.com](https://www.fluentpython.com/) ✅) — Luciano Ramalho — chapters 1–6, 9 (closures/decorators), 17 (iterators).
    * _Python Crash Course_ (**3rd Edition** — the current edition; [No Starch](https://nostarch.com/python-crash-course-3rd-edition) ✅) — Eric Matthes — for absolute beginners only.
  * **Practical Implementation:** **Python 3.12+** (pattern matching, improved error messages, per-interpreter GIL awareness). IDE: **VS Code** with `ms-python.python`, `charliermarsh.ruff`, `ms-python.mypy-type-checker`. Dependency manager: **`uv`** (2024-released, now standard).

* **🛠 Modern Python Tooling:**
  * **Type hints + mypy/pyright + Pydantic v2** — every production ML codebase uses typed Python. Learn: `TypedDict`, `Protocol`, `Generic`, `Annotated`, `TYPE_CHECKING`; [Pydantic v2 docs](https://docs.pydantic.dev/) ✅ for data-validation and settings management.
  * **[`uv` — Astral's ultra-fast package manager (0.11.7, Apr 2026)](https://docs.astral.sh/uv/)** ✅ — replaces `pip`/`pip-tools`/`virtualenv`/`pipx`/`poetry`. Learn `uv init`, `uv add`, `uv run`, `uv lock`, `uv tool install`.
  * **`async`/`asyncio` + `anyio`** — required for serving LLM APIs (M24), streaming pipelines (M8b), and batching tokeniser calls. Read [Python docs asyncio](https://docs.python.org/3/library/asyncio.html) ✅ + *Fluent Python* ch 19–21.
  * **Git + GitHub Actions CI** — pre-commit hooks, branch-protection, conventional commits, GitHub Actions workflows for test/lint/build.
  * **`pytest` + `hypothesis` (property-based testing)** — [hypothesis docs](https://hypothesis.readthedocs.io/) ✅. Every ML engineer at FAANG writes property-based tests for numerical code; learn the `@given` decorator and shrinking.
  * **`ruff` + `pyright`** for lint + typecheck; **`pre-commit`** to run them on every commit.

### 📅 Official pacing structure — the four-phase Python roadmap

The topic list above is *what* to learn. This is *when*, and — more importantly — *what you must have shipped* by the end of each phase. Pacing and milestones adapted from Scrimba's [beginner's guide to learning Python (2026)](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) ✅ and reconciled with the CS50P week map.

| Phase | Weeks | Goal | Core skills | **Milestone you must ship** |
| :--- | :--- | :--- | :--- | :--- |
| **1 — Foundations** | 1–4 | Stop being confused by syntax | Variables, types, operators, conditionals, loops, functions, lists/dicts/tuples/sets, string methods | A **number-guessing game** and a **command-line calculator** — both in a git repo with a README |
| **2 — Working Python** | 5–8 | Write programs that touch the outside world | File I/O, CSV/JSON, exceptions, `pathlib`, modules + `import`, standard library, virtual envs, regular expressions | A **file-I/O CLI tool** (e.g. an expense tracker or file organiser) that reads and writes real files and survives bad input |
| **3 — Real-World Python** | 9–14 | Write code another engineer would accept | OOP (classes, inheritance, dunders), decorators, generators, comprehensions, type hints, `pytest`, `requests`, git branching + PRs, debugging | An **API-consuming application** with a class-based design, a `pytest` suite, type hints, and a CI workflow that runs on every push |
| **4 — Specialisation** | Month 4–6+ | Point Python at a domain | NumPy/pandas (→ [M7](#module-7)), a web framework (Flask/FastAPI), Docker, deployment | **2–3 deployed portfolio projects** — see the [Minimum Production Bar](#production-bar) |

**Phase-matched project ladder.** Match project difficulty to the phase you are actually in. Building above your rung produces copy-paste; building below it produces boredom.

| Rung | Phase | Project options |
| :--- | :--- | :--- |
| **Beginner** | 1 | Number-guessing game · password generator · Pomodoro timer · expense tracker · Markdown-to-HTML converter |
| **Intermediate** | 2–3 | Reddit scraper · Spotify listening-history analyser · Discord bot · weather CLI (real API + caching + error handling) · bulk file organiser |
| **Advanced** | 4 | Flask blog with authentication · sentiment analyser on a pretrained Hugging Face model · stock dashboard · RAG chatbot over your own notes |

> **Note on the advanced rung.** The last two entries are deliberately the *same* deliverables as the [M7](#module-7) and [M21](#module-21) module projects. Phase 4 of Python is not a separate track — it *is* the beginning of the data/AI curriculum. Do not build them twice.

<a id="python-course-matrix"></a>
### 🐍 Free Python course matrix

There is no single best free Python course; there is a best *pair*. This matrix is synthesised from Scrimba's [best free Python courses for beginners in 2026](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/) ✅, with every link independently live-verified (see [`audit/VERIFICATION.md`](audit/VERIFICATION.md)).

| Course | Hours | Format | Free certificate? | Projects | Best for |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Scrimba — Learn Python](https://scrimba.com/learn-python-c02t)** ✅ | ~5.6 h · 58 parts | Interactive screencasts you can edit and run inline (Olof Paulson) | Yes | Many small in-browser challenges | The fastest possible *start*. Removes environment-setup friction entirely |
| **[Harvard CS50P](https://cs50.harvard.edu/python/)** ✅ | ~100 h · 10 weeks | Lectures + graded problem sets (David Malan) | Yes (free certificate) | 9 problem sets + final project | The single best **rigour** option; the spine of this module's topic list |
| **[University of Helsinki — Python Programming MOOC](https://programming-24.mooc.fi/)** ✅ | 200+ h · 14 parts | Text-based, browser-graded, auto-tested exercises (no video) | ECTS credits available | Hundreds of auto-graded exercises | Learners who prefer **reading over watching** and want relentless exercise volume |
| **[freeCodeCamp — Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)** ✅ | ~300 h | Video + browser projects | Yes (free certification) | 5 certification projects | A **free credential** plus scientific-computing framing. ⚠️ Content is older than the others — verify Python-3 idioms against the official docs as you go |
| **[Coursera — Python for Everybody (Michigan, Severance)](https://www.coursera.org/specializations/python)** ✅ | ~32 h (audit) | University lectures + readings | No — certificate is paid; **audit is free** | Weekly assignments | Learners who want a **classic university sequence** and databases/web-scraping coverage |
| **[Official Python Tutorial](https://docs.python.org/3/tutorial/)** ✅ | ~15 h | Reference-grade prose | No | None | The **authoritative** source. Use as a companion, never as your first course |
| **[Google's Python Class](https://developers.google.com/edu/python)** ✅ | ~10 h | Written lessons + exercises | No | Small exercise sets | Programmers **already fluent in another language** who need Python syntax fast |
| **[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)** ✅ | Book (3rd Ed., 2025) | Free full text online (Al Sweigart) | No | Chapter-end practice projects | **Motivation and immediate utility** — the single best "why would I use this?" answer |

> **The recommended pairing stack.** No single course produces competence. Run them in this order:
> **1. [Scrimba — Learn Python](https://scrimba.com/learn-python-c02t)** for a frictionless first two weeks →
> **2. [Automate the Boring Stuff](https://automatetheboringstuff.com/)** to convert syntax into things you actually use →
> **3. [CS50P](https://cs50.harvard.edu/python/) *or* the [Helsinki MOOC](https://programming-24.mooc.fi/)** for the depth, testing discipline, and OOP that the fast courses skip. Pick CS50P if you learn from lectures; pick Helsinki if you learn from exercises.
>
> **Red flags in any Python course you find elsewhere.** Reject it if (a) it teaches **Python 2** (`print` as a statement, `raw_input`, integer division by default) or (b) it **never reaches OOP, exceptions, or testing** — those are exactly the topics that separate a tutorial-completer from someone employable.

### 🔨 How to actually study this module — the tutorial-hell escape protocol

Tutorial hell is the state of continuously consuming instruction while producing nothing. It feels like progress because it is comfortable, and it is the single most common failure mode in self-taught Python. The protocol below is the escape.

1. **Build before you feel ready.** You will never feel ready. Start the phase milestone at ~60 % confidence and let the gaps surface as concrete, searchable questions.
2. **Close the tutorial and rebuild from memory.** After finishing any guided project, delete it and rebuild it with the tab closed. What you cannot reproduce is what you have not learned — that list is your actual study plan.
3. **Hold a 2:1 build-to-watch ratio.** Two hours writing your own code for every one hour of instruction. If the ratio inverts for a week, you are in tutorial hell.
4. **Read, break, and fix other people's code.** Clone a small open-source Python repo, read it until you can explain the entry point, deliberately break something, then fix it. Reading production code is a distinct skill from writing greenfield code, and job interviews test it.
5. **Join a community and be publicly accountable.** Post weekly what you shipped. External accountability is what survives the week your motivation does not — see [Career Operations](#career-operations).

> **The principle underneath all five:** comfortable learning is mostly fake learning. Video 1 (09:30) calls the mechanism the *fluency illusion*; video 2 (07:12) frames the fix as taking the internal locus of control — you own the outcome, so you own the discomfort. Difficulty is the signal that encoding is happening.

### 🤖 Disciplined AI-assistant policy (applies to M1–M5)

AI coding assistants are the fastest way to learn Python and the fastest way to never learn it. The difference is entirely in *what you ask for*.

**Permitted while working through M1–M5:**
* "Explain what this error message means and what category of bug causes it."
* "Review the code I already wrote and name the weaknesses — do not rewrite it."
* "Quiz me on decorators. Ask questions, do not give answers."
* "Explain three ways to structure this, with trade-offs" — then you choose and you type it.

**Not permitted while working through M1–M5:**
* "Write this function for me."
* Pasting a milestone project's requirements into a model and shipping the output.
* Accepting any autocomplete you could not have written yourself and cannot explain line by line.

> **⚠️ The fluency illusion.** Video 1 (09:30): *"There's this fluency illusion where AI hands you a perfect answer, and you walk away feeling like you understood it, but you didn't do the cognitive work that makes the knowledge stick."* This is the failure mode the policy exists to prevent. The cost is invisible until an interview or a production incident, at which point it is total.
>
> **The policy loosens after M5.** Once the fundamentals are encoded, using models to generate boilerplate, scaffold tests, and draft config is straightforward professional leverage — and [M22](#module-22) treats agentic coding as a first-class engineering topic. The restriction is developmental, not moral.

### 📚 Cited sources added in v2026.3

* **[Scrimba — *Best Free Python Courses for Beginners in 2026*](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/)** ✅ *(verified 2026-07-26)* — source for the [free Python course matrix](#python-course-matrix), the pairing stack, and the Python-2/no-OOP red flags.
* **[Scrimba — *How to Learn Python: A Beginner's Guide (2026)*](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/)** ✅ *(verified 2026-07-26)* — source for the four-phase pacing structure, the weekly milestones, the phase-matched project ladder, the tutorial-hell escape protocol, and the honest time-to-competence estimates in the [Fast Lane](#practitioner-track).
* **Video 1 — [*How to Become an ML Engineer*](https://www.youtube.com/watch?v=UZ_rK9gzVSc)** (03:00–04:00) — the Python competence bar for ML work: data types, control flow, functions, and file handling, then straight into NumPy and pandas ([M7](#module-7)). The *fluency illusion* warning is at 09:30.
* **Video 3 — [*The Only 7 Books You Need to Become an AI Engineer*](https://www.youtube.com/watch?v=Pr9oRVtAqCM)** (01:21) — Python is "table stakes" for the AI Engineer role; *Automate the Boring Stuff* is named as the entry point (see the [Practitioner Shelf](#practitioner-shelf)).

* **📦 Module Project (mandatory) — Weather CLI**
  * **Deliverable:** A command-line weather tool that takes a city name, calls a real public weather API, caches responses to disk so repeated calls do not re-hit the network, and prints a formatted forecast. Class-based design, type hints throughout.
  * **Definition of done:** (1) `pytest` suite covering the happy path, a bad city name, a network timeout, and a malformed API response — network mocked, not live; (2) `README.md` with install, usage, and one screenshot of real output; (3) a 1-page results memo recording what broke while you built it and how you diagnosed it.
  * **Stretch (adds one production element):** Wire a GitHub Actions workflow that runs `ruff` + `pytest` on every push, and make the badge green.
  * *Archetype source: video 1 (13:40) — the "weather CLI with real API, caching and error handling" tier; Phase 3 milestone of the [four-phase roadmap](#module-1).*

---

<a id="module-2"></a>
## Module 2: Single-Variable & Multivariable Calculus + Matrix Calculus & Convex Optimisation

* **The Tutor's "Why":** Gradients, backpropagation, maximum-likelihood estimation, and Bayes-rule derivations all live or die on calculus. You will not understand *why* SGD converges without it. Harvard's CS 1810 (2026) explicitly requires AM 22a (calc + lin alg). **Crucially, every modern paper denotes gradients in *matrix-calculus* notation (Jacobians, Hessians, vector-by-matrix derivatives) — and 90 % of self-learners have never seen this formalism.** This module fixes that gap.

* **Strict Prerequisites:** Module 0 (proof literacy) + Module 1 (so you can verify integrals with SymPy).

* **Exhaustive Topic List:**
  * **[MIT 18.01.1x · Differentiation]**: Limits and continuity (ε-δ definition), derivative as a limit, power/product/quotient/chain rules, trig derivatives, exponential and log derivatives, implicit differentiation, linear/quadratic approximations, related rates, Mean Value Theorem, L'Hôpital's rule, optimisation (first/second derivative tests), Newton's method.
  * **[MIT 18.01.2x · Integration]**: Antiderivatives, Fundamental Theorem of Calculus (both parts + proofs), u-substitution, integration by parts, trigonometric integrals, partial fractions, improper integrals, Riemann sums, numerical integration (trapezoidal, Simpson's rule), applications (areas, volumes of revolution, arc length, surface area, centre of mass, work).
  * **[MIT 18.01.3x · Coordinate Systems & Infinite Series]**: Polar coordinates, parametric curves, conic sections, sequences, series convergence tests (ratio, root, integral, comparison, alternating series), power series, Taylor & Maclaurin series (**with remainder bounds — used in Newton's-method convergence and stochastic-gradient analysis**), complex numbers, Euler's formula.
  * **[MIT 18.02 · Multivariable Calculus]**: Vectors in ℝⁿ, dot and cross products, lines and planes, vector-valued functions, partial derivatives, tangent planes, total differential, **gradient vector & directional derivatives** (the foundation of gradient descent), chain rule (multivariable), **Hessian matrix** (used in Newton's method and second-order optimisers), Lagrange multipliers (→ SVM dual), double/triple integrals, change of variables, Jacobian determinant, vector fields, line integrals, Green's theorem, Stokes' theorem, divergence theorem.
  * **[IITM BSMA1001 — Math for DS I]**: Function basics, domain/range, piecewise functions, composition, inverse functions; limits; differentiation applied to business problems; definite vs indefinite integration; matrix-vector product as linear combination (preview of M3).
  * **[IITM BSMA1003 — Math for DS II]**: Vector calculus for optimisation, constrained optimisation, Lagrange multipliers with KKT conditions, convex functions, Jensen's inequality, convex optimisation preview.
  * **[Cambridge Data Science — Wischik]**: Calculus of variations (used in variational inference, M13).
  * **[MIT 18.063 / 18.S096 · Matrix Calculus for Machine Learning, IAP 2023 + Jan 2026 — Edelman & Johnson]**: **Differentials in the language of linear maps** (the *correct* modern view that subsumes both numerator-layout and denominator-layout conventions); derivatives of vector-valued functions of vectors (Jacobians); derivatives of scalar-valued functions of matrices (gradients); derivatives of matrix-valued functions of matrices (4-tensors / Kronecker products); chain rule as composition of linear maps; **forward-mode and reverse-mode automatic differentiation** (the operational foundation of every DL framework); cost analysis of forward-vs-reverse AD (matrix-multiplication-cost argument); derivatives through SVD, eigendecomposition, matrix inverse, determinant, log-determinant, trace, Frobenius norm; **adjoint method** for differentiating through ODE/PDE solutions (used in Neural ODEs and diffusion solvers, M16).
  * **[Stanford EE364A · Convex Optimization I — Boyd & Vandenberghe (Lectures 1–10) — *promoted from Module 9 to here as a foundation*]**: Convex sets (hyperplanes, half-spaces, polyhedra, balls, ellipsoids, norm cones, positive semi-definite cone), operations preserving convexity, convex functions (definition via secant inequality, first- and second-order conditions, Jensen's inequality), epigraph, sub-level sets, conjugate function, **convex optimisation problems** (LP, QP, QCQP, SOCP, SDP — and *which ML problems map to each*), Lagrangian duality, **KKT conditions** (the single most-cited result in classical ML), strong vs weak duality, complementary slackness, perturbation analysis. **Why here, not later:** every regression / SVM / logistic / GLM proof in Modules 9–14 *assumes* this material.
  * **[The Matrix Cookbook — Petersen & Pedersen, 2024 update]** + **[Parr & Howard "The Matrix Calculus You Need For Deep Learning" (arXiv:1802.01528, 2024 revision)]** as *daily-reference* lookup PDFs.

* **2026 Resources:**
  * **Primary Course Link:** [MITx 18.01.1x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.1x/) · [18.01.2x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.2x/) · [18.01.3x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.3x/) · [MIT OCW 18.02SC Multivariable](https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/)
  * **Matrix-Calculus track:** [MIT 18.S096 / 18.063 — Matrix Calculus for ML (IAP 2023 + Jan 2026)](https://github.com/mitmath/matrixcalc) — full lecture notes, video, problem sets *all open* on GitHub.
  * **Convex-Optimisation track:** [Stanford EE364A — Boyd, lectures + slides + book](https://web.stanford.edu/class/ee364a/) · [Free PDF of *Convex Optimization* (Boyd & Vandenberghe, Cambridge 2004, 6th printing 2023)](https://stanford.edu/~boyd/cvxbook/) · YouTube lecture series (re-recorded **Spring 2024**).
  * **Required Reading (Latest 2026 Editions):**
    * _Calculus: Early Transcendentals_ (**9th Edition, 2025 reprint**) — James Stewart — chapters 1–12.
    * **[Recommended freely-available alternative]** _Active Calculus_ (Boelkins et al., **2024 edition, free online**) — used at 80+ liberal-arts colleges.
    * **[Free, MIT-quality, 2024-revised]** Strang & Herman _Calculus, Vol 1–3_ (OpenStax, free PDF) — explicit OCW companion.
    * _Mathematics for Machine Learning_ — Deisenroth, Faisal, Ong (**book PDF last updated December 2025**) — Chapters 5 (Vector Calculus), 6 (Probability), **7 (Continuous Optimization)**. [mml-book.com](https://mml-book.com/) — **explicitly recommended by Harvard CS 1810 (2026)**.
    * ***The Matrix Cookbook*** — Petersen & Pedersen (2024 web update) — [PDF mirror via MIT 18.S096](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/external-resources/the-matrix-cookbook-pdf_fa1edb35-184a-410d-9d60-34488dbc72ee/).
    * **Parr & Howard** "The Matrix Calculus You Need For Deep Learning" — free on arXiv `1802.01528` (revised); also as an HTML web-book at [explained.ai/matrix-calculus](https://explained.ai/matrix-calculus/).
    * **Boyd & Vandenberghe** _Convex Optimization_ (Cambridge 2004; **6th printing 2023**, free PDF as above) — chapters 1–5 mandatory; 6–11 optional and revisited in M9–M11.
    * 3Blue1Brown: [_Essence of Calculus_ playlist (16 videos, ≈ 3 hrs)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — required visual intuition.
    * **[Imperial College "Mathematics for Machine Learning" Coursera Specialization (Deisenroth, Cooper, Page — last refreshed Mar 2025)](https://www.coursera.org/specializations/mathematics-machine-learning)** — three courses: Linear Algebra · Multivariable Calculus · PCA. Free audit. *Pedagogically the gentlest on-ramp.*
  * **Practical Implementation:** **SymPy 1.13+** for symbolic verification; **JAX 0.7+** `jax.grad` / `jax.jacrev` / `jax.jacfwd` / `jax.hessian` for automatic differentiation — learn these NOW as you'll need them for all of M15+. **`cvxpy` 1.5+** for convex optimisation modelling (DCP), **`autograd`** as a teaching aid for hand-coding back-prop. Optionally explore **`Zygote.jl`** in Julia for source-to-source AD intuition.

* **Suggested Sequencing (16 weeks at 10 hrs/week):**
  1. Weeks 1–4: Single-variable calc (18.01.1x + 18.01.2x).
  2. Weeks 5–6: Series + Taylor (18.01.3x).
  3. Weeks 7–10: Multivariable (18.02 SC), with daily SymPy verification.
  4. Weeks 11–13: **Matrix calculus** (MIT 18.063 + Parr-Howard) — *the highest-leverage 3 weeks in the whole curriculum*.
  5. Weeks 14–16: **Convex optimisation** (EE364A Lectures 1–10) — write 5 small `cvxpy` programs (LP, LASSO, SVM, portfolio, max-likelihood logistic).

* **🧠 Automatic Differentiation Theory (2026.2 NEW sub-section):** Understanding AutoDiff is non-negotiable for M15+.
  * **Forward-mode (JVP — Jacobian-Vector Product):** Propagate dual numbers `(x, ẋ)` through the computational graph. Cost: O(n) extra for n inputs. Best when **inputs ≪ outputs** (rare in ML).
  * **Reverse-mode (VJP — Vector-Jacobian Product):** Forward pass builds a tape/graph; backward pass propagates cotangents. Cost: O(n) extra for n outputs. This is **backpropagation**. Best when **outputs ≪ inputs** (always true in ML: scalar loss, millions of parameters).
  * **Mixed-mode:** For Hessian-vector products (`Hv = ∇(∇L · v)`) used in second-order optimisers, Newton-CG, and natural gradient — apply forward-over-reverse or reverse-over-forward.
  * **Checkpointing:** Trade compute for memory by recomputing activations during backward pass (used in FSDP / gradient-checkpointing in M15).
  * **Practical:** `jax.grad`, `jax.jvp`, `jax.vjp`, `jax.jacrev`, `jax.jacfwd`, `jax.hessian`; `torch.autograd.grad`, `torch.func.vmap`, `torch.func.jacrev`; all cross-reference the [MIT 18.063 matrix-calc notes](https://github.com/mitmath/matrixcalc) already cited above.

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The route (≈ 10–15 hours instead of 160):** Watch [3Blue1Brown — *Essence of Calculus*](https://www.3blue1brown.com/topics/calculus) (12 videos) for the derivative-as-rate-of-change and chain-rule pictures, then [StatQuest's gradient-descent series](https://statquest.org/) for the optimisation loop. Read *The Manga Guide to Calculus* if you want a book. Skip Stewart, skip 18.01/18.02, skip EE364A. **Do not skip the AutoDiff sub-section above** — read it as a *conceptual* description of what `loss.backward()` does; you need that model to debug training.
>
> **The argument for it:** Video 1 (01:41–02:06) puts 3Blue1Brown and StatQuest at Phase 1 and budgets **2–4 weeks** for "a rough mental map rather than mastery." Video 3's speaker reports never hand-computing a chain rule in six years at Amazon and Coursera (04:47).
>
> **What you give up — stated plainly:** you will not be able to derive a gradient, verify a paper's update rule, reason about convergence rates, or use KKT conditions to understand why the SVM dual looks the way it does. When a model fails to converge you will be limited to empirical remedies (change the LR, change the optimiser) rather than diagnostic ones.
>
> **Come back when:** you reach [M13](#module-13) variational inference, [M16](#module-16) diffusion/score-matching, [M17](#module-17) policy-gradient derivations, or any research role. The convex-optimisation half (EE364A) in particular is assumed by every proof in M9–M14.

* **📦 Module Project (mandatory) — Gradient-descent laboratory**
  * **Deliverable:** A small NumPy package that minimises a user-supplied scalar function. Implement (a) finite-difference gradients, (b) analytic gradients for three test functions (quadratic bowl, Rosenbrock, logistic loss), and (c) plain gradient descent, momentum, and Adam. Plot the optimisation trajectory over a contour map for each.
  * **Definition of done:** (1) `pytest` suite asserting that your analytic gradient matches the finite-difference gradient to `1e-6` — this is the gradient-check discipline every DL codebase depends on; (2) `README.md` with the three contour plots and a table of iterations-to-convergence per optimiser; (3) a results memo answering *why* momentum beats plain GD on Rosenbrock, in your own words.
  * **Stretch:** Reproduce your Adam result using `jax.grad` and show the two agree — this is your bridge into [M15](#module-15).
  * *Fast-lane note: intuition-track learners may implement (a) and (c) only and skip the analytic derivations, but must still pass the gradient check.*

---

<a id="module-3"></a>
## Module 3: Linear Algebra — Computational, Geometric & Abstract

* **The Tutor's "Why":** *Every* modern ML algorithm — from linear regression to attention heads in GPT-class transformers — is a composition of matrix operations. Strang's 18.06 is the global gold standard for the *computational* view; Axler's *Linear Algebra Done Right* (**4th edition, 2024, freely available**) is the gold standard for the *abstract / proof-based* view that PRML, Bishop 2024, and Cambridge MLMI implicitly assume. **You need both.** Cambridge's MLMI Module 1 requires eigendecomposition mastery before week 3.

* **Strict Prerequisites:** Module 0b (proof literacy) + Module 2 (partial derivatives for matrix calculus).

* **🧭 Suggested Two-Pass Pedagogy:**
  * **Pass 1 — Computational (5 weeks):** Strang 18.06 + 3Blue1Brown — focus on *doing* row-reduction, computing eigenvalues, running SVD on toy matrices. Goal: numerical fluency.
  * **Pass 2 — Abstract (4 weeks):** Axler 4e (Chapters 1–7, skipping Chapter 8 if PhD-track is not the goal) — focus on *proving* spectral theorem, why SVD always exists, why orthogonal projection minimises distance. Goal: theoretical confidence.
  * **Pass 3 — Applications (3 weeks):** Strang's *Linear Algebra and Learning from Data* + Townsend's *Linear Algebra for Data Science* (Cambridge 2024) — focus on *the eight matrix factorisations of ML* (LU, QR, eigendecomposition, SVD, Cholesky, polar, NMF, randomised SVD).

* **Exhaustive Topic List:**
  * **[MIT 18.06 · Strang]**: Systems of linear equations, Gaussian elimination, LU factorisation, vector spaces, subspaces (column space, null space, row space, left null space — the "four fundamental subspaces"), rank-nullity theorem, linear independence, basis, dimension, orthogonality, Gram-Schmidt process, QR decomposition, projections, least squares (normal equations), determinants (cofactor expansion, properties), **eigenvalues and eigenvectors** (characteristic polynomial, diagonalisation), **Singular Value Decomposition (SVD)** (full and reduced forms, Eckart-Young theorem, pseudoinverse), positive-definite matrices (Cholesky), similar matrices, Jordan form, complex matrices (Hermitian, unitary), fast Fourier transform as a change of basis, linear transformations, applications to graphs (Laplacian), applications to differential equations (matrix exponential).
  * **[Axler — *Linear Algebra Done Right* 4e (2024) · *abstract pass*]**: Vector spaces *axiomatically* (no a-priori reference to ℝⁿ), subspaces, sums and direct sums, linear independence, basis, dimension; **linear maps as the central object** (kernel, image, the fundamental theorem of linear algebra); polynomials over ℂ (the algebraic backbone of eigentheory); eigenvalues, eigenvectors, **invariant subspaces, generalised eigenspaces**; **inner-product spaces** (axioms, Cauchy-Schwarz, triangle inequality, orthonormal bases via Gram-Schmidt, orthogonal complements, orthogonal projection as best approximation); **operators on inner-product spaces** (self-adjoint, normal, **the Spectral Theorem — proven without determinants**, polar decomposition, **SVD via the spectral theorem**); positive operators and isometries; trace and determinant *properly* defined (via characteristic polynomial coefficients, not as the Leibniz formula).
  * **[3Blue1Brown — Essence of Linear Algebra (16 videos, evergreen)]**: Geometric intuition for determinants as signed-volume scaling, eigenvectors as invariant directions, change of basis as relabelling, **dot product as the dual of a linear map** (the trick that makes attention "queries · keys" feel inevitable).
  * **[IITM BSMA1003]**: Matrix rank via row reduction, solvability of linear systems, null space / column space correspondence, linear maps, basis transformations, symmetric matrices and spectral theorem.
  * **[Harvard CS 1810 prereq (AM 22a / Math 21b)]**: Inner product spaces, orthogonal complement, projection matrices `P = A(AᵀA)⁻¹Aᵀ`, quadratic forms, positive semi-definiteness as condition for convex loss.
  * **[Cambridge Data Science — Wischik, Lec 2-3 "Feature Spaces"]**: Vector spaces as abstract objects, bases, inner products, orthonormal bases, projection onto subspace, **"model fitting as projection"** (critical insight for understanding linear regression), design of features, basis functions (polynomial, Fourier, radial).
  * **[Cambridge MLMI 1]**: Eigendecomposition as diagonalisation, SVD applications to dimensionality reduction and image compression.
  * **[Strang & Drineas/Mahoney — *Numerical Linear Algebra at scale*]**: Condition number κ(A) and numerical-stability intuition, **why floating-point matters** (catastrophic cancellation; why you never `(AᵀA)⁻¹Aᵀy` in practice — use `np.linalg.lstsq` or QR), **randomised SVD** (Halko-Martinsson-Tropp, 2011 — the algorithm Hugging Face uses for embedding compression), iterative methods (power iteration, Lanczos, Arnoldi → ARPACK), **Krylov subspaces** as preview of conjugate-gradient.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 18.06 OCW SC version (Strang, 2011) — evergreen](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/) · [3Blue1Brown EoLA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
  * **Abstract / Proof Track:** [_Linear Algebra Done Right_ — Axler, **4th Edition, Springer 2024, FREE PDF + Kindle**](https://linear.axler.net/) — the cleanest abstract treatment ever written; 400 pp.; includes worked solutions.
  * **Applications-first Track:** [_Linear Algebra for Data Science, Machine Learning, and Signal Processing_ — Hero/Fessler/Townsend (Cambridge, 2024, hardback)](http://www.cambridge.org/highereducation/isbn/9781009418140) — explicitly cross-references PCA, SVD-of-images, low-rank approximation.
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Linear Algebra_ (**6th Edition, 2023**) — Gilbert Strang. Companion to 18.06.
    * _Linear Algebra and Learning from Data_ (**2019; 2025 reprint with errata**) — Strang — specifically written for ML era; covers randomised SVD, NMF, neural-net Jacobians.
    * ***Linear Algebra Done Right* (Axler, 4e, 2024)** — chapters 1–7 mandatory for proof maturity.
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapters 2, 3, 4.
    * **[*Numerical Linear Algebra* — Trefethen & Bau (SIAM, 1997, 25th-anniversary printing 2022)]** — for any student going into systems / scaling (M19).
  * **Free interactive notebooks:** [`fastai/numerical-linear-algebra` — Rachel Thomas USF (2019, still gold-standard, all-Jupyter)](https://github.com/fastai/numerical-linear-algebra) — covers SVD, randomised methods, PageRank, compressed sensing in 12 lectures.
  * **Practical Implementation:** **NumPy 2.x** (`np.linalg.eig`, `np.linalg.svd`, `np.linalg.solve`, `np.linalg.lstsq`). **SciPy 1.14+** for sparse linear algebra (`scipy.sparse.linalg`, ARPACK eigensolvers, `splu`). Use **`jax.numpy`** for GPU-accelerated linear algebra once comfortable. **`einops` 0.8+** to write tensor operations in *index notation* — once you internalise this, you can read every transformer paper without effort.

* **Mandatory mini-projects (do **all five**):**
  1. **PCA on MNIST from scratch** using only `np.linalg.svd` — recover 95 % variance in `k` components, plot `k`.
  2. **Image compression** via truncated SVD on a single greyscale photo — show MSE-vs-rank curve.
  3. **PageRank** as power iteration on the link-matrix — verify on a 5-node toy graph by hand.
  4. **Linear regression two ways** — `(AᵀA)⁻¹Aᵀy` *vs* `np.linalg.lstsq` *vs* QR *vs* SVD; compare numerical errors on Hilbert matrices (κ ≈ 10¹⁵).
  5. **Spectral clustering** on the two-moons dataset — Laplacian eigenmaps in 30 lines.

* **🔢 Numerical Linear Algebra (2026.2 NEW sub-section):** Production ML code that gets this wrong silently corrupts training.
  * **Factorisations used in ML:** LU (solving Ax=b), Cholesky (SPD systems, Gaussian MLE, KFAC), QR (least-squares, Gram-Schmidt, Arnoldi), **Householder reflections** (numerically stable QR — the *right* way), SVD (low-rank approx, pseudoinverse, PCA), **randomised SVD** (Halko-Martinsson-Tropp — standard for embedding compression at scale).
  * **Iterative solvers:** Conjugate Gradient (CG) for large sparse SPD systems, Lanczos/Arnoldi for dominant eigenvalues, GMRES for non-symmetric. These matter for Gaussian-Process inversion (M13), natural gradient (M17), and implicit differentiation through optimisation (M15).
  * **Condition number & stability:** Why `np.linalg.lstsq(A, b)` beats `np.linalg.inv(A.T @ A) @ A.T @ b` by 10+ orders of magnitude on ill-conditioned designs. Read *Trefethen & Bau* Lectures 12–16.
  * **Floating-point traps:** catastrophic cancellation, log-sum-exp trick, Kahan summation, mixed-precision (bf16/fp16/fp8) for DL.

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The route (≈ 8–12 hours instead of 12 weeks):** Watch [3Blue1Brown — *Essence of Linear Algebra*](https://www.3blue1brown.com/topics/linear-algebra) (16 videos) end to end. That series is already cited in this module's topic list as the source of the geometric intuition — for the fast lane it becomes the *whole* module rather than a companion to Strang and Axler. Optionally add *The Manga Guide to Linear Algebra*. Then do **mini-project 1 only** (PCA on MNIST via `np.linalg.svd`) so the ideas touch code.
>
> **The argument for it:** Video 1 (01:41–02:06) names Essence of Linear Algebra specifically as the Phase 1 resource, with the goal being a mental map, not mastery.
>
> **What you give up — stated plainly:** the two-pass pedagogy above exists because computational fluency and abstract fluency are different skills. You keep neither in full. You will recognise "eigenvector = invariant direction" but not be able to prove the spectral theorem, derive why SVD always exists, or reason about the four fundamental subspaces. Practically, this bites in two places: **understanding *why* PCA works** (rather than that it does), and **numerical stability** — the `(AᵀA)⁻¹Aᵀy` versus `lstsq` trap above is a real production bug you will now only avoid by rule-following.
>
> **Come back when:** you touch [M11](#module-11) beyond `sklearn.decomposition`, [M16](#module-16) attention mathematics, or any systems work where conditioning matters. The Numerical Linear Algebra sub-section is the highest-value re-entry point for engineers.

---

<a id="module-4"></a>
## Module 4: Discrete Math, Algorithms & Data Structures

* **The Tutor's "Why":** Interviews for FAANG/quant/research roles test DSA rigorously; beyond that, you cannot design feature pipelines (hashing, bloom filters) or understand graph ML without it. **Cambridge ML & Bayesian Inference (2025-26) explicitly lists Discrete Mathematics as a prerequisite.**

* **Strict Prerequisites:** Module 1 (can write and debug Python).

* **Exhaustive Topic List:**
  * **[OSSU baseline / GaTech Algorithms I]**: ArrayList implementation, singly/doubly linked lists, stacks, queues, circular buffers, amortised analysis of dynamic arrays.
  * **[OSSU baseline / GaTech Algorithms II]**: Binary trees, BST operations (insert, delete, search, traversal — in/pre/post-order, level-order), heaps (min-heap, max-heap, heapsort, priority queue), skip lists, hashmaps (open addressing vs chaining, load factor, rehashing, perfect hashing).
  * **[GaTech Algorithms III]**: Self-balancing trees — AVL (rotations, balance factor), 2-4 trees, red-black trees, B-trees (used in databases — Module 8), divide-and-conquer (master theorem, merge sort, quicksort, strassen matrix multiplication).
  * **[GaTech Algorithms IV]**: Pattern matching (Boyer-Moore, KMP, Rabin-Karp), graph algorithms (BFS, DFS, topological sort), **Dijkstra's shortest path**, Bellman-Ford, **Minimum Spanning Tree (Prim's, Kruskal's)**, dynamic programming (LCS, edit distance, knapsack, matrix-chain multiplication), NP-completeness, approximation algorithms.
  * **[IITM BSCS2002 — PDSA in Python]**: Complexity analysis (O, Ω, Θ), master theorem proofs, graph representations (adjacency list/matrix), topological sort with DFS, DAG shortest paths, strongly connected components (Tarjan, Kosaraju).
  * **[Cambridge Discrete Math]**: Proof techniques (induction, contradiction, contrapositive), set theory, relations, equivalence classes, partial orders, functions (injection, surjection, bijection), counting (permutations, combinations, inclusion-exclusion, pigeonhole), recurrence relations, generating functions (preview of MGFs in M5), graph theory (Euler paths, Hamiltonian cycles, planarity, chromatic number), elementary number theory (gcd, Euclidean algorithm, modular arithmetic — used in cryptography and hashing).
  * **[Cambridge ML & Real-World Data · Topic 3]**: **Social networks analysis** — properties of networks (degree, diameter), betweenness centrality, clustering using betweenness centrality, detection of cliques in unstructured networks.
  * **[2026.2 addendum — Randomised & Streaming Algorithms]**: **Bloom filters** (false-positive rate calculus, counting bloom, cuckoo filter), **MinHash / locality-sensitive hashing (LSH)** (Jaccard similarity estimation for dedup and near-duplicate detection, used in LLM pre-training data pipelines), **HyperLogLog** (cardinality estimation), **Count-Min Sketch** (frequency estimation for streaming), **reservoir sampling** (uniform sampling from a stream of unknown length), **randomised quicksort**, **Karger's min-cut**. *All of these appear in modern data-engineering interviews (M8a/M8b).*
  * **[Amortised Analysis]**: Aggregate / accounting / potential methods applied to dynamic arrays, splay trees, union-find with path-compression — the mental model behind *"why Python `list.append` is O(1) amortised"*.
  * **[Approximation Algorithms]**: PTAS / FPTAS definitions, vertex-cover 2-approximation, set-cover greedy log-factor, k-means approximation, **primal-dual schema** — relevant for NP-hard pipeline-scheduling problems (M8b).

* **2026 Resources:**
  * **Primary Course Link:** [GaTech DSA I-IV on edX](https://www.edx.org/learn/data-structures/the-georgia-institute-of-technology-data-structures-algorithms-i-arraylists-linkedlists-stacks-and-queues) (Java) **OR** [MIT 6.006 Introduction to Algorithms OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) (Python — **more aligned with 2026 workflow**).
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Algorithms_ (**4th Edition, 2022**) — Cormen, Leiserson, Rivest, Stein (CLRS) — the canonical reference.
    * _Algorithm Design Manual_ (**3rd Edition, 2020**) — Skiena — for problem-solving intuition.
    * _Concrete Mathematics_ (**2nd Edition**) — Graham, Knuth, Patashnik — for discrete-math depth.
  * **Practical Implementation:** Pure Python + `collections` (deque, defaultdict, Counter), **`sortedcontainers`**, **`networkx` 3.x** for graph algorithms, **LeetCode** + **Codeforces** for practice.

* **📦 Module Project (mandatory) — Constraint-based meal planner**
  * **Deliverable:** A program that, given a food database (calories + macros + cost per item) and a set of constraints (daily calorie target, minimum protein, budget ceiling, no more than *k* repeats per week), produces a valid 7-day meal plan. Solve it twice: once with your own search/DP formulation, once with a solver (`pulp` or `ortools`), and compare.
  * **Definition of done:** (1) `pytest` suite including at least one *infeasible* constraint set that your program correctly reports as unsatisfiable rather than crashing or silently returning garbage; (2) `README.md` stating the formulation explicitly — decision variables, objective, constraints; (3) a results memo comparing your hand-rolled search against the solver on runtime and solution quality, and stating the complexity class of the problem you just solved.
  * **Stretch:** Expose it as a Streamlit app so a non-programmer can change the constraints and see a new plan.
  * *Archetype source: video 1 (14:05) — the constraint-based meal planner, cited there specifically because it demonstrates problem formulation rather than model-fitting.*

---

<a id="module-5"></a>
## Module 5: Probability Theory — The Language of Uncertainty

* **The Tutor's "Why":** Harvard's Joe Blitzstein (Stat 110) calls probability "the soul of statistics." In 2026, every ML model is a probability distribution — diffusion models are score-matched Gaussians; LLMs are autoregressive categoricals; Bayesian networks are joint PMFs. This is **the** pivotal module.

* **Strict Prerequisites:** Modules 2 and 3 (integration for continuous RVs; matrices for multivariate distributions).

* **Exhaustive Topic List:** *(Blitzstein's 34-lecture Stat 110 is the spine; everything else confirms or extends it.)*
  * **[Harvard STAT 110 · Lec 1]**: Probability and Counting — sample spaces, events, naïve definition of probability, multiplication rule, permutations, combinations, binomial coefficient identities.
  * **[STAT 110 · Lec 2]**: Story proofs, axioms of probability (Kolmogorov), inclusion-exclusion.
  * **[STAT 110 · Lec 3]**: Birthday problem, properties of probability (monotonicity, Bonferroni).
  * **[STAT 110 · Lec 4-6]**: Conditional probability, Law of Total Probability, Bayes' Theorem, **Monty Hall**, **Simpson's Paradox**.
  * **[STAT 110 · Lec 7-8]**: Gambler's ruin, random variables, CDF, PMF.
  * **[STAT 110 · Lec 9-10]**: **Expectation** — linearity of expectation (with non-independent RVs!), indicator RVs, fundamental bridge.
  * **[STAT 110 · Lec 11]**: **Poisson distribution** — Poisson paradigm, Poisson approximation to binomial.
  * **[STAT 110 · Lec 12-13]**: Discrete vs continuous RVs, **Uniform**, **Normal** (standard and general), 68-95-99.7 rule, universality of the uniform.
  * **[STAT 110 · Lec 14]**: Location, scale, **LOTUS** (Law of the Unconscious Statistician).
  * **[STAT 110 · Lec 16]**: **Exponential distribution** — memorylessness, connection to Poisson process.
  * **[STAT 110 · Lec 17-18]**: **Moment Generating Functions (MGFs)** — uniqueness, computing moments, MGF of sums of independent RVs.
  * **[STAT 110 · Lec 19]**: **Joint, conditional, and marginal distributions**, independence, transformations.
  * **[STAT 110 · Lec 20]**: **Multinomial**, Cauchy (and why its mean doesn't exist).
  * **[STAT 110 · Lec 21]**: **Covariance and Correlation**, Cauchy-Schwarz.
  * **[STAT 110 · Lec 22]**: Transformations of random variables, **convolutions** (sum of RVs).
  * **[STAT 110 · Lec 23]**: **Beta distribution** — conjugate prior for binomial (preview of M13).
  * **[STAT 110 · Lec 24]**: **Gamma distribution**, Poisson process in detail, arrival times.
  * **[STAT 110 · Lec 25-27]**: **Order statistics**, **conditional expectation** as an RV, Adam's law (E[E[Y|X]] = E[Y]), Eve's law (law of total variance).
  * **[STAT 110 · Lec 28]**: **Inequalities** — Markov, Chebyshev, Cauchy-Schwarz, Jensen, Chernoff bounds.
  * **[STAT 110 · Lec 29]**: **Law of Large Numbers** (weak and strong), **Central Limit Theorem** (statement and MGF proof).
  * **[STAT 110 · Lec 30]**: **Chi-squared**, **Student-t**, **Multivariate Normal** (mean vector, covariance matrix, conditional MVN).
  * **[STAT 110 · Lec 31-33]**: **Markov chains** — transition matrix, stationary distribution, reversibility, convergence (detailed balance preview for MCMC).
  * **[STAT 110 · Lec 34]**: A look ahead — Brownian motion, martingales.
  * **[MIT 6.431x / MicroMasters C1]**: Complements Stat 110 with a more engineering-flavoured treatment — probability spaces, conditioning as information update, Bayesian vs frequentist views introduced, discrete/continuous RVs, multiple RVs, derived distributions, convergence in probability vs distribution vs almost sure, Bernoulli process, Poisson process, elementary queueing, hidden random processes.
  * **[IITM BSMA1002 · Week 1-12]**: Types of data and scales of measurement (nominal/ordinal/interval/ratio), descriptive vs inferential statistics; frequency distributions; measures of central tendency (mean/median/mode) with formal definitions; measures of dispersion (range, variance, standard deviation, IQR); five-number summary and boxplots; association (contingency tables, Pearson correlation, point-biserial correlation); counting principles (addition/multiplication rule, factorials); permutations and combinations; probability (events, axioms); conditional probability, multiplication rule, independence, law of total probability, Bayes' theorem; random variables (PMF, CDF); expectation and variance of discrete RVs; Bernoulli trials, binomial, Poisson; continuous RVs (uniform, exponential).
  * **[Cambridge Data Science — Wischik · "Handling probability models"]**: PDF and CDF manipulation, Bayes's rule, **Monte Carlo estimation** (first rigorous introduction), empirical distribution as a function.
  * **[Cambridge Data Science — Wischik · "Random processes"]**: Markov chains (discrete time), **stationarity and drift analysis**, processes with memory, learning a random process from data.

* **Critical Additions (April 2026):**
  * **Concentration inequalities for ML — beyond Chebyshev:** **Hoeffding's inequality** (the workhorse of generalisation bounds), **McDiarmid's bounded-differences inequality**, **Bernstein's inequality**, **sub-Gaussian** and **sub-exponential** random variables, ψ-Orlicz norms, **Bernstein-Chernoff bound for VC-dimension** (the 1971 Vapnik-Chervonenkis result that started statistical learning theory). Without these you cannot read a single PAC-learning theorem in M9.
  * **Information theory primer (the overlap with probability):** **entropy `H(X) = −Σ p log p`**, joint and conditional entropy, **mutual information `I(X;Y)`**, **KL divergence `D_KL(P‖Q)` and Jensen's inequality**, cross-entropy (the loss function of every classifier and every LM), **f-divergences** (TV, JS, Hellinger), **Fano's inequality** (lower bounds for classification error). Cited from MIT 6.7960 Wk 5–6 (Information Theory) and Cover & Thomas Ch 1–2.
  * **Measure-theoretic bridge — *taught minimally so you can read PML2 (Murphy 2023)*:** σ-algebras (Borel), measurable functions, Lebesgue integral *vs* Riemann (why we need it: integrating discontinuous limits), **Radon-Nikodym derivative `dν/dμ`** (the *correct* definition of "density"), almost-sure convergence vs convergence in probability vs in distribution vs in `L²` (the four convergence types every probabilist mixes up), pushforward measures, **dominated and monotone convergence theorems** (used implicitly every time you swap an integral and a limit in MCMC analysis). **Goal:** read Wasserman *All of Statistics* Ch 21 or Murphy PML2 Ch 1 without panic — *not* to do measure-theoretic exercises.
  * **Probability in code — *do these three concretely*:** (1) **inverse-CDF sampling** for any 1-D distribution, hand-coded; (2) **rejection sampling** + **importance sampling** with diagnostics (effective sample size); (3) **Monte-Carlo integration** of a 5-D integral with confidence-interval analysis.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard Stat 110 full playlist (Blitzstein, 34 lectures)](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) · [Handouts & problems](https://stat110.hsites.harvard.edu/) (browser only — `curl` is bot-gated) · [MITx 6.431x](https://micromasters.mit.edu/ds/)
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Probability_ (**2nd Edition, 2019; 2024 reprint**) — Joseph Blitzstein & Jessica Hwang — [free PDF](https://projects.iq.harvard.edu/stat110/home) — **chapters 1-12 cover-to-cover**. This is the primary text.
    * _Introduction to Probability_ (**2nd Edition, 2008**) — Bertsekas & Tsitsiklis — companion to 6.431x.
    * **[_Introduction to Probability for Data Science_ — Stanley H. Chan (Michigan Publishing, 2021/2023, FREE PDF + HTML)](https://probability4datascience.com/)** — *the* book that bridges Stat-110-style probability to Python/MATLAB code; hundreds of worked computational examples; **adopted by 30+ US engineering programmes** (incl. Purdue, Michigan).
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapter 6.
    * **[_Information Theory, Inference, and Learning Algorithms_ — David MacKay (Cambridge 2003, **free PDF**)](https://www.inference.org.uk/itila/)** — a singular masterpiece; chapters 1–6 give the cleanest entropy/MI exposition in any language.
    * **[_High-Dimensional Probability_ — Roman Vershynin (Cambridge 2018, **free draft online**)](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html)** — *the* reference for sub-Gaussian, concentration, and random matrices; chapters 1–3 sufficient for ML purposes.
    * **(Optional, PhD-track only)** _Probability with Martingales_ — David Williams (Cambridge 1991), or _Measure, Integral and Probability_ — Capinski & Kopp (Springer 2nd ed., 2014) — for the measure-theoretic complement after Stat 110.
  * **Practical Implementation:** **SciPy 1.14+** `scipy.stats` (every distribution you'll need); **NumPy** `np.random.Generator` (modern PCG64 / Philox RNG, **default since NumPy 1.17**); begin using **`distrax`** (JAX) or **`torch.distributions`** (PyTorch) for *differentiable* distributions — you'll need these in M13. **`tensorflow_probability` 0.24+** (JAX-substrate) for advanced bijectors (used in normalising flows, M16).

* **Suggested Pace (12 weeks at 10 hrs/week):**
  * Weeks 1–8: Stat 110 lectures 1–28 + Blitzstein-Hwang exercises 1–10 from each chapter.
  * Weeks 9–10: Concentration inequalities + information-theory primer (MacKay Ch 1–6 + Vershynin Ch 1–2).
  * Weeks 11–12: Stat 110 lectures 29–34 + measure-theoretic bridge (Wasserman Ch 21 *or* Capinski-Kopp Ch 1–4 if PhD-track).
  * **Capstone exercise:** write a 30-line script that empirically demonstrates the CLT, the Hoeffding bound, and the Galton-Watson process, all in one notebook. *If you can do this without help, you have actually learned probability.*

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The route (≈ 15–20 hours instead of 120):** [StatQuest's probability and statistics playlists](https://statquest.org/) plus *The Manga Guide to Statistics*, then — and this part is **mandatory even on the fast lane** — the capstone exercise above. Simulating the CLT yourself is cheap, requires no proof machinery, and is the single highest-value hour in this module.
>
> **The argument for it:** Video 1 (02:18–02:42) treats probability as something absorbed through StatQuest alongside ML overviews rather than as a standalone 12-week course. Video 3 (06:03) makes StatQuest's *Illustrated Guide to Machine Learning* one of its seven books precisely because it teaches "how the math actually applies to the results."
>
> **What you give up — stated plainly:** more than in any other math module. Probability is where the fast lane is most expensive, because uncertainty is not an implementation detail — it is the object being modelled. Without MGFs, conditional expectation as a random variable, and the concentration inequalities, you cannot reason about why a validation estimate is trustworthy, why a confidence interval is the width it is, or what a Bayesian posterior actually is. **This is the one math module we recommend fast-lane learners over-invest in relative to the video doctrine.**
>
> **Come back when:** you enter [M6](#module-6) inference in earnest, [M6½](#module-6-half) causal work, [M13](#module-13), or any role with "Data Scientist" in the title. In our [job survey](#skills-checklist), statistics/inference language appeared in 5 of 16 postings and A/B-testing language in 6 of 16 — concentrated almost entirely in the DS roles.

* **📦 Module Project (mandatory) — Monte Carlo intuition engine**
  * **Deliverable:** A simulation suite that answers four probability questions numerically *and* analytically, and shows the two converge: (1) the birthday problem, (2) the Monty Hall problem, (3) the coupon-collector expected time, (4) a random walk's hitting-time distribution. One module per problem, one shared `simulate(n_trials)` interface.
  * **Definition of done:** (1) `pytest` suite asserting each simulated estimate lands within a stated tolerance of the closed-form answer at a fixed seed; (2) `README.md` with a convergence plot per problem (estimate vs `n_trials`, with the analytic value as a horizontal line); (3) a results memo explaining what the convergence rate you observed tells you about the Law of Large Numbers and the CLT.
  * **Stretch:** Add a variance-reduction technique (antithetic variates or control variates) to one problem and quantify the efficiency gain.
  * *This project is the reason the [fast lane](#practitioner-track) tells you to over-invest in M5 relative to the other maths modules: probability is the one branch you cannot fake with library calls.*

---

# 🟨 CORE STATISTICS STRATUM (Modules 6–8)

<img src="assets/stratum-2-statistics.jpg" alt="Statistics and data stratum, modules 6 to 8" width="100%">

---

<a id="module-6"></a>
## Module 6: Statistical Inference

* **The Tutor's "Why":** This is where mathematics meets reality. Every p-value in a Nature paper, every A/B test at Meta, every FDA drug approval, hinges on the concepts in this module. Harvard STAT 111 and MIT 18.6501x are the twin pillars.

* **Strict Prerequisites:** Module 5 (must know MGFs, CLT, joint distributions).

* **Exhaustive Topic List:**
  * **[Harvard STAT 111 / MIT 18.6501x]**: Statistical models (parametric, non-parametric, semi-parametric); estimators and their properties — unbiasedness, consistency, efficiency, sufficiency (Neyman-Fisher factorisation), completeness, Rao-Blackwell theorem, Lehmann-Scheffé theorem; Cramér-Rao lower bound.
  * **[MIT 18.6501x]**: **Maximum Likelihood Estimation** — construction, invariance, asymptotic normality, Fisher information, observed vs expected information; **Method of Moments**; delta method.
  * **[MIT 18.6501x]**: **Parametric hypothesis testing** — null vs alternative, Type I / Type II errors, power, size, Neyman-Pearson lemma, Likelihood Ratio Test (Wilks' theorem), Wald test, score test.
  * **[MIT 18.6501x]**: Confidence intervals — construction by pivoting, Wald CIs, likelihood-based CIs, bootstrap CIs.
  * **[MIT 18.6501x]**: Goodness-of-fit tests — chi-squared test, Kolmogorov-Smirnov test, Anderson-Darling.
  * **[MIT 18.6501x]**: Linear regression inference — Gauss-Markov theorem proof, sampling distribution of β̂, ANOVA decomposition (SST = SSR + SSE), F-test for nested models.
  * **[Harvard CS109A · Lec 7 "Probability"]**: Review of Stat 110 concepts in regression context.
  * **[Harvard CS109A · Lec 8 "Inference in Regression and Hypothesis Testing"]**: t-tests for regression coefficients, confidence vs prediction intervals, multiple testing issues (Bonferroni, Holm, Benjamini-Hochberg FDR).
  * **[Harvard CS109A · Lec 21 "Experimental Design"]**: Randomisation, blocking, factorial designs, power analysis (a priori sample size computation), **causal inference preview** (ATE, ATT), Simpson's paradox revisited.
  * **[Cambridge Data Science · "Inference"]**: **Bayesianism** vs **frequentism** — epistemic vs aleatory uncertainty. Frequentist confidence intervals construction. Hypothesis testing as decision rule. **Bootstrap resampling** (non-parametric bootstrap, parametric bootstrap, block bootstrap for time series).
  * **[IITM BSMA1004 — Statistics for Data Science II]**: Sampling distributions (χ², t, F); estimation (point and interval); tests for one/two means/proportions/variances; paired t-test; McNemar's test; non-parametric tests (sign, Wilcoxon, Mann-Whitney, Kruskal-Wallis); contingency tables (χ² test of independence); ANOVA (one-way, two-way, with and without interaction); simple and multiple linear regression hypothesis testing.
  * **[Harvard CS 1810]**: Estimators — **Maximum a Posteriori (MAP)** as the Bayesian regularised counterpart to MLE.

* **2026 Resources:**
  * **Primary Course Link:** [MITx 18.6501x Fundamentals of Statistics](https://www.edx.org/course/fundamentals-of-statistics) · [Harvard STAT 111 course page](https://beta.my.harvard.edu/course/STAT110/2025-Fall/001)
  * **Required Reading (Latest 2026 Editions):**
    * _All of Statistics_ (**2nd printing, Springer 2004**, still canonical) — Larry Wasserman — chapters 6–15.
    * _Statistical Inference_ (**2nd Edition**) — Casella & Berger — the rigorous graduate-level reference.
    * _An Introduction to Statistical Learning with Python (ISLP)_ (**2023, 2025 reprint**) — James, Witten, Hastie, Tibshirani, Taylor — Chapters 2-3.
  * **Practical Implementation:** **`statsmodels` 0.14+** for classical inference (OLS, GLM, ANOVA), **`pingouin`** for modern stats API, **`scipy.stats`** for tests. Use **R 4.4+** with `{tidyverse}`, `{broom}`, `{infer}` for when you need publication-grade stats.

* **➡️ Cross-ref note (NEW v2026.2):** A/B testing, experimental design, and causal inference have been promoted out of this module into a **dedicated Module 6½ — Causal Inference & Experimentation** (directly below) because every senior-DS interview at Meta / Netflix / Booking / Uber tests this material in depth.

* **📦 Module Project (mandatory) — Inference toolkit from scratch**
  * **Deliverable:** A package implementing, without `scipy.stats` doing the work for you: bootstrap confidence intervals (percentile + BCa), a permutation test, a two-sample t-test, and a multiple-comparison correction (Bonferroni + Benjamini–Hochberg). Then run all four on one real dataset and write up what they disagree about.
  * **Definition of done:** (1) `pytest` suite cross-validating each of your implementations against the `scipy.stats` equivalent to within tolerance; (2) `README.md` stating each test's assumptions and what happens when they are violated; (3) a results memo that includes at least one honest instance of *"this test said significant and I do not believe it, here is why."*
  * **Stretch:** Add a power-analysis function and use it to compute the sample size your dataset would have needed to detect a stated effect. Log the result — this is the calculation that most real experiment designs skip.
  * **Anti-goal:** Do not produce a notebook full of p-values. The deliverable is a tested library plus a document about uncertainty.

---

<a id="module-6-half"></a>
## Module 6½: Causal Inference & Experimentation

* **The Tutor's "Why":** In 2026, this is the #1 differentiator between a *junior ML engineer* and a *senior data scientist*. Netflix, Meta, Uber, Booking, Airbnb, and every product-data-science org hires specifically for causal-inference fluency. Berkeley MIDS dedicates an entire course to it ([DATA 241 · Causal Inference](https://www.ischool.berkeley.edu/courses/datasci/241) ✅). MIT 14.387 *Mostly Harmless Big Data* covers the econometric half. **Correlation≠causation is not a slogan — it is a formal theorem (Pearl's do-calculus).** This module closes the single largest production-DS gap identified in the April 2026 benchmark PDF.

* **Strict Prerequisites:** Module 5 (joint distributions, conditional expectation), Module 6 (hypothesis testing, CIs, bootstrap).

* **Exhaustive Topic List:**
  * **A/B Testing Foundations:** Randomisation as the identification strategy, potential outcomes framework (Rubin/Neyman), ATE / ATT / CATE / LATE estimands, sample-size and MDE (minimum detectable effect) calculations, one-sided vs two-sided tests, Type I/II control, **sequential testing & always-valid p-values** (Howard et al. 2021), **group-sequential designs** with O'Brien-Fleming/Pocock boundaries, **CUPED variance reduction** (Deng et al. Microsoft 2013 — the single most impactful variance-reduction trick), stratified randomisation, cluster-randomised experiments.
  * **Interference & Network Effects:** **SUTVA violations**, switchback experiments (Uber/Lyft), **spillover** in social networks, ego-cluster randomisation, graph-cluster randomisation, synthetic control for marketplace platforms.
  * **Multiple Testing:** Bonferroni, Holm-Bonferroni, Hochberg, **Benjamini-Hochberg FDR control**, Storey's q-values, sequential multiple testing.
  * **Resampling-Based Inference:** Non-parametric bootstrap (Efron), parametric bootstrap, block bootstrap for time-series, **permutation tests** (exact inference under the null), conformal inference preview (M9).
  * **Bayesian A/B Testing:** Beta-Binomial for conversion rates, Normal-Normal for continuous metrics, **expected loss / expected regret stopping rules**, multi-armed bandits (Thompson sampling, UCB) as a replacement for fixed-horizon A/B tests.
  * **Causal Graphs & do-Calculus:** Directed Acyclic Graphs (DAGs), **d-separation** criterion, Markov equivalence classes, **Pearl's do-operator** and the three rules of do-calculus, confounders / mediators / colliders, **M-bias** and **butterfly-bias** (colliders you didn't know you conditioned on), identifiability.
  * **Adjustment Strategies:** **Backdoor criterion** (sufficient-adjustment sets), **frontdoor criterion**, **instrumental variables (IV)** and the LATE theorem (Imbens-Angrist), **2SLS**, **Difference-in-Differences (DiD)** and parallel-trends assumption, **Regression Discontinuity Design (RDD)** sharp and fuzzy, **Synthetic Control Method** (Abadie et al.), **matching** (exact, Mahalanobis, propensity-score, CEM).
  * **Modern Causal ML:** **Double/Debiased ML** (Chernozhukov et al. 2018) as the bridge to high-dimensional confounders, **Causal Forests** (Wager & Athey) for heterogeneous treatment effects, **doubly-robust estimators** (AIPW, TMLE), **meta-learners** (S-, T-, X-, R-, DR-learner), **uplift modelling** for marketing.
  * **Python Stack:** [DoWhy](https://github.com/py-why/dowhy) ✅ (end-to-end causal workflow), [EconML](https://econml.azurewebsites.net/) ✅ (Microsoft, heterogeneous TE), [CausalML](https://causalml.readthedocs.io/) ✅ (Uber, uplift), [Pyro](https://pyro.ai/) (probabilistic programming for causal models), `statsmodels` IV/2SLS, `linearmodels` (panel/IV).

* **2026 Resources:**
  * **Primary Course (free):** [Brady Neal — *Introduction to Causal Inference*, Fall 2020 (YouTube + lecture notes; still the gold-standard free course)](https://www.bradyneal.com/causal-inference-course) ✅
  * **Econometric track:** [MIT 14.387 — *Applied Econometrics (Mostly Harmless Big Data)*, Fall 2014 OCW](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) ✅
  * **Harvard CAUSALab** — [course materials + *What If* book](https://www.hsph.harvard.edu/causal/) ✅
  * **Practical book (free, 2024):** [Matheus Facure — *Causal Inference for the Brave and True*](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) ✅ — every chapter is a runnable notebook.
  * **Required Reading:**
    * Hernán & Robins — [*Causal Inference: What If* (free PDF, 2024 revision)](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf) ✅
    * Pearl, Glymour & Jewell — *Causal Inference in Statistics: A Primer* (Wiley 2016).
    * Pearl — *Causality: Models, Reasoning, and Inference* (Cambridge 2e, 2009) — the reference.
    * **Kohavi, Tang & Xu** — [*Trustworthy Online Controlled Experiments*](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) ✅ (Cambridge 2020) — **the industrial A/B-testing bible**.
  * **Communities / living resources:** [exp-platform.com](https://exp-platform.com/) ✅ (Ron Kohavi's blog + papers from Microsoft ExP platform), [Statistical Modeling, Causal Inference & Social Science (Gelman blog)](https://statmodeling.stat.columbia.edu/), Pearl's *UCLA Causality Blog*.

* **📋 Mandatory mini-projects:**
  1. **Design + simulate an A/B test** with CUPED variance reduction — show the % reduction in required sample size.
  2. **Fit an IV regression** on a realistic dataset (e.g., [NLSY or Angrist-Krueger 1991 compulsory-schooling](https://economics.mit.edu/sites/default/files/publications/Does%20Compulsory%20School%20Attendance.pdf)) — reproduce the returns-to-education estimate.
  3. **Use DoWhy end-to-end**: model → identify → estimate → refute — on a confounded synthetic dataset; show refutation tests (placebo, random common cause, unobserved-confounder sensitivity).
  4. **Causal Forest on lalonde / criteo-uplift**: estimate CATEs, plot HTE heatmap, produce a targeting policy + its evaluation via doubly-robust off-policy estimation.

---

<a id="module-7"></a>
## Module 7: Data Wrangling, EDA & Visualisation

* **The Tutor's "Why":** "The data scientist spends 80% of their time on data preparation" is a cliché because it's true. Harvard CS109A dedicates **three full weeks** to this before any modelling.

* **Strict Prerequisites:** Module 1 (Python).

* **Exhaustive Topic List:**
  * **[Harvard CS109A · Lec 1 "Introduction to CS109A"]**: The data-science life-cycle (CRISP-DM revisited for 2026), question framing, translating business problems into statistical ones.
  * **[Harvard CS109A · Lec 2 "Introduction to PANDAS and EDA"]**: `DataFrame` / `Series` model, indexing (`.loc`, `.iloc`), filtering, `groupby`-`apply`-`combine`, `merge`/`join`/`concat`, `melt`/`pivot`/`stack`/`unstack`, datetime handling, categorical dtype, missing-value representations.
  * **[Harvard CS109A · Lab 1 "Data formats, sources, and scraping"]**: Web scraping with BeautifulSoup, Requests session management, handling JS-rendered pages with Playwright, API consumption (REST, GraphQL, OAuth), handling CSV/TSV/JSON/JSONL/Parquet/Arrow/Avro.
  * **[Harvard CS109A · Lab 2 "Pandas & EDA 2"]**: Outlier detection (z-score, IQR rule, isolation forest preview), distributional plots (histogram binning strategies — Freedman-Diaconis, Sturges, Scott), QQ plots, log-transforms, Box-Cox transforms.
  * **[Harvard CS109A · Lec 9 "Missing Data & Imputation"]**: MCAR / MAR / MNAR taxonomy (Rubin 1976), listwise/pairwise deletion, mean/median/mode imputation, **k-NN imputation**, **MICE (Multivariate Imputation by Chained Equations)**, multiple imputation, domain-specific imputation.
  * **[Harvard CS109A · Lec 12 "Visualization"]**: Grammar of graphics (Wilkinson), Cleveland-McGill perceptual hierarchy (position > length > angle > area > colour), Tufte's principles (data-ink ratio, small multiples), choropleth vs cartogram, interactive dashboards.
  * **[Harvard CS109A · Lec 13 "Ethics"]**: Fairness in data collection, selection bias, survivorship bias, historical bias, measurement bias, informed consent, differential privacy preview.
  * **[IITM BSMS2001 — Business Data Management]**: Real-world data in business context, Excel-to-Python migration, data warehousing vs data lakes, ETL vs ELT, slowly-changing dimensions.
  * **[IITM BSMS2002 — Business Analytics]**: Descriptive / diagnostic / predictive / prescriptive analytics framework, KPIs, dashboarding, **Tableau / PowerBI** vs **Streamlit / Dash / Plotly**.
  * **[MIT 15.773 — Hands-on DL]**: Data-centric AI — **data augmentation**, weak supervision, active learning preview, label noise.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109A 2021 schedule](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) (latest public) · Lectures 1, 2, 9, 12, 13, 21.
  * **Required Reading (Latest 2026 Editions):**
    * _Python for Data Analysis_ (**3rd Edition, 2022**) — Wes McKinney (pandas creator) — chapters 5–10.
    * _Storytelling with Data_ — Cole Nussbaumer Knaflic — communication principles.
    * _Fundamentals of Data Visualization_ — Claus Wilke — [free online](https://clauswilke.com/dataviz/).
  * **Practical Implementation:** **Polars 1.x** (fastest DataFrame library of 2026, Arrow-native, lazy evaluation) as primary; **pandas 2.2+** with PyArrow backend for compatibility. **`matplotlib 3.9+`**, **`seaborn 0.13+`**, **`plotly 5.x`**, **`altair 5.x`**, and **`great_tables`** for publication-grade tables. **`ydata-profiling`** (formerly pandas-profiling) for automated EDA.

* **🔧 Modern Data Tooling:**
  * **[Polars 1.40+](https://pola.rs/)** ✅ — the pandas successor; Rust-powered, Arrow-native, lazy frames, query optimiser. Learn `pl.LazyFrame`, `pl.col`, `pl.Expr`, expression-based group-by, streaming engine.
  * **[DuckDB 1.5+](https://duckdb.org/)** ✅ — "SQLite for analytics." In-process OLAP over Parquet/Arrow; zero-config; faster than pandas on anything > 100MB. Perfect for EDA on 100-GB datasets from a laptop.
  * **[Great Expectations](https://greatexpectations.io/)** ✅ + **[Pandera](https://pandera.readthedocs.io/)** ✅ — schema + data-quality validation; declarative expectations; catch data drift before it reaches models.
  * **[Plotly 5.x](https://plotly.com/python/)** ✅ + **[Altair 5.x](https://altair-viz.github.io/)** ✅ + **[Observable Plot](https://observablehq.com/plot/)** ✅ — the modern grammar-of-graphics ecosystem; Plotly for interactivity, Altair for Vega-Lite precision.
  * **Dashboards:** **[Streamlit](https://streamlit.io/)** ✅ for ML demos, **[Gradio](https://www.gradio.app/)** ✅ for HF-style model UIs, **[Evidently](https://www.evidentlyai.com/)** ✅ for data-drift dashboards.
  * **Feature Engineering Discipline:** Target encoding with K-fold smoothing, **train-test leakage** (temporal, group, target-leak from future aggregates), time-based features (lag, rolling, expanding windows), cyclical encoding (sin/cos of hour/month), **sklearn Pipelines + ColumnTransformer** as the *only* correct way to avoid leakage. Reference: [*Feature Engineering for Machine Learning* — Zheng & Casari (O'Reilly 2018)](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/).

* **📦 Module Project (mandatory) — End-to-end EDA on a dataset nobody has cleaned**
  * **Deliverable:** Pick a genuinely messy public dataset — a government open-data portal, not a Kaggle "cleaned" CSV. Produce a reproducible pipeline (script, not a notebook) that ingests raw files, validates them, cleans them, and emits both a tidy Parquet file and a small set of publication-quality figures answering three questions you wrote down *before* you started.
  * **Definition of done:** (1) A data-validation layer (`pandera` or explicit assertions) that fails loudly on schema drift, plus a `pytest` suite over your transform functions; (2) `README.md` with the three questions, the three figures, and a data dictionary; (3) a results memo listing every judgement call you made while cleaning — dropped rows, imputed values, outliers kept or removed — because that list is what a reviewer will actually interrogate.
  * **Stretch:** Re-run the same pipeline in Polars and report the wall-clock difference on the full dataset.
  * **Anti-goal:** No `df.describe()` dumps. Every figure must answer a stated question.

---

<a id="module-8a"></a>
## Module 8a: Databases, SQL & Warehouses

* **The Tutor's "Why":** In 2026, data rarely fits in RAM. IITM dedicates a full diploma-level course (BSCS2001) + two specialisation courses to this. You need SQL fluency for 90% of industry jobs. **Module 8 has been split in v2026.2** into **M8a (Databases, SQL & Warehouses)** here, and **M8b (Distributed Data & Streaming)** directly below — because the 2026 production data stack (Spark + Iceberg + Airflow + Kafka + dbt) is a full module in its own right and cannot share airtime with SQL fundamentals.

* **Strict Prerequisites:** Module 4 (hashing, trees, randomised/streaming algos).

* **Exhaustive Topic List:**
  * **[IITM BSCS2001 — DBMS (Prof. P.P. Das)]**: Relational model (tuples, relations, schemas, keys — super/primary/candidate/foreign), relational algebra (selection σ, projection π, union, intersection, difference, Cartesian product, join variants, division), **SQL DDL** (CREATE, ALTER, DROP), **SQL DML** (SELECT/INSERT/UPDATE/DELETE), JOINs (inner, left/right/full outer, cross, self, lateral), subqueries (correlated vs uncorrelated), CTEs (recursive and non-recursive), window functions (`OVER`, `PARTITION BY`, `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM() OVER`), set operations (UNION, INTERSECT, EXCEPT), views, indexes (B-tree, hash, bitmap, covering), transactions and **ACID properties**, isolation levels (read uncommitted/committed, repeatable read, serialisable), concurrency control (two-phase locking, MVCC), recovery (WAL, ARIES), normalisation (1NF/2NF/3NF/BCNF/4NF/5NF), functional dependencies, Armstrong's axioms.
  * **Advanced SQL (2026 Industry Interview Canon):** Query plans (EXPLAIN ANALYZE), cost-based optimisation, partitioning (range/list/hash), bitmap indexes, covering indexes, **recursive CTEs** for hierarchical data, **LATERAL joins**, **PIVOT / UNPIVOT**, **MERGE / UPSERT**, JSON/JSONB queries (Postgres), array types, `PERCENTILE_CONT`, `QUALIFY` clause (Snowflake/BQ), approximate aggregations (`APPROX_COUNT_DISTINCT` powered by HyperLogLog).
  * **[OSSU baseline — Coursera DB Specialisation]**: Data warehouse concepts (star schema, snowflake schema, fact/dimension tables), OLAP cubes, slice/dice/drill-down/roll-up, **SCD Type 0/1/2/3/6**, ETL vs ELT pipeline design, **Kimball dimensional modelling**, Data Vault 2.0 (preview).
  * **Cloud Warehouses (2026 production stack):** **Snowflake** (warehouses, virtual warehouses, time travel, zero-copy clone), **BigQuery** (slot-based pricing, BI-engine, materialised views), **Amazon Redshift**, **Databricks SQL Warehouse**, **DuckDB** (single-node), **ClickHouse** (OLAP, real-time).
  * **[dbt — Data Build Tool](https://docs.getdbt.com/)** ✅: models, sources, tests (`unique`, `not_null`, `accepted_values`, relationships), **macros** (Jinja templating), **incremental models** (with `unique_key`, late-arriving facts), **snapshots** (SCD Type 2 automation), **packages** (`dbt_utils`, `dbt_expectations`), exposures, metrics, MetricFlow integration.
  * **[OSSU — MongoDB path]**: Document databases, BSON, sharding, replica sets, aggregation pipeline ($match, $group, $project, $lookup, $unwind), indexing strategies.

* **2026 Resources:**
  * **Primary Course Link:** [IITM BSCS2001 course page](https://study.iitm.ac.in/ds/course_pages/BSCS2001.html) · [Stanford CS145 Intro to Databases](https://web.stanford.edu/class/cs145/) ✅ · [Databricks Academy](https://www.databricks.com/learn/training/home) (free path) · [dbt Learn](https://learn.getdbt.com/) ✅ (free dbt Fundamentals course).
  * **Required Reading (Latest 2026 Editions):**
    * _Designing Data-Intensive Applications_ — Martin Kleppmann (2017; 2026 revised edition in progress) — chapters 1–4, 10–11.
    * _Database System Concepts_ (**7th Edition, 2019**) — Silberschatz, Korth, Sudarshan.
    * **The Kimball Group** — [*The Data Warehouse Toolkit* (3e)](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) ✅ — the dimensional-modelling bible.
    * Reis & Housley — [*Fundamentals of Data Engineering*](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ✅ (O'Reilly 2022) — Chapters 5–8 for the DB/warehouse half.
  * **Practical Implementation:** **PostgreSQL 17** (with `pgvector` extension), **DuckDB 1.5+**, **SQLAlchemy 2.x** with async, **dbt-core 1.11.8**, **sqlmesh** (dbt alternative), **Snowflake** or **BigQuery** free-tier for cloud practice.

* **📦 Module Project (mandatory) — Reddit scraper → warehouse → dashboard**
  * **Deliverable:** A pipeline that pulls posts and comments from a subreddit you actually care about, lands them in PostgreSQL with a sane normalised schema (plus indexes you can justify), transforms them with SQL into a small star schema, and surfaces three metrics in a Streamlit dashboard.
  * **Definition of done:** (1) Schema DDL committed as migrations, not typed into a client by hand; a `pytest` suite over the extraction and transform layers with the API mocked; (2) `README.md` containing your ER diagram and the `EXPLAIN ANALYZE` output for your slowest query, before and after you added the index; (3) a results memo on what you learned about the data that you did not expect.
  * **Stretch:** Add incremental loading with a watermark column so a re-run does not re-ingest history, and schedule it.
  * *Archetype source: video 1 (13:40) — the Reddit-scraper tier, promoted here from a toy script to a warehouse exercise because SQL is the highest-frequency skill in the [surveyed 2026 postings](#skills-checklist).*

---

<a id="module-8b"></a>
## Module 8b: Distributed Data & Streaming Systems

* **The Tutor's "Why":** Every senior-DS / MLE interview in 2026 covers Spark, Kafka, Airflow, and the lakehouse pattern. Closing this is closing Gap #2 in the benchmark PDF — the single largest production gap. Joe Reis (*Fundamentals of Data Engineering*) and the DataExpert free bootcamp are the two canonical on-ramps.

* **Strict Prerequisites:** Module 4 (randomised / streaming algos, hashing), Module 8a (SQL fluency), Module 1 (async Python).

* **Exhaustive Topic List:**
  * **Storage & File Formats:** **Parquet** (columnar, predicate pushdown, row-groups, page-level statistics), **Apache Arrow** (in-memory columnar, zero-copy IPC), **ORC**, **Avro** (schema evolution), object storage (S3 / GCS / Azure Blob), **lakehouse table formats** — [Apache Iceberg](https://iceberg.apache.org/) ✅ (hidden partitioning, snapshot isolation, time travel, MERGE INTO), [Delta Lake](https://delta.io/) ✅ (ACID on data lake, Z-ordering, vacuum), [Apache Hudi](https://hudi.apache.org/) (streaming upserts).
  * **Distributed Compute:** **Apache Spark 3.5+** — RDDs, DataFrames, Dataset API, Catalyst optimiser, Tungsten execution, **Adaptive Query Execution (AQE)**, broadcast joins vs sort-merge, skew-handling, partitioning and bucketing, caching strategies, PySpark idioms, Spark SQL, MLlib (legacy), **Structured Streaming** (micro-batches, triggers, watermarks). **[Ray Data](https://docs.ray.io/en/latest/data/data.html)** ✅ + **[Dask](https://www.dask.org/)** ✅ as Python-native alternatives. **[Apache Beam](https://beam.apache.org/)** as the portable API.
  * **Orchestration:** **[Apache Airflow](https://airflow.apache.org/)** ✅ — DAGs, operators, sensors, XComs, task groups, dynamic task mapping, backfills, SLAs. **[Dagster](https://dagster.io/)** ✅ — asset-oriented orchestration, software-defined assets, declarative scheduling. **[Prefect](https://www.prefect.io/)** ✅ — Pythonic flows, deployments, agents.
  * **Streaming:** **[Apache Kafka](https://kafka.apache.org/)** ✅ — brokers, topics, partitions, consumer groups, offsets, ISR, **exactly-once semantics**, Kafka Streams, Kafka Connect, Schema Registry (Avro/Protobuf). **[Redpanda](https://redpanda.com/)** ✅ (Kafka-compatible, C++). **[Apache Flink](https://flink.apache.org/)** ✅ (true-streaming, event-time, watermarks, windowing — tumbling/sliding/session, stateful functions). **[Materialize](https://materialize.com/)** / **[RisingWave](https://risingwave.com/)** (streaming SQL).
  * **CAP, Consensus & Consistency:** CAP theorem, PACELC, consensus (Paxos, Raft), eventual consistency, **CRDTs** for collaborative systems, idempotency, exactly-once vs at-least-once vs at-most-once.
  * **[MIT Mining Massive Datasets / Stanford CS246]**: MapReduce algorithms (word count, inverted index, joins), **LSH** (MinHash, random projections), PageRank as eigenvector of stochastic matrix, recommendation systems at scale, frequent itemsets (A-Priori, PCY, Multistage), streaming algorithms (reservoir sampling, Bloom, Count-Min Sketch, HyperLogLog), AdWords / online bipartite matching.

* **2026 Resources:**
  * **Primary Course Link:** [Stanford CS246 2025 lectures (Leskovec)](https://web.stanford.edu/class/cs246/) · [DataExpert.io Free Data Engineer Bootcamp (2025, Zach Wilson)](https://www.dataexpert.io/free-data-engineer-bootcamp) ✅ · [Databricks Spark path](https://www.databricks.com/learn/training/home).
  * **Community handbook:** [DataExpert-io / data-engineer-handbook (free, curated)](https://github.com/DataExpert-io/data-engineer-handbook) ✅ — the 2026 community-maintained DE roadmap.
  * **Required Reading:**
    * Kleppmann — *Designing Data-Intensive Applications* — chapters 6–12 for distributed systems, replication, partitioning, consistency.
    * Reis & Housley — [*Fundamentals of Data Engineering*](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ✅ — the full data-engineering lifecycle.
    * *Mining of Massive Datasets* (3e, [free online](http://www.mmds.org/)) — Leskovec, Rajaraman, Ullman — chapters 2–7.
    * [*Streaming Systems*](https://www.oreilly.com/library/view/streaming-systems/9781491983867/) — Akidau, Chernyak, Lax (O'Reilly 2018).
  * **Blogs / Newsletters:** [Joe Reis Substack](https://joereis.substack.com/) ✅, [Kimball Group Tips](https://www.kimballgroup.com/) ✅, [High-Scalability](http://highscalability.com/).
  * **Practical Implementation:** **Apache Spark 3.5+** via **PySpark**, **Apache Iceberg** or **Delta Lake** on Parquet, **Apache Airflow 2.x / 3.0-preview**, **Apache Kafka 3.8+** (local via `kraft` mode), **DuckDB** as your single-node Spark stand-in for learning.

* **📋 Mandatory mini-projects:**
  1. **Build a mini lakehouse** on DuckDB + Parquet + Iceberg on your laptop; write `MERGE INTO` upserts; inspect snapshots and time-travel.
  2. **Airflow DAG** that ingests an open API (e.g., NYC Taxi) → stores Parquet on S3/minio → transforms via dbt → serves to a Streamlit dashboard.
  3. **Kafka + Flink** streaming word-count over a simulated tweet stream; exercise watermarks and late data.
  4. **Spark vs Polars vs DuckDB benchmark** on a 10-GB Parquet dataset — measure wall-clock, peak RAM, and lines-of-code.

---

# 🟧 CLASSICAL MACHINE LEARNING STRATUM (Modules 9–12)

<img src="assets/stratum-3-classical-ml.jpg" alt="Classical machine learning stratum, modules 9 to 12" width="100%">

> This stratum is the intersection of every university's "first ML course" — MIT 6.390, Harvard CS 1810, Cambridge MLRD/MLBI, IITM BSCS2004/2007/2008.

---

<a id="module-9"></a>
## Module 9: Supervised Learning — Regression Family

* **The Tutor's "Why":** Linear regression is the universal first ML algorithm because it teaches you optimisation, loss functions, regularisation, and statistical inference all at once. The **Gauss-Markov theorem** appears in every single one of our four universities.

* **Strict Prerequisites:** Modules 3 (projections, SVD), 5 (Normal/Student-t), 6 (hypothesis tests for coefficients).

* **Exhaustive Topic List:**
  * **[MIT 6.390 · Lec 1 (Spring 2026): "Intro to ML and Linear Regression"]**: Framing ML problems (problem class, assumptions, evaluation), baselines, **generalisation (train vs test)**, the ERM principle.
  * **[MIT 6.390 · Lec 2: "Regression & Regularization"]**: Ordinary Least Squares (OLS), closed-form normal equations β̂ = (XᵀX)⁻¹Xᵀy, geometric interpretation as projection onto column space of X, **Ridge Regression** (L2 regularisation, closed form, ties to Tikhonov regularisation), **Lasso** (L1 regularisation, sparsity, coordinate descent solver), **Elastic Net**.
  * **[MIT 6.390 · Lec 3: "Gradient Descent"]**: Batch GD, SGD, mini-batch SGD, step-size selection, momentum, Nesterov accelerated gradient, convergence analysis for convex quadratic functions.
  * **[Harvard CS109A · Lec 3 "kNN and Linear Regression"]**: **k-Nearest Neighbours regression** (no training, lazy learning, curse of dimensionality), simple linear regression derivation.
  * **[Harvard CS109A · Lec 4 "Multi-linear and Polynomial Regression"]**: Multiple predictors, design matrix, interaction terms, basis expansions (polynomial, piecewise constant, cubic splines, natural cubic splines, smoothing splines).
  * **[Harvard CS109A · Lec 5 "Model Selection and Cross Validation"]**: Validation set, **K-fold cross-validation** (standard, stratified, LOOCV, time-series CV with `TimeSeriesSplit`), **information criteria** (AIC, BIC, Mallow's Cp, adjusted R²), **bias-variance decomposition** (formal proof).
  * **[Harvard CS109A · Lec 6 "Regularization: Ridge and Lasso"]**: Coefficient paths, hyperparameter search (grid, random, Bayesian optimisation with Optuna), early stopping as implicit regularisation.
  * **[Harvard CS109A · Advanced Section 4 "GLMs"]**: **Generalised Linear Models** — exponential family (canonical form, natural parameter, log-partition function, dispersion), link functions (identity, log, logit, probit, complementary log-log), IRLS algorithm (covered in Cambridge ML&BI).
  * **[IITM BSCS2008 Week 3-4]**: Linear regression in scikit-learn; **gradient descent — batch vs stochastic**; polynomial regression pipeline; regularised linear models.
  * **[Cambridge Data Science · "Feature spaces"]**: Linear models as projection onto span of features; design of features.
  * **[Cambridge ML & Bayesian Inference · "Gaussian processes"]** (2 lectures): **Regression via Gaussian processes**, kernel functions (squared exponential, Matérn, periodic), marginal likelihood for hyperparameter learning, **preview of non-parametric Bayesian regression**.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 6.390 Spring 2026](https://introml.mit.edu/spring26/lectures/lec01) · [Harvard CS109A 2021 Lec 3-6](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html).
  * **Required Reading (Latest 2026 Editions):**
    * _An Introduction to Statistical Learning with Python_ (ISLP) — Chapters 3, 5, 6.
    * _The Elements of Statistical Learning_ (ESL, 2nd Ed corrected 12th printing) — Chapters 3, 5.
    * _Pattern Recognition and Machine Learning_ (Bishop, 2006) — Chapter 3.
  * **Practical Implementation:** **scikit-learn 1.5+** (`LinearRegression`, `Ridge`, `Lasso`, `ElasticNet`, `KNeighborsRegressor`, `GaussianProcessRegressor`), **statsmodels** for inferential output, **`torch.optim.SGD` / `torch.optim.AdamW`** once you graduate to M15.

* **📦 Module Project (mandatory) — Linear regression from scratch, then honestly evaluated**
  * **Deliverable:** `LinearRegressionScratch` in pure NumPy — closed-form normal equations *and* gradient descent — plus your own Ridge and Lasso (the latter via coordinate descent or ISTA). Compare against `sklearn` on a real regression dataset with a proper train/validation/test split and a regularisation path plot.
  * **Definition of done:** (1) `pytest` suite asserting your coefficients match `sklearn`'s to within tolerance on a fixed-seed synthetic problem where you know the true weights; (2) `README.md` with the regularisation path, residual diagnostics, and a statement of which assumptions your data violates; (3) a results memo explaining what Lasso zeroed out and whether that matches domain sense.
  * **Stretch:** Add a bootstrap confidence interval for each coefficient using your [M6](#module-6) toolkit and discuss which coefficients you would actually report.
  * *This is the first rung of the from-scratch discipline described in [Stage 4 of the fast lane](#practitioner-track). Video 1 (05:40) is explicit that implementing the algorithm is what converts a course-watcher into someone who can debug a model.*

---

<a id="module-10"></a>
## Module 10: Supervised Learning — Classification & Kernel Methods

* **The Tutor's "Why":** Classification is supervised learning in its most deployed form — spam filters, credit scoring, disease diagnosis. Support Vector Machines are mandatory at every university because their **dual formulation + kernel trick** is the purest expression of convex optimisation meeting functional analysis.

* **Strict Prerequisites:** Module 9, plus Lagrange multipliers (M2) and quadratic forms (M3).

* **Exhaustive Topic List:**
  * **[MIT 6.390 · Lec 4 (S26): "Logistic Regression"]**: Sigmoid function σ(z) = 1/(1+e⁻ᶻ), log-odds/logit, **cross-entropy loss** (NLL of Bernoulli), gradient (no closed form), decision boundary (linear), multiclass softmax with categorical cross-entropy, one-vs-rest vs multinomial, class imbalance (oversampling, undersampling, SMOTE, class weights, focal loss).
  * **[MIT 6.86x · Unit 1 Lec 2-4]**: **Perceptron algorithm** (Rosenblatt 1958) — update rule, mistake bound (Novikoff's theorem, proof), linear separability, **Hinge loss and margin boundaries**, regularisation.
  * **[MIT 6.86x · Unit 2 Lec 6 "Nonlinear Classification"]**: Feature transformations, **kernel trick** motivation.
  * **[Harvard CS109A · Lec 14-15 "Logistic Regression 1 & 2"]**: MLE estimation, Newton-Raphson / IRLS, Wald CIs for odds ratios, ROC curves, AUC, precision/recall/F1/F2, confusion matrix, calibration (Platt scaling, isotonic regression), threshold selection.
  * **[Harvard CS 1810 (S26)]**: **Support Vector Machines (SVMs)** — maximum-margin hyperplane derivation, hard-margin primal problem, soft-margin with slack variables ξᵢ, **Lagrangian dual formulation**, KKT conditions, support vectors, **kernel trick** (Mercer's theorem), standard kernels (linear, polynomial, RBF/Gaussian, sigmoid), kernel construction rules, string kernels, graph kernels.
  * **[Cambridge ML & Bayesian Inference · Lec "Linear classifiers I" (2 lectures)]**: Supervised learning via **error minimisation**, **Iterative Reweighted Least Squares (IRLS)** with full derivation, **maximum margin classifier** geometric derivation.
  * **[Cambridge ML & Bayesian Inference · Lec "Support vector machines (SVMs)" (2 lectures)]**: The kernel trick formalised, problem formulation as QP, **constrained optimisation and the dual problem**, SVM training algorithm (SMO — Sequential Minimal Optimisation), ν-SVM, one-class SVM for anomaly detection.
  * **[Cambridge ML & Bayesian Inference · Lec "How to classify optimally" (2 lectures)]**: Treating learning probabilistically — **Bayesian decision theory**, **Bayes-optimal classifier**, likelihood functions and priors, Bayes' theorem applied to supervised learning, **Maximum Likelihood vs Maximum a Posteriori hypotheses** (with proof of equivalence in flat-prior case), reinterpretation of backprop as MLE with squared-error or cross-entropy loss.
  * **[Cambridge ML & Real-World Data · Topic 1 "Statistical Classification" (7 sessions)]**: **Naive Bayes** parameter estimation with Laplace smoothing, statistical laws of language (Zipf's, Heaps'), **statistical tests for classification tasks** (McNemar's test for paired classifier comparison), **cross-validation and test sets**, uncertainty and human agreement (Cohen's κ, Fleiss' κ).
  * **[IITM BSCS2008 · Week 5-8]**: Logistic regression in scikit-learn; binary vs multiclass classification via one-vs-rest and softmax; **SVMs** with scikit-learn (`SVC`, `LinearSVC`); kernel selection in practice.
  * **[MIT 6.86x · Unit 1 Lec 4 "Linear Classification and Generalization"]**: VC dimension informal, PAC learning introduction.
  * **[Harvard CS 1810]**: **Linear Discriminant Analysis (LDA)** — generative classifier, equal class covariance assumption, **Quadratic Discriminant Analysis (QDA)**, Gaussian Naive Bayes as diagonal-covariance QDA.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 6.390 S26 Lec 4](https://introml.mit.edu/spring26/lectures/lec04) · [Cambridge ML&BI](https://www.cl.cam.ac.uk/teaching/2526/MLBayInfer/).
  * **Required Reading (Latest 2026 Editions):**
    * _Pattern Recognition and Machine Learning_ — Bishop — Chapters 4, 6, 7.
    * ISLP — Chapters 4, 9.
    * _Learning with Kernels_ — Schölkopf & Smola — deep dive on SVMs.
  * **Practical Implementation:** **scikit-learn** (`LogisticRegression`, `SVC`, `LinearSVC`, `GaussianNB`, `MultinomialNB`, `LinearDiscriminantAnalysis`, `QuadraticDiscriminantAnalysis`); **`libsvm`** directly for research; **`cvxpy`** to hand-code the SVM dual QP for didactic clarity.

* **🎯 Calibration & Reliability:** A classifier that outputs `P(y=1 | x) = 0.9` but is right only 70% of the time is *mis-calibrated* — disastrous for medical, financial, and risk-scoring applications.
  * **Calibration methods:** [**Platt scaling**](https://en.wikipedia.org/wiki/Platt_scaling) (logistic calibration on held-out scores), **isotonic regression** (non-parametric, monotone step-function, better for ≥ 1000 calibration samples), **temperature scaling** (single-parameter scalar on logits; the standard for modern neural networks — Guo et al. ICML 2017), **Beta calibration**, **Dirichlet calibration** (multi-class), **histogram binning**.
  * **Metrics:** **Brier score**, **Expected Calibration Error (ECE)**, **Maximum Calibration Error (MCE)**, **reliability diagrams** (calibration curves), **log-loss** decomposition into refinement + calibration.
  * **Practical:** [`sklearn.calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/calibration.html), [`sklearn.calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html), [`netcal`](https://github.com/EFS-OpenSource/calibration-framework) for DL calibration.
  * **Why it matters for 2026 interviews:** every senior-DS interview asks about calibration before asking about model choice.

* **📦 Module Project (mandatory) — Churn prediction, from-scratch core, deployed dashboard**
  * **Deliverable:** Two halves. **(a)** `LogisticRegressionScratch` in NumPy following the `__init__` / `sigmoid` / `fit` / `predict` structure laid out in [the fast lane](#practitioner-track), verified against `sklearn`. **(b)** A real churn-prediction model on a real customer-churn dataset — feature engineering, class-imbalance handling, threshold selection driven by a stated cost matrix rather than by accuracy — surfaced in a deployed Streamlit dashboard that takes a customer record and returns a churn probability plus the top drivers.
  * **Definition of done:** (1) `pytest` suite over both halves, including a leakage test asserting that no feature derived from the target survives into training; (2) `README.md` with the confusion matrix at your chosen threshold, the cost calculation that justified it, a calibration curve, and a **live URL**; (3) a results memo stating what the model would cost the business if deployed at your threshold and at the naive 0.5 threshold.
  * **Stretch:** Add SHAP explanations to the dashboard and a monitoring hook that logs the input-feature distribution so you could detect drift.
  * *Archetype source: video 1 (13:10) — the churn-prediction dashboard is named there as the canonical portfolio project because it forces business framing, not just model-fitting. The "deployed" requirement is not decoration: **a messy project on the internet beats a perfect project on your laptop.***

---

<a id="module-11"></a>
## Module 11: Unsupervised Learning, Dimensionality Reduction & Mixture Models

* **The Tutor's "Why":** The universe is overwhelmingly unlabelled. Every one of our four universities treats PCA as an eigenvalue problem, K-means as Lloyd's algorithm, and mixture models as the EM-algorithm's canonical application. Harvard CS109B's **very first lecture** is clustering.

* **Strict Prerequisites:** Module 3 (SVD, eigendecomposition), Module 5 (multivariate Gaussian), Module 9 (MLE).

* **Exhaustive Topic List:**
  * **[Harvard CS109A · Lec 10 "Principal Component Analysis"]**: **PCA** derivation three ways — variance maximisation, reconstruction error minimisation, and **SVD of the centred data matrix**; eigenvalue scree plot, Kaiser criterion, parallel analysis; **Advanced Section 3: "Math Foundations of PCA"** — formal proof via Lagrange multipliers; kernel PCA; sparse PCA; probabilistic PCA.
  * **[Harvard CS109B · Lec 1-2 "Clustering 1 & 2"]**: **K-means algorithm** (Lloyd's iteration), random initialisation and **K-means++**, within-cluster sum of squares (WCSS), elbow method, silhouette coefficient, gap statistic, **Hierarchical clustering** (agglomerative — single/complete/average/Ward linkage; divisive), dendrograms, cophenetic correlation coefficient, **DBSCAN** (eps, minPts, core vs border vs noise), OPTICS, HDBSCAN (2026 go-to), Mean-Shift, Spectral clustering (graph Laplacian eigenvectors).
  * **[Harvard CS109B · Advanced Section 1 "Gaussian Mixture Models"]**: **GMM** as probabilistic clustering, responsibilities γₙₖ, **EM algorithm** for GMMs — E-step computes responsibilities, M-step updates μₖ, Σₖ, πₖ; convergence proof via Jensen's inequality; choosing K via BIC; comparison to K-means (K-means as degenerate GMM).
  * **[Cambridge ML & Bayesian Inference · "Unsupervised learning I"]**: **The k-means algorithm** derivation, **clustering as a maximum likelihood problem** (hard vs soft assignments).
  * **[Cambridge ML & Bayesian Inference · "Unsupervised learning II"]**: **The EM algorithm** — general form (E-step = variational lower bound, M-step = maximise over parameters), application to clustering, application to missing-data problems, **connection to variational inference** (preview of M13).
  * **[MIT 6.86x · Unit 4 Lec 13-16]**: Clustering 1 & 2; Generative models; **Mixture Models and EM algorithm**; Project 4 — Collaborative Filtering via Gaussian Mixtures (**matrix factorisation perspective**).
  * **[MIT 6.390 · Lec 8 (S26): "Representation Learning"]**: Modern view of unsupervised learning — **autoencoders as non-linear PCA**, bottleneck layer, tied weights, denoising autoencoders, sparse autoencoders.
  * **[MIT 6.790 · Part II "Unsupervised Learning"]**: Dimensionality reduction (PCA, Kernel PCA, **ISOMAP**, **Locally Linear Embedding**, **t-SNE** with perplexity tuning, **UMAP** with `n_neighbors`/`min_dist`), matrix estimation (low-rank matrix completion — Netflix prize), feature extraction from unstructured text (topic models — LDA).
  * **[IITM BSCS2008 · Week 12]**: Unsupervised learning in scikit-learn.
  * **[MIT 6.7960 · Week 7 "Representation learning — similarity-based"]**: **Metric learning**, contrastive learning (SimCLR, MoCo, CLIP training objective), InfoNCE loss, alignment and uniformity criteria.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109B 2022 Lec 1-2](https://harvard-iacs.github.io/2022-CS109B/) · [MIT 6.86x Unit 4](https://www.edx.org/learn/machine-learning/massachusetts-institute-of-technology-machine-learning-with-python-from-linear-models-to-deep-learning).
  * **Required Reading (Latest 2026 Editions):**
    * ESL — Chapter 14.
    * PRML Bishop — Chapters 9, 12.
    * _Probabilistic Machine Learning: An Introduction_ (Murphy, MIT Press 2022) — chapters 20-21.
  * **Practical Implementation:** **scikit-learn** (`KMeans`, `DBSCAN`, `AgglomerativeClustering`, `GaussianMixture`, `PCA`, `KernelPCA`, `TruncatedSVD`); **`hdbscan`**, **`umap-learn`**, **`openTSNE`**; **`pymc`** for Bayesian GMMs.

* **📦 Module Project (mandatory) — K-Means from scratch + a dimensionality-reduction bake-off**
  * **Deliverable:** `KMeansScratch` in NumPy (random init *and* k-means++ init, with inertia tracking and a proper convergence criterion), plus your own PCA via SVD. Then run a comparison on one high-dimensional real dataset: PCA vs t-SNE vs UMAP for visualisation, and K-Means vs DBSCAN vs GMM for clustering, with a defensible cluster-count selection (elbow **and** silhouette **and** a stability check).
  * **Definition of done:** (1) `pytest` suite asserting your K-Means matches `sklearn`'s inertia on a fixed seed and that your PCA's explained-variance ratios match, plus a test that k-means++ beats random init on average over seeds; (2) `README.md` with the embedding plots side by side and an explicit warning about what t-SNE/UMAP distances do *not* mean; (3) a results memo naming the clusters and stating whether you believe they are real structure or artefacts.
  * **Stretch:** Cluster on the PCA projection vs the raw features and quantify how much the preprocessing choice changed your conclusions.
  * *Archetype source: video 1 (06:05) — K-Means is one of the three algorithms named for from-scratch implementation.*

---

<a id="module-12"></a>
## Module 12: Ensemble Methods, Tree-Based Learning & Boosting

* **The Tutor's "Why":** On tabular data (still the majority of enterprise data in 2026), **gradient-boosted trees (XGBoost/LightGBM/CatBoost) beat deep learning** the overwhelming majority of the time. Harvard CS109A dedicates **four full lectures** to trees/bagging/RF/boosting. You must master this before assuming neural networks are always better.

* **Strict Prerequisites:** Modules 9-10 (have solved classification and regression).

* **Exhaustive Topic List:**
  * **[Harvard CS109A · Lec 16 "Decision Tree"]**: CART algorithm (Breiman 1984); splitting criteria — **Gini impurity**, **entropy / information gain**, variance reduction for regression; tree growth; pre-pruning (max_depth, min_samples_split) vs post-pruning (cost-complexity pruning α-path); handling of categorical variables; missing-value handling (surrogate splits).
  * **[Harvard CS109A · Lec 17 "Bagging"]**: Bootstrap aggregation; variance reduction mechanism; out-of-bag (OOB) error estimate as free cross-validation.
  * **[Harvard CS109A · Lec 18 "Random Forest"]**: Feature subsampling (√p for classification, p/3 for regression), **variable importance measures** (Gini importance, permutation importance, SHAP values — previewed), extremely randomised trees (ExtraTrees).
  * **[Harvard CS109A · Lec 19 "Boosting"]**: **AdaBoost** (weighted training, exponential loss derivation, Friedman-Hastie-Tibshirani statistical view), **Gradient Boosting Machines** (functional gradient descent, learning rate shrinkage, stochastic gradient boosting), **XGBoost** (regularised objective, second-order Taylor expansion of loss, handling missing values, sparse-aware split finding), **LightGBM** (histogram binning, GOSS — Gradient-based One-Side Sampling, EFB — Exclusive Feature Bundling, leaf-wise growth), **CatBoost** (ordered boosting, symmetric trees, native categorical handling).
  * **[Harvard CS109A · Lec 20 "Model Interpretability"]**: **SHAP** (Shapley values from coalitional game theory, TreeSHAP efficient computation), **LIME** (local surrogate models), **Partial Dependence Plots**, **ICE plots**, permutation-based feature importance, **counterfactual explanations**.
  * **[Harvard CS109A · Advanced Section 5 "Stacking & Mixture of Experts"]**: **Stacking** (level-0 base learners + level-1 meta-learner), **blending**, **Mixture of Experts** architecture (gating network + expert networks — preview of modern MoE transformers in M18).
  * **[IITM BSCS2008 · Week 9-10]**: Decision Trees, Ensemble Learning, and Random Forests (two full weeks).
  * **[MIT 6.86x]**: Classification and regression trees covered in homework form.
  * **[Harvard CS 1810]**: "Ensemble methods and boosting" as a named topic in the 2026 syllabus.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109A Lec 16-20](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html).
  * **Required Reading (Latest 2026 Editions):**
    * ISLP — Chapter 8.
    * ESL — Chapter 10 (boosting), 15 (random forests).
    * XGBoost paper (Chen & Guestrin 2016) — mandatory.
    * _Interpretable Machine Learning_ — Christoph Molnar — [free online, 2024 edition](https://christophm.github.io/interpretable-ml-book/).
  * **Practical Implementation:** **scikit-learn** (`DecisionTreeClassifier`, `RandomForestClassifier`, `GradientBoostingClassifier`, `HistGradientBoostingClassifier` — now default, C++-backed), **XGBoost 2.x**, **LightGBM 4.x**, **CatBoost 1.2+**, **`shap` 0.46+**, **`interpret` (Microsoft InterpretML)**, **`dalex`**.

* **📦 Module Project (mandatory) — Decision tree from scratch, then a boosting bake-off**
  * **Deliverable:** `DecisionTreeScratch` in NumPy — Gini and entropy criteria, recursive splitting, depth and min-samples stopping rules, and a `predict` that walks the tree. Then, on one tabular dataset, run a fair comparison of your tree vs `RandomForest` vs `XGBoost` vs `LightGBM` vs `CatBoost` with identical folds and a tuned budget per model.
  * **Definition of done:** (1) `pytest` suite covering a pure-node base case, a single-split dataset whose correct split you can compute by hand, and agreement with `sklearn`'s tree on a fixed-seed problem; (2) `README.md` with a leaderboard table (metric ± CV std, fit time, inference latency) — not just the best score; (3) a results memo answering *"would I ship the best model or the second-best, and why"* using the latency and interpretability columns.
  * **Stretch:** Add a permutation-importance and a SHAP comparison, and explain any disagreement between them.
  * *Archetype source: video 1 (06:05) — decision trees are the third named from-scratch implementation.*

---

# 🟦 PROBABILISTIC & BAYESIAN STRATUM (Modules 13–14)

<img src="assets/stratum-4-bayesian.jpg" alt="Probabilistic and Bayesian stratum, modules 13 to 14" width="100%">

---

<a id="module-13"></a>
## Module 13: Bayesian Inference, Graphical Models & MCMC

* **The Tutor's "Why":** Harvard CS109B allocates **weeks 2-4 (five consecutive Bayes lectures)** to this; MIT 6.790 dedicates Part III entirely to it; Cambridge's ML & Bayesian Inference is named after it; Cambridge MLMI Module 1 states it as a foundational objective. Ignore this module and you will never understand uncertainty quantification, variational autoencoders, or modern Bayesian neural networks.

* **Strict Prerequisites:** Module 5 (conjugate priors, Beta, Gamma, Dirichlet, Multivariate Normal), Module 11 (EM algorithm).

* **Exhaustive Topic List:**
  * **[Harvard CS109B · Lec 3 "Bayes 1"]**: **Philosophical basis of Bayesianism** — subjective probability, Cox's theorem (probability as extension of logic), Dutch book argument. Prior × Likelihood ∝ Posterior. Conjugate prior families (Beta-Binomial, Gamma-Poisson, Normal-Normal, Dirichlet-Multinomial, Normal-Inverse-Gamma, Normal-Inverse-Wishart).
  * **[Harvard CS109B · Lec 4 "Bayes 2"]**: **Posterior predictive distribution**, credible intervals vs confidence intervals (conceptual distinction), marginal likelihood (evidence), Bayes factors for model comparison.
  * **[Harvard CS109B · Lec 5 "Bayes 3"]**: **Hierarchical (multi-level) Bayesian models** — partial pooling, shrinkage, James-Stein estimator, empirical Bayes, Gibbs sampling introduction.
  * **[Harvard CS109B · Lec 6 "Bayes 4"]**: **Markov Chain Monte Carlo (MCMC)** — detailed balance condition, **Metropolis-Hastings algorithm** with proposal distributions and acceptance probability, **Gibbs sampling** (when conditionals are tractable), Hamiltonian Monte Carlo (HMC) preview.
  * **[Harvard CS109B · Lec 7 "Bayes 5"]**: **Variational Inference** — ELBO (Evidence Lower Bound) derivation, mean-field approximation, coordinate ascent VI, **stochastic VI**, normalising flows preview, **reparameterisation trick** (preview of VAEs in M16).
  * **[Harvard CS109B · Advanced Section 2 "Particle Filters / Sequential Monte Carlo"]**: **Sequential Monte Carlo** — bootstrap filter, importance sampling, resampling (systematic, residual, stratified), particle degeneracy, effective sample size, auxiliary particle filter.
  * **[Cambridge ML & Bayesian Inference · Lec "Bayesian networks I" (2 lectures)]**: **Directed graphical models (Bayesian networks)** — representing uncertain knowledge as DAGs, joint distribution factorisation, **conditional independence** (d-separation, Markov blanket), **exact inference** (variable elimination, junction tree algorithm / message passing, belief propagation for trees).
  * **[Cambridge ML & Bayesian Inference · Lec "Bayesian networks II"]**: **Markov Random Fields (undirected graphical models)** — Gibbs distributions, potential functions, Hammersley-Clifford theorem, Ising model, **approximate inference**, **Markov chain Monte Carlo methods** (full MH + Gibbs treatment).
  * **[Cambridge ML & Bayesian Inference · Lec "Linear classifiers II"]**: **The Bayesian approach to neural networks** — Laplace approximation (Gaussian at MAP), Bayesian backpropagation (MacKay), MC dropout as approximate Bayesian inference.
  * **[MIT 6.790 · Part III "Probabilistic Modeling"]**: Incorporating prior knowledge, sampling from complex distributions, Bayes rule as basis of all inference, selecting priors (Gaussian → ridge; Laplace → lasso; Dirichlet-process for non-parametric Bayes), **Gibbs sampling derivation**, **Metropolis-Hastings with full proof of detailed balance**.
  * **[MIT 6.790]**: MCMC listed as "one of the top 10 algorithms of all time" alongside quicksort and FFT.
  * **[Cambridge MLMI Module 1]**: **Maximum-likelihood vs Bayesian inference** — strengths and weaknesses of both; **belief propagation** algorithm.
  * **[Harvard CS 1810 (S26)]**: "Graphical models", "hidden Markov models" (→ M14), "inference methods" as syllabus topics.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109B 2022 schedule](https://harvard-iacs.github.io/2022-CS109B/) (Bayes lectures 3-7) · [Cambridge ML&BI 2025-26](https://www.cl.cam.ac.uk/teaching/2526/MLBayInfer/) · [MIT 6.790 Part III](https://gradml.mit.edu/intro/).
  * **Required Reading (Latest 2026 Editions):**
    * _Probabilistic Machine Learning: Advanced Topics_ (Kevin Murphy, **MIT Press 2023**) — Chapters 1-12 (most current Bayesian treatment).
    * _Bayesian Data Analysis_ (**3rd Edition**) — Gelman, Carlin, Stern, Dunson, Vehtari, Rubin (BDA3).
    * _Pattern Recognition and Machine Learning_ — Bishop — Chapters 8 (graphical models), 10 (VI), 11 (MCMC).
    * _Bayesian Reasoning and Machine Learning_ — David Barber — [free PDF](http://www.cs.ucl.ac.uk/staff/D.Barber/brml/) (explicitly listed in Cambridge ML&BI reading list).
  * **Practical Implementation:** **PyMC 5.x** (with PyTensor backend), **NumPyro 0.15+** (JAX-native, 10-100× faster for complex models, standard in 2026 research), **Stan** via `cmdstanpy`, **TensorFlow Probability 0.24+**, **`arviz`** for posterior diagnostics (R̂, ESS, trace plots, posterior predictive checks).

* **📦 Module Project (mandatory) — Bayesian A/B test, end to end**
  * **Deliverable:** A full Bayesian analysis of a real or realistically-simulated experiment in PyMC or NumPyro: state the prior and defend it, fit the posterior, run convergence diagnostics (R-hat, ESS, divergences, trace and rank plots), do prior and posterior predictive checks, and report a decision — including the probability that B beats A by more than a stated business-relevant margin.
  * **Definition of done:** (1) A test asserting R-hat < 1.01 and zero divergences at a fixed seed, so a regression in the model breaks CI; (2) `README.md` with the posterior plots, the prior-sensitivity analysis (re-run under at least two other defensible priors), and the decision rule; (3) a results memo contrasting your Bayesian conclusion with the frequentist p-value from your [M6](#module-6) toolkit on the same data — and explaining precisely what each one does and does not claim.
  * **Stretch:** Extend to a hierarchical model across segments and show partial pooling shrinking the noisy small-segment estimates.
  * **Fast-lane note:** This module is where the [intuition-first shortcut runs out](#module-5). If you are here, you need the probability spine.

---

<a id="module-14"></a>
## Module 14: Sequence Modelling — HMMs, Kalman Filters & Time Series

* **The Tutor's "Why":** Time is the most important axis in the real world. Cambridge ML & Real-World Data dedicates **Topic 2 (4 sessions) entirely** to HMMs with a biological application. MIT MicroMasters C4 is a whole course on time series with interventions. The state-space model framework unifies HMMs, Kalman filters, and particle filters.

* **Strict Prerequisites:** Module 5 (Markov chains — Stat 110 Lec 31-33), Module 13 (message passing).

* **Exhaustive Topic List:**
  * **[Cambridge ML & Real-World Data · Topic 2 "Sequence Analysis" (4 sessions)]**: **Hidden Markov Models (HMM)** — model definition (hidden state chain + observation emissions), assumptions (Markov property on hidden chain, observation independence given state), the three canonical problems (Rabiner 1989):
    1. **Evaluation** — P(observations | model) via **Forward algorithm**.
    2. **Decoding** — most likely hidden sequence via **Viterbi algorithm** (with full dynamic-programming derivation).
    3. **Learning** — parameter estimation via **Baum-Welch / Forward-Backward** (EM for HMMs).
    * Application: **predicting protein interactions with a cell membrane** (Cambridge's specific biological application).
  * **[Harvard CS 1810 (S26)]**: **Hidden Markov Models** as a named 2026 syllabus topic.
  * **[MIT 6.431x]**: Bernoulli process, Poisson process, **hidden random processes** (preview of state-space models).
  * **[Cambridge MLMI 1]**: **Kalman filter** implementation — state-space model for linear Gaussian systems, prediction step and update step, Rauch-Tung-Striebel smoother, **extended Kalman filter (EKF)** for nonlinear systems, **unscented Kalman filter (UKF)**, connection to Bayesian belief update.
  * **[MIT MicroMasters 14.310x / "Data Analysis: Learning Time Series with Interventions"]**: Time series basics — trend, seasonality, cyclicity, stationarity (strong vs weak/covariance stationarity), ACF/PACF, white noise tests (Ljung-Box); ARMA models; **ARIMA** and **SARIMA** (Box-Jenkins methodology); Vector Autoregression (VAR); Granger causality; cointegration and Engle-Granger two-step; **ARCH/GARCH** for volatility; state-space formulation; Kalman filter as linear-Gaussian HMM; structural time-series models (Harvey BSM); **prophet** (Facebook's decomposable model); **DeepAR**, **Temporal Fusion Transformers** (modern 2026 approach); **intervention analysis** (difference-in-differences, interrupted time series, synthetic control); regression discontinuity; instrumental variables for causal inference.
  * **[Harvard CS109B · Lec 17 "Recurrent Neural Networks"]**: **RNN for sequence modelling** (connects to M15).
  * **[Harvard CS109B · Lec 18 "NLP 1 — GRUs / LSTMs"]**: **Long Short-Term Memory (LSTM)** — gate equations (input, forget, output gates), cell state, vanishing gradient solution; **Gated Recurrent Unit (GRU)** — update and reset gates.

* **2026 Resources:**
  * **Primary Course Link:** [Cambridge ML & Real-World Data](https://www.cl.cam.ac.uk/teaching/2324/MLRD/) · [MITx 14.310x](https://micromasters.mit.edu/ds/).
  * **Required Reading (Latest 2026 Editions):**
    * _Forecasting: Principles and Practice_ (**3rd Edition**) — Rob Hyndman — [free online](https://otexts.com/fpp3/).
    * _Time Series Analysis_ — James Hamilton — classical econometric reference.
    * Rabiner, "A Tutorial on Hidden Markov Models" (IEEE 1989) — mandatory historical reading.
    * Bishop PRML — Chapter 13 (sequential data).
  * **Practical Implementation:** **`statsmodels.tsa`** (ARIMA, SARIMAX, VAR, state-space), **`pmdarima`** (auto-ARIMA), **`prophet` 1.1+**, **`hmmlearn`**, **`pykalman`**, **`filterpy`** for Kalman variants, **`darts`** (Unit8's unified TS library — 2026 favourite), **`sktime` 0.30+**, **`neuralforecast`** (Nixtla) for modern deep TS.

* **📦 Module Project (mandatory) — Stock dashboard with honest forecasting**
  * **Deliverable:** A deployed dashboard over a real time series (equities, energy demand, or web traffic) that shows the history, a forecast with prediction intervals, and — critically — a **backtest** using rolling-origin cross-validation. Baselines are mandatory: naive, seasonal-naive, and ARIMA must all appear before any fancy model does.
  * **Definition of done:** (1) `pytest` suite including a test that asserts your backtest split never leaks future data into the past (the single most common bug in time-series code); (2) `README.md` with a metric table across horizons for every model including the naive baselines, and a live URL; (3) a results memo stating plainly whether your model beat seasonal-naive, and if not, saying so.
  * **Stretch:** Add a probabilistic model (or a foundation forecasting model) and compare interval coverage, not just point error.
  * *Archetype source: video 1 (13:55) — the stock dashboard, with the backtest and baseline requirements added because the archetype is otherwise the easiest portfolio project to fake.*

---

# 🟪 DEEP LEARNING STRATUM (Modules 15–17)

<img src="assets/stratum-5-deep-learning.jpg" alt="Deep learning stratum, modules 15 to 17" width="100%">

---

<a id="module-15"></a>
## Module 15: Deep Learning Foundations — MLPs, CNNs, Backprop

* **The Tutor's "Why":** The deep-learning revolution (2012-present) defines modern AI. Harvard CS109B allocates **four full lectures (8-11) to neural network fundamentals**; MIT 6.3900 Spring 2026 spends **three lectures (5, 6, 7) on NNs and CNNs**; MIT 6.7960 is an entire course. Master the mathematics before touching a GPU.

* **Strict Prerequisites:** Module 2 (chain rule), Module 3 (matrix calculus), Module 9 (SGD), Module 10 (logistic regression, cross-entropy loss).

* **Exhaustive Topic List:**
  * **[Harvard CS109B · Lec 8 "Neural Networks 1 (MLP)"]**: Biological motivation vs artificial neuron (McCulloch-Pitts, perceptron), **Multi-Layer Perceptron (MLP)** architecture — affine transformation + activation function; **universal approximation theorem** (Cybenko 1989, Hornik 1991, with proof sketch).
  * **[Harvard CS109B · Lec 9 "NN 2 — Gradient Descent, SGD, BackProp"]**: **Backpropagation algorithm** — full derivation via chain rule as dynamic programming over the computation graph; vanishing/exploding gradients; **Xavier/Glorot initialisation**, **He initialisation** (theoretical justification for each).
  * **[Harvard CS109B · Lec 10 "NN 3 (Optimizers)"]**: **Momentum**, **Nesterov momentum**, **AdaGrad**, **RMSProp**, **Adam**, **AdamW** (decoupled weight decay — 2017 fix), **LAMB** (for large-batch), **Lion** (2023, Chesterton), **Sophia** (2023), learning-rate schedules (step decay, exponential, cosine annealing, warmup, one-cycle), gradient clipping.
  * **[Harvard CS109B · Lec 11 "NN 4 (Regularization)"]**: **L1/L2 weight decay**, **Dropout** (Hinton 2014 — inverted dropout, concrete dropout), **Batch Normalisation** (Ioffe-Szegedy 2015 — full derivation, internal covariate shift debate, post-hoc explanations), **Layer Normalisation**, **Group Normalisation**, **Instance Normalisation**, **RMSNorm** (2026 standard in LLMs), **early stopping**, **data augmentation**, **label smoothing**, **mixup**, **cutmix**.
  * **[Harvard CS109B · Lec 12 "CNNs 1 (Basics)"]**: **Convolutional Neural Networks** — convolution operation (discrete 2D), **kernels as learnable filters**, stride, padding (valid, same, full), pooling (max, average, global), translation equivariance vs invariance; classic architectures: **LeNet-5**, **AlexNet**, **VGG-16/19**, **GoogLeNet/Inception** (1×1 convolutions for dimensionality reduction).
  * **[Harvard CS109B · Lec 13 "CNNs 2 (Regularization)"]**: Data augmentation for vision, dropout in CNNs, batch-norm placement debate.
  * **[Harvard CS109B · Lec 14 "CNNs 3 (Receptive Field)"]**: **Effective receptive field** calculation, dilated/atrous convolutions, **ResNet** (residual connections — identity mapping, full derivation of gradient flow improvement), **DenseNet**, **SqueezeNet**, **MobileNet** (depthwise-separable convolution), **EfficientNet** (compound scaling), **ConvNeXt** (2022 — CNN catches up to ViT).
  * **[Harvard CS109B · Lec 15 "CNNs 4 (Saliency Maps)"]**: Gradient-based saliency, **Grad-CAM** (Selvaraju 2017), integrated gradients, **SmoothGrad**, adversarial examples (FGSM, PGD, Carlini-Wagner).
  * **[Harvard CS109B · Advanced Section 3 "Solvers"]**: Second-order methods, L-BFGS, natural gradient, K-FAC.
  * **[Harvard CS109B · Advanced Section 4 "Segmentation"]**: **Semantic segmentation** (FCN, U-Net, DeepLab); **instance segmentation** (Mask R-CNN); **panoptic segmentation**.
  * **[Harvard CS109B · Advanced Section 5 "SOTA & Transfer Learning"]**: ImageNet pretraining, **fine-tuning** vs **linear probing** vs **LoRA** (→ M18), feature extraction.
  * **[Harvard CS109B · Advanced Section 6 "Autoencoders"]**: Vanilla AEs, denoising AEs, contractive AEs (Jacobian penalty), sparse AEs (KL penalty on activations).
  * **[MIT 6.390 · Lec 5-6-7 (Spring 2026)]**: "Features & Neural Networks I", "Neural Networks II", "Convolutional Neural Networks" — with extensive labs.
  * **[MIT 6.7960 · Fall 2025, Week 1-3 (Beery · He · Khattab)]**: Course overview (Beery); **How to train a neural net** (Beery — SGD, backprop, autodiff, differentiable programming); **Approximation theory** (Khattab — universal approximation, **Barron's theorem**, depth separation); **Architectures: Grids** (Beery — CNNs in depth); **Architectures: Memory and Sequence Modeling** (He — RNNs, LSTMs, sequence models); **PyTorch Tutorial** sessions with Jamie Meindl and Sharut Gupta. Reading: *Foundations of Computer Vision* chapters on neural nets, gradient descent, backprop, CNNs (all [visionbook.mit.edu](https://visionbook.mit.edu/)).
  * **[MIT 6.7960 · Fall 2025, Week 4]**: **Architectures: Transformers** (Beery — tokens + attention + positional codes; Transformers unify MLPs, GNNs, CNNs); **Generalization Theory** (Khattab — PAC, overparameterisation, **double descent**, inadequacy of VC dimension, inductive biases; readings include arXiv 1611.03530, 2503.02113, 2310.00865).
  * **[IITM BSCS3002 — Deep Learning]**: IITM's dedicated Deep Learning course covers the above plus practical engineering on **PyTorch**.
  * **[IITM BSCS2008 · Week 11]**: Neural networks in scikit-learn (MLP introduction).
  * **[Harvard CS 1810]**: Neural networks as a syllabus topic.
  * **[MIT 6.S191 bootcamp]**: Condensed practical treatment.

* **2026 Resources:**
  * **Primary Course Link:** [**MIT 6.7960 Fall 2025 live schedule**](https://deeplearning6-7960.github.io/) (15 weeks · Beery · He · Khattab) · [MIT 6.390 Spring 2026 calendar](https://introml.mit.edu/spring26/calendar) · [**MIT 6.S191 (2026 edition, Amini)**](https://introtodeeplearning.com/) · [Harvard CS109B 2022 (latest public)](https://harvard-iacs.github.io/2022-CS109B/).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * **_Deep Learning: Foundations and Concepts_** — Bishop & Bishop (**Springer 2024**, free online [bishopbook.com](https://bishopbook.com/)) — **primary text** for this module.
    * _Understanding Deep Learning_ — Simon Prince (MIT Press 2024; free online [udlbook.github.io](https://udlbook.github.io/udlbook/)) — chapters 1‑12.
    * _Dive into Deep Learning_ — Zhang, Lipton, Li, Smola — [d2l.ai](https://d2l.ai/) — PyTorch + JAX parallel implementations, continuously updated.
    * _Foundations of Computer Vision_ — Torralba, Isola, Freeman (**MIT Press 2024**, free online at [visionbook.mit.edu](https://visionbook.mit.edu/)) — the official MIT 6.7960 textbook.
    * *Hands‑On Machine Learning with Scikit‑Learn and PyTorch* — Géron (O'Reilly Oct‑Dec 2025).
    * _Deep Learning_ — Goodfellow, Bengio, Courville (2016, still relevant as historical reference).
  * **Practical Implementation:** **PyTorch 2.11.0** (`torch.compile`, FSDP2, CUDA 13, `torch.func.grad`, `torch.distributed.tensor`), **JAX 0.10.0** with **Flax 0.10+** / **NNX** / **Equinox** for functional DL, **Hugging Face Accelerate** for distributed training, **Weights & Biases** or **MLflow 3.11+** for experiment tracking, **Lightning 2.4+** for training‑loop abstraction.

* **🚀 Deep Learning Systems — Training at Scale:** Modern DL is as much a *systems* discipline as an algorithms discipline. Stanford CS336 dedicates weeks to it.
  * **JAX alongside PyTorch:** [JAX docs](https://docs.jax.dev/) ✅, [Flax NNX](https://flax.readthedocs.io/) ✅ — mainstream at Google, DeepMind, Anthropic. Learn `jit`, `vmap`, `pmap`, `scan`, `shard_map`, `jax.Array` with sharding, and the [tour of JAX tutorials](https://docs.jax.dev/en/latest/tutorials.html).
  * **Mixed-Precision Training:** `torch.amp`, `bfloat16` vs `fp16` vs `fp8` (H100/B200), loss-scaling, stochastic rounding; **why bf16 is the 2026 default** (no loss-scaling needed, wider dynamic range).
  * **Gradient Checkpointing:** Trade compute for memory; `torch.utils.checkpoint`, `jax.checkpoint` — required for any model that doesn't fit in GPU RAM.
  * **Fully-Sharded Data Parallel (FSDP / FSDP2):** [PyTorch FSDP API docs](https://docs.pytorch.org/docs/stable/fsdp.html) ✅ + [Getting-Started-with-FSDP2 tutorial](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) ✅. Shard parameters, gradients, and optimiser states across GPUs — the 2026 default for any model > 7B.
  * **Distributed primitives:** DDP, FSDP/FSDP2, Tensor-Parallel (Megatron-style), Pipeline-Parallel (GPipe, PipeDream), **3D parallelism** (DP × TP × PP), ZeRO-1/2/3 (DeepSpeed).
  * **Throughput engineering:** [Triton](https://github.com/triton-lang/triton) ✅ kernels, **FlashAttention-2 / 3** (Tri Dao), **PagedAttention** (vLLM), activation recomputation strategies, `torch.compile` with `fullgraph=True`.
  * **Reading:** [*How to Scale Your Model* (Google JAX scaling book, 2024)](https://jax-ml.github.io/scaling-book/) ✅, [PyTorch DTensor docs](https://pytorch.org/docs/stable/distributed.tensor.html), Stanford CS336 Lectures 5-7 (scaling, parallelism, systems).

* **📦 Module Project (mandatory) — Backprop from scratch, then a real CNN**
  * **Deliverable:** Two halves. **(a)** A NumPy-only MLP with manual forward and backward passes for at least Linear, ReLU, and Softmax-CE layers, trained on MNIST to >97 % test accuracy. **(b)** The same task in PyTorch, then a CNN on CIFAR-10 with augmentation, LR scheduling, and a training loop you wrote yourself.
  * **Definition of done:** (1) A gradient-check test comparing every analytic backward pass against finite differences to `1e-5` — non-negotiable; plus a smoke test that the model can overfit a 10-sample batch to near-zero loss (the fastest way to detect a broken training loop); (2) `README.md` with loss/accuracy curves for train and validation, and a confusion matrix; (3) a results memo describing one bug you hit in the backward pass and how the gradient check found it.
  * **Stretch:** Add mixed-precision training and report the throughput and memory difference.
  * **Anti-goal:** Do not start from a tutorial's training loop. The point of the module is that you can write one.

---

<a id="module-16"></a>
## Module 16: Representation Learning, Transformers & Generative Models

* **The Tutor's "Why":** The Transformer (Vaswani et al. 2017, *Attention is All You Need*) is **the** defining architecture of 2026. MIT 6.390 Spring 2026 dedicates Lecture 9 entirely to it. Every frontier lab, from OpenAI to DeepMind to Anthropic, builds on transformers + diffusion. This module is the ticket to research-grade work.

* **Strict Prerequisites:** Module 15 (backprop, CNNs, RNNs, attention preview).

* **Exhaustive Topic List:**
  * **[Harvard CS109B · Lec 16 "Intro to Language Models"]**: n-gram language models, perplexity, statistical LM vs neural LM.
  * **[Harvard CS109B · Lec 17 "Recurrent Neural Networks"]**: RNN forward/backward through time, bidirectional RNNs.
  * **[Harvard CS109B · Lec 18 "NLP 1 (GRUs/LSTMs)"]**: LSTM full derivation, GRU comparison, vanishing-gradient resolution.
  * **[Harvard CS109B · Lec 19 "NLP 2 (ELMo)"]**: Contextual word embeddings, character-level convolutions, bidirectional LM.
  * **[Harvard CS109B · Advanced Section 7 "Word2Vec"]**: **Skip-gram**, **CBOW**, negative sampling, hierarchical softmax, GloVe (global co-occurrence), FastText (subword embeddings).
  * **[Harvard CS109B · Lec 20 "NLP 3 (Seq2Seq & Attention)"]**: **Encoder-decoder architecture**, **Bahdanau attention** (additive), **Luong attention** (multiplicative), content-based vs location-based attention.
  * **[Harvard CS109B · Lec 21 "NLP 4 (Transformers)"]**: **The Transformer** — Vaswani et al. 2017 in full. Scaled dot-product attention (Q, K, V), **multi-head attention**, **positional encoding** (sinusoidal, learned, rotary RoPE, ALiBi, YaRN), encoder stack, decoder stack with masked self-attention, layer norm placement (pre-LN vs post-LN — 2020 pre-LN victory), feed-forward network (GELU → SwiGLU), residual connections.
  * **[Harvard CS109B · Advanced Section 8 "BERT"]**: **BERT** (bidirectional encoder, masked language modelling, next-sentence prediction), **RoBERTa**, **ALBERT**, **DistilBERT**, **ELECTRA** (replaced token detection), **DeBERTa** (disentangled attention).
  * **[MIT 6.390 · Lec 9 (Spring 2026) "Transformers"]**: Dedicated lecture on transformer architecture.
  * **[MIT 6.7960 · Fall 2025 Week 4 "Architectures: Transformers" (Beery)]**: Three key ideas — **tokens, attention, positional codes**; Transformers as unified framework (subsuming MLPs, GNNs, CNNs); reading = *visionbook.mit.edu/transformers*.
  * **[MIT 6.7960 · Fall 2025 Weeks 5‑7 "Representation Learning" (He, Khattab)]**: **Reconstruction‑based** (autoencoders, VQ-VAE, MAE — Masked Autoencoders); **Similarity‑based / Neural Information Retrieval** — information retrieval, contrastive learning (InfoNCE, hard negatives, KL distillation), sub‑linear search & scaling trade‑offs (cross‑encoders, bi‑encoders, **late interaction / ColBERT**); **Representation Learning and Information Theory** — NN‑GP correspondence, NTK — Neural Tangent Kernel.
  * **[MIT 6.7960 · Fall 2025 Weeks 6‑9 "Foundation Models" (Khattab, He)]**: **Pre‑training** (causal LM loss, SmolLM3, OLMo 2, Marin 8B); **Scaling laws** (Kaplan 2020 + Chinchilla 2022 + Emergent Abilities debate: are emergent abilities a mirage?); **Generative models: basics → VAE & GAN → Diffusion & Flows** (Kaiming He); **Post‑training** (instruction tuning, DPO, GRPO).
  * **[Harvard CS109B · Lec 22-23 "GANs 1 & 2"]**: **Generative Adversarial Networks** — minimax game formulation (Goodfellow 2014), optimal discriminator proof, **mode collapse**, **Wasserstein GAN** (earth-mover distance, Kantorovich-Rubinstein duality), **WGAN-GP** (gradient penalty), **DCGAN**, **Progressive GAN**, **StyleGAN 2/3**, **BigGAN**, **Conditional GAN**, **Pix2Pix**, **CycleGAN** (unpaired translation).
  * **[Harvard CS109B · Advanced Section 9 "More GANs"]**: Evaluation metrics (IS, FID, KID, precision-recall), tricks (spectral normalisation, self-attention GAN — SAGAN).
  * **[MIT 6.7960 · Week 8-9 "Generative models"]**:
    * **Basics** — density models, energy-based models, Langevin samplers, **autoregressive models** (PixelRNN, PixelCNN, MADE, WaveNet), GANs.
    * **Representation-meets-generation** — **VAEs** (Kingma 2013) with full ELBO derivation, **reparameterisation trick** (ε ~ 𝒩(0,I); z = μ + σε), β-VAE for disentanglement, VQ-VAE, NVAE.
    * **Conditional models** — cGAN, cVAE, conditional diffusion, paired image-to-image (Pix2Pix), text-to-image (DALL-E, Imagen, Stable Diffusion, Midjourney), image-to-text (captioning).
  * **[MIT 6.7960]**: **Diffusion Models (DDPM)** — forward noising process, reverse denoising process, **score-matching formulation** (Song & Ermon), **variational diffusion** (Ho et al. 2020), classifier-free guidance, **latent diffusion** (Stable Diffusion), **DPM-Solver / DPM-Solver++** (2022 ODE samplers), **Flow Matching** (2023), **Rectified Flow** (2024 — the 2026 SOTA for image/video gen).
  * **[MIT 6.7960 · Week 10-11 "Generalization (OOD) & Transfer Learning"]**: **Adversarial robustness** (FGSM, PGD attacks, certified defences), **distribution shift** (covariate shift, label shift, concept drift), **domain adaptation** (DANN, CORAL, MMD), **foundation models** — fine-tuning, **linear probing**, **knowledge distillation**, **prompting**, **parameter-efficient fine-tuning** (PEFT: adapters, LoRA, QLoRA, IA³, prompt tuning, prefix tuning).
  * **[MIT 6.7960 · Week 11 "Scaling Laws"]**: **Kaplan scaling laws** (2020), **Chinchilla scaling laws** (Hoffmann 2022 — compute-optimal N*D allocation), power-law behaviour, breaking power laws via data pruning, critical batch size.
  * **[IITM BSCS3005 — Computer Vision]**: Image classification, object detection (YOLO v8-v10, DETR), segmentation, video understanding, 3D vision, **NeRF** (Neural Radiance Fields), **3D Gaussian Splatting** (2023 SOTA — 2026 standard for 3D scenes).
  * **[IITM BSCS3004 — LLMs]**: Dedicated course on language modelling (see M18).

* **2026 Resources:**
  * **Primary Course Link:** [**MIT 6.7960 Fall 2025 full schedule**](https://deeplearning6-7960.github.io/) (weeks 4‑11) · [**Stanford CS336 Spring 2026 Lec 3–4**](https://cs336.stanford.edu/) (architectures + MoE) · [Harvard CS109B 2022 Lec 16‑23](https://harvard-iacs.github.io/2022-CS109B/) · [MIT 6.390 S26 Lec 9](https://introml.mit.edu/spring26/lectures/lec09).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * **Bishop & Bishop — *Deep Learning: Foundations and Concepts*** (Springer 2024, free at [bishopbook.com](https://bishopbook.com/)) — chapters on attention and transformers.
    * _Understanding Deep Learning_ — Prince — Chapters 12‑18 (transformers, GANs, VAEs, diffusion).
    * **_Hands‑On Large Language Models_** — Alammar & Grootendorst (O'Reilly, Sep 2024, 428 pp.) — [HandsOnLLM repo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models).
    * Vaswani et al. 2017 ("Attention is All You Need") — **mandatory primary‑source reading**.
    * Ho, Jain, Abbeel 2020 ("DDPM") — for diffusion.
    * Lipman et al. 2023 ("Flow Matching") & Liu et al. 2022 ("Rectified Flow") — 2026 generative SOTA.
    * Radford et al. 2021 ("CLIP") — multi‑modal foundation.
    * _The Little Book of Deep Learning_ — François Fleuret — concise reference.
  * **Practical Implementation:** **Hugging Face Transformers v5.0 / v4.57 LTS**, **Diffusers 0.30+** (image/video), **PEFT 0.14+** (LoRA/QLoRA/DoRA), **xformers** / **FlashAttention‑3**, **bitsandbytes** (4/8‑bit), **`torch.compile`** + **`torch.fullgraph`** (2× speedups), **Triton 3.x** for custom kernels (Stanford CS336 Lec 6).

* **📦 Module Project (mandatory) — Sentiment analyser on a pretrained model, plus a transformer you built**
  * **Deliverable:** Two halves. **(a)** A deployed sentiment (or topic) classifier built on a pretrained Hugging Face model — fine-tuned or used zero-shot, your choice, but you must justify it — with a proper eval set and error analysis. **(b)** A minimal decoder-only transformer written from scratch (tokeniser → embeddings → multi-head self-attention → residual + layer-norm → LM head) trained on a small corpus until it produces recognisable text.
  * **Definition of done:** (1) `pytest` suite including a shape test for every tensor in the attention block and a causal-mask test proving position *t* cannot attend to *t+1*; (2) `README.md` with the classifier's per-class metrics, a confusion matrix, at least ten inspected misclassifications, and a live URL; (3) a results memo on what your from-scratch model's failure modes taught you about the pretrained one.
  * **Stretch:** Compare your fine-tuned classifier against a well-prompted foundation model on the same eval set and report cost, latency, and accuracy — this is the exact trade-off [M21](#module-21) formalises.
  * *Archetype source: video 1 (13:25) — "sentiment analyser on a pretrained Hugging Face model" is named as the accessible NLP portfolio project; the from-scratch half is added so the module still earns its place in the deep-learning stratum.*

---

<a id="module-17"></a>
## Module 17: Reinforcement Learning & Decision Making

* **The Tutor's "Why":** RL drives robotics, game AI, and — most importantly in 2026 — the RLHF alignment of LLMs. MIT 6.390 Spring 2026 Lec 10-11 covers MDPs and RL. IITM runs a dedicated BSCS3003 course. Harvard CS 1810 (2026) lists reinforcement learning as a named syllabus topic.

* **Strict Prerequisites:** Module 5 (Markov chains, expectation), Module 15 (can train a deep network).

* **Exhaustive Topic List:**
  * **[MIT 6.390 · Lec 10 (Spring 2026) "Markov Decision Processes"]**: **MDP formulation** — (S, A, P, R, γ), episodic vs continuing tasks, **Bellman equations** (value iteration, policy iteration), **optimality** (Bellman optimality operator, contraction mapping theorem proof), dynamic programming for MDPs.
  * **[MIT 6.390 · Lec 11 (Spring 2026) "Reinforcement Learning"]**: **Model-free RL** — **Monte Carlo methods** (first-visit, every-visit), **Temporal Difference (TD)** learning, **TD(0)**, TD(λ), SARSA, **Q-learning** (off-policy TD control), **Deep Q-Networks (DQN)** (Mnih et al. 2015 — experience replay, target network, Atari), Double DQN, Dueling DQN, Rainbow DQN.
  * **[MIT 6.790 · Part IV "Decision Making"]**: Optimising under model uncertainty; **explore-vs-exploit tradeoff**; **credit assignment problem**; two key timescales (state dynamics vs information dynamics) → framework table distinguishing optimisation, MDPs, RL.
  * **[MIT 6.86x · Unit 5 Lec 17-19]**: **Reinforcement Learning 1 & 2**; Applications to **Natural Language Processing** (dialogue systems as RL, text summarisation as RL).
  * **[IITM BSCS3003 — Reinforcement Learning]**: Dedicated 12-week course covering:
    * Multi-armed bandits (ε-greedy, UCB, Thompson sampling, contextual bandits — LinUCB, Neural contextual bandits).
    * Policy gradient methods — **REINFORCE** (Williams 1992, log-likelihood trick derivation), **Actor-Critic** (A2C, A3C), **Advantage function**, **GAE** (Generalised Advantage Estimation).
    * **Trust Region methods** — TRPO (Schulman 2015), **PPO** (Schulman 2017 — clipped objective, the RLHF workhorse), **TRPO vs PPO vs ACKTR**.
    * **Deterministic Policy Gradient** (DPG), **DDPG**, **TD3**, **SAC** (Soft Actor-Critic, max-entropy RL).
    * **Model-based RL** — Dyna-Q, **MuZero**, **DreamerV3** (2024), **World models**.
    * **Inverse RL** (IRL), **Imitation Learning** (Behavioural Cloning, DAgger), **GAIL** (Generative Adversarial Imitation Learning).
    * **Offline RL** — BCQ, CQL, IQL, decision transformer.
    * **Hierarchical RL** — options framework, feudal networks, HIRO.
    * **Multi-agent RL** — self-play, fictitious play, MADDPG, AlphaZero, counterfactual regret minimisation.
  * **[MIT 6.7960 · Week 15 "Efficient Policy Optimization Techniques for LLMs"]**: **RLHF challenges**, simplifying RL policy optimisation to **relative reward regression** (DPO — Direct Preference Optimisation, Rafailov 2023), **IPO**, **KTO**, **ORPO**, multi-turn RLHF extensions.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 6.390 Spring 2026 Lec 10-11](https://introml.mit.edu/spring26/) · [David Silver DeepMind RL Course (YouTube, still canonical)](https://www.youtube.com/watch?v=2pWv7GOvuf0) · **[IITM BSCS3003 Reinforcement Learning](https://study.iitm.ac.in/ds/course_pages/BSCS3003.html)**.
  * **Required Reading (Latest 2026 Editions):**
    * _Reinforcement Learning: An Introduction_ (**2nd Edition, 2018, 2024 reprint**) — Sutton & Barto — [free PDF](http://incompleteideas.net/book/the-book-2nd.html) — **the canonical text**.
    * _Algorithms for Decision Making_ — Kochenderfer, Wheeler, Wray (MIT Press 2022) — [free online](https://algorithmsbook.com/).
    * _Foundations of Deep Reinforcement Learning_ — Graesser & Keng — for practitioners.
  * **Practical Implementation:** **Gymnasium** (successor to OpenAI Gym), **Stable-Baselines3 2.x**, **CleanRL** (single-file implementations — best for learning), **RLlib** (Ray, for distributed), **PettingZoo** (multi-agent), **trl** (Hugging Face — for RLHF), **DeepMind Acme**, **PufferLib** (2025, unified wrapper).

* **📦 Module Project (mandatory) — Agent that actually learns**
  * **Deliverable:** Tabular Q-learning implemented from scratch on a discrete environment (Taxi, FrozenLake, or a gridworld you define), then DQN on a continuous-observation environment (CartPole → LunarLander) with a training loop you wrote. Learning curves over at least five seeds, with mean and spread — single-seed RL results are not evidence.
  * **Definition of done:** (1) `pytest` suite covering the Bellman update on a hand-computable 2-state MDP, the replay buffer's sampling and eviction, and epsilon decay; (2) `README.md` with the multi-seed learning curves, the full hyperparameter table, and a recorded episode; (3) a results memo describing one instability you observed (divergence, catastrophic forgetting, reward hacking of your own reward function) and what fixed it.
  * **Stretch:** Re-run one experiment with a shaped reward and document how the agent exploited your shaping — the cheapest possible lesson in [M23](#module-23)'s specification-gaming material.

---

# 🔴 FRONTIER & PRODUCTION STRATUM — Modules 18, 21–26

<img src="assets/stratum-6-production.jpg" alt="Frontier and production AI stratum, modules 18 and 21 to 26" width="100%">

---

<a id="module-18"></a>
## Module 18: Large Language Models, RLHF & Alignment

* **The Tutor's "Why":** This is the defining technology of 2026. IITM has a **dedicated course BSCS3004 on LLMs**; MIT 6.7960 Week 12 and 15 cover LLMs and RLHF explicitly; Harvard's AC215 covers MLOps for models. If you cannot build, fine-tune, and deploy an LLM in 2026, you are not employable as a senior data scientist.

* **Strict Prerequisites:** Modules 16 (transformers), 17 (PPO, DPO).

* **Exhaustive Topic List:**
  * **[IITM BSCS3004 — LLMs]**: Full dedicated course covering:
    * **Tokenisation** — BPE (Byte Pair Encoding), WordPiece, SentencePiece, Unigram LM, **tiktoken** (OpenAI), SuperBPE (2024).
    * **Pre-training** — causal LM, masked LM, prefix LM, next-token-prediction loss at scale.
    * **Architectures** — GPT family (GPT-2, GPT-3, GPT-4, GPT-4o, **GPT-5** 2025), Llama (1/2/3/4), Mistral, Gemma, Qwen, DeepSeek (R1 reasoning model 2025), Claude (Sonnet 4, Opus 4).
    * **Context-length extensions** — RoPE scaling, YaRN, Position Interpolation, LongRope, ring attention, infinite attention.
    * **Efficient attention** — FlashAttention v1/v2/v3, PagedAttention (vLLM), sliding-window, Mixture-of-Experts (MoE — Mixtral, DeepSeek-V3), State-Space Models (Mamba, Mamba-2, Jamba hybrid), linear attention (RWKV, Retentive Networks).
  * **[MIT 6.7960 Week 12 (2024) "Large Language Models" — Jacob Andreas guest lecture]**: **LLM basics**, **prompting**, **In-Context Learning** (zero-shot, few-shot, chain-of-thought — Wei 2022, tree-of-thought, graph-of-thought), **Chain-of-Thought reasoning** ("Let's think step by step", Kojima 2022), **Instruction tuning** (FLAN, T0, InstructGPT), **Self-Consistency**, **Self-Refine**, **Reflexion**.
  * **[MIT 6.7960 Week 15 / RLHF]**: **RLHF pipeline** — SFT → Reward Modelling → PPO; **Reward hacking** and mitigations; **DPO** (Direct Preference Optimisation, Rafailov 2023 — eliminates reward model); **IPO, KTO, ORPO, SimPO, GRPO** (2025); **Constitutional AI** (Anthropic); **RLAIF** (AI feedback); **multi-turn RLHF**.
  * **[MIT 6.3900 / 6.390 Lec_future]**: Frontier topics.
  * **PEFT — parameter-efficient fine-tuning**: **LoRA** (Hu 2021 — low-rank adaptation), **QLoRA** (Dettmers 2023 — 4-bit quantised), **DoRA** (Weight-Decomposed LoRA, 2024), **AdaLoRA**, **IA³**, **prompt tuning**, **prefix tuning**, **P-tuning v2**, **spectrum fine-tuning**.
  * **Quantisation & compression**: Post-training quantisation (PTQ — GPTQ, AWQ, **SmoothQuant**, **SqueezeLLM**), Quantisation-Aware Training (QAT), 1-bit LLMs (BitNet b1.58), pruning (magnitude, structured, Wanda, SparseGPT), knowledge distillation (TinyBERT, DistilLlama).
  * **Retrieval-Augmented Generation (RAG)**: Dense retrievers (DPR, ColBERT v2, BGE, E5, **Voyage-3** 2025), hybrid search (BM25 + dense), vector databases (**pgvector**, **Qdrant**, **Weaviate**, **Milvus**, **LanceDB** 2026), **GraphRAG** (Microsoft 2024), **Agentic RAG**, reranking (Cohere Rerank 3, **Jina Reranker v2**), **HyDE** (Hypothetical Document Embeddings).
  * **Agentic systems**: Tool use / function calling, **ReAct** (Reasoning + Acting), **MCP (Model Context Protocol)** — Anthropic 2024/2025 standard, multi-agent frameworks (**AutoGen** 0.4+, **CrewAI**, **LangGraph**, **OpenAI Swarm/Agents SDK** 2025, **Claude Code**).
  * **Alignment & Safety**: Red-teaming, jailbreaks (AutoDAN, GCG — Universal Transferable Suffixes), **mechanistic interpretability** (Anthropic, Transformer Circuits — induction heads, circuits, **Sparse Autoencoders** for superposition 2024), **activation steering**, **Representation Engineering** (RepE), scalable oversight (debate, recursive reward modelling, weak-to-strong generalisation).
  * **Evaluation**: MMLU, MMLU-Pro, GPQA, MATH, HumanEval, SWE-Bench, ARC-AGI (François Chollet), BIG-Bench Hard, Long-context (RULER, LongBench), **LMSys Arena** (ELO ratings), **Chatbot Arena Hard**, **LiveCodeBench**, **Aider Leaderboard**.
  * **Multi-modality**: Vision-Language Models (LLaVA, GPT-4V, Claude 3.5 Sonnet Vision, **Molmo** 2024, **Pixtral**), audio (Whisper v3, Voice-Mode, **Moshi**), video (Sora, Veo 2, **Runway Gen-3**, **Kling 2.0**).

* **2026 Resources:**
  * **Primary Course Link:** [**Stanford CS336 Spring 2026 “Language Modeling from Scratch”**](https://cs336.stanford.edu/) (Hashimoto · Liang, LIVE 30 Mar 2026 — 17 lectures + 5 assignments covering tokenizer → Transformer → Triton FlashAttention → parallelism → data pipelines → SFT → RLHF/DPO → RLVR) · [CS336 Spring 2025 archive](https://cs336.stanford.edu/spring2025/) + [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) · [IITM BSCS3004](https://onlinedegree.iitm.ac.in/) · [Princeton COS 597 G](https://princeton-nlp.github.io/cos597G/) · [**MIT 6.7960 Fall 2025 Week 8‑9, 11–13**](https://deeplearning6-7960.github.io/) (Foundation Model pre‑/post‑training, scaling laws, inference‑time algorithms) · [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/) (free, certified) · [Hugging Face Smol Training Playbook](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook) (200+ pages of real training secrets, Oct 2025).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * **_Build a Large Language Model (From Scratch)_** — Sebastian Raschka (Manning 2024) — **do this alongside CS336 Assignment 1**.
    * **_Hands‑On Large Language Models_** — Alammar & Grootendorst (O'Reilly Sep 2024, 428 pp., [HandsOnLLM repo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)).
    * **_AI Engineering_** — Chip Huyen (O'Reilly Jan 2025) — the practical engineer's view.
    * **_Speech and Language Processing_ (3rd Edition draft — continually updated through 2026)** — Jurafsky & Martin — [free online](https://web.stanford.edu/~jurafsky/slp3/) (chapters 9‑11 for LLMs, chapter 14 for dialogue).
    * **_Transformers v5_ release notes** — Hugging Face blog ([huggingface.co/blog/transformers-v5](https://huggingface.co/blog/transformers-v5), Dec 2025).
    * **_MCP Specification — 2025‑06‑18 + Nov 2025 anniversary release_** — [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification/2025-06-18).
    * Anthropic Transformer Circuits thread ([transformer-circuits.pub](https://transformer-circuits.pub/)) — mandatory for interpretability.
    * "A Survey of LLMs" (Zhao et al., 2023, updated 2025) — arXiv comprehensive survey.
  * **Practical Implementation:** **Hugging Face `transformers` v5.6+** (April 2026 PyPI), **`datasets` 3.x**, **`accelerate` 1.x**, **`peft` 0.19+** (LoRA/QLoRA/DoRA), **`trl` 1.2+** (SFT, DPO, GRPO, ORPO, KTO, SimPO), **`bitsandbytes` 0.44+**, **`vLLM` 0.19+** (production inference with continuous batching, paged attention, prefix caching), **`SGLang`** (2026 fastest), **`llama.cpp`** + GGUF (CPU inference), **Ollama** / **LM Studio** (local deployment), **LangGraph 1.1+** / **LlamaIndex 0.11+** / **DSPy 3.2+** (2026 prompting frameworks), **`smolagents` 1.24+** + **MCP SDK (Python/TypeScript)** (Anthropic's Nov 2025 standard — used by Claude Desktop, Cursor, VS Code, Zed), **Unsloth** (efficient fine‑tuning, 2× faster), **Marin** / **OLMo 2** / **SmolLM3** open training recipes.

* **🎯 Fine-Tuning Playbook:** Learn the operational trade-offs behind each parameter-efficient fine-tuning method.
  * **When to full-fine-tune vs LoRA vs QLoRA vs DoRA:** cost curves (VRAM, $, wall-clock), quality trade-offs; **LoRA** works for 90% of alignment tasks; **QLoRA** enables 65B on a single 48GB GPU; **DoRA** (Weight-Decomposed LoRA, 2024) closes the full-FT quality gap at LoRA cost.
  * **Frameworks:**
    * [**Unsloth**](https://github.com/unslothai/unsloth) ✅ — 2× faster, 60% less VRAM; drop-in for HF Trainer.
    * [**Axolotl**](https://github.com/axolotl-ai-cloud/axolotl) ✅ — YAML-configured, handles data-prep/packing/sequence-parallel out of the box; the community standard for reproducible open-source fine-tunes.
    * [**TRL**](https://github.com/huggingface/trl) ✅ 1.2+ — SFTTrainer, DPOTrainer, GRPOTrainer, RewardTrainer, ORPOTrainer.
    * [**PEFT**](https://github.com/huggingface/peft) ✅ 0.19+ — LoRA/QLoRA/DoRA/IA³/Prompt Tuning/Prefix Tuning APIs.
  * **Prompt Compilation & DSPy:** [**DSPy**](https://github.com/stanfordnlp/dspy) ✅ 3.2+ — programs-not-prompts, compile signatures with optimisers (BootstrapFewShotWithRandomSearch, MIPROv2, COPRO); [**TextGrad**](https://github.com/zou-group/textgrad) ✅ — differentiate through LLM calls with natural-language gradients.
  * **Inference Optimisation:** [**vLLM 0.19+**](https://docs.vllm.ai/) ✅ (continuous batching, PagedAttention, prefix caching, speculative decoding), [**SGLang**](https://github.com/sgl-project/sglang) ✅ (fastest for structured output and constrained decoding), [**TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM) ✅, **speculative decoding** (Medusa, EAGLE, self-speculation), **KV-cache tricks** (prefix caching, chunked prefill, multi-query/grouped-query attention).
  * **Lifecycle Evals (must-know frameworks):**
    * [**promptfoo**](https://github.com/promptfoo/promptfoo) ✅ — declarative YAML evals + CI integration.
    * [**DeepEval**](https://github.com/confident-ai/deepeval) ✅ — pytest-like LLM evals with G-Eval, faithfulness, hallucination metrics.
    * [**Ragas**](https://github.com/explodinggradients/ragas) ✅ — the de-facto RAG evaluation framework.
    * [**OpenAI Evals**](https://github.com/openai/evals) ✅ — Python + YAML spec, works with any endpoint.
    * [**lm-evaluation-harness (EleutherAI)**](https://github.com/EleutherAI/lm-evaluation-harness) ✅ — the canonical open-source harness (MMLU, GSM8K, HellaSwag, BBH, TruthfulQA, HumanEval).
    * [**HF Open LLM Leaderboard**](https://huggingface.co/open-llm-leaderboard) ✅ — the public scoreboard.

* **📦 Module Project (mandatory) — Fine-tune a small open model and prove it improved**
  * **Deliverable:** Take a small open-weights model, define a narrow task where you can measure quality, build a dataset for it, fine-tune with LoRA/QLoRA, and evaluate against three baselines: the base model zero-shot, the base model with a well-engineered prompt, and a RAG configuration over the same information. Report cost, latency, and quality for all four.
  * **Definition of done:** (1) A committed eval harness — a versioned eval set plus scoring code, runnable by one command; a `pytest` suite over the data-preparation and scoring functions; (2) `README.md` with the four-way comparison table, a training-loss curve, and your dataset card (size, provenance, licence, known gaps); (3) a results memo giving your recommendation and the conditions under which it would flip.
  * **Stretch:** Add a preference-tuning pass (DPO) on a small preference set and show whether it changed anything measurable — including whether it degraded a capability you did not intend to touch.
  * *This project is the empirical version of the [prompting vs RAG vs fine-tuning decision framework](#module-21). Video 1 (07:15) is explicit that being able to reason about that choice — with numbers — is what employers are testing for.*

---

<a id="module-21"></a>
## Module 21: RAG, Vector DBs & Retrieval Systems

* **The Tutor's "Why":** RAG is the single most-deployed LLM pattern in production (Oct 2025: >70% of enterprise LLM deployments per Menlo Ventures state-of-AI report). Getting chunking + retrieval + reranking right is often the difference between a demo and a product.

* **Strict Prerequisites:** Module 18 (LLMs, tokenisation), Module 11 (embeddings, cosine similarity, PCA/SVD for retrieval concepts), Module 8a (SQL — for metadata filtering and hybrid search).

* **Exhaustive Topic List:**
  * **Chunking strategies:** fixed-size, **recursive character splitters**, **semantic chunking** (embedding-based), **sentence-window retrieval**, **parent-document retrieval**, **auto-merging retrieval** (LlamaIndex), **late chunking** (Jina 2024 — embed whole doc, chunk embeddings post-hoc), **contextual retrieval** (Anthropic 2024 — LLM prepends context to each chunk before embedding).
  * **Embeddings:** **OpenAI text-embedding-3-large/small**, **Voyage-3-large** (2025 leader on MTEB), **BGE-M3** (BAAI, multilingual + multi-granularity), **Jina v3**, **Nomic Embed v2**, **Cohere Embed v4**, **NV-Embed** (NVIDIA). Learn **MTEB benchmark** (Massive Text Embedding Benchmark).
  * **Hybrid search:** **BM25** + dense (reciprocal rank fusion, RRF), **SPLADE** (sparse neural retrieval), **ColBERT v2 / ColPali** (late interaction — [ColBERT repo](https://github.com/stanford-futuredata/ColBERT) ✅).
  * **Rerankers:** **Cohere Rerank 3**, **BGE-Reranker v2**, **Jina Reranker v2**, **Voyage Rerank**, **Answer.ai RankZephyr / RankGPT**.
  * **Vector databases:** [**pgvector**](https://github.com/pgvector/pgvector) ✅ (Postgres extension, 2026 default for mixed workloads), [**Qdrant**](https://qdrant.tech/) ✅, [**Weaviate**](https://weaviate.io/) ✅, [**Milvus**](https://milvus.io/) ✅, [**LanceDB**](https://lancedb.com/) ✅ (embedded, Lance format), **Chroma**, **FAISS** (Meta, library — not a DB).
  * **Indexing & ANN algorithms:** **HNSW** (Hierarchical Navigable Small World), **IVF** (Inverted File with quantisation — IVF-PQ, IVF-SQ), **DiskANN**, **ScaNN** (Google), trade-offs (build time vs query latency vs recall@k).
  * **RAG patterns:** naive RAG, **Advanced RAG** (pre-retrieval query rewriting, HyDE, query decomposition, multi-query, step-back prompting), **GraphRAG** (Microsoft 2024 — community summaries, entity graphs), **Agentic RAG** (router + multi-tool), **Corrective RAG (CRAG)**, **Self-RAG**, **FLARE**.
  * **Evaluation:** **Ragas** metrics (faithfulness, answer relevance, context precision, context recall), **nDCG@k**, **MRR**, **recall@k**, **Needle-in-a-Haystack** for long context.

* **2026 Resources:**
  * **Primary Course Link:** [**Pinecone Learning Center**](https://www.pinecone.io/learn/) ✅ (comprehensive free RAG/vector primer) · [**LlamaIndex docs**](https://docs.llamaindex.ai/) ✅ (practical cookbook-driven) · [**LangChain RAG tutorial**](https://python.langchain.com/docs/tutorials/rag/) · [DeepLearning.AI short courses — "Advanced Retrieval for AI" & "Building and Evaluating Advanced RAG"](https://www.deeplearning.ai/).
  * **Required Reading:**
    * Lewis et al. 2020 ("Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks") — the original RAG paper.
    * Anthropic (Sep 2024) "Introducing Contextual Retrieval" — the 2024 enterprise-grade baseline.
    * Microsoft GraphRAG paper (2024).
    * [BGE / FlagEmbedding docs](https://github.com/FlagOpen/FlagEmbedding) — embeddings best practices.
  * **Practical Implementation:** **LlamaIndex 0.11+**, **LangChain 0.3+**, **Haystack 2.x** (deepset), **DSPy 3.2+** (retrieval modules), **pgvector + Postgres 17**, **Qdrant-client 1.17+**, **Ragas**.

* **⚖️ The decision framework: prompting vs RAG vs fine-tuning (learn this before you build anything)**

  This is the single most-asked design question in an AI-Engineer interview, and the most common way real projects waste money. The failure mode is almost always the same: reaching for fine-tuning when the actual problem was retrieval, or reaching for RAG when a better prompt would have done it. Work down this ladder in order and stop at the first rung that meets your quality bar.

  | Rung | Technique | Fixes | Does **not** fix | Cost / latency | Reach for it when |
  | :-- | :--- | :--- | :--- | :--- | :--- |
  | **1** | **Zero-shot prompting** | Nothing yet — this is your baseline and you are not allowed to skip it | Anything | Cheapest; one call | Always first. You cannot claim an improvement without it. |
  | **2** | **Few-shot / structured prompting** (examples, output schema, chain-of-thought, [DSPy](https://github.com/stanfordnlp/dspy) ✅ optimisers) | Format compliance, task ambiguity, reasoning-depth failures | Missing knowledge; stale facts | Cheap; larger prompt = more tokens | The model *could* know the answer but is answering the wrong question or in the wrong shape. |
  | **3** | **RAG / retrieval** (this module) | **Missing, private, or changing knowledge**; provenance and citation requirements; per-user or per-tenant data | Style, tone, output format, latent skill, deep domain reasoning | Moderate; +retrieval latency, +index cost | The failure is *"it does not know this"* — and especially when the knowledge changes faster than you could retrain. |
  | **4** | **Fine-tuning** (SFT / LoRA — [M18](#module-18)) | **Style, tone, consistent output format, domain-specific behaviour**, latency and cost via a smaller model, skills that do not fit in a prompt | Facts. A fine-tuned model still hallucinates about things it was not taught, and your training set is stale the day you freeze it | Highest up-front; cheapest per token afterwards | The failure is *"it knows this but behaves wrong"*, or you need a small model to do one narrow job cheaply. |
  | **5** | **RAG + fine-tuning together** | Both classes of failure | Bad data or an undefined eval | Highest total | You have measured both failure modes and have the eval suite to prove each component earns its keep. |

  * **The rule that makes this framework operational:** you cannot choose a rung without an **eval set**. Build the eval set first — 50–200 real queries with acceptable answers — then climb. Anyone who fine-tunes before they can measure has bought an unfalsifiable improvement. The [M18 module project](#module-18) makes you run this comparison empirically, with cost and latency columns.
  * **The default answer in 2026 is rung 3.** RAG is cheaper, updates instantly, gives citations, and keeps private data out of weights. Fine-tuning is the specialist tool, not the prestige tool.
  * **Two common misdiagnoses:** (a) *"the model hallucinates, so we will fine-tune"* — hallucination from missing knowledge is a retrieval problem, and fine-tuning usually makes it worse by teaching confident wrongness; (b) *"our RAG returns irrelevant chunks, so we need a better model"* — that is a chunking, embedding, or reranking problem, all of which live in this module and none of which are fixed by a bigger LLM.
  * **Also on the ladder, and frequently forgotten:** longer context windows, tool use / function calling ([M22](#module-22)), and simply routing to a stronger model. Each is cheaper than fine-tuning and should be priced before it.
  * **Sources:** video 1 (07:15) names *"knowing when to use RAG versus fine-tuning"* as a distinguishing skill employers probe for; video 3 (05:52) frames the whole AI-Engineer role as composing prompting, RAG, fine-tuning, and agents over models you did not train. Chip Huyen's [*AI Engineering*](#practitioner-shelf) is the long-form treatment.

* **📋 Mandatory mini-projects:**
  1. **Build a RAG over your own PDFs** — chunking → pgvector → BGE reranker → answer-with-citations; measure Ragas faithfulness & context precision.
  2. **Hybrid search A/B** — BM25-only vs dense-only vs hybrid-with-RRF; measure nDCG@10 on a labelled query set.
  3. **GraphRAG on a technical corpus** — run Microsoft GraphRAG, inspect community summaries, compare against vanilla RAG on multi-hop questions.

---

<a id="module-22"></a>
## Module 22: Agentic AI — LangGraph, CrewAI, MCP & A2A

* **The Tutor's "Why":** 2025 was the "year of the agent" and 2026 is the year of *reliable* agents. Every 2026 senior AI-engineer interview covers LangGraph + MCP + SWE-bench. HuggingFace launched a certified free [Agents Course](https://huggingface.co/learn/agents-course/) specifically to teach this. Closes Gap #4 of the benchmark PDF.

* **Strict Prerequisites:** Module 18 (LLMs, tool-use, function calling), Module 21 (retrieval).

* **Exhaustive Topic List:**
  * **Agent architectures:** ReAct (Reasoning + Acting), **Reflexion** (self-reflection), **Plan-and-Solve**, **Chain-of-Thought with tools**, **Tree-of-Thoughts**, **Graph-of-Thoughts**, **LATS** (Language Agent Tree Search).
  * **Frameworks (open-source):**
    * [**LangGraph**](https://www.langchain.com/langgraph) ✅ 1.1+ — stateful, cyclic, multi-agent graphs; the 2026 production default.
    * [**CrewAI**](https://docs.crewai.com/) ✅ — role-based multi-agent orchestration.
    * [**smolagents**](https://github.com/huggingface/smolagents) ✅ 1.24+ (Hugging Face) — code-agents that write Python to act; ~1000 LOC.
    * **AutoGen** 0.4+ (Microsoft), **OpenAI Agents SDK** (formerly Swarm, 2025), **Anthropic Claude Agent SDK** (2025).
  * **Model Context Protocol (MCP)** — Anthropic-led open standard (Nov 2024) for LLMs to access tools, resources, and prompts across applications.
    * Base spec: [modelcontextprotocol.io](https://modelcontextprotocol.io/) ✅
    * Spec revisions: [**2025-06-18 spec**](https://modelcontextprotocol.io/specification/2025-06-18) ✅ (structured tool output, resource-based OAuth), **Nov 2025 anniversary release** (code-execution-with-MCP pattern).
    * Implementations: `@modelcontextprotocol/sdk` (Python + TypeScript), [**mcp-servers**](https://github.com/modelcontextprotocol/servers) reference implementations (Filesystem, GitHub, Postgres, Slack, Browser, Google Drive, Sentry). Used in production by Claude Desktop, Cursor, VS Code, Zed, Replit, Sourcegraph Cody, Windsurf.
  * **Agent-to-Agent (A2A) Protocol** — Google's Apr 2025 open standard for cross-platform agent interop (complements MCP: MCP = tool-layer, A2A = agent-layer).
  * **Tooling & Sandboxing:** [**E2B**](https://e2b.dev/) ✅ (cloud sandboxes for code-execution agents), [**Daytona**](https://www.daytona.io/) ✅, [**Modal**](https://modal.com/) ✅ (serverless GPU sandboxes).
  * **Evaluation benchmarks:**
    * [**GAIA**](https://huggingface.co/gaia-benchmark) ✅ — Meta/HF general AI-assistant benchmark (3 levels).
    * [**SWE-bench**](https://www.swebench.com/) ✅ — resolve real GitHub issues; SWE-bench Verified (2024), SWE-bench Multimodal (2025).
    * **τ-bench** (tau-bench, Sierra 2024) — tool-use in realistic customer-service scenarios.
    * **WebArena**, **VisualWebArena** — browser-based agent eval.
    * **BrowseComp** (OpenAI 2025) — hard web-research eval.
  * **Patterns from Anthropic's ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) ✅ (Dec 2024):** workflows (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer) vs true agents (loops with tools). **"Start with prompts, graduate to workflows, only use full agents when you need them."**
  * **🔓 Agent security — prompt injection as a first-class engineering concern:** An agent with tools is an agent with a blast radius. The moment your system reads untrusted text (a web page, an email, a PDF, a user upload, another agent's output) and can then *act*, prompt injection stops being a curiosity and becomes your primary threat model.
    * **Direct prompt injection** — the user tries to override your system prompt ("ignore previous instructions"). Annoying, usually low-impact, easy to demo.
    * **Indirect prompt injection** — the payload is hidden in *content the agent retrieves*, not in what the user typed: a hostile instruction in a web page, a document, a code comment, an issue description, or a tool's response. This is the serious one, because the attacker never has to talk to your system directly. It is also the failure mode that RAG ([M21](#module-21)) and browsing agents structurally invite.
    * **What injection escalates into:** data exfiltration (the agent is told to append secrets to an image URL it fetches), unauthorised tool calls, destructive actions, and **confused-deputy** problems where the agent's credentials are more privileged than the requester's.
    * **Defences, honestly rated — none of them is a solution, and prompt-level mitigation is the weakest layer:**
      * **Least privilege on tools.** Read-only by default; scope credentials per-task; separate the agent that reads untrusted content from the agent that holds write access. This is the only defence with real leverage.
      * **Human-in-the-loop confirmation** for irreversible or privileged actions.
      * **Sandboxed execution** for anything code-shaped (E2B / Daytona / Modal / Firecracker / gVisor, above).
      * **Egress control** — allow-list the domains an agent may fetch or post to; this is what actually stops URL-based exfiltration.
      * **Content/tool-output isolation** — mark retrieved text as data, never as instructions; strip or neutralise instruction-shaped content; do not let tool output flow straight into the system-prompt position.
      * **Input/output guardrails** — [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) ✅, [Guardrails AI](https://www.guardrailsai.com/) ✅, [Llama Guard / PurpleLlama](https://github.com/meta-llama/PurpleLlama) ✅, Rebuff, Lakera Guard. Treat these as filters that raise cost for an attacker, not as boundaries.
    * **The stance to hold:** prompt injection is **not solved**, and any vendor claiming otherwise is wrong. Design so that a successful injection is survivable — that is an architecture decision, not a prompt-engineering one. Red-teaming technique and jailbreak taxonomy live in [M23](#module-23); the OWASP Top 10 for LLM Applications is the reference checklist.
  * **📊 Agent eval pipelines — treat evaluation as the deliverable, not the afterthought:** The benchmarks above (GAIA, SWE-bench, τ-bench, WebArena) tell you where the field is; they do not tell you whether *your* agent regressed this morning. You need your own harness.
    * **Trajectory evaluation, not just final-answer accuracy.** Score the steps: did it pick the right tool, with the right arguments, in a sensible order, and did it stop? An agent that reaches the right answer through six wrong tool calls is a latency and cost incident waiting to happen.
    * **Layered metrics:** task success rate · **pass@k** (agents are stochastic — a single run is not a measurement) · steps and tokens per task · **cost per successful task** (the number that actually gets budget approved) · wall-clock latency · tool-error and retry rate · termination behaviour (does it loop forever?).
    * **LLM-as-judge, used with discipline:** cheap and scalable, but biased toward verbose and self-similar answers. Calibrate it against a human-labelled subset, report the agreement rate, and never let an unvalidated judge gate a release.
    * **Run evals as CI.** A frozen eval set + a scored run on every prompt, model, or tool change — this is the agentic equivalent of a test suite, and it is what makes a portfolio project read as production work. Tooling: [DeepEval](https://github.com/confident-ai/deepeval) ✅ (pytest-like), **promptfoo**, [Ragas](https://github.com/explodinggradients/ragas) ✅ for the retrieval leg, [Arize Phoenix](https://github.com/Arize-ai/phoenix) ✅ / [LangSmith](https://www.langchain.com/langsmith) ✅ / W&B Weave for traces (cross-ref [M24](#module-24) AgentOps).
    * **Why this is emphasised:** **6 of the 7 AI-Engineer / Forward-Deployed postings [we surveyed](#skills-checklist) name evaluation explicitly** — more than RAG, agents, or fine-tuning individually. Building the demo is table stakes; proving it works is the job.

* **2026 Resources:**
  * **Primary Course (free, certified):** [**Hugging Face AI Agents Course**](https://huggingface.co/learn/agents-course/) ✅ — free, certified, uses smolagents + LangGraph + LlamaIndex; covers MCP integration.
  * **Berkeley LLM Agents MOOC:** [**llmagents-learning.org**](https://llmagents-learning.org/) ✅ (Fall 2024, Advanced Spring 2025) — with speakers including Denny Zhou, Graham Neubig, Jason Weston.
  * **Primary articles:**
    * [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) ✅
    * [OpenAI Cookbook — Agents](https://cookbook.openai.com/topic/agents)
    * [LangChain — "In the Loop" agent series](https://blog.langchain.dev/)
  * **Practical Implementation:** **LangGraph 1.1+**, **CrewAI**, **smolagents 1.24+**, **MCP Python SDK** (`pip install mcp`), **E2B / Modal / Daytona** for sandboxing, **Arize Phoenix / LangSmith / W&B Weave** for tracing (cross-ref to M24).

* **📋 Mandatory mini-projects:**
  1. **Build an MCP server** that exposes a small SQL database; connect it to Claude Desktop or Cursor and run ~10 queries.
  2. **LangGraph multi-agent** researcher that does planning → parallel web-search → synthesis → citation-checking; trace with LangSmith.
  3. **SWE-bench-Lite subset:** run a minimal agent on 5 SWE-bench instances and measure pass@1 vs pass@10.

---

<a id="module-23"></a>
## Module 23: AI Safety, Alignment, Interpretability, Evals & Policy

* **The Tutor's "Why":** No serious 2026 AI/ML role is hired without alignment and safety literacy. MIT AI Safety Forum + Berkeley MIDS + [AISF Alignment Fundamentals](https://aisafetyfundamentals.com/alignment/) ✅ all cover this. Closes Gaps #6, #12, and #13 of the benchmark PDF.

* **Strict Prerequisites:** Module 18 (LLMs, RLHF), Module 22 (agents).

* **Exhaustive Topic List:**
  * **Alignment problem framing:** outer vs inner alignment, specification gaming, reward hacking (Krakovna et al. 2020 taxonomy), mesa-optimisation, goal misgeneralisation (Langosco et al. 2022), deceptive alignment, sycophancy (Sharma et al. Anthropic 2024).
  * **RLHF pathologies & mitigations:** reward-model overoptimisation (Gao et al. 2023 scaling laws for reward hacking), length bias, sycophancy, mode collapse; **Constitutional AI** (Bai 2022), **RLAIF**, **weak-to-strong generalisation** (OpenAI 2023), **scalable oversight** (debate — Irving 2018, recursive reward modelling — Leike 2018, prover-verifier games).
  * **Mechanistic Interpretability:** [**Transformer Circuits thread**](https://transformer-circuits.pub/) ✅ (Anthropic). Core concepts: **features, circuits, motifs**, **induction heads** (Olsson et al. 2022), **superposition** (many features in few neurons), **polysemanticity**, **Sparse Autoencoders (SAEs)** as the 2024-2026 workhorse for recovering monosemantic features — see [**Scaling Monosemanticity** (Templeton et al. 2024)](https://transformer-circuits.pub/2024/scaling-monosemanticity/) ✅ and [**Golden Gate Claude**](https://www.anthropic.com/news/golden-gate-claude) ✅. Extensions: **Crosscoders**, **Transcoders**, **attribution patching**, **path patching**, **activation patching**.
  * **Activation/Representation Engineering:** RepE (Zou et al. 2023), steering vectors, contrastive activation addition (CAA), honesty probes.
  * **Eval harnesses (beyond basic LLM evals):**
    * [**OpenAI evals**](https://github.com/openai/evals) ✅
    * [**lm-evaluation-harness** (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness) ✅
    * [**Inspect** (UK AISI)](https://inspect.ai-safety-institute.org.uk/) — dedicated safety-eval framework.
    * [**HF Open LLM Leaderboard**](https://huggingface.co/open-llm-leaderboard) ✅
    * [**METR evals**](https://metr.org/) — task-duration-based capability evals.
    * Dangerous-capability evals: cyber (Cybench), CBRN, persuasion, agentic autonomy.
  * **Jailbreaks & red-teaming:** GCG (Universal adversarial suffixes, Zou 2023), AutoDAN, PAIR, Crescendo, many-shot jailbreaking (Anthropic 2024), prompt-injection at tool layer.
  * **AI Safety Policy & Regulation (2026):**
    * [**EU AI Act**](https://artificialintelligenceact.eu/) ✅ (fully in force 2 Aug 2026 for GPAI, risk categories, transparency, copyright, datasheets).
    * [**NIST AI RMF 1.0 + GenAI Profile**](https://www.nist.gov/itl/ai-risk-management-framework) ✅ (Jul 2024).
    * [**AI.gov**](https://ai.gov/) ✅ (US federal portal), US Executive Orders 2023/2025, UK AISI, Singapore AI Verify.
    * **ISO/IEC 42001:2023** (AI management system), **ISO 23894** (AI risk), **ISO 42005** (AI impact assessment).
    * **Model cards** (Mitchell et al. 2019), **datasheets for datasets** (Gebru et al. 2021), **system cards** (OpenAI/Anthropic style), **responsible scaling policies** (Anthropic RSP v2.1, OpenAI Preparedness Framework, Google DeepMind Frontier Safety Framework).
  * **Ethics foundations:** dual-use research, **differential privacy** (re-iterated from M24), fairness (DP/EO/Calibration trade-offs, impossibility result — Chouldechova 2017), FAT/FAccT community.

* **2026 Resources:**
  * **Primary Course (free):** [**AI Safety Fundamentals — Alignment Track**](https://aisafetyfundamentals.com/alignment/) ✅ (Bluedot Impact, 12-week curriculum, free facilitated cohorts 3×/year).
  * **Supplementary:** [AISF Governance Track](https://aisafetyfundamentals.com/governance/), [ARENA ML alignment curriculum](https://www.arena.education/), [Neel Nanda — MI study guide](https://www.neelnanda.io/mechanistic-interpretability/getting-started), [**EleutherAI Cookbook**](https://github.com/EleutherAI/cookbook) ✅.
  * **Required Reading:**
    * Amodei et al. 2016 "Concrete Problems in AI Safety" — the canonical problem enumeration.
    * Olah et al. — [Transformer Circuits thread](https://transformer-circuits.pub/) ✅.
    * Hubinger et al. 2019 "Risks from Learned Optimization" (mesa-optimisation).
    * Russell — *Human Compatible* (2019).
    * Christian — *The Alignment Problem* (2020).
    * [Anthropic "Core Views on AI Safety"](https://www.anthropic.com/news/core-views-on-ai-safety) (2023).
  * **Practical Implementation:** **TransformerLens** (Neel Nanda) for mech-interp, **SAELens** for Sparse Autoencoders, **`garak`** (red-teaming LLM scanner), **`pyrit`** (Microsoft AI red-team toolkit), **inspect-ai** (UK AISI evals), **promptfoo / DeepEval** (cross-ref M18).

* **📋 Mandatory mini-projects:**
  1. **Reproduce an induction head** on a 2-layer attention-only toy transformer (from the Transformer Circuits thread).
  2. **Train an SAE** on GPT-2 small activations at one layer; find and label 5 monosemantic features.
  3. **Red-team an open model** using `garak` or hand-crafted GCG suffixes; write a 2-page eval report with model card.
  4. **Draft an EU-AI-Act-compliant model card** for a hypothetical general-purpose AI model.

---

<a id="module-24"></a>
## Module 24: MLOps + LLMOps + AgentOps



* **The Tutor's "Why":** A Jupyter notebook is not a product. The 2026 data scientist must understand the entire lifecycle across three operational tiers: **(1) MLOps** for classical models, **(2) LLMOps** for prompt- and model-driven systems, and **(3) AgentOps** for the new class of stateful, tool-using agents from M22. Harvard's AC215 (new 2024) covers the first tier in depth; the other two are 2024-2026 standards, not yet in any university course.

* **Strict Prerequisites:** Any model from Modules 9-18.

* **Exhaustive Topic List:**
  * **[Harvard AC215 "Advanced Practical Data Science"]**: Containers (Docker, Docker Compose), container orchestration (Kubernetes, KubeFlow, Ray), **data pipelines** (Apache Airflow, Dagster 1.x, Prefect 3.x), **model registries**, **feature stores** (Feast, Tecton), API serving (FastAPI, BentoML, Ray Serve, Modal, Replicate), **A/B testing** (multi-armed bandit deployment, shadow deployment, canary, blue-green), **model monitoring** (data drift — KS test, PSI, JS divergence; concept drift; prediction drift), **observability** (OpenTelemetry, Weights & Biases, Arize, WhyLabs, Evidently).
  * **[IITM BSCS2003 — Modern Application Development I]**: Flask, Vue.js, REST APIs, OAuth, JWT, WebSockets, deployment to Heroku/Vercel/Fly.io.
  * **[IITM BSSE2001/BSSE2002 — Software Engineering & Testing]**: SDLC, agile, scrum, unit/integration/system testing, TDD, BDD, code review, pair programming, version control workflows (git-flow, trunk-based, GitHub Flow), CI/CD (GitHub Actions, GitLab CI, Jenkins).
  * **Experiment tracking & reproducibility**: Weights & Biases, MLflow 2.x, Neptune.ai, DVC (Data Version Control), Hydra for config, Pydantic 2.x for validation.
  * **GPU clusters & distributed training** (see **Stanford CS336 Lec 7–8 “Parallelism”**): Data parallelism (PyTorch DDP, **FSDP2**), tensor parallelism (Megatron‑LM), pipeline parallelism (GPipe, PipeDream), **3D parallelism**, ZeRO (DeepSpeed 1/2/3), **context parallelism** (Ring Attention), communication primitives (AllReduce, NCCL), gradient checkpointing, gradient accumulation, mixed precision (fp16, bf16, **fp8** — H100/H200/B200), **NVIDIA Blackwell (B200)** training (since PyTorch 2.7, April 2025).
  * **Inference optimisation**: TensorRT-LLM, vLLM continuous batching, speculative decoding, **prefix caching**, **chunked prefill**, INT8/INT4 quantisation at inference, KV-cache management.
  * **Responsible AI & governance**:
    * **Fairness metrics** — demographic parity, equalised odds, equal opportunity, calibration within groups; Aequitas, Fairlearn, AIF360.
    * **Explainability** — SHAP, LIME, Captum (for PyTorch), TCAV, counterfactuals (DiCE).
    * **Privacy** — **Differential Privacy** (Dwork 2006 formal definition, ε-δ-DP, Laplace and Gaussian mechanisms, composition theorems, moments accountant, DP-SGD — Abadi 2016), **Federated Learning** (FedAvg, FedProx, personalised FL), **Secure Multi-Party Computation** (SMPC), **Homomorphic Encryption** preview.
    * **Security** — adversarial attacks (M15), **prompt injection**, **data poisoning**, **model stealing / extraction**, **membership inference attacks**.
    * **Regulation (2026)** — **EU AI Act** (fully in force 2 Aug 2026 for GPAI obligations; risk categories, transparency duties, copyright and datasheet requirements), GDPR Art 22 (right to explanation), **ISO/IEC 42001:2023** (AI management), **NIST AI Risk Management Framework 1.0 + GenAI Profile (Jul 2024)**, **UK AI Safety Institute / AISI Inspect** evaluation framework, **US Executive Order on AI** (Biden 2023; Trump admin 2025 rollback + new E.O. on AI competitiveness).
  * **Agents and tool/data plumbing (2026)** — **Model Context Protocol (MCP)** — Anthropic‑led open standard for LLM↔tool/data servers; **2025‑06‑18 spec revision** + **Nov 2025 anniversary release** add structured tool output, resource‑based OAuth auth, code‑execution‑with‑MCP design pattern. Used in production by Claude Desktop, Cursor, VS Code, Zed, Replit, Sourcegraph Cody. Core ecosystem: **`@modelcontextprotocol/sdk`** (Python + TypeScript), `mcp-servers/*` (reference implementations for Filesystem, GitHub, Postgres, Slack, Browser).
  * **[Harvard CS109A · Lec 13 "Ethics"]**: Formal ethics module — fairness, accountability, transparency (FAT/FAccT), **dual-use research**, embedded ethics (Harvard Embedded EthiCS).
  * **[Harvard CS 1810 "Philosophy"]**: "With great power comes great responsibility" — mandatory embedded-ethics lecture.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard AC215 2024](https://harvard-iacs.github.io/2024-AC215/) · [Made With ML](https://madewithml.com/) · [Full Stack Deep Learning](https://fullstackdeeplearning.com/) · [**Hugging Face Agents Course**](https://huggingface.co/learn/agents-course/) (MCP + smolagents, free) · [**MCP docs**](https://modelcontextprotocol.io/) (Nov 2025 spec).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * _Designing Machine Learning Systems_ — Chip Huyen (O'Reilly 2022, still canonical).
    * **_AI Engineering_** — Chip Huyen (O'Reilly **Jan 2025**) — the 2026 successor.
    * _Machine Learning Engineering_ — Andriy Burkov.
    * _Algorithms of Oppression_ — Safiya Umoja Noble.
    * _Weapons of Math Destruction_ — Cathy O'Neil.
    * **EU AI Act consolidated text** (Regulation (EU) 2024/1689) — Annexes III–IV for high‑risk systems.
    * **NIST AI RMF 1.0 + GenAI Profile** ([nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)).
  * **Practical Implementation (MLOps tier):** **Docker 27+** / **Podman 5+**, **Kubernetes 1.32+**, **Terraform 1.9+**, **Pulumi** (modern alternative), **AWS/GCP/Azure SDKs**, **Ray 2.x** (Ray Tune, Ray Serve, Ray Data, RLlib), **vLLM**, **SGLang**, **BentoML**, **SkyPilot** (multi‑cloud), **Modal** (serverless GPU, $30/mo free tier, Stanford CS336 sponsor), **RunPod** / **Lambda** / **Nebius** (B200 access from ~$5/h), **Fairlearn 0.11+**, **AIF360**, **Opacus** (DP for PyTorch), **Flower** (federated learning), **MCP SDK** (Python + TypeScript, `pip install mcp`), **LangFuse** / **Arize Phoenix** (LLM observability), **Weights & Biases Weave** (LLM tracing), **Evidently 0.4+** (drift monitoring).

* **🤖 LLMOps Tier:** Operational practices specific to prompt-driven and LLM-driven systems.
  * **Prompt versioning & CI:** [**Langfuse**](https://langfuse.com/) ✅ (open-source, self-hostable), [**PromptLayer**](https://promptlayer.com/) ✅, [**Helicone**](https://www.helicone.ai/) ✅ (gateway + observability).
  * **Token & cost monitoring:** per-user, per-feature, per-model budgeting; rate-limit backpressure; fallback routing (GPT-4 → Claude → Llama 3); **LiteLLM** proxy, **OpenRouter**, **Portkey**.
  * **Guardrails:** [**NeMo Guardrails** (NVIDIA)](https://github.com/NVIDIA/NeMo-Guardrails) ✅, [**Guardrails AI**](https://www.guardrailsai.com/) ✅, [**Llama Guard / PurpleLlama**](https://github.com/meta-llama/PurpleLlama) ✅ (Meta), **Rebuff** (prompt-injection detection), **Lakera Guard**.
  * **LLM observability & tracing:** [**OpenTelemetry GenAI semantic conventions**](https://opentelemetry.io/docs/specs/semconv/gen-ai/) ✅ (the 2025-2026 standard), **Langfuse traces**, **Honeycomb for AI**, cost & latency dashboards.
  * **Evals in production:** reuse **promptfoo**, **DeepEval**, **Ragas** (M18); **A/B test prompts** as you would models.

* **🤖 AgentOps Tier:** Operational practices for stateful, tool-using agents (from M22).
  * **Agent tracing & debugging:** [**LangSmith**](https://www.langchain.com/langsmith) ✅, [**Arize Phoenix**](https://github.com/Arize-ai/phoenix) ✅ (open-source OTel-native), [**W&B Weave**](https://wandb.ai/site/weave) ✅, **Helicone Agents**, **Comet Opik**.
  * **Agent eval harnesses (production):** [**GAIA**](https://huggingface.co/gaia-benchmark) ✅, [**SWE-bench**](https://www.swebench.com/) ✅, **τ-bench**, **WebArena** — run these as regression tests.
  * **Sandboxing & isolation:** [**E2B**](https://e2b.dev/) ✅, [**Daytona**](https://www.daytona.io/) ✅, [**Modal**](https://modal.com/) ✅, Firecracker microVMs, gVisor.
  * **Key primary anchors for all three tiers:** [**Full Stack Deep Learning**](https://fullstackdeeplearning.com/) ✅, [**Made With ML** (Goku Mohandas)](https://madewithml.com/) ✅, [**Chip Huyen — *AI Engineering***](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) ✅.

* <a id="production-bar"></a>**🏁 Minimum Production Bar for Portfolio Projects**

  Every [module project](#module-projects) accumulates one production element via its stretch goal. This is the full list they accumulate *toward*. At least **one** project in your portfolio must satisfy every line below — that project is what separates a hireable repository from a bootcamp repository. The [M24 module project](#module-24) exists specifically to get you there.

  | # | Requirement | Passes when | Fails when |
  | :-- | :--- | :--- | :--- |
  | **1** | **Repository structure, not a loose notebook** | A real package (`src/` or `pkg/`, `__init__.py`, `pyproject.toml`), importable modules, an entry point, and pinned dependencies via `uv` or a lockfile. Notebooks exist only for exploration and are clearly marked as such. | The project *is* `analysis_final_v3.ipynb`. |
  | **2** | **Automated tests** | A `pytest` suite that runs in one command and covers the data layer, the transform logic, and at least one end-to-end path. Numerical code has a tolerance-based assertion; ML code has an overfit-a-tiny-batch smoke test. | "It works when I run it." |
  | **3** | **Typed Python** | Type hints on public functions, checked by `mypy` or `pyright` in CI. Pydantic v2 models for anything crossing a boundary (API request, config file, external payload). | Untyped `dict` passed between six functions. |
  | **4** | **Structured logging** | The `logging` module (or `structlog`) with levels, correlation/request IDs, and no secrets. You can reconstruct what happened from logs alone. | `print()` statements, or silence. |
  | **5** | **Configuration outside code** | Environment variables and/or a config file validated on startup (Hydra + Pydantic Settings). Secrets never committed — `.env` is gitignored and `.env.example` is not. | Hardcoded API key, hardcoded paths. |
  | **6** | **Containerised** | A `Dockerfile` that builds from a clean clone and runs. Pinned base image, non-root user, sensible layer caching, `.dockerignore`. | "Install these 14 things first." |
  | **7** | **CI pipeline** | A GitHub Actions workflow running lint (`ruff`) + typecheck + tests on every push and PR, with a green badge in the README. | Manual testing. |
  | **8** | **Experiment tracking** | Runs logged to **MLflow** or **Weights & Biases**: parameters, metrics, artefacts, git SHA. Your reported best result is reproducible from the tracked run. | Best score remembered from a terminal you have since closed. |
  | **9** | **Deployed and reachable** | A live URL. Streamlit Community Cloud, Hugging Face Spaces, Modal, Fly.io, Railway, or Cloud Run — free tiers are entirely acceptable. Include the URL at the top of the README. | Runs on your laptop only. |
  | **10** | **Monitoring** | Health check, request/latency/error metrics, and **one thing that would actually alert you**: input-distribution drift (Evidently), a quality metric, or a cost ceiling. For LLM systems, traces via Langfuse / Phoenix / LangSmith. | Deployed and never looked at again. |
  | **11** | **README a stranger can execute** | What it does · why · architecture diagram · quickstart that works from a clean clone · **results with numbers** · known limitations. | "Data science project." |
  | **12** | **Results memo** | ≤2 pages: the question, what you did, what you found, what you are uncertain about, what you would do next. This is the most-skipped and most-senior-reading artefact in the entire list. | No written interpretation of the numbers. |

  * **Reproducibility check (do this, it is brutal and it is fast):** clone your own repo into a fresh directory on a machine with nothing installed, follow only your README, and time yourself to first working output. If you cannot get there in 10 minutes, item 11 has failed regardless of what the file says.
  * **Do not apply this to all twelve projects.** Applying the full bar once, deeply, beats applying it partially twelve times — and a partially-productionised project is indistinguishable from an unproductionised one. Get **one** project to all twelve lines; keep the rest at their stretch-goal level.
  * **Then ship it anyway.** The bar is the target, not a gate on publishing. Push the repository at line 1 and work up in public — **a messy project on the internet beats a perfect project on your laptop**, and an in-progress repo with an honest "what's missing" section in the README is a stronger signal than a private perfect one.
  * **Sources:** video 1 (10:45–12:30) specifies the portfolio architecture standard — Docker, cloud deployment, CI/CD, MLflow or W&B, and monitoring — as the differentiator employers actually notice. Catherine Nelson's [*Software Engineering for Data Scientists*](#practitioner-shelf) is the book-length treatment of items 1–5; [*AI Engineering*](#practitioner-shelf) covers 9–10 for foundation-model systems.

* **📦 Module Project (mandatory) — Productionise one earlier project**
  * **Deliverable:** Do not build something new. Take the single best project you have already shipped — the churn dashboard from [M10](#module-10), the RAG system from [M21](#module-21), or the agent from [M22](#module-22) — and bring it to the full [Minimum Production Bar](#production-bar): package layout, tests, typed Python, structured logging, Dockerfile, CI pipeline, experiment tracking, a deployment target, and monitoring that would actually page you.
  * **Definition of done:** (1) Every line of the [Minimum Production Bar](#production-bar) checklist ticked, with the CI badge green and the deployment URL live; (2) `README.md` containing an architecture diagram, the runbook (how to deploy, how to roll back, what to do when the model degrades), and the cost per 1,000 requests; (3) a results memo — an incident write-up of one failure you deliberately induced (kill the vector DB, exhaust the rate limit, feed drifted input) and what your monitoring actually showed you.
  * **Stretch:** Add a canary or shadow deployment and an automated rollback triggered by your own quality metric.
  * *Rationale: video 1 (10:45–12:30) argues that the differentiator between a bootcamp portfolio and a hireable one is not more models, it is one model with Docker, cloud deployment, CI/CD, experiment tracking, and monitoring around it. This module exists to make that true of your repository.*

---

<a id="module-25"></a>
## Module 25: Product DS, Business, Communication & Storytelling

* **The Tutor's "Why":** A senior data scientist must be able to (a) frame a business problem as a measurable DS problem, (b) communicate results to non-technical stakeholders, and (c) drive decisions. Most theory-heavy curricula ignore this; CMU's MSPPM-DA and UMich MADS programs dedicate entire courses to it. Every Meta / Airbnb / Uber / Spotify DS interview has a "product case" loop.

* **Strict Prerequisites:** Module 6½ (A/B testing literacy), any modelling module.

* **Exhaustive Topic List:**
  * **Decision Intelligence framework:** Cassie Kozyrkov's five stages — frame the decision → explore the data → form hypothesis → build the model → make the decision; **cost of being wrong** analysis before modelling.
  * **Metric design:** north-star metrics, input vs output metrics, guardrail metrics, leading vs lagging indicators, **proxy metrics** (and their failures — Campbell's / Goodhart's laws), **OEC** (Overall Evaluation Criterion, Kohavi), product ↔ platform metric trees.
  * **Stakeholder communication:** executive summaries (1-page, BLUF — Bottom Line Up Front), **pyramid principle** (Minto), narrative structuring (situation → complication → question → answer), **SCQA** framework.
  * **Data storytelling & visualisation (cross-ref M7):** Cole Nussbaumer Knaflic's *Storytelling with Data*, [**Ben Shneiderman's "Overview, Zoom & Filter, Details-on-Demand"**](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf) framework, Edward Tufte's data-ink ratio.
  * **Business framing:** CRISP-DM revisited for 2026, **problem decomposition trees**, **assumption stacks**, **back-of-envelope sizing** (Fermi estimation), TAM/SAM/SOM, unit economics.
  * **Product-DS interview loops:** Meta product-analytics loop, Airbnb "diagnose a drop" question class, case frameworks for growth / engagement / retention / monetisation, A/B-test design under interviews (cross-ref M6½).
  * **Experimentation culture & governance:** experiment review processes, **trustworthy experimentation** (Kohavi's 12 pitfalls), **HiPPO** (Highest-Paid Person's Opinion) management, pre-registration of analysis plans.
  * **Communication artefacts:** **one-pagers**, **tech-spec docs**, **model cards** (cross-ref M23), **PR/FAQ** (Amazon working-backwards), post-launch readouts.
  * **Ethics in product decisions:** dark patterns, informed consent, opt-out vs opt-in, **digital wellbeing** metrics.

* **2026 Resources:**
  * **Primary Anchors (free):**
    * [**Cassie Kozyrkov — Decision Intelligence / Making Better Decisions with AI**](https://www.decisionintelligence.co/) ✅ + her [LinkedIn Learning course](https://www.linkedin.com/learning/instructors/cassie-kozyrkov) ✅ (free via many library programs).
    * **Ron Kohavi** — [exp-platform.com](https://exp-platform.com/) ✅ (industrial A/B testing, shared with M6½).
    * **Erika Hall** — *Just Enough Research* (free chapter; full book Rosenfeld Media 2019).
  * **University programs that teach this rigorously:**
    * [**CMU MSPPM-DA (Heinz College — Master of Science in Public Policy & Management: Data Analytics)**](https://www.heinz.cmu.edu/programs/public-policy-management-master/data-analytics) ✅ — policy-DS communication focus.
    * [**UMich School of Information — Master of Applied Data Science (MADS)**](https://www.si.umich.edu/programs/master-applied-data-science) ⚠️ bot-gated for curl but reader-accessible; explicitly teaches storytelling, communication, and stakeholder management in dedicated courses.
    * **Berkeley MIDS W271** (statistical methods for discrete response) + **W241** (experiments) for the methodological side.
  * **Required Reading:**
    * Cole Nussbaumer Knaflic — *Storytelling with Data* (Wiley 2015; *Let's Practice!* 2019).
    * Kohavi, Tang, Xu — [*Trustworthy Online Controlled Experiments*](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) ✅ (Cambridge 2020) — shared with M6½.
    * Barbara Minto — *The Pyramid Principle*.
    * Edward Tufte — *The Visual Display of Quantitative Information* (2e, 2001).
    * Cathy O'Neil — *Weapons of Math Destruction* (for the ethics layer).
  * **Blogs & newsletters:** [**Decision Intelligence / Decision.AI**](https://decision.ai/), Cassie Kozyrkov's Medium (archive), Amplitude / Mixpanel analytics blogs, [**Locally Optimistic** (analytics engineering community)](https://locallyoptimistic.com/).

* **📋 Mandatory mini-projects:**
  1. **One-page product memo:** Given a ∆-metric scenario (e.g., 7-day retention drops 3 pp), write a one-page memo — framing, root-cause hypotheses, proposed experiments, expected ROI.
  2. **Metric tree exercise:** For a product of your choice (marketplace, social, SaaS, media), construct a 3-level metric tree from north-star to input-level; identify guardrails.
  3. **Stakeholder readout:** Take any modelling project (your own or a Kaggle one); produce a 10-minute executive readout video + 3-page brief targeted at a non-technical VP.

---

<a id="module-26"></a>
## Module 26: Capstone — Research, Systems & Applied Tracks



* **The Tutor's "Why":** Every one of our four reference universities requires a substantial capstone. IITM requires a capstone project; Harvard CS109B culminates in a final project showcase; MIT 6.7960's grade is 35% final project; Cambridge MLMI runs a **4-month research dissertation** from end of Lent Term; Berkeley MIDS runs a client-sponsored capstone. This is the module where you convert a portfolio into a career. **v2026.2 introduces three tracks** so that research-leaning, systems-leaning, and applied-leaning students all have a rubric that matches their intended next step.

* **🎯 Three-Track Capstone Rubric (NEW v2026.2):**

  **Track 1 — Research** *(submit to a workshop; appropriate for PhD-bound / research-engineer roles).*
  - **Goal:** Produce a short paper (4–8 pages) worthy of an arXiv preprint + a NeurIPS / ICML / ICLR workshop submission.
  - **Rubric (100 pts):** Novelty (25) · Rigor — proofs, ablations, baselines (25) · Reproducibility — public repo + seeds + environment (25) · Clarity — writing quality & figures (25).
  - **Cross-reference:** Cambridge MLMI dissertation + MIT 6.7960 final-project blog post (Distill-quality).

  **Track 2 — Systems** *(deploy a production system with SLOs; appropriate for ML-engineer / AI-engineer roles).*
  - **Goal:** A publicly deployed LLM- or ML-driven system with measurable SLOs and an ops runbook.
  - **Rubric (100 pts):** Architecture diagram + tech spec (25) · Evals — promptfoo/Ragas/lm-eval (25) · Latency + cost SLOs met (p50/p95/p99, $/request) (25) · Ops runbook — on-call, rollback, monitoring dashboards (25).
  - **Cross-reference:** Stanford CS336 Assignment 5 (scaling + systems) + Chip Huyen's *AI Engineering* Ch 9–10.

  **Track 3 — Applied** *(real business / sponsored problem with causal evaluation; appropriate for product-DS / senior-DS roles).*
  - **Goal:** Address a real stakeholder's problem with a defensible causal estimate of impact.
  - **Rubric (100 pts):** Problem framing — business → DS translation (25) · Causal validity — identification strategy, sensitivity (25) · Stakeholder communication — one-pager + exec readout (25) · Measured impact — A/B test or quasi-experiment results (25).
  - **Cross-reference:** Berkeley MIDS capstone + CMU MSPPM-DA + IITM BSMS2001P Business Data Management Project.

* **Strict Prerequisites:** All previous modules, or sufficient depth in a chosen specialisation.

* **Exhaustive Topic List:**
  * **[Cambridge MLMI Research Project]**: Substantial research project from end of Lent Term through end of course, leading to **dissertation and poster presentation**. Must be in chosen track area.
  * **[Cambridge MLMI 2022-23 example projects]**: "Disease Subtyping and Biomarker Discovery using High-Dimensional Bayesian Mixture Models with Feature Selection", "Diffusion Models for Peptide Bonding" — demonstrates expected scope.
  * **[MIT 6.7960 Final Project]**: Research blog post format — background, investigation, results, with plots/animations/interactive graphics. Distill-pub standard.
  * **[Harvard CS109A/B Final Project]**: Final Project Showcase with peer evaluations.
  * **[IITM BS Project / MSMS2001P Business Data Management Project]**: Real-world applied project with business stakeholder.
  * **The Capstone Framework (synthesised)**:
    1. **Problem identification** — Novel contribution or improved benchmark. Connect to one of: climate/energy, medicine/bio, education, robotics, finance, public-interest tech.
    2. **Literature review** — Use **Semantic Scholar** + **Connected Papers** + **Elicit** + **OpenReview** for systematic search; maintain **Zotero 7** library.
    3. **Reproducibility package** — Repo with `README.md`, `pyproject.toml` (using `uv`), `data/` (with DVC or HuggingFace datasets), `notebooks/`, `src/` with typed Python, `tests/`, `Dockerfile`, GitHub Actions CI, arXiv paper (LaTeX `acmart` or `NeurIPS`), model card, datasheet for datasets (Gebru et al. 2018).
    4. **Writing** — Follow ICML/NeurIPS/ICLR/JMLR style; include reproducibility checklist; publish blog post on Distill-style platform.
    5. **Dissemination** — Release to arXiv, submit to workshop/conference, present poster, tweet-summary, **HuggingFace model/dataset release**.
  * **Suggested 2026-relevant capstone directions**:
    * Fine-tune a small LLM (<7B) on a domain corpus with **DPO/GRPO**; benchmark vs base.
    * Train a **diffusion model** or **flow-matching** generator on a novel domain.
    * Build an **agentic system** using MCP + an open-source model; evaluate on a task suite.
    * **Mechanistic interpretability** — find circuits in a small transformer using Sparse Autoencoders.
    * **Bayesian deep learning** — variational BNN / Laplace approximation on a scientific dataset.
    * Climate/energy ML — solar forecasting, grid optimisation, satellite-image analysis.
    * Medical ML — with proper IRB/data-use agreement; e.g., MIMIC-IV, UK Biobank.

* **2026 Resources:**
  * **Primary Course Link:** [Cambridge MLMI course structure](https://www.mlmi.eng.cam.ac.uk/about-programme/course-structure) · [MLMI past projects](https://www.mlmi.eng.cam.ac.uk/course-highlights/2022-2023-course-highlights).
  * **Required Reading (Latest 2026 Editions):**
    * _The Craft of Research_ (4th Ed) — Booth, Colomb, Williams.
    * _How to Write a Lot_ — Paul Silvia.
    * _Writing Science_ — Joshua Schimel.
    * ML Reproducibility Checklist — NeurIPS 2019+.
  * **Practical Implementation:** **Zotero 7** + **Better BibTeX**, **Obsidian** or **LogSeq** for research notes, **Typst** or **LaTeX Overleaf** for writing, **Jupyter Book** for interactive docs, **HuggingFace Spaces** for demo deployment, **ArXiv** for preprints, **OpenReview** for submissions.

---

<a id="books"></a>
# 📖 Core Textbook Reading List

> **Tier 1 (own a copy)**. These are the books you should have on your shelf, marked-up, for the rest of your career.

| # | Title | Authors | Edition / Year | Primary Modules | Free PDF? |
|---|---|---|---|---|---|
| 1 | _Introduction to Probability_ | Blitzstein & Hwang | 2nd Ed. (2019; 2024 reprint) | M5 | ✅ [stat110](https://projects.iq.harvard.edu/stat110/home) |
| 2 | _Mathematics for Machine Learning_ | Deisenroth, Faisal, Ong | 2020 (2024 reprint) | M2, M3, M5 | ✅ [mml-book.com](https://mml-book.com/) |
| 3 | _An Introduction to Statistical Learning with Python_ (ISLP) | James, Witten, Hastie, Tibshirani, Taylor | 1st Ed. (2023, 2025 reprint) | M6, M9-M12 | ✅ [statlearning.com](https://www.statlearning.com/) |
| 4 | _Elements of Statistical Learning_ (ESL) | Hastie, Tibshirani, Friedman | 2nd Ed., 12th printing | M9-M12 | ✅ [hastie.su.domains](https://hastie.su.domains/ElemStatLearn/) |
| 5 | **_Deep Learning: Foundations and Concepts_** (NEW — primary DL text) | Christopher M. Bishop & Hugh Bishop | **Springer 2024**, 1st Ed., 607 pp., ISBN 978‑3‑031‑45467‑7 | M15‑M16 | ✅ [bishopbook.com](https://bishopbook.com/) |
| 6 | _Probabilistic Machine Learning: An Introduction_ (PML1) | Kevin P. Murphy | MIT Press 2022 | M11-M16 | ✅ [probml.github.io](https://probml.github.io/pml-book/book1.html) |
| 7 | _Probabilistic Machine Learning: Advanced Topics_ (PML2) | Kevin P. Murphy | MIT Press 2023 | M13-M17 | ✅ [probml.github.io](https://probml.github.io/pml-book/book2.html) |
| 8 | _Understanding Deep Learning_ | Simon Prince | MIT Press 2024 | M15-M16 | ✅ [udlbook.github.io](https://udlbook.github.io/udlbook/) |
| 9 | _Dive into Deep Learning_ | Zhang, Lipton, Li, Smola | 2024, continuously updated | M15-M16 | ✅ [d2l.ai](https://d2l.ai/) |
| 10 | _Reinforcement Learning: An Introduction_ | Sutton & Barto | 2nd Ed. 2018 (2024 reprint) | M17 | ✅ [incompleteideas.net](http://incompleteideas.net/book/the-book-2nd.html) |
| 11 | _Bayesian Data Analysis_ (BDA3) | Gelman et al. | 3rd Ed. 2013 (2024 reprint) | M6, M13 | ✅ [stat.columbia.edu](http://www.stat.columbia.edu/~gelman/book/) |
| 12 | _Introduction to Algorithms_ (CLRS) | Cormen, Leiserson, Rivest, Stein | 4th Ed. 2022 | M4 | — |
| 13 | _Introduction to Linear Algebra_ | Gilbert Strang | 6th Ed. 2023 | M3 | — |
| 14 | _Designing Data-Intensive Applications_ | Martin Kleppmann | 1st Ed. 2017 (2nd Ed. coming 2026) | M8, M19 | — |
| 15 | **_Speech and Language Processing_ (3rd Ed. draft, continually updated)** | Jurafsky & Martin | Draft 2024–2026 | M16, M18 | ✅ [stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/) |
| 16 | _Foundations of Computer Vision_ | Torralba, Isola, Freeman | **MIT Press 2024** | M15-M16 | ✅ [visionbook.mit.edu](https://visionbook.mit.edu/) |
| 17 | _Designing Machine Learning Systems_ | Chip Huyen | O'Reilly 2022 (2024 reprint) | M19 | — |
| 18 | _Build a Large Language Model (From Scratch)_ | Sebastian Raschka | Manning **2024** | M18 | Partial GitHub mirror |
| 19 | _Python for Data Analysis_ | Wes McKinney | 3rd Ed. 2022 | M7 | ✅ [wesmckinney.com](https://wesmckinney.com/book/) |
| 20 | _Fluent Python_ | Luciano Ramalho | 2nd Ed. 2022 (3rd Ed. in progress) | M1 | — |
| **21** | **_Hands‑On Machine Learning with Scikit‑Learn and PyTorch_** (NEW, **replaces TF edition**) | Aurélien Géron | **O'Reilly, Oct–Dec 2025**, 878 pp. | M9‑M17 | GitHub: [ageron/handson-mlp](https://github.com/ageron/handson-mlp) |
| **22** | **_Hands‑On Large Language Models_** (NEW) | Jay Alammar & Maarten Grootendorst | **O'Reilly, Sep 2024**, 428 pp. | M18 | [HandsOnLLM repo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) |
| **23** | **_AI Engineering_** (NEW) | Chip Huyen | O'Reilly Jan 2025 | M18‑M19 | — |
| **24** | **_Pattern Recognition and Machine Learning_** (PRML — moved to Tier 1‑reference) | Christopher Bishop | 2006 (still in print) | M9‑M17 | — |
| **25** | **_Linear Algebra Done Right_ — 4th Edition (the abstract / proof‑track linear algebra)** | Sheldon Axler | **Springer 2024**, 400 pp., ISBN 978‑3‑031‑41025‑3 | M3 | ✅ [linear.axler.net](https://linear.axler.net/) |
| **26** | **_Introduction to Probability for Data Science_ — bridges Stat 110 to Python code** | Stanley H. Chan | Michigan Publishing **2021/2023**, 700+ pp. | M5 | ✅ [probability4datascience.com](https://probability4datascience.com/) |
| **27** | **_Convex Optimization_** (paired with Stanford EE364A) | Stephen Boyd & Lieven Vandenberghe | Cambridge 2004, **6th printing 2023** | M2, M9‑M11 | ✅ [stanford.edu/~boyd/cvxbook/](https://stanford.edu/~boyd/cvxbook/) |
| **28** | **_Information Theory, Inference, and Learning Algorithms_** | David J. C. MacKay | Cambridge **2003** (the gold-standard intro to entropy/MI) | M5, M16, M18 | ✅ [inference.org.uk/itila](https://www.inference.org.uk/itila/) |
| **29** | **_High-Dimensional Probability_ — concentration inequalities for ML/statistics** | Roman Vershynin | Cambridge **2018** (free draft online) | M5, M9, M15 | ✅ [vershyn HDP draft](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html) |
| **30** | **_Book of Proof_ — proof-writing for first-year university** | Richard Hammack | **3rd Edition, 2018** (CC-BY) | **M0b** | ✅ [richardhammack.github.io/BookOfProof](https://richardhammack.github.io/BookOfProof/) |
| **31** | **_How to Prove It: A Structured Approach_ + *With Lean* (browser-interactive)** | Daniel J. Velleman | Cambridge **3e, 2019** + Lean companion **2024** | **M0b** | Lean: ✅ [djvelleman.github.io/HTPIwL](https://djvelleman.github.io/HTPIwL/) |
| **32** | **_Mathematics for Computer Science_ (MIT 6.042J textbook)** | Lehman, Leighton, Meyer | **2015 final, still current**, MIT Press | **M0b**, M4 | ✅ [OCW PDF](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) |
| **33** | **_Numerical Linear Algebra_** | Lloyd N. Trefethen & David Bau III | SIAM **1997**, 25th-anniversary printing 2022 | M3, M24 | — |
| **34** | **_Trustworthy Online Controlled Experiments_** (industrial A/B-testing bible) | Ron Kohavi, Diane Tang, Ya Xu | Cambridge **2020** | **M6½**, M25 | — |
| **35** | **_Fundamentals of Data Engineering_** (Gap #2 anchor) | Joe Reis & Matt Housley | O'Reilly **2022** | **M8a, M8b** | — |
| **36** | **_Causal Inference: What If_** (free) | Miguel A. Hernán & James M. Robins | Continuously updated, **2024 revision** | **M6½** | ✅ [Harvard / Hernan What If PDF](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf) |
| **37** | **_Causal Inference in Statistics: A Primer_** | Judea Pearl, Madelyn Glymour, Nicholas P. Jewell | Wiley **2016** | **M6½** | — |
| **38** | **_Storytelling with Data_** (+ *Let's Practice!*) | Cole Nussbaumer Knaflic | Wiley 2015 / 2019 | **M25** | — |

> **Tier 2 (reference)**: _All of Statistics_ (Wasserman), _Statistical Inference_ (Casella & Berger), _Bayesian Reasoning and Machine Learning_ (Barber), _Machine Learning: A Probabilistic Perspective_ (Murphy 2012), _Deep Learning_ (Goodfellow/Bengio/Courville 2016), _Algorithms for Decision Making_ (Kochenderfer), _Interpretable Machine Learning_ (Molnar), _Forecasting: Principles and Practice_ (Hyndman 3rd Ed. 2021), _Mining of Massive Datasets_ (Leskovec 3rd Ed. 2020, free at [mmds.org](http://www.mmds.org/)), _The Elements of Statistical Learning_ (ESL — still canonical), **_Active Calculus_** (Boelkins, free 2024), **_Linear Algebra and Learning from Data_** (Strang 2019/25 reprint), **_The Matrix Cookbook_** (Petersen-Pedersen 2024), **_Probability with Martingales_** (Williams 1991, PhD-track), **_Measure, Integral and Probability_** (Capinski-Kopp 2e 2014, PhD-track), **_Tao Analysis I & II_** (Hindustan Book Agency, 4e 2022, real-analysis bridge for PhD-track).

<a id="practitioner-shelf"></a>
## 🧰 The Practitioner Shelf

> **What this subsection is, and what it is not.** The Tier 1 and Tier 2 lists above are the **academic spine** — they are what you read to be able to *check* a claim, derive a result, and read a paper. Nothing in them is deprecated by this subsection.
>
> This shelf is the **applied canon**: the shorter, faster, code-first books that get you from "I can write a loop" to "I have shipped a product built on a foundation model." It is the reading list attached to the [Practitioner Fast Lane](#practitioner-track) and the [AI Engineer (Applications)](#choose-your-track) track, sourced from [video 3](#refresh-log) — an ex-Coursera / ex-Amazon engineer's seven-book canon for the AI Engineer role — and reconciled against what this roadmap already carried.
>
> **The trade-off, stated plainly.** These books teach you to *build*. They do not teach you to *prove*. Every one of them optimises intuition and working code over derivation, which is exactly why they are fast and exactly why they are insufficient for research work. If your target is a PhD, a research-scientist role, or reading NeurIPS papers critically, this shelf is a supplement to the Tier 1 spine, not a substitute for it. Video 3 (04:47) makes the intuition-over-derivation argument explicitly; [Tier 1](#books) is the counterargument, and both are correct within their own conditions.

| # | Title | Author(s) | Edition / Year | Serves | Access |
| :-- | :--- | :--- | :--- | :--- | :--- |
| **P1** | _Automate the Boring Stuff with Python_ | Al Sweigart | No Starch, **3rd Ed.** | [M1](#module-1) · [Fast lane](#practitioner-track) Stage 1 | ✅ **Free full text**: [automatetheboringstuff.com](https://automatetheboringstuff.com/) · print: [No Starch](https://nostarch.com/automate-boring-stuff-python-3rd-edition) |
| **P2** | _Software Engineering for Data Scientists: From Notebooks to Scalable Systems_ | Catherine Nelson | O'Reilly, **May 2024** | [M1](#module-1) · [M24](#module-24) · the [Minimum Production Bar](#production-bar) | ✅ [Author's book page](https://catherinenelson.dev/books/software-engineering-for-data-scientists) · ⚠️ [O'Reilly](https://www.oreilly.com/library/view/software-engineering-for/9781098136192/) (403 to crawlers, opens in a browser) · ISBN 978-1-098-13619-2 |
| **P3** | _The Manga Guide to Statistics_ | Shin Takahashi | No Starch | [M6](#module-6) intuition track | ✅ [No Starch](https://nostarch.com/mg_statistics.htm) |
| **P3b** | _The Manga Guide to Linear Algebra_ | Shin Takahashi | No Starch | [M3](#module-3) intuition track | ✅ [No Starch](https://nostarch.com/mg_linearalgebra.htm) |
| **P3c** | _The Manga Guide to Regression Analysis_ | Shin Takahashi | No Starch | [M9](#module-9) intuition track | ✅ [No Starch](https://nostarch.com/regression) |
| **P4** | _StatQuest Illustrated Guides_ — three volumes: **Machine Learning**, **Neural Networks and AI**, **Statistics** | Josh Starmer | Self-published | [M6](#module-6) · [M9](#module-9)–[M12](#module-12) · [M15](#module-15) intuition track | ✅ [statquest.org store](https://statquest.org/statquest-store/) · free companion videos at [statquest.org](https://statquest.org/) |
| **P5** | _Build a Large Language Model (From Scratch)_ | Sebastian Raschka | Manning, **2024** | [M16](#module-16) · [M18](#module-18) — **already [Tier 1 #18](#books)** | ✅ [Manning](https://www.manning.com/books/build-a-large-language-model-from-scratch) · ✅ free code: [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) |
| **P6** | _AI Engineering_ | Chip Huyen | O'Reilly, **Jan 2025** | **Primary text of the [AI Engineer (Applications)](#choose-your-track) track** · [M18](#module-18) · [M21](#module-21)–[M24](#module-24) — **already [Tier 1 #23](#books)** | ✅ [Author's book page](https://huyenchip.com/books/) · ⚠️ [O'Reilly](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) (403 to crawlers) · ISBN 978-1-098-16629-8 |
| **P7** | _Generative AI System Design Interview_ | Alex Xu, **Ali Aminian, Hao Sheng** | ByteByteGo, **2024** | [M21](#module-21) · [M22](#module-22) · [M24](#module-24) · interview prep for the [AI Eng track](#skills-checklist) | ✅ [Publisher announcement](https://blog.bytebytego.com/p/our-new-book-generative-ai-system) · ISBN 1736049143 |

### How to actually use this shelf

The seven entries are not a reading order — they are four distinct jobs.

| Job | Books | When |
| :--- | :--- | :--- |
| **Get Python useful fast** | P1 | [M1](#module-1), weeks 1–8. Read alongside the [free-course matrix](#python-course-matrix), not instead of it. |
| **Stop writing notebook code** | P2 | The moment your first project outgrows one file. This is the single most under-read book on the shelf and the one that maps most directly onto the [Minimum Production Bar](#production-bar). |
| **Get maths and ML intuition without proofs** | P3 series, P4 | Paired with the [⚡ Intuition-First callouts](#module-3) in M3, M5, M6, M9–M12. Watch the free StatQuest videos first; buy the illustrated guides only if you want the offline reference. |
| **Become an AI Engineer** | P5, P6, P7 | [M18](#module-18) onward. **P6 is the anchor text** — read it end to end. P5 gives you the mechanical understanding of what you are building on; P7 gives you the system-design vocabulary that interviews use. |

> **On the notebook-to-production progression.** Video 3 (07:30) frames P2 as the hinge of the whole shelf: the gap between someone who can produce a working notebook and someone employable is testing, structure, refactoring, and APIs — not more modelling. Our [surveyed 2026 postings](#skills-checklist) agree: 15 of 16 asked for communication and collaboration, and none asked for Kaggle standing.
>
> **On P6 as the track's primary text.** Chip Huyen's own framing of the discipline — *"AI engineering: the process of building applications with readily available foundation models"* ([huyenchip.com/books](https://huyenchip.com/books/) ✅) — is precisely the role definition the [AI Engineer (Applications)](#choose-your-track) track targets: you build **on** models, you do not train them from scratch. It is also the reason this roadmap keeps a separate research-adjacent AI Engineer row rather than collapsing the two.

### Corrections logged while verifying this shelf

Recorded here because the repo's [audit discipline](audit/VERIFICATION.md) requires that corrections be visible rather than silently applied:

* **P7 authorship.** The source video credits this book to Alex Xu and Sahn Lam. The publisher's own announcement names **Alex Xu, Ali Aminian, and Hao Sheng**; Sahn Lam is a co-author of ByteByteGo's *System Design Interview* series, not of this title. The corrected attribution is used above.
* **P4 link structure.** Per-title StatQuest URLs (e.g. `statquest.org/statquest-illustrated-guide-to-machine-learning/`) return **404**. The canonical entry point is the [store page](https://statquest.org/statquest-store/). A **third** volume — *Statistics* — exists and is not mentioned in the source video; it is included above.
* **P7 URL.** `bytebytego.com/courses/generative-ai-system-design-interview` returns **404** and is not cited. The publisher announcement post is used instead.

Full HTTP status log for every link in this subsection: [`audit/VERIFICATION.md`](audit/VERIFICATION.md) and [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md).

---

<a id="toolchain"></a>
# 🛠️ Production Toolchain

A practical stack mapped to the curriculum. Version numbers below are a dated reference snapshot, not permanent recommendations; check the linked project before installing.

| Category | Tool | **Reference snapshot** | Why it matters |
|---|---|---|---|
| **Python runtime** | CPython | **3.13+** (3.14 RC compatible) | Free‑threaded build (PEP 703) in experimental; per‑interpreter GIL for parallel ML workloads |
| **Package manager** | `uv` | **0.11.7** (Apr 2026) | 10‑100× faster than pip/poetry; now the de‑facto standard; replaces `pipenv`/`poetry`/`virtualenv` |
| **Env manager** | `pixi` or `conda` / `mamba` | latest | For non‑Python system deps (CUDA 13, MKL, mamba = fast conda) |
| **IDE** | VS Code + Cursor / Zed | latest | Cursor = AI‑native forks; Zed = Rust‑fast, multiplayer |
| **Notebooks** | Jupyter Lab / `marimo` | Lab 4.x / marimo 0.10+ | marimo = reactive + reproducible notebooks (2026 favourite) |
| **Formatter / Linter** | `ruff` | **0.7+** | One Rust binary replaces Black, isort, flake8, pylint, pyupgrade, autoflake, pydocstyle |
| **Type checker** | `pyright` (or `mypy`) | 1.1.400+ | Gradual typing essential; `pyright` is the 2026 default |
| **DataFrames** | **Polars** + **DuckDB** | **1.40.1 / 1.5.2** | Polars streaming engine 3‑7× faster than in‑memory; DuckDB 1.5 for single-node OLAP |
| **Data validation** | **Pandera** / **Great Expectations** | latest | Schema + quality contracts for pipelines (M7, M8a/b, M24) |
| **Numerical core** | NumPy | **2.2+** | New dtypes (StringDType, variable‑precision); 50% smaller wheel |
| **Classical ML** | scikit-learn | **1.8.0** (Dec 2025) | Native Polars support; `set_output("polars")` on every transformer |
| **Boosting** | XGBoost / LightGBM / CatBoost | 2.x / 4.x / 1.2+ | Still dominant on tabular; XGBoost 2 has GPU hist + vector leaf |
| **Causal Inference** | **DoWhy** / **EconML** / **CausalML** | latest | End-to-end causal workflow (M6½); DoWhy = identify→estimate→refute |
| **Deep Learning** | **PyTorch** | **2.11.0** (23 Mar 2026) | `torch.compile` + FSDP2 + CUDA 13 + Blackwell (B200); TorchTitan for large‑scale |
| **Alt DL** | **JAX** + Flax / Equinox / NNX | **0.10.0** (16 Apr 2026) | TPU‑first; PT/JAX bridge via PyTorch/XLA 2.7; `jax.jit()` decorator‑factory pattern |
| **Bayesian** | NumPyro / PyMC / blackjax | **0.20.1 / 5.28.4 / latest** | JAX‑backed; PyMC 5 uses PyTensor backend |
| **Transformers** | **Hugging Face Transformers** | **v5.6.2** (Apr 2026) | v5 = simplified model definitions; v4.57 LTS = final v4 branch. Works with PyTorch 2.4+. |
| **LLM fine‑tuning** | `trl` + `peft` + **Unsloth** + Axolotl | **TRL 1.2.0 · PEFT 0.19.1** | SFT / DPO / **GRPO** / **RLVR** / KTO / IPO / ORPO / SimPO — one surface |
| **LLM inference** | **vLLM** / **SGLang** / TensorRT-LLM | **0.19.1** / latest | Continuous batching, paged‑attention, prefix caching, **FlashAttention‑3**, speculative decoding |
| **LLM evals** | **promptfoo** / **DeepEval** / **Ragas** / **lm-eval-harness** | latest | M18 fine-tuning playbook + M24 LLMOps |
| **Agents & Tools** | `smolagents` / **LangGraph** / LlamaIndex / **CrewAI** | **smolagents 1.26.0 · LangGraph 1.2.10 · CrewAI 1.15.9 · LlamaIndex 0.14.23** (PyPI, 30 Jul 2026) | **MCP‑native** since v1.0; Hugging Face Agents Course covers all three. CrewAI = role-based crews (M22) |
| **MCP** | Anthropic MCP SDK (Py / TS) | 2025‑06‑18 spec + Nov 2025 anniversary | Standard for LLM↔tool/data interoperability |
| **Agent sandboxing** | E2B / Daytona / Modal | latest | Isolated code-execution for agents (M22, M24 AgentOps) |
| **Prompting** | **DSPy** | **3.2.0** (Apr 2026) | Programmatic prompting; optimiser‑driven; 2026 research favourite |
| **Vector DB** | **pgvector** / **Qdrant** / Weaviate / Milvus / LanceDB | **Qdrant-client 1.17.1** | pgvector = Postgres‑native; Qdrant = Rust; LanceDB = arrow‑first |
| **RAG orchestration** | **LlamaIndex** / **LangChain** / Haystack | latest | M21 toolchain; cookbook-driven |
| **MLOps** | **Ray** / **MLflow** / **W&B** | 2.x / **3.11.1** / latest | Ray for scaling / RLlib; MLflow 3 tracking; W&B for research |
| **LLMOps** | **Langfuse** / Helicone / PromptLayer | latest | Prompt versioning + observability (M24 tier) |
| **AgentOps** | **LangSmith** / **Arize Phoenix** / W&B Weave | latest | Agent tracing + replay (M24 tier) |
| **Guardrails** | NeMo Guardrails / Guardrails AI / Llama Guard | latest | Input/output filtering + jailbreak defence (M23, M24) |
| **Interpretability** | **TransformerLens** / SAELens | latest | Mech-interp + sparse autoencoders (M23) |
| **Data Engineering** | **dbt-core** / Airflow / Dagster / Prefect / Kafka / Spark / Flink | **dbt 1.11.8** | M8a/b stack |
| **Containers** | Docker / Podman | 27+ / 5+ | Multi‑arch, rootless, SBOM |
| **Orchestration** | Kubernetes / **Dagster** / Prefect | 1.32+ / 1.x / 3.x | Dagster > Airflow for ML pipelines (asset‑centric) |
| **Serving** | **FastAPI** + BentoML / **Modal** | latest | Modal = serverless GPU with $30/mo free; used by Stanford CS336 |
| **Dashboards & demo UIs** | **Streamlit** / Gradio / Evidently | **Streamlit 1.60.0** (PyPI, 21 Jul 2026) | The default free deployment target for the [Minimum Production Bar](#production-bar) item 9 (Streamlit Community Cloud · HF Spaces); Evidently for drift dashboards (M24) |
| **Experiment config** | **Hydra** + **Pydantic** | 1.3+ / 2.10+ | Pydantic 2 is 20× faster than v1 |
| **Reproducibility** | DVC + Git LFS | 3.x / latest | Version control for data + models |
| **Writing** | Typst or LaTeX + Zotero 7 | latest | Typst = modern LaTeX alternative, compiles in ms |
| **GPU compute (self‑study)** | Modal · RunPod · Lambda · Nebius · Together | March 2026 prices | B200: Modal $6.25/h · RunPod $4.99/h · Lambda $6.69/h (Stanford CS336 sponsor list) |

---

<a id="career-operations"></a>
# 🧭 Career Operations

Everything above this line is about competence. This section is about the entirely separate skill of **converting competence into a job** — which most technical curricula omit, and which is where most self-taught learners actually stall.

Two honest caveats before anything else. First, the guidance here is doctrine drawn from named practitioners (see [sources](#refresh-log)), not from a controlled study; treat it as informed heuristics. Second, nothing in this section substitutes for the [module projects](#module-projects). Career tactics applied to an empty portfolio do not work.

## 1. The internal locus of control

The single highest-leverage mental model in the source material. An **internal** locus of control means you attribute outcomes to your own actions; an **external** locus means you attribute them to the market, your degree, your age, or luck.

Video 2 (07:12) makes the operational case: the market, the hiring bar, and your background are all fixed inputs you cannot edit. The only editable variables are what you build, who you talk to, and how many attempts you make. Every hour spent on the fixed inputs is an hour not spent on the editable ones.

What this looks like in practice:

| External framing (stalls) | Internal framing (moves) |
| :--- | :--- |
| "The market is terrible for juniors." | "The market is competitive, so my portfolio has to be visibly better than a bootcamp's. Here is the specific project that does that." |
| "I don't have a CS degree." | "I don't have the credential, so I need the work to speak first. My repo is the credential." |
| "I got rejected, I'm not good enough." | "I got rejected. What did the process tell me about the gap? Which module closes it?" |
| "I'll apply once I've finished the roadmap." | "I'll apply now, and use the rejections to find out which modules actually matter for the roles I want." |

The framing is not positive thinking. It is a filter that routes your attention to the variables you can act on.

## 2. Iterative job seeking — apply at ~70 % match

Job descriptions are wish-lists assembled by committee, not specifications. The observed practice among people who transition successfully is to **apply when you meet roughly 70 % of the listed requirements**, and to treat the remaining 30 % as the thing the job will teach you.

* **Apply early and continuously, not after "finishing."** Applications are a data-collection instrument, and they have a long latency. Starting them six months before you feel ready is how you find out what the real bar is while you still have time to move it.
* **Do not gate on the roadmap being complete.** By the end of [M12](#module-12) plus [M24](#module-24)'s production discipline you are already applicable to a meaningful slice of roles. See the [track table](#choose-your-track) for the minimum module set per role.
* **Track your funnel.** Applications sent → screens → technical rounds → onsites → offers. If a stage has a zero conversion rate after 20+ attempts, the problem is located at that stage and nowhere else. Resume problem, screen problem, and technical problem all look identical from the inside if you are not counting.
* **Expect a high denominator.** Video 2 (14:20) is blunt that the number of applications is measured in the hundreds, not the dozens, and that this is normal rather than a signal of failure.

## 3. Interviews as data gathering

Reframe the interview: it is the only place you get free, high-fidelity information about the gap between what you know and what the market pays for.

* **Ask what the last person in this role spent their time on.** This tells you the real job, which is frequently not the job description.
* **Ask what the team's biggest technical problem is right now.** Notice whether your roadmap covers it. If three separate companies name the same problem, that is a curriculum signal — go build a project on it.
* **Log every question you could not answer.** That log is a personalised syllabus derived from actual demand. Map each entry to a module and close it.
* **Debrief every rejection in writing.** Video 2 (16:05) treats a failed interview as a completed experiment: it cost you two hours and returned a list of specific, addressable gaps. The only wasted interview is the one you do not write up.
* **Do informational interviews too.** A 20-minute conversation with someone doing the job you want is cheaper than six months of guessing which skills matter.

## 4. Cold outreach

Cold outreach has a low response rate and an extremely high value per response, which makes it worth doing badly at volume rather than perfectly at low volume.

* **Message the practitioner, not the recruiter.** Someone doing the job can tell you what the job is; a recruiter can only tell you what the requisition says.
* **Lead with the work, not with a request.** "I built *X*, here is the repo, I noticed your team works on *Y* — did I get the hard part wrong?" outperforms "can I pick your brain."
* **Be specific and short.** Three sentences. One question that can be answered in one paragraph.
* **Ask for information, not a referral.** Referrals follow from relationships; asking for one first ends the conversation.
* **Follow up once, then stop.** Silence is usually a full inbox, not a verdict — but two follow-ups is a cost imposed on a stranger.

## 5. Build for real people, not for datasets

The strongest single differentiator in the source material. Video 2 (11:30) argues that a project built **for a real person or organisation that wanted the result** outperforms any generic dataset project, because it carries a stakeholder, a constraint, a deadline, and an outcome — the four things that make it an interview story instead of a screenshot.

Where to find real problems, in rough order of accessibility:

1. **A local non-profit, charity, or community organisation.** They have data, no analyst, and no budget. Offer one specific deliverable, not "help with data."
2. **Your current employer, in your current non-technical role.** This is the highest-conversion path in the material: you already have domain context, data access, and trust. Automate something painful, then present it.
3. **Open-source projects.** Real code, real review, a public record of collaboration, and a maintainer who will tell you when your PR is wrong.
4. **A small business you already use.** A café, a gym, a freelancer. Scope it to one week.
5. **Your own recurring annoyance.** You are a real user with real requirements — a legitimate stakeholder of one.

> **The Kaggle caveat, stated fairly.** Kaggle is genuinely excellent for learning modelling technique against a strong benchmark, and notably **zero of the 16 [surveyed 2026 postings](#skills-checklist) mention Kaggle at all**, while 15 of 16 ask for stakeholder communication. Use Kaggle to build skill; do not expect it to carry a portfolio. The competition hands you a cleaned dataset, a defined target, and a fixed metric — which is to say it removes exactly the three parts of the job that are hard.

## 6. Community and accountability

Self-directed study fails at the motivation layer far more often than at the difficulty layer. Structural fixes, in increasing order of effectiveness:

* **Publish weekly.** One post, one commit log, one paragraph on what you shipped. Public and boring beats private and ambitious.
* **Find one accountability partner** at a similar stage, with a fixed weekly check-in. Two people rarely quit in the same week.
* **Join a technical community and answer questions**, not just ask them. Explaining something badly and being corrected is the highest-bandwidth learning available for free.
* **Work in public.** Post the broken version. Video 2 (09:40) treats visible, in-progress work as both an accountability mechanism and a discovery mechanism — people cannot offer you opportunities they cannot see.
* **Beginner's mindset.** Video 2 (04:30) frames the transition from a senior non-technical role to a junior technical one as requiring you to be publicly, comfortably bad at something for a year. That is the actual cost of the transition, and it is a cost, not a personality flaw.

## 7. Honest timelines — two estimates, both with conditions

The sources disagree, and the disagreement is informative rather than a contradiction to be resolved. Both are presented with their conditions attached; pick the row whose conditions match your situation.

| Estimate | Source & conditions | What it assumes |
| :--- | :--- | :--- |
| **9–12 months to job-ready** | Scrimba's [Python guide](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) ✅ | Consistent near-full-time study; scope is **Python-centric software/data roles**, not research; you build a real portfolio; some prior technical or quantitative background. This is *"job-ready for a first junior role"*, not *"competent ML engineer."* |
| **18–36 months for a career change** | Video 2 (18:40) — a transition into Applied Science from a non-technical background | Part-time study alongside an existing job; starting with little or no programming; targeting roles with a genuine mathematical bar. 18 months is the fast case with unusual intensity; 24–30 is typical; 36 is normal with a demanding job or caregiving. |
| **24–36 months for the full roadmap** | This roadmap's own [pacing](#curriculum-at-a-glance) | Completing all 27 modules including the [full maths spine](#module-0) at ~15–20 h/week. This is the *research-capable* target, not the employability target. |

**How to reconcile them.** They measure different finish lines. Employability arrives well before completion: the [Practitioner Fast Lane](#practitioner-track) targets 6–9 months to a shippable AI-Engineer portfolio precisely by deferring the proof-level mathematics, and the full spine continues afterwards. If you are studying part-time from a non-technical background, plan for the 18–36 month band and treat the 9–12 month figure as the best case for someone with prior technical background studying near-full-time. Anyone quoting a single number without stating these conditions is selling something.

<a id="skills-checklist"></a>
## 8. Skills checklist ↔ job-description mapping

Grounded in a survey of **16 live 2026 postings** pulled from public Greenhouse job boards on **2026-07-26** — Anthropic (4), Scale AI (3), Figma (3), Databricks (2), Cloudflare (2), Discord (1), Airtable (1) — spanning AI Engineer / Forward-Deployed / Applied AI (7), ML Engineer (3), Data Scientist (4), and Data Engineer (2). Full posting list is in [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md).

**Counts below are literal mention frequencies in that sample.** The sample is small and skewed toward AI-native companies, so read it as a directional signal about *what these employers emphasise*, not as a national labour-market statistic.

> **The three findings that should change how you study.**
> 1. **Communication outranks every technical skill.** 15 of 16 postings ask for stakeholder communication, cross-functional collaboration, or customer-facing ability — more than Python (9), SQL (6), or any framework. This is why [M25](#module-25) is a required module and not an appendix.
> 2. **Evaluation is the AI-Engineer skill.** 6 of 7 AI-Engineer/Forward-Deployed postings name evaluation explicitly. Building a RAG demo is table stakes; *proving it works* is the job. See [M21](#module-21) and [M23](#module-23).
> 3. **Nobody asked for a PhD, and nobody asked about Kaggle.** 0 of 16 required a doctorate; 0 of 16 mentioned Kaggle. 5 of 16 mentioned a degree at all, most as "or equivalent experience."

### AI Engineer (Applications) — 7 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| Customer-facing communication, translating ambiguous business problems into technical scope | **7/7** | [M25](#module-25) |
| Evaluation of LLM systems — quality measurement, regression suites, benchmark design | **6/7** | [M21](#module-21) · [M23](#module-23) · [M18](#module-18) |
| Cloud platforms (AWS/GCP/Azure) and deploying into a customer's environment | 3/7 | [M24](#module-24) |
| Python as the primary implementation language | 2/7 | [M1](#module-1) |
| LLM / foundation-model application development | 2/7 | [M18](#module-18) · [M21](#module-21) |
| Agents, tool-use, multi-step workflows | 2/7 | [M22](#module-22) |
| Distributed data processing (Spark and similar) | 2/7 | [M8b](#module-8b) |
| RAG / retrieval / vector search | 1/7 | [M21](#module-21) |
| Fine-tuning and adaptation | 1/7 | [M18](#module-18) |
| Prompt design and prompt-injection awareness | 1/7 | [M22](#module-22) · [M23](#module-23) |

> **Note on the Forward-Deployed Engineer title.** 5 of the 7 postings in this family are "Forward Deployed Engineer" or "Applied AI Architect" rather than "AI Engineer." This is currently the highest-volume real title for the [AI Engineer (Applications)](#choose-your-track) role, and its defining requirement is the pairing of solid software engineering with direct customer contact — which is exactly why [M25](#module-25) sits on the critical path of that track.

### ML Engineer — 3 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| LLM / foundation-model systems in production | **3/3** | [M18](#module-18) · [M21](#module-21) |
| Agent systems and agent oversight | **3/3** | [M22](#module-22) · [M23](#module-23) |
| Python | 2/3 | [M1](#module-1) |
| RAG / retrieval infrastructure | 2/3 | [M21](#module-21) |
| Pipeline orchestration (Airflow/Dagster) | 2/3 | [M24](#module-24) · [M8b](#module-8b) |
| MLOps, monitoring, observability | 2/3 | [M24](#module-24) |
| Experimentation and A/B measurement | 2/3 | [M6½](#module-6-half) |
| Statistics, causal reasoning, regression | 2/3 | [M6](#module-6) · [M9](#module-9) |
| Evaluation pipelines | 2/3 | [M23](#module-23) |
| Stakeholder collaboration | 2/3 | [M25](#module-25) |
| Deep-learning frameworks (PyTorch) | 1/3 | [M15](#module-15) |
| Containers / Kubernetes | 1/3 | [M24](#module-24) |
| Warehouse / dbt | 1/3 | [M8a](#module-8a) |

### Data Scientist — 4 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| SQL — fluent, non-negotiable | **4/4** | [M8a](#module-8a) |
| Stakeholder communication and influencing product decisions | **4/4** | [M25](#module-25) |
| Python | **3/4** | [M1](#module-1) · [M7](#module-7) |
| Experimentation / A/B testing | **3/4** | [M6½](#module-6-half) |
| Statistical inference, causal reasoning, regression | **3/4** | [M6](#module-6) · [M6½](#module-6-half) · [M9](#module-9) |
| Warehouse / dbt / BigQuery-class tooling | **3/4** | [M8a](#module-8a) |
| LLM-related analysis | 2/4 | [M18](#module-18) |
| Large-scale data processing | 2/4 | [M8b](#module-8b) |
| Metrics definition and instrumentation | 2/4 | [M25](#module-25) |

> **The DS pattern is stable and it is not glamorous.** SQL + statistics + experimentation + communication appears in essentially every posting; deep learning appears in none of the four. If your target is Data Scientist, the highest-return modules are [M6](#module-6), [M6½](#module-6-half), [M8a](#module-8a), and [M25](#module-25) — not [M15](#module-15)–[M18](#module-18).

### Data Engineer — 2 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| SQL | **2/2** | [M8a](#module-8a) |
| Python | **2/2** | [M1](#module-1) |
| Orchestration (Airflow/Dagster/equivalent) | **2/2** | [M24](#module-24) · [M8b](#module-8b) |
| Warehouse modelling / dbt | **2/2** | [M8a](#module-8a) |
| Cross-functional partnership with DS and product | **2/2** | [M25](#module-25) |
| Streaming / event pipelines | 1/2 | [M8b](#module-8b) |
| LLM-adjacent data work | 1/2 | [M18](#module-18) |

> **Sample-size discipline.** Two postings is an anecdote, not a distribution. The Data Engineer row is included for completeness and because it agrees with the widely-observed core (SQL + Python + orchestration + modelling), but do not weight it as evidence. Before committing to any track, run this same exercise yourself on 10–15 postings **at companies you would actually join** — the mechanics are documented in [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md), take about an hour, and produce a checklist calibrated to your market rather than to this sample.

---

<a id="progress-tracker"></a>
# ✅ Progress Tracker

> Fork this repo, copy this section, and replace `[ ]` with `[x]` as you complete each sub-module.

### 🧭 Route selection (do this first)
- [ ] Read [Start here](#start-here) and picked a route: **full spine** or [**🚀 Practitioner fast lane**](#practitioner-track)
- [ ] Chose a target role from [Choose your track](#choose-your-track) and wrote down its minimum module set
- [ ] Read the [module-project enforcement rule](#module-projects) and accepted it
- [ ] Read [Career Operations §7](#career-operations) and picked the timeline band whose **conditions** match my situation

### 🩺 Math-Foundations Diagnostic
- [ ] Took the **15-question diagnostic** and recorded my score per strand
- [ ] Decided whether to do **Module 0** (mandatory if any strand < 70%)

### 🟩 Foundation Stratum
- [ ] **Module 0a**: Pre-Calculus & Trigonometry (Khan Academy / MIT 18.01A)
- [ ] **Module 0b**: Logic, Proof & Discrete-Math Primer (Hammack + Velleman + MIT 6.042J; optional: Lean 4 first proof)
- [ ] **Module 1**: Programming Foundations (CS50P + MIT 6.0001/6.0002)
- [ ] **Module 2**: Calculus + Matrix Calculus + Convex Optimisation (MITx 18.01.1/2/3x + 18.02 + **MIT 18.S096/063 Matrix Calc** + **Stanford EE364A Boyd**)
- [ ] **Module 3**: Linear Algebra — Computational + Abstract + Applications (MIT 18.06 + 3Blue1Brown + **Axler 4e 2024** + Townsend 2024 + Trefethen/Bau)
- [ ] **Module 4**: DSA (MIT 6.006 + GaTech series)
- [ ] **Module 5**: Probability + Concentration + Information Theory + Measure Bridge (Stat 110 + MITx 6.431x + **Stanley Chan 2021** + **MacKay 2003** + **Vershynin 2018**)

### 🟨 Core Statistics Stratum
- [ ] **Module 6**: Inference (MITx 18.6501x + STAT 111)
- [ ] **Module 6½**: Causal Inference & Experimentation (Brady Neal + MIT 14.387 + Kohavi + DoWhy)
- [ ] **Module 7**: EDA & Viz (CS109A Lec 1-2, 9, 12-13 + Polars/DuckDB modernisation)
- [ ] **Module 8a**: Databases, SQL & Warehouses (IITM BSCS2001 + Kimball + dbt Learn)
- [ ] **Module 8b**: Distributed Data & Streaming (Stanford CS246 + DataExpert.io + Reis & Housley + Spark + Kafka + Airflow + Iceberg)

### 🟧 Classical ML Stratum
- [ ] **Module 9**: Regression (MIT 6.390 Lec 1-3, CS109A Lec 3-6)
- [ ] **Module 10**: Classification & SVMs + Calibration (MIT 6.390 Lec 4, CS109A Lec 14-15, CS 1810, Cambridge ML&BI + Platt/Isotonic/Temperature scaling)
- [ ] **Module 11**: Unsupervised (CS109A Lec 10, CS109B Lec 1-2, MIT 6.86x Unit 4)
- [ ] **Module 12**: Ensembles (CS109A Lec 16-20)

### 🟦 Probabilistic Stratum
- [ ] **Module 13**: Bayes + MCMC (CS109B Lec 3-7, Cambridge ML&BI, MIT 6.790 Part III; PyMC 5.28 + NumPyro 0.20)
- [ ] **Module 14**: HMMs & Time Series + Foundation Models (Cambridge MLRD Topic 2, MITx 14.310x; + Prophet/TimeGPT/Chronos/Lag-Llama)

### 🟪 Deep Learning Stratum
- [ ] **Module 15**: DL Foundations + JAX/FSDP/Mixed-Precision (CS109B Lec 8–15, MIT 6.390 Lec 5–7, **MIT 6.7960 Fall 2025 W1–4**, **MIT 6.S191 2026**, **Google Scaling Book**)
- [ ] **Module 16**: Transformers + ViT + Diffusion + SSMs + MoE (CS109B Lec 16–23, **MIT 6.7960 Fall 2025 W4‑11**, MIT 6.390 Lec 9, **Stanford CS336 Lec 3–4, 6**; DINOv2/SAM 2/LLaVA/Mamba)
- [ ] **Module 17**: RL + Modern LLM RL (MIT 6.390 Lec 10–11, IITM BSCS3003, **Stanford CS336 Lec 15–17 RLVR**, CleanRL, Berkeley CS285, Spinning Up)

### 🔴 Frontier / Production Stratum
- [ ] **Module 18**: LLMs & Fine-Tuning Playbook (**Stanford CS336 Spring 2026**, IITM BSCS3004, MIT 6.7960 W8–13, **HF Agents Course**, **MCP Nov 2025 spec**, Unsloth/Axolotl/TRL/PEFT/DSPy/vLLM/SGLang)
- [ ] **Module 21**: RAG + Vector DBs (Pinecone Learn + LlamaIndex + pgvector + Qdrant + Ragas)
- [ ] **Module 22**: Agentic AI — LangGraph/CrewAI/MCP/A2A (HF Agents Course + Berkeley LLM Agents + Anthropic Building Effective Agents + GAIA + SWE-bench)
- [ ] **Module 23**: AI Safety + Interpretability + Evals + Policy (AISF Alignment Fundamentals + Transformer Circuits + EU AI Act + NIST AI RMF + inspect-ai)
- [ ] **Module 24**: MLOps + LLMOps + AgentOps (Harvard AC215, Chip Huyen AI Engineering, FSDL, Made With ML, Langfuse/LangSmith/Phoenix/Weave)
- [ ] **Module 25**: Product DS · Communication · Decision Intelligence (Kozyrkov + Kohavi Trustworthy Experiments + Storytelling with Data + CMU MSPPM-DA / UMich MADS)

### 📦 Module projects (one public repo each — see [the rule](#module-projects))
- [ ] **M1** Weather CLI · **M2** gradient-descent lab · **M3** five linear-algebra mini-projects · **M4** constraint meal planner · **M5** Monte Carlo lab
- [ ] **M6** inference toolkit · **M6½** causal mini-projects · **M7** end-to-end EDA · **M8a** Reddit scraper → warehouse · **M8b** streaming mini-projects
- [ ] **M9** regression from scratch · **M10** churn dashboard + `LogisticRegressionScratch` · **M11** K-Means from scratch · **M12** decision tree from scratch + boosting bake-off
- [ ] **M13** Bayesian A/B · **M14** forecasting dashboard with backtest · **M15** backprop from scratch + CNN · **M16** HF sentiment analyser + transformer from scratch · **M17** RL agent over 5 seeds
- [ ] **M18** fine-tune + four-way eval · **M21** RAG mini-projects · **M22** agent mini-projects · **M23** safety mini-projects · **M24** productionise one project · **M25** product-DS mini-projects
- [ ] At least **one** project satisfies all 12 lines of the [Minimum Production Bar](#production-bar)
- [ ] At least **one** project was built **for a real person or organisation** ([why](#career-operations))

### 🧭 Career Operations
- [ ] Ran my own [job-description survey](#skills-checklist) on 10–15 postings at companies I would actually join
- [ ] Built my per-track [skills checklist](#skills-checklist) and mapped each gap to a module
- [ ] Started applying at ~70 % match and began tracking the funnel (applications → screens → technicals → onsites)
- [ ] Wrote up my first rejection as a completed experiment
- [ ] Have an accountability partner or public weekly log

### 🏆 Capstone Stratum
- [ ] **Module 26**: Capstone Project — Choose **1 of 3 tracks**: Research / Systems / Applied (arXiv preprint + HF release + MCP‑compliant tool/agent OR production system with SLOs OR stakeholder-sponsored applied project with causal evaluation)

---

<a id="refresh-log"></a>
# 🗓️ Refresh Log

Each pass records what changed, what was verified, and what was deliberately left alone. Full HTTP status logs live in [`audit/VERIFICATION.md`](audit/VERIFICATION.md); per-pass reports live in [`audit/`](audit/).

### v2026.3 — Practitioner's Pass · 2026-07-30

**Diagnosis addressed:** the curriculum was academically strong but theory-first and intimidating — no practitioner entry point, no enforced project-per-module, no career-reality layer, and no distinct "AI Engineer (Applications)" identity of the kind the 2026 market hires for.

| Workstream | Change | Primary evidence |
| :-- | :--- | :--- |
| **A** | [🚀 Practitioner Track (Fast Lane)](#practitioner-track) — a sequenced 6-stage / 6–9-month path; the [track table](#choose-your-track) split into **AI Engineer (Applications)** and **AI Engineer (Systems/Research-adjacent)**; ⚡ **Intuition-First Alternative** callouts added to [M0](#module-0), [M2](#module-2), [M3](#module-3), [M5](#module-5), each stating what you give up and when to come back | Video 1 (00:44–01:09, 03:00–07:15); video 3 (00:53, 04:47) |
| **B** | [Module 1](#module-1) rebuilt around a four-phase pacing structure with ship-milestones, a [free Python course matrix](#python-course-matrix) (8 courses), the recommended pairing stack, the **tutorial-hell escape protocol**, and a disciplined AI-assistant policy naming the **fluency illusion** | Both Scrimba articles; video 1 (03:00–04:00, 09:30); video 3 (01:21) |
| **C** | [Module-project enforcement rule](#module-projects) + **18 new 📦 Module Project blocks** so every module M1–M25 now carries a mandatory deliverable with tests, README, and a results memo | Video 1 (05:40–06:05, 10:45–14:05); video 2 (11:30) |
| **D** | [🧭 Career Operations](#career-operations) appendix and the [skills ↔ job-description mapping](#skills-checklist) grounded in **16 live 2026 postings** | Video 2 (04:30–18:40); 16 Greenhouse postings, surveyed 2026-07-26 |
| **E** | [🧰 Practitioner Shelf](#practitioner-shelf) — the applied seven-book canon added alongside (not instead of) the Tier 1 academic spine | Video 3 (full); publisher/author pages |
| **F** | [Minimum Production Bar](#production-bar) (12 items) in M24 + toolchain; the [prompting vs RAG vs fine-tuning ladder](#module-21) in M21; prompt-injection security and agent eval pipelines promoted to first-class topics in [M22](#module-22); Streamlit added and agent-framework pins refreshed in the [toolchain](#toolchain) | Video 1 (07:15, 10:45–12:30); video 3 (05:52); surveyed postings (evaluation in 6/7 AI-Eng roles) |
| **G** | Audit trail, TOC, progress tracker, version badge, `coursepages/` sync, and this log | [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md) |
| **H** | **Visual pass** — a hero banner, a six-stratum journey infographic, and a section banner for each stratum, all in one consistent dark-navy visual language. Every asset is licence-clean: two are model-generated originals, six are rendered deterministically by [`assets/make_banners.py`](assets/make_banners.py), which is committed so any banner can be regenerated or restyled. No third-party or stock imagery is used. Provenance in [`assets/README.md`](assets/README.md) | Trailing brief instruction to match the presentation quality of [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) |

**Sources consumed in full**

* **Video 1** — [How to Become an ML Engineer](https://www.youtube.com/watch?v=UZ_rK9gzVSc) (Senior Applied Scientist, Twitch) — five-phase practical path, from-scratch NumPy discipline, portfolio architecture standard, the fluency illusion, project archetypes.
* **Video 2** — [Breaking into AI/ML from a non-technical background](https://www.youtube.com/watch?v=FeQZmQMffzc) (Applied Scientist, Amazon) — internal locus of control, real-projects-for-real-organisations, interviews-as-data, realistic transition windows.
* **Video 3** — [The Only 7 Books You Need to Become an AI Engineer](https://www.youtube.com/watch?v=Pr9oRVtAqCM) (ex-Coursera / ex-Amazon) — the AI Engineer role definition, intuition-over-derivation, notebook-to-production progression, the seven-book canon.
* **Article 1** — [Scrimba: Best Free Python Courses for Beginners in 2026](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/) ✅
* **Article 2** — [Scrimba: How to Learn Python — A Beginner's Guide (2026)](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) ✅
* **Job market** — 16 live postings from public Greenhouse boards (Anthropic, Scale AI, Figma, Databricks, Cloudflare, Discord, Airtable), surveyed 2026-07-26. Enumerated in [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md).

**Verification summary:** 70 URLs HTTP-checked · **66 ✅ 200** · **3 ⚠️ 403** (bot-gated, browser-accessible: two O'Reilly product pages, BLS) · **0 ❌ dead links shipped**. Four candidate URLs were found broken during research and are **not** in the README: two No Starch Manga Guide path guesses, the per-title StatQuest URLs, and `bytebytego.com/courses/generative-ai-system-design-interview`. Framework versions re-pulled from the PyPI JSON API on 2026-07-30.

**Corrections made to previously-published claims** (found while verifying, not part of any workstream's remit):

| Location | Was | Verified actual | Evidence |
| :-- | :--- | :--- | :--- |
| M1 Required Reading | _Fluent Python_ "3rd Edition, 2025" | **2nd Edition (2022)**; a 3rd edition is not published | [fluentpython.com](https://www.fluentpython.com/) ✅ states "Fluent Python, Second Edition"; matches Tier 1 row 20 |
| M1 Required Reading | _Python Crash Course_ "4th Edition, 2025" | **3rd Edition**; no 4th edition exists | [No Starch catalogue](https://nostarch.com/python-crash-course-3rd-edition) ✅ lists 3rd Ed. as current |
| Practitioner Shelf P7 | Source video credits Alex Xu & Sahn Lam | **Alex Xu, Ali Aminian, Hao Sheng** | [Publisher announcement](https://blog.bytebytego.com/p/our-new-book-generative-ai-system) ✅ |
| Toolchain agents row | smolagents 1.24.0 · LangGraph 1.1.9 | **smolagents 1.26.0 · LangGraph 1.2.10** | PyPI JSON API, 2026-07-30 |

**Deliberately not changed:** the Tier 1 / Tier 2 reading lists, the module numbering scheme (including the M6½ and M8a/M8b splits and the M19/M20 gap), and the mathematical content of M0, M2, M3, M5, M9–M12, M13, and M15. The practitioner doctrine is added **alongside** the academic spine as a labelled alternative route, never as a replacement — where the two conflict, both are stated with their conditions.

### v2026.2 and earlier

See [`audit/FINAL_AUDIT.md`](audit/FINAL_AUDIT.md), [`audit/VERIFICATION.md`](audit/VERIFICATION.md), and [`audit/IMPROVEMENT_SPEC.md`](audit/IMPROVEMENT_SPEC.md) for the P1–P5 verification passes that established the 27-module structure, the free-first resource policy, and the link-verification conventions (✅ live · ⚠️ bot-gated · ❌ dead · 🔁 fixed-with-alternative) used throughout.

---

<a id="acknowledgements"></a>
# 🙏 Acknowledgements & Attribution

This curriculum synthesises publicly-available syllabi from:

* **IIT Madras** — [study.iitm.ac.in/ds](https://study.iitm.ac.in/ds/) (BS in Data Science and Applications, 2025–26).
* **Harvard University** — [harvard-iacs.github.io](https://harvard-iacs.github.io/) (CS 109A/B), [stat110.hsites.harvard.edu](https://stat110.hsites.harvard.edu/) (STAT 110), [harvard-ml-courses.github.io/cs181-web/](https://harvard-ml-courses.github.io/cs181-web/) (CS 1810, Spring 2026), [cs50.harvard.edu/python](https://cs50.harvard.edu/python/) (CS50P).
* **Massachusetts Institute of Technology** — [introml.mit.edu/spring26](https://introml.mit.edu/spring26) (6.390), [gradml.mit.edu](https://gradml.mit.edu/) (6.790), [**deeplearning6-7960.github.io**](https://deeplearning6-7960.github.io/) (6.7960 Fall 2025), [introtodeeplearning.com](https://introtodeeplearning.com/) (6.S191 2026), [micromasters.mit.edu/ds](https://micromasters.mit.edu/ds/) (Statistics & Data Science MicroMasters), [visionbook.mit.edu](https://visionbook.mit.edu/) (Foundations of Computer Vision 2024), [ocw.mit.edu](https://ocw.mit.edu/) (18.01/18.02/18.06/6.0001/6.0002/6.006), [ocw.mit.edu/14-387](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) (14.387 Applied Econometrics).
* **University of Cambridge** — [cl.cam.ac.uk/teaching/2526](https://www.cl.cam.ac.uk/teaching/) (Part IA/IB/II), [mlmi.eng.cam.ac.uk](https://www.mlmi.eng.cam.ac.uk/) (MPhil MLMI 2026 entry).
* **Stanford University** — [cs336.stanford.edu](https://cs336.stanford.edu/) (Language Modeling from Scratch, Spring 2026) · [cs246.stanford.edu](https://web.stanford.edu/class/cs246/) (Mining Massive Datasets) · [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/) (SLP 3rd ed. draft) · [web.stanford.edu/class/ee364a](https://web.stanford.edu/class/ee364a/) (Convex Optimization).
* **UC Berkeley** — [ischool.berkeley.edu/courses/datasci/241](https://www.ischool.berkeley.edu/courses/datasci/241) (MIDS Causal Inference — anchor for M6½) · [rail.eecs.berkeley.edu/deeprlcourse](https://rail.eecs.berkeley.edu/deeprlcourse/) (CS285 Deep RL) · [llmagents-learning.org](https://llmagents-learning.org/) (LLM Agents MOOC — anchor for M22).
* **CMU / UMich (Product-DS anchors)** — [heinz.cmu.edu](https://www.heinz.cmu.edu/programs/public-policy-management-master/data-analytics) (MSPPM-DA) · [si.umich.edu](https://www.si.umich.edu/programs/master-applied-data-science) (MADS).
* **Hugging Face** — [huggingface.co/learn](https://huggingface.co/learn) (Agents Course, Smol Course, Smol Training Playbook).
* **Microsoft** — [Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) and [ML for Beginners](https://github.com/microsoft/ML-For-Beginners), used as project-based companion curricula with quizzes, assignments, and guided lesson navigation.
* **Anthropic / MCP Consortium** — [modelcontextprotocol.io](https://modelcontextprotocol.io/) (Nov 2025 spec) · [transformer-circuits.pub](https://transformer-circuits.pub/) (mechanistic interpretability research).

All university material remains © their respective institutions; this repository only cites and organises publicly‑disclosed syllabi.

**Images.** All artwork in [`assets/`](assets/) is original to this repository and carries no third-party licence obligation. `hero-banner.jpg` and `roadmap-overview.jpg` are AI-generated originals; the six `stratum-*.jpg` section banners are drawn programmatically by [`assets/make_banners.py`](assets/make_banners.py) (Pillow only, deterministic — re-run it to regenerate or restyle them). No stock photography, no commercially-licensed imagery, and no images scraped from third-party pages are used anywhere in this repository. See [`assets/README.md`](assets/README.md).

---

<div align="center">

**Learn the foundations. Build the systems. Show the work.**

Maintained as a free-first curriculum · [CC BY-SA 4.0](LICENSE.md) · Corrections and resource updates are welcome

</div>
