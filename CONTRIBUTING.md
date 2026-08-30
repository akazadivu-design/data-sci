[🏠 Roadmap home](README.md) · [🧭 Start here](START-HERE.md) · [❓ FAQ](FAQ.md)

---

<a id="contributing"></a>
# 🤝 Contributing

Thanks for being here. This curriculum stays useful only because people report the things that
break — and links break constantly. **Reporting one dead link is a real contribution.** You do not
need to be an expert, and you do not need to write code.

<a id="tldr"></a>
## The 30-second version

| I want to… | Do this |
| :--- | :--- |
| Report a dead or moved link | [Open an issue](https://github.com/akazadivu-design/data-sci/issues/new/choose) → *Dead or moved link*. Paste the URL and the file it's in. |
| Fix a typo | Edit the file on GitHub and open a pull request. No issue needed. |
| Suggest a better course for a module | [Open an issue](https://github.com/akazadivu-design/data-sci/issues/new/choose) → *Resource change*. Read [the resource bar](#resource-bar) first. |
| Propose restructuring the curriculum | Open an **RFC** issue. See [Bigger changes](#rfc). |
| Ask a question | Check the [FAQ](FAQ.md) first — most questions are answered there. |

<a id="no-setup"></a>
## There is nothing to install

This repository is **documentation only**. There is no application, no build step, no package
manager, and no dependencies. It is Markdown files plus images.

The only tool is the internal link checker, which needs nothing but Python 3:

```bash
git clone https://github.com/akazadivu-design/data-sci.git
cd data-sci
python3 tools/check_links.py
```

Expected output is a line reporting the number of internal links checked and **0 failures**.
Run it before you submit any pull request that adds, moves, or renames a link, a file, or a
heading. See [`tools/README.md`](tools/README.md) for what each script does.

> **What the checker does and does not do.** It validates *internal* links — relative file paths
> and `#anchors` — using GitHub's slug rules and explicit `<a id="...">` tags. It does **not** check
> external URLs, because there are over 800 of them and many return `403` to bots while working fine
> in a browser. External links are verified by hand during a refresh pass and logged in
> [`audit/VERIFICATION.md`](audit/VERIFICATION.md).

---

<a id="dead-links"></a>
## Reporting a dead link

This is the most valuable thing you can do. Please include:

1. **The URL** that is broken.
2. **The file and module** it appears in — e.g. `curriculum/3-classical-ml.md`, Module 9.
3. **What you saw** — a 404 page, a paywall, a redirect somewhere unrelated, or a video marked
   private.
4. **A replacement, if you found one** — optional, but it speeds things up enormously.

If the link works in your browser but the checker or a bot reports it failing, say so. That is a
`403` bot-gate, not a dead link, and the repository marks those `⚠️` rather than removing them.

<a id="verification-legend"></a>
### The status legend this repo uses

Every verified resource is recorded with one of four markers. If you are filing a report or a PR,
using the same markers helps a lot:

| Marker | Meaning |
| :---: | :--- |
| ✅ | Live — HTTP `200` or `302`. Use as-is. |
| ⚠️ | Bot-gated — HTTP `403` to automated fetches, but reachable in a normal browser. Kept, with disclosure. |
| ❌ | Dead — HTTP `4xx`, `5xx`, or DNS failure. Must be replaced. |
| 🔁 | Replaced — a dead or wrong resource swapped for a verified alternative. |

The full legend for curriculum symbols (📦 ⚡ 🩺 ⏭ and the stratum colours) is in the
[FAQ](FAQ.md#symbols).

---

<a id="resource-bar"></a>
## Proposing a different resource

The curriculum is opinionated on purpose, so resource swaps are held to a bar. A proposal is most
likely to be accepted if it clears these:

| Criterion | Why it exists |
| :--- | :--- |
| **Free to complete** | The badge says every *required* resource is free. Paid material can only ever be listed as **optional**, and must be labelled as such. |
| **From a named, checkable source** | A university course, an institutional textbook, an official docs site, or a clearly credentialed author. Not an anonymous blog aggregating other people's content. |
| **Covers the module's stated outcome** | Each module names what you should be able to do afterwards. A resource that teaches an adjacent topic is not a substitute. |
| **Verified live at time of proposal** | Say what you got: `200`, `403`-but-browser-OK, etc. |
| **Replaces rather than piles on** | See below. |

<a id="no-piling-on"></a>
### Please do not just add more links

The single biggest complaint about this repository has been that modules list so many resources
that readers freeze and don't start. The lists are a **menu, not a to-do list** — they exist as
link-rot insurance — but every extra entry makes that harder to see.

So:

- **Prefer replacing** a dead or weaker resource over appending a new one.
- If you genuinely want to *add*, say which existing entry it should displace, or argue why the
  module needs another alternative.
- If your resource is better than the current default, propose updating the
  [Pick-One table](guides/how-to-read-a-module.md#pick-one) too — that table is what most readers
  actually follow.

<a id="citations"></a>
### If you cite a video or article

Citations in the curriculum look like *"Video 1 (05:05)"* and resolve through
[`guides/sources.md`](guides/sources.md#citation-key). If you introduce a new source, add it to
that key with its full URL and a one-line note on what kind of evidence it is. Practitioner
interviews are testimony, not research, and the repository labels them that way.

---

<a id="pull-requests"></a>
## Pull requests

Small and focused beats large and sweeping.

1. Fork the repository and create a branch — e.g. `fix/dead-link-m9`.
2. Make the change. Keep the surrounding formatting: tables stay tables, the breadcrumb line stays
   at the top of the file, `<a id="...">` anchors are **never** deleted or renamed.
3. Run `python3 tools/check_links.py` and confirm 0 failures.
4. Open the PR against `master` with a description that says **what** changed and **why**, plus the
   verification status of any URL you touched.

<a id="anchors-warning"></a>
> ### ⚠️ Never remove an anchor or renumber a module
>
> Explicit `<a id="...">` tags exist so that links from outside the repository keep working. The
> same reasoning is why the module numbers **skip 19 and 20**, and why **M6½** and **M8a/M8b**
> exist instead of a clean renumber. Old M19 became [M24](curriculum/6-frontier-production.md#module-24)
> and old M20 became [M26](curriculum/6-frontier-production.md#module-26); those two numbers were
> left vacant deliberately. A PR that "tidies up" the numbering breaks every inbound link and will
> be declined. Background is in the [FAQ](FAQ.md#structure).

<a id="prose"></a>
### Editing prose

Curriculum text is moved verbatim between refactors and diff-verified — see the verbatim-move
guarantee in [`tools/README.md`](tools/README.md). If you are rewriting module prose rather than
correcting an error, open an issue first so the intent can be discussed before you spend the effort.

<a id="changelog"></a>
### The changelog

Substantive changes get an entry in [`CHANGELOG.md`](CHANGELOG.md). You don't have to write it
yourself — flag in your PR that it needs one, or add a line under the newest version heading if
you're comfortable doing so.

---

<a id="rfc"></a>
## Bigger changes: the RFC process

For anything that changes the **shape** of the curriculum — adding or removing a module, resequencing
a stratum, changing a prerequisite chain, altering the free-first policy — open an issue using the
**RFC** template rather than a pull request.

An RFC states the problem in one sentence, gives the background and the trade-offs, lists the
concrete proposed changes, and lists the alternatives considered. It stays open for comment for
about a month before anything is merged, so that people part-way through the affected modules get a
chance to object.

This is deliberately slower than a normal PR. People are following this thing for months at a time;
reshuffling it under them has a real cost.

---

<a id="conduct"></a>
## Code of conduct

Be decent. Assume the person on the other end is learning, is short on time, or is in a different
timezone and a second language. Critique resources, not people.

Participation is governed by the [Contributor Covenant v2.1](CODE_OF_CONDUCT.md). Unacceptable
behaviour can be reported by opening an issue or contacting a maintainer privately.

<a id="licence"></a>
## Licence

By contributing, you agree your contribution is licensed under
[CC BY-SA 4.0](LICENSE.md), the same licence as the rest of the repository. This covers this
repository's own text and images — linked course material stays with its respective institution.

---

[🏠 Roadmap home](README.md) · [🧭 Start here](START-HERE.md) · [❓ FAQ](FAQ.md) · [🗓️ Changelog](CHANGELOG.md)
