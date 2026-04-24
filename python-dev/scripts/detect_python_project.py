#!/usr/bin/env python3
"""Detect common Python project tooling and suggest validation commands."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="ignore")
    except OSError:
        return ""


def exists_any(root: Path, names: list[str]) -> list[str]:
    found: list[str] = []
    for name in names:
        if any(root.glob(name)):
            found.append(name)
    return found


def has_command(command: str) -> bool:
    paths = os.environ.get("PATH", "").split(os.pathsep)
    extensions = os.environ.get("PATHEXT", "").split(os.pathsep) if os.name == "nt" else [""]
    for directory in paths:
        base = Path(directory) / command
        candidates = [base.with_suffix(ext.lower()) for ext in extensions if ext] + [base]
        if any(candidate.is_file() for candidate in candidates):
            return True
    return False


def detect(root: Path) -> dict[str, Any]:
    pyproject = root / "pyproject.toml"
    pyproject_text = read_text(pyproject) if pyproject.exists() else ""
    files = {path.name for path in root.iterdir()} if root.exists() else set()

    tests_present = any((root / name).exists() for name in ("tests", "test")) or bool(list(root.glob("test_*.py")))
    pytest_configured = "pytest" in pyproject_text or bool(files & {"pytest.ini"}) or tests_present

    tools = {
        "package_metadata": [name for name in ("pyproject.toml", "setup.cfg", "setup.py") if name in files],
        "dependency_files": [name for name in ("uv.lock", "poetry.lock", "Pipfile.lock", "requirements.txt", "requirements-dev.txt") if name in files]
        + exists_any(root, ["requirements*.txt", "conda*.yml", "environment*.yml"]),
        "test_tools": [],
        "lint_format_tools": [],
        "type_tools": [],
        "available_commands": [cmd for cmd in ("python", "uv", "poetry", "pytest", "ruff", "mypy", "pyright") if has_command(cmd)],
    }

    if pytest_configured:
        tools["test_tools"].append("pytest")
    if "unittest" in pyproject_text or exists_any(root, ["test*.py"]):
        tools["test_tools"].append("unittest")
    for tool in ("tox", "nox"):
        if (root / f"{tool}.ini").exists() or (root / f"{tool}file.py").exists() or tool in pyproject_text:
            tools["test_tools"].append(tool)
    for tool in ("ruff", "black", "isort", "flake8", "pylint"):
        if tool in pyproject_text or (root / f".{tool}").exists() or (root / f"{tool}.ini").exists():
            tools["lint_format_tools"].append(tool)
    for tool in ("mypy", "pyright", "pyre"):
        if tool in pyproject_text or (root / f"{tool}.ini").exists() or (root / f".{tool}").exists():
            tools["type_tools"].append(tool)

    suggestions: list[str] = []
    runner = "uv run " if "uv.lock" in files and has_command("uv") else "poetry run " if "poetry.lock" in files and has_command("poetry") else ""
    if "pytest" in tools["test_tools"]:
        suggestions.append(f"{runner}pytest -q".strip())
    elif tests_present:
        suggestions.append("python -m unittest discover")
    if "ruff" in tools["lint_format_tools"]:
        suggestions.append(f"{runner}ruff check .".strip())
    if "mypy" in tools["type_tools"]:
        suggestions.append(f"{runner}mypy .".strip())
    if "pyright" in tools["type_tools"]:
        suggestions.append(f"{runner}pyright".strip())

    return {
        "root": str(root),
        "tools": tools,
        "suggested_commands": suggestions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect common Python project tooling.")
    parser.add_argument("path", nargs="?", default=".", help="Project root to inspect")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"not a directory: {root}")

    result = detect(root)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"Python project scan: {result['root']}")
    for group, values in result["tools"].items():
        display = ", ".join(dict.fromkeys(values)) if values else "none detected"
        print(f"- {group.replace('_', ' ')}: {display}")
    if result["suggested_commands"]:
        print("Suggested validation commands:")
        for command in result["suggested_commands"]:
            print(f"- {command}")
    else:
        print("Suggested validation commands: none detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
