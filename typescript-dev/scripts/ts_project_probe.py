#!/usr/bin/env python3
"""Lightweight TypeScript/JavaScript project inventory.

Usage: python scripts/ts_project_probe.py [repo]
Prints package metadata, tsconfig files, and likely validation scripts.
"""
from __future__ import annotations

import json
import argparse
import sys
from pathlib import Path
from typing import Any

INTERESTING_SCRIPT_WORDS = (
    "build",
    "test",
    "lint",
    "typecheck",
    "type-check",
    "check",
    "tsc",
    "vitest",
    "jest",
    "mocha",
    "eslint",
)

INTERESTING_COMPILER_OPTIONS = (
    "strict",
    "noImplicitAny",
    "strictNullChecks",
    "noUncheckedIndexedAccess",
    "exactOptionalPropertyTypes",
    "allowJs",
    "checkJs",
    "declaration",
    "composite",
    "incremental",
    "module",
    "moduleResolution",
    "target",
    "jsx",
    "baseUrl",
    "paths",
)


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as error:
        print(f"! {path}: invalid JSON: {error}")
        return None


def find_tsconfigs(root: Path) -> list[Path]:
    ignored = {"node_modules", ".git", "dist", "build", "coverage", ".next", ".turbo"}
    configs: list[Path] = []
    for path in root.rglob("tsconfig*.json"):
        if any(part in ignored for part in path.relative_to(root).parts):
            continue
        configs.append(path)
    return sorted(configs)


def print_package(root: Path) -> None:
    package_path = root / "package.json"
    package = load_json(package_path)
    print(f"# package.json: {'found' if package else 'missing'}")
    if not package:
        return

    print(f"name: {package.get('name', '<unnamed>')}")
    manager = package.get("packageManager")
    if manager:
        print(f"packageManager: {manager}")

    scripts = package.get("scripts", {})
    if isinstance(scripts, dict) and scripts:
        print("\n## likely validation scripts")
        matched = False
        for name, command in sorted(scripts.items()):
            haystack = f"{name} {command}".lower()
            if any(word in haystack for word in INTERESTING_SCRIPT_WORDS):
                matched = True
                print(f"- {name}: {command}")
        if not matched:
            print("- none matched build/test/lint/typecheck keywords")

    deps = set()
    for section in ("dependencies", "devDependencies", "peerDependencies"):
        values = package.get(section, {})
        if isinstance(values, dict):
            deps.update(values)
    notable = sorted(dep for dep in deps if dep in {"typescript", "ts-node", "tsx", "jest", "vitest", "eslint", "webpack", "vite", "rollup", "tsup"} or dep.startswith("@types/"))
    if notable:
        print("\n## notable TS/tool deps")
        for dep in notable:
            print(f"- {dep}")


def print_tsconfigs(root: Path) -> None:
    configs = find_tsconfigs(root)
    print(f"\n# tsconfig files: {len(configs)}")
    for config_path in configs:
        rel = config_path.relative_to(root)
        print(f"\n## {rel}")
        config = load_json(config_path)
        if not config:
            continue
        if "extends" in config:
            print(f"extends: {config['extends']}")
        options = config.get("compilerOptions", {})
        if isinstance(options, dict):
            for key in INTERESTING_COMPILER_OPTIONS:
                if key in options:
                    value = options[key]
                    print(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        for key in ("include", "exclude", "files", "references"):
            if key in config:
                print(f"{key}: {json.dumps(config[key], ensure_ascii=False)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect a TypeScript/JavaScript project for package scripts and tsconfig settings."
    )
    parser.add_argument(
        "repo",
        nargs="?",
        default=".",
        help="Repository or project path to inspect (default: current directory).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo).resolve()
    if not root.exists():
        print(f"error: path does not exist: {root}", file=sys.stderr)
        return 2
    if root.is_file():
        root = root.parent

    print(f"TypeScript project probe: {root}\n")
    print_package(root)
    print_tsconfigs(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
