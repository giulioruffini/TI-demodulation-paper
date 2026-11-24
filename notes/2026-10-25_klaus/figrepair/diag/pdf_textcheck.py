#!/usr/bin/env python3
"""Measure text collisions, clipping and printed type size in figure PDFs.

Usage: python3 pdf_textcheck.py PLACED_FRAC file.pdf [file.pdf ...]
PLACED_FRAC is the \\includegraphics width as a fraction of \\textwidth (464.9 pt
for the JNE build). Needs PyMuPDF (import fitz). Boxes are shrunk to the ink
height from the font ascender/descender so that touching descenders do not
count; a collision is reported when the intersection exceeds 15% of the smaller
box. Printed size = span size x placed width / figure width.
"""
import sys, itertools
import fitz

TEXTWIDTH_PT = 464.9
MIN_PT, TOL = 6.0, 0.15


def spans(page):
    """One box per text line (a mathtext label is one line of several spans); the
    size is the line's largest span (the base size, not its sub/superscripts)."""
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            sp = [s for s in l["spans"] if s["text"].strip()]
            if not sp:
                continue
            txt = "".join(s["text"] for s in sp).strip()
            size = max(s["size"] for s in sp)
            x0 = min(s["bbox"][0] for s in sp); x1 = max(s["bbox"][2] for s in sp)
            y0 = min(s["bbox"][1] for s in sp); y1 = max(s["bbox"][3] for s in sp)
            oy = max(s["origin"][1] for s in sp)
            top = oy - size * 0.72          # cap height
            bot = oy + size * 0.12          # shallow descender allowance
            out.append((txt, size, fitz.Rect(x0, top, x1, bot), fitz.Rect(x0, y0, x1, y1)))
    return out


def check(path, placed_frac):
    doc = fitz.open(path)
    page = doc[0]
    pw = page.rect.width
    scale = placed_frac * TEXTWIDTH_PT / pw
    items = spans(page)
    findings = []
    for (t1, s1, r1, _), (t2, s2, r2, _) in itertools.combinations(items, 2):
        inter = r1 & r2
        if inter.is_empty:
            continue
        small = min(r1.get_area(), r2.get_area())
        if small > 0 and inter.get_area() / small > TOL:
            findings.append(f"COLLISION  {t1[:24]!r} x {t2[:24]!r} ({100*inter.get_area()/small:.0f}%)"
                            f" at ({inter.x0:.0f},{inter.y0:.0f})")
    for t, s, _, full in items:
        if not page.rect.contains(full):
            findings.append(f"CLIPPED    {t[:30]!r}")
    sizes = sorted({round(s * scale, 1) for _, s, _, _ in items})
    small = [(t, round(s * scale, 1)) for t, s, _, _ in items if s * scale < MIN_PT]
    print(f"{path.split('/')[-1]}: {pw:.0f} pt wide, placed {placed_frac:g}, scale {scale:.3f};"
          f" printed sizes {sizes[0]}..{sizes[-1]} pt; {len(items)} spans")
    for f in dict.fromkeys(findings):
        print("   ", f)
    if small:
        n = len(small)
        ex = ", ".join(f"{t!r}@{p}" for t, p in small[:6])
        print(f"    TOO SMALL  {n} span(s) below {MIN_PT} pt: {ex}")
    return findings, small


if __name__ == "__main__":
    frac = float(sys.argv[1])
    for p in sys.argv[2:]:
        check(p, frac)
