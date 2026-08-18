# Module 21 — RAG, Vector DBs & Retrieval Systems

> **Status:** v2026.3 scaffold · full spec in the root [README.md § Module 21](../../curriculum/6-frontier-production.md#module-21).

## Why this module exists

Retrieval-Augmented Generation is the single most-deployed LLM pattern in production (Menlo Ventures Oct 2025: >70% of enterprise LLM deployments). Getting chunking + retrieval + reranking + evaluation right is the difference between a demo and a product. Closes Gap #5.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| Pinecone Learning Center | Free RAG/vector primer | <https://www.pinecone.io/learn/> |
| LlamaIndex docs | Practical cookbook | <https://docs.llamaindex.ai/> |
| LangChain RAG tutorial | Framework walkthrough | <https://python.langchain.com/docs/tutorials/rag/> |
| pgvector | Postgres vector extension | <https://github.com/pgvector/pgvector> |
| Qdrant | Rust vector DB | <https://qdrant.tech/> |
| Weaviate | Open-source vector DB | <https://weaviate.io/> |
| Milvus | Distributed vector DB | <https://milvus.io/> |
| LanceDB | Embedded, Lance-format vector DB | <https://lancedb.com/> |
| ColBERT | Late-interaction retrieval | <https://github.com/stanford-futuredata/ColBERT> |
| Ragas | RAG evaluation framework | — see `github.com/explodinggradients/ragas` |
| Anthropic — Contextual Retrieval (Sep 2024) | SOTA chunking technique | <https://www.anthropic.com/news/contextual-retrieval> |
| Microsoft GraphRAG (2024) | Graph-based RAG | <https://github.com/microsoft/graphrag> |

## ⚖️ Before you build: the prompting → RAG → fine-tuning ladder

Do not start this module by writing a retrieval pipeline. Start by deciding whether you need one.
The root README carries the full decision table — see
[README.md § Module 21 → the decision framework](../../curriculum/6-frontier-production.md#module-21). Short version:

| Rung | Technique | Reach for it when |
|---|---|---|
| 1 | Zero-shot prompting | Always first — it is your baseline, and you may not skip it |
| 2 | Few-shot / structured prompting | The model *could* know the answer but answers the wrong question, or in the wrong shape |
| 3 | **RAG (this module)** | The failure is *"it does not know this"* — private, missing, or fast-changing knowledge; citations required |
| 4 | Fine-tuning (SFT / LoRA — M18) | The failure is *"it knows this but behaves wrong"* — style, tone, format, or a small cheap specialist model |
| 5 | RAG + fine-tuning | You have measured **both** failure modes and can prove each component earns its keep |

**The rule that makes this operational:** you cannot pick a rung without an eval set.
Build 50–200 real queries with acceptable answers *first*, then climb. Fine-tuning before you can
measure buys an unfalsifiable improvement.

**In 2026 the default answer is rung 3.** RAG is cheaper, updates instantly, cites its sources, and
keeps private data out of the weights. Fine-tuning is the specialist tool, not the prestige tool.

## Mandatory mini-projects

1. Build a RAG over your own PDFs: chunking → pgvector → BGE reranker → answer-with-citations; measure Ragas faithfulness + context precision.
2. Hybrid search A/B: BM25-only vs dense-only vs hybrid-with-RRF; measure nDCG@10 on a labelled query set.
3. GraphRAG on a technical corpus; compare multi-hop accuracy vs vanilla RAG.

## Prerequisites

- Module 18 (LLMs, tokenisation), Module 11 (embeddings, cosine similarity, PCA/SVD), Module 8a (SQL metadata filters + hybrid search)
