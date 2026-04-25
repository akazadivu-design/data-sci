# Module 8b — Distributed Data & Streaming Systems

> **Status:** v2026.2 scaffold · full spec in the root [README.md § Module 8b](../../README.md#module-8b-distributed-data--streaming-systems-new--v20262).

## Why this module exists

The April 2026 benchmark identified *Modern Data Engineering* (Spark, Kafka, Airflow, Iceberg, lakehouse) as Gap #2 — the largest production-DS gap after causal inference. This module closes it. Module 8 was split so SQL fundamentals (M8a) and distributed/streaming systems (M8b) each get full airtime.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| Stanford CS246 — *Mining Massive Datasets* (Leskovec, 2025) | Academic spine | <https://web.stanford.edu/class/cs246/> |
| DataExpert.io Free Data Engineer Bootcamp (Zach Wilson) | Practical on-ramp | <https://www.dataexpert.io/free-data-engineer-bootcamp> |
| DataExpert-io / data-engineer-handbook | Community roadmap | <https://github.com/DataExpert-io/data-engineer-handbook> |
| Reis & Housley — *Fundamentals of Data Engineering* (O'Reilly 2022) | Canonical text | <https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/> |
| *Mining of Massive Datasets* (Leskovec et al., 3e, free) | Textbook | <http://www.mmds.org/> |
| Kleppmann — *Designing Data-Intensive Applications* | Systems foundations | — |
| Apache Spark | Distributed compute | <https://spark.apache.org/> |
| Apache Kafka | Streaming platform | <https://kafka.apache.org/> |
| Apache Flink | True streaming | <https://flink.apache.org/> |
| Apache Iceberg | Lakehouse table format | <https://iceberg.apache.org/> |
| Delta Lake | ACID on data lake | <https://delta.io/> |
| Apache Airflow | Workflow orchestration | <https://airflow.apache.org/> |
| Dagster | Asset-oriented orchestration | <https://dagster.io/> |
| Prefect | Pythonic flows | <https://www.prefect.io/> |
| Joe Reis Substack | Living resource | <https://joereis.substack.com/> |

## Mandatory mini-projects

1. **Mini-lakehouse:** DuckDB + Parquet + Iceberg on your laptop; exercise `MERGE INTO` + snapshots + time-travel.
2. **Airflow DAG:** Ingest NYC Taxi API → S3/minio Parquet → dbt transform → Streamlit dashboard.
3. **Kafka + Flink** streaming word-count over a simulated tweet stream; watermarks and late data.
4. **Benchmark:** Spark vs Polars vs DuckDB on a 10-GB Parquet dataset; compare wall-clock, RAM, LOC.

## Prerequisites

- Module 4 (randomised/streaming algos), Module 8a (SQL), Module 1 (async Python)
