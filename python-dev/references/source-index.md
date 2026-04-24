# Source Index

Use these bundled/offline materials before external documentation. Load the smallest relevant file or directory.

## Python 3.14 Official Docs Text

Bundled root: `references/offline/python-3.14-docs-text/`

High-signal paths:

- Table of contents: `contents.txt`
- Language/reference semantics: `reference/`
- Standard library APIs: `library/`
- Packaging/installing guidance: `installing/`, `distributing/`
- How-to guides: `howto/`
- CLI/runtime usage: `using/`
- Version changes: `whatsnew/`, `deprecations/`
- Glossary lookup: `glossary.txt`

Usage rule: prefer docs matching the target repository's configured Python version. Treat bundled 3.14 docs as authoritative only for projects that target or allow 3.14; otherwise use them for general concepts and verify version-sensitive behavior locally.

## Awesome Python Ecosystem List

Bundled root: `references/offline/awesome-python/`

Primary file: `README.md`

Included key files: `README.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `LICENSE`, `pyproject.toml`, `uv.lock`, `.impeccable.md`, `Makefile`, and `.claude/`.

Usage rule: use as an offline library/category discovery index. Before adding a dependency, prefer packages already present in the user repo and check local version constraints.

## Python Algorithm/Example Index

Bundled index: `references/offline/python-examples-index.md`

Bundled source root: `references/offline/Python-master/`

Use the index for categories and sample paths. Inspect bundled source files only when a specific example is needed. Do not paste substantial code wholesale without checking project fit and license.

## Network Policy

Do not require web access for normal Python development tasks. Use network only when the user asks for latest/current information, the target package/version is not covered by local materials, or high-stakes accuracy requires fresh official docs.
