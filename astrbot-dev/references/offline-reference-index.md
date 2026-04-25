# Offline Reference Index

Use these bundled files before browsing or using external documentation. Load only the smallest file(s) needed for the task.

## Primary AstrBot Docs

- Full Chinese docs: `references/offline/AstrbotDoc/zh/`
- Key English development docs: `references/offline/AstrbotDoc/en/dev/`
- Start here for plugin development: `references/offline/AstrbotDoc/zh/dev/star/plugin.md`
- New plugin workflow: `references/offline/AstrbotDoc/zh/dev/star/plugin-new.md`
- Publishing guidance: `references/offline/AstrbotDoc/zh/dev/star/plugin-publish.md`

## AI-Structured AstrBot Skill Snapshot

- Bundled snapshot root: `references/offline/xunxiing-AstrBot-Skill/`
- Local topic index: `references/structured-skill-index.md`
- Reference skill workflow: `references/offline/xunxiing-AstrBot-Skill/docs/REFERENCE.md`
- Core concepts/API map: `references/offline/xunxiing-AstrBot-Skill/docs/design_standards/core_concepts.md`
- Use this snapshot for fast topic routing across plugin config, messages, platform adapters, storage/utils, and agent features.

## Development Topic Map

- Basic plugin example: `references/offline/AstrbotDoc/zh/dev/star/guides/simple.md`
- Event listening and filters: `references/offline/AstrbotDoc/zh/dev/star/guides/listen-message-event.md`
- Sending active/passive messages: `references/offline/AstrbotDoc/zh/dev/star/guides/send-message.md`
- Plugin config schema: `references/offline/AstrbotDoc/zh/dev/star/guides/plugin-config.md`
- Persistent storage and data dirs: `references/offline/AstrbotDoc/zh/dev/star/guides/storage.md`
- AI/provider calls and LLM tools: `references/offline/AstrbotDoc/zh/dev/star/guides/ai.md`
- HTML-to-image rendering: `references/offline/AstrbotDoc/zh/dev/star/guides/html-to-pic.md`
- Session/conversation control: `references/offline/AstrbotDoc/zh/dev/star/guides/session-control.md`
- Runtime environment and dependencies: `references/offline/AstrbotDoc/zh/dev/star/guides/env.md`
- Miscellaneous APIs: `references/offline/AstrbotDoc/zh/dev/star/guides/other.md`
- Platform adapter development: `references/offline/AstrbotDoc/zh/dev/plugin-platform-adapter.md`
- AstrBot config reference: `references/offline/AstrbotDoc/zh/dev/astrbot-config.md`
- OpenAPI reference: `references/offline/AstrbotDoc/zh/dev/openapi.md`

## Bundled Prior Art

- Previous development skill snapshot: `references/offline/skill-astrbot-dev/REFERENCE.md`
- Official reviewer skill snapshot: `references/offline/astrbot-official-reviewer/REFERENCE.md`
- Review rules and checklist: `references/offline/review-astrbot-plugin/references/`
- xunxiing/AstrBot-Skill snapshot and docs4agent reference: `references/offline/xunxiing-AstrBot-Skill/`

## Offline Strategy

1. Prefer concise generated references in `references/*.md` for common patterns.
2. Use `references/structured-skill-index.md` for AI-friendly topic routing before reading large docs.
3. For exact API behavior, read the matching local official doc under `references/offline/AstrbotDoc/zh/`.
4. Use the English `references/offline/AstrbotDoc/en/dev/` files only when English wording helps disambiguate development docs.
5. Do not browse unless the local docs and the target project code cannot answer the question, or the user explicitly asks for current upstream information.
