#!/usr/bin/env python3
"""Refresh the repository manifest and checksums from Git-visible files."""
import hashlib
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def inventory():
    result = subprocess.run(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
        cwd=ROOT, check=True, stdout=subprocess.PIPE,
    )
    return sorted({path.decode('utf-8') for path in result.stdout.split(b'\0')
                   if path and (ROOT / path.decode('utf-8')).is_file()})

if __name__ == '__main__':
    paths = [path for path in inventory() if path not in {'MANIFEST.txt', 'SHA256SUMS.txt'}]
    (ROOT / 'MANIFEST.txt').write_text(''.join(
        f'{path}\t{(ROOT / path).stat().st_size}\n' for path in paths), encoding='utf-8')
    paths = sorted(paths + ['MANIFEST.txt'])
    (ROOT / 'SHA256SUMS.txt').write_text(''.join(
        f'{hashlib.sha256((ROOT / path).read_bytes()).hexdigest()}  {path}\n'
        for path in paths), encoding='utf-8')
    print(f'Refreshed manifest ({len(paths) - 1} files) and checksums ({len(paths)} files).')
