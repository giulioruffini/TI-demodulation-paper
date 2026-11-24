"""Count the reviewed JNE Introduction–Conclusion, excluding math tokens."""

import importlib.util
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("redline", ROOT / "code/build_jne_redline.py")
redline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(redline)
source = redline.expanded_source("6c0e23a")
body = source[source.index(r"\section{Introduction}"):
              source.index(r"\section*{Code and data availability}")]
with tempfile.TemporaryDirectory(prefix="tn0484-prose-count-") as folder:
    path = Path(folder) / "main.tex"
    path.write_text(r"\documentclass{article}\begin{document}" + "\n" + body
                    + r"\end{document}" + "\n")
    result = subprocess.run(
        ["texcount", "-sum=1,1,1,0,0,0,0", "-sub=section", str(path)],
        text=True, capture_output=True, check=True,
    )
    report = "Revision: 6c0e23a; Introduction through Conclusion; math excluded.\n"
    report += result.stdout.replace(str(path), "main.tex")
    (Path(__file__).parent / "main_prose_wordcount.txt").write_text(report)
    print(report)
