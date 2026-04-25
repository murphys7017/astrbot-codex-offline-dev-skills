# Live2D Cubism Web Framework API Index

Generated from bundled `references/offline/CubismSdkForWeb-5-r.5/Framework/src/**/*.ts`.
Use this as the first local API router, then open the specific source file for exact signatures and comments.

## Categories

- `effect`: High-level effects such as eye blink, breath, look, and pose.
- `id`: Cubism ID objects and ID manager lookup.
- `math`: Matrices, vectors, view/model transforms, target point smoothing.
- `model`: MOC/model loading, parameter/part/drawable access, user model wrapper.
- `motion`: Motion playback, queues, expressions, update scheduler, motion events.
- `physics`: Physics JSON parsing and parameter evaluation/interpolation.
- `rendering`: Renderer abstraction, WebGL renderer, clipping, masks, shaders, render targets.
- `root`: Framework startup, model setting JSON, default parameter IDs, and base interfaces.
- `type`: Small shared value types.
- `utils`: Debug logging, JSON parser, strings, array helpers.

## effect

High-level effects such as eye blink, breath, look, and pose.

### `effect/cubismbreath.ts`
Exports: class `CubismBreath`; class `BreathParameterData`; namespace `Live2DCubismFramework`; type `BreathParameterData`; type `CubismBreath`

Common methods:
- `CubismBreath.setParameters(breathParameters: Array<BreathParameterData>)` → `void`
- `CubismBreath.getParameters()` → `Array<BreathParameterData>`
- `CubismBreath.updateParameters(model: CubismModel, deltaTimeSeconds: number)` → `void`

### `effect/cubismeyeblink.ts`
Exports: class `CubismEyeBlink`; enum `EyeState`; namespace `Live2DCubismFramework`; type `CubismEyeBlink`; type `EyeState`

Common methods:
- `CubismEyeBlink.setBlinkingInterval(blinkingInterval: number)` → `void`
- `CubismEyeBlink.setParameterIds(parameterIds: Array<CubismIdHandle>)` → `void`
- `CubismEyeBlink.getParameterIds()` → `Array<CubismIdHandle>`
- `CubismEyeBlink.updateParameters(model: CubismModel, deltaTimeSeconds: number)` → `void`
- `CubismEyeBlink.determinNextBlinkingTiming()` → `number`

### `effect/cubismlook.ts`
Exports: class `CubismLook`; class `LookParameterData`; namespace `Live2DCubismFramework`; type `LookParameterData`; type `CubismLook`

Common methods:
- `CubismLook.setParameters(lookParameters: Array<LookParameterData>)` → `void`
- `CubismLook.getParameters()` → `Array<LookParameterData>`

### `effect/cubismpose.ts`
Exports: class `CubismPose`; class `PartData`; namespace `Live2DCubismFramework`; type `CubismPose`; type `PartData`

Common methods:
- `CubismPose.updateParameters(model: CubismModel, deltaTimeSeconds: number)` → `void`
- `CubismPose.reset(model: CubismModel)` → `void`
- `CubismPose.copyPartOpacities(model: CubismModel)` → `void`
- `PartData.assignment(v: PartData)` → `PartData`
- `PartData.initialize(model: CubismModel)` → `void`
- `PartData.clone()` → `PartData`

## id

Cubism ID objects and ID manager lookup.

### `id/cubismid.ts`
Exports: class `CubismId`; namespace `Live2DCubismFramework`; type `CubismId`; type `CubismIdHandle`

Common methods:
- `CubismId.getString()`
- `CubismId.isEqual(c: string | CubismId)` → `boolean`
- `CubismId.isNotEqual(c: string | CubismId)` → `boolean`

### `id/cubismidmanager.ts`
Exports: class `CubismIdManager`; namespace `Live2DCubismFramework`; type `CubismIdManager`

Common methods:
- `CubismIdManager.release()` → `void`
- `CubismIdManager.registerIds(ids: string[])` → `void`
- `CubismIdManager.registerId(id: string)` → `CubismId`
- `CubismIdManager.getId(id: string)` → `CubismId`
- `CubismIdManager.isExist(id: string)` → `boolean`

## math

Matrices, vectors, view/model transforms, target point smoothing.

### `math/cubismmath.ts`
Exports: class `CubismMath`; namespace `Live2DCubismFramework`; type `CubismMath`

Common methods:
- `CubismMath.range(value: number, min: number, max: number)` → `number`
- `CubismMath.sin(x: number)` → `number`
- `CubismMath.cos(x: number)` → `number`
- `CubismMath.abs(x: number)` → `number`
- `CubismMath.sqrt(x: number)` → `number`
- `CubismMath.cbrt(x: number)` → `number`
- `CubismMath.getEasingSine(value: number)` → `number`
- `CubismMath.max(left: number, right: number)` → `number`
- `CubismMath.min(left: number, right: number)` → `number`
- `CubismMath.degreesToRadian(degrees: number)` → `number`
- `CubismMath.radianToDegrees(radian: number)` → `number`
- `CubismMath.directionToRadian(from: CubismVector2, to: CubismVector2)` → `number`
- `CubismMath.directionToDegrees(from: CubismVector2, to: CubismVector2)` → `number`
- `CubismMath.radianToDirection(totalAngle: number)` → `CubismVector2`
- `CubismMath.quadraticEquation(a: number, b: number, c: number)` → `number`
- `CubismMath.mod(dividend: number, divisor: number)` → `number`

### `math/cubismmatrix44.ts`
Exports: class `CubismMatrix44`; namespace `Live2DCubismFramework`; type `CubismMatrix44`

Common methods:
- `CubismMatrix44.loadIdentity()` → `void`
- `CubismMatrix44.setMatrix(tr: Float32Array)` → `void`
- `CubismMatrix44.getArray()` → `Float32Array`
- `CubismMatrix44.getScaleX()` → `number`
- `CubismMatrix44.getScaleY()` → `number`
- `CubismMatrix44.getTranslateX()` → `number`
- `CubismMatrix44.getTranslateY()` → `number`
- `CubismMatrix44.transformX(src: number)` → `number`
- `CubismMatrix44.transformY(src: number)` → `number`
- `CubismMatrix44.invertTransformX(src: number)` → `number`
- `CubismMatrix44.invertTransformY(src: number)` → `number`
- `CubismMatrix44.translateRelative(x: number, y: number)` → `void`
- `CubismMatrix44.translate(x: number, y: number)` → `void`
- `CubismMatrix44.translateX(x: number)` → `void`
- `CubismMatrix44.translateY(y: number)` → `void`
- `CubismMatrix44.scaleRelative(x: number, y: number)` → `void`
- `CubismMatrix44.scale(x: number, y: number)` → `void`
- `CubismMatrix44.multiplyByMatrix(m: CubismMatrix44)` → `void`
- `CubismMatrix44.getInvert()` → `CubismMatrix44`
- `CubismMatrix44.clone()` → `CubismMatrix44`

### `math/cubismmodelmatrix.ts`
Exports: class `CubismModelMatrix`; namespace `Live2DCubismFramework`; type `CubismModelMatrix`

Common methods:
- `CubismModelMatrix.setWidth(w: number)` → `void`
- `CubismModelMatrix.setHeight(h: number)` → `void`
- `CubismModelMatrix.setPosition(x: number, y: number)` → `void`
- `CubismModelMatrix.setCenterPosition(x: number, y: number)`
- `CubismModelMatrix.top(y: number)` → `void`
- `CubismModelMatrix.bottom(y: number)`
- `CubismModelMatrix.left(x: number)` → `void`
- `CubismModelMatrix.right(x: number)` → `void`
- `CubismModelMatrix.centerX(x: number)` → `void`
- `CubismModelMatrix.setX(x: number)` → `void`
- `CubismModelMatrix.centerY(y: number)` → `void`
- `CubismModelMatrix.setY(y: number)` → `void`
- `CubismModelMatrix.setupFromLayout(layout: Map<string, number>)` → `void`

### `math/cubismtargetpoint.ts`
Exports: class `CubismTargetPoint`; namespace `Live2DCubismFramework`; type `CubismTargetPoint`

Common methods:
- `CubismTargetPoint.update(deltaTimeSeconds: number)` → `void`
- `CubismTargetPoint.getX()` → `number`
- `CubismTargetPoint.getY()` → `number`
- `CubismTargetPoint.set(x: number, y: number)` → `void`

### `math/cubismvector2.ts`
Exports: class `CubismVector2`; namespace `Live2DCubismFramework`; type `CubismVector2`

Common methods:
- `CubismVector2.add(vector2: CubismVector2)` → `CubismVector2`
- `CubismVector2.substract(vector2: CubismVector2)` → `CubismVector2`
- `CubismVector2.multiply(vector2: CubismVector2)` → `CubismVector2`
- `CubismVector2.multiplyByScaler(scalar: number)` → `CubismVector2`
- `CubismVector2.division(vector2: CubismVector2)` → `CubismVector2`
- `CubismVector2.divisionByScalar(scalar: number)` → `CubismVector2`
- `CubismVector2.getLength()` → `number`
- `CubismVector2.getDistanceWith(a: CubismVector2)` → `number`
- `CubismVector2.dot(a: CubismVector2)` → `number`
- `CubismVector2.normalize()` → `void`
- `CubismVector2.isEqual(rhs: CubismVector2)` → `boolean`
- `CubismVector2.isNotEqual(rhs: CubismVector2)` → `boolean`

### `math/cubismviewmatrix.ts`
Exports: class `CubismViewMatrix`; namespace `Live2DCubismFramework`; type `CubismViewMatrix`

Common methods:
- `CubismViewMatrix.adjustTranslate(x: number, y: number)` → `void`
- `CubismViewMatrix.adjustScale(cx: number, cy: number, scale: number)` → `void`
- `CubismViewMatrix.setMaxScale(maxScale: number)` → `void`
- `CubismViewMatrix.setMinScale(minScale: number)` → `void`
- `CubismViewMatrix.getMaxScale()` → `number`
- `CubismViewMatrix.getMinScale()` → `number`
- `CubismViewMatrix.isMaxScale()` → `boolean`
- `CubismViewMatrix.isMinScale()` → `boolean`
- `CubismViewMatrix.getScreenLeft()` → `number`
- `CubismViewMatrix.getScreenRight()` → `number`
- `CubismViewMatrix.getScreenBottom()` → `number`
- `CubismViewMatrix.getScreenTop()` → `number`
- `CubismViewMatrix.getMaxLeft()` → `number`
- `CubismViewMatrix.getMaxRight()` → `number`
- `CubismViewMatrix.getMaxBottom()` → `number`
- `CubismViewMatrix.getMaxTop()` → `number`

## model

MOC/model loading, parameter/part/drawable access, user model wrapper.

### `model/cubismmoc.ts`
Exports: class `CubismMoc`; namespace `Live2DCubismFramework`; type `CubismMoc`

Common methods:
- `CubismMoc.release()` → `void`
- `CubismMoc.getLatestMocVersion()` → `number`
- `CubismMoc.getMocVersion()` → `number`

### `model/cubismmodel.ts`
Exports: enum `CubismColorBlend`; enum `CubismAlphaBlend`; enum `CubismModelObjectType`; class `ParameterRepeatData`; class `DrawableCullingData`; class `CullingData`; class `PartChildDrawObjects`; class `CubismModelObjectInfo`; class `CubismModelPartInfo`; class `CubismModel`; namespace `Live2DCubismFramework`; type `CubismModel`

Common methods:
- `CubismModelPartInfo.getChildObjectCount()` → `number`
- `CubismModel.update()` → `void`
- `CubismModel.getPixelsPerUnit()` → `number`
- `CubismModel.getCanvasWidth()` → `number`
- `CubismModel.getCanvasHeight()` → `number`
- `CubismModel.saveParameters()` → `void`
- `CubismModel.getOverrideMultiplyAndScreenColor()` → `CubismModelMultiplyAndScreenColor`
- `CubismModel.getOverrideFlagForModelParameterRepeat()` → `boolean`
- `CubismModel.setOverrideFlagForModelParameterRepeat(isRepeat: boolean)` → `void`
- `CubismModel.getOverrideFlagForParameterRepeat(parameterIndex: number)` → `boolean`
- `CubismModel.getRepeatFlagForParameterRepeat(parameterIndex: number)` → `boolean`
- `CubismModel.getDrawableCulling(drawableIndex: number)` → `boolean`
- `CubismModel.setDrawableCulling(drawableIndex: number, isCulling: boolean)` → `void`
- `CubismModel.getOffscreenCulling(offscreenIndex: number)` → `boolean`
- `CubismModel.setOffscreenCulling(offscreenIndex: number, isCulling: boolean)` → `void`
- `CubismModel.getOverrideFlagForModelCullings()` → `boolean`
- `CubismModel.setOverrideFlagForModelCullings(isOverriddenCullings: boolean)` → `void`
- `CubismModel.getOverrideFlagForDrawableCullings(drawableIndex: number)` → `boolean`
- `CubismModel.getOverrideFlagForOffscreenCullings(offscreenIndex: number)` → `boolean`
- `CubismModel.getModelOapcity()` → `number`
- `CubismModel.setModelOapcity(value: number)`
- `CubismModel.getModel()` → `Live2DCubismCore.Model`
- `CubismModel.getPartIndex(partId: CubismIdHandle)` → `number`
- `CubismModel.getPartId(partIndex: number)` → `CubismIdHandle`
- `CubismModel.getPartCount()` → `number`
- `CubismModel.getPartOffscreenIndices()` → `Int32Array`
- `CubismModel.getPartParentPartIndices()` → `Int32Array`
- `CubismModel.setPartOpacityByIndex(partIndex: number, opacity: number)` → `void`
- `CubismModel.setPartOpacityById(partId: CubismIdHandle, opacity: number)` → `void`
- `CubismModel.getPartOpacityByIndex(partIndex: number)` → `number`
- `CubismModel.getPartOpacityById(partId: CubismIdHandle)` → `number`
- `CubismModel.getParameterIndex(parameterId: CubismIdHandle)` → `number`
- `CubismModel.getParameterCount()` → `number`
- `CubismModel.getParameterMaximumValue(parameterIndex: number)` → `number`
- `CubismModel.getParameterMinimumValue(parameterIndex: number)` → `number`
- ... 48 more; open the source file for full list

### `model/cubismmodelmultiplyandscreencolor.ts`
Exports: class `ColorData`; class `CubismModelMultiplyAndScreenColor`

Common methods:
- `CubismModelMultiplyAndScreenColor.setMultiplyColorEnabled(value: boolean)` → `void`
- `CubismModelMultiplyAndScreenColor.getMultiplyColorEnabled()` → `boolean`
- `CubismModelMultiplyAndScreenColor.setScreenColorEnabled(value: boolean)` → `void`
- `CubismModelMultiplyAndScreenColor.getScreenColorEnabled()` → `boolean`
- `CubismModelMultiplyAndScreenColor.setPartMultiplyColorEnabled(partIndex: number, value: boolean)` → `void`
- `CubismModelMultiplyAndScreenColor.getPartMultiplyColorEnabled(partIndex: number)` → `boolean`
- `CubismModelMultiplyAndScreenColor.setPartScreenColorEnabled(partIndex: number, value: boolean)` → `void`
- `CubismModelMultiplyAndScreenColor.getPartScreenColorEnabled(partIndex: number)` → `boolean`
- `CubismModelMultiplyAndScreenColor.getPartMultiplyColor(partIndex: number)` → `CubismTextureColor`
- `CubismModelMultiplyAndScreenColor.getPartScreenColor(partIndex: number)` → `CubismTextureColor`
- `CubismModelMultiplyAndScreenColor.getDrawableMultiplyColorEnabled(drawableIndex: number)` → `boolean`
- `CubismModelMultiplyAndScreenColor.getDrawableScreenColorEnabled(drawableIndex: number)` → `boolean`
- `CubismModelMultiplyAndScreenColor.getDrawableMultiplyColor(drawableIndex: number)` → `CubismTextureColor`
- `CubismModelMultiplyAndScreenColor.getDrawableScreenColor(drawableIndex: number)` → `CubismTextureColor`
- `CubismModelMultiplyAndScreenColor.getOffscreenMultiplyColorEnabled(offscreenIndex: number)` → `boolean`
- `CubismModelMultiplyAndScreenColor.getOffscreenScreenColorEnabled(offscreenIndex: number)` → `boolean`
- `CubismModelMultiplyAndScreenColor.getOffscreenMultiplyColor(offscreenIndex: number)` → `CubismTextureColor`
- `CubismModelMultiplyAndScreenColor.getOffscreenScreenColor(offscreenIndex: number)` → `CubismTextureColor`

### `model/cubismmodeluserdata.ts`
Exports: class `CubismModelUserDataNode`; class `CubismModelUserData`; namespace `Live2DCubismFramework`; type `CubismModelUserData`; type `CubismModelUserDataNode`

Common methods:
- `CubismModelUserData.getArtMeshUserDatas()` → `Array<CubismModelUserDataNode>`
- `CubismModelUserData.parseUserData(buffer: ArrayBuffer, size: number)` → `void`
- `CubismModelUserData.release()` → `void`

### `model/cubismmodeluserdatajson.ts`
Exports: class `CubismModelUserDataJson`; namespace `Live2DCubismFramework`; type `CubismModelUserDataJson`

Common methods:
- `CubismModelUserDataJson.release()` → `void`
- `CubismModelUserDataJson.getUserDataCount()` → `number`
- `CubismModelUserDataJson.getTotalUserDataSize()` → `number`
- `CubismModelUserDataJson.getUserDataTargetType(i: number)` → `string`
- `CubismModelUserDataJson.getUserDataId(i: number)` → `CubismIdHandle`
- `CubismModelUserDataJson.getUserDataValue(i: number)` → `string`

### `model/cubismusermodel.ts`
Exports: class `CubismUserModel`; namespace `Live2DCubismFramework`; type `CubismUserModel`

Common methods:
- `CubismUserModel.isInitialized()` → `boolean`
- `CubismUserModel.setInitialized(v: boolean)` → `void`
- `CubismUserModel.isUpdating()` → `boolean`
- `CubismUserModel.setUpdating(v: boolean)` → `void`
- `CubismUserModel.setDragging(x: number, y: number)` → `void`
- `CubismUserModel.getModelMatrix()` → `CubismModelMatrix`
- `CubismUserModel.setRenderTargetSize(width: number, height: number)` → `void`
- `CubismUserModel.setOpacity(a: number)` → `void`
- `CubismUserModel.getOpacity()` → `number`
- `CubismUserModel.loadModel(buffer: ArrayBuffer, shouldCheckMocConsistency = false)`
- `CubismUserModel.loadPose(buffer: ArrayBuffer, size: number)` → `void`
- `CubismUserModel.loadUserData(buffer: ArrayBuffer, size: number)` → `void`
- `CubismUserModel.loadPhysics(buffer: ArrayBuffer, size: number)` → `void`
- `CubismUserModel.getModel()` → `CubismModel`
- `CubismUserModel.getMocVersionFromBuffer(mocBytes: ArrayBuffer)` → `number`
- `CubismUserModel.getRenderer()` → `CubismRenderer_WebGL`
- `CubismUserModel.deleteRenderer()` → `void`
- `CubismUserModel.motionEventFired(eventValue: string)` → `void`
- `CubismUserModel.release()`

## motion

Motion playback, queues, expressions, update scheduler, motion events.

### `motion/acubismmotion.ts`
Exports: type `BeganMotionCallback`; type `FinishedMotionCallback`; class `ACubismMotion`; namespace `Live2DCubismFramework`; type `ACubismMotion`; type `BeganMotionCallback`; type `FinishedMotionCallback`

Common methods:
- `ACubismMotion.release()` → `void`
- `ACubismMotion.setFadeInTime(fadeInSeconds: number)` → `void`
- `ACubismMotion.setFadeOutTime(fadeOutSeconds: number)` → `void`
- `ACubismMotion.getFadeOutTime()` → `number`
- `ACubismMotion.getFadeInTime()` → `number`
- `ACubismMotion.setWeight(weight: number)` → `void`
- `ACubismMotion.getWeight()` → `number`
- `ACubismMotion.getDuration()` → `number`
- `ACubismMotion.getLoopDuration()` → `number`
- `ACubismMotion.setOffsetTime(offsetSeconds: number)` → `void`
- `ACubismMotion.setLoop(loop: boolean)` → `void`
- `ACubismMotion.getLoop()` → `boolean`
- `ACubismMotion.setLoopFadeIn(loopFadeIn: boolean)`
- `ACubismMotion.getLoopFadeIn()` → `boolean`
- `ACubismMotion.isExistModelOpacity()` → `boolean`
- `ACubismMotion.getModelOpacityIndex()` → `number`
- `ACubismMotion.getModelOpacityId(index: number)` → `CubismIdHandle`
- `ACubismMotion.getModelOpacityValue()` → `number`
- `ACubismMotion.adjustEndTime(motionQueueEntry: CubismMotionQueueEntry)`

### `motion/cubismbreathupdater.ts`
Exports: class `CubismBreathUpdater`; namespace `Live2DCubismFramework`; type `CubismBreathUpdater`

### `motion/cubismexpressionmotion.ts`
Exports: class `CubismExpressionMotion`; enum `ExpressionBlendType`; class `ExpressionParameter`; namespace `Live2DCubismFramework`; type `CubismExpressionMotion`; type `ExpressionBlendType`; type `ExpressionParameter`

Common methods:
- `CubismExpressionMotion.getExpressionParameters()`
- `CubismExpressionMotion.parse(buffer: ArrayBuffer, size: number)`

### `motion/cubismexpressionmotionmanager.ts`
Exports: class `ExpressionParameterValue`; class `CubismExpressionMotionManager`; namespace `Live2DCubismFramework`; type `CubismExpressionMotionManager`

Common methods:
- `CubismExpressionMotionManager.release()` → `void`
- `CubismExpressionMotionManager.getFadeWeight(index: number)` → `number`
- `CubismExpressionMotionManager.setFadeWeight(index: number, expressionFadeWeight: number)` → `void`
- `CubismExpressionMotionManager.updateMotion(model: CubismModel, deltaTimeSeconds: number)` → `boolean`

### `motion/cubismexpressionupdater.ts`
Exports: class `CubismExpressionUpdater`; namespace `Live2DCubismFramework`; type `CubismExpressionUpdater`

### `motion/cubismeyeblinkupdater.ts`
Exports: class `CubismEyeBlinkUpdater`; namespace `Live2DCubismFramework`; type `CubismEyeBlinkUpdater`

### `motion/cubismlipsyncupdater.ts`
Exports: class `CubismLipSyncUpdater`; namespace `Live2DCubismFramework`; type `CubismLipSyncUpdater`

### `motion/cubismlookupdater.ts`
Exports: class `CubismLookUpdater`; namespace `Live2DCubismFramework`; type `CubismLookUpdater`

### `motion/cubismmotion.ts`
Exports: enum `MotionBehavior`; class `CubismMotion`; namespace `Live2DCubismFramework`; type `CubismMotion`

Common methods:
- `CubismMotion.setMotionBehavior(motionBehavior: MotionBehavior)`
- `CubismMotion.getMotionBehavior()` → `MotionBehavior`
- `CubismMotion.getDuration()` → `number`
- `CubismMotion.getLoopDuration()` → `number`
- `CubismMotion.getParameterFadeInTime(parameterId: CubismIdHandle)` → `number`
- `CubismMotion.getParameterFadeOutTime(parameterId: CubismIdHandle)` → `number`
- `CubismMotion.release()` → `void`
- `CubismMotion.isExistModelOpacity()` → `boolean`
- `CubismMotion.getModelOpacityIndex()` → `number`
- `CubismMotion.getModelOpacityId(index: number)` → `CubismIdHandle`
- `CubismMotion.getModelOpacityValue()` → `number`
- `CubismMotion.setDebugMode(debugMode: boolean)` → `void`

### `motion/cubismmotioninternal.ts`
Exports: enum `CubismMotionCurveTarget`; enum `CubismMotionSegmentType`; class `CubismMotionPoint`; interface `csmMotionSegmentEvaluationFunction`; class `CubismMotionSegment`; class `CubismMotionCurve`; class `CubismMotionEvent`; class `CubismMotionData`; namespace `Live2DCubismFramework`; type `CubismMotionCurve`; type `CubismMotionCurveTarget`; type `CubismMotionData`; type `CubismMotionEvent`; type `CubismMotionPoint`; type `CubismMotionSegment`; type `CubismMotionSegmentType`; type `csmMotionSegmentEvaluationFunction`

### `motion/cubismmotionjson.ts`
Exports: class `CubismMotionJson`; enum `EvaluationOptionFlag`; namespace `Live2DCubismFramework`; type `CubismMotionJson`

Common methods:
- `CubismMotionJson.release()` → `void`
- `CubismMotionJson.getMotionDuration()` → `number`
- `CubismMotionJson.isMotionLoop()` → `boolean`
- `CubismMotionJson.getEvaluationOptionFlag(flagType: EvaluationOptionFlag)` → `boolean`
- `CubismMotionJson.getMotionCurveCount()` → `number`
- `CubismMotionJson.getMotionFps()` → `number`
- `CubismMotionJson.getMotionTotalSegmentCount()` → `number`
- `CubismMotionJson.getMotionTotalPointCount()` → `number`
- `CubismMotionJson.isExistMotionFadeInTime()` → `boolean`
- `CubismMotionJson.isExistMotionFadeOutTime()` → `boolean`
- `CubismMotionJson.getMotionFadeInTime()` → `number`
- `CubismMotionJson.getMotionFadeOutTime()` → `number`
- `CubismMotionJson.getMotionCurveTarget(curveIndex: number)` → `string`
- `CubismMotionJson.getMotionCurveId(curveIndex: number)` → `CubismIdHandle`
- `CubismMotionJson.isExistMotionCurveFadeInTime(curveIndex: number)` → `boolean`
- `CubismMotionJson.isExistMotionCurveFadeOutTime(curveIndex: number)` → `boolean`
- `CubismMotionJson.getMotionCurveFadeInTime(curveIndex: number)` → `number`
- `CubismMotionJson.getMotionCurveFadeOutTime(curveIndex: number)` → `number`
- `CubismMotionJson.getMotionCurveSegmentCount(curveIndex: number)` → `number`
- `CubismMotionJson.getEventCount()` → `number`
- `CubismMotionJson.getTotalEventValueSize()` → `number`
- `CubismMotionJson.getEventTime(userDataIndex: number)` → `number`
- `CubismMotionJson.getEventValue(userDataIndex: number)` → `string`

### `motion/cubismmotionmanager.ts`
Exports: class `CubismMotionManager`; namespace `Live2DCubismFramework`; type `CubismMotionManager`

Common methods:
- `CubismMotionManager.getCurrentPriority()` → `number`
- `CubismMotionManager.getReservePriority()` → `number`
- `CubismMotionManager.setReservePriority(val: number)` → `void`
- `CubismMotionManager.updateMotion(model: CubismModel, deltaTimeSeconds: number)` → `boolean`
- `CubismMotionManager.reserveMotion(priority: number)` → `boolean`

### `motion/cubismmotionqueueentry.ts`
Exports: class `CubismMotionQueueEntry`; namespace `Live2DCubismFramework`; type `CubismMotionQueueEntry`

Common methods:
- `CubismMotionQueueEntry.release()` → `void`
- `CubismMotionQueueEntry.setFadeOut(fadeOutSeconds: number)` → `void`
- `CubismMotionQueueEntry.startFadeOut(fadeOutSeconds: number, userTimeSeconds: number)` → `void`
- `CubismMotionQueueEntry.isFinished()` → `boolean`
- `CubismMotionQueueEntry.isStarted()` → `boolean`
- `CubismMotionQueueEntry.getStartTime()` → `number`
- `CubismMotionQueueEntry.getFadeInStartTime()` → `number`
- `CubismMotionQueueEntry.getEndTime()` → `number`
- `CubismMotionQueueEntry.setStartTime(startTime: number)` → `void`
- `CubismMotionQueueEntry.setFadeInStartTime(startTime: number)` → `void`
- `CubismMotionQueueEntry.setEndTime(endTime: number)` → `void`
- `CubismMotionQueueEntry.setIsFinished(f: boolean)` → `void`
- `CubismMotionQueueEntry.setIsStarted(f: boolean)` → `void`
- `CubismMotionQueueEntry.isAvailable()` → `boolean`
- `CubismMotionQueueEntry.setIsAvailable(v: boolean)` → `void`
- `CubismMotionQueueEntry.setState(timeSeconds: number, weight: number)` → `void`
- `CubismMotionQueueEntry.getStateTime()` → `number`
- `CubismMotionQueueEntry.getStateWeight()` → `number`
- `CubismMotionQueueEntry.getLastCheckEventSeconds()` → `number`
- `CubismMotionQueueEntry.setLastCheckEventSeconds(checkSeconds: number)` → `void`
- `CubismMotionQueueEntry.isTriggeredFadeOut()` → `boolean`
- `CubismMotionQueueEntry.getFadeOutSeconds()` → `number`
- `CubismMotionQueueEntry.getCubismMotion()` → `ACubismMotion`

### `motion/cubismmotionqueuemanager.ts`
Exports: class `CubismMotionQueueManager`; interface `CubismMotionEventFunction`; namespace `Live2DCubismFramework`; type `CubismMotionQueueManager`; type `CubismMotionQueueEntryHandle`; type `CubismMotionEventFunction`

Common methods:
- `CubismMotionQueueManager.release()` → `void`
- `CubismMotionQueueManager.isFinished()` → `boolean`
- `CubismMotionQueueManager.stopAllMotions()` → `void`
- `CubismMotionQueueManager.getCubismMotionQueueEntries()` → `Array<CubismMotionQueueEntry>`
- `CubismMotionQueueManager.doUpdateMotion(model: CubismModel, userTimeSeconds: number)` → `boolean`

### `motion/cubismphysicsupdater.ts`
Exports: class `CubismPhysicsUpdater`; namespace `Live2DCubismFramework`; type `CubismPhysicsUpdater`

### `motion/cubismposeupdater.ts`
Exports: class `CubismPoseUpdater`; namespace `Live2DCubismFramework`; type `CubismPoseUpdater`

### `motion/cubismupdatescheduler.ts`
Exports: class `CubismUpdateScheduler`; namespace `Live2DCubismFramework`; type `CubismUpdateScheduler`

Common methods:
- `CubismUpdateScheduler.release()` → `void`
- `CubismUpdateScheduler.addUpdatableList(updatable: ICubismUpdater)` → `void`
- `CubismUpdateScheduler.removeUpdatableList(updatable: ICubismUpdater)` → `boolean`
- `CubismUpdateScheduler.sortUpdatableList()` → `void`
- `CubismUpdateScheduler.onLateUpdate(model: CubismModel, deltaTimeSeconds: number)` → `void`
- `CubismUpdateScheduler.getUpdatableCount()` → `number`
- `CubismUpdateScheduler.getUpdatable(index: number)` → `ICubismUpdater | null`
- `CubismUpdateScheduler.hasUpdatable(updatable: ICubismUpdater)` → `boolean`
- `CubismUpdateScheduler.clearUpdatableList()` → `void`
- `CubismUpdateScheduler.onUpdaterChanged(updater: ICubismUpdater)` → `void`

### `motion/icubismupdater.ts`
Exports: interface `ICubismUpdaterChangeListener`; enum `CubismUpdateOrder`; class `ICubismUpdater`; namespace `Live2DCubismFramework`; type `ICubismUpdater`; type `ICubismUpdaterChangeListener`

Common methods:
- `ICubismUpdater.sortFunction(left: ICubismUpdater, right: ICubismUpdater)` → `number`

### `motion/iparameterprovider.ts`
Exports: class `IParameterProvider`; namespace `Live2DCubismFramework`; type `IParameterProvider`

## physics

Physics JSON parsing and parameter evaluation/interpolation.

### `physics/cubismphysics.ts`
Exports: class `CubismPhysics`; class `Options`; class `PhysicsOutput`; namespace `Live2DCubismFramework`; type `CubismPhysics`; type `Options`

Common methods:
- `CubismPhysics.parse(physicsJson: ArrayBuffer, size: number)` → `void`
- `CubismPhysics.stabilization(model: CubismModel)` → `void`
- `CubismPhysics.evaluate(model: CubismModel, deltaTimeSeconds: number)` → `void`
- `CubismPhysics.interpolate(model: CubismModel, weight: number)` → `void`
- `CubismPhysics.setOptions(options: Options)` → `void`
- `CubismPhysics.getOption()` → `Options`
- `CubismPhysics.release()` → `void`
- `CubismPhysics.initialize()` → `void`

### `physics/cubismphysicsinternal.ts`
Exports: enum `CubismPhysicsTargetType`; enum `CubismPhysicsSource`; class `PhysicsJsonEffectiveForces`; class `CubismPhysicsParameter`; class `CubismPhysicsNormalization`; class `CubismPhysicsParticle`; class `CubismPhysicsSubRig`; interface `normalizedPhysicsParameterValueGetter`; interface `physicsValueGetter`; interface `physicsScaleGetter`; class `CubismPhysicsInput`; class `CubismPhysicsOutput`; class `CubismPhysicsRig`; namespace `Live2DCubismFramework`; type `CubismPhysicsInput`; type `CubismPhysicsNormalization`; type `CubismPhysicsOutput`; type `CubismPhysicsParameter`; type `CubismPhysicsParticle`; type `CubismPhysicsRig`; type `CubismPhysicsSource`; type `CubismPhysicsSubRig`; type `CubismPhysicsTargetType`; type `PhysicsJsonEffectiveForces`; type `normalizedPhysicsParameterValueGetter`; type `physicsScaleGetter`; type `physicsValueGetter`

### `physics/cubismphysicsjson.ts`
Exports: class `CubismPhysicsJson`; namespace `Live2DCubismFramework`; type `CubismPhysicsJson`

Common methods:
- `CubismPhysicsJson.release()` → `void`
- `CubismPhysicsJson.getGravity()` → `CubismVector2`
- `CubismPhysicsJson.getWind()` → `CubismVector2`
- `CubismPhysicsJson.getFps()` → `number`
- `CubismPhysicsJson.getSubRigCount()` → `number`
- `CubismPhysicsJson.getTotalInputCount()` → `number`
- `CubismPhysicsJson.getTotalOutputCount()` → `number`
- `CubismPhysicsJson.getVertexCount()` → `number`
- `CubismPhysicsJson.getInputCount(physicsSettingIndex: number)` → `number`
- `CubismPhysicsJson.getInputType(physicsSettingIndex: number, inputIndex: number)` → `string`
- `CubismPhysicsJson.getOutputCount(physicsSettingIndex: number)` → `number`
- `CubismPhysicsJson.getParticleCount(physicsSettingIndex: number)` → `number`

## rendering

Renderer abstraction, WebGL renderer, clipping, masks, shaders, render targets.

### `rendering/cubismclippingmanager.ts`
Exports: type `ClippingContextConstructor`; interface `ICubismClippingManager`; class `CubismClippingManager`

Common methods:
- `CubismClippingManager.release()` → `void`
- `CubismClippingManager.setupLayoutBounds(usingClipCount: number)` → `void`
- `CubismClippingManager.getClippingContextListForDraw()` → `Array<T_ClippingContext>`
- `CubismClippingManager.getClippingContextListForOffscreen()` → `Array<T_ClippingContext>`
- `CubismClippingManager.getClippingMaskBufferSize()` → `number`
- `CubismClippingManager.getRenderTextureCount()` → `number`
- `CubismClippingManager.getChannelFlagAsColor(channelNo: number)` → `CubismTextureColor`
- `CubismClippingManager.setClippingMaskBufferSize(size: number)` → `void`

### `rendering/cubismoffscreenmanager.ts`
Exports: class `CubismWebGLOffscreenManager`

Common methods:
- `CubismWebGLOffscreenManager.release()` → `void`

### `rendering/cubismoffscreenrendertarget_webgl.ts`
Exports: class `CubismOffscreenRenderTarget_WebGL`

Common methods:
- `CubismOffscreenRenderTarget_WebGL.getUsingRenderTextureState()` → `boolean`
- `CubismOffscreenRenderTarget_WebGL.startUsingRenderTexture()` → `void`
- `CubismOffscreenRenderTarget_WebGL.stopUsingRenderTexture()` → `void`
- `CubismOffscreenRenderTarget_WebGL.setOffscreenIndex(offscreenIndex: number)` → `void`
- `CubismOffscreenRenderTarget_WebGL.getOffscreenIndex()` → `number`
- `CubismOffscreenRenderTarget_WebGL.getOldOffscreen()` → `CubismOffscreenRenderTarget_WebGL`
- `CubismOffscreenRenderTarget_WebGL.getParentPartOffscreen()` → `CubismOffscreenRenderTarget_WebGL`
- `CubismOffscreenRenderTarget_WebGL.release()` → `void`

### `rendering/cubismrenderer.ts`
Exports: class `CubismRenderer`; enum `CubismBlendMode`; enum `DrawableObjectType`; class `CubismTextureColor`; class `CubismClippingContext`; namespace `Live2DCubismFramework`; type `CubismBlendMode`; type `CubismRenderer`; type `CubismTextureColor`

Common methods:
- `CubismRenderer.initialize(model: CubismModel)` → `void`
- `CubismRenderer.drawModel(shaderPath: string = null)` → `void`
- `CubismRenderer.setMvpMatrix(matrix44: CubismMatrix44)` → `void`
- `CubismRenderer.getMvpMatrix()` → `CubismMatrix44`
- `CubismRenderer.getModelColor()` → `CubismTextureColor`
- `CubismRenderer.setIsPremultipliedAlpha(enable: boolean)` → `void`
- `CubismRenderer.isPremultipliedAlpha()` → `boolean`
- `CubismRenderer.setIsCulling(culling: boolean)` → `void`
- `CubismRenderer.isCulling()` → `boolean`
- `CubismRenderer.setAnisotropy(n: number)` → `void`
- `CubismRenderer.getAnisotropy()` → `number`
- `CubismRenderer.getModel()` → `CubismModel`
- `CubismRenderer.useHighPrecisionMask(high: boolean)` → `void`
- `CubismRenderer.isUsingHighPrecisionMask()` → `boolean`
- `CubismRenderer.setRenderTargetSize(width: number, height: number)` → `void`
- `CubismClippingContext.release()` → `void`
- `CubismClippingContext.addClippedDrawable(drawableIndex: number)`
- `CubismClippingContext.addClippedOffscreen(offscreenIndex: number)`

### `rendering/cubismrenderer_webgl.ts`
Exports: class `CubismClippingManager_WebGL`; class `CubismClippingContext_WebGL`; class `CubismRendererProfile_WebGL`; class `CubismRenderer_WebGL`; namespace `Live2DCubismFramework`; type `CubismClippingContext`; type `CubismClippingManager_WebGL`; type `CubismRenderer_WebGL`

Common methods:
- `CubismClippingManager_WebGL.setGL(gl: WebGLRenderingContext)` → `void`
- `CubismClippingManager_WebGL.getClippingMaskCount()` → `number`
- `CubismClippingContext_WebGL.getClippingManager()` → `CubismClippingManager_WebGL`
- `CubismClippingContext_WebGL.setGl(gl: WebGLRenderingContext)` → `void`
- `CubismRendererProfile_WebGL.save()` → `void`
- `CubismRendererProfile_WebGL.restore()` → `void`
- `CubismRendererProfile_WebGL.setGl(gl: WebGLRenderingContext)` → `void`
- `CubismRenderer_WebGL.initialize(model: CubismModel, maskBufferCount = 1)` → `void`
- `CubismRenderer_WebGL.bindTexture(modelTextureNo: number, glTexture: WebGLTexture)` → `void`
- `CubismRenderer_WebGL.getBindedTextures()` → `Map<number, WebGLTexture>`
- `CubismRenderer_WebGL.setClippingMaskBufferSize(size: number)`
- `CubismRenderer_WebGL.getClippingMaskBufferSize()` → `number`
- `CubismRenderer_WebGL.getModelRenderTarget(index: number)` → `CubismRenderTarget_WebGL`
- `CubismRenderer_WebGL.getRenderTextureCount()` → `number`
- `CubismRenderer_WebGL.release()` → `void`
- `CubismRenderer_WebGL.loadShaders(shaderPath: string = null)` → `void`
- `CubismRenderer_WebGL.doDrawModel(shaderPath: string = null)` → `void`
- `CubismRenderer_WebGL.drawObjectLoop(lastFbo: WebGLFramebuffer)` → `void`
- `CubismRenderer_WebGL.drawDrawable(drawableIndex: number, rootFbo: WebGLFramebuffer)` → `void`
- `CubismRenderer_WebGL.drawMeshWebGL(model: Readonly<CubismModel>, index: number)` → `void`
- `CubismRenderer_WebGL.addOffscreen(offscreenIndex: number)` → `void`
- `CubismRenderer_WebGL.drawOffscreen(offscreen: CubismOffscreenRenderTarget_WebGL)` → `void`
- `CubismRenderer_WebGL.saveProfile()` → `void`
- `CubismRenderer_WebGL.restoreProfile()` → `void`
- `CubismRenderer_WebGL.beforeDrawModelRenderTarget()` → `void`
- `CubismRenderer_WebGL.afterDrawModelRenderTarget()` → `void`
- `CubismRenderer_WebGL.setRenderState(fbo: WebGLFramebuffer, viewport: number[])` → `void`
- `CubismRenderer_WebGL.preDraw()` → `void`
- `CubismRenderer_WebGL.getDrawableMaskBuffer(index: number)` → `CubismRenderTarget_WebGL`
- `CubismRenderer_WebGL.setClippingContextBufferForMask(clip: CubismClippingContext_WebGL)`
- `CubismRenderer_WebGL.getClippingContextBufferForMask()` → `CubismClippingContext_WebGL`
- `CubismRenderer_WebGL.getClippingContextBufferForDrawable()` → `CubismClippingContext_WebGL`
- `CubismRenderer_WebGL.getClippingContextBufferForOffscreen()` → `CubismClippingContext_WebGL`
- `CubismRenderer_WebGL.isGeneratingMask()`
- `CubismRenderer_WebGL.startUp(gl: WebGLRenderingContext | WebGL2RenderingContext)` → `void`

### `rendering/cubismrendertarget_webgl.ts`
Exports: class `CubismRenderTarget_WebGL`; namespace `Live2DCubismFramework`; type `CubismOffscreenSurface_WebGL`

Common methods:
- `CubismRenderTarget_WebGL.beginDraw(restoreFbo: WebGLFramebuffer = null)` → `void`
- `CubismRenderTarget_WebGL.endDraw()` → `void`
- `CubismRenderTarget_WebGL.clear(r: number, g: number, b: number, a: number)` → `void`
- `CubismRenderTarget_WebGL.destroyRenderTarget()` → `void`
- `CubismRenderTarget_WebGL.getGL()` → `WebGLRenderingContext | WebGL2RenderingContext`
- `CubismRenderTarget_WebGL.getRenderTexture()` → `WebGLFramebuffer`
- `CubismRenderTarget_WebGL.getColorBuffer()` → `WebGLTexture`
- `CubismRenderTarget_WebGL.getBufferWidth()` → `number`
- `CubismRenderTarget_WebGL.getBufferHeight()` → `number`
- `CubismRenderTarget_WebGL.isValid()` → `boolean`
- `CubismRenderTarget_WebGL.getOldFBO()` → `WebGLFramebuffer`

### `rendering/cubismshader_webgl.ts`
Exports: class `CubismShader_WebGL`; class `CubismShaderManager_WebGL`; class `CubismShaderSet`; enum `ShaderNames`; enum `ShaderType`; namespace `Live2DCubismFramework`; type `CubismShaderSet`; type `CubismShader_WebGL`; type `CubismShaderManager_WebGL`; type `ShaderNames`

Common methods:
- `CubismShader_WebGL.release()` → `void`
- `CubismShader_WebGL.releaseShaderProgram()` → `void`
- `CubismShader_WebGL.generateShaders()` → `void`
- `CubismShader_WebGL.registerShader()` → `void`
- `CubismShader_WebGL.registerBlendShader()` → `void`
- `CubismShader_WebGL.setGl(gl: WebGLRenderingContext | WebGL2RenderingContext)` → `void`
- `CubismShader_WebGL.setShaderPath(shaderPath: string)` → `void`
- `CubismShader_WebGL.getShaderPath()` → `string`
- `CubismShaderManager_WebGL.release()` → `void`
- `CubismShaderManager_WebGL.getShader(gl: WebGLRenderingContext)` → `CubismShader_WebGL`
- `CubismShaderManager_WebGL.setGlContext(gl: WebGLRenderingContext)` → `void`

## root

Framework startup, model setting JSON, default parameter IDs, and base interfaces.

### `cubismdefaultparameterid.ts`
Exports: namespace `Live2DCubismFramework`

### `cubismmodelsettingjson.ts`
Exports: enum `FrequestNode`; class `CubismModelSettingJson`; namespace `Live2DCubismFramework`; type `CubismModelSettingJson`; type `FrequestNode`

Common methods:
- `CubismModelSettingJson.release()` → `void`
- `CubismModelSettingJson.getJson()` → `CubismJson`
- `CubismModelSettingJson.getModelFileName()` → `string`
- `CubismModelSettingJson.getTextureCount()` → `number`
- `CubismModelSettingJson.getTextureDirectory()` → `string`
- `CubismModelSettingJson.getTextureFileName(index: number)` → `string`
- `CubismModelSettingJson.getHitAreasCount()` → `number`
- `CubismModelSettingJson.getHitAreaId(index: number)` → `CubismIdHandle`
- `CubismModelSettingJson.getHitAreaName(index: number)` → `string`
- `CubismModelSettingJson.getPhysicsFileName()` → `string`
- `CubismModelSettingJson.getPoseFileName()` → `string`
- `CubismModelSettingJson.getExpressionCount()` → `number`
- `CubismModelSettingJson.getExpressionName(index: number)` → `string`
- `CubismModelSettingJson.getExpressionFileName(index: number)` → `string`
- `CubismModelSettingJson.getMotionGroupCount()` → `number`
- `CubismModelSettingJson.getMotionGroupName(index: number)` → `string`
- `CubismModelSettingJson.getMotionCount(groupName: string)` → `number`
- `CubismModelSettingJson.getMotionFileName(groupName: string, index: number)` → `string`
- `CubismModelSettingJson.getMotionSoundFileName(groupName: string, index: number)` → `string`
- `CubismModelSettingJson.getMotionFadeInTimeValue(groupName: string, index: number)` → `number`
- `CubismModelSettingJson.getMotionFadeOutTimeValue(groupName: string, index: number)` → `number`
- `CubismModelSettingJson.getUserDataFile()` → `string`
- `CubismModelSettingJson.getLayoutMap(outLayoutMap: Map<string, number>)` → `boolean`
- `CubismModelSettingJson.getEyeBlinkParameterCount()` → `number`
- `CubismModelSettingJson.getEyeBlinkParameterId(index: number)` → `CubismIdHandle`
- `CubismModelSettingJson.getLipSyncParameterCount()` → `number`
- `CubismModelSettingJson.getLipSyncParameterId(index: number)` → `CubismIdHandle`
- `CubismModelSettingJson.isExistModelFile()` → `boolean`
- `CubismModelSettingJson.isExistTextureFiles()` → `boolean`
- `CubismModelSettingJson.isExistHitAreas()` → `boolean`
- `CubismModelSettingJson.isExistPhysicsFile()` → `boolean`
- `CubismModelSettingJson.isExistPoseFile()` → `boolean`
- `CubismModelSettingJson.isExistExpressionFile()` → `boolean`
- `CubismModelSettingJson.isExistMotionGroups()` → `boolean`
- `CubismModelSettingJson.isExistMotionGroupName(groupName: string)` → `boolean`
- ... 6 more; open the source file for full list

### `icubismallcator.ts`
Exports: class `ICubismAllocator`; namespace `Live2DCubismFramework`; type `ICubismAllocator`

### `icubismmodelsetting.ts`
Exports: class `ICubismModelSetting`; namespace `Live2DCubismFramework`; type `ICubismModelSetting`

### `live2dcubismframework.ts`
Exports: function `strtod`; function `csmDelete`; class `CubismFramework`; class `Option`; enum `LogLevel`; namespace `Live2DCubismFramework`; type `CubismFramework`

## type

Small shared value types.

### `type/csmrectf.ts`
Exports: class `csmRect`; namespace `Live2DCubismFramework`; type `csmRect`

Common methods:
- `csmRect.getCenterX()` → `number`
- `csmRect.getCenterY()` → `number`
- `csmRect.getRight()` → `number`
- `csmRect.getBottom()` → `number`
- `csmRect.setRect(r: csmRect)` → `void`
- `csmRect.expand(w: number, h: number)`

## utils

Debug logging, JSON parser, strings, array helpers.

### `utils/cubismarrayutils.ts`
Exports: function `updateSize`

### `utils/cubismdebug.ts`
Exports: class `CubismDebug`; namespace `Live2DCubismFramework`; type `CubismDebug`

### `utils/cubismjson.ts`
Exports: class `Value`; class `CubismJson`; class `JsonFloat`; class `JsonBoolean`; class `JsonString`; class `JsonError`; class `JsonNullvalue`; class `JsonArray`; class `JsonMap`; namespace `Live2DCubismFramework`; type `CubismJson`; type `JsonArray`; type `JsonBoolean`; type `JsonError`; type `JsonFloat`; type `JsonMap`; type `JsonNullvalue`; type `JsonString`; type `Value`

Common methods:
- `Value.getRawString(defaultValue?: string, indent?: string)` → `string`
- `Value.toInt(defaultValue = 0)` → `number`
- `Value.toFloat(defaultValue = 0)` → `number`
- `Value.toBoolean(defaultValue = false)` → `boolean`
- `Value.getSize()` → `number`
- `Value.getArray(defaultValue: Value[] = null)` → `Value[]`
- `Value.getVector(defaultValue = new Array<Value>()`
- `Value.getMap(defaultValue?: Map<string, Value>)` → `Map<string, Value>`
- `Value.getValueByIndex(index: number)` → `Value`
- `Value.getValueByString(s: string)` → `Value`
- `Value.getKeys()` → `Array<string>`
- `Value.isError()` → `boolean`
- `Value.isNull()` → `boolean`
- `Value.isBool()` → `boolean`
- `Value.isFloat()` → `boolean`
- `Value.isString()` → `boolean`
- `Value.isArray()` → `boolean`
- `Value.isMap()` → `boolean`
- `Value.equals(value: string)` → `boolean`
- `Value.equals(value: string)` → `boolean`
- `Value.equals(value: number)` → `boolean`
- `Value.equals(value: boolean)` → `boolean`
- `Value.equals(value: any)` → `boolean`
- `Value.isStatic()` → `boolean`
- `Value.setErrorNotForClientCall(errorStr: string)` → `Value`
- `CubismJson.getRoot()` → `Value`
- `CubismJson.getParseError()` → `string`
- `CubismJson.checkEndOfFile()` → `boolean`
- `JsonFloat.isFloat()` → `boolean`
- `JsonFloat.getString(defaultValue: string, indent: string)` → `string`
- `JsonFloat.toInt(defaultValue = 0)` → `number`
- `JsonFloat.toFloat(defaultValue = 0.0)` → `number`
- `JsonFloat.equals(value: string)` → `boolean`
- `JsonFloat.equals(value: string)` → `boolean`
- `JsonFloat.equals(value: number)` → `boolean`
- ... 42 more; open the source file for full list

### `utils/cubismjsonextension.ts`
Exports: class `CubismJsonExtension`

Common methods:
- `CubismJsonExtension.parseJsonObject(obj: Value, map: JsonMap)`

### `utils/cubismstring.ts`
Exports: class `CubismString`; namespace `Live2DCubismFramework`; type `CubismString`
