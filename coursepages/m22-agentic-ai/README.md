# Module 22 — Agentic AI (LangGraph, CrewAI, MCP & A2A)

> **Status:** v2026.3 scaffold · full spec in the root [README.md § Module 22](../../curriculum/6-frontier-production.md#module-22).

## Why this module exists

2025 was the "year of the agent" and 2026 is the year of *reliable* agents. Every 2026 senior AI-engineer interview covers LangGraph + MCP + SWE-bench. Closes Gap #4 of the benchmark PDF.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| Hugging Face AI Agents Course (free, certified) | Primary course | <https://huggingface.co/learn/agents-course/> |
| Berkeley LLM Agents MOOC | University course | <https://llmagents-learning.org/> |
| Anthropic — Building Effective Agents (Dec 2024) | Canonical patterns article | <https://www.anthropic.com/research/building-effective-agents> |
| LangGraph | Stateful multi-agent framework | <https://www.langchain.com/langgraph> |
| CrewAI | Role-based orchestration | <https://docs.crewai.com/> |
| smolagents (Hugging Face) | ~1000 LOC code-agents | <https://github.com/huggingface/smolagents> |
| Model Context Protocol | LLM↔tool/data open standard | <https://modelcontextprotocol.io/> |
| MCP 2025-06-18 spec | Latest MCP revision | <https://modelcontextprotocol.io/specification/2025-06-18> |
| MCP reference servers | Filesystem, GitHub, Postgres, Slack, etc. | <https://github.com/modelcontextprotocol/servers> |
| GAIA benchmark | General assistant eval | <https://huggingface.co/gaia-benchmark> |
| SWE-bench | Real GitHub issues eval | <https://www.swebench.com/> |
| E2B / Daytona / Modal | Agent sandboxing | <https://e2b.dev/> · <https://www.daytona.io/> · <https://modal.com/> |

## 🔓 Agent security — prompt injection is the threat model

An agent with tools is an agent with a blast radius. The moment your system reads untrusted text
(a web page, an email, a PDF, an upload, another agent's output) and can then *act*, prompt injection
stops being a curiosity. Full treatment in [README.md § Module 22](../../curriculum/6-frontier-production.md#module-22).

* **Direct injection** — the user tries to override your system prompt. Usually low impact.
* **Indirect injection** — the payload is hidden in content the agent *retrieves*. This is the serious
  one: the attacker never has to talk to your system. RAG (M21) and browsing agents structurally invite it.
* **What it escalates into** — data exfiltration via fetched URLs, unauthorised tool calls, destructive
  actions, and confused-deputy problems where the agent's credentials outrank the requester's.

**Defences, honestly rated** — none is a solution, and prompt-level mitigation is the *weakest* layer:

| Layer | Leverage | Notes |
|---|---|---|
| Least privilege on tools | **Highest** | Read-only by default; per-task credentials; split the reader agent from the writer agent |
| Egress allow-listing | High | This is what actually stops URL-based exfiltration |
| Sandboxed execution | High | E2B / Daytona / Modal / Firecracker / gVisor for anything code-shaped |
| Human-in-the-loop | High | Gate irreversible or privileged actions |
| Tool-output isolation | Medium | Mark retrieved text as *data*, never as instructions |
| Guardrail filters | **Lowest** | <https://github.com/NVIDIA/NeMo-Guardrails> · <https://www.guardrailsai.com/> · <https://github.com/meta-llama/PurpleLlama> — raise attacker cost; they are not boundaries |

**The stance to hold:** prompt injection is **not solved**, and any vendor claiming otherwise is wrong.
Design so a successful injection is *survivable* — an architecture decision, not a prompt-engineering one.
Red-teaming technique and jailbreak taxonomy live in M23; OWASP Top 10 for LLM Applications is the checklist.

## 📊 Agent eval pipelines — evaluation is the deliverable

GAIA / SWE-bench / τ-bench tell you where the field is. They do not tell you whether *your* agent
regressed this morning. You need your own harness.

* **Score trajectories, not just final answers.** Right tool, right arguments, sensible order, and did it
  stop? An agent that succeeds through six wrong tool calls is a cost and latency incident waiting to happen.
* **Layered metrics:** task success rate · **pass@k** (agents are stochastic — one run is not a measurement)
  · steps and tokens per task · **cost per successful task** (the number that gets budget approved)
  · latency · tool-error and retry rate · termination behaviour.
* **LLM-as-judge, with discipline:** biased toward verbose, self-similar answers. Calibrate against a
  human-labelled subset, report the agreement rate, and never let an unvalidated judge gate a release.
* **Run evals as CI:** a frozen eval set scored on every prompt, model, or tool change. This is what makes
  a portfolio project read as production work rather than a demo.

| Tool | Role | Link |
|---|---|---|
| DeepEval | pytest-like LLM/agent assertions | <https://github.com/confident-ai/deepeval> |
| promptfoo | Declarative eval matrices in CI | <https://github.com/promptfoo/promptfoo> |
| Ragas | The retrieval leg of the eval | <https://github.com/explodinggradients/ragas> |
| Arize Phoenix | OTel-native trace inspection | <https://github.com/Arize-ai/phoenix> |
| LangSmith | Managed tracing + datasets | <https://www.langchain.com/langsmith> |

**Why this is emphasised:** 6 of the 7 AI-Engineer / Forward-Deployed postings surveyed for v2026.3 name
evaluation explicitly — more often than RAG, agents, or fine-tuning individually. Building the demo is
table stakes; proving it works is the job. Operational tracing lives in M24 (AgentOps).

## 📌 Pinned versions (PyPI, verified 2026-07-30)

| Package | Version |
|---|---|
| `langgraph` | 1.2.10 |
| `crewai` | 1.15.9 |
| `smolagents` | 1.26.0 |
| `llama-index` | 0.14.23 |
| `deepeval` | 4.1.4 |

Re-verify with `pip index versions <pkg>` before pinning in your own project — these move fast.

## Mandatory mini-projects

1. Build an MCP server that exposes a small SQL DB; connect it to Claude Desktop or Cursor; run 10 queries.
2. LangGraph multi-agent researcher: planning → parallel web-search → synthesis → citation-checking; trace with LangSmith.
3. Run a minimal agent on 5 SWE-bench instances; measure pass@1 vs pass@10.

## Prerequisites

- Module 18 (LLMs, tool-use, function calling), Module 21 (retrieval)
