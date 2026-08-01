#!/usr/bin/env python3
"""
Generate the OBITO roadmap section banners.

Deterministic, dependency-light (Pillow only), and licence-clean: every pixel is
drawn here, so there is no third-party image licensing to reason about and the
typography cannot be misspelled the way a generative model can misspell it.

Style is matched to assets/hero-banner.jpg: midnight-navy gradient, faint dotted
grid, a coloured accent bar, white title, accent-coloured module caption, and a
row of thin-line glyphs with a soft neon glow.

Run:  python3 assets/make_banners.py   (from the repository root)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1600, 400
BG_TOP = (10, 14, 31)
BG_BOT = (17, 26, 56)
GRID = (27, 37, 71)
WHITE = (255, 255, 255)
SUB = (150, 163, 196)
RULE = (30, 42, 77)

F_TITLE = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

OUT = "assets"

# --------------------------------------------------------------------------- #
# canvas helpers
# --------------------------------------------------------------------------- #


def background():
    """Vertical gradient + dotted grid + soft corner vignette."""
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / (H - 1)
        d.line(
            [(0, y), (W, y)],
            fill=tuple(round(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)),
        )
    for x in range(0, W, 40):
        for y in range(0, H, 40):
            d.point((x, y), fill=GRID)
    return im


def text_tracked(d, xy, s, font, fill, tracking=0):
    """Draw text with manual letter-spacing; returns the advance width."""
    x, y = xy
    for ch in s:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking
    return x - xy[0]


# --------------------------------------------------------------------------- #
# glyphs -- each takes (d, cx, cy, s, col, w) and draws a thin-line icon
# s is the half-extent in px; w is the stroke width
# --------------------------------------------------------------------------- #


def _poly(d, pts, col, w):
    d.line(pts, fill=col, width=w, joint="curve")


def g_integral(d, cx, cy, s, col, w):
    """Render the real U+222B glyph -- a hand-built path reads as a chevron."""
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(s * 2.6))
    d.text((cx, cy), "\u222b", font=f, fill=col if len(col) == 4 else col + (255,), anchor="mm")


def g_matrix(d, cx, cy, s, col, w):
    b = int(s * 0.55)
    for sx in (-1, 1):
        x = cx + sx * s * 0.85
        _poly(d, [(x - sx * b, cy - s), (x, cy - s), (x, cy + s), (x - sx * b, cy + s)], col, w)
    r = max(2, w)
    for gx in (-0.34, 0.34):
        for gy in (-0.42, 0.0, 0.42):
            px, py = cx + gx * s, cy + gy * s
            d.ellipse([px - r, py - r, px + r, py + r], fill=col)


def g_qed(d, cx, cy, s, col, w):
    k = s * 0.62
    d.rectangle([cx - k, cy - k, cx + k, cy + k], outline=col, width=w)
    d.rectangle([cx - k * 0.42, cy - k * 0.42, cx + k * 0.42, cy + k * 0.42], fill=col)


def g_snake(d, cx, cy, s, col, w):
    pts = []
    for i in range(61):
        t = i / 60
        pts.append((cx - s + 2 * s * t, cy + s * 0.72 * math.sin(2.4 * math.pi * t)))
    _poly(d, pts, col, w)
    d.ellipse([cx + s - w * 2, cy - w * 2, cx + s + w * 2, cy + w * 2], fill=col)


def g_dice(d, cx, cy, s, col, w):
    k = s * 0.78
    d.rounded_rectangle([cx - k, cy - k, cx + k, cy + k], radius=int(s * 0.22), outline=col, width=w)
    r = max(2, int(w * 1.2))
    for gx, gy in ((-0.42, -0.42), (0, 0), (0.42, 0.42), (0.42, -0.42), (-0.42, 0.42)):
        px, py = cx + gx * k, cy + gy * k
        d.ellipse([px - r, py - r, px + r, py + r], fill=col)


def g_axes(d, cx, cy, s, col, w):
    o = (cx - s * 0.45, cy + s * 0.62)
    for dx, dy in ((0, -1.5 * s), (1.5 * s, 0), (-0.8 * s, 0.72 * s)):
        _poly(d, [o, (o[0] + dx, o[1] + dy)], col, w)


def g_bell(d, cx, cy, s, col, w):
    base = cy + s * 0.7
    pts = []
    for i in range(61):
        x = -1 + 2 * i / 60
        pts.append((cx + x * s, base - 1.5 * s * math.exp(-(x * x) / (2 * 0.32 ** 2))))
    _poly(d, pts, col, w)
    _poly(d, [(cx - s, base), (cx + s, base)], col, w)
    for sx in (-1, 1):
        seg = [p for p in pts if (p[0] - cx) * sx > s * 0.55]
        if len(seg) > 1:
            d.polygon(seg + [(seg[-1][0], base), (seg[0][0], base)], fill=col)


def g_errorbar(d, cx, cy, s, col, w):
    _poly(d, [(cx, cy - s * 0.9), (cx, cy + s * 0.9)], col, w)
    for sy in (-1, 1):
        _poly(d, [(cx - s * 0.45, cy + sy * s * 0.9), (cx + s * 0.45, cy + sy * s * 0.9)], col, w)
    r = s * 0.26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)


def g_abtest(d, cx, cy, s, col, w):
    for sx in (-1, 1):
        x0 = cx + (0.08 if sx > 0 else -0.98) * s
        d.rounded_rectangle([x0, cy - s * 0.8, x0 + s * 0.9, cy + s * 0.8],
                            radius=int(s * 0.16), outline=col, width=w)
    h = s * 0.5
    d.rectangle([cx - 0.72 * s, cy + s * 0.8 - h, cx - 0.34 * s, cy + s * 0.8], fill=col)
    d.rectangle([cx + 0.34 * s, cy + s * 0.8 - h * 1.7, cx + 0.72 * s, cy + s * 0.8], fill=col)


def g_dag(d, cx, cy, s, col, w):
    nodes = [(cx - s * 0.8, cy - s * 0.5), (cx + s * 0.8, cy - s * 0.5), (cx, cy + s * 0.7)]
    for a, b in ((0, 2), (1, 2), (0, 1)):
        _poly(d, [nodes[a], nodes[b]], col, w)
    r = s * 0.24
    for nx, ny in nodes:
        d.ellipse([nx - r, ny - r, nx + r, ny + r], fill=BG_BOT, outline=col, width=w)


def g_database(d, cx, cy, s, col, w):
    rx, ry = s * 0.75, s * 0.26
    top, bot = cy - s * 0.72, cy + s * 0.5
    d.ellipse([cx - rx, top - ry, cx + rx, top + ry], outline=col, width=w)
    for sx in (-1, 1):
        _poly(d, [(cx + sx * rx, top), (cx + sx * rx, bot)], col, w)
    d.arc([cx - rx, bot - ry, cx + rx, bot + ry], 0, 180, fill=col, width=w)
    d.arc([cx - rx, cy - s * 0.16 - ry, cx + rx, cy - s * 0.16 + ry], 0, 180, fill=col, width=w)


def g_table(d, cx, cy, s, col, w):
    k = s * 0.8
    d.rectangle([cx - k, cy - k * 0.85, cx + k, cy + k * 0.85], outline=col, width=w)
    for i in (1, 2):
        y = cy - k * 0.85 + i * (1.7 * k / 3)
        _poly(d, [(cx - k, y), (cx + k, y)], col, w)
    _poly(d, [(cx, cy - k * 0.85), (cx, cy + k * 0.85)], col, w)
    d.rectangle([cx - k, cy - k * 0.85, cx + k, cy - k * 0.85 + 1.7 * k / 3], fill=col)


def g_pipeline(d, cx, cy, s, col, w):
    _poly(d, [(cx - s, cy - s * 0.32), (cx + s, cy - s * 0.32)], col, w)
    _poly(d, [(cx - s, cy + s * 0.32), (cx + s, cy + s * 0.32)], col, w)
    r = max(2, int(w * 1.1))
    for t in (-0.62, -0.1, 0.42, 0.86):
        px = cx + t * s
        d.ellipse([px - r, cy - r, px + r, cy + r], fill=col)


def g_scatter_line(d, cx, cy, s, col, w):
    _poly(d, [(cx - s * 0.9, cy + s * 0.62), (cx + s * 0.9, cy - s * 0.66)], col, w)
    r = max(2, int(w * 1.1))
    for t, o in ((-0.72, 0.3), (-0.36, -0.22), (0.0, 0.26), (0.34, -0.3), (0.7, 0.22)):
        px = cx + t * s
        py = cy + s * 0.62 + (-1.28 * s) * ((t + 0.9) / 1.8) + o * s * 0.5
        d.ellipse([px - r, py - r, px + r, py + r], fill=col)


def g_margin(d, cx, cy, s, col, w):
    _poly(d, [(cx - s * 0.75, cy + s * 0.9), (cx + s * 0.75, cy - s * 0.9)], col, w)
    for off in (-0.32, 0.32):
        pts = [(cx - s * 0.75 + off * s, cy + s * 0.9 + off * s * 0.6),
               (cx + s * 0.75 + off * s, cy - s * 0.9 + off * s * 0.6)]
        for i in range(0, 10, 2):
            a = i / 10
            b = (i + 1) / 10
            _poly(d, [(pts[0][0] + (pts[1][0] - pts[0][0]) * a, pts[0][1] + (pts[1][1] - pts[0][1]) * a),
                      (pts[0][0] + (pts[1][0] - pts[0][0]) * b, pts[0][1] + (pts[1][1] - pts[0][1]) * b)],
                  col, max(1, w - 1))
    r = max(2, int(w * 1.1))
    for px, py in ((-0.72, -0.3), (-0.5, -0.66), (-0.86, -0.62)):
        d.ellipse([cx + px * s - r, cy + py * s - r, cx + px * s + r, cy + py * s + r], fill=col)
    for px, py in ((0.72, 0.34), (0.5, 0.68), (0.86, 0.62)):
        d.ellipse([cx + px * s - r, cy + py * s - r, cx + px * s + r, cy + py * s + r],
                  outline=col, width=max(1, w - 1))


def g_clusters(d, cx, cy, s, col, w):
    r = max(2, int(w * 1.0))
    for ox, oy in ((-0.6, -0.42), (0.58, -0.5), (0.0, 0.6)):
        bx, by = cx + ox * s, cy + oy * s
        for ang in (0, 72, 144, 216, 288):
            px = bx + math.cos(math.radians(ang)) * s * 0.26
            py = by + math.sin(math.radians(ang)) * s * 0.26
            d.ellipse([px - r, py - r, px + r, py + r], fill=col)
        k = s * 0.16
        _poly(d, [(bx - k, by), (bx + k, by)], col, w)
        _poly(d, [(bx, by - k), (bx, by + k)], col, w)


def g_tree(d, cx, cy, s, col, w):
    root = (cx, cy - s * 0.85)
    mid = [(cx - s * 0.62, cy), (cx + s * 0.62, cy)]
    leaf = [(cx - s * 0.92, cy + s * 0.85), (cx - s * 0.3, cy + s * 0.85),
            (cx + s * 0.3, cy + s * 0.85), (cx + s * 0.92, cy + s * 0.85)]
    for m in mid:
        _poly(d, [root, m], col, w)
    for i, m in enumerate(mid):
        for lf in leaf[2 * i:2 * i + 2]:
            _poly(d, [m, lf], col, w)
    r = s * 0.2
    d.ellipse([root[0] - r, root[1] - r, root[0] + r, root[1] + r], fill=col)
    for m in mid:
        d.ellipse([m[0] - r, m[1] - r, m[0] + r, m[1] + r], fill=BG_BOT, outline=col, width=w)
    for lf in leaf:
        d.rectangle([lf[0] - r * 0.8, lf[1] - r * 0.8, lf[0] + r * 0.8, lf[1] + r * 0.8], fill=col)


def g_forest(d, cx, cy, s, col, w):
    for i, ox in enumerate((-0.66, 0.0, 0.66)):
        bx = cx + ox * s
        h = s * (0.9 if i == 1 else 0.72)
        d.polygon([(bx, cy - h), (bx - s * 0.3, cy + s * 0.42), (bx + s * 0.3, cy + s * 0.42)],
                  outline=col, width=w)
        _poly(d, [(bx, cy + s * 0.42), (bx, cy + s * 0.78)], col, w)


def g_confusion(d, cx, cy, s, col, w):
    k = s * 0.72
    d.rectangle([cx - k, cy - k, cx + k, cy + k], outline=col, width=w)
    _poly(d, [(cx, cy - k), (cx, cy + k)], col, w)
    _poly(d, [(cx - k, cy), (cx + k, cy)], col, w)
    d.rectangle([cx - k, cy - k, cx, cy], fill=col)
    d.rectangle([cx, cy, cx + k, cy + k], fill=col)


def g_roc(d, cx, cy, s, col, w):
    k = s * 0.82
    _poly(d, [(cx - k, cy - k), (cx - k, cy + k), (cx + k, cy + k)], col, w)
    for i in range(0, 8, 2):
        a, b = i / 8, (i + 1) / 8
        _poly(d, [(cx - k + 2 * k * a, cy + k - 2 * k * a), (cx - k + 2 * k * b, cy + k - 2 * k * b)],
              col, max(1, w - 1))
    pts = [(cx - k + 2 * k * (i / 30), cy + k - 2 * k * ((i / 30) ** 0.42)) for i in range(31)]
    _poly(d, pts, col, w)


def g_dists(d, cx, cy, s, col, w):
    base = cy + s * 0.72
    for off, sg, fill in ((-0.34, 0.3, False), (0.3, 0.22, True)):
        pts = []
        for i in range(61):
            x = -1.1 + 2.2 * i / 60
            pts.append((cx + x * s, base - 1.45 * s * math.exp(-((x - off) ** 2) / (2 * sg ** 2))))
        if fill:
            d.polygon(pts + [(pts[-1][0], base), (pts[0][0], base)], outline=col)
        _poly(d, pts, col, w if not fill else max(1, w - 1))
    _poly(d, [(cx - s * 1.1, base), (cx + s * 1.1, base)], col, w)


def g_trace(d, cx, cy, s, col, w):
    """A burn-in-then-stationary MCMC trace: legible at 44px, unlike dense noise."""
    pts = []
    seed = 11
    n = 30
    for i in range(n + 1):
        seed = (seed * 1103515245 + 12345) % 2147483648
        t = i / n
        amp = 0.9 * math.exp(-3.2 * t) + 0.3
        pts.append((cx - s + 2 * s * t,
                    cy - s * 0.55 * amp * (2 * ((seed >> 16) % 100) / 100 - 1)))
    _poly(d, pts, col, max(1, w - 1))
    _poly(d, [(cx - s, cy), (cx + s, cy)], col, 1)


def g_timeseries(d, cx, cy, s, col, w):
    pts = [(cx - s + 1.2 * s * i / 24, cy + s * 0.5 * math.sin(i * 0.55) - s * 0.1 * (i / 24))
           for i in range(25)]
    _poly(d, pts, col, w)
    tip = pts[-1]
    fan = [tip, (cx + s, cy - s * 0.85), (cx + s, cy + s * 0.5)]
    d.polygon(fan, outline=col)
    _poly(d, [tip, (cx + s, cy - s * 0.2)], col, max(1, w - 1))


def g_nn(d, cx, cy, s, col, w):
    layers = [3, 4, 3, 2]
    xs = [cx - s + 2 * s * i / (len(layers) - 1) for i in range(len(layers))]
    pos = []
    for li, n in enumerate(layers):
        col_pts = [(xs[li], cy + (j - (n - 1) / 2) * (1.7 * s / max(n, 3))) for j in range(n)]
        pos.append(col_pts)
    for a, b in zip(pos, pos[1:]):
        for p in a:
            for q in b:
                _poly(d, [p, q], col, 1)
    r = s * 0.14
    for layer in pos:
        for p in layer:
            d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=col)


def g_attention(d, cx, cy, s, col, w):
    n = 5
    k = s * 0.86
    cell = 2 * k / n
    vals = [(i * 7 + j * 3) % 5 for i in range(n) for j in range(n)]
    for i in range(n):
        for j in range(n):
            v = vals[i * n + j]
            x0, y0 = cx - k + j * cell, cy - k + i * cell
            if j <= i:
                d.rectangle([x0 + 1, y0 + 1, x0 + cell - 2, y0 + cell - 2], fill=col)
            elif v > 3:
                d.rectangle([x0 + 1, y0 + 1, x0 + cell - 2, y0 + cell - 2], outline=col, width=1)
    d.rectangle([cx - k, cy - k, cx + k, cy + k], outline=col, width=w)


def g_chip(d, cx, cy, s, col, w):
    k = s * 0.62
    d.rounded_rectangle([cx - k, cy - k, cx + k, cy + k], radius=int(s * 0.1), outline=col, width=w)
    d.rounded_rectangle([cx - k * 0.44, cy - k * 0.44, cx + k * 0.44, cy + k * 0.44],
                        radius=int(s * 0.06), fill=col)
    for i in range(-1, 2):
        o = i * k * 0.55
        _poly(d, [(cx + o, cy - k), (cx + o, cy - k - s * 0.3)], col, w)
        _poly(d, [(cx + o, cy + k), (cx + o, cy + k + s * 0.3)], col, w)
        _poly(d, [(cx - k, cy + o), (cx - k - s * 0.3, cy + o)], col, w)
        _poly(d, [(cx + k, cy + o), (cx + k + s * 0.3, cy + o)], col, w)


def g_rl_loop(d, cx, cy, s, col, w):
    """Agent box above, environment box below, one arrow each way down the sides."""
    bw, bh = s * 0.56, s * 0.26
    for sy in (-1, 1):
        d.rounded_rectangle([cx - bw, cy + sy * s * 0.66 - bh, cx + bw, cy + sy * s * 0.66 + bh],
                            radius=int(s * 0.09), outline=col, width=w)
    d.ellipse([cx - s * 0.16, cy - s * 0.82, cx + s * 0.16, cy - s * 0.5], fill=col)
    for sx in (-1, 1):
        x = cx + sx * s * 0.9
        _poly(d, [(cx + sx * bw, cy - sx * s * 0.66), (x, cy - sx * s * 0.66),
                  (x, cy + sx * s * 0.66), (cx + sx * bw * 0.55, cy + sx * s * 0.66)], col, w)
        tipx = cx + sx * bw * 0.55
        tipy = cy + sx * s * 0.66
        d.polygon([(tipx, tipy), (tipx + sx * s * 0.2, tipy - s * 0.13),
                   (tipx + sx * s * 0.2, tipy + s * 0.13)], fill=col)


def g_tokens(d, cx, cy, s, col, w):
    widths = [0.34, 0.5, 0.28, 0.44]
    x = cx - s
    for i, ww in enumerate(widths):
        wpx = ww * s
        d.rounded_rectangle([x, cy - s * 0.26, x + wpx, cy + s * 0.26],
                            radius=int(s * 0.12), outline=col, width=w,
                            fill=col if i == 1 else None)
        x += wpx + s * 0.14
    r = max(2, int(w * 1.0))
    for t in (-0.5, 0.0, 0.5):
        d.ellipse([cx + t * s - r, cy + s * 0.66 - r, cx + t * s + r, cy + s * 0.66 + r], fill=col)


def g_vector_cube(d, cx, cy, s, col, w):
    k = s * 0.6
    o = s * 0.32
    front = [(cx - k, cy - k + o), (cx + k - o, cy - k + o), (cx + k - o, cy + k), (cx - k, cy + k)]
    back = [(p[0] + o, p[1] - o) for p in front]
    d.polygon(front, outline=col)
    d.polygon(back, outline=col)
    for a, b in zip(front, back):
        _poly(d, [a, b], col, max(1, w - 1))
    r = max(2, int(w * 1.0))
    for px, py in ((-0.3, -0.05), (0.05, 0.2), (0.22, -0.28)):
        d.ellipse([cx + px * s - r, cy + py * s - r, cx + px * s + r, cy + py * s + r], fill=col)


def g_agents(d, cx, cy, s, col, w):
    r0 = s * 0.28
    d.ellipse([cx - r0, cy - r0, cx + r0, cy + r0], outline=col, width=w)
    d.ellipse([cx - r0 * 0.4, cy - r0 * 0.4, cx + r0 * 0.4, cy + r0 * 0.4], fill=col)
    r = s * 0.17
    for ang in (30, 150, 270):
        px = cx + math.cos(math.radians(ang)) * s * 0.78
        py = cy + math.sin(math.radians(ang)) * s * 0.78
        _poly(d, [(cx, cy), (px, py)], col, max(1, w - 1))
        d.rounded_rectangle([px - r, py - r, px + r, py + r], radius=int(r * 0.4),
                            fill=BG_BOT, outline=col, width=w)


def g_shield(d, cx, cy, s, col, w):
    k = s * 0.72
    pts = [(cx, cy - k), (cx + k * 0.86, cy - k * 0.6), (cx + k * 0.72, cy + k * 0.36),
           (cx, cy + k), (cx - k * 0.72, cy + k * 0.36), (cx - k * 0.86, cy - k * 0.6)]
    d.polygon(pts, outline=col)
    for i in range(len(pts)):
        _poly(d, [pts[i], pts[(i + 1) % len(pts)]], col, w)
    _poly(d, [(cx - k * 0.34, cy), (cx - k * 0.06, cy + k * 0.3), (cx + k * 0.4, cy - k * 0.28)],
          col, w + 1)


def g_cicd(d, cx, cy, s, col, w):
    k = s * 0.66
    d.arc([cx - k, cy - k, cx + k, cy + k], 40, 320, fill=col, width=w)
    d.polygon([(cx + k * 0.78, cy - k * 0.72), (cx + k * 1.02, cy - k * 0.1),
               (cx + k * 0.4, cy - k * 0.2)], fill=col)
    r = s * 0.14
    for ang in (90, 210, 330):
        px = cx + math.cos(math.radians(ang)) * k
        py = cy + math.sin(math.radians(ang)) * k
        d.ellipse([px - r, py - r, px + r, py + r], fill=col)


def g_cloud_rocket(d, cx, cy, s, col, w):
    """Cloud outline with an upward deploy arrow (the rocket version read as a blob)."""
    base = cy + s * 0.5
    d.arc([cx - s * 0.9, base - s * 0.62, cx - s * 0.22, base + s * 0.06], 150, 350, fill=col, width=w)
    d.arc([cx - s * 0.48, base - s * 0.92, cx + s * 0.42, base + s * 0.02], 175, 365, fill=col, width=w)
    d.arc([cx + s * 0.16, base - s * 0.66, cx + s * 0.9, base + s * 0.06], 190, 30, fill=col, width=w)
    _poly(d, [(cx - s * 0.84, base), (cx + s * 0.84, base)], col, w)
    _poly(d, [(cx, base - s * 0.1), (cx, base - s * 0.62)], col, w + 1)
    d.polygon([(cx, base - s * 0.86), (cx + s * 0.2, base - s * 0.52),
               (cx - s * 0.2, base - s * 0.52)], fill=col)


def g_chain(d, cx, cy, s, col, w):
    """Hidden Markov / state chain: latent row above, observed row below."""
    xs = [cx - s * 0.72, cx, cx + s * 0.72]
    r = s * 0.2
    for i, x in enumerate(xs):
        d.ellipse([x - r, cy - s * 0.5 - r, x + r, cy - s * 0.5 + r],
                  fill=BG_BOT, outline=col, width=w)
        d.rectangle([x - r * 0.85, cy + s * 0.5 - r * 0.85, x + r * 0.85, cy + s * 0.5 + r * 0.85],
                    fill=col)
        _poly(d, [(x, cy - s * 0.5 + r), (x, cy + s * 0.5 - r * 0.9)], col, max(1, w - 1))
        if i < 2:
            _poly(d, [(x + r, cy - s * 0.5), (xs[i + 1] - r, cy - s * 0.5)], col, w)


def g_descent(d, cx, cy, s, col, w):
    """Loss bowl with a descending optimisation path."""
    pts = [(cx - s + 2 * s * (i / 40),
            cy + s * 0.62 - 1.5 * s * ((i / 40 - 0.5) ** 2) * 2.6) for i in range(41)]
    _poly(d, pts, col, w)
    r = max(2, int(w * 1.1))
    for t in (0.06, 0.2, 0.34, 0.46):
        x = cx - s + 2 * s * t
        y = cy + s * 0.62 - 1.5 * s * ((t - 0.5) ** 2) * 2.6
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)


def g_conv(d, cx, cy, s, col, w):
    """Convolution: a kernel window over a feature grid."""
    n = 4
    k = s * 0.82
    cell = 2 * k / n
    for i in range(n + 1):
        _poly(d, [(cx - k, cy - k + i * cell), (cx + k, cy - k + i * cell)], col, 1)
        _poly(d, [(cx - k + i * cell, cy - k), (cx - k + i * cell, cy + k)], col, 1)
    d.rectangle([cx - k, cy - k, cx - k + 2 * cell, cy - k + 2 * cell], outline=col, width=w + 1)
    d.rectangle([cx + k - cell * 1.0, cy + k - cell * 1.0, cx + k, cy + k], fill=col)


# --------------------------------------------------------------------------- #
# banner assembly
# --------------------------------------------------------------------------- #


def banner(path, title, caption, accent, glyphs, title_size=64):
    im = background()
    accent_rgb = accent

    # glow layer (blurred) + crisp layer, both RGBA
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    crisp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dg, dc = ImageDraw.Draw(glow), ImageDraw.Draw(crisp)

    f_title = ImageFont.truetype(F_TITLE, title_size)
    f_cap = ImageFont.truetype(F_MONO, 24)

    # left accent bar
    bar_x, bar_top, bar_bot = 74, 128, 272
    for dd, wdt in ((dg, 14), (dc, 7)):
        dd.rounded_rectangle([bar_x - wdt // 2, bar_top, bar_x + wdt // 2, bar_bot],
                            radius=wdt // 2, fill=accent_rgb + (255,))

    tx = bar_x + 34
    dc.text((tx, bar_top - 6), title, font=f_title, fill=WHITE + (255,))
    text_tracked(dc, (tx + 3, bar_top + title_size + 16), caption, f_cap,
                 accent_rgb + (255,), tracking=3.2)
    text_tracked(dg, (tx + 3, bar_top + title_size + 16), caption, f_cap,
                 accent_rgb + (140,), tracking=3.2)

    # divider between text block and glyph row
    title_w = dc.textlength(title, font=f_title)
    div_x = max(tx + title_w + 70, 640)
    dc.line([(div_x, 118), (div_x, 282)], fill=RULE + (255,), width=2)

    # glyph row
    n = len(glyphs)
    x0, x1 = div_x + 74, W - 82
    step = (x1 - x0) / max(n - 1, 1)
    cy = 200
    s = min(44, step * 0.42)
    for i, g in enumerate(glyphs):
        cx = x0 + i * step
        g(dg, cx, cy, s, accent_rgb, 6)
        g(dc, cx, cy, s, accent_rgb, 3)

    # thin guide line behind the glyph row
    dg.line([(x0 - 40, cy), (x1 + 40, cy)], fill=accent_rgb + (26,), width=2)

    im = im.convert("RGBA")
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(11)))
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(3)))
    im = Image.alpha_composite(im, crisp)
    im.convert("RGB").save(path, quality=92, optimize=True, progressive=True)
    print("wrote", path, os.path.getsize(path) // 1024, "KB")


SPECS = [
    ("stratum-1-foundations.jpg", "FOUNDATIONS", "MODULES 0-5", (52, 211, 153),
     [g_qed, g_snake, g_integral, g_matrix, g_axes, g_dice]),
    ("stratum-2-statistics.jpg", "STATISTICS & DATA", "MODULES 6-8", (250, 204, 21),
     [g_bell, g_errorbar, g_abtest, g_dag, g_database, g_table, g_pipeline]),
    ("stratum-3-classical-ml.jpg", "CLASSICAL ML", "MODULES 9-12", (251, 146, 60),
     [g_scatter_line, g_margin, g_clusters, g_tree, g_forest, g_confusion, g_roc]),
    ("stratum-4-bayesian.jpg", "PROBABILISTIC & BAYESIAN", "MODULES 13-14", (56, 160, 255),
     [g_dists, g_dag, g_trace, g_chain, g_timeseries], 52),
    ("stratum-5-deep-learning.jpg", "DEEP LEARNING", "MODULES 15-17", (167, 139, 250),
     [g_nn, g_conv, g_attention, g_descent, g_chip, g_rl_loop]),
    ("stratum-6-production.jpg", "FRONTIER & PRODUCTION", "MODULES 18, 21-26", (248, 113, 113),
     [g_tokens, g_vector_cube, g_agents, g_shield, g_cicd, g_cloud_rocket], 56),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for spec in SPECS:
        fn, title, cap, accent, glyphs = spec[:5]
        ts = spec[5] if len(spec) > 5 else 64
        banner(os.path.join(OUT, fn), title, cap, accent, glyphs, ts)
