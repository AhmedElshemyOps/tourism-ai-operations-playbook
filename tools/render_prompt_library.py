#!/usr/bin/env python3
"""Render the individual prompt library from the canonical tourism dataset."""
from pathlib import Path
import argparse
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true', help='Check generated files without writing them')
args = parser.parse_args()
outputs = {}

def write(root, path, text):
    outputs[path] = text

root = Path(__file__).resolve().parents[1]
prompts = json.loads((root / 'data/prompts.json').read_text())
articles = json.loads((root / 'data/articles.json').read_text())
directories = ['01-tourism-prompting-framework', '02-front-line-tourism-ai-toolkit', '03-dmc-operations-ai-prompts', '04-tourism-transport-dispatch-ai-prompts', '05-tourism-product-development-ai-prompts', '06-tourism-itinerary-ai-prompts', '07-tourism-sales-quotation-ai-prompts', '08-guest-experience-ai-prompts', '09-tourism-quality-sop-ai-prompts', '10-responsible-ai-tourism-guide']
library_paths = [f"prompt-library/{directories[p['article_number'] - 1]}/{p['prompt_number']:02d}-{p['id'][6:]}.md" for p in prompts]
assert len(library_paths) == len(prompts) == 100
groups = {}
for prompt, path in zip(prompts, library_paths):
    assert int(path.split('/')[1][:2]) == prompt['article_number']
    assert int(Path(path).name[:2]) == prompt['prompt_number']
    assert Path(path).stem[3:] == prompt['id'][6:]
    def bullets(values):
        return '\n'.join('- ' + value for value in values)
    text = f"""# {prompt['title']}

**Prompt ID:** `{prompt['id']}`  
**Category:** {prompt['category']}  
**Department:** {prompt['department']}  
**Risk level:** {prompt['risk_level']}  
**Human approval:** Required  
**Version:** {prompt['version']}  
**Last reviewed:** {prompt['last_reviewed']}

{prompt['description']}

## When to use

{prompt['when_to_use']}

**Example scenario:** {prompt['example_scenario']}

## Required inputs

{bullets(prompt['required_inputs'])}

## Expected outputs

{bullets(prompt['expected_outputs'])}

## Copy-ready prompt

```text
{prompt['prompt']}
```

## Trainer note

{prompt['trainer_note']}

[Source article]({prompt['source_article']}) · [Library index](../README.md)
"""
    write(root, path, text)
    groups.setdefault(str(Path(path).parent), []).append((prompt, Path(path).name))
index = '# Tourism Prompt Library\n\n100 copy-ready prompts rendered from [data/prompts.json](../data/prompts.json). The dataset remains the source for prompt text and metadata; regenerate the Markdown files after an approved dataset update.\n\n'
for group, entries in groups.items():
    article = articles[entries[0][0]['article_number'] - 1]
    index += f"- [{article['category']}]({Path(group).name}/README.md) — 10 prompts\n"
    text = f"# {article['category']}\n\n[Read the chapter](../../{article['markdown_path']}) · [All categories](../README.md)\n\n"
    text += '\n'.join(f"{p['prompt_number']}. [{p['title']}]({name})" for p, name in entries) + '\n'
    write(root, group + '/README.md', text)
index += '\nRun `python3 tools/validate_repository.py` to check dataset counts, prompt text fidelity, metadata, links, the manifest and checksums. Human review and the [responsible-use policy](../PRIVACY-AND-RESPONSIBLE-USE.md) still apply.\n'
write(root, 'prompt-library/README.md', index)

if args.check:
    errors = [path for path, text in outputs.items() if not (root / path).is_file() or (root / path).read_text(encoding='utf-8') != text]
    actual = {p.relative_to(root).as_posix() for p in (root / 'prompt-library').rglob('*.md')}
    errors += sorted(actual - set(outputs))
    if errors:
        raise SystemExit('Prompt library differs from the dataset: ' + ', '.join(errors))
    print('Prompt library matches the dataset: 100 prompts and 11 indexes.')
else:
    for path, text in outputs.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('w', encoding='utf-8', newline='\n') as stream:
            stream.write(text)
    print('Rendered 100 prompts and 11 indexes. Refresh the inventories before validation.')
