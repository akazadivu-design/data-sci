# 🎨 P2 — Improvement Specification (v2026.2)

**Target:** Transform the README from the current 21-module "theory-first" curriculum into the v2026.2 **26-module** spec the PDF recommends — without weakening the math spine.

**Guiding principles:**
1. **Preserve what's ✅ Elite.** Do not rewrite M0, M2, M3, M5, M9-M12, M13, M15 content — the PDF explicitly approves these.
2. **Expand, don't replace.** Add new topic bullets + verified anchor URLs to existing modules.
3. **New modules use the same format.** Identical structure: "The Tutor's Why" / Prereqs / Exhaustive Topic List / Resources.
4. **Every URL is P1-verified.** No resource enters without a 2026-04-23 ✅ in `VERIFICATION.md`.
5. **Preserve backward compatibility where cheap.** Keep existing anchor names; add new ones.

---

## Strategy: Minimal-Diff Renumbering

Renumbering all 20 modules risks breaking anchors and internal links. Instead:

| Option | Pro | Con | Choice |
|---|---|---|---|
| **Full renumber** (M1–M26) | Clean numbering matches PDF exactly | Breaks every `#module-X` link + TOC + progress tracker | ❌ |
| **Append-only** (keep M1–M20, add M21–M26 for new frontier content) | Zero-risk, additive | Doesn't capture the "Split M8" / "New M7 Causal" intent | ❌ |
| **🎯 Hybrid (chosen)**: Keep M0–M20 numbering intact; add new modules as **M21-M26** + **promote Causal out of M6 as M6.5** + **split M8 into M8a/M8b** | Preserves anchors; still implements PDF's intent; explicit cross-refs to PDF's 26-module plan in a dedicated "v2026.2 Architecture" table | Small numbering friction vs PDF | ✅ |

**Result:** The README will carry:
- Original 21 modules (**M0–M20**) updated with new content + verified URLs
- NEW: **Module 6½ — Causal Inference & Experimentation** (sits between M6 and M7 semantically; PDF's "M7")
- **Module 8 becomes 8a (DB/SQL) + 8b (Distributed & Streaming)**
- NEW sections: **M21 RAG**, **M22 Agentic**, **M23 AI Safety**, **M24 MLOps/LLMOps/AgentOps**, **M25 Product DS** — numbering now matches PDF
- **M20** Capstone (original) stays last; renamed internally to be consistent with PDF's "M26" → README uses both numbers in a mapping table

A **"v2026.2 Architecture Map"** table at the top shows the README-number ↔ PDF-number mapping so readers are never confused.

---

## The Concrete Edit List (by section)

### Edit 1 — Top Banner

* Bump version badge: `2026 Edition` → `2026.2 Edition (Production Superstructure Pass)`
* Add badge: `26 Modules · 150+ Live-Verified Links · April 23 2026`

### Edit 2 — Preamble (line 16)

Add a short paragraph introducing the v2026.2 rationale ("benchmark report against Berkeley MIDS / MIT 6.390 / Stanford CS336 / HF Agents / 2026 agentic roadmap / MIT AISF / CMU MSPPM-DA revealed a production gap — v2026.2 patches it").

### Edit 3 — Refresh Log (line 28)

Insert a **"🎯 April 2026.2 Production Superstructure Pass"** subsection documenting:
- 13 gaps identified via benchmark PDF → all closed
- 6 new modules (6½, 8b split, 21–25)
- Version bumps (JAX 0.10, sklearn 1.8, vLLM 0.19, new frameworks added)
- 3 PDF errors corrected: CMU MADS phrasing, mitaisafety.com URL, FSDP docs URL
- 150+ newly verified URLs

### Edit 4 — TOC (line 129)

Insert new entries:
- Module 6½ Causal Inference
- Module 8a / 8b split
- Module 21 RAG
- Module 22 Agentic AI
- Module 23 AI Safety & Evals
- Module 24 MLOps/LLMOps/AgentOps (renames & supersedes old M19)
- Module 25 Product DS
- Module 26 Capstone (formerly M20)
- "2026 Tooling" appendix already exists, will be expanded

### Edit 5 — Progression Map ASCII (line 170)

Replace the 20-module diagram with a 26-module + M0 diagram that adds the new rows. Keep the same visual style (ASCII boxes).

### Edit 6 — Meta-Information (line 197)

Bump frameworks table:
- PyTorch 2.11.0 ✅ (keep)
- JAX 0.7.x → **0.10.0**
- scikit-learn 1.7+ → **1.8.0**
- Add: uv 0.11 · dbt-core 1.11 · DuckDB 1.5 · MLflow 3.11 · LangGraph 1.1 · smolagents 1.24 · DSPy 3.2 · TRL 1.2 · PEFT 0.19 · Qdrant-client 1.17 · PyMC 5.28 · NumPyro 0.20

### Edit 7 — Module 1 (line 402)

Add sub-section **"🛠 Modern Python Tooling (2026 addendum)"** with verified links:
- Type hints + `mypy` + Pydantic
- `uv` package manager
- `async`/`asyncio`
- Git + GitHub Actions
- `pytest` + `hypothesis` (property-based)

### Edit 8 — Module 2 (line 433)

Add **"Automatic Differentiation Theory"** sub-section (forward/reverse-mode, JVP/VJP).  
No new URL needed beyond JAX/PyTorch; reference MIT 18.S096 which is already cited.

### Edit 9 — Module 3 (line 476)

Add **"Numerical Linear Algebra"** sub-section (LU, QR, Householder, CG).  
Anchor: Trefethen & Bau book entry #33 already in reading list.

### Edit 10 — Module 4 (line 519)

Add three items to topic list:
- Randomized algorithms (bloom filters, MinHash, reservoir sampling)
- Amortized analysis
- Approximation algorithms

### Edit 11 — Module 6 (line 609)

Insert a note at the bottom: "→ A/B testing, experimental design, and causal inference now have a **dedicated Module 6½** below."

### Edit 12 — **NEW Module 6½ — Causal Inference & Experimentation** (inserted after line ~638)

Full module with:
- Tutor's Why (senior DS interviews at FAANG test this; Berkeley MIDS has a whole course; Netflix/Meta hire specifically)
- Prereqs: M5, M6
- Topic list:
  - A/B testing: sample size, MDE, sequential testing, CUPED variance reduction, interference, switchback experiments
  - Multiple testing: Bonferroni, BH-FDR
  - Bootstrap & permutation tests
  - Bayesian A/B testing
  - Causal graphs (DAGs), d-separation, do-calculus
  - Backdoor / frontdoor adjustment, IV, DiD, RDD, synthetic controls
  - Python stack: DoWhy, EconML, CausalML, Pyro
- Resources:
  - [Brady Neal — Intro to Causal Inference](https://www.bradyneal.com/causal-inference-course) ✅
  - [Harvard CAUSALab](https://www.hsph.harvard.edu/causal/) ✅
  - [Matheus Facure — CIBT](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) ✅
  - [MIT 14.387 Applied Econometrics](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) ✅
  - [DoWhy](https://github.com/py-why/dowhy) ✅
  - [EconML](https://econml.azurewebsites.net/) ✅
  - [CausalML](https://causalml.readthedocs.io/) ✅
  - [Kohavi — Trustworthy Online Controlled Experiments](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) ✅
  - [exp-platform.com](https://exp-platform.com/) ✅

### Edit 13 — Module 7 (line 639) — "🔧 2026 Tooling Modernization"

Add sub-section:
- **Polars** (pandas successor) ✅
- **DuckDB** (SQLite for analytics) ✅
- **Great Expectations / Pandera** (data validation) ✅
- **Plotly / Altair / Observable Plot** ✅
- **Streamlit + Gradio + Evidently** (dashboards) ✅
- **Feature engineering discipline**: target encoding, leakage, time-based features (citation to Feature Engineering book / sklearn Pipelines)

### Edit 14 — Module 8 (line 667) — Split into M8a + M8b

Keep the module heading. Split the content into two explicit sub-modules:
- **Module 8a — Databases & SQL (Warehouses)**:
  - Advanced SQL (window functions, CTEs, recursive, query plans, partitioning)
  - Warehouses: Snowflake, BigQuery, Redshift, DuckDB ✅
  - Transform: dbt (tests, macros, incremental models) ✅
  - Modeling: Kimball dimensional modeling, star/snowflake schemas, SCDs ✅
- **Module 8b — Distributed Data & Streaming Systems**:
  - Storage: Parquet, Iceberg, Delta Lake, S3/GCS, lakehouse ✅
  - Processing: Spark/PySpark, Ray Data, Dask ✅
  - Orchestration: Airflow, Dagster, Prefect ✅
  - Streaming: Kafka, Flink, Redpanda ✅
- Resources:
  - [Reis & Housley — *Fundamentals of Data Engineering*](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ✅
  - [DataExpert.io handbook (free)](https://github.com/DataExpert-io/data-engineer-handbook) ✅
  - [DataExpert free bootcamp](https://www.dataexpert.io/free-data-engineer-bootcamp) ✅
  - Kimball Group, Joe Reis Substack ✅

### Edit 15 — Module 10 (line 726)

Add **Calibration** sub-topic: Platt scaling, isotonic regression, reliability diagrams, Brier score. Reference `sklearn.calibration` + book: *Forecasting: Principles and Practice* (Hyndman, already in Tier 2 list).

### Edit 16 — Module 13 (line 816)

Add **2026 probabilistic programming** note: PyMC 5.28 + NumPyro 0.20 (JAX-backed, the 2026 standard).

### Edit 17 — Module 14 (line 848) — Time Series Foundation Models

Add "2026 Frontier Additions" sub-section:
- [Prophet](https://facebook.github.io/prophet/) / [NeuralProphet](https://neuralprophet.com/) ✅
- [TimeGPT / Nixtla](https://www.nixtla.io/) ✅
- [Amazon Chronos](https://github.com/amazon-science/chronos-forecasting) ✅
- [Lag-Llama](https://github.com/time-series-foundation-models/lag-llama) ✅
- N-BEATS, N-HiTS, Temporal Fusion Transformer
- Practical anomaly detection at scale

### Edit 18 — Module 15 (line 882) — JAX Alongside PyTorch + Systems

Add "2026 DL systems" sub-section:
- **JAX + Flax** alongside PyTorch (mainstream at Google/DeepMind/Anthropic) ✅
- Mixed-precision training
- Gradient checkpointing
- **FSDP / FSDP2** (verified URL: https://pytorch.org/docs/stable/fsdp.html) ✅

### Edit 19 — Module 16 (line 922) — Add ViT, Diffusion, SSMs, MoE

Add topics:
- **Vision Transformers** (ViT, DINOv2, SAM 2) — [DINOv2](https://github.com/facebookresearch/dinov2) ✅ · [SAM 2](https://github.com/facebookresearch/sam2) ✅
- **Diffusion from scratch** (DDPM, DDIM, score-matching, flow-matching, rectified flow) — already in UDL book
- **Multimodal** (CLIP, LLaVA, Qwen-VL) — [CLIP](https://github.com/openai/CLIP) ✅ · [LLaVA](https://github.com/haotian-liu/LLaVA) ✅
- **State-Space Models** (Mamba, Mamba-2, RWKV) — [Mamba](https://github.com/state-spaces/mamba) ✅ · [RWKV](https://github.com/BlinkDL/RWKV-LM) ✅
- **Mixture-of-Experts** — explicitly named

### Edit 20 — Module 17 (line 968) — Modern RL

Add topics:
- **PPO / GRPO / DPO** (DPO in M17 + M18)
- **RLVR** (DeepSeek-R1, o-series reasoning models)
- **Offline RL** (CQL, IQL, Decision Transformers)
- Hands-on: [CleanRL](https://github.com/vwxyzjn/cleanrl) ✅ or [Stable-Baselines3](https://stable-baselines3.readthedocs.io/) ✅
- Supplement: [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) ✅, [Spinning Up](https://spinningup.openai.com/) ✅

### Edit 21 — Module 18 (line 1005) — Add Fine-Tuning Playbook + App Layer

Add sub-sections (CS336 stays for foundation):
- **Fine-Tuning Playbook**: LoRA, QLoRA, DoRA, cost curves, [Unsloth](https://github.com/unslothai/unsloth) ✅, [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) ✅, [TRL](https://github.com/huggingface/trl) ✅, [PEFT](https://github.com/huggingface/peft) ✅
- **Prompt Compilation**: [DSPy](https://github.com/stanfordnlp/dspy) ✅, [TextGrad](https://github.com/zou-group/textgrad) ✅
- **Inference Optimization**: [vLLM](https://docs.vllm.ai/) ✅, [SGLang](https://github.com/sgl-project/sglang) ✅, [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) ✅, speculative decoding, KV-cache tricks
- **Lifecycle Evals**: [promptfoo](https://github.com/promptfoo/promptfoo) ✅ · [DeepEval](https://github.com/confident-ai/deepeval) ✅ · [Ragas](https://github.com/explodinggradients/ragas) ✅ · [OpenAI evals](https://github.com/openai/evals) ✅ · [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness) ✅

### Edit 22 — Module 19 (line 1044) — TRANSFORM INTO M24 (MLOps+LLMOps+AgentOps)

**This is the biggest rewrite.** Replace the existing thin content with three organised tiers:

**MLOps (classical):**
- Docker + Kubernetes fundamentals
- CI/CD: GH Actions, Jenkins, CML
- Experiment tracking: [MLflow](https://mlflow.org/) ✅, [W&B](https://wandb.ai/) ✅, Neptune
- Feature stores: [Feast](https://feast.dev/) ✅, [Tecton](https://www.tecton.ai/) ✅
- Model registry + versioning
- Monitoring: [Evidently](https://www.evidentlyai.com/) ✅, [Arize](https://arize.com/) ✅, [WhyLabs](https://whylabs.ai/) ✅ (drift, PSI)
- Serving: [BentoML](https://www.bentoml.com/) ✅, [KServe](https://kserve.github.io/website/) ✅, [Ray Serve](https://docs.ray.io/en/latest/serve/) ✅, [Triton](https://developer.nvidia.com/nvidia-triton-inference-server) ✅

**LLMOps (2024–2026):**
- Prompt versioning: [Langfuse](https://langfuse.com/) ✅, [PromptLayer](https://promptlayer.com/) ✅, [Helicone](https://www.helicone.ai/) ✅
- Token/cost monitoring & budgeting
- Guardrails: [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) ✅, [Guardrails AI](https://www.guardrailsai.com/) ✅, [Llama Guard](https://github.com/meta-llama/PurpleLlama) ✅
- LLM observability & tracing: [OTel GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) ✅

**AgentOps (2025–2026):**
- Agent tracing: [LangSmith](https://www.langchain.com/langsmith) ✅, [Arize Phoenix](https://github.com/Arize-ai/phoenix) ✅, [W&B Weave](https://wandb.ai/site/weave) ✅
- Agent eval harnesses: [GAIA](https://huggingface.co/gaia-benchmark) ✅, [SWE-bench](https://www.swebench.com/) ✅, τ-bench
- Sandboxing: [E2B](https://e2b.dev/) ✅, [Daytona](https://www.daytona.io/) ✅, [Modal](https://modal.com/) ✅

Primary anchors: [FSDL](https://fullstackdeeplearning.com/) ✅, [Chip Huyen *AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) ✅ (already in Tier 1), [Made With ML](https://madewithml.com/) ✅

### Edit 23 — **NEW Module 21 — RAG, Vector DBs & Retrieval Systems** (insert after old M18)

Full module:
- Chunking strategies, hybrid search (BM25+dense), rerankers (Cohere, BGE), late chunking, [ColBERT](https://github.com/stanford-futuredata/ColBERT)/ColPali ✅
- Vector DBs: [pgvector](https://github.com/pgvector/pgvector) ✅, [Qdrant](https://qdrant.tech/) ✅, [Weaviate](https://weaviate.io/) ✅, [Milvus](https://milvus.io/) ✅, [LanceDB](https://lancedb.com/) ✅
- Indexing: HNSW, IVF, trade-offs
- Primary anchors: [Pinecone Learning](https://www.pinecone.io/learn/) ✅, [LlamaIndex docs](https://docs.llamaindex.ai/) ✅

### Edit 24 — **NEW Module 22 — Agentic AI**

Full module:
- [LangGraph](https://www.langchain.com/langgraph) ✅
- [CrewAI](https://docs.crewai.com/) ✅
- [MCP](https://modelcontextprotocol.io/) ✅ (latest: [2025-06-18 spec](https://modelcontextprotocol.io/specification/2025-06-18) ✅)
- A2A (Agent-to-Agent)
- [smolagents](https://github.com/huggingface/smolagents) ✅
- [GAIA benchmark](https://huggingface.co/gaia-benchmark) ✅
- [SWE-bench](https://www.swebench.com/) ✅
- Sandboxing: [E2B](https://e2b.dev/) ✅, [Daytona](https://www.daytona.io/) ✅, [Modal](https://modal.com/) ✅
- Primary anchors: [HF AI Agents Course](https://huggingface.co/learn/agents-course/) ✅, [Anthropic Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) ✅, [Berkeley LLM Agents MOOC](https://llmagents-learning.org/) ✅

### Edit 25 — **NEW Module 23 — AI Safety, Alignment, Interpretability, Evals & Policy**

Full module:
- Outer/inner alignment
- Mechanistic interpretability — SAEs, circuits, [transformer-circuits.pub](https://transformer-circuits.pub/) ✅, [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/) ✅, [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude) ✅
- Eval harnesses: [OpenAI evals](https://github.com/openai/evals) ✅, [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness) ✅, [HF Open LLM Leaderboard](https://huggingface.co/open-llm-leaderboard) ✅
- Policy: [EU AI Act](https://artificialintelligenceact.eu/) ✅, [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) ✅, [AI.gov](https://ai.gov/) ✅, model cards, datasheets
- Primary anchors: [AISF](https://aisafetyfundamentals.com/alignment/) ✅, [EleutherAI cookbook](https://github.com/EleutherAI/cookbook) ✅

### Edit 26 — **NEW Module 25 — Product DS, Business, Communication & Storytelling**

Full module:
- Decision intelligence framework
- Stakeholder comms, executive presentations, storytelling
- Framing DS problems as business outcomes
- Primary anchors:
  - [Cassie Kozyrkov — Decision Intelligence](https://www.decisionintelligence.co/) ✅
  - [CMU MSPPM-DA (Heinz — substitute for PDF's "CMU MADS")](https://www.heinz.cmu.edu/programs/public-policy-management-master/data-analytics) ✅
  - [UMich MADS — the actual MADS program](https://www.si.umich.edu/programs/master-applied-data-science) ⚠️ bot-gated, reader-accessible

### Edit 27 — Module 20 Capstone (line 1081) — Add THREE TRACKS with Rubric

Insert at the top of Module 20 a new "Three-Track Capstone Rubric":

**Track 1 — Research:** Submit to workshop. Pipeline: arXiv preprint → NeurIPS/ICML/ICLR workshop. Graded on novelty (25%), rigor (25%), reproducibility (25%), clarity (25%).

**Track 2 — Systems:** Deploy production system with SLOs. Graded on architecture (25%), evals (25%), latency/cost SLOs (25%), ops runbook (25%).

**Track 3 — Applied:** Real business/sponsored problem with causal evaluation. Graded on problem framing (25%), causal validity (25%), stakeholder comms (25%), measured impact (25%).

Rubric cross-ref: Berkeley MIDS capstone + CS336 Assignment 5.

### Edit 28 — Textbook List (line 1119)

Add **5 new Tier-1 books** (PDF-recommended, verified):
- Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments* (Cambridge 2020) — Module 6½
- Reis & Housley — *Fundamentals of Data Engineering* (O'Reilly 2022) — Module 8a/8b
- Chip Huyen — *AI Engineering* (O'Reilly 2025) — already present in Tier-1 (row 23)
- Pearl, Glymour, Jewell — *Causal Inference in Statistics: A Primer* — Module 6½
- Hernán & Robins — *Causal Inference: What If* (free) — Module 6½

### Edit 29 — 2026 Toolchain (line 1163)

Bump versions + add new rows:
- PyTorch 2.11.0 ✅ (keep)
- **JAX 0.10.0** (was 0.7.x) — 2026-04-16
- **scikit-learn 1.8.0** (was 1.7+)
- **Polars 1.40+** (keep "1.x" claim; pin to 1.40 for 2026.2)
- **HF Transformers v5.6+** (bump from "v5.0")
- **vLLM 0.19+** (was 0.6+)
- Add rows: **uv 0.11+**, **dbt-core 1.11+**, **DuckDB 1.5+**, **MLflow 3.11+**, **LangGraph 1.1+**, **smolagents 1.24+**, **DSPy 3.2+** (bump from 2.5+), **TRL 1.2+**, **PEFT 0.19+**, **Qdrant-client 1.17+**, **PyMC 5.28+** (bump from 5.17+), **NumPyro 0.20+** (bump from 0.17+)

### Edit 30 — Progress Tracker (line 1201)

Add checkboxes for new modules: 6½, 8a/8b (replace "8"), 21, 22, 23, 24 (replace "19"), 25, 26 (replace "20").

### Edit 31 — Dependency Graph (line 1245)

Expand ASCII diagram with new modules (6½ feeds from M6, 21/22/23/24/25 form Frontier + Production strata).

### Edit 32 — New "v2026.2 Architecture Map" Table

Insert after the meta-info table (line ~210): a clean table mapping README numbers ↔ PDF v2026.2 numbers so readers aren't confused by the 6½/8a/8b hybrid numbering. Include a one-line rationale per module.

### Edit 33 — Expand "2026 Tooling" Appendix

Already partially in the toolchain table. Add a new short standalone section **"🗂 2026 Tooling Quick-Reference"** right before Acknowledgements — a condensed cheat sheet: `Polars · DuckDB · uv · JAX · Qdrant · vLLM · LangGraph · dbt · MLflow · MCP` with one-line description each. (PDF §8.5 explicitly recommends this.)

### Edit 34 — Acknowledgements

Add a citation: "**Benchmark gap analysis** — this v2026.2 structure closes 13 production-superstructure gaps identified in the April 2026 benchmark report against Berkeley MIDS, UMich MADS, CMU MSPPM-DA, MIT 6.390, Stanford CS336, HuggingFace Agents Course, MIT AISF, and the 2026 Agentic AI Roadmap. See `audit/VERIFICATION.md` for the 150+-URL verification record."

---

## P2 → P3 Gate

All 34 edits above are backed by P1-verified URLs. P3 now executes them in order using `Edit` / `MultiEdit` tool calls, committing logical groups as we go. After each logical block (Banner+Log · TOC+Map · Foundation adds · Data-stack splits · DL+RL expansions · NEW frontier modules · MLOps rewrite · Appendix+Tooling bumps · Capstone rubric · Grand re-read), P3 stops and self-checks before proceeding.

## Protected / Must-Not-Touch (recap)

- Module 0 text (pre-calc, proofs, discrete math) — PDF §M0 "elite, unique strength"
- Measure-theoretic probability + concentration content in M5 — PDF §M5 "stronger than most PhD qualifiers"
- Two-pass Linear Algebra (Strang + Axler) in M3 — PDF §M3 "extremely rare in bootcamps"
- The overall math spine (M0 → M5) — "don't let anyone convince you to delete it"
