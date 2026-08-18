# Repository tooling

| Script | Status | Purpose |
| :--- | :--- | :--- |
| [`check_links.py`](check_links.py) | **Active** | Validates every internal markdown link and `#anchor` in the repo (GitHub slug rules + explicit `<a id>` tags). Run locally with `python3 tools/check_links.py`. |
| [`check-links.workflow.yml`](check-links.workflow.yml) | **Ready to install** | GitHub Actions workflow that runs `check_links.py` on every push/PR touching markdown. The automation token used to open this PR cannot write to `.github/workflows/`, so to enable it, move this file to `.github/workflows/check-links.yml` in a commit made from your own account (one click in the GitHub web editor). |
| [`split_readme.py`](split_readme.py) | Historical (v2026.4 migration) | Split the former monolithic 2,236-line `README.md` into `curriculum/`, `guides/`, `resources/`, and `CHANGELOG.md` by verbatim line ranges, rewriting only link paths. Kept for auditability of the move; it expects the pre-split README and is not meant to be re-run. |
| [`build_hub.py`](build_hub.py) | Historical (v2026.4 migration) | Assembled the current hub `README.md` from verbatim segments of the pre-split README (which it read from a `README.md.orig` snapshot) plus the new navigation tables. Kept for auditability; not meant to be re-run. |

**Verbatim-move guarantee.** During the v2026.4 restructure, each moved section was
diff-verified against its original line range after mechanically un-doing the link-path
rewrites — 13/13 sections matched byte-for-byte. No curriculum prose was altered.
