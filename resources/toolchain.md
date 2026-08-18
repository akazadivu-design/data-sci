[🏠 Roadmap home](../README.md)

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
| **Dashboards & demo UIs** | **Streamlit** / Gradio / Evidently | **Streamlit 1.60.0** (PyPI, 21 Jul 2026) | The default free deployment target for the [Minimum Production Bar](../curriculum/6-frontier-production.md#production-bar) item 9 (Streamlit Community Cloud · HF Spaces); Evidently for drift dashboards (M24) |
| **Experiment config** | **Hydra** + **Pydantic** | 1.3+ / 2.10+ | Pydantic 2 is 20× faster than v1 |
| **Reproducibility** | DVC + Git LFS | 3.x / latest | Version control for data + models |
| **Writing** | Typst or LaTeX + Zotero 7 | latest | Typst = modern LaTeX alternative, compiles in ms |
| **GPU compute (self‑study)** | Modal · RunPod · Lambda · Nebius · Together | March 2026 prices | B200: Modal $6.25/h · RunPod $4.99/h · Lambda $6.69/h (Stanford CS336 sponsor list) |

---

[🏠 Roadmap home](../README.md)
