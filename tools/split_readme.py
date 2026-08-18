#!/usr/bin/env python3
"""Split the monolithic README.md into a hub + per-section files.

Content is moved VERBATIM by line ranges (1-indexed, inclusive).
The only transformations applied to moved text are link-path rewrites:
  - `](#anchor)`  ->  `](<relative-path-to-owner-file>#anchor)` when the
    anchor now lives in a different file;
  - asset/audit/license relative paths get `../` prefixes for files that
    move into subdirectories.
Nothing else in the moved text is altered.
"""
import os
import re
import sys

ROOT = "/home/user/webapp"
SRC = os.path.join(ROOT, "README.md")

with open(SRC, encoding="utf-8") as f:
    LINES = f.read().split("\n")  # LINES[0] is line 1


def seg(a, b):
    """Return verbatim lines a..b (1-indexed, inclusive), trailing
    separator ('---') and blank lines stripped."""
    out = LINES[a - 1 : b]
    while out and out[-1].strip() in ("", "---"):
        out.pop()
    return "\n".join(out)


# ---------------------------------------------------------------- segments
# Verified boundaries (see analysis): each range starts at its <a id> or
# heading line and ends just before the next section's separator.
SEGMENTS = {
    "guides/practitioner-track.md": seg(69, 132),
    "guides/companion-curricula.md": seg(228, 264),
    "curriculum/1-foundations.md": seg(285, 771),
    "curriculum/2-statistics-and-data.md": seg(773, 963),
    "curriculum/3-classical-ml.md": seg(965, 1120),
    "curriculum/4-probabilistic-ml.md": seg(1122, 1202),
    "curriculum/5-deep-learning.md": seg(1204, 1356),
    "curriculum/6-frontier-production.md": seg(1358, 1769),
    "resources/books.md": seg(1771, 1865),
    "resources/toolchain.md": seg(1867, 1915),
    "guides/career-operations.md": seg(1917, 2083),
    "guides/progress-tracker.md": seg(2085, 2158),
    "CHANGELOG.md": seg(2160, 2206),
}

MODULE_PROJECTS_RULE = seg(266, 284)  # goes into curriculum/README.md

# ------------------------------------------------------------- anchor map
# Explicit <a id> anchors -> the file that now owns them.
ANCHOR_OWNER = {
    # hub README keeps these (explicit anchor or heading-derived)
    "start-here": "README.md",
    "choose-your-track": "README.md",
    "roadmap": "README.md",
    "curriculum-at-a-glance": "README.md",
    "who-this-is-for": "README.md",
    "how-to-use-this-roadmap": "README.md",
    "goal": "README.md",
    "acknowledgements": "README.md",
    # moved sections
    "practitioner-track": "guides/practitioner-track.md",
    "companion-curricula": "guides/companion-curricula.md",
    "module-projects": "curriculum/README.md",
    "math-diagnostic": "curriculum/1-foundations.md",
    "python-course-matrix": "curriculum/1-foundations.md",
    "career-operations": "guides/career-operations.md",
    "skills-checklist": "guides/career-operations.md",
    "progress-tracker": "guides/progress-tracker.md",
    "refresh-log": "CHANGELOG.md",
    "books": "resources/books.md",
    "practitioner-shelf": "resources/books.md",
    "toolchain": "resources/toolchain.md",
    "production-bar": "curriculum/6-frontier-production.md",
}
_MODULE_FILES = {
    "curriculum/1-foundations.md": ["module-0", "module-1", "module-2",
                                    "module-3", "module-4", "module-5"],
    "curriculum/2-statistics-and-data.md": ["module-6", "module-6-half",
                                            "module-7", "module-8a",
                                            "module-8b"],
    "curriculum/3-classical-ml.md": ["module-9", "module-10", "module-11",
                                     "module-12"],
    "curriculum/4-probabilistic-ml.md": ["module-13", "module-14"],
    "curriculum/5-deep-learning.md": ["module-15", "module-16", "module-17"],
    "curriculum/6-frontier-production.md": ["module-18", "module-21",
                                            "module-22", "module-23",
                                            "module-24", "module-25",
                                            "module-26"],
}
for fpath, anchors in _MODULE_FILES.items():
    for a in anchors:
        ANCHOR_OWNER[a] = fpath

LINK_RE = re.compile(r"\]\(#([A-Za-z0-9._-]+)\)")


def rel(from_file, to_file):
    r = os.path.relpath(to_file, os.path.dirname(from_file) or ".")
    return r.replace(os.sep, "/")


def rewrite_links(text, current_file):
    unknown = []

    def sub(m):
        anchor = m.group(1)
        owner = ANCHOR_OWNER.get(anchor)
        if owner is None:
            unknown.append(anchor)
            return m.group(0)
        if owner == current_file:
            return m.group(0)
        return "](%s#%s)" % (rel(current_file, owner), anchor)

    out = LINK_RE.sub(sub, text)
    if unknown:
        print("WARN %s: unmapped anchors: %s" % (current_file, sorted(set(unknown))))
    return out


def fix_relative_paths(text, current_file):
    """Files moved into a subdirectory need ../ on repo-root-relative paths."""
    if "/" not in current_file:
        return text
    text = text.replace('src="assets/', 'src="../assets/')
    text = text.replace("](assets/", "](../assets/")
    text = text.replace("](audit/", "](../audit/")
    text = text.replace("](LICENSE.md)", "](../LICENSE.md)")
    return text


# ------------------------------------------------------- navigation extras
CURRICULUM_ORDER = [
    ("curriculum/1-foundations.md", "🟩 Foundations (M0–M5)"),
    ("curriculum/2-statistics-and-data.md", "🟨 Statistics & Data (M6–M8b)"),
    ("curriculum/3-classical-ml.md", "🟧 Classical ML (M9–M12)"),
    ("curriculum/4-probabilistic-ml.md", "🟦 Probabilistic ML (M13–M14)"),
    ("curriculum/5-deep-learning.md", "🟪 Deep Learning (M15–M17)"),
    ("curriculum/6-frontier-production.md", "🔴 Frontier & Production (M18, M21–M26)"),
]


def breadcrumb(current_file):
    parts = ["[🏠 Roadmap home](%s)" % rel(current_file, "README.md")]
    idx = [i for i, (f, _) in enumerate(CURRICULUM_ORDER) if f == current_file]
    if idx:
        i = idx[0]
        parts.append("[📚 Curriculum index](%s)" % rel(current_file, "curriculum/README.md"))
        if i > 0:
            pf, pt = CURRICULUM_ORDER[i - 1]
            parts.append("[← %s](%s)" % (pt, rel(current_file, pf)))
        if i < len(CURRICULUM_ORDER) - 1:
            nf, nt = CURRICULUM_ORDER[i + 1]
            parts.append("[%s →](%s)" % (nt, rel(current_file, nf)))
    return " · ".join(parts)


def main():
    written = []
    for fpath, body in SEGMENTS.items():
        body = rewrite_links(body, fpath)
        body = fix_relative_paths(body, fpath)
        nav = breadcrumb(fpath)
        content = nav + "\n\n---\n\n" + body + "\n\n---\n\n" + nav + "\n"
        full = os.path.join(ROOT, fpath)
        os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(content)
        written.append((fpath, content.count("\n") + 1))

    # curriculum/README.md — index + verbatim enforcement rule
    rule = rewrite_links(MODULE_PROJECTS_RULE, "curriculum/README.md")
    rule = fix_relative_paths(rule, "curriculum/README.md")
    with open(os.path.join(ROOT, "curriculum/_index_rule.part"), "w", encoding="utf-8") as f:
        f.write(rule)
    print("Wrote curriculum/_index_rule.part (%d lines) for manual index assembly"
          % (rule.count("\n") + 1))

    for fpath, n in written:
        print("Wrote %-42s %5d lines" % (fpath, n))


if __name__ == "__main__":
    main()
