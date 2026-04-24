#!/usr/bin/env python3
"""Lightweight AstrBot plugin structure checker.

Usage:
    python check_astrbot_plugin.py path/to/astrbot_plugin_xxx

This script is intentionally conservative: it reports likely issues without
requiring AstrBot to be installed or importing plugin code.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None

REQUIRED_METADATA = ("name", "desc", "version", "author", "repo")
RECOMMENDED_METADATA = ("display_name",)
SPECIAL_NO_YIELD_HOOKS = {
    "on_llm_request",
    "on_llm_response",
    "on_decorating_result",
    "after_message_sent",
}


def parse_metadata(path: Path) -> tuple[dict, list[str]]:
    warnings: list[str] = []
    if not path.exists():
        return {}, ["missing metadata.yaml"]

    text = path.read_text(encoding="utf-8-sig")
    if yaml is not None:
        try:
            data = yaml.safe_load(text) or {}
            if isinstance(data, dict):
                return data, warnings
            return {}, ["metadata.yaml is not a mapping"]
        except Exception as exc:
            return {}, [f"metadata.yaml parse failed: {exc}"]

    data: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip('"\'')
    warnings.append("PyYAML unavailable; used simple top-level metadata parser")
    return data, warnings


def dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = dotted_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    if isinstance(node, ast.Call):
        return dotted_name(node.func)
    return ""


def is_filter_decorator(node: ast.AST) -> bool:
    name = dotted_name(node)
    return name.startswith("filter.") or name.startswith("event_message_type")


def check_main(path: Path) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    if not path.exists():
        return [("ERROR", "missing main.py")]

    text = path.read_text(encoding="utf-8-sig")
    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        return [("ERROR", f"main.py syntax error: {exc}")]

    imports_text = text
    if "from astrbot.api.event import" not in imports_text or "filter" not in imports_text:
        findings.append(("WARN", "expected `from astrbot.api.event import filter, AstrMessageEvent`"))
    if "from astrbot.api.star import" not in imports_text or "Star" not in imports_text:
        findings.append(("WARN", "expected `from astrbot.api.star import Context, Star`"))
    if "from astrbot.api import logger" not in imports_text:
        findings.append(("INFO", "prefer `from astrbot.api import logger` for plugin logging"))
    if re.search(r"^\s*import\s+logging\b|^\s*from\s+logging\s+import\b", text, re.M):
        findings.append(("INFO", "Python logging imported; AstrBot plugins usually use astrbot.api.logger"))

    star_classes: list[ast.ClassDef] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and any(dotted_name(base).endswith("Star") for base in node.bases):
            star_classes.append(node)
    if not star_classes:
        findings.append(("ERROR", "no class inheriting Star found in main.py"))
        return findings

    for cls in star_classes:
        init = next((item for item in cls.body if isinstance(item, ast.FunctionDef) and item.name == "__init__"), None)
        if init is None:
            findings.append(("WARN", f"{cls.name} has no __init__(self, context)"))
        else:
            calls_super = any(
                isinstance(call, ast.Call) and dotted_name(call.func).endswith("super.__init__")
                for call in ast.walk(init)
            )
            if not calls_super:
                findings.append(("WARN", f"{cls.name}.__init__ does not appear to call super().__init__(context)"))

        for item in cls.body:
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            decorators = list(item.decorator_list)
            if not any(is_filter_decorator(deco) for deco in decorators):
                continue
            if not isinstance(item, ast.AsyncFunctionDef):
                findings.append(("WARN", f"filter handler `{item.name}` should usually be async def"))
            arg_names = [arg.arg for arg in item.args.args]
            if item.name != "on_astrbot_loaded" and "event" not in arg_names:
                findings.append(("WARN", f"filter handler `{item.name}` has no `event` parameter"))
            if item.name in SPECIAL_NO_YIELD_HOOKS and any(isinstance(n, (ast.Yield, ast.YieldFrom)) for n in ast.walk(item)):
                findings.append(("ERROR", f"hook `{item.name}` must not use yield; use event.send(...)"))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check an AstrBot plugin directory.")
    parser.add_argument("plugin_dir", type=Path)
    args = parser.parse_args()

    plugin_dir = args.plugin_dir.resolve()
    if not plugin_dir.exists() or not plugin_dir.is_dir():
        print(f"ERROR: not a directory: {plugin_dir}")
        return 2

    findings: list[tuple[str, str]] = []
    main_py = plugin_dir / "main.py"
    metadata_yaml = plugin_dir / "metadata.yaml"
    config_schema = plugin_dir / "_conf_schema.json"
    readme = plugin_dir / "README.md"

    findings.extend(check_main(main_py))

    metadata, metadata_warnings = parse_metadata(metadata_yaml)
    findings.extend(("WARN", warning) for warning in metadata_warnings)
    for key in REQUIRED_METADATA:
        if not metadata.get(key):
            findings.append(("ERROR", f"metadata.yaml missing required field `{key}`"))
    for key in RECOMMENDED_METADATA:
        if not metadata.get(key):
            findings.append(("INFO", f"metadata.yaml missing recommended field `{key}`"))
    name = str(metadata.get("name", ""))
    if name and not name.startswith("astrbot_plugin_"):
        findings.append(("INFO", "metadata `name` usually starts with `astrbot_plugin_`"))

    if not config_schema.exists():
        findings.append(("INFO", "no _conf_schema.json found; add one if plugin has settings or secrets"))
    if not readme.exists():
        findings.append(("INFO", "no README.md found"))

    severity_order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda item: (severity_order.get(item[0], 9), item[1]))

    for level, message in findings:
        print(f"{level}: {message}")

    error_count = sum(1 for level, _ in findings if level == "ERROR")
    warn_count = sum(1 for level, _ in findings if level == "WARN")
    info_count = sum(1 for level, _ in findings if level == "INFO")
    print(f"Summary: {error_count} error(s), {warn_count} warning(s), {info_count} info item(s)")
    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
