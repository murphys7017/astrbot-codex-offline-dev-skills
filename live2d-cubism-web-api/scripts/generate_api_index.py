#!/usr/bin/env python3
"""Generate a compact API index from Cubism Web Framework TypeScript sources."""
from __future__ import annotations

import re
import sys
from pathlib import Path

EXPORT_RE = re.compile(r"^export\s+(?:abstract\s+)?(class|interface|enum|type|namespace|function)\s+([A-Za-z_][\w]*)")
METHOD_RE = re.compile(r"^\s*(public|protected|static)\s+(?:async\s+)?(?:get\s+|set\s+)?([A-Za-z_][\w]*)\s*\(([^)]*)\)\s*(?::\s*([^\{;]+))?")

CATEGORY_NOTES = {
    "root": "Framework startup, model setting JSON, default parameter IDs, and base interfaces.",
    "effect": "High-level effects such as eye blink, breath, look, and pose.",
    "id": "Cubism ID objects and ID manager lookup.",
    "math": "Matrices, vectors, view/model transforms, target point smoothing.",
    "model": "MOC/model loading, parameter/part/drawable access, user model wrapper.",
    "motion": "Motion playback, queues, expressions, update scheduler, motion events.",
    "physics": "Physics JSON parsing and parameter evaluation/interpolation.",
    "rendering": "Renderer abstraction, WebGL renderer, clipping, masks, shaders, render targets.",
    "type": "Small shared value types.",
    "utils": "Debug logging, JSON parser, strings, array helpers.",
}


def rel_category(path: Path, src_root: Path) -> str:
    rel = path.relative_to(src_root)
    return rel.parts[0] if len(rel.parts) > 1 else "root"


def parse_file(path: Path) -> tuple[list[str], list[str]]:
    exports: list[str] = []
    methods: list[str] = []
    current_export = ""
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        stripped = line.strip()
        export_match = EXPORT_RE.match(stripped)
        if export_match:
            kind, name = export_match.groups()
            current_export = name
            exports.append(f"{kind} `{name}`")
            continue
        method_match = METHOD_RE.match(line)
        if method_match and current_export:
            visibility, name, args, ret = method_match.groups()
            if name in {"constructor"}:
                continue
            signature = f"`{current_export}.{name}({args.strip()})`"
            if ret:
                signature += f" → `{ret.strip()}`"
            methods.append(signature)
    return exports, methods


def generate(src_root: Path, out_path: Path) -> None:
    sections: dict[str, list[tuple[Path, list[str], list[str]]]] = {}
    for path in sorted(src_root.rglob("*.ts")):
        category = rel_category(path, src_root)
        exports, methods = parse_file(path)
        if exports or methods:
            sections.setdefault(category, []).append((path, exports, methods))

    lines: list[str] = [
        "# Live2D Cubism Web Framework API Index",
        "",
        "Generated from bundled `references/offline/CubismSdkForWeb-5-r.5/Framework/src/**/*.ts`.",
        "Use this as the first local API router, then open the specific source file for exact signatures and comments.",
        "",
        "## Categories",
        "",
    ]
    for category in sorted(sections):
        lines.append(f"- `{category}`: {CATEGORY_NOTES.get(category, 'Framework APIs.')}")
    lines.append("")

    for category in sorted(sections):
        lines.extend([f"## {category}", "", CATEGORY_NOTES.get(category, "Framework APIs."), ""])
        for path, exports, methods in sections[category]:
            rel = path.relative_to(src_root).as_posix()
            lines.append(f"### `{rel}`")
            if exports:
                lines.append("Exports: " + "; ".join(exports))
            if methods:
                lines.append("")
                lines.append("Common methods:")
                for item in methods[:35]:
                    lines.append(f"- {item}")
                if len(methods) > 35:
                    lines.append(f"- ... {len(methods) - 35} more; open the source file for full list")
            lines.append("")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    skill_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    src_root = skill_root / "references" / "offline" / "CubismSdkForWeb-5-r.5" / "Framework" / "src"
    out_path = skill_root / "references" / "api-index.md"
    if not src_root.exists():
        print(f"missing source root: {src_root}", file=sys.stderr)
        return 2
    generate(src_root, out_path)
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())