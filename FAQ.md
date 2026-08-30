[🏠 Roadmap home](README.md) · [🧭 Start here](START-HERE.md)

---

# ❓ Frequently Asked Questions

Short answers to the questions people actually ask on first contact. If your question is about *how to
use* a module rather than *what this repo is*, see [How to read a module](guides/how-to-read-a-module.md).

**Jump to:** [The basics](#basics) · [Structure](#structure) · [Using it](#using-it) · [Time & difficulty](#time) · [Symbols](#symbols) · [Contributing](#contributing)

---

<a id="basics"></a>
## The basics

### What is this repository?

A free, self-study curriculum for data science and AI. It tells you which courses to take, which books
to read, and which projects to build, in what order.

### Is there code to run or software to install?

**No.** This repository contains only Markdown documents. There is nothing to `pip install`, no notebook
to open, no dataset to download. You write code in *your own* repositories as you work through the
modules. If you were looking for a runnable project, this is not that — and nothing is broken.

### Do I need to clone or fork it?

Neither is required; reading it on GitHub is enough. **Fork** it if you want to use the
[progress tracker](guides/progress-tracker.md) as your personal checklist, which is the intended use.

### Who is it for?

Beginners who want a complete path, analysts moving into data science, engineers moving into ML or AI
engineering, and anyone preparing for graduate-level ML. See [Who this is for](README.md#who-this-is-for).

### Does it cost anything?

Every **required** resource is free to access. Some books are listed as optional references and cost
money; they are always labelled, and a free alternative is given wherever one of comparable quality
exists.

### Is it affiliated with a university?

No. It synthesises **publicly-available syllabi** from universities including MIT, Harvard, Stanford,
Cambridge, and IIT Madras into one prerequisite-ordered sequence. All course material remains the
property of those institutions. There is no credential, no enrolment, and no accreditation here.

---

<a id="structure"></a>
## Structure

### Why do the modules skip 19 and 20? Is something missing?

**Nothing is missing.** M19 and M20 existed in earlier versions and were reorganised: old M19 (MLOps)
grew into the current [M24](curriculum/6-frontier-production.md#module-24), and old M20 (Capstone) became
[M26](curriculum/6-frontier-production.md#module-26). Their numbers were deliberately left vacant so that
existing external links and bookmarks to M0–M18 keep working. Renumbering would have broken every
inbound deep link for a purely cosmetic gain. The same reasoning explains **M6½** and the **M8a / M8b**
split — these were inserted between existing modules rather than pushing every later number up by one.

### So how many modules are there really?

**27.** They are numbered M0–M18, M21–M26, plus M6½, with M8 split into M8a and M8b. The count is
27 distinct modules, not 27 consecutive numbers. Full list: [curriculum index](curriculum/README.md).

### What is in each top-level folder?

| Folder | Contents | Read it when |
| :--- | :--- | :--- |
[`curriculum/`](curriculum/) | The 27 module specifications, in six stratum pages | Constantly — this is the curriculum |
| [`guides/`](guides/) | How to read a module, fast lane, career ops, progress tracker, sources | Early and often |
| [`resources/`](resources/) | The book list and the production toolchain | When you need a specific book or tool |
| [`coursepages/`](coursepages/) | Extra scaffolding for the newest modules (M6½, M8b, M21–M25) | Only when you reach those modules |
| [`audit/`](audit/) | Link-verification and fact-checking logs | Basically never, unless you doubt a claim |
| [`tools/`](tools/) | The internal link checker | Only if contributing |
| [`assets/`](assets/) | Banner images and the script that generates them | Only if contributing |

### Why are the module pages so long?

They are **reference documents**, not scripts to be read start to finish. The "Exhaustive Topic List" in
particular exists so you can (a) verify your chosen course covers the material and (b) revise before
interviews. Nobody reads it linearly. See [the anatomy of a module](guides/how-to-read-a-module.md).

---

<a id="using-it"></a>
## Using it

### Where do I actually start?

[START-HERE.md](START-HERE.md). It gives you a four-day plan and one decision to make.

### There are hundreds of links. Which resource do I pick?

Use the [Pick-One table](guides/how-to-read-a-module.md#pick-one) — one default course per module, all
free. The other links are alternatives for when a default does not suit you, and insurance against link
rot. **A module's resource list is a menu, not a to-do list.**

### Do I have to do all 27 modules?

**No,** and you should not by default. Pick a target role in
[Choose your track](README.md#choose-your-track) and do that track's module set. Only the research /
PhD-prep track uses nearly everything.

### Can I skip the mathematics?

Yes, with a stated cost. The maths-heavy modules each carry an **⚡ Intuition-First Alternative** callout
naming exactly what you give up and when you will need to come back. The
[Practitioner fast lane](guides/practitioner-track.md) is the fully sequenced version of that route.
Short version: you will be able to *use* methods and unable to *verify* them — fine for most applied
jobs, disqualifying for research.

### Do I have to build the projects?

Yes. This is the one non-negotiable rule: **you do not advance until the current module's project is
pushed to a public repository.** Course completion is not evidence; a repository is. See
[the enforcement rule](curriculum/README.md#module-projects).

### Can I do modules out of order or in parallel?

Respect the **Strict Prerequisites** line in each module and you can otherwise arrange things freely.
Running a maths module in parallel with a programming module is a common and effective pattern.

### What does "Video 1 (05:05)" mean?

It is a citation. The key is in [guides/sources.md](guides/sources.md#citation-key) — it names all three
videos, both articles, and the job-posting survey, with links and what each is used to support.

---

<a id="time"></a>
## Time & difficulty

<a id="how-long"></a>
### How long does this take?

It depends entirely on which finish line you mean, which is why you will see different numbers in
different places:

| Goal | Estimate | Conditions |
| :--- | :--- | :--- |
| Employable in an applied AI/ML role | **6–9 months** | [Fast lane](guides/practitioner-track.md), 15–20 hrs/week, already comfortable programming |
| Python job-ready (analyst / junior) | **9–12 months** | 5–10 hrs/week, portfolio built |
| Career change from a non-tech background | **18–36 months** | Competing with laid-off senior engineers |
| The complete curriculum incl. maths spine + capstone | **24–36 months** | 20–25 hrs/week, all tracks |

These are not in conflict — they measure different things. Sources and reasoning:
[sources](guides/sources.md).

### Is it beginner-friendly?

The *sequence* is, and prerequisites are stated everywhere. But the primary resources are real
university courses, which are demanding. If you are new to programming, start with the
[Microsoft companion curricula](guides/companion-curricula.md), which supply the guided lessons,
quizzes, and solutions that university courses assume you don't need.

### I'm stuck / demoralised. Is that normal?

Yes, and it is usually a prerequisite gap rather than lack of ability. Check the **Strict
Prerequisites** line and go back one module. The other common cause is *tutorial hell* — consuming
instruction while producing nothing; the fix is the five-step protocol in
[Module 1](curriculum/1-foundations.md#module-1).

---

<a id="symbols"></a>
## Symbols

These marks appear next to links and claims throughout the repository.

| Symbol | Meaning |
| :--- | :--- |
| ✅ | Link was HTTP-checked and returned 200 at the last audit |
| ⚠️ | Returns 403 to automated checkers but **opens normally in a browser** (common for O'Reilly and some publishers) — the link is good |
| ❌ | Dead. These are removed rather than shipped; the mark appears only in [`audit/`](audit/) logs |
| 🔁 | The original URL broke and was replaced with a verified alternative |
| ⏭ | Deliberately deferred to a later release |
| 📦 | A mandatory module project |
| ⚡ | An intuition-first alternative route for the practitioner track |
| 🩺 | The maths diagnostic |
| 🟩 🟨 🟧 🟦 🟪 🔴 | The six curriculum strata, in order |

---

<a id="contributing"></a>
## Contributing

### Can I contribute?

Yes — corrections, dead-link reports, and resource updates are welcome, and you don't need to be an
expert. Reporting a single dead link is a real contribution. See [CONTRIBUTING.md](CONTRIBUTING.md)
for the resource bar and the [code of conduct](CODE_OF_CONDUCT.md) for expected behaviour.

### I found a broken link.

Open an issue using the **Dead or moved link** template — it prompts for the URL, the file it appears
in, and what you saw. Or open a PR replacing it with a verified alternative. Run
`python3 tools/check_links.py` before submitting to confirm internal links still pass.

### The docs confused me. Is that worth reporting?

Yes. There is a **Something was confusing** issue template for exactly this. If you couldn't work out
what to do, the signposting failed — that is a defect, not your mistake.

### What licence is this under?

[CC BY-SA 4.0](LICENSE.md). You may share and adapt it, including commercially, with attribution and
under the same licence. Note this covers **this repository's own text and images** — linked course
material belongs to its respective institution.

---

**Question not answered here?** Open an issue. If it is a question about first contact with the repo,
it belongs on this page and the answer will be added.

---

[🏠 Roadmap home](README.md) · [🧭 Start here](START-HERE.md) · [📖 How to read a module](guides/how-to-read-a-module.md)
