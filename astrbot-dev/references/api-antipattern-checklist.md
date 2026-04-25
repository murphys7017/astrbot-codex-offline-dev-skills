# Common API and Anti-Pattern Checklist

Use this before finalizing AstrBot plugin code.

## Structure

- `main.py` exists and contains a class inheriting `Star`.
- `__init__(self, context: Context)` calls `super().__init__(context)`.
- `metadata.yaml` exists and includes `name`, `desc`, `version`, `author`, and `repo`; `display_name` is recommended.
- Plugin package name and metadata `name` should usually start with `astrbot_plugin_`.
- README matches implemented commands, config, permissions, and supported platforms.

## Imports and Logging

- Correct: `from astrbot.api.event import filter, AstrMessageEvent`.
- Correct: `from astrbot.api.star import Context, Star`.
- Correct: `from astrbot.api import logger`.
- Avoid importing decorator functions directly in ways that shadow or bypass `filter` conventions.
- Avoid Python `logging` for normal plugin logs unless integrating a third-party library.

## Handlers and Hooks

- Filter-decorated handlers normally include `event: AstrMessageEvent`.
- Handlers are `async def`; any blocking work is isolated from the event loop.
- Normal command/message handlers may `yield event.plain_result(...)` or chain/image results.
- `on_llm_request`, `on_llm_response`, `on_decorating_result`, and `after_message_sent` must not use `yield`; send directly with `event.send(...)` if needed.
- LLM request/response hooks use the documented third parameter type, such as provider request/LLM response objects.
- Do not confuse plugin event hooks with agent runner hooks; route through `references/offline/xunxiing-AstrBot-Skill/docs/plugin_config/hooks.md` or `references/offline/xunxiing-AstrBot-Skill/docs/agent/agent-related-hooks.md` as appropriate.
- Avoid broad catch-and-ignore exception blocks; log actionable errors.

## Message Chains

- Use `event.message_str` only for plain text; use message chains for images, mentions, replies, voice, video, and platform-specific components.
- Do not assume every platform supports every component; degrade gracefully.
- Avoid accessing `raw_message` for portable logic unless no normalized component exists.
- Be careful with aiocqhttp plain-message trimming when exact whitespace matters.

## Config and Data

- Put user-editable settings, secrets, feature toggles, API endpoints, and provider IDs in `_conf_schema.json`.
- Never commit API keys, cookies, bot tokens, local absolute paths, or personal IDs.
- Use `StarTools.get_data_dir()` for plugin persistence; treat it as a `Path`.
- Validate numeric limits, URLs, and enum-like config values before use.

## AI, Tools, MCP

- Prefer dataclass/class-based `FunctionTool` for complex LLM tools when supported; keep JSON schema and callable parameters in sync.
- `@filter.llm_tool` requires a clear docstring with argument names/types/descriptions.
- Do not apply `@filter.permission_type` to `@filter.llm_tool` methods.
- Document MCP prerequisites instead of hiding external server startup inside message handlers.
- Make provider/tool selection configurable when multiple providers or toolsets may exist.

## HTML-to-Image and Files

- Sanitize or escape user-generated text inserted into HTML templates.
- Keep generated image files in plugin data/cache directories and clean up temporary files.
- Provide fallback text if image rendering or platform image send fails.
- Avoid writing into plugin source directories at runtime.

## Debugging Signals

- Command not firing: check import of `filter`, class inheritance, handler signature, command prefix, permissions, and plugin enabled state.
- Config missing: check `_conf_schema.json`, plugin reload, and default values.
- Message parsing wrong: log `event.message_obj.message` and `event.message_obj.raw_message`.
- AI/tool failure: check provider supports function calling, tool enabled state, schema mismatch, and timeout settings.
