# Official Documentation Index

Use official pages for conceptual behavior and version-sensitive notes. Use bundled SDK source for exact TypeScript signatures.

## Primary Pages

- Cubism SDK for Web overview: `https://docs.live2d.com/zh-CHS/cubism-sdk-manual/cubism-sdk-for-web/`
- Framework startup/dispose for Web: `https://docs.live2d.com/zh-CHS/cubism-sdk-manual/framework-init-close-web/`
- Model loading for Web: `https://docs.live2d.com/zh-CHS/cubism-sdk-manual/model-web/`
- Parameter operations: `https://docs.live2d.com/zh-CHS/cubism-sdk-manual/parameters/`
- Motion: `https://docs.live2d.com/zh-CHS/cubism-sdk-manual/motion/`
- Expression motion: `https://docs.live2d.com/zh-CHS/cubism-sdk-manual/expression/`
- Web-specific notes: `https://docs.live2d.com/zh-CHS/cubism-sdk-manual/point-to-note/`

## Local Summary

- SDK for Web is for using Cubism models in programs and is composed around Core, Framework, and application-side integration.
- Cubism Core is not distributed on GitHub; the local SDK package contains the Core files and license/notice documents.
- Framework startup requires `CubismFramework.startUp(option)` before `CubismFramework.initialize()`.
- `.model3.json` references the model file, textures, physics, pose, motions, expressions, user data, hit areas, and parameter groups.
- For WebGL, renderer texture association is handled by `CubismRenderer_WebGL.bindTexture(modelTextureNo, glTexture)`.
- Parameter operations support set/add/multiply variants by ID or by index; cache indices for hot paths.

## Network Policy

Do not browse for normal API usage. Browse only when the user asks for latest official behavior, a bundled SDK version mismatch is suspected, or the target project uses APIs not present in the bundled source.