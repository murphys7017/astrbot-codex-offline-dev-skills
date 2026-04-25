---
name: astrbot-dev
description: "Use for AstrBot plugin development tasks: creating or modifying plugins, event listeners and filters, message chains/components, plugin metadata/config, session/conversation control, AI/provider calls and LLM tools, HTML-to-image output, active/passive message sending, basic MCP/skill integration, and debugging AstrBot plugin behavior."
---

# AstrBot Dev

Use this skill when building, modifying, or debugging AstrBot plugins. Focus on development decisions and implementation patterns; use review-only skills only for audits after code is written.

## Workflow

1. Identify the target AstrBot version if specified; otherwise prefer bundled offline docs and local project code when available.
2. Read only the relevant reference file(s):
   - `references/offline-reference-index.md` for local-first source selection.
   - `references/structured-skill-index.md` for the AI-oriented `xunxiing/AstrBot-Skill` topic map.
   - `references/official-doc-index.md` for source mapping.
   - `references/plugin-development-workflow.md` for implementation flow and examples.
   - `references/api-antipattern-checklist.md` before finalizing code.
3. Inspect the plugin directory before editing: `main.py`, `metadata.yaml`, `_conf_schema.json`, `requirements.txt`, `README.md`, and submodules.
4. Implement with AstrBot SDK imports and async handlers; keep `main.py` focused on event wiring and orchestration.
5. Validate structure with `scripts/check_astrbot_plugin.py <plugin_dir>` when a plugin directory is available.

## Development Defaults

- Prefer bundled docs under `references/offline/AstrbotDoc/zh/` over external websites; browse only when local docs/project code are insufficient or the user asks for latest upstream information.
- Plugin entry file is `main.py`; define a class inheriting `Star` and call `super().__init__(context)`.
- Use `from astrbot.api.event import filter, AstrMessageEvent` and `from astrbot.api.star import Context, Star`.
- Use `from astrbot.api import logger` instead of Python `logging` for plugin logs.
- Prefer `metadata.yaml` for marketplace metadata; use `_conf_schema.json` for user-editable settings and secrets.
- Use `yield event.plain_result(...)` or chain/image results in normal message handlers; use `await event.send(...)` in hooks where `yield` is unsupported.
- Use `event.message_str` for plain text and `event.message_obj.message` for message-chain components.
- Use `StarTools.get_data_dir()` for persistent plugin data instead of hard-coded project paths.
- Do not mix plugin event hooks (`references/offline/xunxiing-AstrBot-Skill/docs/plugin_config/hooks.md`) with agent runner hooks (`references/offline/xunxiing-AstrBot-Skill/docs/agent/agent-related-hooks.md`).
- For v4.5.7+ LLM tools, prefer dataclass `FunctionTool` patterns when the target AstrBot version supports them; cross-check `references/offline/xunxiing-AstrBot-Skill/docs/design_standards/core_concepts.md`.
- If AstrBot SDK/source is already present in the target project, use it for signature lookup. Do not install or upgrade packages unless the user asks.

## When Coding

- Keep handlers small and typed; move API calls, parsing, storage, and rendering into helpers or submodules.
- Guard platform-specific features with metadata/support checks and graceful fallback.
- Avoid blocking I/O in handlers; use async clients or `asyncio.to_thread` for unavoidable synchronous work.
- Never hard-code provider IDs, tokens, webhook URLs, or local absolute paths; expose config instead.
- For LLM tools, provide clear names, descriptions, JSON-schema parameters, and docstrings the framework can parse.

## Useful Commands

```powershell
python scripts/check_astrbot_plugin.py path/to/plugin
```
