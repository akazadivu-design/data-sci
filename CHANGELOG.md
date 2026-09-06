[🏠 Roadmap home](README.md)

---

<a id="refresh-log"></a>
# 🗓️ Refresh Log

Each pass records what changed, what was verified, and what was deliberately left alone. Full HTTP status logs live in [`audit/VERIFICATION.md`](audit/VERIFICATION.md); per-pass reports live in [`audit/`](audit/).

### Module 0 focused review · 2026-09-06

**Scope:** Module 0 and its placement diagnostic only; Modules 1 onward, numbering, and explicit existing anchors are unchanged. [Online research and implementation plan](https://github.com/akazadivu-design/data-sci/issues/11).

- Replaced the purported “15-question” link list with an original 12-question, two-strand diagnostic, a parallel retest, answer/marking guidance and topic-specific remediation. Later calculus, linear-algebra and probability tests no longer gate entry to M0.
- Reconciled exemption, full-bridge completion and application-first proof deferral. Preserved the proof core while labelling advanced topics optional; removed the requirement to know Python before M1.
- Added an 80-hour example schedule within a 60–100-hour planning range, practice/retrieval loop, hint-only AI guidance, a no-code reasoning evidence pack, scored rubric and explicit exit gate. Updated only the M0 row of the Pick-One table.
- Replaced unlabelled paid/uncertain-access reading with free OpenStax and Hammack defaults. Corrected Hammack's CC-BY label (the author restricts commercial use and adaptations) and identified its 3.4 revision dated 2025-02-05. Removed the unsupported “2024 edition” description of the Spring 2015 MIT archive, the “60%+ stall” statistic and “10×” proof-assistant claim.
- Added optional runnable SymPy checks with explicit imports, real-domain assumptions, excluded-input caveats and the distinction between finite tests and proof.
- Recorded Video 4 as a verified title/channel/chapter-topic source, **not** a verified transcript: playback/captions were blocked, and conflicting automated analysis was rejected. Detailed speech alignment remains pending; the independent publisher/institution evidence and access limitations are linked from the source key and plan.

**Validation:** Internal links/anchors, embedded SymPy checks, diagnostic calculations, project cases and byte-for-byte preservation of M1 onward are checked in the pull request. No site deployment, later-module rewrite or automatic merge is part of this pass.

### v2026.5 — Clear Path · 2026-08-30

**Diagnosis addressed:** first-time readers could not tell **what to do**. Feedback from students reading the repo cold produced three complaints: it was unclear whether this was software to install or a document to read; the entry points offered ~35 competing starting choices before any action; and each module's long resource list read as a mandatory to-do list rather than as link-rot insurance. No curriculum content was rewritten in this pass — every change is navigational, explanatory, or a factual correction.

| Change | Detail |
| :--- | :--- |
| **[`START-HERE.md`](START-HERE.md)** | New single entry point, linked from the top of the README. States plainly that there is no software to install, reduces the whole repository to **one** decision ("can you already write Python loops and functions?"), and gives a day-1-to-day-7 plan. |
| **[`guides/how-to-read-a-module.md`](guides/how-to-read-a-module.md)** | Explains module anatomy and what each resource label obliges you to do. Contains the **[Pick-One table](guides/how-to-read-a-module.md#pick-one)** — one default free course pre-chosen for all 27 modules, extracted from the existing `Primary Course Link` lines — plus a worked example of reading M9 correctly (total consumed: one course, three chapters, one project). |
| **[`FAQ.md`](FAQ.md)** | Answers the recurring structural questions: why the module numbers skip 19 and 20, the true module count, realistic timelines, and a full **symbol legend** (✅ ⚠️ ❌ 🔁 ⏭ 📦 ⚡ 🩺 + stratum colours) that previously existed only in this changelog and `audit/`. |
| **[`guides/sources.md`](guides/sources.md)** | 39 citations of the form *"Video 1 (05:05)"* appeared across 10 files with no key anywhere in the repo. All are now resolvable to full URLs, with a note on reading practitioner interviews as testimony rather than research. |
| **README first screen** | Removed the pre-content navigation clutter. Added a "what this is in 30 seconds" table, a prominent pointer to `START-HERE.md`, and an explicit warning that resource lists are **a menu, not a to-do list**. "Start here" became "Entry points by experience" (anchor preserved); the file map is now tiered, ending with *maintainer material — safe to ignore as a learner*. |
| **Stratum pages** | A one-line "reading this page" note added to all six curriculum pages, pointing at the Pick-One table and the citation key. |
| **Factual corrections** | Four reader-facing references to the non-existent **M19** repaired (three in [`resources/books.md`](resources/books.md), one in [`curriculum/1-foundations.md`](curriculum/1-foundations.md)) — they now point at M24 and the M21–M24 range. The version badge, which read `2026.3` while this log read `v2026.4`, is now generated to match. |
| **Community health files** | [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) (Contributor Covenant v2.1) added, per [GitHub's community-health guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors). `CONTRIBUTING.md` documents the resource bar (free-first, named source, replaces-rather-than-adds), the ✅/⚠️/❌/🔁 verification legend actually used in `audit/`, and why module numbers are never recycled. |
| **Issue templates** | The inherited RFC template still described "the current OSSU Curriculum" and linked to `ossu/data-science`. Replaced with four **YAML issue forms** — dead link, resource change, *something was confusing*, and RFC — plus a `config.yml` chooser pointing at `START-HERE.md`, the FAQ, and the module guide. The empty-issue workflow keyed off a sentence in the deleted template, so it needed correcting too; because the automation token cannot write to `.github/workflows/`, the fixed version ships as [`tools/delete-empty-issues.workflow.yml`](tools/delete-empty-issues.workflow.yml) for one-step manual install (see [`tools/README.md`](tools/README.md)). |
| **Link integrity** | All internal links and anchors re-verified with [`tools/check_links.py`](tools/check_links.py) — 0 failures. |

**Deliberately unchanged:** module sequencing, prerequisites, the free-first policy, all curriculum prose, and the vacant M19/M20 numbering.

### v2026.4 — Readable Repo · 2026-08-18

**Diagnosis addressed:** the roadmap's content was strong but delivered as a single 2,236-line, ~300 KB `README.md` — overwhelming on first contact and slow to render. No curriculum text was rewritten in this pass; content was **moved verbatim** and only link paths were mechanically rewritten.

| Change | Detail |
| :--- | :--- |
| **Hub README** | Root `README.md` reduced to a ~160-line landing page: hero, goal, who-this-is-for, start-here, track chooser, a "where everything lives" map, curriculum-at-a-glance, and acknowledgements. |
| **`curriculum/`** | Six stratum pages (`1-foundations.md` … `6-frontier-production.md`) carrying all 27 module specs, plus a [`curriculum/README.md`](curriculum/README.md) index listing every module and the project-enforcement rule. Every page has home/prev/next breadcrumbs. |
| **`guides/`** | [Practitioner fast lane](guides/practitioner-track.md), [companion curricula](guides/companion-curricula.md), [career operations](guides/career-operations.md), and the [progress tracker](guides/progress-tracker.md) as standalone pages. |
| **`resources/`** | [Books + Practitioner Shelf](resources/books.md) and the [production toolchain](resources/toolchain.md). |
| **`CHANGELOG.md`** | The refresh log moved here from the README (this file). |
| **Link integrity** | All internal links (including `coursepages/` and `audit/` cross-references) were rewritten to the new locations and verified by [`tools/check_links.py`](tools/check_links.py) — 0 failures across every `.md` file. A ready-to-install CI workflow ships as [`tools/check-links.workflow.yml`](tools/check-links.workflow.yml) (see [`tools/README.md`](tools/README.md) for the one-step install). |
| **Tooling** | The split itself was performed by [`tools/split_readme.py`](tools/split_readme.py) and [`tools/build_hub.py`](tools/build_hub.py), committed for auditability; a byte-level diff verified all 13 moved sections match the original text exactly after un-doing the mechanical link rewrites. |

### v2026.3 — Practitioner's Pass · 2026-07-30

**Diagnosis addressed:** the curriculum was academically strong but theory-first and intimidating — no practitioner entry point, no enforced project-per-module, no career-reality layer, and no distinct "AI Engineer (Applications)" identity of the kind the 2026 market hires for.

| Workstream | Change | Primary evidence |
| :-- | :--- | :--- |
| **A** | [🚀 Practitioner Track (Fast Lane)](guides/practitioner-track.md#practitioner-track) — a sequenced 6-stage / 6–9-month path; the [track table](README.md#choose-your-track) split into **AI Engineer (Applications)** and **AI Engineer (Systems/Research-adjacent)**; ⚡ **Intuition-First Alternative** callouts added to [M0](curriculum/1-foundations.md#module-0), [M2](curriculum/1-foundations.md#module-2), [M3](curriculum/1-foundations.md#module-3), [M5](curriculum/1-foundations.md#module-5), each stating what you give up and when to come back | Video 1 (00:44–01:09, 03:00–07:15); video 3 (00:53, 04:47) |
| **B** | [Module 1](curriculum/1-foundations.md#module-1) rebuilt around a four-phase pacing structure with ship-milestones, a [free Python course matrix](curriculum/1-foundations.md#python-course-matrix) (8 courses), the recommended pairing stack, the **tutorial-hell escape protocol**, and a disciplined AI-assistant policy naming the **fluency illusion** | Both Scrimba articles; video 1 (03:00–04:00, 09:30); video 3 (01:21) |
| **C** | [Module-project enforcement rule](curriculum/README.md#module-projects) + **18 new 📦 Module Project blocks** so every module M1–M25 now carries a mandatory deliverable with tests, README, and a results memo | Video 1 (05:40–06:05, 10:45–14:05); video 2 (11:30) |
| **D** | [🧭 Career Operations](guides/career-operations.md#career-operations) appendix and the [skills ↔ job-description mapping](guides/career-operations.md#skills-checklist) grounded in **16 live 2026 postings** | Video 2 (04:30–18:40); 16 Greenhouse postings, surveyed 2026-07-26 |
| **E** | [🧰 Practitioner Shelf](resources/books.md#practitioner-shelf) — the applied seven-book canon added alongside (not instead of) the Tier 1 academic spine | Video 3 (full); publisher/author pages |
| **F** | [Minimum Production Bar](curriculum/6-frontier-production.md#production-bar) (12 items) in M24 + toolchain; the [prompting vs RAG vs fine-tuning ladder](curriculum/6-frontier-production.md#module-21) in M21; prompt-injection security and agent eval pipelines promoted to first-class topics in [M22](curriculum/6-frontier-production.md#module-22); Streamlit added and agent-framework pins refreshed in the [toolchain](resources/toolchain.md#toolchain) | Video 1 (07:15, 10:45–12:30); video 3 (05:52); surveyed postings (evaluation in 6/7 AI-Eng roles) |
| **G** | Audit trail, TOC, progress tracker, version badge, `coursepages/` sync, and this log | [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md) |
| **H** | **Visual pass** — a hero banner, a six-stratum journey infographic, and a section banner for each stratum, all in one consistent dark-navy visual language. Every asset is licence-clean: two are model-generated originals, six are rendered deterministically by [`assets/make_banners.py`](assets/make_banners.py), which is committed so any banner can be regenerated or restyled. No third-party or stock imagery is used. Provenance in [`assets/README.md`](assets/README.md) | Trailing brief instruction to match the presentation quality of [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) |

**Sources consumed in full**

* **Video 1** — [How to Become an ML Engineer](https://www.youtube.com/watch?v=UZ_rK9gzVSc) (Senior Applied Scientist, Twitch) — five-phase practical path, from-scratch NumPy discipline, portfolio architecture standard, the fluency illusion, project archetypes.
* **Video 2** — [Breaking into AI/ML from a non-technical background](https://www.youtube.com/watch?v=FeQZmQMffzc) (Applied Scientist, Amazon) — internal locus of control, real-projects-for-real-organisations, interviews-as-data, realistic transition windows.
* **Video 3** — [The Only 7 Books You Need to Become an AI Engineer](https://www.youtube.com/watch?v=Pr9oRVtAqCM) (ex-Coursera / ex-Amazon) — the AI Engineer role definition, intuition-over-derivation, notebook-to-production progression, the seven-book canon.
* **Article 1** — [Scrimba: Best Free Python Courses for Beginners in 2026](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/) ✅
* **Article 2** — [Scrimba: How to Learn Python — A Beginner's Guide (2026)](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) ✅
* **Job market** — 16 live postings from public Greenhouse boards (Anthropic, Scale AI, Figma, Databricks, Cloudflare, Discord, Airtable), surveyed 2026-07-26. Enumerated in [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md).

**Verification summary:** 70 URLs HTTP-checked · **66 ✅ 200** · **3 ⚠️ 403** (bot-gated, browser-accessible: two O'Reilly product pages, BLS) · **0 ❌ dead links shipped**. Four candidate URLs were found broken during research and are **not** in the README: two No Starch Manga Guide path guesses, the per-title StatQuest URLs, and `bytebytego.com/courses/generative-ai-system-design-interview`. Framework versions re-pulled from the PyPI JSON API on 2026-07-30.

**Corrections made to previously-published claims** (found while verifying, not part of any workstream's remit):

| Location | Was | Verified actual | Evidence |
| :-- | :--- | :--- | :--- |
| M1 Required Reading | _Fluent Python_ "3rd Edition, 2025" | **2nd Edition (2022)**; a 3rd edition is not published | [fluentpython.com](https://www.fluentpython.com/) ✅ states "Fluent Python, Second Edition"; matches Tier 1 row 20 |
| M1 Required Reading | _Python Crash Course_ "4th Edition, 2025" | **3rd Edition**; no 4th edition exists | [No Starch catalogue](https://nostarch.com/python-crash-course-3rd-edition) ✅ lists 3rd Ed. as current |
| Practitioner Shelf P7 | Source video credits Alex Xu & Sahn Lam | **Alex Xu, Ali Aminian, Hao Sheng** | [Publisher announcement](https://blog.bytebytego.com/p/our-new-book-generative-ai-system) ✅ |
| Toolchain agents row | smolagents 1.24.0 · LangGraph 1.1.9 | **smolagents 1.26.0 · LangGraph 1.2.10** | PyPI JSON API, 2026-07-30 |

**Deliberately not changed:** the Tier 1 / Tier 2 reading lists, the module numbering scheme (including the M6½ and M8a/M8b splits and the M19/M20 gap), and the mathematical content of M0, M2, M3, M5, M9–M12, M13, and M15. The practitioner doctrine is added **alongside** the academic spine as a labelled alternative route, never as a replacement — where the two conflict, both are stated with their conditions.

### v2026.2 and earlier

See [`audit/FINAL_AUDIT.md`](audit/FINAL_AUDIT.md), [`audit/VERIFICATION.md`](audit/VERIFICATION.md), and [`audit/IMPROVEMENT_SPEC.md`](audit/IMPROVEMENT_SPEC.md) for the P1–P5 verification passes that established the 27-module structure, the free-first resource policy, and the link-verification conventions (✅ live · ⚠️ bot-gated · ❌ dead · 🔁 fixed-with-alternative) used throughout.

---

[🏠 Roadmap home](README.md)
