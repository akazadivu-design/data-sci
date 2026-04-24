# Module 22 — Agentic AI (LangGraph, CrewAI, MCP & A2A)

> **Status:** v2026.2 scaffold · full spec in the root [README.md § Module 22](../../README.md#module-22-agentic-ai--langgraph-crewai-mcp--a2a-new--v20262).

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

## Mandatory mini-projects

1. Build an MCP server that exposes a small SQL DB; connect it to Claude Desktop or Cursor; run 10 queries.
2. LangGraph multi-agent researcher: planning → parallel web-search → synthesis → citation-checking; trace with LangSmith.
3. Run a minimal agent on 5 SWE-bench instances; measure pass@1 vs pass@10.

## Prerequisites

- Module 18 (LLMs, tool-use, function calling), Module 21 (retrieval)
