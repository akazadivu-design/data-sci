#!/usr/bin/env python3
"""Assemble the new hub README.md.

All prose is taken VERBATIM from the original README (by line range).
Only navigation tables / repository-map sections are new, and they contain
only links to files that exist. Internal anchor links are rewritten with the
same ANCHOR_OWNER map used by split_readme.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from split_readme import ANCHOR_OWNER, LINK_RE, rel

ROOT = "/home/user/webapp"
with open(os.path.join(ROOT, "README.md.orig"), encoding="utf-8") as f:
    LINES = f.read().split("\n")

def seg(a, b):
    out = LINES[a-1:b]
    while out and out[-1].strip() in ("", "---"):
        out.pop()
    return "\n".join(out)

def rw(text):
    def sub(m):
        anchor = m.group(1)
        owner = ANCHOR_OWNER.get(anchor)
        if owner is None:
            print("WARN unmapped anchor in hub:", anchor)
            return m.group(0)
        if owner == "README.md":
            return m.group(0)
        return "](%s#%s)" % (owner, anchor)
    return LINK_RE.sub(sub, text)

# ---- verbatim pieces from the original ----
HERO       = seg(1, 15)            # banner, title, badges, subject strip (excl. old quicklinks)
GOAL       = seg(22, 33)           # ## Goal
WHO        = seg(34, 43)           # ## Who this is for
HOWTO      = seg(44, 53)           # ## How to use this roadmap
STARTHERE  = seg(54, 67)           # ## Start here (incl. anchor + table + milestone note)
TRACKS     = seg(133, 146)         # ## Choose your track (table + AI-engineer note)
GLANCE     = seg(211, 226)         # ## Curriculum at a glance (image + table)
ACK        = seg(2208, 2226)       # acknowledgements body (without trailing footer div)
FOOTER     = seg(2230, 2236)       # closing centered div

QUICKNAV = """\
[🚀 Fast lane (6–9 mo)](guides/practitioner-track.md) · [📚 Full curriculum](curriculum/README.md) · [🧭 Choose a track](#choose-your-track) · [📖 Books](resources/books.md) · [🛠️ Toolchain](resources/toolchain.md) · [💼 Career ops](guides/career-operations.md) · [✅ Progress tracker](guides/progress-tracker.md)"""

ROADMAP_NAV = """\
<a id="roadmap"></a>
## 🗺️ Where everything lives

The curriculum is split into focused pages so you never scroll through 2,000 lines again. **Start with the [curriculum index](curriculum/README.md)** — it lists every module with a one-line description.

| Section | What you will find there |
|---|---|
| 🚀 [Practitioner Track (fast lane)](guides/practitioner-track.md) | The 6-stage, 6–9-month employment-first sequence, with the trade-offs stated |
| 📚 [Curriculum index](curriculum/README.md) | All 27 modules across six strata, plus the module-project enforcement rule |
| 🟩 [1 · Foundations](curriculum/1-foundations.md) | Math diagnostic · M0–M5: proof, Python, calculus, linear algebra, algorithms, probability |
| 🟨 [2 · Statistics & Data](curriculum/2-statistics-and-data.md) | M6–M8b: inference, causal inference, EDA, SQL, distributed data |
| 🟧 [3 · Classical ML](curriculum/3-classical-ml.md) | M9–M12: regression, classification, unsupervised, ensembles |
| 🟦 [4 · Probabilistic ML](curriculum/4-probabilistic-ml.md) | M13–M14: Bayesian inference, MCMC, time series |
| 🟪 [5 · Deep Learning](curriculum/5-deep-learning.md) | M15–M17: MLPs/CNNs, transformers, generative models, RL |
| 🔴 [6 · Frontier & Production](curriculum/6-frontier-production.md) | M18, M21–M26: LLMs, RAG, agents, safety, MLOps, product, capstone |
| 🤝 [Companion curricula](guides/companion-curricula.md) | Where the two Microsoft beginner curricula slot into this roadmap |
| 📖 [Books](resources/books.md) | Core textbook list + the 🧰 Practitioner Shelf |
| 🛠️ [Toolchain](resources/toolchain.md) | The production tool choices, with versions |
| 🧭 [Career Operations](guides/career-operations.md) | Job search mechanics + the skills ↔ job-description mapping |
| ✅ [Progress tracker](guides/progress-tracker.md) | Fork-and-tick checklist for every module and project |
| 🗓️ [Changelog](CHANGELOG.md) | Versioned refresh log with what changed and why |
| 🔍 [Audit trail](audit/) | Link-verification and fact-checking logs for every release |
| 📂 [Course pages](coursepages/) | Per-module scaffolds for the newest modules (M6½, M8b, M21–M25) |"""

parts = [
    rw(HERO),
    "",
    QUICKNAV,
    "",
    "</div>",
    "",
    "---",
    "",
    rw(GOAL),
    "",
    rw(WHO),
    "",
    rw(HOWTO),
    "",
    rw(STARTHERE),
    "",
    rw(TRACKS),
    "",
    ROADMAP_NAV,
    "",
    rw(GLANCE),
    "",
    "> **Guided companions:** the [Microsoft Data Science / ML for Beginners pairing](guides/companion-curricula.md) supplies lesson-by-lesson beginner material that maps onto these modules.",
    "",
    "---",
    "",
    rw(ACK),
    "",
    "---",
    "",
    FOOTER,
    "",
]
out = "\n".join(parts)
with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(out)
print("hub README.md written:", out.count("\n") + 1, "lines")
