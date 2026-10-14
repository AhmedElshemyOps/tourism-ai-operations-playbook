# Contributing

Thank you for helping improve the Tourism AI Operations Playbook.

## Useful contributions

- a missing tourism operational scenario;
- clearer verification or privacy controls;
- accessibility and cultural-sensitivity improvements;
- better prompt inputs or output structures;
- regional adaptations that remain clearly labelled;
- corrections to broken links, spelling or formatting;
- fictional examples that improve training value;
- translations reviewed by a competent professional.

## Do not submit

- guest or employee personal data;
- confidential company information;
- supplier rates, contracts or credentials;
- copied content without permission;
- invented statistics, testimonials or expert quotations;
- prompts that remove human approval from high-risk decisions.

## Contribution workflow

1. Search existing issues.
2. Open a structured issue describing the tourism problem.
3. Fork the repository and create a focused branch.
4. Update the relevant chapter and data indexes when applicable. Individual prompt Markdown files are generated from `data/prompts.json`.
5. Run `python3 tools/render_prompt_library.py`, `python3 tools/refresh_inventory.py`, then `python3 tools/validate_repository.py`. Include the generated files and inventories in your pull request.
6. Submit a pull request using the provided template.

## Prompt quality standard

Every new prompt must include:

- AI role;
- business task;
- operational context;
- required inputs;
- output structure;
- limitations;
- missing-information instruction;
- privacy rule;
- verification requirements;
- accountable human approval point.

## Review

The project maintainer may request evidence, clearer wording, stronger risk controls or a narrower scope before accepting a contribution.
