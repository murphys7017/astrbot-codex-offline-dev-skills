# Effective TypeScript Index

This index maps TypeScript development problems to the 83 bundled offline source skills. Load only the specific local source skill files that match the current task; paths are relative to this skill directory.

## Project Setup, Tooling, And Environment

- `references/offline/effective-typescript-skills/tsconfig-options/SKILL.md` (`tsconfig-options`): setting up TypeScript projects, strict mode, surprising type-check behavior.
- `references/offline/effective-typescript-skills/typescript-devdependencies/SKILL.md` (`typescript-devdependencies`): installing TypeScript, `@types/*`, package dependency and publishing setup.
- `references/offline/effective-typescript-skills/accurate-environment-model/SKILL.md` (`accurate-environment-model`): globals, `window`, environment variables, build-time constants, global type definitions.
- `references/offline/effective-typescript-skills/write-modern-javascript/SKILL.md` (`write-modern-javascript`): TS output, `target`, language features, browser/runtime support, bundle size.
- `references/offline/effective-typescript-skills/compiler-performance/SKILL.md` (`compiler-performance`): slow builds, IDE responsiveness, project references, large codebases.
- `references/offline/effective-typescript-skills/source-maps-debugging/SKILL.md` (`source-maps-debugging`): debugging compiled TS/JS, stack traces, sourcemaps.
- `references/offline/effective-typescript-skills/editor-interrogation/SKILL.md` (`editor-interrogation`): using editor hover, go-to-definition, quick info, and type inspection to understand compiler behavior.
- `references/offline/effective-typescript-skills/three-versions-types/SKILL.md` (`three-versions-types`): type declaration publishing, `@types` conflicts, library type version mismatches.
- `references/offline/effective-typescript-skills/export-public-types/SKILL.md` (`export-public-types`): designing and exporting public library types.
- `references/offline/effective-typescript-skills/tsdoc-comments/SKILL.md` (`tsdoc-comments`): public API docs, generated docs, comments for complex types.

## JavaScript Interop And Migration

- `references/offline/effective-typescript-skills/ts-js-relationship/SKILL.md` (`ts-js-relationship`): explaining TS vs JS, migration concepts, newcomer guidance.
- `references/offline/effective-typescript-skills/allowjs-mixing/SKILL.md` (`allowjs-mixing`): gradual JS-to-TS adoption, mixed codebases, large migrations.
- `references/offline/effective-typescript-skills/ts-check-jsdoc-experiment/SKILL.md` (`ts-check-jsdoc-experiment`): using `// @ts-check` and JSDoc before or during migration.
- `references/offline/effective-typescript-skills/module-by-module-migration/SKILL.md` (`module-by-module-migration`): incremental migration strategy by module boundaries.
- `references/offline/effective-typescript-skills/noimplicitany-completion/SKILL.md` (`noimplicitany-completion`): resolving `noImplicitAny` during migration.
- `references/offline/effective-typescript-skills/type-coverage/SKILL.md` (`type-coverage`): measuring type safety and reducing hidden `any`.
- `references/offline/effective-typescript-skills/type-safe-monkey-patching/SKILL.md` (`type-safe-monkey-patching`): globals, built-ins, DOM extensions, jQuery/D3-style patches.
- `references/offline/effective-typescript-skills/module-augmentation/SKILL.md` (`module-augmentation`): augmenting third-party modules or global declarations.

## Core Type Modeling

- `references/offline/effective-typescript-skills/types-as-sets/SKILL.md` (`types-as-sets`): reasoning about assignability, unions, intersections, and `extends`.
- `references/offline/effective-typescript-skills/structural-typing/SKILL.md` (`structural-typing`): structural compatibility, excess compatibility surprises.
- `references/offline/effective-typescript-skills/domain-language-types/SKILL.md` (`domain-language-types`): modeling domain concepts in names and types.
- `references/offline/effective-typescript-skills/valid-state-types/SKILL.md` (`valid-state-types`): representing states without invalid combinations.
- `references/offline/effective-typescript-skills/tagged-unions/SKILL.md` (`tagged-unions`): discriminated unions and variant modeling.
- `references/offline/effective-typescript-skills/exclusive-or-properties/SKILL.md` (`exclusive-or-properties`): object shapes where exactly one property set is valid.
- `references/offline/effective-typescript-skills/distinct-special-values/SKILL.md` (`distinct-special-values`): avoiding ambiguous sentinel values.
- `references/offline/effective-typescript-skills/branded-types/SKILL.md` (`branded-types`): nominal distinctions for primitive IDs, units, and semantic strings/numbers.
- `references/offline/effective-typescript-skills/precise-string-types/SKILL.md` (`precise-string-types`): string literal unions, enums alternatives, constrained strings.
- `references/offline/effective-typescript-skills/template-literal-types/SKILL.md` (`template-literal-types`): deriving precise string patterns and APIs.
- `references/offline/effective-typescript-skills/type-vs-interface/SKILL.md` (`type-vs-interface`): choosing `type` vs `interface` for object modeling.
- `references/offline/effective-typescript-skills/record-types-sync/SKILL.md` (`record-types-sync`): keeping records, keys, and value types synchronized.
- `references/offline/effective-typescript-skills/mirror-types/SKILL.md` (`mirror-types`): deriving types from values or external APIs without duplication.
- `references/offline/effective-typescript-skills/unify-types/SKILL.md` (`unify-types`): reducing near-duplicate types and noisy unions.
- `references/offline/effective-typescript-skills/dry-types/SKILL.md` (`dry-types`): removing repeated type declarations safely.
- `references/offline/effective-typescript-skills/index-signature-alternatives/SKILL.md` (`index-signature-alternatives`): replacing broad index signatures with safer mapped/object types.
- `references/offline/effective-typescript-skills/avoid-numeric-index/SKILL.md` (`avoid-numeric-index`): array-like types and numeric index pitfalls.
- `references/offline/effective-typescript-skills/limit-optional-properties/SKILL.md` (`limit-optional-properties`): optional properties, undefined semantics, and clearer alternatives.
- `references/offline/effective-typescript-skills/no-null-in-aliases/SKILL.md` (`no-null-in-aliases`): nullability placement and alias design.
- `references/offline/effective-typescript-skills/push-null-to-perimeter/SKILL.md` (`push-null-to-perimeter`): containing nullable values at boundaries.
- `references/offline/effective-typescript-skills/use-readonly/SKILL.md` (`use-readonly`): readonly arrays/objects, mutation prevention, API intent.

## Inference, Narrowing, And Control Flow

- `references/offline/effective-typescript-skills/type-narrowing/SKILL.md` (`type-narrowing`): unions, nullable values, undefined checks, discriminated unions.
- `references/offline/effective-typescript-skills/consistent-aliases/SKILL.md` (`consistent-aliases`): lost refinements from aliases and property variables.
- `references/offline/effective-typescript-skills/context-type-inference/SKILL.md` (`context-type-inference`): contextual typing, extracted callbacks/values, `as const`.
- `references/offline/effective-typescript-skills/understand-type-widening/SKILL.md` (`understand-type-widening`): literal widening, `let` vs `const`, preserving narrow types.
- `references/offline/effective-typescript-skills/evolving-types/SKILL.md` (`evolving-types`): variables whose inferred type evolves through assignments.
- `references/offline/effective-typescript-skills/prefer-type-annotations/SKILL.md` (`prefer-type-annotations`): when explicit annotations improve checking or API clarity.
- `references/offline/effective-typescript-skills/avoid-inferable-annotations/SKILL.md` (`avoid-inferable-annotations`): removing redundant annotations when inference is sufficient.
- `references/offline/effective-typescript-skills/create-objects-all-at-once/SKILL.md` (`create-objects-all-at-once`): avoiding incremental object construction type errors.
- `references/offline/effective-typescript-skills/different-variables-types/SKILL.md` (`different-variables-types`): avoiding reused variables with changing types.
- `references/offline/effective-typescript-skills/excess-property-checking/SKILL.md` (`excess-property-checking`): object literal checks, assignment differences, API shape validation.
- `references/offline/effective-typescript-skills/exhaustiveness-checking/SKILL.md` (`exhaustiveness-checking`): exhaustive switches/checks over unions.
- `references/offline/effective-typescript-skills/imprecise-over-inaccurate/SKILL.md` (`imprecise-over-inaccurate`): choosing safe broad types over incorrect precise types.
- `references/offline/effective-typescript-skills/avoid-anecdotal-types/SKILL.md` (`avoid-anecdotal-types`): avoiding types inferred only from incomplete example data.

## Generics And Type-Level Programming

- `references/offline/effective-typescript-skills/generics-as-functions/SKILL.md` (`generics-as-functions`): thinking about generics as type-level functions.
- `references/offline/effective-typescript-skills/avoid-unnecessary-type-params/SKILL.md` (`avoid-unnecessary-type-params`): removing type parameters that do not relate values.
- `references/offline/effective-typescript-skills/conditional-types-over-overloads/SKILL.md` (`conditional-types-over-overloads`): replacing overload sets when return type depends on input type.
- `references/offline/effective-typescript-skills/control-union-distribution/SKILL.md` (`control-union-distribution`): distributive conditional type surprises, `never`, boolean, unions.
- `references/offline/effective-typescript-skills/tail-recursive-generics/SKILL.md` (`tail-recursive-generics`): recursive type utilities and compiler depth/performance.
- `references/offline/effective-typescript-skills/variadic-tuple-types/SKILL.md` (`variadic-tuple-types`): rest parameters, tuple preservation, typed pipelines/composition.
- `references/offline/effective-typescript-skills/currying-inference/SKILL.md` (`currying-inference`): improving inference with currying or builder-style APIs.
- `references/offline/effective-typescript-skills/functional-constructs-types/SKILL.md` (`functional-constructs-types`): typing higher-order functions and functional patterns.
- `references/offline/effective-typescript-skills/codegen-over-complex-types/SKILL.md` (`codegen-over-complex-types`): replacing fragile type-level logic with generated types.
- `references/offline/effective-typescript-skills/type-display-attention/SKILL.md` (`type-display-attention`): improving IDE display for public or complex types.

## Functions, APIs, And Library Design

- `references/offline/effective-typescript-skills/function-type-expressions/SKILL.md` (`function-type-expressions`): choosing function type syntax and call signatures.
- `references/offline/effective-typescript-skills/avoid-repeated-params/SKILL.md` (`avoid-repeated-params`): replacing same-typed parameter lists with objects/options.
- `references/offline/effective-typescript-skills/liberal-accept-strict-return/SKILL.md` (`liberal-accept-strict-return`): API inputs broad, outputs precise.
- `references/offline/effective-typescript-skills/callback-this-type/SKILL.md` (`callback-this-type`): callbacks with `this` context, event handlers, library callbacks.
- `references/offline/effective-typescript-skills/async-over-callbacks/SKILL.md` (`async-over-callbacks`): preferring promises/async flows over callbacks.
- `references/offline/effective-typescript-skills/conditional-types-over-overloads/SKILL.md` (`conditional-types-over-overloads`): APIs with input-dependent return types.
- `references/offline/effective-typescript-skills/export-public-types/SKILL.md` (`export-public-types`): stable public API type exports.
- `references/offline/effective-typescript-skills/tsdoc-comments/SKILL.md` (`tsdoc-comments`): documenting public APIs and complex types.

## Runtime Boundaries And Safety

- `references/offline/effective-typescript-skills/code-gen-independent/SKILL.md` (`code-gen-independent`): types are erased, runtime checks still needed, `instanceof` limitations.
- `references/offline/effective-typescript-skills/runtime-type-reconstruction/SKILL.md` (`runtime-type-reconstruction`): deriving runtime checks/schema from static types or vice versa.
- `references/offline/effective-typescript-skills/hide-unsafe-assertions/SKILL.md` (`hide-unsafe-assertions`): isolating assertions behind validated helpers.
- `references/offline/effective-typescript-skills/prefer-unknown-over-any/SKILL.md` (`prefer-unknown-over-any`): safe handling of untrusted values.
- `references/offline/effective-typescript-skills/limit-any-type/SKILL.md` (`limit-any-type`): reducing `any` and preventing unsound spread.
- `references/offline/effective-typescript-skills/narrow-any-scope/SKILL.md` (`narrow-any-scope`): containing unavoidable `any` locally.
- `references/offline/effective-typescript-skills/precise-any-variants/SKILL.md` (`precise-any-variants`): choosing `any` variants only when truly needed.
- `references/offline/effective-typescript-skills/soundness-traps/SKILL.md` (`soundness-traps`): known unsoundness in arrays, variance, refinements, and declarations.
- `references/offline/effective-typescript-skills/type-checking-vs-testing/SKILL.md` (`type-checking-vs-testing`): deciding what belongs in types vs tests.
- `references/offline/effective-typescript-skills/test-your-types/SKILL.md` (`test-your-types`): testing type-level behavior and public declarations.

## TypeScript/JavaScript Language Edges

- `references/offline/effective-typescript-skills/type-value-space/SKILL.md` (`type-value-space`): type space vs value space, `typeof`, classes, destructuring issues.
- `references/offline/effective-typescript-skills/ecmascript-over-typescript-features/SKILL.md` (`ecmascript-over-typescript-features`): preferring standard JS features over TS-only syntax where appropriate.
- `references/offline/effective-typescript-skills/avoid-wrapper-types/SKILL.md` (`avoid-wrapper-types`): `string`/`number`/`boolean` vs `String`/`Number`/`Boolean`.
- `references/offline/effective-typescript-skills/dom-hierarchy/SKILL.md` (`dom-hierarchy`): DOM element/event hierarchy and safe DOM typing.
- `references/offline/effective-typescript-skills/iterate-objects-safely/SKILL.md` (`iterate-objects-safely`): object iteration, `Object.keys`, key typing.
- `references/offline/effective-typescript-skills/avoid-wrapper-types/SKILL.md` (`avoid-wrapper-types`): primitive wrapper confusion in APIs and errors.
- `references/offline/effective-typescript-skills/no-type-in-docs/SKILL.md` (`no-type-in-docs`): avoiding stale type info in prose comments.

## Quick Loading Recipes

- Build or IDE is slow: load `compiler-performance`, then `tsconfig-options`.
- Strict migration is noisy: load `allowjs-mixing`, `module-by-module-migration`, `noimplicitany-completion`, `type-coverage`.
- API response or env var typing: load `accurate-environment-model`, `prefer-unknown-over-any`, `runtime-type-reconstruction`, `hide-unsafe-assertions`.
- Generic utility fails on unions: load `control-union-distribution`, `generics-as-functions`, `avoid-unnecessary-type-params`.
- Public library API types: load `export-public-types`, `type-display-attention`, `test-your-types`, `three-versions-types`.
- Nullable or impossible state bugs: load `valid-state-types`, `tagged-unions`, `push-null-to-perimeter`, `limit-optional-properties`.
