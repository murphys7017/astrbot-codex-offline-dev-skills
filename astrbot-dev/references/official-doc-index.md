# Official Documentation Index

Use this index to load the minimum bundled AstrBot material needed for plugin development. All paths are relative to `generated-skills/astrbot-dev/`.

## Local-First Rule

Prefer `references/offline/...` paths before external docs or network access. Browse only when bundled docs and the target project code are insufficient, or when the user explicitly asks for latest upstream information.

## Core Plugin Docs

- `references/offline/AstrbotDoc/zh/dev/star/plugin-new.md` — current plugin development overview: template, local clone workflow, logo/display name, supported platforms, version constraints, debugging, dependency management, and input semantics.
- `references/offline/AstrbotDoc/zh/dev/star/plugin.md` — detailed legacy-but-still-useful API guide: minimal plugin, event filters, message sending, config, HTML-to-image, sessions, AI/provider calls, function tools, conversation/persona managers, platform instances, async tasks.
- `references/offline/AstrbotDoc/zh/use/plugin.md` — user-facing plugin install/update/enable behavior; useful when writing README or install notes.
- `references/offline/AstrbotDoc/zh/dev/plugin-platform-adapter.md` — platform adapter development and prompt semantic attachment; use only for adapter/plugin boundary work.
- `references/offline/AstrbotDoc/zh/dev/astrbot-config.md` — global AstrBot config fields; use when plugin behavior depends on platform/provider settings.

## AI, Tools, MCP, Skills

- `references/offline/AstrbotDoc/zh/dev/star/guides/ai.md` — provider calls, LLM tools, and agent-facing tool patterns.
- `references/offline/AstrbotDoc/zh/use/function-calling.md` — tool/function-calling behavior and user commands such as `/tool ls`, `/tool on`, `/tool off`.
- `references/offline/AstrbotDoc/zh/use/mcp.md` — MCP server setup and tool integration concepts; use for plugins that depend on external MCP tools.
- `references/offline/AstrbotDoc/zh/use/skills.md` — AstrBot runtime Skills packaging and execution environments; useful when a plugin coordinates with skills.
- `references/offline/AstrbotDoc/zh/providers/` — provider-specific setup; load only when a plugin targets a provider.

## Topic Shortcuts

- Events and filters: `references/offline/AstrbotDoc/zh/dev/star/guides/listen-message-event.md`
- Sending messages: `references/offline/AstrbotDoc/zh/dev/star/guides/send-message.md`
- Plugin config: `references/offline/AstrbotDoc/zh/dev/star/guides/plugin-config.md`
- Storage/data directories: `references/offline/AstrbotDoc/zh/dev/star/guides/storage.md`
- HTML-to-image: `references/offline/AstrbotDoc/zh/dev/star/guides/html-to-pic.md`
- Session control: `references/offline/AstrbotDoc/zh/dev/star/guides/session-control.md`
- Runtime/dependencies: `references/offline/AstrbotDoc/zh/dev/star/guides/env.md`

## Bundled Source/Review Inputs

- `references/offline/skill-astrbot-dev/REFERENCE.md` — existing compact development reference; use as a cross-check for imports, structure, and high-signal code entry points.
- `references/offline/review-astrbot-plugin/references/astrbot-api-rules.md` — API rules and pitfalls extracted for review; use as a final sanity pass.
- `references/offline/review-astrbot-plugin/references/astrbot-review-checklist.md` — quality/security checklist; use selectively, not as the primary development workflow.
- `references/offline/astrbot-official-reviewer/REFERENCE.md` — official-review expectations; useful for publish-ready plugins.

## Source Priority

1. User-provided target repository code and version-specific AstrBot source.
2. Bundled official docs under `references/offline/AstrbotDoc/zh/`.
3. Bundled English development docs under `references/offline/AstrbotDoc/en/dev/` when helpful.
4. Bundled local skills/review references as secondary summaries.
5. Inferences from examples only when APIs are not explicitly documented.
