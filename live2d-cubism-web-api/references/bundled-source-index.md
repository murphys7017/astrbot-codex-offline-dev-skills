# Bundled Source Index

This skill is API-first. It intentionally excludes official Demo app files and sample model resources.

## Bundled Files

- Framework TypeScript source: `references/offline/CubismSdkForWeb-5-r.5/Framework/src/`
- Framework README/package metadata: `references/offline/CubismSdkForWeb-5-r.5/Framework/`
- Core type declarations: `references/offline/CubismSdkForWeb-5-r.5/Core/live2dcubismcore.d.ts`
- SDK license/notice/readme: `references/offline/CubismSdkForWeb-5-r.5/`

## Not Bundled

- `Samples/TypeScript/Demo/`
- `Samples/Resources/`
- Core JavaScript/WASM runtime binaries except `.d.ts`

## Reason

The skill should teach API usage and API responsibilities. Demo structure and model assets are intentionally excluded to avoid overfitting to the sample application and to reduce license/redistribution risk.