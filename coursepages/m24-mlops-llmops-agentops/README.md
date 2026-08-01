# Module 24 — MLOps + LLMOps + AgentOps

> **Status:** v2026.3 scaffold · full spec in the root [README.md § Module 24](../../README.md#module-24).
>
> Supersedes old Module 19 (MLOps / Systems / Responsible AI) by expanding into three operational tiers.

## Why this module exists

Closes Gap #3 of the benchmark PDF — the 2026 operational stack for (1) classical ML (MLOps), (2) prompt/LLM-driven systems (LLMOps), and (3) stateful tool-using agents (AgentOps).

## Primary anchors (P1-verified)

### MLOps (classical)

| Resource | Role | Link |
|---|---|---|
| Full Stack Deep Learning | Canonical open course | <https://fullstackdeeplearning.com/> |
| Made With ML (Goku Mohandas) | End-to-end MLOps course | <https://madewithml.com/> |
| Chip Huyen — *Designing ML Systems* | Canonical text | — |
| Chip Huyen — *AI Engineering* (O'Reilly 2025) | 2026 successor text | <https://www.oreilly.com/library/view/ai-engineering/9781098166298/> |
| MLflow | Experiment tracking + registry | <https://mlflow.org/> |
| Weights & Biases | Research experiment tracking | <https://wandb.ai/> |
| Feast | Open-source feature store | <https://feast.dev/> |
| Evidently | Drift monitoring | <https://www.evidentlyai.com/> |
| BentoML / KServe / Ray Serve / Triton | Serving | <https://www.bentoml.com/> · <https://kserve.github.io/website/> · <https://docs.ray.io/en/latest/serve/> · <https://developer.nvidia.com/nvidia-triton-inference-server> |

### LLMOps (2024–2026)

| Resource | Role | Link |
|---|---|---|
| Langfuse (self-hostable) | Prompt versioning + observability | <https://langfuse.com/> |
| Helicone | Gateway + observability | <https://www.helicone.ai/> |
| PromptLayer | Prompt management | <https://promptlayer.com/> |
| NeMo Guardrails | Guardrails framework | <https://github.com/NVIDIA/NeMo-Guardrails> |
| Guardrails AI | Guardrails | <https://www.guardrailsai.com/> |
| Llama Guard / PurpleLlama | Meta guardrails | <https://github.com/meta-llama/PurpleLlama> |
| OTel GenAI semantic conventions | LLM observability standard | <https://opentelemetry.io/docs/specs/semconv/gen-ai/> |

### AgentOps (2025–2026)

| Resource | Role | Link |
|---|---|---|
| LangSmith | Agent tracing | <https://www.langchain.com/langsmith> |
| Arize Phoenix | Open-source OTel-native tracing | <https://github.com/Arize-ai/phoenix> |
| W&B Weave | LLM/agent tracing | <https://wandb.ai/site/weave> |
| GAIA benchmark | Agent eval | <https://huggingface.co/gaia-benchmark> |
| SWE-bench | Software-engineering eval | <https://www.swebench.com/> |
| E2B / Daytona / Modal | Sandboxing | <https://e2b.dev/> · <https://www.daytona.io/> · <https://modal.com/> |

## 🏁 The Minimum Production Bar

Every project you ship from Modules 1–25 is measured against one standard, defined in full at
[README.md § Minimum Production Bar](../../README.md#production-bar). A notebook that only ever ran on
your laptop is not a project — it is a homework file. The bar, in brief:

1. Runs from a clean clone with one documented command
2. Pinned dependencies (`uv` / `requirements.txt` / lockfile), stated Python version
3. A README that says what it does, why, and what the result was — with a number in it
4. Version control with real commit history, not one `initial commit`
5. Tests on the non-obvious logic, and CI that runs them
6. Config and secrets outside the code (`.env`, never committed)
7. Structured logging, not `print`
8. A reachable artefact: an endpoint, a Streamlit/Gradio app, a scheduled job, or a container image
9. A stated evaluation with a baseline to compare against
10. Error handling for the inputs you know are malformed
11. A written limitations section — what it does *not* do, and where it fails
12. Reproducibility: fixed seeds, versioned data, recorded run parameters

Items 1–4 are non-negotiable for every project. Items 5–12 are what separate the two or three
portfolio-centrepiece projects from the rest.

## Mandatory mini-projects

1. **MLOps:** Package a scikit-learn model with MLflow tracking + BentoML serving + Evidently drift dashboard.
2. **LLMOps:** Instrument an LLM app with Langfuse traces + OTel GenAI semantic conventions + a promptfoo eval in CI.
3. **AgentOps:** Trace a LangGraph agent with LangSmith or Phoenix; run GAIA-Level-1 as a regression suite.

## Prerequisites

- Any model from Modules 9–18; Module 22 for the AgentOps half.
