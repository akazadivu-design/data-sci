# 📋 P0 — Baseline Audit & Gap-to-Line Traceability Matrix

**Date:** 2026-04-23  
**Input:** Spark PDF *"Data science curriculum benchmarking and gap analysis request"* (15 pp, 21 sources cited)  
**Target:** `akazadivu-design/data-sci` (this repo) — currently v2026 Edition, 21 modules, 1397-line README

---

## Current Module Inventory (from README.md)

| Line | Module | Status per PDF |
|---:|---|---|
| 341 | **M0** — Mathematical Maturity Bridge | ✅ Elite (unique differentiator) |
| 402 | **M1** — Programming Foundations | ✅ Strong, one addition needed |
| 433 | **M2** — Calculus + Matrix Calc + Convex Opt | ✅ Elite |
| 476 | **M3** — Linear Algebra | ✅ Elite |
| 519 | **M4** — Discrete Math, Algorithms & DSA | ✅ Strong |
| 544 | **M5** — Probability Theory | ✅ Elite |
| 609 | **M6** — Statistical Inference | ⚠️ Strong, major addition needed (A/B + causal) |
| 639 | **M7** — Data Wrangling, EDA & Visualisation | ⚠️ Theory-heavy, hands-on light |
| 667 | **M8** — Databases, SQL & Big Data | 🔴 Needs a rewrite (biggest classical gap) |
| 697 | **M9** — Supervised Regression | ✅ Elite |
| 726 | **M10** — Supervised Classification & Kernels | ✅ Elite (add calibration) |
| 756 | **M11** — Unsupervised & Dim. Reduction | ✅ Elite |
| 784 | **M12** — Ensembles & Boosting | ✅ Strong |
| 816 | **M13** — Bayesian / PGM / MCMC | ✅ Elite (add PyMC5 + NumPyro) |
| 848 | **M14** — Sequence Modelling & Time Series | ✅ Strong (add foundation models) |
| 882 | **M15** — Deep Learning Foundations | ✅ Elite (add JAX/Flax + FSDP) |
| 922 | **M16** — Transformers & Generative | ⚠️ Needs 2026 refresh (ViT, Diffusion, SSMs, MoE) |
| 968 | **M17** — Reinforcement Learning | ⚠️ Solid, add PPO/GRPO/DPO/RLVR |
| 1005 | **M18** — LLMs, RLHF & Alignment | ⚠️ Delegates to CS336 — add app layer |
| 1044 | **M19** — MLOps, Scaling, Systems | 🔴 Thinnest module; biggest production gap |
| 1081 | **M20** — Capstone | ⚠️ Good concept, add rubric |

---

## PDF's 13 Gaps → Target Location Map

| # | Gap (PDF priority order) | Size | Action | Target Location |
|---:|---|:---:|---|---|
| 1 | **Causal Inference / A/B Testing** dedicated module | L | **NEW M7** (shift others down) | Insert between current M6 & M7 (line ~639) |
| 2 | **Modern Data Engineering** (Spark/dbt/Airflow/Kafka) | L | **Split M8 into M9+M10** (DE-I + DE-II) | Rewrite lines 667–696 |
| 3 | **LLMOps + AgentOps** | M | Expand M19 → new **M24** | Rewrite lines 1044–1080 |
| 4 | **Agentic AI** (LangGraph/CrewAI/MCP/A2A) | M | **NEW M22** | Insert after M20 (old LLMs module) |
| 5 | **RAG + Vector DBs** chapter | S | **NEW M21** | Insert after M20 |
| 6 | **AI Safety, Alignment & Evals** | M | **NEW M23** | Insert after M22 |
| 7 | **Product DS / Communication** | S | **NEW M25** | Insert after M24 |
| 8 | **Modern Tooling** (Polars, DuckDB, uv, JAX) | S | Modernize M7 (EDA) + M1 (Python) + M15 (DL) + add **Tooling Appendix** | Multi-point edits |
| 9 | **ViT + Diffusion Models** | M | Expand M16 (→ new M18) | Rewrite lines 922–967 |
| 10 | **Time-Series Foundation Models** (Chronos, TimeGPT, Lag-Llama) | S | Expand M14 (→ new M16) | Add subsection to lines 848–881 |
| 11 | **Fine-Tuning Playbook** (LoRA/QLoRA/DPO/GRPO/RLVR) | S | Expand M18 (→ new M20) | Rewrite lines 1005–1043 |
| 12 | **Mechanistic Interpretability** (SAEs, circuits) | S | Add to new M23 (Safety) | In NEW M23 |
| 13 | **Ethics, Privacy & AI Policy** | S | Add to new M23 (Safety) | In NEW M23 |

---

## Per-Module Additions (PDF verbatim)

### M0 — Elite (verify only, no change)
Verify coverage: ε-δ limit proofs, graph theory basics, combinatorics (inclusion-exclusion, generating functions).

### M1 — Add Modern Python Tooling
- Type hints + `mypy` / Pydantic
- `uv` / `poetry` package management (pip no longer default in 2026)
- `async` / `asyncio` (mandatory for agents)
- Git + GitHub Actions fundamentals
- Testing with `pytest` + `hypothesis` property-based testing

### M2 — Optional Add
- Automatic differentiation theory (forward/reverse-mode, JVP/VJP)

### M3 — Optional Add
- Numerical linear algebra (LU, QR, Householder, CG) — Trefethen & Bau

### M4 — Add
- Randomized algorithms (bloom filters, MinHash, reservoir sampling)
- Amortized analysis
- Approximation algorithms

### M5 — Elite (optional add)
- Empirical process theory / VC theory (Mohri, Rostamizadeh, Talwalkar bridge)

### M6 — Stays, but preface that causal material moves to new M7

### **NEW M7 — Causal Inference & Experimentation**
- A/B testing (sample size, MDE, sequential, CUPED, interference, switchback)
- Multiple testing correction (Bonferroni, BH-FDR)
- Bootstrap & permutation tests
- Bayesian A/B testing
- DAGs, do-calculus, backdoor/frontdoor, instrumental variables
- DiD, RDD, synthetic controls
- **Primary anchors (from PDF):** Harvard CAUSALab, Brady Neal's course, Matheus Facure *CIBT*, MIT 14.387

### M8 (new name: Modernize current M7 EDA) — Add
- Polars (2026 pandas successor)
- DuckDB
- Great Expectations / Pandera
- Plotly / Altair / Observable Plot
- Streamlit + Gradio + Evidently
- Feature engineering as a discipline (target encoding, leakage, time-based features)

### **NEW M9 — Data Engineering I (SQL & Warehouses)**
- Advanced SQL (window, CTEs, recursive, plans, partitioning)
- Snowflake / BigQuery / Redshift / DuckDB
- dbt (tests, macros, incremental models)
- Kimball dimensional modeling, star/snowflake schemas, SCDs
- **Primary anchor:** Joe Reis *Fundamentals of Data Engineering*, DataExpert.io free bootcamp

### **NEW M10 — Data Engineering II (Distributed & Streaming)**
- Parquet, Iceberg, Delta Lake, S3/GCS, lakehouse
- Spark/PySpark, Ray Data, Dask
- Airflow, Dagster, Prefect
- Kafka, Flink, Redpanda

### M11–M14 — Classical ML (mostly keep)
- Add `sklearn` Pipelines + ColumnTransformer hands-on (M11–M14)
- Add calibration (Platt, isotonic) to M12
- Add PyMC 5 + NumPyro to M15 (Bayesian)
- Add Prophet, NeuralProphet, TimeGPT, Chronos, Lag-Llama, N-BEATS, N-HiTS, Temporal Fusion Transformer to M16 (Sequence)

### M17 — DL Foundations (modernize)
- JAX + Flax alongside PyTorch
- Mixed-precision, gradient checkpointing, FSDP

### **M18 — Representation Learning / Transformers (expand)**
- Vision Transformers (ViT, DINOv2, SAM 2)
- Diffusion models from scratch (DDPM, DDIM, score-matching, flow-matching, rectified flow)
- Multimodal models (CLIP, LLaVA, Qwen-VL)
- State-space models (Mamba, Mamba-2, RWKV)
- Mixture-of-Experts (MoE) — explicitly named

### **M19 — RL (modernize)**
- PPO / GRPO / DPO (DPO in M19 + M20)
- RLVR (Reinforcement Learning from Verifiable Rewards) — DeepSeek-R1, o-series
- Offline RL (CQL, IQL, decision transformers)
- Hands-on: CleanRL or Stable-Baselines3

### **M20 — LLMs from Scratch + Fine-Tuning Playbook**
- CS336 track (tokenization → architectures → parallelism → scaling → RLHF/DPO → data)
- **Application layer CS336 omits:**
  - RAG engineering (moved to M21)
  - Vector DBs (moved to M21)
  - Fine-tuning playbook: LoRA, QLoRA, DoRA, cost curves, Unsloth, Axolotl
  - Prompt compilation: DSPy, TextGrad
  - Inference optimization: vLLM, TensorRT-LLM, SGLang, speculative decoding, KV-cache
  - Lifecycle evals: LLM-as-judge, rubric-based, adversarial, promptfoo / DeepEval / Ragas

### **NEW M21 — RAG, Vector DBs & Retrieval Systems**
- Chunking strategies, hybrid search (BM25 + dense), rerankers (Cohere, BGE), late chunking, ColBERT, ColPali
- Vector DBs: pgvector, Qdrant, Weaviate, Milvus, LanceDB (HNSW, IVF trade-offs)
- **Primary anchor:** Pinecone DL course, LlamaIndex docs, Jerry Liu RAG taxonomy

### **NEW M22 — Agentic AI**
- LangGraph, CrewAI, MCP (Model Context Protocol), A2A (Agent-to-Agent)
- GAIA benchmark, SWE-bench, τ-bench
- Sandboxing & tool-execution safety (E2B, Daytona, Modal)
- **Primary anchor:** HuggingFace AI Agents Course, Anthropic "Building Effective Agents", Berkeley LLM Agents MOOC

### **NEW M23 — AI Safety, Alignment, Interpretability, Evals & Policy**
- Outer/inner alignment, interpretability, evals
- Mechanistic interpretability (SAEs, circuits)
- Ethics, Privacy, AI Policy: EU AI Act, NIST AI RMF, model cards
- **Primary anchor:** MIT AISF Spring 2026, Anthropic Interpretability posts, EleutherAI cookbook

### **NEW M24 — MLOps + LLMOps + AgentOps (evolving disciplines)**
- **MLOps:** Docker/K8s, CI/CD (GH Actions, Jenkins, CML), MLflow / W&B / Neptune, Feature stores (Feast, Tecton), model registry, monitoring (Evidently, Arize, WhyLabs — drift, PSI), serving (BentoML, KServe, Ray Serve, Triton)
- **LLMOps:** Prompt versioning (Langfuse, PromptLayer, Helicone), token/cost monitoring, guardrails (Nemo Guardrails, Guardrails AI, Llama Guard), PII, OpenTelemetry GenAI
- **AgentOps:** Agent tracing (LangSmith, Arize Phoenix, W&B Weave), GAIA/SWE-bench/τ-bench harnesses, sandboxing (E2B, Daytona, Modal)
- **Primary anchor:** Full Stack Deep Learning LLM Bootcamp, Chip Huyen *DMLS* + *AI Engineering* (2025), Made With ML

### **NEW M25 — Product DS, Business, Communication & Storytelling**
- **Primary anchor:** CMU MADS Professional Skills sequence, Cassie Kozyrkov decision intelligence

### **M26 — Capstone — THREE TRACKS with rubric**
1. **Research track** — arXiv + NeurIPS/ICML workshop pipeline
2. **Systems track** — end-to-end production system with SLOs
3. **Applied track** — sponsored/real business problem with causal evaluation
- **Rubric reference:** Berkeley MIDS capstone + CS336 Assignment 5

---

## Global Additions

- **"2026 Tooling" Appendix:** Polars, DuckDB, uv, JAX, Qdrant, vLLM, LangGraph, dbt

## Protected / Must-Not-Touch (per PDF §7)

1. **Module 0 (Math Maturity Bridge)** — "your moat. Don't let anyone convince you to delete it."
2. **Measure-theoretic probability + concentration inequalities in M5** — "stronger than most MS programs."
3. **Two-pass Linear Algebra (Strang + Axler) in M3** — "extremely rare in bootcamps."

---

## Final Target Architecture (v2026.2 — 26 modules + M0)

```
STRATUM 0 — Mathematical Maturity
  M0   Pre-Calc, Logic, Proof, Discrete Math                     [keep]

STRATUM 1 — Foundation
  M1   Programming Foundations + Modern Python Tooling           [EXPAND]
  M2   Calculus + Matrix Calc + Convex Opt + Autodiff            [small add]
  M3   Linear Algebra + Numerical LA                             [small add]
  M4   DSA + Randomized & Approximation Algorithms               [expand]
  M5   Probability (Stat110 + measure + concentration)           [keep]

STRATUM 2 — Statistics & Data
  M6   Statistical Inference                                     [keep]
  M7   ⭐ NEW: Causal Inference & Experimentation
  M8   EDA & Visualisation (Polars, DuckDB, Plotly, Streamlit)   [MODERNIZE]
  M9   ⭐ NEW: Data Engineering I — SQL & Warehouses
  M10  ⭐ NEW: Data Engineering II — Distributed & Streaming

STRATUM 3 — Classical ML
  M11  Supervised Regression                                     [keep]
  M12  Supervised Classification & Kernels + Calibration         [small add]
  M13  Unsupervised & Dim. Reduction                             [keep]
  M14  Ensembles & Boosting                                      [keep]

STRATUM 4 — Probabilistic
  M15  Bayesian Inference, PGMs, MCMC (+ PyMC/NumPyro)           [modernize]
  M16  Sequence Models + Modern TS (Chronos, TimeGPT, Lag-Llama) [modernize]

STRATUM 5 — Deep Learning
  M17  DL Foundations (PyTorch + JAX, FSDP, mixed-prec)          [modernize]
  M18  Representation Learning + ViT + Diffusion + SSMs + MoE    [EXPAND]
  M19  Reinforcement Learning + PPO/GRPO/DPO/RLVR                [modernize]

STRATUM 6 — Frontier
  M20  LLMs from Scratch (CS336) + Fine-Tuning Playbook          [expand]
  M21  ⭐ NEW: RAG, Vector DBs & Retrieval Systems
  M22  ⭐ NEW: Agentic AI (LangGraph, CrewAI, MCP, A2A, GAIA)
  M23  ⭐ NEW: AI Safety, Alignment, Interpretability, Evals & Policy

STRATUM 7 — Production & Delivery
  M24  MLOps + LLMOps + AgentOps                                 [REWRITE from old M19]
  M25  ⭐ NEW: Product DS, Business, Communication & Storytelling
  M26  Capstone (3 tracks: Research / Systems / Applied)         [rubric added]
```

**Net change:** +6 modules (7/9/10/21/22/23/25), 2 full rewrites (8 modernize, 24 MLOps→all-Ops), 0 deletions. Spine preserved.

---

## Remaining Phase 0 Deliverables

✅ Inventory complete  
✅ Gap-to-line traceability done  
✅ Per-module additions extracted from PDF  
✅ Protected spine identified  
✅ Target architecture locked

**Next (Phase 1):** Cross-verify every PDF-cited URL, book, and framework version against the live web. Nothing enters the README from this doc until P1 gives it a ✅.
