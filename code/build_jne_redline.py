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
    """Expand shared inputs and retain the material printed in the JNE edition."""
    source = source_at(SOURCE, revision)
    # Compare the JNE reading edition. Before draft14 all appendices were hidden;
    # from draft14 Appendix A is visible and only the later appendices are hidden.
    # Removing the unprinted tail also prevents latexdiff from treating the old
    # three-column supplement table as an in-place four-column article table edit.
    for marker in [r"\ifappendices" + "\n" + r"\clearpage" + "\n" + r"\appendix",
                   r"\ifappendices" + "\n" + r"\renewcommand{\thefigure}"]:
        if marker in source:
            source = source[:source.index(marker)] + r"\end{document}" + "\n"
            break
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
    # Include the notation source so its table is visible in the comparison.
    notation = "planning/tn0484_notation.tex"
    token = r"\input{" + notation + "}"
    if token in source:
        source = source.replace(token, source_at(notation, revision))
    caption = "figures_src/fig_models_ti_caption.tex"
    token = r"\input{" + caption + "}"
    if token in source:
        source = source.replace(token, source_at(caption, revision))
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
        # latexdiff can retain a label inside a deleted, unnumbered formula.
        # After a move to the supplement, that stale label collides with the
        # current external label. Keep the deleted formula, without its label.
        def without_deleted_label(match):
            block = match.group()
            if r"\DIFdel{" in block and r"\DIFadd{" not in block:
                return re.sub(r"\\label\{[^}]+\}(?:[ \t]*\n)?", "", block)
            return block
        text = re.sub(r"\\begin\{displaymath\}.*?\\end\{displaymath\}",
                      without_deleted_label, text, flags=re.DOTALL)
        label = (r"\noindent{\small Changes relative to v"
                 + config["baseline_version"] + " (" + baseline + r").}\par")
        text = text.replace(r"\begin{document}", r"\begin{document}" + "\n" + label, 1)
        tex = stage / f"{job}.tex"
        tex.write_text(text)
        try:
            with (stage / "build.txt").open("w") as log:
                command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                           f"-output-directory={stage}", f"-jobname={job}",
                           r"\def\jnebuild{}\input{" + str(tex) + "}"]
                subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
                subprocess.run(["bibtex", job], cwd=stage, env=environment,
                               stdout=log, stderr=subprocess.STDOUT, check=True)
                for _ in range(2):
                    subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
        except subprocess.CalledProcessError:
            # TemporaryDirectory removes the failed stage; retain diagnostics first.
            for source, suffix in [(tex, ".tex"), (stage / "build.txt", ".txt"),
                                   (stage / (job + ".log"), ".log")]:
                if source.exists():
                    (ROOT / ("build/redline_build_failure" + suffix)).write_bytes(source.read_bytes())
            raise
        diagnostics = (stage / f"{job}.log").read_text(errors="replace")
        if re.search(r"^!|undefined|Overfull|multiply defined", diagnostics, re.MULTILINE):
            (ROOT / "build/redline_build_failure.log").write_text(diagnostics)
            raise RuntimeError("Redline failed validation; see build/redline_build_failure.log")
        for suffix in [".tex", ".pdf", ".bbl", ".log"]:
            os.replace(stage / (job + suffix), destination.with_suffix(suffix))
    print(f"Updated {config['redline']} against {baseline}")


if __name__ == "__main__":
    main()
