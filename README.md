<div align="center">

<img src="assets/hero-banner.jpg" alt="Data Science and AI Roadmap - foundations to production AI" width="100%">

# Data Science & AI Roadmap

### A rigorous, free-first path from foundations to production AI

[![Version](https://img.shields.io/badge/version-2026.5%20Clear%20Path-blue)](CHANGELOG.md#refresh-log)
[![Modules](https://img.shields.io/badge/modules-27-6f42c1)](curriculum/README.md)
[![Level](https://img.shields.io/badge/level-beginner%20to%20advanced-0969da)](#who-this-is-for)
[![Cost](https://img.shields.io/badge/required%20resources-free-1a7f37)](FAQ.md#basics)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-lightgrey)](LICENSE.md)

**A free self-study plan for data science and AI — from mathematics to production systems.**

</div>

> ### 👉 New here? Read **[START-HERE.md](START-HERE.md)** first. It takes five minutes and tells you exactly what to do on day one.

---

## What this is (in 30 seconds)

This repository is a **study plan written in Markdown**. It tells you which free courses to take, which
books to read, and which projects to build — in an order where nothing depends on something you have not
learned yet.

| ❓ | Answer |
| :--- | :--- |
| **Is there software to install?** | **No.** There is no code to run and nothing to `pip install` here. |
| **What do I do with it, then?** | Open one module. Take the one course it names. Build the one project it names. Repeat. |
| **What does it cost?** | Every required resource is free. Optional books are labelled as optional. |
| **How long?** | 6–9 months to employable on the [fast lane](guides/practitioner-track.md); 24–36 months for the complete path. [Details](FAQ.md#how-long). |
| **Do I need all 27 modules?** | **No.** [Pick a track](#choose-your-track) and do that track's modules. |

**The method, in one line:** one course + one book + one public project per module, in prerequisite order.

> ⚠️ **The one mistake to avoid.** Each module lists many resources. That is a **menu, not a to-do
> list** — it exists so the curriculum still works if a link dies or a course doesn't suit you. Pick
> *one* course per module. The [Pick-One table](guides/how-to-read-a-module.md#pick-one) has already
> chosen a default for all 27 modules if you'd rather not decide.

## Where to go next

| If you are… | Go here |
| :--- | :--- |
| **Brand new to this repo** | 🧭 **[START-HERE.md](START-HERE.md)** — a four-day plan and one decision |
| Confused by a module's length or link count | 📖 [How to read a module](guides/how-to-read-a-module.md) |
| Wondering why modules skip 19 and 20, or other oddities | ❓ [FAQ](FAQ.md) |
| Aiming at a job as fast as defensibly possible | 🚀 [Practitioner fast lane](guides/practitioner-track.md) |
| Ready to browse the whole thing | 📚 [Curriculum index](curriculum/README.md) |
| Tracking your own progress | ✅ [Progress tracker](guides/progress-tracker.md) |

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

1. **Take the [math diagnostic](curriculum/1-foundations.md#math-diagnostic).** Complete Module 0 if any foundation is weak.
2. **Choose a destination** in the role-track table below instead of studying everything by default.
3. **Respect prerequisites.** Each module states what you should know before starting.
4. **Use one primary course and one primary book** — the [Pick-One table](guides/how-to-read-a-module.md#pick-one) names a default for every module. Treat the remaining links as alternatives or references.
5. **Build every mandatory project.** Passive course completion is not enough.
6. **Track your work** with the [progress checklist](guides/progress-tracker.md#progress-tracker).
7. **Finish with a capstone** that matches your intended role.

<a id="start-here"></a>
## Entry points by experience

> **First visit?** Use **[START-HERE.md](START-HERE.md)** instead of this table — it gives you one
> decision and a four-day plan. The table below is for when you already know how the repo works and
> just want the module sequence for your background.

Use the shortest entry point that matches your current experience. You can return to the full curriculum whenever you need more depth.

| If you are... | Start with | Then continue to |
|---|---|---|
| **New to programming and data** | [Microsoft Data Science for Beginners](guides/companion-curricula.md#companion-curricula), then [M1](curriculum/1-foundations.md#module-1) | [M5](curriculum/1-foundations.md#module-5) → [M6](curriculum/2-statistics-and-data.md#module-6) → [M7](curriculum/2-statistics-and-data.md#module-7) → [M8a](curriculum/2-statistics-and-data.md#module-8a) |
| **Comfortable with Python, new to ML** | [Microsoft ML for Beginners](guides/companion-curricula.md#companion-curricula) alongside [M9](curriculum/3-classical-ml.md#module-9) | M9 → [M10](curriculum/3-classical-ml.md#module-10) → [M11](curriculum/3-classical-ml.md#module-11) → [M12](curriculum/3-classical-ml.md#module-12) |
| **An analyst moving into data science** | [M5](curriculum/1-foundations.md#module-5) → [M6](curriculum/2-statistics-and-data.md#module-6) → [M7](curriculum/2-statistics-and-data.md#module-7) | [M9](curriculum/3-classical-ml.md#module-9) → [M14](curriculum/4-probabilistic-ml.md#module-14) → [M25](curriculum/6-frontier-production.md#module-25) |
| **An ML practitioner moving into production AI** | [M8b](curriculum/2-statistics-and-data.md#module-8b) and [M24](curriculum/6-frontier-production.md#module-24) | [M18](curriculum/6-frontier-production.md#module-18) → [M21](curriculum/6-frontier-production.md#module-21) → [M22](curriculum/6-frontier-production.md#module-22) → [M23](curriculum/6-frontier-production.md#module-23) |
| **Preparing for research** | [Math diagnostic](curriculum/1-foundations.md#math-diagnostic) | Follow M0–M18 in order, then [M23](curriculum/6-frontier-production.md#module-23) and the [research capstone](curriculum/6-frontier-production.md#module-26) |

> **First milestone:** complete one small project before collecting more resources. The [Microsoft companion courses](guides/companion-curricula.md) supply guided lessons, quizzes, assignments, and solutions; this roadmap supplies the deeper prerequisite and production sequence.


## Choose your track

| Track | Recommended modules | Portfolio outcome |
|---|---|---|
| **Data Analyst** | M1 → M6 → M7 → M8a → M25 → M26 | Reproducible analysis, dashboard, and stakeholder memo |
| **Data Scientist** | M1–M7 → M9–M14 → M25 → M26 | Validated model plus causal or experimental evaluation |
| **Data Engineer** | M1 → M4 → M7 → M8a → M8b → M24 → M26 | Tested batch/streaming data platform with observability |
| **ML Engineer** | M1–M12 → M15–M17 → M24 → M26 | Model served behind an API with CI, monitoring, and SLOs |
| **AI Engineer (Applications)** | [Fast lane](guides/practitioner-track.md#practitioner-track): M1 → M7 → M8a → intuition-level M2/M3/M5 → M18 → M21–M24 → M26 | Deployed product built **on** a foundation model: RAG or agent system with an eval suite, tracing, guardrails, and a cost/latency budget |
| **AI Engineer (Systems/Research-adjacent)** | M1 → M8a → M15–M18 → M21–M24 → M26 | Evaluated RAG or agent system with tracing and guardrails, plus architecture-level understanding of the models it serves |
| **Research / PhD prep** | M0–M18 → M23 → M26 Research Track | Reproducible paper, ablations, and public research artifact |

> **Reading the two AI Engineer rows.** They are different jobs, not seniority levels. The **Applications** row matches the role as defined in [video 3](guides/sources.md#citation-key), 00:53: a software engineer who turns GPT/Claude/Llama into products via prompting, RAG, fine-tuning, and agents, and who does *not* train models from scratch. Its primary text is **Chip Huyen, _AI Engineering: Building Applications with Foundation Models_** (O'Reilly, Jan 2025 — see the [Practitioner Shelf](resources/books.md#practitioner-shelf)). The **Systems** row keeps the deep-learning spine (M15–M17) for people who must also reason about the model internals, not just the API surface. In our [survey of 16 live 2026 postings](guides/career-operations.md#skills-checklist), titles for the Applications row appear as "AI Engineer", "Applied AI Architect", and "Forward Deployed Engineer (GenAI)".

<a id="roadmap"></a>
## 🗺️ Where everything lives

The curriculum is split into focused pages so you never scroll through 2,000 lines again. Pages are
grouped below by **when you need them** — you are not expected to read the bottom group at all.

### Read these first

| Page | What you will find there |
|---|---|
| 🧭 [**START-HERE**](START-HERE.md) | What this repo is, one decision, and a four-day plan |
| 📖 [How to read a module](guides/how-to-read-a-module.md) | Module anatomy + the **Pick-One table**: one default resource per module |
| ❓ [FAQ](FAQ.md) | Why modules skip 19/20, how long it takes, what the symbols mean |
| 📚 [Curriculum index](curriculum/README.md) | All 27 modules across six strata, plus the module-project enforcement rule |

### The curriculum itself

| Page | What you will find there |
|---|---|
| 🟩 [1 · Foundations](curriculum/1-foundations.md) | Math diagnostic · M0–M5: proof, Python, calculus, linear algebra, algorithms, probability |
| 🟨 [2 · Statistics & Data](curriculum/2-statistics-and-data.md) | M6–M8b: inference, causal inference, EDA, SQL, distributed data |
| 🟧 [3 · Classical ML](curriculum/3-classical-ml.md) | M9–M12: regression, classification, unsupervised, ensembles |
| 🟦 [4 · Probabilistic ML](curriculum/4-probabilistic-ml.md) | M13–M14: Bayesian inference, MCMC, time series |
| 🟪 [5 · Deep Learning](curriculum/5-deep-learning.md) | M15–M17: MLPs/CNNs, transformers, generative models, RL |
| 🔴 [6 · Frontier & Production](curriculum/6-frontier-production.md) | M18, M21–M26: LLMs, RAG, agents, safety, MLOps, product, capstone |

### Guides and reference — when you need them

| Page | Open it when… |
|---|---|
| 🚀 [Practitioner Track (fast lane)](guides/practitioner-track.md) | You want the 6–9-month employment-first sequence, trade-offs stated |
| 🤝 [Companion curricula](guides/companion-curricula.md) | You are a beginner and want guided lessons alongside M1–M14 |
| ✅ [Progress tracker](guides/progress-tracker.md) | You have forked the repo and want to tick modules off |
| 🧭 [Career Operations](guides/career-operations.md) | You are ready to apply for jobs |
| 📖 [Books](resources/books.md) | You need a specific book — your module already names the one to use |
| 🛠️ [Toolchain](resources/toolchain.md) | You reach M8 or start deploying. A dated snapshot, not a shopping list |
| 🔗 [Sources](guides/sources.md) | You see a citation like "Video 1 (05:05)" and want to resolve it |
| 📂 [Course pages](coursepages/) | You reach M6½, M8b, or M21–M25 and want the extra scaffolding |

### Maintainer material — safe to ignore as a learner

| Page | Purpose |
|---|---|
| 🗓️ [Changelog](CHANGELOG.md) | Versioned refresh log with what changed and why |
| 🔍 [Audit trail](audit/) | Link-verification and fact-checking logs backing every claim |
| 🔧 [Tools](tools/) | The internal link checker |
| 🤝 [Contributing](CONTRIBUTING.md) | How to report a dead link or propose a resource change |
| 📜 [Code of conduct](CODE_OF_CONDUCT.md) | Contributor Covenant v2.1 |

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

> **Guided companions:** the [Microsoft Data Science / ML for Beginners pairing](guides/companion-curricula.md) supplies lesson-by-lesson beginner material that maps onto these modules.

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
