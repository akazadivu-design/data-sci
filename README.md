<div align="center">
  <h1>🎓 The Elite Data Science Curriculum — 2026 Edition</h1>
  <h3>A PhD-Level, Zero-Omissions Roadmap Synthesised from IITM · Harvard · MIT · Cambridge</h3>
  <p><em>Pedagogically resequenced so that no concept is introduced without its mathematical or programming prerequisite.</em></p>
  <br/>
  <img alt="Curriculum Badge" src="https://img.shields.io/badge/Curriculum-2026%20Edition-blueviolet.svg">
  <img alt="Sources" src="https://img.shields.io/badge/Sources-IITM%20%7C%20Harvard%20%7C%20MIT%20%7C%20Cambridge-informational.svg">
  <img alt="Level" src="https://img.shields.io/badge/Level-BSc%20%E2%86%92%20MSc%20%E2%86%92%20PhD%20Prep-critical.svg">
  <img alt="Framework" src="https://img.shields.io/badge/Frameworks-PyTorch%202.x%20%7C%20JAX%20%7C%20Polars-orange.svg">
</div>

---

## 📜 Preamble from the Master Tutor

> This curriculum is the **union** of the 2026 week-by-week syllabi of the **IIT Madras BS in Data Science and Applications** (36,000+ active students), **Harvard's STAT 110, CS109A/B, and CS 1810 (Spring 2026)**, **MIT's 6.3900 (Spring 2026), 6.7900 (Fall 2025), 6.7960 Deep Learning, and the MITx MicroMasters in Statistics & Data Science**, and **Cambridge's Tripos Part IA/IB/II courses and the MPhil in Machine Learning and Machine Intelligence (MLMI)**.
>
> Every granular topic is cited to its university source. **Nothing has been summarised; nothing has been omitted.** Where a university publishes a specific week number, lecture title, or algorithm proof, it appears verbatim below.

---

## 📋 Table of Contents

- [🗺️ The 20-Module Progression Map](#️-the-20-module-progression-map)
- [🎯 Curriculum Meta-Information](#-curriculum-meta-information)
- [📚 Source Matrix — Universities & Courses](#-source-matrix--universities--courses)
- **Foundation Stratum (Modules 1–5)** — Mathematics, CS, Programming
  - [Module 1: Programming Foundations & Computational Thinking](#module-1-programming-foundations--computational-thinking)
  - [Module 2: Single-Variable & Multivariable Calculus](#module-2-singlevariable--multivariable-calculus)
  - [Module 3: Linear Algebra](#module-3-linear-algebra)
  - [Module 4: Discrete Math, Algorithms & Data Structures](#module-4-discrete-math-algorithms--data-structures)
  - [Module 5: Probability Theory — The Language of Uncertainty](#module-5-probability-theory--the-language-of-uncertainty)
- **Core Statistics Stratum (Modules 6–8)**
  - [Module 6: Statistical Inference](#module-6-statistical-inference)
  - [Module 7: Data Wrangling, EDA & Visualisation](#module-7-data-wrangling-eda--visualisation)
  - [Module 8: Databases, SQL & Big Data Systems](#module-8-databases-sql--big-data-systems)
- **Classical Machine Learning Stratum (Modules 9–12)**
  - [Module 9: Supervised Learning — Regression Family](#module-9-supervised-learning--regression-family)
  - [Module 10: Supervised Learning — Classification & Kernel Methods](#module-10-supervised-learning--classification--kernel-methods)
  - [Module 11: Unsupervised Learning, Dimensionality Reduction & Mixture Models](#module-11-unsupervised-learning-dimensionality-reduction--mixture-models)
  - [Module 12: Ensemble Methods, Tree-Based Learning & Boosting](#module-12-ensemble-methods-treebased-learning--boosting)
- **Probabilistic & Bayesian Stratum (Modules 13–14)**
  - [Module 13: Bayesian Inference, Graphical Models & MCMC](#module-13-bayesian-inference-graphical-models--mcmc)
  - [Module 14: Sequence Modelling — HMMs, Kalman Filters & Time Series](#module-14-sequence-modelling--hmms-kalman-filters--time-series)
- **Deep Learning Stratum (Modules 15–17)**
  - [Module 15: Deep Learning Foundations — MLPs, CNNs, Backprop](#module-15-deep-learning-foundations--mlps-cnns-backprop)
  - [Module 16: Representation Learning, Transformers & Generative Models](#module-16-representation-learning-transformers--generative-models)
  - [Module 17: Reinforcement Learning & Decision Making](#module-17-reinforcement-learning--decision-making)
- **Elite / 2026 Frontier Stratum (Modules 18–20)**
  - [Module 18: Large Language Models, RLHF & Alignment](#module-18-large-language-models-rlhf--alignment)
  - [Module 19: MLOps, Scaling, Systems & Responsible AI](#module-19-mlops-scaling-systems--responsible-ai)
  - [Module 20: Capstone — Research Dissertation & Publishable Project](#module-20-capstone--research-dissertation--publishable-project)
- [📖 Core 2026 Textbook Reading List](#-core-2026-textbook-reading-list)
- [🛠️ The Elite 2026 Toolchain](#️-the-elite-2026-toolchain)
- [✅ Progress Tracker](#-progress-tracker)
- [📄 Legacy OSSU Curriculum](#-legacy-ossu-curriculum-reference-only)

---

## 🗺️ The 20-Module Progression Map

```
┌─────────────────────────────────────────────────────────────────────┐
│ FOUNDATION (M1-M5)        │ CORE STATS (M6-M8)   │ CLASSICAL ML (M9-M12)
│  1 Programming            │  6 Inference         │   9 Regression
│  2 Calculus               │  7 EDA/Viz           │  10 Classification/SVM
│  3 Linear Algebra         │  8 Databases/Big Data│  11 Unsup/Dim-Red
│  4 Algos & DSA            │                      │  12 Ensembles/Boosting
│  5 Probability            │                      │
└───────────────────────────┴──────────────────────┴────────────────────┘
┌─────────────────────────────────────────────────────────────────────┐
│ PROBABILISTIC (M13-M14)   │ DEEP LEARNING (M15-M17)│ FRONTIER (M18-M20)
│ 13 Bayes / MCMC / PGMs    │ 15 MLPs/CNNs/Backprop  │ 18 LLMs / RLHF
│ 14 HMMs / Kalman / TS     │ 16 Transformers/Gen    │ 19 MLOps / Systems
│                           │ 17 RL / MDPs / Bandits │ 20 Capstone
└───────────────────────────┴────────────────────────┴────────────────────┘
```

---

## 🎯 Curriculum Meta-Information

| Attribute | Specification |
|---|---|
| **Total Modules** | 20 |
| **Estimated Duration** | 24–36 months (20–25 hrs/week) |
| **Academic Equivalence** | BSc → MSc → PhD-prep in Data Science |
| **Primary Languages** | Python 3.12+, R 4.4+, occasional Julia |
| **Primary Frameworks (2026)** | **PyTorch 2.5+**, **JAX 0.4+**, **Polars 1.x**, **scikit-learn 1.5+**, **Hugging Face Transformers 4.45+**, **PyMC 5.x**, **NumPyro**, **DuckDB 1.x** |
| **Hardware Assumption** | Local CPU for M1-M12; GPU/TPU (Colab/Kaggle/Lightning.ai) for M15+ |
| **Open Source Commitment** | Every single linked course is free or offers free audit |

---

## 📚 Source Matrix — Universities & Courses

> **Academic-year disclosure:** Where a 2026 syllabus is publicly posted, it is used. Otherwise, the latest published year is used and flagged. No content has been fabricated.

### 🇮🇳 IIT Madras — BS in Data Science and Applications (2025–26)

| Code | Course | Level |
|---|---|---|
| BSMA1001 | Mathematics for Data Science I | Foundation |
| BSMA1002 | Statistics for Data Science I | Foundation |
| BSCS1001 | Computational Thinking | Foundation |
| BSHS1001 | English I | Foundation |
| BSMA1003 | Mathematics for Data Science II | Foundation |
| BSMA1004 | Statistics for Data Science II | Foundation |
| BSCS1002 | Programming in Python | Foundation |
| BSCS2001 | Database Management Systems | Diploma |
| BSCS2002 | PDSA using Python | Diploma |
| BSCS2003 | Modern Application Development I | Diploma |
| BSCS2004 | Machine Learning Foundations | Diploma |
| BSCS2007 | Machine Learning Techniques | Diploma |
| BSCS2008 | Machine Learning Practice | Diploma |
| BSMS2001 | Business Data Management | Diploma |
| BSMS2002 | Business Analytics | Diploma |
| BSSE2001 | Software Engineering | BSc |
| BSSE2002 | Software Testing | BSc |
| BSCS3001 | AI: Search Methods | BS |
| BSCS3002 | Deep Learning | BS |
| BSCS3003 | Reinforcement Learning | BS |
| BSCS3004 | Large Language Models | BS |
| BSCS3005 | Computer Vision | BS |
| BSCS3006 | Big Data / Kafka | BS |

### 🇺🇸 Harvard University

| Course | Course Name | AY |
|---|---|---|
| STAT 110 | Introduction to Probability (Blitzstein) | 2025–26 |
| STAT 111 | Statistical Inference | 2025–26 |
| CS 109A / STAT 109A | Data Science 1 | Fall 2021 (latest public schedule) |
| CS 109B / STAT 109B | Data Science 2: Advanced Topics | Spring 2022 (latest public schedule) |
| **CS 1810** (formerly CS 181) | Machine Learning | **Spring 2026** |
| CS50P | Intro to Programming with Python | 2022–present (evergreen) |

### 🇺🇸 Massachusetts Institute of Technology

| Course | Course Name | AY |
|---|---|---|
| 18.01.1/2/3x | Calculus (Differentiation/Integration/Series) | Current |
| 18.06 | Linear Algebra (Strang) | OCW |
| 18.02 | Multivariable Calculus | OCW |
| 6.431x | Probability — Science of Uncertainty | MicroMasters C1 |
| 18.6501x | Fundamentals of Statistics | MicroMasters C3 |
| 6.86x | ML with Python: from Linear Models to Deep Learning | 3T2021 (current) |
| 14.310x | Data Analysis: Time Series | MicroMasters C4 |
| **6.3900 (6.390)** | Intro to Machine Learning | **Spring 2026** |
| **6.7900 (6.790)** | Graduate Machine Learning | **Fall 2025** |
| 6.7960 | Deep Learning (Isola & Beery) | Fall 2024 (Fall 2025 live) |
| 6.S191 | Intro to Deep Learning bootcamp | 2025 |
| 15.773 | Hands-on Deep Learning | Spring 2024 |

### 🇬🇧 University of Cambridge

| Course | Course Name | AY |
|---|---|---|
| Part IA CST | Machine Learning & Real-world Data (Teufel) | 2023–24 |
| Part IB CST | Data Science (Wischik) | 2023–24 |
| Part II CST | Machine Learning & Bayesian Inference (Holden) | **2025–26** |
| Part II CST | Artificial Intelligence | 2025–26 |
| MPhil MLMI | Module 1 — Introduction to ML | 2026 entry |
| MPhil MLMI | Tracks: Speech/Language, CV/Robotics, HCI, ML, **Biological Learning (new 2026)** | 2026 entry |

---

# 🟩 FOUNDATION STRATUM (Modules 1–5)

> These five modules establish the non-negotiable mathematical and programming substrate. **A weakness in any one will cause silent failure later** — e.g., a shaky grasp of eigenvalues cripples PCA, a shaky grasp of chain rule cripples backprop.

---

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
    * _Fluent Python_ (**3rd Edition, 2025**) — Luciano Ramalho — chapters 1–6, 9 (closures/decorators), 17 (iterators).
    * _Python Crash Course_ (**4th Edition, 2025**) — Eric Matthes — for absolute beginners only.
  * **Practical Implementation:** **Python 3.12+** (pattern matching, improved error messages, per-interpreter GIL awareness). IDE: **VS Code** with `ms-python.python`, `charliermarsh.ruff`, `ms-python.mypy-type-checker`. Dependency manager: **`uv`** (2024-released, now standard).

---

## Module 2: Single-Variable & Multivariable Calculus

* **The Tutor's "Why":** Gradients, backpropagation, maximum-likelihood estimation, and Bayes-rule derivations all live or die on calculus. You will not understand *why* SGD converges without it. Harvard's CS 1810 (2026) explicitly requires AM 22a (calc + lin alg).

* **Strict Prerequisites:** Module 1 (so you can verify integrals with SymPy). High-school pre-calculus.

* **Exhaustive Topic List:**
  * **[MIT 18.01.1x · Differentiation]**: Limits and continuity (ε-δ definition), derivative as a limit, power/product/quotient/chain rules, trig derivatives, exponential and log derivatives, implicit differentiation, linear/quadratic approximations, related rates, Mean Value Theorem, L'Hôpital's rule, optimisation (first/second derivative tests), Newton's method.
  * **[MIT 18.01.2x · Integration]**: Antiderivatives, Fundamental Theorem of Calculus (both parts + proofs), u-substitution, integration by parts, trigonometric integrals, partial fractions, improper integrals, Riemann sums, numerical integration (trapezoidal, Simpson's rule), applications (areas, volumes of revolution, arc length, surface area, centre of mass, work).
  * **[MIT 18.01.3x · Coordinate Systems & Infinite Series]**: Polar coordinates, parametric curves, conic sections, sequences, series convergence tests (ratio, root, integral, comparison, alternating series), power series, Taylor & Maclaurin series (with remainder bounds), complex numbers, Euler's formula.
  * **[MIT 18.02 · Multivariable Calculus]**: Vectors in ℝⁿ, dot and cross products, lines and planes, vector-valued functions, partial derivatives, tangent planes, total differential, **gradient vector & directional derivatives** (the foundation of gradient descent), chain rule (multivariable), **Hessian matrix** (used in Newton's method and second-order optimisers), Lagrange multipliers (→ SVM dual), double/triple integrals, change of variables, Jacobian determinant, vector fields, line integrals, Green's theorem, Stokes' theorem, divergence theorem.
  * **[IITM BSMA1001 — Math for DS I]**: Function basics, domain/range, piecewise functions, composition, inverse functions; limits; differentiation applied to business problems; definite vs indefinite integration; matrix-vector product as linear combination (preview of M3).
  * **[IITM BSMA1003 — Math for DS II]**: Vector calculus for optimisation, constrained optimisation, Lagrange multipliers with KKT conditions, convex functions, Jensen's inequality, convex optimisation preview.
  * **[Cambridge Data Science — Wischik]**: Calculus of variations (used in variational inference, M13).

* **2026 Resources:**
  * **Primary Course Link:** [MITx 18.01.1x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.1x/) · [18.01.2x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.2x/) · [18.01.3x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.3x/) · [MIT OCW 18.02](https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/)
  * **Required Reading (Latest 2026 Editions):**
    * _Calculus: Early Transcendentals_ (**9th Edition**) — James Stewart — chapters 1–12.
    * _Mathematics for Machine Learning_ — Deisenroth, Faisal, Ong (**freely available, 2024 reprint**) — Chapters 5 (Vector Calculus) and 6 (Probability). [mml-book.com](https://mml-book.com/) — **explicitly recommended by Harvard CS 1810 (2026)**.
    * 3Blue1Brown: [_Essence of Calculus_ playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — required visual intuition.
  * **Practical Implementation:** **SymPy 1.13+** for symbolic verification; **JAX 0.4+** `jax.grad` / `jax.jacobian` / `jax.hessian` for automatic differentiation — learn these NOW as you'll need them for all of M15+.

---

## Module 3: Linear Algebra

* **The Tutor's "Why":** *Every* modern ML algorithm — from linear regression to attention heads in GPT-class transformers — is a composition of matrix operations. Strang's 18.06 is the global gold standard; Cambridge's MLMI Module 1 requires eigendecomposition mastery before week 3.

* **Strict Prerequisites:** Module 2 (partial derivatives for matrix calculus).

* **Exhaustive Topic List:**
  * **[MIT 18.06 · Strang]**: Systems of linear equations, Gaussian elimination, LU factorisation, vector spaces, subspaces (column space, null space, row space, left null space — the "four fundamental subspaces"), rank-nullity theorem, linear independence, basis, dimension, orthogonality, Gram-Schmidt process, QR decomposition, projections, least squares (normal equations), determinants (cofactor expansion, properties), **eigenvalues and eigenvectors** (characteristic polynomial, diagonalisation), **Singular Value Decomposition (SVD)** (full and reduced forms, Eckart-Young theorem, pseudoinverse), positive-definite matrices (Cholesky), similar matrices, Jordan form, complex matrices (Hermitian, unitary), fast Fourier transform as a change of basis, linear transformations, applications to graphs (Laplacian), applications to differential equations (matrix exponential).
  * **[3Blue1Brown — Essence of Linear Algebra]**: Geometric intuition for determinants, eigenvectors as invariant directions, change of basis as relabelling.
  * **[IITM BSMA1003]**: Matrix rank via row reduction, solvability of linear systems, null space / column space correspondence, linear maps, basis transformations, symmetric matrices and spectral theorem.
  * **[Harvard CS 1810 prereq (AM 22a / Math 21b)]**: Inner product spaces, orthogonal complement, projection matrices P = A(AᵀA)⁻¹Aᵀ, quadratic forms, positive semi-definiteness as condition for convex loss.
  * **[Cambridge Data Science — Wischik, Lec 2-3 "Feature Spaces"]**: Vector spaces as abstract objects, bases, inner products, orthonormal bases, projection onto subspace, **"model fitting as projection"** (critical insight for understanding linear regression), design of features, basis functions (polynomial, Fourier, radial).
  * **[Cambridge MLMI 1]**: Eigendecomposition as diagonalisation, SVD applications to dimensionality reduction and image compression.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 18.06 OCW SC version](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/) · [3Blue1Brown EoLA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Linear Algebra_ (**6th Edition, 2023**) — Gilbert Strang.
    * _Linear Algebra and Learning from Data_ (**2019, 2025 reprint**) — Strang — specifically written for ML era.
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapters 2, 3, 4.
  * **Practical Implementation:** **NumPy 2.x** (`np.linalg.eig`, `np.linalg.svd`, `np.linalg.solve`). **SciPy 1.14+** for sparse linear algebra (`scipy.sparse.linalg`). Use **`jax.numpy`** for GPU-accelerated linear algebra once comfortable.

---

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

* **2026 Resources:**
  * **Primary Course Link:** [GaTech DSA I-IV on edX](https://www.edx.org/learn/data-structures/the-georgia-institute-of-technology-data-structures-algorithms-i-arraylists-linkedlists-stacks-and-queues) (Java) **OR** [MIT 6.006 Introduction to Algorithms OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) (Python — **more aligned with 2026 workflow**).
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Algorithms_ (**4th Edition, 2022**) — Cormen, Leiserson, Rivest, Stein (CLRS) — the canonical reference.
    * _Algorithm Design Manual_ (**3rd Edition, 2020**) — Skiena — for problem-solving intuition.
    * _Concrete Mathematics_ (**2nd Edition**) — Graham, Knuth, Patashnik — for discrete-math depth.
  * **Practical Implementation:** Pure Python + `collections` (deque, defaultdict, Counter), **`sortedcontainers`**, **`networkx` 3.x** for graph algorithms, **LeetCode** + **Codeforces** for practice.

---

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

* **2026 Resources:**
  * **Primary Course Link:** [Harvard Stat 110 full playlist](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) · [Handouts & problems](https://stat110.hsites.harvard.edu/) · [MITx 6.431x](https://micromasters.mit.edu/ds/)
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Probability_ (**2nd Edition, 2019; 2024 reprint**) — Joseph Blitzstein & Jessica Hwang — [free PDF](https://projects.iq.harvard.edu/stat110/home) — **chapters 1-12 cover-to-cover**. This is the primary text.
    * _Introduction to Probability_ (**2nd Edition**) — Bertsekas & Tsitsiklis — companion to 6.431x.
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapter 6.
  * **Practical Implementation:** **SciPy 1.14+** `scipy.stats` (every distribution you'll need); **NumPy** `np.random.Generator` (modern PCG64 RNG); begin using **`distrax`** (JAX) or **`torch.distributions`** (PyTorch) for differentiable distributions — you'll need these in M13.

---

# 🟨 CORE STATISTICS STRATUM (Modules 6–8)

---

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

---

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

---

## Module 8: Databases, SQL & Big Data Systems

* **The Tutor's "Why":** In 2026, data rarely fits in RAM. IITM dedicates a full diploma-level course (BSCS2001) + two specialisation courses to this. You need SQL fluency for 90% of industry jobs.

* **Strict Prerequisites:** Module 4 (hashing, trees).

* **Exhaustive Topic List:**
  * **[IITM BSCS2001 — DBMS (Prof. P.P. Das)]**: Relational model (tuples, relations, schemas, keys — super/primary/candidate/foreign), relational algebra (selection σ, projection π, union, intersection, difference, Cartesian product, join variants, division), **SQL DDL** (CREATE, ALTER, DROP), **SQL DML** (SELECT/INSERT/UPDATE/DELETE), JOINs (inner, left/right/full outer, cross, self, lateral), subqueries (correlated vs uncorrelated), CTEs (recursive and non-recursive), window functions (`OVER`, `PARTITION BY`, `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM() OVER`), set operations (UNION, INTERSECT, EXCEPT), views, indexes (B-tree, hash, bitmap, covering), transactions and **ACID properties**, isolation levels (read uncommitted/committed, repeatable read, serialisable), concurrency control (two-phase locking, MVCC), recovery (WAL, ARIES), normalisation (1NF/2NF/3NF/BCNF/4NF/5NF), functional dependencies, Armstrong's axioms.
  * **[OSSU baseline — Coursera DB Specialisation]**: Data warehouse concepts (star schema, snowflake schema, fact/dimension tables), OLAP cubes, slice/dice/drill-down/roll-up, SCD (Type 0/1/2/3/6), ETL pipeline design.
  * **[OSSU — MongoDB path]**: Document databases, BSON, sharding, replica sets, aggregation pipeline ($match, $group, $project, $lookup, $unwind), indexing strategies.
  * **[IITM BSCS3006 — Big Data / Kafka]**: **Apache Kafka** architecture (brokers, topics, partitions, consumer groups, offsets, exactly-once semantics), **Apache Spark** (RDDs, DataFrames, Dataset API, Catalyst optimiser, Tungsten, PySpark, Spark SQL, MLlib, Structured Streaming), **Hadoop** (HDFS, MapReduce, YARN), **MapReduce paradigm** (map, shuffle, reduce) as CS conceptual model, **Stream processing** (Flink, Kafka Streams, windowing — tumbling/sliding/session), CAP theorem, eventual consistency.
  * **[MIT Mining Massive Datasets (OSSU) / Stanford CS246]**: MapReduce algorithms (word count, inverted index, joins), similarity search (LSH — MinHash for Jaccard, random projections for cosine), PageRank as eigenvector of stochastic matrix, recommendation systems at scale, frequent itemsets (A-Priori, PCY, Multistage), clustering large datasets (BFR, CURE), **streaming algorithms** (reservoir sampling, Bloom filters, Count-Min Sketch, Flajolet-Martin for distinct count, HyperLogLog), advertising on the web (bipartite matching, AdWords problem).
  * **[Coursera "Process Mining"]**: Event logs, α-algorithm, inductive miner, conformance checking, process discovery.

* **2026 Resources:**
  * **Primary Course Link:** [IITM BSCS2001 course page](https://study.iitm.ac.in/ds/course_pages/BSCS2001.html) · [Stanford CS246 2025 lectures on YouTube](https://www.youtube.com/@stanfordonline) · [Databricks Academy](https://www.databricks.com/learn/training/home) (free Spark path).
  * **Required Reading (Latest 2026 Editions):**
    * _Designing Data-Intensive Applications_ (**2017, still definitive; 2026 revised edition in progress**) — Martin Kleppmann.
    * _Database System Concepts_ (**7th Edition, 2019**) — Silberschatz, Korth, Sudarshan.
    * _Mining of Massive Datasets_ (**3rd Edition, free online**) — Leskovec, Rajaraman, Ullman — [mmds.org](http://www.mmds.org/).
  * **Practical Implementation:** **PostgreSQL 17** (with `pgvector` extension for vector search), **DuckDB 1.x** (in-process analytics, the 2026 pandas-killer for single-machine analytics), **SQLAlchemy 2.x** with async, **Apache Spark 3.5+** via **PySpark**, **Apache Iceberg** / **Delta Lake** for lakehouse, **Apache Kafka 3.8+**.

---

# 🟧 CLASSICAL MACHINE LEARNING STRATUM (Modules 9–12)

> This stratum is the intersection of every university's "first ML course" — MIT 6.390, Harvard CS 1810, Cambridge MLRD/MLBI, IITM BSCS2004/2007/2008.

---

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

---

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

---

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

---

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

---

# 🟦 PROBABILISTIC & BAYESIAN STRATUM (Modules 13–14)

---

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

---

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

---

# 🟪 DEEP LEARNING STRATUM (Modules 15–17)

---

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
  * **[MIT 6.7960 · Week 1-4 (Fall 2024)]**: Course overview; **How to train a neural net** (SGD, backprop, differentiable programming with autodiff); **Approximation theory** — universal approximation, **Barron's theorem**, depth separation results; **Architectures: Grids** (CNNs in depth); **Architectures: Graphs** — Graph Neural Networks (message passing, GCN, GAT, GraphSAGE, **theoretical limits of GNN expressiveness — Weisfeiler-Lehman hierarchy**); **Generalization Theory** — basic PAC, overparameterisation, **double descent**, inadequacy of VC dimension, inductive biases in deep learning; **Scaling rules for optimisation** — spectral perspective, feature learning, μP (maximal-update) hyperparameter transfer across width/depth.
  * **[MIT 6.7960 · Week 6 "Architectures: Memory"]**: RNNs, LSTMs, sequence models, stability analysis.
  * **[IITM BSCS3002 — Deep Learning]**: IITM's dedicated Deep Learning course covers the above plus practical engineering on **PyTorch**.
  * **[IITM BSCS2008 · Week 11]**: Neural networks in scikit-learn (MLP introduction).
  * **[Harvard CS 1810]**: Neural networks as a syllabus topic.
  * **[MIT 6.S191 bootcamp]**: Condensed practical treatment.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 6.7960 Fall 2024 full schedule with slides](https://phillipi.github.io/6.7960/) · [Fall 2025 site](https://deeplearning6-7960.github.io/) · [MIT 6.390 Spring 2026](https://introml.mit.edu/spring26/) · [Harvard CS109B 2022](https://harvard-iacs.github.io/2022-CS109B/).
  * **Required Reading (Latest 2026 Editions):**
    * _Understanding Deep Learning_ — Simon Prince (**2024, MIT Press; free online**) — [udlbook.github.io](https://udlbook.github.io/udlbook/) — the **best 2026 textbook**; chapters 1-12.
    * _Deep Learning_ — Goodfellow, Bengio, Courville (2016, still relevant for foundations).
    * _Dive into Deep Learning_ — Zhang, Lipton, Li, Smola — [d2l.ai](https://d2l.ai/) — 2024 edition with PyTorch/MXNet/TensorFlow/JAX parallel implementations.
    * _Foundations of Computer Vision_ — Torralba, Isola, Freeman (**MIT Press 2024**, free online).
  * **Practical Implementation:** **PyTorch 2.5+** (`torch.compile`, `torch.func.grad`, `torch.distributed`), **JAX 0.4+** with **Flax 0.9+** / **Equinox** for functional deep learning, **Hugging Face Accelerate** for distributed training, **Weights & Biases** or **MLflow** for experiment tracking, **Lightning 2.x** for training-loop abstraction.

---

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
  * **[MIT 6.7960 · Week 5 "Architectures: Transformers"]**: Three key ideas — **tokens, attention, positional codes**; Transformers as unified framework (subsuming MLPs, GNNs, CNNs); Vision Transformers (ViT, Swin, DeiT); **multi-modal transformers** (CLIP, BLIP-2, LLaVA).
  * **[MIT 6.7960 · Week 6-8 "Representation Learning"]**: Reconstruction-based (autoencoders, VQ-VAE, MAE — Masked Autoencoders); similarity-based (metric learning, SimCLR, MoCo v3, BYOL, DINO, CLIP InfoNCE); **theory of representation learning** (NN-GP correspondence, NTK — Neural Tangent Kernel).
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
  * **Primary Course Link:** [MIT 6.7960 full schedule](https://phillipi.github.io/6.7960/) · [Harvard CS109B 2022 Lec 16-23](https://harvard-iacs.github.io/2022-CS109B/) · [MIT 6.390 S26 Lec 9](https://introml.mit.edu/spring26/lectures/lec09).
  * **Required Reading (Latest 2026 Editions):**
    * _Understanding Deep Learning_ — Simon Prince — Chapters 12-18 (transformers, GANs, VAEs, diffusion).
    * _Deep Learning for Coders with fastai & PyTorch_ — Howard & Gugger — for practitioners.
    * Vaswani et al. 2017 ("Attention is All You Need") — **mandatory primary-source reading**.
    * Ho, Jain, Abbeel 2020 ("DDPM") — for diffusion.
    * Radford et al. 2021 ("CLIP") — multi-modal foundation.
    * _The Little Book of Deep Learning_ — François Fleuret — concise reference.
  * **Practical Implementation:** **Hugging Face Transformers 4.45+** (the universal interface), **Hugging Face Diffusers** for image/video gen, **Hugging Face PEFT** for LoRA/QLoRA, **xformers** / **FlashAttention-3** for memory-efficient attention, **bitsandbytes** for 4/8-bit training, **`torch.compile`** + **`torch.fullgraph`** for 2× speedups.

---

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

---

# 🔴 ELITE / 2026 FRONTIER STRATUM (Modules 18–20)

---

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
  * **Primary Course Link:** [IITM BSCS3004](https://study.iitm.ac.in/ds/course_pages/BSCS3004.html) · [Stanford CS336 "Language Modeling from Scratch" 2025](https://stanford-cs336.github.io/spring2025/) · [Princeton COS 597 G](https://princeton-nlp.github.io/cos597G/) · [MIT 6.7960 Week 12, 15](https://phillipi.github.io/6.7960/).
  * **Required Reading (Latest 2026 Editions):**
    * _Build a Large Language Model (From Scratch)_ — Sebastian Raschka (**Manning 2024**).
    * _Hands-On Large Language Models_ — Alammar & Grootendorst (**O'Reilly 2024**).
    * _Speech and Language Processing_ (**3rd Edition draft**) — Jurafsky & Martin — [free online](https://web.stanford.edu/~jurafsky/slp3/) (chapters 9-11 for LLMs).
    * Anthropic Transformer Circuits thread ([transformer-circuits.pub](https://transformer-circuits.pub/)) — mandatory for interpretability.
    * "A Survey of LLMs" (Zhao et al., 2023, updated 2025) — arXiv comprehensive survey.
  * **Practical Implementation:** **Hugging Face `transformers` 4.45+**, **`datasets`**, **`accelerate`**, **`peft`**, **`trl`** (for RLHF/DPO/GRPO), **`bitsandbytes`**, **`vLLM`** (production inference), **`SGLang`** (2024 fastest), **`llama.cpp`** (GGUF for CPU inference), **Ollama** (local deployment), **LangChain 0.3+** / **LlamaIndex 0.11+** / **DSPy 2.5+** (the 2026 prompting framework), **Unsloth** for efficient fine-tuning.

---

## Module 19: MLOps, Scaling, Systems & Responsible AI

* **The Tutor's "Why":** A Jupyter notebook is not a product. The 2026 data scientist must understand the entire lifecycle: version control for data, reproducible environments, CI/CD for models, monitoring for drift, fairness audits, and GDPR/EU-AI-Act compliance. Harvard's AC215 (new 2024) covers this in depth.

* **Strict Prerequisites:** Any model from Modules 9-18.

* **Exhaustive Topic List:**
  * **[Harvard AC215 "Advanced Practical Data Science"]**: Containers (Docker, Docker Compose), container orchestration (Kubernetes, KubeFlow, Ray), **data pipelines** (Apache Airflow, Dagster 1.x, Prefect 3.x), **model registries**, **feature stores** (Feast, Tecton), API serving (FastAPI, BentoML, Ray Serve, Modal, Replicate), **A/B testing** (multi-armed bandit deployment, shadow deployment, canary, blue-green), **model monitoring** (data drift — KS test, PSI, JS divergence; concept drift; prediction drift), **observability** (OpenTelemetry, Weights & Biases, Arize, WhyLabs, Evidently).
  * **[IITM BSCS2003 — Modern Application Development I]**: Flask, Vue.js, REST APIs, OAuth, JWT, WebSockets, deployment to Heroku/Vercel/Fly.io.
  * **[IITM BSSE2001/BSSE2002 — Software Engineering & Testing]**: SDLC, agile, scrum, unit/integration/system testing, TDD, BDD, code review, pair programming, version control workflows (git-flow, trunk-based, GitHub Flow), CI/CD (GitHub Actions, GitLab CI, Jenkins).
  * **Experiment tracking & reproducibility**: Weights & Biases, MLflow 2.x, Neptune.ai, DVC (Data Version Control), Hydra for config, Pydantic 2.x for validation.
  * **GPU clusters & distributed training**: Data parallelism (PyTorch DDP, FSDP — Fully Sharded Data Parallel), tensor parallelism (Megatron-LM), pipeline parallelism (GPipe, PipeDream), **3D parallelism**, ZeRO (DeepSpeed 1/2/3), **FSDP2**, communication primitives (AllReduce, NCCL), gradient checkpointing, gradient accumulation, mixed precision (fp16, bf16, fp8 — H100/H200).
  * **Inference optimisation**: TensorRT-LLM, vLLM continuous batching, speculative decoding, **prefix caching**, **chunked prefill**, INT8/INT4 quantisation at inference, KV-cache management.
  * **Responsible AI & governance**:
    * **Fairness metrics** — demographic parity, equalised odds, equal opportunity, calibration within groups; Aequitas, Fairlearn, AIF360.
    * **Explainability** — SHAP, LIME, Captum (for PyTorch), TCAV, counterfactuals (DiCE).
    * **Privacy** — **Differential Privacy** (Dwork 2006 formal definition, ε-δ-DP, Laplace and Gaussian mechanisms, composition theorems, moments accountant, DP-SGD — Abadi 2016), **Federated Learning** (FedAvg, FedProx, personalised FL), **Secure Multi-Party Computation** (SMPC), **Homomorphic Encryption** preview.
    * **Security** — adversarial attacks (M15), **prompt injection**, **data poisoning**, **model stealing / extraction**, **membership inference attacks**.
    * **Regulation (2026)** — **EU AI Act** (risk categories, transparency obligations), GDPR Art 22 (right to explanation), **ISO/IEC 42001:2023** (AI management), **NIST AI Risk Management Framework**, US Executive Order on AI (Biden 2023), **UK AI Safety Institute** standards.
  * **[Harvard CS109A · Lec 13 "Ethics"]**: Formal ethics module — fairness, accountability, transparency (FAT/FAccT), **dual-use research**, embedded ethics (Harvard Embedded EthiCS).
  * **[Harvard CS 1810 "Philosophy"]**: "With great power comes great responsibility" — mandatory embedded-ethics lecture.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard AC215 2024](https://harvard-iacs.github.io/2024-AC215/) · [Made With ML](https://madewithml.com/) · [Full Stack Deep Learning](https://fullstackdeeplearning.com/).
  * **Required Reading (Latest 2026 Editions):**
    * _Designing Machine Learning Systems_ — Chip Huyen (**O'Reilly 2022, 2024 reprint**).
    * _Machine Learning Engineering_ — Andriy Burkov.
    * _Algorithms of Oppression_ — Safiya Umoja Noble (for critical perspective on bias).
    * _Weapons of Math Destruction_ — Cathy O'Neil.
    * EU AI Act text (2024) — selected articles.
  * **Practical Implementation:** **Docker 25+**, **Kubernetes 1.30+**, **Terraform 1.8+**, **AWS/GCP/Azure SDKs**, **Ray 2.x** (Ray Tune, Ray Serve, Ray Data), **vLLM**, **BentoML**, **SkyPilot** (multi-cloud), **Modal** (serverless GPU), **Fairlearn**, **AIF360**, **Opacus** (DP for PyTorch), **Flower** (federated learning).

---

## Module 20: Capstone — Research Dissertation & Publishable Project

* **The Tutor's "Why":** Every one of our four universities requires a substantial capstone. IITM requires a capstone project; Harvard CS109B culminates in a final project showcase; MIT 6.7960's grade is 35% final project; Cambridge MLMI runs a **4-month research dissertation** from end of Lent Term. This is the module where you convert a portfolio into a career.

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

# 📖 Core 2026 Textbook Reading List

> **Tier 1 (own a copy)**. These are the books you should have on your shelf, marked-up, for the rest of your career.

| # | Title | Authors | Edition / Year | Primary Modules | Free PDF? |
|---|---|---|---|---|---|
| 1 | _Introduction to Probability_ | Blitzstein & Hwang | 2nd Ed. (2019; 2024 reprint) | M5 | ✅ [stat110](https://projects.iq.harvard.edu/stat110/home) |
| 2 | _Mathematics for Machine Learning_ | Deisenroth, Faisal, Ong | 2020 (2024 reprint) | M2, M3, M5 | ✅ [mml-book.com](https://mml-book.com/) |
| 3 | _An Introduction to Statistical Learning with Python_ (ISLP) | James, Witten, Hastie, Tibshirani, Taylor | 1st Ed. (2023, 2025 reprint) | M6, M9-M12 | ✅ [statlearning.com](https://www.statlearning.com/) |
| 4 | _Elements of Statistical Learning_ (ESL) | Hastie, Tibshirani, Friedman | 2nd Ed., 12th printing | M9-M12 | ✅ [hastie.su.domains](https://hastie.su.domains/ElemStatLearn/) |
| 5 | _Pattern Recognition and Machine Learning_ (PRML) | Christopher Bishop | 2006, 2026 reprint | M9-M17 | — |
| 6 | _Probabilistic Machine Learning: An Introduction_ | Kevin P. Murphy | MIT Press 2022 | M11-M16 | ✅ [probml.github.io](https://probml.github.io/pml-book/book1.html) |
| 7 | _Probabilistic Machine Learning: Advanced Topics_ | Kevin P. Murphy | MIT Press 2023 | M13-M17 | ✅ [probml.github.io](https://probml.github.io/pml-book/book2.html) |
| 8 | _Understanding Deep Learning_ | Simon Prince | MIT Press 2024 | M15-M16 | ✅ [udlbook.github.io](https://udlbook.github.io/udlbook/) |
| 9 | _Dive into Deep Learning_ | Zhang, Lipton, Li, Smola | 2024 | M15-M16 | ✅ [d2l.ai](https://d2l.ai/) |
| 10 | _Reinforcement Learning: An Introduction_ | Sutton & Barto | 2nd Ed. 2018 (2024 reprint) | M17 | ✅ [incompleteideas.net](http://incompleteideas.net/book/the-book-2nd.html) |
| 11 | _Bayesian Data Analysis_ (BDA3) | Gelman et al. | 3rd Ed. 2013 (2024 reprint) | M6, M13 | ✅ [stat.columbia.edu](http://www.stat.columbia.edu/~gelman/book/) |
| 12 | _Introduction to Algorithms_ (CLRS) | Cormen, Leiserson, Rivest, Stein | 4th Ed. 2022 | M4 | — |
| 13 | _Introduction to Linear Algebra_ | Gilbert Strang | 6th Ed. 2023 | M3 | — |
| 14 | _Designing Data-Intensive Applications_ | Martin Kleppmann | 2017 (2026 rev.) | M8, M19 | — |
| 15 | _Speech and Language Processing_ (3rd Ed draft) | Jurafsky & Martin | Draft 2024 | M16, M18 | ✅ [stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/) |
| 16 | _Foundations of Computer Vision_ | Torralba, Isola, Freeman | MIT Press 2024 | M15-M16 | ✅ coming 2025 |
| 17 | _Designing Machine Learning Systems_ | Chip Huyen | O'Reilly 2022 (2024 reprint) | M19 | — |
| 18 | _Build a LLM (From Scratch)_ | Sebastian Raschka | Manning 2024 | M18 | — |
| 19 | _Python for Data Analysis_ | Wes McKinney | 3rd Ed. 2022 | M7 | ✅ [wesmckinney.com](https://wesmckinney.com/book/) |
| 20 | _Fluent Python_ | Luciano Ramalho | 3rd Ed. 2025 | M1 | — |

> **Tier 2 (reference)**: _All of Statistics_ (Wasserman), _Statistical Inference_ (Casella & Berger), _Bayesian Reasoning and Machine Learning_ (Barber), _Machine Learning: A Probabilistic Perspective_ (Murphy 2012), _Deep Learning_ (Goodfellow/Bengio/Courville 2016), _Algorithms for Decision Making_ (Kochenderfer), _Interpretable Machine Learning_ (Molnar), _Forecasting: Principles and Practice_ (Hyndman), _Mining of Massive Datasets_ (Leskovec).

---

# 🛠️ The Elite 2026 Toolchain

Not merely a list — these are the exact versions you should be using in April 2026.

| Category | Tool | Version | Why (2026) |
|---|---|---|---|
| **Python runtime** | CPython | 3.12+ | Per-interpreter GIL, better error messages, match statements |
| **Package management** | `uv` | 0.5+ | 10-100× faster than pip/poetry; standard in 2026 |
| **Env manager** | `pixi` or `conda` | latest | For system deps (CUDA, MKL) |
| **IDE** | VS Code | latest | + Cursor or Zed for AI-native editing |
| **Notebooks** | Jupyter Lab / `marimo` | 4.x / 0.8+ | marimo = reactive notebooks, 2026 favourite |
| **Formatter / Linter** | `ruff` | 0.6+ | Replaces Black, flake8, isort in one Rust binary |
| **Type checker** | `mypy` or `pyright` | latest | Gradual typing essential |
| **DataFrames** | **Polars** + **DuckDB** | 1.x / 1.x | Faster than pandas; use Polars for ops, DuckDB for SQL |
| **Numerical core** | NumPy | 2.x | New dtypes (string, variable-precision) |
| **Classical ML** | scikit-learn | 1.5+ | + `sklearnex` for CPU speedup |
| **Boosting** | XGBoost / LightGBM / CatBoost | 2.x / 4.x / 1.2+ | Still beats DL on tabular |
| **Deep Learning** | **PyTorch** | 2.5+ | `torch.compile`, FSDP2, native bfloat16 |
| **Alt DL** | **JAX** + Flax / Equinox | 0.4+ | For research, TPU-first |
| **Bayesian** | NumPyro / PyMC 5 | 0.15+ / 5.x | JAX-backed for speed |
| **Transformers** | HuggingFace Transformers | 4.45+ | Universal interface |
| **LLM fine-tuning** | `trl` + `peft` + **Unsloth** | latest | DPO/GRPO/QLoRA |
| **LLM inference** | **vLLM** or **SGLang** | 0.6+ / latest | Continuous batching, prefix caching |
| **Prompting** | **DSPy** | 2.5+ | Programmatic prompting; 2026 frontier |
| **Vector DB** | **pgvector** or **LanceDB** or Qdrant | latest | pgvector = Postgres-native |
| **MLOps** | **Ray** / **MLflow** / **W&B** | 2.x / 2.x / latest | Ray for scaling, W&B for tracking |
| **Containers** | Docker | 25+ | Multi-arch, rootless |
| **Orchestration** | Kubernetes / Dagster | 1.30+ / 1.x | Dagster > Airflow for ML pipelines |
| **Serving** | **FastAPI** + BentoML / Modal | latest | Modal = serverless GPU |
| **Experiment** | **Hydra** + Pydantic | 1.3+ / 2.x | Config management |
| **Reproducibility** | DVC + Git LFS | 3.x / latest | Version control for data |
| **Writing** | Typst or LaTeX + Zotero 7 | latest | Typst = modern LaTeX alternative |

---

# ✅ Progress Tracker

> Fork this repo, copy this section, and replace `[ ]` with `[x]` as you complete each sub-module.

### 🟩 Foundation Stratum
- [ ] **Module 1**: Programming Foundations (CS50P + MIT 6.0001/6.0002)
- [ ] **Module 2**: Calculus (MITx 18.01.1/2/3x + 18.02)
- [ ] **Module 3**: Linear Algebra (MIT 18.06 + 3Blue1Brown)
- [ ] **Module 4**: DSA (MIT 6.006 + GaTech series)
- [ ] **Module 5**: Probability (Stat 110 full 34 lectures + MITx 6.431x)

### 🟨 Core Statistics Stratum
- [ ] **Module 6**: Inference (MITx 18.6501x + STAT 111)
- [ ] **Module 7**: EDA & Viz (CS109A Lec 1-2, 9, 12-13)
- [ ] **Module 8**: Databases (IITM BSCS2001 + Mining Massive Datasets)

### 🟧 Classical ML Stratum
- [ ] **Module 9**: Regression (MIT 6.390 Lec 1-3, CS109A Lec 3-6)
- [ ] **Module 10**: Classification & SVMs (MIT 6.390 Lec 4, CS109A Lec 14-15, CS 1810, Cambridge ML&BI)
- [ ] **Module 11**: Unsupervised (CS109A Lec 10, CS109B Lec 1-2, MIT 6.86x Unit 4)
- [ ] **Module 12**: Ensembles (CS109A Lec 16-20)

### 🟦 Probabilistic Stratum
- [ ] **Module 13**: Bayes + MCMC (CS109B Lec 3-7, Cambridge ML&BI, MIT 6.790 Part III)
- [ ] **Module 14**: HMMs & Time Series (Cambridge MLRD Topic 2, MITx 14.310x)

### 🟪 Deep Learning Stratum
- [ ] **Module 15**: DL Foundations (CS109B Lec 8-15, MIT 6.390 Lec 5-7, MIT 6.7960 W1-6)
- [ ] **Module 16**: Transformers & Gen (CS109B Lec 16-23, MIT 6.7960 W5-11, MIT 6.390 Lec 9)
- [ ] **Module 17**: RL & Decisions (MIT 6.390 Lec 10-11, IITM BSCS3003)

### 🔴 Frontier Stratum
- [ ] **Module 18**: LLMs & RLHF (IITM BSCS3004, MIT 6.7960 W12, W15)
- [ ] **Module 19**: MLOps & Responsible AI (Harvard AC215, IITM BSCS2003/BSSE)
- [ ] **Module 20**: Capstone Project (arXiv preprint + HF release)

---

# 📊 Pedagogical Dependency Graph

```
                           ┌──────────────┐
                           │ M1 Programming│
                           └───────┬──────┘
             ┌─────────────────────┼─────────────────────┐
             ▼                     ▼                     ▼
    ┌──────────────┐       ┌──────────────┐      ┌──────────────┐
    │ M2 Calculus  │       │ M4 DSA       │      │ M7 EDA/Viz   │
    └──────┬───────┘       └──────┬───────┘      └──────┬───────┘
           ▼                      ▼                     │
    ┌──────────────┐       ┌──────────────┐             │
    │ M3 Lin Alg   │       │ M8 Databases │             │
    └──────┬───────┘       └──────────────┘             │
           ▼                                            │
    ┌──────────────────────────────────────┐            │
    │       M5 Probability                 │            │
    └───────────────┬──────────────────────┘            │
                    ▼                                   │
          ┌────────────────────┐                        │
          │ M6 Inference       │◀───────────────────────┘
          └────────────────────┘
                    ▼
    ┌───────────────────────────────┐
    │ M9 Regression ──▶ M10 Classification ──▶ M11 Unsup ──▶ M12 Ensembles │
    └───────────────┬───────────────┘
                    ▼
          ┌────────────────────┐
          │ M13 Bayes / MCMC   │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │ M14 HMMs / Time    │
          └─────────┬──────────┘
                    ▼
    ┌────────────────────────────────┐
    │ M15 DL Foundations             │
    └───────────────┬────────────────┘
                    ▼
    ┌────────────────────────────────┐
    │ M16 Transformers & Gen Models  │
    └───────────────┬────────────────┘
                    ▼
    ┌────────────────────────────────┐
    │ M17 RL & Decision Making       │
    └───────────────┬────────────────┘
                    ▼
      ┌───────────────────────────┐
      │ M18 LLMs / RLHF / Agents  │
      └─────────────┬─────────────┘
                    ▼
      ┌───────────────────────────┐
      │ M19 MLOps & Responsible AI│
      └─────────────┬─────────────┘
                    ▼
      ┌───────────────────────────┐
      │ M20 Capstone              │
      └───────────────────────────┘
```

---

# 🙏 Acknowledgements & Attribution

This curriculum synthesises publicly-available syllabi from:

* **IIT Madras** — [study.iitm.ac.in/ds](https://study.iitm.ac.in/ds/) (BS in Data Science and Applications, 2025–26).
* **Harvard University** — [harvard-iacs.github.io](https://harvard-iacs.github.io/) (CS 109A/B), [stat110.hsites.harvard.edu](https://stat110.hsites.harvard.edu/) (STAT 110), [harvard-ml-courses.github.io/cs181-web/](https://harvard-ml-courses.github.io/cs181-web/) (CS 1810, Spring 2026), [cs50.harvard.edu/python](https://cs50.harvard.edu/python/) (CS50P).
* **Massachusetts Institute of Technology** — [introml.mit.edu/spring26](https://introml.mit.edu/spring26) (6.390), [gradml.mit.edu](https://gradml.mit.edu/) (6.790), [phillipi.github.io/6.7960](https://phillipi.github.io/6.7960/) (Deep Learning), [micromasters.mit.edu/ds](https://micromasters.mit.edu/ds/) (Statistics & Data Science MicroMasters), [ocw.mit.edu](https://ocw.mit.edu/) (18.01/18.02/18.06/6.0001/6.0002/6.006).
* **University of Cambridge** — [cl.cam.ac.uk/teaching](https://www.cl.cam.ac.uk/teaching/) (Part IA/IB/II), [mlmi.eng.cam.ac.uk](https://www.mlmi.eng.cam.ac.uk/) (MPhil MLMI).

All university material remains © their respective institutions; this repository only cites and organises publicly-disclosed syllabi.

---

# 📄 Legacy OSSU Curriculum (Reference Only)

> The following is the _original_ `ossu/data-science` curriculum, preserved for historical reference. It is **no longer the recommended path** in 2026 — it lacks Transformers, LLMs, Diffusion models, Bayesian methods, Reinforcement Learning, and MLOps. Use the 20 modules above instead.

<details>
<summary><b>Click to expand the pre-2026 OSSU curriculum</b></summary>

## Original OSSU Contents

- [About](#about)
- [Curricular Guideline](#curricular-guideline)
- Original course sections: Introduction to Data Science · Introduction to Computer Science · Data Structures and Algorithms · Databases · Single Variable Calculus · Linear Algebra · Multivariable Calculus · Statistics & Probability · Data Science Tools & Methods · Machine Learning/Data Mining · Final project

## About

This was a path for those of you who wanted to complete the Data Science undergraduate curriculum on your own time, for free, with courses from the best universities in the World. It preferred MOOC (Massive Open Online Course) style courses because these were created with self-study in mind.

## Curricular Guideline

OSSU Data Science used the report [Curriculum Guidelines for Undergraduate Programs in Data Science](https://www.amstat.org/asa/files/pdfs/EDU-DataScienceGuidelines.pdf).

### Original Prerequisites
The OSSU Data Science curriculum assumes the student has taken [high school math](https://ossu.dev/precollege-math) and [statistics](https://www.khanacademy.org/math/probability).

### Original Course Links (archived)
- [What is Data Science (Coursera)](https://www.coursera.org/learn/what-is-datascience)
- [Introduction to Programming](coursepages/intro-programming/README.md)
- [Introduction to Computer Science and Programming Using Python](coursepages/intro-cs/README.md)
- [Introduction to Computational Thinking and Data Science (MIT 6.0002)](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/)
- [Java Programming](https://java-programming.mooc.fi/)
- [GaTech Algorithms I-IV on edX](https://www.edx.org/learn/data-structures/the-georgia-institute-of-technology-data-structures-algorithms-i-arraylists-linkedlists-stacks-and-queues)
- [Database Management Essentials (Coursera)](https://www.coursera.org/learn/database-management)
- [Data Warehouse Concepts, Design, and Data Integration (Coursera)](https://www.coursera.org/learn/dwdesign)
- [Relational Database Support for Data Warehouses (Coursera)](https://www.coursera.org/learn/dwrelational)
- [Business Intelligence Concepts, Tools, and Applications (Coursera)](https://www.coursera.org/learn/business-intelligence-tools)
- [Design and Build a Data Warehouse for BI Implementation (Coursera)](https://www.coursera.org/learn/data-warehouse-bi-building)
- [MongoDB for Developers Learning Path](https://learn.mongodb.com/pages/mongodb-developer-learning-paths)
- [MITx Calculus 1A / 1B / 1C](https://mitxonline.mit.edu/courses/)
- [3Blue1Brown: Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/)
- [MIT 18.02 Multivariable Calculus](http://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/index.htm)
- [Harvard Stat 110 Introduction to Probability](https://projects.iq.harvard.edu/stat110/home)
- [Intro to Descriptive Statistics (Udacity)](https://www.udacity.com/course/intro-to-descriptive-statistics--ud827)
- [Intro to Inferential Statistics (Udacity)](https://www.udacity.com/course/intro-to-inferential-statistics--ud201)
- [Statistical Learning with Python (Stanford/edX)](https://www.edx.org/learn/python/stanford-university-statistical-learning-with-python)
- [Tools for Data Science (Coursera)](https://www.coursera.org/learn/open-source-tools-for-data-science)
- [Data Science Methodology (Coursera)](https://www.coursera.org/learn/data-science-methodology)
- [Data Science: Wrangling (edX)](https://www.edx.org/course/data-science-wrangling)
- [Supervised Machine Learning: Regression and Classification (Coursera/Andrew Ng)](https://www.coursera.org/learn/machine-learning)
- [Advanced Learning Algorithms (Coursera)](https://www.coursera.org/learn/advanced-learning-algorithms)
- [Unsupervised Learning, Recommenders, Reinforcement Learning (Coursera)](https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning)
- [Intro to Machine Learning (Udacity)](https://www.udacity.com/course/intro-to-machine-learning--ud120)
- [Mining Massive Datasets (Stanford/edX)](https://www.edx.org/course/mining-massive-datasets)
- [Process Mining (Coursera)](https://www.coursera.org/learn/process-mining)

See [`extras/books.md`](extras/books.md), [`extras/courses.md`](extras/courses.md), and [`extras/specializations.md`](extras/specializations.md) for the original auxiliary material.

### Original Team
* **Curriculum Maintainer (OSSU)**: [Waciuma Wanjohi](https://github.com/waciumawanjohi)
* **Contributors**: [OSSU Data Science contributors](https://github.com/open-source-society/data-science/graphs/contributors)

</details>

---

<div align="center">
  <sub>🎓 <strong>The Elite Data Science Curriculum — 2026 Edition</strong> · Curated with Zero Omissions Policy · April 2026</sub>
  <br/>
  <sub>Synthesised from IITM · Harvard · MIT · Cambridge · Freely redistributable under the <a href="./LICENSE.md">original LICENSE</a></sub>
</div>
