# TypeScript Development Workflow

Use this workflow after inspecting the repository. Load matching Effective TypeScript source skills from the index only when the current task needs deeper guidance.

## 1. Inventory

- Read `package.json` scripts and dependencies.
- Read `tsconfig*.json` and note `strict`, `noImplicitAny`, `strictNullChecks`, `module`, `moduleResolution`, `target`, `jsx`, `allowJs`, `checkJs`, `declaration`, `composite`, and project references.
- Identify source/test/build entry points and framework conventions.
- Run `scripts/ts_project_probe.py <repo>` when a quick inventory helps.

## 2. Choose The Work Mode

- Feature or bug work: follow project conventions, keep type changes local, add runtime checks at untrusted boundaries.
- Type modeling: represent valid states, prefer discriminated unions, keep derived types synchronized with source values.
- Generic/type utility work: ensure type parameters relate inputs/outputs, test distribution and edge cases like `never`, unions, tuples, and readonly data.
- Migration: move module by module, enable stricter options incrementally, track and shrink `any`/assertion debt.
- Config/tooling: change the narrowest config needed, explain behavior changes, and verify with the project command.
- Runtime boundary: treat external data as `unknown`, validate/parse once, then expose safe typed values.

## 3. Implementation Preferences

- Prefer inference for local values; add annotations at API boundaries, exported values, or places that improve checking.
- Prefer `unknown` over `any` for untrusted inputs.
- Prefer `readonly` inputs when functions should not mutate data.
- Prefer object parameters over repeated same-typed positional parameters.
- Prefer standard JavaScript syntax over TS-only runtime-emitting features unless the project already uses them.
- Prefer precise but honest types; avoid types that are only correct for observed examples.

## 4. Validation Order

Start narrow and expand only as confidence grows:

1. Targeted unit/type test for touched code, if available.
2. Typecheck command, often `npm run typecheck`, `pnpm typecheck`, `yarn typecheck`, or `tsc --noEmit`.
3. Relevant test command.
4. Build command.
5. Lint/format command if configured and relevant.

Do not weaken validation by changing scripts or compiler options unless the user explicitly asks for migration scaffolding.

## 5. Debugging Checklist

- If a type error appears wrong, inspect the displayed type and the declared source type separately.
- If narrowing fails, look for mutation, aliases, optional properties, or callbacks crossing control-flow boundaries.
- If inference widens, check `let` vs `const`, contextual typing, object literal placement, and `as const`/`satisfies` opportunities.
- If generics infer poorly, check whether each type parameter appears in multiple positions and whether currying adds an inference site.
- If runtime disagrees with types, remember TypeScript emits JavaScript independently of type correctness and erases types.
- If build behavior changed, compare `tsconfig` inheritance and package manager scripts before editing source.

## 6. Reporting Back

- Summarize changed files and the reason for type/config choices.
- Mention which validation commands ran and their result.
- Call out remaining type debt explicitly, especially assertions, `any`, skipped checks, or migration TODOs.
