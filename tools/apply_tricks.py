#!/usr/bin/env python3
"""
apply_tricks.py — Replace # TRICK placeholders in generated room files with
has_trick_enabled() calls using Randovania's global category names (Option B).

Usage:
    python tools/apply_tricks.py [--dry-run] [--update-options]
"""

import re
import sys
from pathlib import Path

TRICK_NAMES: dict[str, str] = {
    "Dash":               "Combat/Scan Dash",
    "BombJump":           "Bomb Jump",
    "SlopeJump":          "Slope Jump",
    "Movement":           "Movement",
    "BSJ":                "Bomb Space Jump",
    "RollJump":           "Roll Jump",
    "UnderwaterDash":     "Underwater Dash",
    "AirUnderwater":      "Air Underwater",
    "OoB":                "Single Room Out of Bounds",
    "NoSuits":            "Suitless Dark Aether",
    "SAnoSJ":             "Screw Attack without Space Jump",
    "WallBoost":          "Wall Boost",
    "EnemyHop":           "Jump Off Enemy",
    "Combat":             "Combat",
    "InstantMorph":       "Instant Morph",
    "InvisibleObjects":   "Invisible Objects",
    "StandableTerrain":   "Standable Terrain",
    "TerminalFall":       "Terminal Fall Abuse",
    "BoostJump":          "Boost Jump",
    "EDash":              "Extended Dash",
    "BomblessSlot":       "Bomb Slot without Bombs",
    "ScanPost":           "Open Gates from Behind",
    "ScrewAttackTunnels": "Screw Attack into Tunnels/Openings",
    "Knowledge":          "Knowledge",
    "SeekerlessLocks":    "Seeker Locks without Seeker Missiles",
}

# Matches:  <indent>False,\n<whitespace># TRICK: TrickName level=N <anything>
TRICK_PATTERN = re.compile(
    r'([ \t]+)False,\n[ \t]+# TRICK: (\w+) level=\d+[^\n]*'
)


def replace_tricks(content: str) -> tuple[str, list[str]]:
    used: list[str] = []

    def replacer(m: re.Match) -> str:
        indent = m.group(1)
        short = m.group(2)
        long_name = TRICK_NAMES.get(short, short)
        used.append(long_name)
        return f'{indent}has_trick_enabled(state, player, "{long_name}"),'

    return TRICK_PATTERN.sub(replacer, content), used


def main() -> None:
    dry_run     = "--dry-run"       in sys.argv
    upd_options = "--update-options" in sys.argv

    repo_root = Path(__file__).parent.parent
    logic_dir = repo_root / "src" / "logic" / "metroidprime2"

    target_dirs = [
        logic_dir / "light_world" / "agon_wastes",
        logic_dir / "dark_world"  / "dark_agon_wastes",
        logic_dir / "light_world" / "torvus_bog",
        logic_dir / "dark_world"  / "dark_torvus_bog",
        logic_dir / "light_world" / "sanctuary_fortress",
        logic_dir / "dark_world"  / "ing_hive",
    ]

    all_used: set[str] = set()
    files_changed = 0
    total_replaced = 0

    for d in target_dirs:
        for py_file in sorted(d.glob("*.py")):
            if py_file.name == "__init__.py":
                continue
            content = py_file.read_text(encoding="utf-8")
            if "# TRICK:" not in content:
                continue
            new_content, used = replace_tricks(content)
            all_used.update(used)
            total_replaced += len(used)
            files_changed += 1
            if dry_run:
                print(f"  [DRY] {py_file.parent.name}/{py_file.name}  ({len(used)} tricks)")
            else:
                py_file.write_text(new_content, encoding="utf-8")

    tag = "[DRY RUN] " if dry_run else ""
    print(f"\n{tag}{files_changed} files, {total_replaced} trick placeholders replaced")
    print(f"Unique trick categories: {sorted(all_used)}")

    if upd_options and not dry_run:
        options_path = repo_root / "src" / "Options.py"
        options_content = options_path.read_text(encoding="utf-8")

        marker = (
            '        "Temple Grounds - Trooper Security Station | SA to break the gate",\n'
            '    ]'
        )
        if marker not in options_content:
            print("\nWARNING: insertion point not found in Options.py — add tricks manually")
            return

        new_lines = "\n".join(f'        "{t}",' for t in sorted(all_used))
        replacement = (
            '        "Temple Grounds - Trooper Security Station | SA to break the gate",\n'
            f'{new_lines}\n'
            '    ]'
        )
        options_path.write_text(
            options_content.replace(marker, replacement),
            encoding="utf-8",
        )
        print(f"\nAdded {len(all_used)} global trick categories to Options.py")


if __name__ == "__main__":
    main()
