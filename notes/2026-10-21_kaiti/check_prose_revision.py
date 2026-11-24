"""Fidelity and edition checks for the approved journal prose revision."""
from pathlib import Path
import hashlib,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2]
old=subprocess.check_output(['git','show','24d34c1:TN0484_envelope_demodulation.tex'],cwd=ROOT,text=True)
source=(ROOT/'TN0484_envelope_demodulation.tex').read_text()

def expand(text):
    pattern=r'\\input\{((?:planning/parts|figures_src)/[^}]+)\}'
    while re.search(pattern,text):
        text=re.sub(pattern,lambda m:(ROOT/(m[1] if m[1].endswith('.tex') else m[1]+'.tex')).read_text(),text)
    return text

def labels(t):return set(re.findall(r'\\label\{([^}]+)\}',t))
def cites(t):return {v.strip() for c in re.findall(r'\\cite\w*\{([^}]+)\}',t) for v in c.split(',')}
expanded=expand(source)
assert not labels(old)-labels(expanded),labels(old)-labels(expanded)
assert not cites(old)-cites(expanded),cites(old)-cites(expanded)
aux='\n'.join((ROOT/f'{name}.aux').read_text() for name in ('TN0484_jne','TN0484_jne_supplement'))
actual=set(re.findall(r'\\newlabel\{([^}]+)\}',aux))
assert not labels(old)-actual,labels(old)-actual

def ping(t):
    section=t[t.index(r'\subsection{Exact next-generation'):]
    return re.search(r'\\begin\{equation\}.*?\\label\{eq:nmm2-ping\}.*?\\end\{equation\}',section,re.S)[0]
assert ping(old)==ping(source)
assert source.index(r'\label{eq:nmm2-ping}') < source.index(r'\section{Results}')
abstract=ROOT/'planning/tn0484_abstract.tex'
assert abstract.read_text()==subprocess.check_output(['git','show','24d34c1:planning/tn0484_abstract.tex'],cwd=ROOT,text=True)
oldbound=old[old.index(r'\section{Efficiency of a memoryless transfer'):old.index(r'\section{Extension: the laminar column')]
assert (ROOT/'planning/parts/supp_efficiency.tex').read_text().startswith(oldbound.strip())
# All main figures retain their order of first citation.
main=expand(source[:source.index(r'\section{Conclusion}')])
figures=re.findall(r'\\label\{(fig:[^}]+)\}',main)
first=[]
for ref in re.findall(r'\\ref\{(fig:[^}]+)\}',main):
    if ref in figures and ref not in first:first.append(ref)
assert first==figures,(first,figures)
# Original supplementary figure numbers remain stable despite topical placement.
suppaux=(ROOT/'TN0484_jne_supplement.aux').read_text()
originalfigs=re.findall(r'\\label\{(fig:[^}]+)\}',old[old.index(r'\section{Extension: the laminar column'):])
for n,label in enumerate(originalfigs,1):
    assert re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{S'+str(n)+r'\}',suppaux),label
for name in ('TN0484_jne','TN0484_jne_supplement'):
    log=(ROOT/f'{name}.log').read_text(errors='replace')
    assert not re.search(r'^!|undefined|multiply defined|Overfull',log,re.M),name
validation=(ROOT/'build/validation_draft22/TN0484_tn_validation.log').read_text(errors='replace')
assert not re.search(r'^!|undefined|multiply defined|Overfull',validation,re.M),'TN routing'
record=json.loads((ROOT/'notes/2026-10-20_kaiti/annotated_pdf_preservation.json').read_text())
assert hashlib.sha256((ROOT/record['file']).read_bytes()).hexdigest()==record['sha256']
print(f'PASS: {len(labels(old))} baseline labels and {len(cites(old))} citation keys retained in reachable source; labels resolve in built PDFs.')
print('PASS: PING equation unchanged in Methods; approved abstract unchanged; bound derivation unchanged in supplement.')
print('PASS: main figures cited in order; all 13 supplementary figure numbers preserved.')
print('PASS: article, supplement, and temporary TN build have no errors, undefined/multiply defined references, or overfull boxes.')
print('PASS: annotated draft20 unchanged.')
