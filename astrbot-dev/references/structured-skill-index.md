# Structured AstrBot Skill Index

Use this index for the bundled `xunxiing/AstrBot-Skill` snapshot. It is AI-oriented: compact topic folders, API lists, and workflow notes. Prefer it for fast orientation, then cross-check exact behavior against official bundled docs or target project code.

## Entry Points

- Skill workflow reference: `references/offline/xunxiing-AstrBot-Skill/docs/REFERENCE.md`
- Site index: `references/offline/xunxiing-AstrBot-Skill/docs/index.md`
- Core concepts/API list: `references/offline/xunxiing-AstrBot-Skill/docs/design_standards/core_concepts.md`
- Best practices: `references/offline/xunxiing-AstrBot-Skill/docs/design_standards/best_practices.md`
- Architecture overview: `references/offline/xunxiing-AstrBot-Skill/docs/design_standards/architecture_overview.md`
- AI-friendly docs writing reference: `references/offline/xunxiing-AstrBot-Skill/docs4agent/REFERENCE.md`

## Topic Routing

- Plugin decorators, hooks, lifecycle, config schema: `references/offline/xunxiing-AstrBot-Skill/docs/plugin_config/`
- Message model, events, components, UMO: `references/offline/xunxiing-AstrBot-Skill/docs/messages/`
- Agent system, providers, tools, subagents, sandbox, cron, context compression: `references/offline/xunxiing-AstrBot-Skill/docs/agent/`
- Platform adapter interface and message conversion: `references/offline/xunxiing-AstrBot-Skill/docs/platform_adapters/`
- Storage, KV, file storage, text-to-image utilities: `references/offline/xunxiing-AstrBot-Skill/docs/Storage & Utils/`
- Generated or helper scripts from the reference repo: `references/offline/xunxiing-AstrBot-Skill/scripts/`

## High-Value Files

- Plugin event hooks: `references/offline/xunxiing-AstrBot-Skill/docs/plugin_config/hooks.md`
- Agent runner hooks: `references/offline/xunxiing-AstrBot-Skill/docs/agent/agent-related-hooks.md`
- Agent runner architecture: `references/offline/xunxiing-AstrBot-Skill/docs/agent/agent-runner.md`
- Tool registration: `references/offline/xunxiing-AstrBot-Skill/docs/agent/registe tools.md`
- Official tool list: `references/offline/xunxiing-AstrBot-Skill/docs/agent/offical-tool-list/tools.md`
- Message conversion: `references/offline/xunxiing-AstrBot-Skill/docs/platform_adapters/message_conversion.md`
- Adapter interface: `references/offline/xunxiing-AstrBot-Skill/docs/platform_adapters/adapter_interface.md`
- Plugin config file format: `references/offline/xunxiing-AstrBot-Skill/docs/plugin_config/file_config.md`
- Plugin config schema: `references/offline/xunxiing-AstrBot-Skill/docs/plugin_config/schema.md`
- Session control: `references/offline/xunxiing-AstrBot-Skill/docs/plugin_config/session_control.md`

## Learned Usage Pattern

1. Start from one entrypoint, not a broad read.
2. Pick one topic folder and stay focused.
3. Do not mix plugin event hooks with agent runner hooks.
4. Treat local target project code as final authority when docs disagree.
5. Use the structured docs for fast orientation and the bundled official docs for exact user-facing or version-specific behavior.
