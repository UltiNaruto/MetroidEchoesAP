#!/usr/bin/env python3
"""
list_events.py — Extract all event node definitions from Randovania JSON files
and cross-reference with Event IDs used in the generated room files.
"""

import json
import pathlib
import re

TOOLS = pathlib.Path(__file__).parent
REPO  = TOOLS.parent

JSON_FILES = [
    ("Agon Wastes",       TOOLS / "Agon_Wastes.json"),
    ("Dark Agon Wastes",  TOOLS / "Dark Agon Wastes.json"),
    ("Torvus Bog",        TOOLS / "Torvus Bog.json"),
    ("Dark Torvus Bog",   TOOLS / "Dark Torvus Bog.json"),
    ("Sanctuary Fortress",TOOLS / "Sanctuary Fortress.json"),
    ("Ing Hive",          TOOLS / "Ing Hive.json"),
]

# Collect event_id -> (region, area, node_name) from JSON
event_defs: dict[str, tuple[str, str, str]] = {}

for region_label, jpath in JSON_FILES:
    data = json.loads(jpath.read_text(encoding="utf-8"))
    for area_name, area in data.get("areas", {}).items():
        for node_name, node in area.get("nodes", {}).items():
            if node.get("node_type") == "event":
                ev_id = node.get("event_name", "")
                event_defs[ev_id] = (region_label, area_name, node_name)

print(f"Found {len(event_defs)} event definitions in Randovania JSONs\n")

# Collect EventXX strings used in generated room files
GENERATED_DIRS = [
    REPO / "src/logic/metroidprime2/light_world/agon_wastes",
    REPO / "src/logic/metroidprime2/dark_world/dark_agon_wastes",
    REPO / "src/logic/metroidprime2/light_world/torvus_bog",
    REPO / "src/logic/metroidprime2/dark_world/dark_torvus_bog",
    REPO / "src/logic/metroidprime2/light_world/sanctuary_fortress",
    REPO / "src/logic/metroidprime2/dark_world/ing_hive",
]

event_pat = re.compile(r'"(Event\d+)"')
used_events: dict[str, list[str]] = {}  # EventXX -> [file, ...]

for d in GENERATED_DIRS:
    for py_file in sorted(d.glob("*.py")):
        content = py_file.read_text(encoding="utf-8")
        for m in event_pat.finditer(content):
            ev = m.group(1)
            used_events.setdefault(ev, []).append(py_file.name)

print(f"EventXX IDs referenced in generated files: {len(used_events)}\n")
print(f"{'EventID':<12}  {'Files':<35}  Definition")
print("-" * 100)
missing = []
def _ev_sort(x: str) -> int:
    num = x[5:]  # strip "Event"
    return int(num) if num.isdigit() else 9999

for ev_id in sorted(used_events, key=_ev_sort):
    files = ", ".join(sorted(set(used_events[ev_id])))
    if ev_id in event_defs:
        region, area, node = event_defs[ev_id]
        print(f"{ev_id:<12}  {files:<35}  {region} | {area} | {node}")
    else:
        print(f"{ev_id:<12}  {files:<35}  *** NOT FOUND IN RANDOVANIA DATA ***")
        missing.append(ev_id)

if missing:
    print(f"\nMissing definitions: {missing}")
