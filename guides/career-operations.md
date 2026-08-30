[🏠 Roadmap home](../README.md)

---

<a id="career-operations"></a>
# 🧭 Career Operations

Everything above this line is about competence. This section is about the entirely separate skill of **converting competence into a job** — which most technical curricula omit, and which is where most self-taught learners actually stall.

> **Citations on this page.** *"Video 2 (07:12)"* and similar refer to named practitioner sources resolved in [sources](sources.md#citation-key).

Two honest caveats before anything else. First, the guidance here is doctrine drawn from named practitioners (see [sources](../CHANGELOG.md#refresh-log)), not from a controlled study; treat it as informed heuristics. Second, nothing in this section substitutes for the [module projects](../curriculum/README.md#module-projects). Career tactics applied to an empty portfolio do not work.

## 1. The internal locus of control

The single highest-leverage mental model in the source material. An **internal** locus of control means you attribute outcomes to your own actions; an **external** locus means you attribute them to the market, your degree, your age, or luck.

Video 2 (07:12) makes the operational case: the market, the hiring bar, and your background are all fixed inputs you cannot edit. The only editable variables are what you build, who you talk to, and how many attempts you make. Every hour spent on the fixed inputs is an hour not spent on the editable ones.

What this looks like in practice:

| External framing (stalls) | Internal framing (moves) |
| :--- | :--- |
| "The market is terrible for juniors." | "The market is competitive, so my portfolio has to be visibly better than a bootcamp's. Here is the specific project that does that." |
| "I don't have a CS degree." | "I don't have the credential, so I need the work to speak first. My repo is the credential." |
| "I got rejected, I'm not good enough." | "I got rejected. What did the process tell me about the gap? Which module closes it?" |
| "I'll apply once I've finished the roadmap." | "I'll apply now, and use the rejections to find out which modules actually matter for the roles I want." |

The framing is not positive thinking. It is a filter that routes your attention to the variables you can act on.

## 2. Iterative job seeking — apply at ~70 % match

Job descriptions are wish-lists assembled by committee, not specifications. The observed practice among people who transition successfully is to **apply when you meet roughly 70 % of the listed requirements**, and to treat the remaining 30 % as the thing the job will teach you.

* **Apply early and continuously, not after "finishing."** Applications are a data-collection instrument, and they have a long latency. Starting them six months before you feel ready is how you find out what the real bar is while you still have time to move it.
* **Do not gate on the roadmap being complete.** By the end of [M12](../curriculum/3-classical-ml.md#module-12) plus [M24](../curriculum/6-frontier-production.md#module-24)'s production discipline you are already applicable to a meaningful slice of roles. See the [track table](../README.md#choose-your-track) for the minimum module set per role.
* **Track your funnel.** Applications sent → screens → technical rounds → onsites → offers. If a stage has a zero conversion rate after 20+ attempts, the problem is located at that stage and nowhere else. Resume problem, screen problem, and technical problem all look identical from the inside if you are not counting.
* **Expect a high denominator.** Video 2 (14:20) is blunt that the number of applications is measured in the hundreds, not the dozens, and that this is normal rather than a signal of failure.

## 3. Interviews as data gathering

Reframe the interview: it is the only place you get free, high-fidelity information about the gap between what you know and what the market pays for.

* **Ask what the last person in this role spent their time on.** This tells you the real job, which is frequently not the job description.
* **Ask what the team's biggest technical problem is right now.** Notice whether your roadmap covers it. If three separate companies name the same problem, that is a curriculum signal — go build a project on it.
* **Log every question you could not answer.** That log is a personalised syllabus derived from actual demand. Map each entry to a module and close it.
* **Debrief every rejection in writing.** Video 2 (16:05) treats a failed interview as a completed experiment: it cost you two hours and returned a list of specific, addressable gaps. The only wasted interview is the one you do not write up.
* **Do informational interviews too.** A 20-minute conversation with someone doing the job you want is cheaper than six months of guessing which skills matter.

## 4. Cold outreach

Cold outreach has a low response rate and an extremely high value per response, which makes it worth doing badly at volume rather than perfectly at low volume.

* **Message the practitioner, not the recruiter.** Someone doing the job can tell you what the job is; a recruiter can only tell you what the requisition says.
* **Lead with the work, not with a request.** "I built *X*, here is the repo, I noticed your team works on *Y* — did I get the hard part wrong?" outperforms "can I pick your brain."
* **Be specific and short.** Three sentences. One question that can be answered in one paragraph.
* **Ask for information, not a referral.** Referrals follow from relationships; asking for one first ends the conversation.
* **Follow up once, then stop.** Silence is usually a full inbox, not a verdict — but two follow-ups is a cost imposed on a stranger.

## 5. Build for real people, not for datasets

The strongest single differentiator in the source material. Video 2 (11:30) argues that a project built **for a real person or organisation that wanted the result** outperforms any generic dataset project, because it carries a stakeholder, a constraint, a deadline, and an outcome — the four things that make it an interview story instead of a screenshot.

Where to find real problems, in rough order of accessibility:

1. **A local non-profit, charity, or community organisation.** They have data, no analyst, and no budget. Offer one specific deliverable, not "help with data."
2. **Your current employer, in your current non-technical role.** This is the highest-conversion path in the material: you already have domain context, data access, and trust. Automate something painful, then present it.
3. **Open-source projects.** Real code, real review, a public record of collaboration, and a maintainer who will tell you when your PR is wrong.
4. **A small business you already use.** A café, a gym, a freelancer. Scope it to one week.
5. **Your own recurring annoyance.** You are a real user with real requirements — a legitimate stakeholder of one.

> **The Kaggle caveat, stated fairly.** Kaggle is genuinely excellent for learning modelling technique against a strong benchmark, and notably **zero of the 16 [surveyed 2026 postings](#skills-checklist) mention Kaggle at all**, while 15 of 16 ask for stakeholder communication. Use Kaggle to build skill; do not expect it to carry a portfolio. The competition hands you a cleaned dataset, a defined target, and a fixed metric — which is to say it removes exactly the three parts of the job that are hard.

## 6. Community and accountability

Self-directed study fails at the motivation layer far more often than at the difficulty layer. Structural fixes, in increasing order of effectiveness:

* **Publish weekly.** One post, one commit log, one paragraph on what you shipped. Public and boring beats private and ambitious.
* **Find one accountability partner** at a similar stage, with a fixed weekly check-in. Two people rarely quit in the same week.
* **Join a technical community and answer questions**, not just ask them. Explaining something badly and being corrected is the highest-bandwidth learning available for free.
* **Work in public.** Post the broken version. Video 2 (09:40) treats visible, in-progress work as both an accountability mechanism and a discovery mechanism — people cannot offer you opportunities they cannot see.
* **Beginner's mindset.** Video 2 (04:30) frames the transition from a senior non-technical role to a junior technical one as requiring you to be publicly, comfortably bad at something for a year. That is the actual cost of the transition, and it is a cost, not a personality flaw.

## 7. Honest timelines — two estimates, both with conditions

The sources disagree, and the disagreement is informative rather than a contradiction to be resolved. Both are presented with their conditions attached; pick the row whose conditions match your situation.

| Estimate | Source & conditions | What it assumes |
| :--- | :--- | :--- |
| **9–12 months to job-ready** | Scrimba's [Python guide](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) ✅ | Consistent near-full-time study; scope is **Python-centric software/data roles**, not research; you build a real portfolio; some prior technical or quantitative background. This is *"job-ready for a first junior role"*, not *"competent ML engineer."* |
| **18–36 months for a career change** | Video 2 (18:40) — a transition into Applied Science from a non-technical background | Part-time study alongside an existing job; starting with little or no programming; targeting roles with a genuine mathematical bar. 18 months is the fast case with unusual intensity; 24–30 is typical; 36 is normal with a demanding job or caregiving. |
| **24–36 months for the full roadmap** | This roadmap's own [pacing](../README.md#curriculum-at-a-glance) | Completing all 27 modules including the [full maths spine](../curriculum/1-foundations.md#module-0) at ~15–20 h/week. This is the *research-capable* target, not the employability target. |

**How to reconcile them.** They measure different finish lines. Employability arrives well before completion: the [Practitioner Fast Lane](practitioner-track.md#practitioner-track) targets 6–9 months to a shippable AI-Engineer portfolio precisely by deferring the proof-level mathematics, and the full spine continues afterwards. If you are studying part-time from a non-technical background, plan for the 18–36 month band and treat the 9–12 month figure as the best case for someone with prior technical background studying near-full-time. Anyone quoting a single number without stating these conditions is selling something.

<a id="skills-checklist"></a>
## 8. Skills checklist ↔ job-description mapping

Grounded in a survey of **16 live 2026 postings** pulled from public Greenhouse job boards on **2026-07-26** — Anthropic (4), Scale AI (3), Figma (3), Databricks (2), Cloudflare (2), Discord (1), Airtable (1) — spanning AI Engineer / Forward-Deployed / Applied AI (7), ML Engineer (3), Data Scientist (4), and Data Engineer (2). Full posting list is in [`audit/AUDIT_v2026.3.md`](../audit/AUDIT_v2026.3.md).

**Counts below are literal mention frequencies in that sample.** The sample is small and skewed toward AI-native companies, so read it as a directional signal about *what these employers emphasise*, not as a national labour-market statistic.

> **The three findings that should change how you study.**
> 1. **Communication outranks every technical skill.** 15 of 16 postings ask for stakeholder communication, cross-functional collaboration, or customer-facing ability — more than Python (9), SQL (6), or any framework. This is why [M25](../curriculum/6-frontier-production.md#module-25) is a required module and not an appendix.
> 2. **Evaluation is the AI-Engineer skill.** 6 of 7 AI-Engineer/Forward-Deployed postings name evaluation explicitly. Building a RAG demo is table stakes; *proving it works* is the job. See [M21](../curriculum/6-frontier-production.md#module-21) and [M23](../curriculum/6-frontier-production.md#module-23).
> 3. **Nobody asked for a PhD, and nobody asked about Kaggle.** 0 of 16 required a doctorate; 0 of 16 mentioned Kaggle. 5 of 16 mentioned a degree at all, most as "or equivalent experience."

### AI Engineer (Applications) — 7 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| Customer-facing communication, translating ambiguous business problems into technical scope | **7/7** | [M25](../curriculum/6-frontier-production.md#module-25) |
| Evaluation of LLM systems — quality measurement, regression suites, benchmark design | **6/7** | [M21](../curriculum/6-frontier-production.md#module-21) · [M23](../curriculum/6-frontier-production.md#module-23) · [M18](../curriculum/6-frontier-production.md#module-18) |
| Cloud platforms (AWS/GCP/Azure) and deploying into a customer's environment | 3/7 | [M24](../curriculum/6-frontier-production.md#module-24) |
| Python as the primary implementation language | 2/7 | [M1](../curriculum/1-foundations.md#module-1) |
| LLM / foundation-model application development | 2/7 | [M18](../curriculum/6-frontier-production.md#module-18) · [M21](../curriculum/6-frontier-production.md#module-21) |
| Agents, tool-use, multi-step workflows | 2/7 | [M22](../curriculum/6-frontier-production.md#module-22) |
| Distributed data processing (Spark and similar) | 2/7 | [M8b](../curriculum/2-statistics-and-data.md#module-8b) |
| RAG / retrieval / vector search | 1/7 | [M21](../curriculum/6-frontier-production.md#module-21) |
| Fine-tuning and adaptation | 1/7 | [M18](../curriculum/6-frontier-production.md#module-18) |
| Prompt design and prompt-injection awareness | 1/7 | [M22](../curriculum/6-frontier-production.md#module-22) · [M23](../curriculum/6-frontier-production.md#module-23) |

> **Note on the Forward-Deployed Engineer title.** 5 of the 7 postings in this family are "Forward Deployed Engineer" or "Applied AI Architect" rather than "AI Engineer." This is currently the highest-volume real title for the [AI Engineer (Applications)](../README.md#choose-your-track) role, and its defining requirement is the pairing of solid software engineering with direct customer contact — which is exactly why [M25](../curriculum/6-frontier-production.md#module-25) sits on the critical path of that track.

### ML Engineer — 3 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| LLM / foundation-model systems in production | **3/3** | [M18](../curriculum/6-frontier-production.md#module-18) · [M21](../curriculum/6-frontier-production.md#module-21) |
| Agent systems and agent oversight | **3/3** | [M22](../curriculum/6-frontier-production.md#module-22) · [M23](../curriculum/6-frontier-production.md#module-23) |
| Python | 2/3 | [M1](../curriculum/1-foundations.md#module-1) |
| RAG / retrieval infrastructure | 2/3 | [M21](../curriculum/6-frontier-production.md#module-21) |
| Pipeline orchestration (Airflow/Dagster) | 2/3 | [M24](../curriculum/6-frontier-production.md#module-24) · [M8b](../curriculum/2-statistics-and-data.md#module-8b) |
| MLOps, monitoring, observability | 2/3 | [M24](../curriculum/6-frontier-production.md#module-24) |
| Experimentation and A/B measurement | 2/3 | [M6½](../curriculum/2-statistics-and-data.md#module-6-half) |
| Statistics, causal reasoning, regression | 2/3 | [M6](../curriculum/2-statistics-and-data.md#module-6) · [M9](../curriculum/3-classical-ml.md#module-9) |
| Evaluation pipelines | 2/3 | [M23](../curriculum/6-frontier-production.md#module-23) |
| Stakeholder collaboration | 2/3 | [M25](../curriculum/6-frontier-production.md#module-25) |
| Deep-learning frameworks (PyTorch) | 1/3 | [M15](../curriculum/5-deep-learning.md#module-15) |
| Containers / Kubernetes | 1/3 | [M24](../curriculum/6-frontier-production.md#module-24) |
| Warehouse / dbt | 1/3 | [M8a](../curriculum/2-statistics-and-data.md#module-8a) |

### Data Scientist — 4 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| SQL — fluent, non-negotiable | **4/4** | [M8a](../curriculum/2-statistics-and-data.md#module-8a) |
| Stakeholder communication and influencing product decisions | **4/4** | [M25](../curriculum/6-frontier-production.md#module-25) |
| Python | **3/4** | [M1](../curriculum/1-foundations.md#module-1) · [M7](../curriculum/2-statistics-and-data.md#module-7) |
| Experimentation / A/B testing | **3/4** | [M6½](../curriculum/2-statistics-and-data.md#module-6-half) |
| Statistical inference, causal reasoning, regression | **3/4** | [M6](../curriculum/2-statistics-and-data.md#module-6) · [M6½](../curriculum/2-statistics-and-data.md#module-6-half) · [M9](../curriculum/3-classical-ml.md#module-9) |
| Warehouse / dbt / BigQuery-class tooling | **3/4** | [M8a](../curriculum/2-statistics-and-data.md#module-8a) |
| LLM-related analysis | 2/4 | [M18](../curriculum/6-frontier-production.md#module-18) |
| Large-scale data processing | 2/4 | [M8b](../curriculum/2-statistics-and-data.md#module-8b) |
| Metrics definition and instrumentation | 2/4 | [M25](../curriculum/6-frontier-production.md#module-25) |

> **The DS pattern is stable and it is not glamorous.** SQL + statistics + experimentation + communication appears in essentially every posting; deep learning appears in none of the four. If your target is Data Scientist, the highest-return modules are [M6](../curriculum/2-statistics-and-data.md#module-6), [M6½](../curriculum/2-statistics-and-data.md#module-6-half), [M8a](../curriculum/2-statistics-and-data.md#module-8a), and [M25](../curriculum/6-frontier-production.md#module-25) — not [M15](../curriculum/5-deep-learning.md#module-15)–[M18](../curriculum/6-frontier-production.md#module-18).

### Data Engineer — 2 postings

| Skill the postings ask for | Sample | Where you learn it |
| :--- | :--- | :--- |
| SQL | **2/2** | [M8a](../curriculum/2-statistics-and-data.md#module-8a) |
| Python | **2/2** | [M1](../curriculum/1-foundations.md#module-1) |
| Orchestration (Airflow/Dagster/equivalent) | **2/2** | [M24](../curriculum/6-frontier-production.md#module-24) · [M8b](../curriculum/2-statistics-and-data.md#module-8b) |
| Warehouse modelling / dbt | **2/2** | [M8a](../curriculum/2-statistics-and-data.md#module-8a) |
| Cross-functional partnership with DS and product | **2/2** | [M25](../curriculum/6-frontier-production.md#module-25) |
| Streaming / event pipelines | 1/2 | [M8b](../curriculum/2-statistics-and-data.md#module-8b) |
| LLM-adjacent data work | 1/2 | [M18](../curriculum/6-frontier-production.md#module-18) |

> **Sample-size discipline.** Two postings is an anecdote, not a distribution. The Data Engineer row is included for completeness and because it agrees with the widely-observed core (SQL + Python + orchestration + modelling), but do not weight it as evidence. Before committing to any track, run this same exercise yourself on 10–15 postings **at companies you would actually join** — the mechanics are documented in [`audit/AUDIT_v2026.3.md`](../audit/AUDIT_v2026.3.md), take about an hour, and produce a checklist calibrated to your market rather than to this sample.

---

[🏠 Roadmap home](../README.md)
