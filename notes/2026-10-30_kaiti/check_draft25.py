"""Check draft25's preserved science, edition routing, and article builds."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('redline', ROOT/'code/build_jne_redline.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
BASE='8ecc70a'
old=m.expanded_source(BASE);new=m.expanded_source()

def labels(text):
    return {x for x in re.findall(r'\\label\{([^}]+)\}',text) if not x.startswith('\\')}

def cites(text):
    return {k.strip() for g in re.findall(r'\\cite\w*\{([^}]+)\}',text) for k in g.split(',')}

def equations(text):
    result={}
    for match in re.finditer(r'\\begin\{(equation|align)\}(.*?)\\end\{\1\}',text,re.S):
        for key in re.findall(r'\\label\{([^}]+)\}',match[2]):
            value=re.sub(r'\s+','',match[2])
            result[key]=re.sub(r'[,.;](?=\\label|$)','',value)
    return result

assert labels(old)<=labels(new),labels(old)-labels(new)
assert cites(old)<=cites(new),cites(old)-cites(new)
assert equations(old)==equations(new),'A labeled equation changed beyond punctuation/spacing.'
for name in ('planning/tn0484_abstract.tex',
             'planning/parts/supp_efficiency.tex','code/qif_raster.py',
             'code/fem_quadmaps.npz','code/fem_quadmaps.json'):
    assert (ROOT/name).read_bytes()==subprocess.check_output(['git','show',f'{BASE}:{name}'],cwd=ROOT),name

def ping(text):
    return re.search(r'\\begin\{equation\}[^\0]*?\\label\{eq:nmm2-ping\}.*?\\end\{equation\}',
                     text[text.index(r'\subsection{Exact next-generation'):],re.S)[0]

assert ping(old)==ping(new)
assert new.index(r'\label{eq:nmm2-ping}')<new.index(r'\section{Results}')
aux='\n'.join((ROOT/f'{name}.aux').read_text() for name in ('TN0484_jne','TN0484_jne_supplement'))
assert labels(old)<=set(re.findall(r'\\newlabel\{([^}]+)\}',aux))
for job in ('TN0484_jne','TN0484_jne_supplement'):
    log=(ROOT/f'{job}.log').read_text(errors='replace')
    assert not re.search(r'^!|undefined|multiply defined|Overfull',log,re.M),job
    printed=subprocess.check_output(['pdftotext',str(ROOT/f'{job}.pdf'),'-'],text=True)
    assert '??' not in printed,job

expected={'lanmm_p2':1,'lanmm_setup':2,'tacs':3,'entrain':4,'khz':5,'khz_twotone':6,
          'lanmm_p1':7,'nmm2_map':8,'khz_direct':9,'nmm2_jcurve':10,'timing':11,
          'qif_timing':12,'spatial_maps':13}
suppaux=(ROOT/'TN0484_jne_supplement.aux').read_text()
for key,num in expected.items():
    assert re.search(r'\\newlabel\{fig:'+key+r'\}\{\{S'+str(num)+r'\}',suppaux),key

record=json.loads((ROOT/'notes/2026-10-20_kaiti/annotated_pdf_preservation.json').read_text())
assert hashlib.sha256((ROOT/record['file']).read_bytes()).hexdigest()==record['sha256']
tnlog=(ROOT/'build/validation_draft25/TN0484_tn_validation.log').read_text(errors='replace')
assert not re.search(r'^!|undefined|multiply defined|Overfull',tnlog,re.M),'TN edition routing'
print(f'PASS: {len(labels(old))} baseline labels and {len(cites(old))} citations retained and resolved.')
print(f'PASS: {len(equations(old))} labeled equation bodies unchanged apart from punctuation/spacing.')
print('PASS: abstract, full PING system, efficiency derivation and original QIF/FEM inputs unchanged.')
print('PASS: article/supplement logs, printed references, historical S1–S13 labels and annotated draft20.')
print('PASS: isolated full-TN routing build; canonical TN artifacts were not regenerated.')


manifest=json.loads((ROOT/'notes/2026-10-30_kaiti/draft25_baseline_manifest.json').read_text())
for name in ('TN0484_envelope_demodulation.pdf','TN0484_envelope_demodulation.bbl'):
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==manifest[name]['sha256'],name
for name in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'figures','figures_src'],cwd=ROOT,text=True).splitlines():
    assert (ROOT/name).read_bytes()==subprocess.check_output(['git','show',f'{BASE}:{name}'],cwd=ROOT),name
assert (ROOT/'planning/review_baseline.json').read_bytes()==subprocess.check_output(['git','show',f'{BASE}:planning/review_baseline.json'],cwd=ROOT)
print('PASS: all figure sources/artifacts, recorded reading baseline and pre-existing canonical TN artifacts unchanged.')
