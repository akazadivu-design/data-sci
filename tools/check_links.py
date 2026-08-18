#!/usr/bin/env python3
"""Validate every internal (relative) markdown link and anchor in the repo.

Checks:
  1. relative file targets exist;
  2. #anchors resolve in the target file, using GitHub's rules:
     explicit <a id="..."> tags OR heading-derived slugs
     (lowercase, strip punctuation/emoji, spaces->hyphens, dedupe with -1, -2).
Exit code 1 on any failure.
"""
import glob
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MD_FILES = [p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
            if "/node_modules/" not in p and not p.endswith("README.md.orig")]

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
AID = re.compile(r'<a id="([^"]+)"></a>')
HEADING = re.compile(r"^(#{1,6})\s+(.*)$", re.M)


def github_slug(text):
    # strip markdown emphasis and links, keep link text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("*", "").replace("`", "")
    out = []
    for ch in text.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in (" ", "-"):
            out.append("-" if ch == "-" else "-")
        elif unicodedata.category(ch).startswith(("L", "N")):
            out.append(ch)
        # else drop (punctuation, emoji, symbols)
    return "".join(out).replace("--", "--")  # github keeps consecutive hyphens


def anchors_of(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    anchors = set(AID.findall(text))
    counts = {}
    # strip fenced code blocks so '#' comments aren't headings
    text_noc = re.sub(r"```.*?```", "", text, flags=re.S)
    for m in HEADING.finditer(text_noc):
        s = github_slug(m.group(2))
        n = counts.get(s, 0)
        counts[s] = n + 1
        anchors.add(s if n == 0 else "%s-%d" % (s, n))
    return anchors

ANCHORS = {p: anchors_of(p) for p in MD_FILES}

fails = 0
checked = 0
for p in MD_FILES:
    with open(p, encoding="utf-8") as f:
        text = f.read()
    # also check <img src="...">
    targets = LINK.findall(text) + re.findall(r'src="([^"]+)"', text)
    for t in targets:
        if t.startswith(("http://", "https://", "mailto:")):
            continue
        if "…" in t:  # prose placeholder (e.g. `src="assets/…"` in audit docs)
            continue
        checked += 1
        if t.startswith("#"):
            fpath, anchor = p, t[1:]
        else:
            part = t.split("#", 1)
            rel_file = part[0]
            anchor = part[1] if len(part) > 1 else None
            fpath = os.path.normpath(os.path.join(os.path.dirname(p), rel_file))
            if not os.path.exists(fpath):
                print("MISSING FILE  %s -> %s" % (os.path.relpath(p, ROOT), t))
                fails += 1
                continue
            if anchor is None or os.path.isdir(fpath):
                continue
            if not fpath.endswith(".md"):
                continue
        if fpath not in ANCHORS:
            ANCHORS[fpath] = anchors_of(fpath)
        if anchor not in ANCHORS[fpath]:
            print("BAD ANCHOR    %s -> %s (in %s)" % (os.path.relpath(p, ROOT), t,
                                                      os.path.relpath(fpath, ROOT)))
            fails += 1

print("\nchecked %d internal links across %d md files; %d failures" %
      (checked, len(MD_FILES), fails))
sys.exit(1 if fails else 0)
