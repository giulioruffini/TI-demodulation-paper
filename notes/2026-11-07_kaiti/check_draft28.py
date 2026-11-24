"""Check draft28's preserved science, edition routing, and article builds."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('redline', ROOT/'code/build_jne_redline.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
BASE='146679e'
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
assert all(equations(new).get(k)==v for k,v in equations(old).items()), 'A baseline labeled equation changed.'
for name in ('planning/tn0484_abstract.tex',
             'code/qif_raster.py',
             'code/fem_quadmaps.npz', 'LICENSE'):
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
tnlog=(ROOT/'build/validation_draft28/TN0484_tn_validation.log').read_text(errors='replace')
assert not re.search(r'^!|undefined|multiply defined|Overfull',tnlog,re.M),'TN edition routing'
print(f'PASS: {len(labels(old))} baseline labels and {len(cites(old))} citations retained and resolved.')
print(f'PASS: {len(equations(old))} labeled equation bodies unchanged apart from punctuation/spacing.')
print('PASS: abstract, full PING system and original QIF code and FEM figure cache unchanged; all derivation equations preserved.')
print('PASS: article/supplement logs, printed references, historical S1–S13 labels and annotated draft20.')
print('PASS: isolated full-TN routing build; canonical TN artifacts were not regenerated.')


manifest=json.loads((ROOT/'notes/2026-11-06_kaiti/draft27_baseline_manifest.json').read_text())
for name in ('TN0484_envelope_demodulation.pdf','TN0484_envelope_demodulation.bbl'):
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==manifest['files'][name]['sha256'],name
for name in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'figures','figures_src'],cwd=ROOT,text=True).splitlines():
    assert (ROOT/name).read_bytes()==subprocess.check_output(['git','show',f'{BASE}:{name}'],cwd=ROOT),name
assert (ROOT/'planning/review_baseline.json').read_bytes()==subprocess.check_output(['git','show',f'{BASE}:planning/review_baseline.json'],cwd=ROOT)
print('PASS: all figure sources/artifacts, recorded reading baseline and pre-existing canonical TN artifacts unchanged.')

# All non-FEM scientific modules remain byte-identical to draft27.
allowed={'planning/parts/fem_sensitivities.tex','planning/parts/steering_algebra.tex',
         'planning/parts/supp_spatial.tex'}
for name in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'planning/parts'],cwd=ROOT,text=True).splitlines():
    if name not in allowed:
        assert (ROOT/name).read_bytes()==subprocess.check_output(['git','show',f'{BASE}:{name}'],cwd=ROOT),name
old_data=json.loads(subprocess.check_output(['git','show',f'{BASE}:code/fem_quadmaps.json'],cwd=ROOT))
new_data=json.loads((ROOT/'code/fem_quadmaps.json').read_text())
def preserve(a,b,path='root'):
    if isinstance(a,dict):
        for k,v in a.items():
            assert k in b,path+'.'+k
            preserve(v,b[k],path+'.'+k)
    elif isinstance(a,list):
        assert len(a)==len(b),path
        for i,(x,y) in enumerate(zip(a,b)): preserve(x,y,f'{path}[{i}]')
    else: assert a==b,(path,a,b)
preserve(old_data,new_data)
print('PASS: all old FEM output leaves and all non-FEM scientific modules retained.')
for name in ('fem_quadmaps','fem_orientation_interface'):
    path=ROOT/f'code/{name}.json'
    assert path.read_bytes()==subprocess.check_output(['git','show',f'6ade413:code/{name}.json'],cwd=ROOT)
print('PASS: imported numerical outputs are byte-identical to Ricardo PR head 6ade413.')
