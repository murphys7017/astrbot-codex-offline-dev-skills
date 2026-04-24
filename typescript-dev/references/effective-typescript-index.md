# Effective TypeScript Index

This index maps TypeScript development problems to the 83 bundled offline source skills. Load only the specific local source skill files that match the current task; paths are relative to this skill directory.

## Project Setup, Tooling, And Environment

- `references/offline/effective-typescript-skills/tsconfig-options/REFERENCE.md` (`tsconfig-options`): setting up TypeScript projects, strict mode, surprising type-check behavior.
- `references/offline/effective-typescript-skills/typescript-devdependencies/REFERENCE.md` (`typescript-devdependencies`): installing TypeScript, `@types/*`, package dependency and publishing setup.
- `references/offline/effective-typescript-skills/accurate-environment-model/REFERENCE.md` (`accurate-environment-model`): globals, `window`, environment variables, build-time constants, global type definitions.
- `references/offline/effective-typescript-skills/write-modern-javascript/REFERENCE.md` (`write-modern-javascript`): TS output, `target`, language features, browser/runtime support, bundle size.
- `references/offline/effective-typescript-skills/compiler-performance/REFERENCE.md` (`compiler-performance`): slow builds, IDE responsiveness, project references, large codebases.
- `references/offline/effective-typescript-skills/source-maps-debugging/REFERENCE.md` (`source-maps-debugging`): debugging compiled TS/JS, stack traces, sourcemaps.
- `references/offline/effective-typescript-skills/editor-interrogation/REFERENCE.md` (`editor-interrogation`): using editor hover, go-to-definition, quick info, and type inspection to understand compiler behavior.
- `references/offline/effective-typescript-skills/three-versions-types/REFERENCE.md` (`three-versions-types`): type declaration publishing, `@types` conflicts, library type version mismatches.
- `references/offline/effective-typescript-skills/export-public-types/REFERENCE.md` (`export-public-types`): designing and exporting public library types.
- `references/offline/effective-typescript-skills/tsdoc-comments/REFERENCE.md` (`tsdoc-comments`): public API docs, generated docs, comments for complex types.

## JavaScript Interop And Migration

- `references/offline/effective-typescript-skills/ts-js-relationship/REFERENCE.md` (`ts-js-relationship`): explaining TS vs JS, migration concepts, newcomer guidance.
- `references/offline/effective-typescript-skills/allowjs-mixing/REFERENCE.md` (`allowjs-mixing`): gradual JS-to-TS adoption, mixed codebases, large migrations.
- `references/offline/effective-typescript-skills/ts-check-jsdoc-experiment/REFERENCE.md` (`ts-check-jsdoc-experiment`): using `// @ts-check` and JSDoc before or during migration.
- `references/offline/effective-typescript-skills/module-by-module-migration/REFERENCE.md` (`module-by-module-migration`): incremental migration strategy by module boundaries.
- `references/offline/effective-typescript-skills/noimplicitany-completion/REFERENCE.md` (`noimplicitany-completion`): resolving `noImplicitAny` during migration.
- `references/offline/effective-typescript-skills/type-coverage/REFERENCE.md` (`type-coverage`): measuring type safety and reducing hidden `any`.
- `references/offline/effective-typescript-skills/type-safe-monkey-patching/REFERENCE.md` (`type-safe-monkey-patching`): globals, built-ins, DOM extensions, jQuery/D3-style patches.
- `references/offline/effective-typescript-skills/module-augmentation/REFERENCE.md` (`module-augmentation`): augmenting third-party modules or global declarations.

## Core Type Modeling

- `references/offline/effective-typescript-skills/types-as-sets/REFERENCE.md` (`types-as-sets`): reasoning about assignability, unions, intersections, and `extends`.
- `references/offline/effective-typescript-skills/structural-typing/REFERENCE.md` (`structural-typing`): structural compatibility, excess compatibility surprises.
- `references/offline/effective-typescript-skills/domain-language-types/REFERENCE.md` (`domain-language-types`): modeling domain concepts in names and types.
- `references/offline/effective-typescript-skills/valid-state-types/REFERENCE.md` (`valid-state-types`): representing states without invalid combinations.
- `references/offline/effective-typescript-skills/tagged-unions/REFERENCE.md` (`tagged-unions`): discriminated unions and variant modeling.
- `references/offline/effective-typescript-skills/exclusive-or-properties/REFERENCE.md` (`exclusive-or-properties`): object shapes where exactly one property set is valid.
- `references/offline/effective-typescript-skills/distinct-special-values/REFERENCE.md` (`distinct-special-values`): avoiding ambiguous sentinel values.
- `references/offline/effective-typescript-skills/branded-types/REFERENCE.md` (`branded-types`): nominal distinctions for primitive IDs, units, and semantic strings/numbers.
- `references/offline/effective-typescript-skills/precise-string-types/REFERENCE.md` (`precise-string-types`): string literal unions, enums alternatives, constrained strings.
- `references/offline/effective-typescript-skills/template-literal-types/REFERENCE.md` (`template-literal-types`): deriving precise string patterns and APIs.
- `references/offline/effective-typescript-skills/type-vs-interface/REFERENCE.md` (`type-vs-interface`): choosing `type` vs `interface` for object modeling.
- `references/offline/effective-typescript-skills/record-types-sync/REFERENCE.md` (`record-types-sync`): keeping records, keys, and value types synchronized.
- `references/offline/effective-typescript-skills/mirror-types/REFERENCE.md` (`mirror-types`): deriving types from values or external APIs without duplication.
- `references/offline/effective-typescript-skills/unify-types/REFERENCE.md` (`unify-types`): reducing near-duplicate types and noisy unions.
- `references/offline/effective-typescript-skills/dry-types/REFERENCE.md` (`dry-types`): removing repeated type declarations safely.
- `references/offline/effective-typescript-skills/index-signature-alternatives/REFERENCE.md` (`index-signature-alternatives`): replacing broad index signatures with safer mapped/object types.
- `references/offline/effective-typescript-skills/avoid-numeric-index/REFERENCE.md` (`avoid-numeric-index`): array-like types and numeric index pitfalls.
- `references/offline/effective-typescript-skills/limit-optional-properties/REFERENCE.md` (`limit-optional-properties`): optional properties, undefined semantics, and clearer alternatives.
- `references/offline/effective-typescript-skills/no-null-in-aliases/REFERENCE.md` (`no-null-in-aliases`): nullability placement and alias design.
- `references/offline/effective-typescript-skills/push-null-to-perimeter/REFERENCE.md` (`push-null-to-perimeter`): containing nullable values at boundaries.
- `references/offline/effective-typescript-skills/use-readonly/REFERENCE.md` (`use-readonly`): readonly arrays/objects, mutation prevention, API intent.

## Inference, Narrowing, And Control Flow

- `references/offline/effective-typescript-skills/type-narrowing/REFERENCE.md` (`type-narrowing`): unions, nullable values, undefined checks, discriminated unions.
- `references/offline/effective-typescript-skills/consistent-aliases/REFERENCE.md` (`consistent-aliases`): lost refinements from aliases and property variables.
- `references/offline/effective-typescript-skills/context-type-inference/REFERENCE.md` (`context-type-inference`): contextual typing, extracted callbacks/values, `as const`.
- `references/offline/effective-typescript-skills/understand-type-widening/REFERENCE.md` (`understand-type-widening`): literal widening, `let` vs `const`, preserving narrow types.
- `references/offline/effective-typescript-skills/evolving-types/REFERENCE.md` (`evolving-types`): variables whose inferred type evolves through assignments.
- `references/offline/effective-typescript-skills/prefer-type-annotations/REFERENCE.md` (`prefer-type-annotations`): when explicit annotations improve checking or API clarity.
- `references/offline/effective-typescript-skills/avoid-inferable-annotations/REFERENCE.md` (`avoid-inferable-annotations`): removing redundant annotations when inference is sufficient.
- `references/offline/effective-typescript-skills/create-objects-all-at-once/REFERENCE.md` (`create-objects-all-at-once`): avoiding incremental object construction type errors.
- `references/offline/effective-typescript-skills/different-variables-types/REFERENCE.md` (`different-variables-types`): avoiding reused variables with changing types.
- `references/offline/effective-typescript-skills/excess-property-checking/REFERENCE.md` (`excess-property-checking`): object literal checks, assignment differences, API shape validation.
- `references/offline/effective-typescript-skills/exhaustiveness-checking/REFERENCE.md` (`exhaustiveness-checking`): exhaustive switches/checks over unions.
- `references/offline/effective-typescript-skills/imprecise-over-inaccurate/REFERENCE.md` (`imprecise-over-inaccurate`): choosing safe broad types over incorrect precise types.
- `references/offline/effective-typescript-skills/avoid-anecdotal-types/REFERENCE.md` (`avoid-anecdotal-types`): avoiding types inferred only from incomplete example data.

## Generics And Type-Level Programming

- `references/offline/effective-typescript-skills/generics-as-functions/REFERENCE.md` (`generics-as-functions`): thinking about generics as type-level functions.
- `references/offline/effective-typescript-skills/avoid-unnecessary-type-params/REFERENCE.md` (`avoid-unnecessary-type-params`): removing type parameters that do not relate values.
- `references/offline/effective-typescript-skills/conditional-types-over-overloads/REFERENCE.md` (`conditional-types-over-overloads`): replacing overload sets when return type depends on input type.
- `references/offline/effective-typescript-skills/control-union-distribution/REFERENCE.md` (`control-union-distribution`): distributive conditional type surprises, `never`, boolean, unions.
- `references/offline/effective-typescript-skills/tail-recursive-generics/REFERENCE.md` (`tail-recursive-generics`): recursive type utilities and compiler depth/performance.
- `references/offline/effective-typescript-skills/variadic-tuple-types/REFERENCE.md` (`variadic-tuple-types`): rest parameters, tuple preservation, typed pipelines/composition.
- `references/offline/effective-typescript-skills/currying-inference/REFERENCE.md` (`currying-inference`): improving inference with currying or builder-style APIs.
- `references/offline/effective-typescript-skills/functional-constructs-types/REFERENCE.md` (`functional-constructs-types`): typing higher-order functions and functional patterns.
- `references/offline/effective-typescript-skills/codegen-over-complex-types/REFERENCE.md` (`codegen-over-complex-types`): replacing fragile type-level logic with generated types.
- `references/offline/effective-typescript-skills/type-display-attention/REFERENCE.md` (`type-display-attention`): improving IDE display for public or complex types.

## Functions, APIs, And Library Design

- `references/offline/effective-typescript-skills/function-type-expressions/REFERENCE.md` (`function-type-expressions`): choosing function type syntax and call signatures.
- `references/offline/effective-typescript-skills/avoid-repeated-params/REFERENCE.md` (`avoid-repeated-params`): replacing same-typed parameter lists with objects/options.
- `references/offline/effective-typescript-skills/liberal-accept-strict-return/REFERENCE.md` (`liberal-accept-strict-return`): API inputs broad, outputs precise.
- `references/offline/effective-typescript-skills/callback-this-type/REFERENCE.md` (`callback-this-type`): callbacks with `this` context, event handlers, library callbacks.
- `references/offline/effective-typescript-skills/async-over-callbacks/REFERENCE.md` (`async-over-callbacks`): preferring promises/async flows over callbacks.
- `references/offline/effective-typescript-skills/conditional-types-over-overloads/REFERENCE.md` (`conditional-types-over-overloads`): APIs with input-dependent return types.
- `references/offline/effective-typescript-skills/export-public-types/REFERENCE.md` (`export-public-types`): stable public API type exports.
- `references/offline/effective-typescript-skills/tsdoc-comments/REFERENCE.md` (`tsdoc-comments`): documenting public APIs and complex types.

## Runtime Boundaries And Safety

- `references/offline/effective-typescript-skills/code-gen-independent/REFERENCE.md` (`code-gen-independent`): types are erased, runtime checks still needed, `instanceof` limitations.
- `references/offline/effective-typescript-skills/runtime-type-reconstruction/REFERENCE.md` (`runtime-type-reconstruction`): deriving runtime checks/schema from static types or vice versa.
- `references/offline/effective-typescript-skills/hide-unsafe-assertions/REFERENCE.md` (`hide-unsafe-assertions`): isolating assertions behind validated helpers.
- `references/offline/effective-typescript-skills/prefer-unknown-over-any/REFERENCE.md` (`prefer-unknown-over-any`): safe handling of untrusted values.
- `references/offline/effective-typescript-skills/limit-any-type/REFERENCE.md` (`limit-any-type`): reducing `any` and preventing unsound spread.
- `references/offline/effective-typescript-skills/narrow-any-scope/REFERENCE.md` (`narrow-any-scope`): containing unavoidable `any` locally.
- `references/offline/effective-typescript-skills/precise-any-variants/REFERENCE.md` (`precise-any-variants`): choosing `any` variants only when truly needed.
- `references/offline/effective-typescript-skills/soundness-traps/REFERENCE.md` (`soundness-traps`): known unsoundness in arrays, variance, refinements, and declarations.
- `references/offline/effective-typescript-skills/type-checking-vs-testing/REFERENCE.md` (`type-checking-vs-testing`): deciding what belongs in types vs tests.
- `references/offline/effective-typescript-skills/test-your-types/REFERENCE.md` (`test-your-types`): testing type-level behavior and public declarations.

## TypeScript/JavaScript Language Edges

- `references/offline/effective-typescript-skills/type-value-space/REFERENCE.md` (`type-value-space`): type space vs value space, `typeof`, classes, destructuring issues.
- `references/offline/effective-typescript-skills/ecmascript-over-typescript-features/REFERENCE.md` (`ecmascript-over-typescript-features`): preferring standard JS features over TS-only syntax where appropriate.
- `references/offline/effective-typescript-skills/avoid-wrapper-types/REFERENCE.md` (`avoid-wrapper-types`): `string`/`number`/`boolean` vs `String`/`Number`/`Boolean`.
- `references/offline/effective-typescript-skills/dom-hierarchy/REFERENCE.md` (`dom-hierarchy`): DOM element/event hierarchy and safe DOM typing.
- `references/offline/effective-typescript-skills/iterate-objects-safely/REFERENCE.md` (`iterate-objects-safely`): object iteration, `Object.keys`, key typing.
- `references/offline/effective-typescript-skills/avoid-wrapper-types/REFERENCE.md` (`avoid-wrapper-types`): primitive wrapper confusion in APIs and errors.
- `references/offline/effective-typescript-skills/no-type-in-docs/REFERENCE.md` (`no-type-in-docs`): avoiding stale type info in prose comments.

## Quick Loading Recipes

- Build or IDE is slow: load `compiler-performance`, then `tsconfig-options`.
- Strict migration is noisy: load `allowjs-mixing`, `module-by-module-migration`, `noimplicitany-completion`, `type-coverage`.
- API response or env var typing: load `accurate-environment-model`, `prefer-unknown-over-any`, `runtime-type-reconstruction`, `hide-unsafe-assertions`.
- Generic utility fails on unions: load `control-union-distribution`, `generics-as-functions`, `avoid-unnecessary-type-params`.
- Public library API types: load `export-public-types`, `type-display-attention`, `test-your-types`, `three-versions-types`.
- Nullable or impossible state bugs: load `valid-state-types`, `tagged-unions`, `push-null-to-perimeter`, `limit-optional-properties`.
