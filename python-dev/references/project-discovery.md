# Project Discovery

Use this checklist before changing a Python repository.

## Identify Layout

- Packages: `src/<name>/`, top-level package dirs, namespace packages, scripts.
- Tests: `tests/`, `test_*.py`, `*_test.py`, doctests, examples used as tests.
- Entry points: `[project.scripts]`, console scripts, `__main__.py`, Docker/Cron/server commands.
- Runtime: `requires-python`, `.python-version`, CI matrix, Docker base images, tox/nox envs.

## Identify Tooling

- Package metadata: `pyproject.toml`, `setup.cfg`, `setup.py`.
- Dependency manager: `uv.lock`, `poetry.lock`, `Pipfile.lock`, `requirements*.txt`, `conda*.yml`.
- Tests: `pytest`, `unittest`, `tox`, `nox`, coverage config.
- Lint/format: `ruff`, `black`, `isort`, `flake8`, `pylint`.
- Types: `mypy`, `pyright`, `pyre`, `py.typed`, stub files.

## Pick Validation Commands

Prefer existing commands from docs, Makefiles, task runners, CI, or `pyproject.toml` scripts. If none are obvious:

- `pytest path/to/test_file.py -q` for pytest projects.
- `python -m unittest path.to.test_module` for unittest projects.
- `ruff check <changed paths>` when ruff is configured.
- `mypy <package-or-file>` when mypy is configured.
- `pyright <package-or-file>` when pyright is configured.

In interactive approval modes, ask before broad or slow full-suite commands unless the user requested test work.
