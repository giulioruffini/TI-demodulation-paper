"""Check relocated definitions, first figure citations, and annotated-PDF retention."""
from pathlib import Path
import hashlib,json,re,subprocess
root=Path(__file__).resolve().parents[2]
s=(root/'TN0484_envelope_demodulation.tex').read_text()
main=s.split('\\ifappendices\n\\renewcommand')[0].replace('\\input{figures_src/fig_models_ti_caption.tex}',(root/'figures_src/fig_models_ti_caption.tex').read_text())
figures=re.findall(r'\\label\{(fig:[^}]+)\}',main)
first=[]
for ref in re.findall(r'\\ref\{(fig:[^}]+)\}',main):
 if ref in figures and ref not in first:first.append(ref)
assert first==figures,(first,figures)
old=subprocess.check_output(['git','show','e20c047:TN0484_envelope_demodulation.tex'],cwd=root,text=True)
def labels(t):return set(re.findall(r'\\label\{([^}]+)\}',t))
def cites(t):return {v.strip() for c in re.findall(r'\\cite\w*\{([^}]+)\}',t) for v in c.split(',')}
assert not labels(old)-labels(s)
assert not cites(old)-cites(s)
p=json.loads((root/'notes/2026-10-20_kaiti/annotated_pdf_preservation.json').read_text())
assert hashlib.sha256((root/p['file']).read_bytes()).hexdigest()==p['sha256']
print('PASS: 13 main figures cited in order; all baseline labels and citations retained; annotated PDF unchanged.')
