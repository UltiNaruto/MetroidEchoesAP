#!/usr/bin/env python3
"""
apply_door_weaknesses.py — Replace unknown door weakness TODO comments in
generated room files with the correct DoorCover enum values.

Usage:
    python tools/apply_door_weaknesses.py [--dry-run]
"""

import re
import sys
from pathlib import Path

WEAKNESS_MAP: dict[str, str] = {
    "Annihilator Door": "DoorCover.Annihilator",
    "Dark Door":        "DoorCover.Dark",
    "Dark Portal":      "DoorCover.Opened",
    "Light Door":       "DoorCover.Light",
    "Light Portal":     "DoorCover.Opened",
    "Open Passage":     "DoorCover.Opened",
    "Scan Portal":      "DoorCover.Opened",
    "Teleporter":       "DoorCover.Opened",
}

# Matches the two-line pattern:
#   <indent># TODO: unknown weakness 'X' — map to correct DoorCover\n
#   <indent>door=DoorCover.Any,
TODO_PAT = re.compile(
    r"[ \t]+# TODO: unknown weakness '([^']+)' [^\n]*\n"
    r"([ \t]+)door=DoorCover\.Any,"
)

REPO = Path(__file__).parent.parent
GENERATED_DIRS = [
    REPO / "src/logic/metroidprime2/light_world/agon_wastes",
    REPO / "src/logic/metroidprime2/dark_world/dark_agon_wastes",
    REPO / "src/logic/metroidprime2/light_world/torvus_bog",
    REPO / "src/logic/metroidprime2/dark_world/dark_torvus_bog",
    REPO / "src/logic/metroidprime2/light_world/sanctuary_fortress",
    REPO / "src/logic/metroidprime2/dark_world/ing_hive",
]


def replace_weaknesses(content: str) -> tuple[str, int, list[str]]:
    count = 0
    unknowns: list[str] = []

    def replacer(m: re.Match) -> str:
        nonlocal count
        weakness = m.group(1)
        indent   = m.group(2)
        if weakness in WEAKNESS_MAP:
            count += 1
            return f"{indent}door={WEAKNESS_MAP[weakness]},"
        unknowns.append(weakness)
        return m.group(0)

    new_content = TODO_PAT.sub(replacer, content)
    return new_content, count, unknowns


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    files_changed = total = 0
    all_unknowns: list[str] = []

    for d in GENERATED_DIRS:
        for py_file in sorted(d.glob("*.py")):
            if py_file.name == "__init__.py":
                continue
            content = py_file.read_text(encoding="utf-8")
            if "# TODO: unknown weakness" not in content:
                continue
            new_content, count, unknowns = replace_weaknesses(content)
            all_unknowns.extend(unknowns)
            if count:
                files_changed += 1
                total += count
                if dry_run:
                    print(f"  [DRY] {py_file.parent.name}/{py_file.name} ({count} fixed)")
                else:
                    py_file.write_text(new_content, encoding="utf-8")

    tag = "[DRY RUN] " if dry_run else ""
    print(f"{tag}{files_changed} files, {total} door weaknesses fixed")
    if all_unknowns:
        print(f"Still unmapped: {sorted(set(all_unknowns))}")


if __name__ == "__main__":
    main()
