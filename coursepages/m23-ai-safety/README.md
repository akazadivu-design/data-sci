# Module 23 — AI Safety, Alignment, Interpretability, Evals & Policy

> **Status:** v2026.2 scaffold · full spec in the root [README.md § Module 23](../../README.md#module-23-ai-safety-alignment-interpretability-evals--policy-new--v20262).

## Why this module exists

No serious 2026 AI/ML role is hired without alignment and safety literacy. MIT AI Safety Forum + Berkeley MIDS + AISF Alignment Fundamentals all cover this. Closes Gaps #6, #12, and #13 of the benchmark PDF.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| AI Safety Fundamentals — Alignment Track (Bluedot Impact) | Primary course, free | <https://aisafetyfundamentals.com/alignment/> |
| AISF Governance Track | Policy complement | <https://aisafetyfundamentals.com/governance/> |
| Anthropic Transformer Circuits | Mechanistic interpretability | <https://transformer-circuits.pub/> |
| Scaling Monosemanticity (Templeton et al., 2024) | SAE on Claude 3 Sonnet | <https://transformer-circuits.pub/2024/scaling-monosemanticity/> |
| Golden Gate Claude | SAE public demo | <https://www.anthropic.com/news/golden-gate-claude> |
| OpenAI evals | Eval framework | <https://github.com/openai/evals> |
| lm-evaluation-harness (EleutherAI) | Canonical harness | <https://github.com/EleutherAI/lm-evaluation-harness> |
| HF Open LLM Leaderboard | Public leaderboard | <https://huggingface.co/open-llm-leaderboard> |
| EU AI Act | Regulation | <https://artificialintelligenceact.eu/> |
| NIST AI RMF + GenAI Profile | US framework | <https://www.nist.gov/itl/ai-risk-management-framework> |
| AI.gov | US federal portal | <https://ai.gov/> |
| EleutherAI Cookbook | Practical reference | <https://github.com/EleutherAI/cookbook> |

## Mandatory mini-projects

1. Reproduce an induction head on a 2-layer attention-only toy transformer (Transformer Circuits).
2. Train a Sparse Autoencoder on GPT-2 small activations; label 5 monosemantic features.
3. Red-team an open model with `garak` or hand-crafted GCG suffixes; write a 2-page eval report with model card.
4. Draft an EU-AI-Act-compliant model card for a hypothetical general-purpose AI model.

## Prerequisites

- Module 18 (LLMs, RLHF), Module 22 (agents)
