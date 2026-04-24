# Quality Checklist

## Tests

- Cover the changed behavior and at least one failure/edge path when meaningful.
- Keep tests deterministic: avoid real network, wall-clock timing, random seeds, and machine-specific paths unless isolated.
- Prefer existing fixtures, factories, and parametrization style.
- Do not rewrite unrelated tests to fit a preferred style.

## Typing

- Preserve compatibility with the configured Python version.
- Use `collections.abc` for container protocols when supported.
- Prefer narrow protocols or typed dicts for public contracts only when they reduce ambiguity.
- Avoid `Any` as a blanket fix; localize ignores and include the narrowest practical target.

## Lint/Format

- Follow configured tools. Do not introduce formatting-only churn across unrelated files.
- Treat generated files, vendored code, migrations, and notebooks according to repo conventions.
- Prefer automated fixes only when the project already uses that tool and the affected scope is small.

## Performance

- Check algorithmic complexity, repeated I/O, unnecessary serialization, N+1 queries, and repeated regex compilation.
- Use `timeit`, `cProfile`, `pyinstrument`, benchmark tests, or app-specific profiling only when useful and available.
- Keep readability unless the hot path is proven or obvious.

## Security Basics

- Avoid `pickle`, `marshal`, unsafe YAML loaders, and dynamic imports for untrusted input.
- Use `subprocess.run([...], shell=False)` unless shell behavior is explicitly required and sanitized.
- Normalize and bound file paths before reading/writing user-selected paths.
- Parameterize SQL/queries and avoid string-built commands.
- Do not log secrets, tokens, full auth headers, or sensitive payloads.
- Use modern password hashing and cryptographic libraries rather than custom crypto.
