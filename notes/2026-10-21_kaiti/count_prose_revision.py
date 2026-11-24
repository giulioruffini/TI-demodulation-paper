"""Compare the printed JNE prose, keeping article appendices separate."""
import importlib.util
from pathlib import Path
import re, subprocess, tempfile
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('redline', ROOT/'code/build_jne_redline.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def selected(text):
    stack=[]; out=[]
    for token in re.split(r'(\\ifjne\b|\\ifsupp\b|\\ifappendices\b|\\else\b|\\fi\b)',text):
        if token in (r'\ifjne',r'\ifsupp',r'\ifappendices'):
            stack.append(token==r'\ifjne')
        elif token==r'\else':
            if stack: stack[-1]=not stack[-1]
        elif token==r'\fi':
            if stack: stack.pop()
        elif all(stack): out.append(token)
    return ''.join(out)

def count(text):
    with tempfile.TemporaryDirectory(prefix='tn0484-count-') as folder:
        path=Path(folder)/'count.tex'
        path.write_text(r'\documentclass{article}\begin{document}'+'\n'+text+r'\end{document}')
        result=subprocess.run(['texcount','-sum=1,1,1,0,0,0,0','-sub=section',str(path)],check=True,capture_output=True,text=True)
        return result.stdout.replace(str(path),'count.tex')

reports=[]
for revision in ('24d34c1',None):
    s=m.expanded_source(revision)
    body=selected(s[s.index(r'\section{Introduction}'):s.index(r'\section*{Code and data availability}')])
    # Both versions use an explicit appendix boundary after the main bibliography.
    appendices=selected(s[s.index(r'\appendix')+len(r'\appendix'):])
    reports.append(f'REVISION {revision or "working tree"}\nMAIN NARRATIVE\n'+count(body)+'\nARTICLE APPENDICES\n'+count(appendices))
report='\n'.join(reports)
(ROOT/'notes/2026-10-21_kaiti/prose_revision_wordcount.txt').write_text(report)
print(report)
