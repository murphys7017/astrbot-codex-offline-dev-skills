---
name: python-dev
description: Practical offline-first Python development workflow support for writing, refactoring, reviewing, testing, typing, dependency management, CLI/API design, scripts, performance tuning, and basic security checks. Use when working on Python projects, packages, pyproject/requirements environments, pytest/unittest suites, ruff/black/mypy/pyright tooling, uv/poetry/pip workflows, FastAPI/Flask/Django APIs, Typer/Click/argparse CLIs, automation scripts, profiling, or safe code quality improvements.
---

# Python Dev

Use this skill for focused Python changes with local repository discovery, local validation, and offline bundled references. Prefer the files under this skill before using external documentation.

## Workflow

1. Inspect project shape: package layout, `pyproject.toml`, lockfiles, tests, entry points, CI, and existing style.
2. Run `python scripts/detect_python_project.py <repo>` from this skill directory when useful.
3. Prefer existing conventions. Do not add new formatters, type checkers, test frameworks, or dependency managers unless requested or already configured.
4. Make minimal root-cause changes. Preserve public APIs unless the task explicitly requests an API change.
5. Validate narrow to broad: targeted test, related module/file, then full suite or lint/type checks when practical.
6. Document behavior changes where the project already keeps docs, examples, changelogs, or CLI help text.

## Offline-First Rules

- Use bundled docs first: `references/offline/python-3.14-docs-text/` mirrors the Python 3.14 text docs.
- Use local ecosystem discovery first: `references/offline/awesome-python/README.md` and `references/ecosystem-index.md`.
- Use `references/offline/python-examples-index.md` to locate bundled algorithm/example categories under `references/offline/Python-master/` without loading the whole source set.
- Avoid network access unless the user explicitly requests current information or the local bundle is insufficient for a version/package not covered offline.
- Apply 3.14-specific semantics only when the target project allows Python 3.14; otherwise infer compatibility from project config.

## Editing Guidance

- Packaging: treat `pyproject.toml` as source of truth for build backend, dependencies, extras, scripts, and tool config.
- Dependencies: prefer the active manager (`uv.lock`, `poetry.lock`, `Pipfile.lock`, `requirements*.txt`, `conda*.yml`). Avoid broad upgrades unless requested.
- Tests: add or update nearby tests only when the repo already has tests. Match local fixtures and parametrization style.
- Typing: improve annotations where they clarify contracts. Avoid annotation churn. Use modern `typing`/`collections.abc` forms only when compatible.
- Errors: raise specific exceptions, preserve traceback context, and keep user-facing messages actionable.
- CLIs/APIs: preserve argument names, status codes, response schemas, exit codes, and backwards compatibility.
- Scripts: prefer `pathlib`, idempotent behavior, explicit encodings, and non-destructive defaults.
- Security: check unsafe deserialization, shell injection, path traversal, secret leakage, weak crypto, SQL injection, SSRF, and broad permissions.

## References

Load only the smallest needed file:

- `references/source-index.md` maps all bundled/offline materials.
- `references/project-discovery.md` gives project inspection and command-selection checklists.
- `references/quality-checklist.md` covers tests, typing, linting, performance, and security prompts.
- `references/ecosystem-index.md` summarizes common library/tool choices backed by the local awesome-python bundle.
- `references/offline/python-3.14-docs-text/contents.txt` is the official docs table of contents.
- `references/offline/python-examples-index.md` is the local examples category map.

## Useful Commands

- Detect project tools: `python scripts/detect_python_project.py <repo>`
- Search Python files: `rg --files -g '*.py' <repo>`
- Find config: `rg --files -g 'pyproject.toml' -g 'setup.cfg' -g 'tox.ini' -g 'noxfile.py' -g 'requirements*.txt' <repo>`
