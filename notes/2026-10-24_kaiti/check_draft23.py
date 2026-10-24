"""Scientific retention and build checks for draft23 against the editing baseline."""
from pathlib import Path
import hashlib, importlib.util, json, re, subprocess
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('redline', ROOT/'code/build_jne_redline.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
old=m.expanded_source('69c106b');new=m.expanded_source()
def labels(t): return {x for x in re.findall(r'\\label\{([^}]+)\}',t) if not x.startswith('\\')}
def cites(t): return {k.strip() for group in re.findall(r'\\cite\w*\{([^}]+)\}',t) for k in group.split(',')}
assert not labels(old)-labels(new),labels(old)-labels(new)
assert not cites(old)-cites(new),cites(old)-cites(new)
def ping(t):
 t=t[t.index(r'\subsection{Exact next-generation'):]
 return re.search(r'\\begin\{equation\}.*?\\label\{eq:nmm2-ping\}.*?\\end\{equation\}',t,re.S)[0]
assert ping(old)==ping(new)
assert new.index(r'\label{eq:nmm2-ping}')<new.index(r'\section{Results}')
for path in ('planning/parts/article_models.tex','planning/parts/supp_efficiency.tex'):
 assert (ROOT/path).read_text()==m.source_at(path,'69c106b'),path
aux='\n'.join((ROOT/f'{name}.aux').read_text() for name in ('TN0484_jne','TN0484_jne_supplement'))
actual=set(re.findall(r'\\newlabel\{([^}]+)\}',aux))
assert not labels(old)-actual, labels(old)-actual
for name in ('TN0484_jne','TN0484_jne_supplement'):
 log=(ROOT/f'{name}.log').read_text(errors='replace')
 assert not re.search(r'^!|undefined|multiply defined|Overfull',log,re.M),name
validation=(ROOT/'build/validation_draft23/TN0484_tn_validation.log').read_text(errors='replace')
assert not re.search(r'^!|undefined|multiply defined|Overfull',validation,re.M),'TN routing'
record=json.loads((ROOT/'notes/2026-10-20_kaiti/annotated_pdf_preservation.json').read_text())
assert hashlib.sha256((ROOT/record['file']).read_bytes()).hexdigest()==record['sha256']
print(f'PASS: {len(labels(old))} baseline labels and {len(cites(old))} citation keys retained; labels resolve.')
print('PASS: full PING system remains unchanged in Methods; model appendix and efficiency derivation unchanged.')
print('PASS: journal and supplement compile without errors, undefined/multiple references, or overfull boxes.')
print('PASS: isolated TN routing build has no errors or reference/overflow warnings; annotated draft20 unchanged.')
