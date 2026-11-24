#!/usr/bin/env python3
"""Compare TeXcount prose counts by section, excluding equations and references."""

import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "TN0484_envelope_demodulation.tex"


def read(path, revision):
    if revision == "working":
        return (ROOT / path).read_text()
    return subprocess.check_output(
        ["git", "show", f"{revision}:{path}"], cwd=ROOT, text=True
    )


def count(text):
    # Text, headings, and captions are words; formulas are counted separately.
    text = (r"\begin{document}" + "\n" + text.replace(r"\end{document}", "")
            + "\n" + r"\end{document}")
    result = subprocess.run(
        ["texcount", "-", "-nobib", "-sum=1,1,1,0,0,0,0",
         "-template={1}|{2}|{3}|{6}|{7}|{SUM}"],
        input=text, text=True, capture_output=True, check=True,
    )
    values = result.stdout.strip().split("|")
    return dict(zip(
        ["text", "headings", "captions", "inline_math", "display_math", "words"],
        map(int, values),
    ))


def sections(revision):
    source = read(SOURCE, revision)
    starts = list(re.finditer(r"^\\section(\*)?\{", source, re.MULTILINE))
    result = {}
    appendix = False
    for index, match in enumerate(starts):
        begin = end = match.end()
        depth = 1
        while depth:
            depth += (source[end] == "{") - (source[end] == "}")
            end += 1
        title = " ".join(source[begin:end - 1].split())
        if title == "Abstract":
            continue
        if title == "Notation and units":
            appendix = True
        label = ("Appendix: " if appendix else "") + title
        stop = starts[index + 1].start() if index + 1 < len(starts) else len(source)
        result[label] = count(source[match.start():stop])
    abstract = read("planning/tn0484_abstract.tex", revision)
    # TeXcount normally ignores command definitions; count their prose bodies.
    abstract = re.sub(r"\\newcommand\{\\abs\w+\}\{", "{", abstract)
    result = {"Abstract": count(abstract), **result}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", default="b6fc18b")
    parser.add_argument("--after", default="working")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    before, after = sections(args.before), sections(args.after)
    if before.keys() != after.keys():
        raise ValueError("Section inventory changed; supply an explicit retention map")
    record = {"before": args.before, "after": args.after,
              "method": "TeXcount text + headings + captions; math, bibliography, and front matter excluded. All source sections counted, including JNE declarations and the supplement.",
              "sections": {name: {"before": before[name], "after": after[name],
                                  "change": after[name]["words"] - before[name]["words"]}
                           for name in before}}
    if args.json:
        args.json.write_text(json.dumps(record, indent=2) + "\n")
    print("| Section | Before | After | Change |")
    print("|---|---:|---:|---:|")
    for name, row in record["sections"].items():
        print(f"| {name} | {row['before']['words']} | {row['after']['words']} | {row['change']:+} |")


if __name__ == "__main__":
    main()
