# Desktop Integration Notes

Use this only for Electron, Tauri, WebView, or always-on-top desktop companions.

## Resource Paths

- Do not hard-code development paths such as `C:\Users\...\Samples\Resources`.
- Resolve model URLs through the desktop app asset pipeline: Vite public assets, Electron protocol, Tauri asset URLs, or an app-local static server.
- `.model3.json` references are relative to its directory; preserve model directory structure during packaging.
- Ensure `.moc3`, textures, `.motion3.json`, `.exp3.json`, `.physics3.json`, `.pose3.json`, `.userdata3.json`, and audio files are copied if used.

## WebGL And Window Lifecycle

- Create the WebGL context after the canvas exists and after the desktop window/webview is ready.
- Handle resize and device pixel ratio changes; update canvas pixel size and renderer render target size.
- Listen for `webglcontextlost` and `webglcontextrestored` if the app runs long-lived on desktop.
- Release renderer/model resources when the window closes or model is swapped.

## Transparent Desktop Character Windows

- Use premultiplied alpha consistently between texture upload and renderer state.
- For transparent windows, verify the WebGL canvas clear color and OS/window transparency settings.
- If click-through is needed, separate hit testing from visual transparency; do not rely on canvas alpha alone.

## Performance

- Cache `CubismIdHandle` and parameter indices for per-frame updates.
- Avoid re-fetching `.model3.json`, textures, motions, and expressions after model setup.
- Avoid creating WebGL textures or matrices inside every frame unless necessary.
- Keep render loop tied to `requestAnimationFrame`; pause or throttle when hidden/minimized.