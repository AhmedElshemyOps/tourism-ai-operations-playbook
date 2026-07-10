#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []

# Required files
required = [
    'README.md', 'START-HERE.md', 'LICENSE', 'CITATION.cff',
    'data/articles.json', 'data/prompts.json', 'data/prompts.csv',
    'docs/index.html'
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f'Missing required file: {rel}')

# JSON and prompt counts
try:
    prompts = json.loads((ROOT / 'data/prompts.json').read_text(encoding='utf-8'))
    if len(prompts) != 100:
        errors.append(f'Expected 100 prompts, found {len(prompts)}')
    ids = [p['id'] for p in prompts]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate prompt IDs found')
    for p in prompts:
        for key in ['title','prompt','risk_level','version','source_article']:
            if not p.get(key):
                errors.append(f"Prompt {p.get('id')} missing {key}")
except Exception as exc:
    errors.append(f'Invalid prompts.json: {exc}')

try:
    articles = json.loads((ROOT / 'data/articles.json').read_text(encoding='utf-8'))
    if len(articles) != 10:
        errors.append(f'Expected 10 articles, found {len(articles)}')
except Exception as exc:
    errors.append(f'Invalid articles.json: {exc}')

# Local Markdown links
link_re = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for path in ROOT.rglob('*.md'):
    text = path.read_text(encoding='utf-8', errors='ignore')
    for target in link_re.findall(text):
        target = target.strip().split()[0].strip('<>')
        if target.startswith(('http://','https://','mailto:','#')):
            continue
        target = target.split('#')[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f'Broken Markdown link in {path.relative_to(ROOT)}: {target}')

# Simple HTML local references
class RefParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        for key in ('href','src'):
            if key in d: self.refs.append(d[key])

for path in (ROOT / 'docs').rglob('*.html'):
    parser=RefParser(); parser.feed(path.read_text(encoding='utf-8', errors='ignore'))
    for ref in parser.refs:
        if ref.startswith(('http://','https://','mailto:','tel:','#','data:','javascript:')):
            continue
        clean=urlparse(ref).path
        if not clean: continue
        resolved=(path.parent / clean).resolve()
        if not resolved.exists():
            errors.append(f'Broken HTML reference in {path.relative_to(ROOT)}: {ref}')

if errors:
    print('Repository validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print('Repository validation passed.')
print('- 10 playbook chapters')
print('- 100 prompt records')
print('- Local Markdown and HTML references resolved')
