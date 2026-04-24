# Offline Reference Strategy

Use bundled references before network access. Treat `references/offline/` as the local documentation snapshot for this skill.

## Rules

1. Start from the local index files in `references/`.
2. Load only the smallest relevant bundled file under `references/offline/`.
3. Do not browse or download docs unless the user explicitly asks for latest upstream behavior or the bundled snapshot is missing/ambiguous.
4. When bundled docs conflict with project-local code, prefer project-local code for implementation details.
5. When version-specific behavior matters, identify the target version from the project before using newer docs.

## Recommended Layout

- `references/offline/<source>/`: copied source documentation or skill files.
- `references/offline-index.md`: map of bundled sources, scope, and entry points.
- Existing workflow/checklist files should link to bundled paths rather than external URLs.