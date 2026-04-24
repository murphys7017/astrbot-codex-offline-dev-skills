# Ecosystem Index

Use the bundled `references/offline/awesome-python/README.md` as the first-pass category index for library discovery. Prefer standard library or dependencies already present in the target repository before adding anything new.

## Common Tool Areas

- Packaging/build: `setuptools`, `hatchling`, `flit`, `pdm`, `poetry`.
- Environments/dependencies: `uv`, `pip`, `pip-tools`, `poetry`, `pdm`, `conda`.
- Testing: `pytest`, `unittest`, `hypothesis`, `coverage.py`, `tox`, `nox`.
- Lint/format: `ruff`, `black`, `isort`, `flake8`, `pylint`.
- Types: `mypy`, `pyright`, `typing_extensions`, stub packages.
- CLI: `argparse`, `click`, `typer`, `rich`.
- Web/API: `FastAPI`, `Starlette`, `Flask`, `Django`, `Pydantic`, `SQLAlchemy`.
- Async/network: `asyncio`, `httpx`, `aiohttp`, `requests` for sync clients.
- Data: `pandas`, `polars`, `numpy`, `scipy`, `pyarrow`.
- Security: `cryptography`, `passlib`, `bandit`, `pip-audit`.

## Dependency Selection Rules

- Reuse dependencies already present in the project.
- Prefer standard library solutions for small scripts and simple CLIs.
- Avoid adding heavyweight frameworks for isolated tasks.
- Check Python-version compatibility, license fit, maintenance status from local metadata when available.
- Use external official docs only when local information is insufficient for the requested package/version.
