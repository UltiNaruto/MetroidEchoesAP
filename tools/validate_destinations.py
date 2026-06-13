"""
Validates all MetroidPrime2Exit destination strings against known region names.
Finds destinations that point to non-existent regions.
Run with: python tools/validate_destinations.py
"""

import re
import sys
from pathlib import Path

src = Path(__file__).parent.parent / "src" / "logic"

# --- Step 1: Collect all valid region names ---
# Full region name = "{area_title_case} - {class.name} ({class.desc})" or "{area} - {class.name}"
# We can reconstruct this from class definitions.

name_re = re.compile(r'^\s+name\s*=\s*"([^"]+)"', re.MULTILINE)
desc_re = re.compile(r'^\s+desc\s*=\s*"([^"]+)"', re.MULTILINE)
class_re = re.compile(r'^class (\w+)\(MetroidPrime2Region\)', re.MULTILINE)

def snake_to_title(s: str) -> str:
    return " ".join(w[0].upper() + w[1:] for w in s.split("_"))

valid_regions: set[str] = set()
file_region_map: dict[str, list[str]] = {}

for py_file in sorted(src.rglob("*.py")):
    if py_file.name.startswith("__"):
        continue
    text = py_file.read_text(encoding="utf-8")
    classes = class_re.findall(text)
    if not classes:
        continue

    # Area name comes from the parent directory (e.g. temple_grounds -> Temple Grounds)
    area_dir = py_file.parent.name
    area_name = snake_to_title(area_dir)

    # Split text into per-class sections
    class_sections = re.split(r'^class \w+\(MetroidPrime2Region\)', text, flags=re.MULTILINE)
    class_sections = class_sections[1:]  # skip before first class

    file_regions = []
    for section in class_sections:
        # Get first name and desc in this section
        name_m = name_re.search(section)
        desc_m = desc_re.search(section)
        if not name_m:
            continue
        room_name = name_m.group(1)
        if desc_m:
            full = f"{area_name} - {room_name} ({desc_m.group(1)})"
        else:
            full = f"{area_name} - {room_name}"
        valid_regions.add(full)
        file_regions.append(full)
    file_region_map[str(py_file.relative_to(src))] = file_regions

# --- Step 2: Collect all destination strings ---
dest_re = re.compile(r'destination\s*=\s*"([^"]+)"')

bad: list[tuple[str, str]] = []

for py_file in sorted(src.rglob("*.py")):
    if py_file.name.startswith("__"):
        continue
    text = py_file.read_text(encoding="utf-8")
    for m in dest_re.finditer(text):
        dest = m.group(1)
        # Strip P| E| prefixes
        lookup = dest[2:] if dest.startswith(("P|", "E|")) else dest
        if lookup not in valid_regions:
            bad.append((str(py_file.relative_to(src)), dest))

# --- Report ---
if not bad:
    print("All destinations are valid!")
else:
    print(f"Found {len(bad)} invalid destination(s):\n")
    for f, d in bad:
        print(f"  {f}")
        print(f"    -> '{d}'")
        # Suggest close matches
        stripped = d[2:] if d.startswith(("P|", "E|")) else d
        close = [r for r in valid_regions if stripped.lower().replace(" ", "") == r.lower().replace(" ", "")]
        if close:
            print(f"    SUGGESTION: '{close[0]}'")
        print()

print(f"\nTotal valid region names: {len(valid_regions)}")
