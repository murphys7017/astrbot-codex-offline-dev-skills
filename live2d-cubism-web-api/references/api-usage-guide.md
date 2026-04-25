# API Usage Guide

Use this as the compact API workflow. For exact signatures, open `references/api-index.md` then the specific `Framework/src` file.

## 1. Framework Lifecycle

Main classes/files:

- `live2dcubismframework.ts`: `CubismFramework`, `Option`, `LogLevel`.
- `id/cubismidmanager.ts`: ID lookup used by parameters, parts, drawables.

Required order:

1. Configure `Option.logFunction` and `Option.loggingLevel` if logging is needed.
2. Call `CubismFramework.startUp(option)` once before using the Framework.
3. Call `CubismFramework.initialize()` once before creating/using models.
4. Use `CubismFramework.getIdManager()` after initialization for `CubismIdHandle` lookup.
5. Call `CubismFramework.dispose()` when Framework resources should be released.
6. Call `CubismFramework.cleanUp()` only when fully tearing down static state.

## 2. Model Manifest And Loading

Main classes/files:

- `cubismmodelsettingjson.ts`: `CubismModelSettingJson`.
- `icubismmodelsetting.ts`: manifest query interface.
- `model/cubismmoc.ts`: `CubismMoc` creation.
- `model/cubismusermodel.ts`: user-facing wrapper for model, physics, pose, renderer.

Use `.model3.json` as a manifest:

- `getModelFileName()` for `.moc3`.
- `getTextureCount()`, `getTextureDirectory()`, `getTextureFileName(index)` for textures.
- `getPhysicsFileName()`, `getPoseFileName()`, `getUserDataFile()` for optional files.
- `getExpressionCount()`, `getExpressionName(index)`, `getExpressionFileName(index)` for expressions.
- `getMotionGroupCount()`, `getMotionGroupName(index)`, `getMotionCount(groupName)`, `getMotionFileName(groupName, index)` for motions.
- `getEyeBlinkParameterId(index)`, `getLipSyncParameterId(index)` for effect parameter mapping.

## 3. Model Parameters, Parts, And Drawables

Main class/file: `model/cubismmodel.ts`.

Use IDs for clarity and indices for hot paths:

- Get ID: `CubismFramework.getIdManager().getId("ParamAngleX")`.
- Get index: `model.getParameterIndex(id)`.
- Read value: `model.getParameterValueById(id)` or `model.getParameterValueByIndex(index)`.
- Set value: `model.setParameterValueById(id, value, weight?)`.
- Add value: `model.addParameterValueById(id, value, weight?)`.
- Multiply value: `model.multiplyParameterValueById(id, value, weight?)`.
- Save/restore: `model.saveParameters()` and `model.loadParameters()`.

Part APIs:

- `getPartIndex(id)`, `getPartCount()`, `getPartOpacityById(id)`, `setPartOpacityById(id, opacity)`.

Drawable APIs:

- `getDrawableCount()`, `getDrawableId(index)`, `getDrawableVertices(index)`, `getDrawableVertexUvs(index)`, `getDrawableOpacity(index)`, `getDrawableBlendMode(index)`, `getDrawableDynamicFlagIsVisible(index)`.

## 4. Rendering And WebGL

Main files:

- `rendering/cubismrenderer.ts`: renderer abstraction.
- `rendering/cubismrenderer_webgl.ts`: WebGL implementation.
- `math/cubismmatrix44.ts`, `math/cubismmodelmatrix.ts`, `math/cubismviewmatrix.ts`: transforms.

Typical responsibilities:

- Create/initialize renderer with a `CubismModel`.
- Set WebGL context with `setGl`/`setGL` according to the concrete class.
- Create WebGL textures in application code.
- Register each texture with `CubismRenderer_WebGL.bindTexture(modelTextureNo, glTexture)`.
- Set premultiplied alpha consistently with texture upload and renderer settings.
- Build MVP matrix with model/view/projection matrices and pass it with `setMvpMatrix(matrix)`.
- Call `drawModel()` after update and texture binding.
- Release WebGL resources and renderer objects on teardown/context loss.

## 5. Motions And Expressions

Main files:

- `motion/acubismmotion.ts`: base motion and callbacks.
- `motion/cubismmotion.ts`: `.motion3.json` motion implementation.
- `motion/cubismmotionmanager.ts`: priority and playback manager.
- `motion/cubismmotionqueuemanager.ts`: queue, events, finish state.
- `motion/cubismexpressionmotion.ts`: expression motion.
- `motion/cubismexpressionmotionmanager.ts`: expression blending manager.

Rules:

- Keep motion group names and file names from `ICubismModelSetting` instead of hard-coding paths.
- Use priority reservation before starting important motions.
- Apply motion/expression updates before final `model.update()`/rendering.
- Use callbacks/events from `ACubismMotion` / queue manager for start/end behavior when needed.

## 6. Physics And Effects

Main files:

- `physics/cubismphysics.ts`: parse/evaluate/interpolate physics.
- `effect/cubismeyeblink.ts`: auto eye blink.
- `effect/cubismbreath.ts`: breath parameter oscillation.
- `effect/cubismlook.ts`: look-at parameter mapping.
- `effect/cubismpose.ts`: pose opacity transitions.
- `motion/*updater.ts` and `motion/cubismupdatescheduler.ts`: update order helpers.

Rules:

- Load optional files only if manifest entries exist.
- Pass `deltaTimeSeconds` consistently.
- Apply look/drag values before rendering.
- Stabilize physics after load if immediate stable display is required.

## 7. Core Type Declarations

Use `references/offline/CubismSdkForWeb-5-r.5/Core/live2dcubismcore.d.ts` for low-level Core objects and types. Do not assume Core JavaScript/WASM files are bundled in this skill; they must come from the user's SDK/app package and comply with Live2D licensing.