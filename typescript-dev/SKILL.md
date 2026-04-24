---
name: typescript-dev
description: TypeScript and JavaScript project development guidance for TS/JS application or library work, type modeling, generics, tsconfig setup, JavaScript-to-TypeScript migration, type safety improvements, runtime boundary validation, tests, builds, linting, and debugging TypeScript compiler or toolchain issues.
---

# TypeScript Dev

Use this skill as the top-level workflow for TypeScript/JavaScript repository work. Keep the main context small: inspect the project first, then load only the relevant reference sections or Effective TypeScript source skills needed for the task.

## First Steps

1. Identify package manager and scripts from `package.json`.
2. Inspect `tsconfig*.json`, build config, test config, and source layout.
3. Run `scripts/ts_project_probe.py <repo>` when you need a quick inventory of package scripts and TS config files.
4. Classify the request with `references/effective-typescript-index.md`.
5. Load specific bundled offline source skills from `references/offline/effective-typescript-skills/<skill-name>/SKILL.md` only when their row matches the current problem.
6. Follow `references/typescript-workflow.md` for task execution and validation order.

## Operating Rules

- Prefer local project conventions over generic advice.
- Do not copy broad Effective TypeScript content into answers; use it as targeted guidance.
- Fix root causes in types, APIs, config, or runtime boundaries rather than silencing errors.
- Avoid `any`, broad assertions, `skipLibCheck`, or weakened compiler options unless explicitly justified as migration debt.
- For high-risk boundary data, pair static types with runtime validation or parsing.
- Validate with the narrowest available command first, then broaden to typecheck/build/test/lint when practical.

## Bundled References

- `references/effective-typescript-index.md`: category index for the 83 bundled Effective TypeScript skills and their local load paths.
- `references/offline/effective-typescript-skills/`: complete offline copy of the 83 Effective TypeScript source skills.
- `references/typescript-workflow.md`: development, migration, type-safety, runtime-boundary, and debugging workflow.

## Bundled Scripts

- `scripts/ts_project_probe.py`: lightweight inventory for `package.json`, `tsconfig*.json`, and likely test/build/lint/typecheck commands.
