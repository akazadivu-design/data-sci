# Assets — provenance and licence

Every image in this directory is **original to this repository**. There is no stock photography, no
commercially-licensed imagery (Getty / Shutterstock / Alamy / iStock / Adobe Stock), and nothing
scraped from a third-party page. This is deliberate: the roadmap makes factual claims that are
verified before publication, and the artwork is held to the same standard — if we cannot state where
an asset came from, it does not ship.

| File | How it was produced | Notes |
| :--- | :--- | :--- |
| `hero-banner.jpg` | AI-generated original (Gemini "Nano Banana Pro"), prompt written for this repository | 1600 × 893, JPEG q90. Text content proof-read after generation. |
| `roadmap-overview.jpg` | AI-generated original (same model and session) | 1600 × 893. The six stations mirror the six curriculum strata and their module ranges. |
| `stratum-1-foundations.jpg` | Rendered by [`make_banners.py`](make_banners.py) | 1600 × 400 |
| `stratum-2-statistics.jpg` | Rendered by [`make_banners.py`](make_banners.py) | 1600 × 400 |
| `stratum-3-classical-ml.jpg` | Rendered by [`make_banners.py`](make_banners.py) | 1600 × 400 |
| `stratum-4-bayesian.jpg` | Rendered by [`make_banners.py`](make_banners.py) | 1600 × 400 |
| `stratum-5-deep-learning.jpg` | Rendered by [`make_banners.py`](make_banners.py) | 1600 × 400 |
| `stratum-6-production.jpg` | Rendered by [`make_banners.py`](make_banners.py) | 1600 × 400 |

## Regenerating the section banners

```bash
python3 -m pip install pillow      # the only dependency
python3 assets/make_banners.py     # run from the repository root
```

The script is deterministic — the same input produces byte-comparable output — so the banners can be
regenerated in CI or restyled wholesale by editing one table.

**Why the banners are drawn in code rather than generated.** Two reasons, both practical:

1. **Text is guaranteed correct.** Image models misspell. Every banner carries a title and a module
   range, and a curriculum that audits its own URLs cannot ship a header reading "MODUELS 9-12".
2. **They are editable.** When a module is renumbered or a stratum is renamed, the fix is a one-line
   edit and a re-run, not a new generation with a new visual style to reconcile.

## Style contract

Anything added here should match the existing visual language:

| Element | Value |
| :--- | :--- |
| Background | vertical gradient `#0a0e1f` → `#111a38`, dotted grid at 40 px |
| Foundations accent | `#34d399` (emerald) |
| Statistics accent | `#facc15` (amber) |
| Classical ML accent | `#fb923c` (orange) |
| Bayesian accent | `#38a0ff` (blue) |
| Deep Learning accent | `#a78bfa` (violet) |
| Production accent | `#f87171` (red) |
| Title face | Liberation Sans Bold, white, uppercase |
| Caption face | DejaVu Sans Mono Bold, accent colour, letter-spaced |
| Iconography | thin-line, uniform stroke, soft neon glow (two blurred passes under one crisp pass) |

The accent colours match the coloured-square emoji already used on the stratum headings in the root
`README.md` (🟩 🟨 🟧 🟦 🟪 🔴), so the text and the artwork agree.

## Accessibility

Every embed in `README.md` uses a descriptive `alt` attribute and `width="100%"`. The banners are
decorative reinforcement — **no information appears only in an image.** Every stratum heading, module
range, and navigation link is present as text, so the roadmap is fully usable with images disabled,
in a screen reader, or in a plain-text renderer.
