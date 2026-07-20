#!/usr/bin/env python3
"""Check that figure panel letters agree with their captions.

IOP: "If there is more than one part to a figure ... the parts should be
identified by a lower-case letter in parentheses close to or within the area of
the figure", and all parts described in a single caption. So for every figure:

  letters drawn IN the image  ==  letters referenced IN the caption

Reports any figure where the two sets differ, plus captions still using
positional wording ("Left:", "Top right:") instead of letters.

Usage:  python3 code/check_panels.py [figdir]
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEX = os.path.join(ROOT, "TN0484_envelope_demodulation.tex")
FIGDIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "figures")

POSITIONAL = re.compile(r"\\emph\{(Left|Right|Top left|Top right|Bottom left|Bottom right):\}")


def caption_letters(cap):
    r"""Letters the caption refers to, e.g. \emph{(a)} or \emph{(a,b)} or (c,d)."""
    out = set()
    for grp in re.findall(r"\\emph\{\(([a-z][a-z,\s]*)\)\}", cap):
        out |= set(re.findall(r"[a-z]", grp))
    return out


def figure_letters(path):
    """Letters actually drawn in the image, read back from the rendered PDF."""
    if not path.lower().endswith(".pdf") or not os.path.exists(path):
        return None
    try:
        txt = subprocess.run(["pdftotext", path, "-"],
                             capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return None
    out = set()
    for m in re.findall(r"\(([a-d])\)", txt):
        out.add(m)
    # also accept bare "a)" / "b)" styles
    for m in re.findall(r"(?<![A-Za-z])([a-d])\)", txt):
        out.add(m)
    return out


def main():
    src = open(TEX).read()
    problems = 0
    print(f"  figures dir: {FIGDIR}\n")
    print(f"  {'label':22}{'in figure':>12}{'in caption':>13}  verdict")
    for m in re.finditer(r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}", src, re.S):
        blk = m.group(0)
        lab = re.search(r"\\label\{(fig:[^}]+)\}", blk)
        inc = re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", blk)
        cap = re.search(r"\\caption\{(.*)\}\s*\\label", blk, re.S)
        if not (lab and inc and cap):
            continue
        lab, fname, cap = lab.group(1), inc.group(1), cap.group(1)
        figl = figure_letters(os.path.join(FIGDIR, fname))
        capl = caption_letters(cap)
        positional = POSITIONAL.findall(cap)
        if figl is None:
            verdict, bad = "raster/missing - check by eye", False
        elif figl == capl:
            verdict, bad = "ok" if figl else "single panel", False
        else:
            only_fig = "".join(sorted(figl - capl))
            only_cap = "".join(sorted(capl - figl))
            bits = []
            if only_fig:
                bits.append(f"in figure only: {only_fig}")
            if only_cap:
                bits.append(f"in caption only: {only_cap}")
            verdict, bad = "MISMATCH - " + "; ".join(bits), True
        if positional:
            verdict += f"  [caption still positional: {', '.join(positional)}]"
            bad = True
        problems += bad
        f = "".join(sorted(figl)) if figl else "-"
        c = "".join(sorted(capl)) if capl else "-"
        print(f"  {lab:22}{f:>12}{c:>13}  {verdict}")
    print(f"\n  {problems} figure(s) need attention")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
