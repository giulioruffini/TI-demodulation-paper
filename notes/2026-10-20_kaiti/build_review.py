"""Build the separate reading copy; never publish over the annotated draft20."""
from pathlib import Path
import subprocess, shutil, re

ROOT=Path(__file__).resolve().parents[2]
STAGE=ROOT/"build/review"
(STAGE/"build").mkdir(parents=True,exist_ok=True)
for name in ["TN0484_envelope_demodulation.tex", "references.bib"]:
    shutil.copy2(ROOT/name,STAGE/name)
for name in ["planning","figures_src","figures"]:
    shutil.copytree(ROOT/name,STAGE/name,dirs_exist_ok=True)
jobs=[("TN0484_jne",r"\def\jnebuild{}"),("TN0484_jne_supplement",r"\def\suppbuild{}")]
for cycle in range(2):
    for job,prelude in jobs:
        cmd=["pdflatex","-interaction=nonstopmode","-halt-on-error","-jobname="+job,
             prelude+r"\input{TN0484_envelope_demodulation.tex}"]
        with (STAGE/"build"/(job+"_build.txt")).open("a") as log:
            subprocess.run(cmd,cwd=STAGE,stdout=log,stderr=subprocess.STDOUT,check=True)
            if cycle==0:
                subprocess.run(["bibtex",job],cwd=STAGE,stdout=log,stderr=subprocess.STDOUT,check=True)
            for _ in range(2):
                subprocess.run(cmd,cwd=STAGE,stdout=log,stderr=subprocess.STDOUT,check=True)
for job,_ in jobs:
    text=(STAGE/(job+".log")).read_text(errors="replace")
    warnings=re.findall(r"^.*(?:undefined|Overfull|multiply defined|Rerun to get).*$",text,re.M)
    print(job, re.findall(r"Output written.*",text),warnings,flush=True)

    if warnings:
        raise RuntimeError(f"Unresolved build diagnostics in {job}")
