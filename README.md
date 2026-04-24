# Codex Offline Development Skills

Offline-first Codex skills for Python development, TypeScript development, and AstrBot plugin development.

## Skills

- `python-dev`: Python project development, refactoring, testing, typing, dependencies, CLI/API work, scripts, performance, and basic security checks with bundled offline Python references.
- `typescript-dev`: TypeScript/JavaScript development, type modeling, generics, tsconfig, migration, type safety, runtime boundaries, tests, builds, linting, and compiler/toolchain debugging with bundled Effective TypeScript skills.
- `astrbot-dev`: AstrBot plugin development, event listeners, message chains, config, session control, AI/provider calls, HTML-to-image output, message sending, MCP/skill integration basics, and debugging with bundled AstrBot docs.

## Offline Reference Policy

Each skill prefers bundled files under `references/offline/` before web access. Browse or download only when the user explicitly asks for latest upstream behavior or when the bundled snapshot is insufficient.

## Install Locally

Copy the skill directories into your Codex skills folder:

```powershell
Copy-Item -Recurse -Force python-dev C:\Users\Administrator\.codex\skills\python-dev
Copy-Item -Recurse -Force typescript-dev C:\Users\Administrator\.codex\skills\typescript-dev
Copy-Item -Recurse -Force astrbot-dev C:\Users\Administrator\.codex\skills\astrbot-dev
```

Restart Codex so the skill list reloads.

## Validate

```powershell
python C:\Users\Administrator\.codex\skills\.system\skill-creator\scripts\quick_validate.py python-dev
python C:\Users\Administrator\.codex\skills\.system\skill-creator\scripts\quick_validate.py typescript-dev
python C:\Users\Administrator\.codex\skills\.system\skill-creator\scripts\quick_validate.py astrbot-dev
```