#!/usr/bin/env python3
"""Build the current JNE redline without advancing its recorded review baseline."""

import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "TN0484_envelope_demodulation.tex"
ABSTRACT = "planning/tn0484_abstract.tex"


def source_at(path, revision=None):
    if revision is None:
        return (ROOT / path).read_text()
    return subprocess.check_output(
        ["git", "show", f"{revision}:{path}"], cwd=ROOT, text=True
    )


def expanded_source(revision=None):
    """Expose the shared abstract to latexdiff; earlier inline abstracts also work."""
    source = source_at(SOURCE, revision)
    include = r"\input{planning/tn0484_abstract.tex}"
    if include in source:
        definitions = source_at(ABSTRACT, revision)
        source = source.replace(include, "")
        for match in re.finditer(r"\\newcommand\{\\(abs\w+)\}\{", definitions):
            start = end = match.end()
            depth = 1
            while depth:
                depth += (definitions[end] == "{") - (definitions[end] == "}")
                end += 1
            value = definitions[start:end - 1]
            source = re.sub(
                r"\\" + match.group(1) + r"\b", lambda _: value, source
            )
    # Join adjacent inline math spans only in the comparison inputs.
    return source.replace("$$", "")


def main():
    config = json.loads((ROOT / "planning/review_baseline.json").read_text())
    baseline = config["baseline_commit"]
    destination = ROOT / config["redline"]
    job = destination.stem
    environment = os.environ.copy()
    environment.update(BIBINPUTS=str(ROOT) + ":", BSTINPUTS=str(ROOT) + ":")
    with tempfile.TemporaryDirectory(prefix=".latex-redline-", dir=ROOT / "build") as temp:
        stage = Path(temp)
        for name, revision in [("old", baseline), ("new", None)]:
            (stage / f"{name}.tex").write_text(expanded_source(revision))
        result = subprocess.run(
            ["latexdiff", "--type=CFONT", "--math-markup=whole",
             "--graphics-markup=none", "--disable-citation-markup",
             str(stage / "old.tex"), str(stage / "new.tex")],
            cwd=ROOT, text=True, capture_output=True, check=True,
        )
        text = "\n".join(line.rstrip() for line in result.stdout.splitlines()) + "\n"
        label = (r"\noindent{\small Changes relative to v"
                 + config["baseline_version"] + " (" + baseline + r").}\par")
        text = text.replace(r"\begin{document}", r"\begin{document}" + "\n" + label, 1)
        tex = stage / f"{job}.tex"
        tex.write_text(text)
        with (stage / "build.txt").open("w") as log:
            command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                       f"-output-directory={stage}", f"-jobname={job}",
                       r"\def\jnebuild{}\input{" + str(tex) + "}"]
            subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
            subprocess.run(["bibtex", job], cwd=stage, env=environment,
                           stdout=log, stderr=subprocess.STDOUT, check=True)
            for _ in range(2):
                subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
        diagnostics = (stage / f"{job}.log").read_text(errors="replace")
        if re.search(r"^!|undefined|Overfull", diagnostics, re.MULTILINE):
            (ROOT / "build/redline_build_failure.log").write_text(diagnostics)
            raise RuntimeError("Redline failed validation; see build/redline_build_failure.log")
        for suffix in [".tex", ".pdf", ".bbl", ".log"]:
            os.replace(stage / (job + suffix), destination.with_suffix(suffix))
    print(f"Updated {config['redline']} against {baseline}")


if __name__ == "__main__":
    main()
