# Module 6½ — Causal Inference & Experimentation

> **Status:** v2026.2 scaffold · full spec in the root [README.md § Module 6½](../../README.md#module-6-causal-inference--experimentation-new--v20262).
>
> This folder will hold problem sets, notebooks, and reading-group notes for Module 6½. The root README holds the authoritative topic list and resource links.

## Why this module exists

The April 2026 benchmark against Berkeley MIDS / MIT 6.390 / UC-industry DS job-specs identified **Causal Inference & A/B testing** as the single largest production-DS gap versus theory-heavy curricula. This module closes that gap.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| Brady Neal — *Introduction to Causal Inference* (Fall 2020, free) | Primary course | <https://www.bradyneal.com/causal-inference-course> |
| MIT 14.387 — *Applied Econometrics (Mostly Harmless Big Data)* | Econometric track | <https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/> |
| Matheus Facure — *Causal Inference for the Brave and True* | Runnable notebooks | <https://matheusfacure.github.io/python-causality-handbook/landing-page.html> |
| Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments* (Cambridge 2020) | Industrial A/B-testing canon | <https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59> |
| Hernán & Robins — *Causal Inference: What If* (free 2024 revision) | Graduate text | <https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf> |
| Berkeley MIDS DATA 241 — Causal Inference | University benchmark course | <https://www.ischool.berkeley.edu/courses/datasci/241> |
| DoWhy (py-why) | End-to-end Python stack | <https://github.com/py-why/dowhy> |
| EconML (Microsoft) | Heterogeneous treatment effects | <https://econml.azurewebsites.net/> |
| CausalML (Uber) | Uplift modelling | <https://causalml.readthedocs.io/> |
| exp-platform.com (Ron Kohavi) | Industrial experimentation blog | <https://exp-platform.com/> |

## Mandatory mini-projects

1. Simulate an A/B test with CUPED variance reduction; measure the sample-size reduction.
2. Fit an IV regression on Angrist-Krueger 1991 compulsory-schooling; reproduce the returns-to-education estimate.
3. Use DoWhy end-to-end (model → identify → estimate → refute) on a confounded synthetic dataset; show refutation tests.
4. Train a Causal Forest on a public dataset (lalonde / criteo-uplift); plot HTE heatmap and evaluate a targeting policy via doubly-robust off-policy estimation.

## Prerequisites

- Module 5 (probability), Module 6 (hypothesis testing + bootstrap)

## Next step

→ Module 7 (Data Wrangling & EDA — Polars/DuckDB modernisation) or → Module 21 (RAG) once M9–M12 are done.
