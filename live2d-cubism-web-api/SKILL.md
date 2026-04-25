---
name: live2d-cubism-web-api
description: "API-first guidance for Live2D Cubism SDK for Web development in TypeScript/WebGL desktop or web apps. Use when working with Cubism SDK for Web APIs: CubismFramework startup/dispose, Cubism Core types, CubismUserModel, CubismModel parameters/parts/drawables, model3.json and moc3 loading, WebGL renderer and textures, motions, expressions, physics, eye blink, breath, look, lip sync, pose, asset paths, and Electron/Tauri/WebView integration."
---

# Live2D Cubism Web API

Use this skill as an API map for Live2D Cubism SDK for Web. Prefer API signatures and source comments over sample app structure. Demo code is not a primary reference.

## Workflow

1. Identify the target project stack: browser, Electron, Tauri, WebView, Vite, Webpack, or custom TypeScript build.
2. Start with `references/api-index.md` to find the relevant class/file.
3. Open only the exact bundled source file under `references/offline/CubismSdkForWeb-5-r.5/Framework/src/` for signatures and comments.
4. Use `references/api-usage-guide.md` for lifecycle, model loading, parameter control, rendering, motion, and effects rules.
5. Use `references/desktop-integration-notes.md` only for desktop shell concerns such as resource paths, WebGL context, DPI, transparent windows, and packaging.
6. Do not use SDK demo files or sample resources unless the user explicitly asks for sample migration or debugging against the official sample.

## Source Priority

1. User project code and installed SDK version.
2. Bundled Framework source: `references/offline/CubismSdkForWeb-5-r.5/Framework/src/`.
3. Bundled Core type declarations: `references/offline/CubismSdkForWeb-5-r.5/Core/live2dcubismcore.d.ts`.
4. Generated API router: `references/api-index.md`.
5. Official documentation links in `references/official-doc-index.md` for conceptual checks.

## API Rules

- Call `CubismFramework.startUp(option)` before `CubismFramework.initialize()`; call `CubismFramework.dispose()` when the app no longer uses Framework resources.
- Treat `.model3.json` as the model manifest. Use `CubismModelSettingJson` / `ICubismModelSetting` to discover `.moc3`, textures, motions, expressions, physics, pose, user data, hit areas, and parameter IDs.
- Use `CubismFramework.getIdManager().getId("Param...")` for `CubismIdHandle`; cache parameter indices for high-frequency updates.
- Use `CubismModel` APIs for parameters, parts, drawables, canvas size, opacity, culling, and vertex data.
- Use `CubismRenderer_WebGL` for WebGL-specific texture binding and drawing; bind all model textures before drawing.
- Keep update order explicit: time delta → motion/expression/effects/physics/pose/lip sync → model update → renderer draw.
- Manage WebGL context loss, resize, device pixel ratio, and resource URL resolution explicitly in desktop shells.

## Useful Commands

```powershell
python scripts/generate_api_index.py .
```
