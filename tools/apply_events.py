#!/usr/bin/env python3
"""
apply_events.py — Replace state.has("EventXX", player) placeholders in generated
room files with the real MetroidEchoesAP item name for each event.

Usage:
    python tools/apply_events.py [--dry-run]
"""

import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).parent
REPO  = TOOLS.parent

JSON_FILES = [
    ("Agon Wastes",        TOOLS / "Agon_Wastes.json"),
    ("Dark Agon Wastes",   TOOLS / "Dark Agon Wastes.json"),
    ("Torvus Bog",         TOOLS / "Torvus Bog.json"),
    ("Dark Torvus Bog",    TOOLS / "Dark Torvus Bog.json"),
    ("Sanctuary Fortress", TOOLS / "Sanctuary Fortress.json"),
    ("Ing Hive",           TOOLS / "Ing Hive.json"),
]

GENERATED_DIRS = [
    REPO / "src/logic/metroidprime2/light_world/agon_wastes",
    REPO / "src/logic/metroidprime2/dark_world/dark_agon_wastes",
    REPO / "src/logic/metroidprime2/light_world/torvus_bog",
    REPO / "src/logic/metroidprime2/dark_world/dark_torvus_bog",
    REPO / "src/logic/metroidprime2/light_world/sanctuary_fortress",
    REPO / "src/logic/metroidprime2/dark_world/ing_hive",
]

# Hardcoded overrides for events defined outside the 6 new region JSONs
event_map: dict[str, str] = {
    # Defined in Great Temple JSON; gates the energy controller teleporter network,
    # which opens once all three dark energies are returned and the Light Suit room unlocks.
    "Event77": "Great Temple - Main Energy Controller | Can Pick Up Light Suit Item",
}
for region_label, jpath in JSON_FILES:
    data = json.loads(jpath.read_text(encoding="utf-8"))
    for area_name, area in data.get("areas", {}).items():
        for node_name, node in area.get("nodes", {}).items():
            if node.get("node_type") == "event":
                ev_id = node.get("event_name", "")
                item_name = f"{region_label} - {area_name} | {node_name}"
                event_map[ev_id] = item_name

EVENT_PAT = re.compile(r'state\.has\("(Event\d+)", player\)')


def replace_events(content: str) -> tuple[str, list[tuple[str, str]], list[str]]:
    """Returns (new_content, [(EventXX, item_name), ...], [unknown_ids])."""
    replaced: list[tuple[str, str]] = []
    unknown:  list[str] = []

    def replacer(m: re.Match) -> str:
        ev_id = m.group(1)
        if ev_id in event_map:
            item_name = event_map[ev_id]
            replaced.append((ev_id, item_name))
            return f'state.has("{item_name}", player)'
        else:
            unknown.append(ev_id)
            return m.group(0)  # leave unchanged

    return EVENT_PAT.sub(replacer, content), replaced, unknown


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    files_changed = 0
    total_replaced = 0
    all_unknown: dict[str, list[str]] = {}

    for d in GENERATED_DIRS:
        for py_file in sorted(d.glob("*.py")):
            if py_file.name == "__init__.py":
                continue
            content = py_file.read_text(encoding="utf-8")
            if not EVENT_PAT.search(content):
                continue
            new_content, replaced, unknown = replace_events(content)
            if replaced or unknown:
                files_changed += 1
                total_replaced += len(replaced)
                for ev_id in unknown:
                    all_unknown.setdefault(ev_id, []).append(py_file.name)
                if dry_run:
                    for ev_id, item_name in replaced:
                        print(f"  [DRY] {py_file.name}: {ev_id} -> {item_name!r}")
                    for ev_id in unknown:
                        print(f"  [DRY] {py_file.name}: {ev_id} *** UNKNOWN — left as-is")
                else:
                    py_file.write_text(new_content, encoding="utf-8")

    tag = "[DRY RUN] " if dry_run else ""
    print(f"\n{tag}{files_changed} files, {total_replaced} Event IDs replaced")

    if all_unknown:
        print(f"\nUnknown Event IDs (not in Randovania JSONs — need manual mapping):")
        for ev_id, files in sorted(all_unknown.items()):
            print(f"  {ev_id}: {', '.join(files)}")


if __name__ == "__main__":
    main()
