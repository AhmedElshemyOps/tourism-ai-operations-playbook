#!/usr/bin/env python3
from __future__ import annotations

import json
import hashlib
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

from refresh_inventory import inventory

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
    for article in articles:
        if not (ROOT / article['markdown_path']).is_file():
            errors.append(f"Missing article: {article['markdown_path']}")
except Exception as exc:
    errors.append(f'Invalid articles.json: {exc}')

# The generated library must preserve the complete dataset text and metadata.
result = subprocess.run([sys.executable, str(ROOT / 'tools/render_prompt_library.py'), '--check'],
                        capture_output=True, text=True)
if result.returncode:
    errors.append(result.stderr.strip() or result.stdout.strip())

# Packaging inventories must match the actual Git-visible repository files.
try:
    actual = set(inventory()) - {'MANIFEST.txt', 'SHA256SUMS.txt'}
    rows = [line.split('\t') for line in (ROOT / 'MANIFEST.txt').read_text().splitlines()]
    listed = {row[0] for row in rows}
    if listed != actual or len(rows) != len(listed):
        errors.append('Manifest paths do not match repository files; run tools/refresh_inventory.py')
    for path, size in rows:
        if not (ROOT / path).is_file() or (ROOT / path).stat().st_size != int(size):
            errors.append(f'Manifest size mismatch: {path}')
    sums = [line.split('  ', 1) for line in (ROOT / 'SHA256SUMS.txt').read_text().splitlines()]
    if {path for digest, path in sums} != actual | {'MANIFEST.txt'} or len(sums) != len(actual) + 1:
        errors.append('Checksum paths do not match repository files')
    for digest, path in sums:
        if not (ROOT / path).is_file() or hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != digest:
            errors.append(f'Checksum mismatch: {path}')
except Exception as exc:
    errors.append(f'Invalid packaging inventory: {exc}')

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
print('- Individual prompt files match the dataset')
print('- Manifest and checksums match repository files')
print('- Local Markdown and HTML references resolved')
