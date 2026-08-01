# ✅ P6 — Practitioner's Pass Audit (v2026.3)

**Date:** 2026-07-30 (research 2026-07-26, final re-verification 2026-07-30)
**Scope:** A curriculum-engineering pass adding a practitioner's fast lane, project-per-module enforcement, a career-reality layer, an applied reading shelf, and a production-first standard — without weakening the academic spine.
**Method:** RESEARCH → PLAN → EDIT → VERIFY → COMMIT. Every factual claim HTTP-checked or cross-referenced against a primary source before entering the README. Full status log: [`VERIFICATION.md` § P6](VERIFICATION.md).
**Legend:** ✅ live · ⚠️ bot-gated · ❌ dead · 🔁 fixed-with-alternative · ⏭ deliberately deferred.

---

## Summary

| Outcome | Count |
|---|---:|
| URLs HTTP-checked | 70 |
| ✅ PASS (200) | 66 (94 %) |
| ⚠️ WARN (403 bot-gated, browser-accessible) | 3 (4 %) |
| ❌ FAIL shipped into README | **0** |
| ❌ FAIL found during research and omitted/replaced | 6 |
| PyPI framework versions re-pulled | 13 |
| Stale version claims corrected | 2 |
| Source-brief claims falsified and corrected | 3 |
| Previously-published README claims falsified and corrected | 2 |
| Pre-existing `#anchor`s broken | **0** |
| New `#anchor`s added | 40 |
| README lines added / removed | +678 / −8 |

---

## Sources consumed (complete list)

### Repository documents

| Document | Used for |
|---|---|
| `README.md` (v2026.2, 1544 lines) | Baseline structure, house format, module inventory, existing anchors |
| `audit/FINAL_AUDIT.md` | Audit report format replicated by this file; verification conventions |
| `audit/VERIFICATION.md` | URL-status table format; the ✅/⚠️/❌/🔁 legend; prior verification history |
| `audit/IMPROVEMENT_SPEC.md` | The protected-content list (M0, M2, M3, M5, M9–M12, M13, M15) and the minimal-diff / append-only renumbering policy |
| `audit/AUDIT.md` | Prior-pass gap taxonomy |
| `coursepages/m21…m25, m6h, m8b/README.md` | Sub-page format (Status line · Why · Primary anchors table · Mandatory mini-projects · Prerequisites) |

### Video sources (mined in full, timestamps recorded)

| # | URL | Speaker context | Doctrine extracted |
|---|---|---|---|
| **1** | <https://www.youtube.com/watch?v=UZ_rK9gzVSc> | Senior Applied Scientist, Twitch | Five-phase practical path (maths *intuition* → ML overviews → Python → from-scratch NumPy → GenAI skills); the `__init__`/`sigmoid`/`fit`/`predict` implementation pattern; K-Means and decision trees as the other two from-scratch algorithms; portfolio architecture standard (Docker + cloud + CI/CD + MLflow/W&B + monitoring); the **fluency illusion** (09:30); project archetypes (13:10–14:05); RAG-vs-fine-tuning decisioning (07:15) |
| **2** | <https://www.youtube.com/watch?v=FeQZmQMffzc> | Applied Scientist, Amazon (non-technical origin) | Internal locus of control (07:12); beginner's mindset (04:30); working in public (09:40); build for real people/organisations (11:30); application volume (14:20); interviews-as-data / rejection-as-experiment (16:05); 18–36-month transition window (18:40) |
| **3** | <https://www.youtube.com/watch?v=Pr9oRVtAqCM> | ex-Coursera / ex-Amazon | AI Engineer role definition — build **on** foundation models, do not train them (00:53, 05:52); Python as table stakes (01:21); intuition over derivation (04:47); notebook-to-production progression (07:30); the seven-book canon |

### Article sources (read in full — required by the brief)

| # | URL | Status | Doctrine extracted |
|---|---|:---:|---|
| **1** | <https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/> | ✅ 200 | The eight-course free-Python landscape with hours/format/certificate/projects data; the pairing strategy; the Python-2 and no-OOP red flags |
| **2** | <https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/> | ✅ 200 | The four-phase roadmap with weekly milestones; time-to-competence estimates (4–8 wk basics / 3–6 mo useful / 9–12 mo job-ready); the tutorial-hell escape protocol; the phase-matched project ladder; the disciplined-AI-use rule |

Both appear as clickable citations in the README's Module 1 resource list, satisfying the brief's hard constraint 7.

### Job-market survey — 16 live postings, 2026-07-26

LinkedIn, Indeed, RemoteOK and the YC job board are JavaScript-gated and returned only page chrome to a crawler. The survey therefore used the **public Greenhouse job-board API** (`https://boards-api.greenhouse.io/v1/boards/<company>/jobs` for the index, `/jobs/<id>?content=true` for full descriptions), which returns complete, readable postings.

| # | Company | Title | Family |
|---:|---|---|---|
| 1 | Databricks | AI Engineer — FDE (Forward Deployed Engineer) | AI Eng |
| 2 | Databricks | Forward Deployed Engineer | AI Eng |
| 3 | Scale AI | Forward Deployed Engineer, GenAI | AI Eng |
| 4 | Anthropic | Applied AI Architect | AI Eng |
| 5 | Anthropic | Applied AI Security Architect | AI Eng |
| 6 | Figma | Forward Deployed Engineer | AI Eng |
| 7 | Airtable | Forward Deployed Engineer | AI Eng |
| 8 | Scale AI | Machine Learning Engineer, Platform | ML Eng |
| 9 | Scale AI | Senior Machine Learning Engineer, Agent Oversight | ML Eng |
| 10 | Cloudflare | Machine Learning Engineer | ML Eng |
| 11 | Anthropic | Data Scientist, Developer Productivity | DS |
| 12 | Discord | Data Scientist, Analytics | DS |
| 13 | Figma | Data Scientist | DS |
| 14 | Cloudflare | Data Scientist | DS |
| 15 | Anthropic | Data Engineer | DE |
| 16 | Figma | Data Engineer | DE |

**Aggregate mention frequency (n = 16).** Counts are literal keyword/phrase matches over full posting text.

| Skill | Count | Skill | Count |
|---|---:|---|---:|
| Stakeholder / cross-functional communication | **15** | Airflow / orchestration | 4 |
| Python | 9 | CI/CD | 3 |
| LLM / foundation models | 8 | PyTorch / TensorFlow | 2 |
| Evaluation | 8 | Fine-tuning | 2 |
| Statistics / causal / regression | 7 | Kubernetes | 1 |
| Warehouse / dbt | 6 | Docker | 1 |
| Spark / distributed | 6 | Terraform / IaC | 1 |
| SQL | 6 | Prompt engineering | 1 |
| Agents / tool use | 6 | **PhD required** | **0** |
| A/B testing / experimentation | 6 | **Kaggle** | **0** |
| Streaming (Kafka / Flink) | 4 | Degree mentioned at all | 5 |
| RAG / retrieval / vector search | 4 | | |
| MLOps / monitoring / observability | 4 | | |
| Cloud (AWS / GCP / Azure) | 4 | | |

**Per-family split** (AI Eng n=7 · ML Eng n=3 · DS n=4 · DE n=2) is reproduced in the README's [skills-checklist](../README.md#skills-checklist) section.

**Sampling limitations, stated in the README as well as here:** n=16 is small; the sample skews toward AI-native technology companies (which is *why* it is useful for reading where AI-Engineer demand is going, and why it is *not* a labour-market statistic); the Data Engineer row is n=2 and is labelled an anecdote. Greenhouse posting IDs are ephemeral, so the URLs were **deliberately not** placed in the README — only the methodology, the company list, and the counts.

---

## Gaps identified, and the edit that closes each

| # | Gap in v2026.2 | Closing edit | Workstream |
|---|---|---|---|
| 1 | No practitioner entry point; the only route in was the full maths spine | [🚀 Practitioner Track](../README.md#practitioner-track): a 6-stage, 6–9-month sequence with a "what you give up" column | A |
| 2 | One undifferentiated "AI Engineer" row, research-flavoured | Split into **AI Engineer (Applications)** and **AI Engineer (Systems/Research-adjacent)**, with Chip Huyen's *AI Engineering* named as the Applications primary text | A |
| 3 | Maths modules offered no honest shortcut, so beginners bounced | ⚡ **Intuition-First Alternative** callouts in M0, M2, M3, M5 — each with the route, the argument, what you give up, and when to return | A |
| 4 | M1 had a topic list but no pacing, no course comparison, and no study method | Four-phase pacing with ship-milestones; the 8-course [matrix](../README.md#python-course-matrix); the pairing stack; the tutorial-hell protocol; the AI-use policy | B |
| 5 | Only 7 of 25 modules mandated a project | [Enforcement rule](../README.md#module-projects) + **18 new 📦 Module Project blocks** — all M1–M25 now covered | C |
| 6 | Zero career content; competence was assumed to convert itself into a job | [🧭 Career Operations](../README.md#career-operations): locus of control, ~70 %-match applying, funnel tracking, outreach, real-org sourcing, accountability, reconciled timelines | D |
| 7 | No grounding in what employers actually ask for | [Skills ↔ JD mapping](../README.md#skills-checklist), 4 per-track tables from the 16-posting survey, every skill pointing at a module | D |
| 8 | Reading list was entirely academic; nothing for a builder | [🧰 Practitioner Shelf](../README.md#practitioner-shelf) — 7-book applied canon, annotated by module/track, Tier 1 and 2 untouched | E |
| 9 | "Production quality" was implied but never specified | [🏁 Minimum Production Bar](../README.md#production-bar) — a 12-item pass/fail table + clean-clone reproducibility check | F |
| 10 | The most-asked AI-Engineer design question had no framework | The five-rung [prompting vs RAG vs fine-tuning ladder](../README.md#module-21) in M21, with the eval-set-first rule and two named misdiagnoses | F |
| 11 | Prompt injection existed in M23/M24 but not in M22, where agents get tools | Agent-security block in M22: direct vs indirect injection, escalation paths, defences honestly ranked | F |
| 12 | Agent evaluation was benchmark-listing only, with no harness discipline | Agent eval-pipeline block: trajectory scoring, pass@k, cost-per-successful-task, LLM-as-judge calibration, evals-as-CI | F |
| 13 | Streamlit absent from the toolchain; agent pins stale | New "Dashboards & demo UIs" row; agents row refreshed and CrewAI pinned | F |
| 14 | All 7 `coursepages/` sub-pages still said v2026.2, and every one of their root cross-links was **broken** — they targeted GitHub heading slugs carrying a `(NEW · v2026.2)` suffix that an earlier pass had removed from the headings | All 7 repointed to the stable explicit `#module-NN` anchors and bumped to v2026.3; m21 gained the decision ladder, m22 the security + eval-pipeline sections and PyPI pins, m24 the Production Bar | G |
| 15 | The roadmap was entirely text — a 2,200-line wall of prose with no visual entry point, against a stated benchmark (microsoft/Data-Science-For-Beginners) whose approachability is largely visual | 8 licence-clean images: hero banner, six-stratum journey infographic, and one section banner per stratum, in a single dark-navy visual language | H |

---

## Pre-edit checks performed (so nothing was added that already existed)

| Claim to add | Pre-check result | Action |
|---|---|---|
| Prompt-injection security | Present in M23 (jailbreak taxonomy) and M24 (guardrails tooling); **absent from M22** | Added to M22 only |
| Eval pipelines | Tooling present in M18, M21, M23; **agent-eval discipline absent** | Added agent-eval block to M22 |
| CrewAI | **Already present** in M22 and the toolchain, unpinned | Pinned; not duplicated |
| Streamlit | Present in M7/M8a prose; **absent from the toolchain table** | Added one toolchain row |
| Prompting vs RAG vs fine-tuning framework | `zero-shot` appeared only as in-context-learning terminology; **framework genuinely absent** | Added to M21 |
| Module projects | 7 modules already had `📋 Mandatory mini-projects` (M3, M6½, M8b, M21, M22, M23, M25) | Left untouched; 18 new blocks only where missing |

---

## Structural integrity checks

- [x] **Zero pre-existing anchors lost.** Baseline (`aac9ba8`) 102 anchors → 144 now (counting heading slugs and explicit `<a id>` together); set difference `baseline − current` is empty, re-checked after the visual pass.
- [x] **Every internal link present in the baseline still resolves** in the new file.
- [x] **Zero unresolved internal links overall** — 47 internal links, 141 anchors, 0 missing.
- [x] **Module numbering untouched** — 28 explicit module anchors before and after; M6½, M8a/M8b splits and the M19/M20 gap preserved.
- [x] **README ↔ PDF benchmark mapping intact** — all 3 `Gap #` references preserved verbatim.
- [x] **House format preserved** — every new module block uses the existing bullet grammar; no module's *Tutor's "Why"* / *Strict Prerequisites* / *Exhaustive Topic List* / *2026 Resources* structure was altered.
- [x] **Append-only in practice** — +678 / −8 lines, and each of the 8 removed lines is either a strict superset replacement (nav bar, TOC groups, the split AI-Engineer row, the refreshed toolchain row) or one of the two verified edition corrections.
- [x] **Protected content untouched** — no mathematical content in M0, M2, M3, M5, M9–M12, M13, M15 was rewritten; the four intuition callouts are *appended* blockquotes that explicitly point back at the spine.
- [x] **Images are insert-only and lossless to structure** — the 8 embeds sit above the H1, under one existing heading, and after the six stratum H1s. No heading text, no slug, and no anchor changed; anchor count is identical before and after the visual commit.
- [x] **Every embedded image path resolves** — all 8 `src="assets/…"` targets checked against the working tree; repo-relative so GitHub serves them (no session-scoped or hotlinked URLs, which would 403 for other readers).
- [x] **No information exists only in an image** — every stratum name, module range, and navigation target is also present as text; all embeds carry descriptive `alt` attributes.
- [x] **Free-first policy held** — every paid item (Manga Guides, StatQuest guides, Manning, O'Reilly, ByteByteGo) is labelled optional, and free alternatives (StatQuest videos, 3Blue1Brown, ATBS full text, LLMs-from-scratch code) are linked alongside.

---

## Image licensing (Workstream H)

The brief's anti-fabrication discipline was applied to artwork as well as to facts: an asset ships only if its origin can be stated.

| Requirement | How it was met |
|---|---|
| No commercially-licensed imagery | Nothing from Getty / Shutterstock / Alamy / iStock / Adobe Stock. No image search was used at all. |
| No scraped third-party images | No image was taken from a crawled page or search result. |
| No session-scoped URLs embedded | The two generated images were **downloaded into the repository** and committed. Generator file-wrapper URLs return 403 outside the authoring session, so embedding them would have shown broken images to every other reader. |
| Reproducible provenance | The 6 stratum banners are drawn by the committed [`assets/make_banners.py`](../assets/make_banners.py) (Pillow only, deterministic). Anyone can regenerate them. |
| Documented | [`assets/README.md`](../assets/README.md) records per-file origin, the style contract, and the accessibility position; `README.md` Acknowledgements carries an **Images** paragraph. |

**Why 6 of 8 are code-drawn rather than model-generated.** Generative models misspell, and every banner
carries a title plus a module range. A curriculum that HTTP-checks its own URLs cannot ship a header
reading "MODUELS 9-12". Code-drawing also makes the banners editable: a renumbered module is a one-line
change and a re-run, not a fresh generation with a new style to reconcile. The two model-generated images
were proof-read for text accuracy before being committed — the first pair of drafts was checked
character-by-character and passed.

**Repository weight.** 8 images, 656 KB total (hero 206 KB, infographic 138 KB, banners 36–47 KB each),
downscaled to 1600 px and JPEG q90–92. The originals were 4.19 MB and 4.04 MB; shipping them unprocessed
would have made cloning meaningfully worse for a decorative gain.

---

## Anti-hallucination rules applied (recap)

1. **Nothing entered the README that is not in [`VERIFICATION.md` § P6](VERIFICATION.md).**
2. **The brief was treated as a hypothesis, not as fact.** Three of its claims were falsified by primary sources and corrected: the *Generative AI System Design Interview* author list, the StatQuest per-title URL structure, and the ByteByteGo course URL.
3. **Pre-existing README claims were re-checked when touched**, which surfaced two false edition claims in M1 (Fluent Python, Python Crash Course). Both corrected against the author's own site and the publisher's catalogue.
4. **Bot-gated ≠ dead.** The two O'Reilly pages return 403 to crawlers; they are marked ⚠️, cited with ISBNs, and paired with a 200-verified author page as the primary clickable link.
5. **Dead URLs were omitted, not guessed at.** Six were found; all six are recorded in P6-G with their resolution.
6. **Volatile URLs were kept out of the README.** Greenhouse posting IDs rotate, so the job survey is cited by methodology and company list rather than by link.
7. **Doctrinal conflicts were presented, not resolved by fiat.** Intuition-first vs proof-first, and the 9–12 vs 18–36-month timelines, are both stated with their conditions attached.

---

## Deliberately NOT changed, and why

| Item | Reason |
|---|---|
| Tier 1 (38 rows) and Tier 2 reading lists | Marked elite/approved by `IMPROVEMENT_SPEC.md`. The Practitioner Shelf is additive. |
| Mathematical content of M0, M2, M3, M5, M9–M12, M13, M15 | Protected list. Only additive blockquote callouts were appended. |
| Module numbering, incl. the M19/M20 gap | Renumbering would break every external deep link and the PDF mapping table. |
| `mlflow` 3.11.1 → 3.14.0 and `langchain` 0.3+ → 1.3.14 in existing lines | Outside this pass's remit; changing untouched lines widens the diff without evidence that the pass required it. Logged in P6-F for the next refresh. |
| Job-posting URLs in the README | Greenhouse IDs are ephemeral; shipping them would guarantee future dead links. |
| The 7 existing `📋 Mandatory mini-projects` blocks | They already satisfy the project requirement; rewriting them into the new format would be churn. |

---

## Recommended next passes

1. **Version-refresh pass.** `mlflow`, `langchain`, `llama-index`, `haystack`, `dspy` and the M21/M24 practical-implementation lines carry pins that are now behind PyPI. A mechanical sweep with the PyPI JSON API would close them.
2. **Solution-repository pass.** The 25 module projects now have definitions of done but no reference implementations. A companion `projects/` scaffold (one starter repo per module with the test skeleton pre-written) would remove the highest-friction step.
3. **Visual-completion pass.** Six stratum banners exist; per-module inline diagrams do not. The highest-value additions would be a Practitioner-Track flow graphic, a prerequisite DAG for M0–M18 (the prerequisites are stated in prose but never drawn), and a decision-tree graphic for the prompting-vs-RAG-vs-fine-tuning ladder. All three are code-drawable with the existing `make_banners.py` primitives.
4. **Broader job-market pass.** Re-run the survey at n≈60 across non-AI-native employers (banks, healthcare, retail, government, agencies) to test whether the communication-over-frameworks finding holds outside the current sample, and to give the Data Engineer track a real distribution instead of an anecdote.

---

## Status

**PASS.** All eight workstreams implemented (A–G from the brief, plus H for the follow-up appearance request), 0 dead links shipped, 0 anchors broken, 0 protected content rewritten, 0 third-party image licences incurred, and every edit traceable to a named source with a timestamp or a section reference.
