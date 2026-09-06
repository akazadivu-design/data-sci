[🏠 Roadmap home](../README.md) · [🧭 Start here](../START-HERE.md)

---

# 📖 How to read a module

Every module in this curriculum has the same seven parts. Once you know what they are, a module that
looked like a wall of links becomes a short checklist.

**The single most important thing on this page:** most of a module's length is a *menu of alternatives*,
not a list of things you must do. If you try to complete every resource listed in a module, you will
never finish one. That is the mistake this page exists to prevent.

---

## The anatomy of a module

Modules are long because they are *reference* documents — you read the relevant part, not all of it.
Here is what each part is for and whether you must act on it.

| Part | What it is | Must you do it? |
| :--- | :--- | :--- |
| **The Tutor's "Why"** | One paragraph on why this module exists and what breaks later if you skip it. | **Read it.** 30 seconds. It tells you whether you can skip the module. |
| **Strict Prerequisites** | Which earlier modules you need first. | **Check it.** If you don't have them, go back. This is the one rule that prevents silent failure. |
| **Exhaustive Topic List** | Every topic the module covers, tagged with the university lecture it comes from (e.g. `[MIT 6.390 · Lec 2]`). | **No — do not work through this.** It is a **syllabus checklist**, used two ways: (1) to confirm your chosen course covers the topics, and (2) as a revision list before interviews. |
| **2026 Resources** | Courses, books, and tools. Split into *Primary* and everything else. | **Only the primary one.** See below. |
| **⚡ Intuition-First Alternative** | A shorter route through the module for people who want to build rather than prove, with the trade-off stated. | Optional. Only on the maths-heavy modules. |
| **📦 Module Project** | The deliverable, its definition of done, and one stretch goal. | **Yes. This is the part that counts.** |
| **Suggested Pace / Sequencing** | A week-by-week plan. | Guidance only. Adjust to your own hours. |

> **Rule of thumb.** A module is done when its **project is public** — not when you have read every
> line of it. Nobody reads the exhaustive topic list end to end, including the people who wrote it.

---

## Which resource do I actually pick?

Inside **2026 Resources** you will see up to four labels. Treat them like this:

| Label | Meaning | Action |
| :--- | :--- | :--- |
| **Primary Course Link** | The one course the module is built around. If several are listed separated by `·`, **the first is the default**. | Take **one**. |
| **Required Reading** | Reference texts. You look things up in them; you do not read them cover to cover. | Own or bookmark **one**. Read the named chapters only. |
| **Practical Implementation** | The libraries you will actually type. | Install as needed. |
| **Alternative / Companion** | Backups for when the primary does not click. | Ignore until the primary fails you. |

### Why so many links then?

Because learners arrive with different backgrounds, budgets, and tolerances for mathematics — and
because links rot. Listing three courses per topic means the module still works in two years and still
works for someone who cannot follow the default. **The cost of that robustness is that you must
choose.** The table below chooses for you.

---

<a id="pick-one"></a>
## 🎯 The Pick-One table — one default resource per module

If you do not want to think, use this column. Every entry is free to access. These are the defaults;
each module lists alternatives if a default does not suit you.

### 🟩 Foundations

| Module | Take this one course | Then build |
| :--- | :--- | :--- |
| [M0](../curriculum/1-foundations.md#module-0) Maths bridge | [Book of Proof](https://richardhammack.github.io/BookOfProof/) for 0b; [Khan Precalculus](https://www.khanacademy.org/math/precalculus) or [OpenStax](https://openstax.org/details/books/precalculus-2e) only if 0a needs repair | [Reasoning Evidence Pack + exit gate](../curriculum/1-foundations.md#m0-project); exempt/deferred routes are labelled in M0 |
| [M1](../curriculum/1-foundations.md#module-1) Python | [Harvard CS50P](https://cs50.harvard.edu/python/) | Weather CLI |
| [M2](../curriculum/1-foundations.md#module-2) Calculus | [MIT 18.01 / MITx 18.01.1x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.1x/) | Gradient-descent lab |
| [M3](../curriculum/1-foundations.md#module-3) Linear algebra | [MIT 18.06 SC](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/) | 5 linear-algebra minis |
| [M4](../curriculum/1-foundations.md#module-4) Algorithms | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | Meal planner |
| [M5](../curriculum/1-foundations.md#module-5) Probability | [Harvard Stat 110](https://stat110.hsites.harvard.edu/) | Monte Carlo lab |

### 🟨 Statistics & Data

| Module | Take this one course | Then build |
| :--- | :--- | :--- |
| [M6](../curriculum/2-statistics-and-data.md#module-6) Inference | [MITx 18.6501x](https://www.edx.org/course/fundamentals-of-statistics) | Inference toolkit |
| [M6½](../curriculum/2-statistics-and-data.md#module-6-half) Causal | [Brady Neal — Causal Inference](https://www.bradyneal.com/causal-inference-course) | Causal minis |
| [M7](../curriculum/2-statistics-and-data.md#module-7) EDA | [Harvard CS109A](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) | End-to-end EDA |
| [M8a](../curriculum/2-statistics-and-data.md#module-8a) SQL | [Stanford CS145](https://web.stanford.edu/class/cs145/) | Scraper → warehouse |
| [M8b](../curriculum/2-statistics-and-data.md#module-8b) Distributed | [Stanford CS246](https://web.stanford.edu/class/cs246/) | Streaming minis |

### 🟧 Classical ML

| Module | Take this one course | Then build |
| :--- | :--- | :--- |
| [M9](../curriculum/3-classical-ml.md#module-9) Regression | [MIT 6.390](https://introml.mit.edu/spring26/lectures/lec01) | Regression from scratch |
| [M10](../curriculum/3-classical-ml.md#module-10) Classification | [MIT 6.390 Lec 4](https://introml.mit.edu/spring26/lectures/lec04) | Churn dashboard |
| [M11](../curriculum/3-classical-ml.md#module-11) Unsupervised | [Harvard CS109B](https://harvard-iacs.github.io/2022-CS109B/) | K-Means from scratch |
| [M12](../curriculum/3-classical-ml.md#module-12) Ensembles | [Harvard CS109A Lec 16–20](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) | Decision tree from scratch |

### 🟦 Probabilistic ML

| Module | Take this one course | Then build |
| :--- | :--- | :--- |
| [M13](../curriculum/4-probabilistic-ml.md#module-13) Bayesian | [Harvard CS109B Bayes lectures](https://harvard-iacs.github.io/2022-CS109B/) | Bayesian A/B test |
| [M14](../curriculum/4-probabilistic-ml.md#module-14) Time series | [Cambridge MLRD](https://www.cl.cam.ac.uk/teaching/2324/MLRD/) | Forecast + backtest |

### 🟪 Deep Learning

| Module | Take this one course | Then build |
| :--- | :--- | :--- |
| [M15](../curriculum/5-deep-learning.md#module-15) DL foundations | [MIT 6.7960](https://deeplearning6-7960.github.io/) | Backprop from scratch |
| [M16](../curriculum/5-deep-learning.md#module-16) Transformers | [MIT 6.7960 wks 4–11](https://deeplearning6-7960.github.io/) | Transformer from scratch |
| [M17](../curriculum/5-deep-learning.md#module-17) RL | [MIT 6.390 Lec 10–11](https://introml.mit.edu/spring26/) | RL agent, 5 seeds |

### 🔴 Frontier & Production

| Module | Take this one course | Then build |
| :--- | :--- | :--- |
| [M18](../curriculum/6-frontier-production.md#module-18) LLMs | [Stanford CS336](https://cs336.stanford.edu/) | Fine-tune + eval |
| [M21](../curriculum/6-frontier-production.md#module-21) RAG | [Pinecone Learn](https://www.pinecone.io/learn/) | RAG minis |
| [M22](../curriculum/6-frontier-production.md#module-22) Agents | [HF Agents Course](https://huggingface.co/learn/agents-course/) | Agent minis |
| [M23](../curriculum/6-frontier-production.md#module-23) Safety | [AI Safety Fundamentals](https://aisafetyfundamentals.com/alignment/) | Safety minis |
| [M24](../curriculum/6-frontier-production.md#module-24) MLOps | [Made With ML](https://madewithml.com/) | Productionise one project |
| [M25](../curriculum/6-frontier-production.md#module-25) Product DS | [Storytelling with Data](https://www.storytellingwithdata.com/) (book) | Product-DS minis |
| [M26](../curriculum/6-frontier-production.md#module-26) Capstone | — pick a track — | Your public capstone |

> **Beginners:** run the [Microsoft companion curricula](companion-curricula.md) alongside M1–M14.
> They supply guided lessons, quizzes, and solutions — the scaffolding university courses assume you
> don't need.

---

## A worked example — reading Module 9 correctly

Module 9 is about 40 lines long and names 11 lecture sources and 3 books. Here is the *correct* 4-minute
read of it:

1. **Read the "Why"** → linear regression teaches optimisation, loss, regularisation, and inference at once. Worth doing. ✅
2. **Check prerequisites** → M3, M5, M6. Have them? Continue. ✅
3. **Skim the topic list** → note that OLS, ridge, lasso, cross-validation, and bias-variance are the load-bearing ideas. Do **not** try to study all 11 sources.
4. **Take the primary** → [MIT 6.390](https://introml.mit.edu/spring26/lectures/lec01), lectures 1–3. Ignore CS109A, IITM, and Cambridge unless 6.390 confuses you.
5. **Open one book to the named chapters only** → ISLP chapters 3, 5, 6. Not the whole book.
6. **Build the project** → `LinearRegressionScratch` in NumPy, compared against scikit-learn, with tests and a results memo.
7. **Push it publicly.** Module 9 is now done. Go to Module 10.

Total resources actually consumed: **one course, three book chapters, one project.** Everything else in
the module was reference material for a future version of you.

---

## Common ways people get stuck

| Symptom | Cause | Fix |
| :--- | :--- | :--- |
| "There are too many links, I don't know where to start." | Reading the resource list as a to-do list. | Use the [Pick-One table](#pick-one). One course. |
| "I've been on Module 1 for four months." | Collecting courses instead of shipping the project. | Ship the project at 60% confidence. Gaps become searchable questions. |
| "I don't understand the lecture." | Missing a prerequisite, not lack of ability. | Re-read **Strict Prerequisites** and go back one module. |
| "I finished the course but can't build anything." | Passive consumption. | Close the tutorial, rebuild from memory. See the [tutorial-hell protocol](../curriculum/1-foundations.md#module-1). |
| "Should I do the maths or skip it?" | Both are valid — the repo states both. | Read the ⚡ **Intuition-First** callout in that module; it names exactly what you give up. |

---

[🏠 Roadmap home](../README.md) · [🧭 Start here](../START-HERE.md) · [❓ FAQ](../FAQ.md) · [📚 Curriculum index](../curriculum/README.md)
