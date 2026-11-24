"""Build the full TN in an isolated directory; leave canonical artifacts untouched."""
from pathlib import Path
import os,subprocess
root=Path(__file__).resolve().parents[2]
stage=root/'build/validation_draft23';stage.mkdir(exist_ok=True)
job='TN0484_tn_validation'
cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={stage}',f'-jobname={job}',r'\def\tnbuild{}\input{TN0484_envelope_demodulation}']
env=os.environ.copy();env.update(BIBINPUTS=str(root)+':',BSTINPUTS=str(root)+':')
with (stage/'build.txt').open('w') as log:
 subprocess.run(cmd,cwd=root,stdout=log,stderr=subprocess.STDOUT,check=True)
 subprocess.run(['bibtex',job],cwd=stage,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
 for _ in range(2):subprocess.run(cmd,cwd=root,stdout=log,stderr=subprocess.STDOUT,check=True)
print(stage/(job+'.pdf'))
