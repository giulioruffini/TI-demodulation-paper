#!/usr/bin/env python3
"""Count the printed article, including ordinary table bodies TeXcount skips."""
import argparse
import json
from pathlib import Path
import re
import subprocess

from build_jne_redline import expanded_source, source_at

ROOT = Path(__file__).resolve().parents[1]


def article_branch(text):
    stack, result = [], []
    for token in re.split(r'(\\ifjne\b|\\ifsupp\b|\\ifappendices\b|\\else\b|\\fi\b)', text):
        if token in (r'\ifjne', r'\ifsupp', r'\ifappendices'):
            stack.append(token == r'\ifjne')
        elif token == r'\else':
            if stack:
                stack[-1] = not stack[-1]
        elif token == r'\fi':
            if stack:
                stack.pop()
        elif all(stack):
            result.append(token)
    return ''.join(result)


def texcount(text):
    text = (r'\documentclass{article}\begin{document}' + '\n'
            + text.replace(r'\end{document}', '') + '\n' + r'\end{document}')
    result = subprocess.run(
        ['texcount', '-', '-sum=1,1,1,0,0,0,0',
         '-template=COUNT|{1}|{2}|{3}|{SUM}'],
        input=text, capture_output=True, text=True, check=True)
    match = re.search(r'COUNT\|(\d+)\|(\d+)\|(\d+)\|(\d+)', result.stdout)
    if match is None or '!!!' in result.stdout:
        raise RuntimeError(result.stdout + result.stderr)
    return dict(zip(('text', 'headings', 'captions', 'base_total'), map(int, match.groups())))


def count(text):
    result = texcount(text)
    # Ordinary tables are inside floats, which TeXcount treats as captions-only.
    # The notation longtable is outside a float and is already counted.
    bodies = re.findall(
        r'\\begin\{tabular\}[\s\S]*?\\toprule([\s\S]*?)\\end\{tabular\}', text)
    result['ordinary_table_words'] = sum(texcount(body)['base_total'] for body in bodies)
    result['total'] = result['base_total'] + result['ordinary_table_words']
    return result


def report(revision=None):
    source = expanded_source(revision)
    main = article_branch(source[source.index(r'\section{Introduction}'):
                                 source.index(r'\section*{Code and data availability}')])
    appendices = article_branch(source[source.index(r'\appendix') + len(r'\appendix'):])
    result = dict(revision=revision or 'working tree', sections={})
    starts = list(re.finditer(r'^\\section\{([^}]+)\}', main, re.M))
    for i, start in enumerate(starts):
        end = starts[i+1].start() if i+1 < len(starts) else len(main)
        result['sections'][start[1]] = count(main[start.start():end])
    result['main'] = count(main)
    result['appendices'] = count(appendices)
    result['total'] = result['main']['total'] + result['appendices']['total']
    abstract = source_at('planning/tn0484_abstract.tex', revision)
    parts = []
    for match in re.finditer(r'\\newcommand\{\\abs\w+\}\{', abstract):
        start = end = match.end()
        depth = 1
        while depth:
            depth += (abstract[end] == '{') - (abstract[end] == '}')
            end += 1
        parts.append(abstract[start:end-1])
    result['abstract'] = texcount('\n'.join(parts))['base_total']
    result['total_with_abstract'] = result['total'] + result['abstract']
    result['method'] = ('TeXcount text + headings + captions, plus ordinary table bodies; '
                        'longtable counted once. Excludes math, abstract, references, '
                        'front matter and declarations.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline')
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    results = [report(args.baseline)] if args.baseline else []
    results.append(report())
    if args.json:
        args.json.write_text(json.dumps(results, indent=2) + '\n')
    for result in results:
        print(result['revision'])
        for name, row in result['sections'].items():
            print(f"  {name}: {row['total']}")
        print(f"  Article appendices: {result['appendices']['total']}")
        print(f"  TOTAL: {result['total']}")
        print(f"  Abstract: {result['abstract']}; total with abstract: {result['total_with_abstract']}")


if __name__ == '__main__':
    main()
