# Quality Assurance Report

**Project:** Tourism AI Operations Playbook  
**Content audit date:** 2026-10-14

## Scope

The published repository was missing its individual prompt library and hidden configuration files. The 100 Markdown prompt files and category indexes have been reconstructed from the existing JSON dataset, preserving the prompt text and metadata. Contribution templates and a Repository Quality workflow are supplied in this correction.

## Reproducible repository checks

Run `python3 tools/validate_repository.py` from the repository root. The check covers:

- 10 chapter records with existing Markdown paths;
- 100 unique JSON prompt records and 100 individual prompt files;
- exact copy-ready prompt text and metadata agreement with the dataset;
- local Markdown links and HTML file references;
- tracked-file manifest paths and byte sizes;
- SHA-256 checksums for the files listed in the checksum inventory.

`MANIFEST.txt` excludes itself and `SHA256SUMS.txt`; `SHA256SUMS.txt` excludes itself and includes the manifest. This avoids self-referential inventories. Git-tracked files plus proposed new repository files form the inventory; local caches and `.git/` are excluded.

## Limits

The correction validates repository content. Browser interaction, mobile layout, external links and the deployed website have not been re-tested as part of this content correction. Historical browser checks from the original package do not establish the behavior of this revision. The new GitHub workflow must run on the pull request before its result can be reported as passing.

Responsible-use policies and human approval requirements remain in the existing prompt text.
