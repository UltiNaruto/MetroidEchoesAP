#!/usr/bin/env python3
"""
Translates a Randovania MP2 logic-database JSON region file into
MetroidEchoesAP Python room files.

Usage:
    python tools/rando_translator.py <region.json> <output_dir> --prefix "Agon Wastes"

Example (after downloading Agon Wastes.json from Randovania):
    python tools/rando_translator.py "Agon Wastes.json" \\
        src/logic/metroidprime2/light_world/agon_wastes/ \\
        --prefix "Agon Wastes"

One .py file is written per Randovania area (room).
Look for "# TODO" and "# TRICK" comments — those need human review.
"# REVIEW: asymmetric" means the room likely needs sub-region splitting.
"""

import argparse
import json
import re
from pathlib import Path
from typing import Optional

# ── Mapping: Randovania item resource name → MetroidEchoesAP expression ──────

ITEM_MAP: dict[str, str] = {
    # Beams — use helpers because of progressive variants
    "Power":        "can_use_power_beam(state, player)",
    "Dark":         "can_use_dark_beam(state, player)",
    "Light":        "can_use_light_beam(state, player)",
    "Annihilator":  "can_use_annihilator_beam(state, player)",
    "Supers":       "can_use_super_missile(state, player)",
    "Darkburst":    "can_use_darkburst(state, player)",
    "Sunburst":     "can_use_sunburst(state, player)",
    "SonicBoom":    "can_use_sonic_boom(state, player)",
    "Charge":       'state.has("Charge Beam", player)',
    # Visors
    "Combat":       'state.has("Combat Visor", player)',
    "Scan":         'state.has("Scan Visor", player)',
    "DarkVisor":    'state.has("Dark Visor", player)',
    "Echo":         'state.has("Echo Visor", player)',
    # Suits — use helpers because of progressive variant
    "Varia":        'state.has("Varia Suit", player)',
    "DarkSuit":     "has_dark_suit(state, player)",
    "LightSuit":    "has_light_suit(state, player)",
    # Movement
    "MorphBall":    'state.has("Morph Ball", player)',
    "Bombs":        "can_lay_bomb(state, player)",
    "PowerBomb":    "can_lay_pb(state, player)",
    "Boost":        "can_use_boost_ball(state, player)",
    "Spider":       "can_use_spider_ball(state, player)",
    "SpaceJump":    'state.has("Space Jump Boots", player)',
    "Grapple":      "can_use_grapple_beam(state, player)",
    "ScrewAttack":  "can_use_screw_attack(state, player)",
    "Seekers":      "can_use_seeker_launcher(state, player)",
    "Gravity":      'state.has("Gravity Boost", player)',
    # Translators
    "Violet":       'state.has("Violet Translator", player)',
    "Amber":        'state.has("Amber Translator", player)',
    "Emerald":      'state.has("Emerald Translator", player)',
    "Cobalt":       'state.has("Cobalt Translator", player)',
    # Misc
    "SpringBall":   'state.has("Spring Ball", player)',
    "CannonBall":   'state.has("Cannon Ball", player)',
    "DoubleDamage": 'state.has("Double Damage", player)',
    "ETM":          'state.has("Energy Transfer Module", player)',
    # Keys
    "AgonKey1":     'state.has("Dark Agon Key 1", player)',
    "AgonKey2":     'state.has("Dark Agon Key 2", player)',
    "AgonKey3":     'state.has("Dark Agon Key 3", player)',
    "TorvusKey1":   'state.has("Dark Torvus Key 1", player)',
    "TorvusKey2":   'state.has("Dark Torvus Key 2", player)',
    "TorvusKey3":   'state.has("Dark Torvus Key 3", player)',
    "HiveKey1":     'state.has("Ing Hive Key 1", player)',
    "HiveKey2":     'state.has("Ing Hive Key 2", player)',
    "HiveKey3":     'state.has("Ing Hive Key 3", player)',
    "TempleKey1":   'state.has("Sky Temple Key 1", player)',
    "TempleKey2":   'state.has("Sky Temple Key 2", player)',
    "TempleKey3":   'state.has("Sky Temple Key 3", player)',
    "TempleKey4":   'state.has("Sky Temple Key 4", player)',
    "TempleKey5":   'state.has("Sky Temple Key 5", player)',
    "TempleKey6":   'state.has("Sky Temple Key 6", player)',
    "TempleKey7":   'state.has("Sky Temple Key 7", player)',
    "TempleKey8":   'state.has("Sky Temple Key 8", player)',
    "TempleKey9":   'state.has("Sky Temple Key 9", player)',
}

# Items where the required amount matters
ITEM_AMOUNT_MAP: dict[str, object] = {
    "Missile":    lambda n: f"has_missile_count(state, player, {n})",
    "DarkAmmo":   lambda n: f"has_dark_ammo(state, player, {n})",
    "LightAmmo":  lambda n: f"has_light_ammo(state, player, {n})",
    "EnergyTank": lambda n: f'state.count("Energy Tank", player) >= {n}',
    "PowerBomb":  lambda n: (
        f"can_lay_pb(state, player, {n})" if n > 1 else "can_lay_pb(state, player)"
    ),
}

# Randovania requirement template name → MetroidEchoesAP expression
TEMPLATE_MAP: dict[str, str] = {
    "Use Screw Attack (Space Jump)":
        "can_use_screw_attack(state, player)",
    "Use Screw Attack (No Space Jump)":
        "can_use_screw_attack(state, player, z_axis=True)",
    "Shoot Dark Beam":
        "can_use_dark_beam(state, player)",
    "Shoot Light Beam":
        "can_use_light_beam(state, player)",
    "Shoot Annihilator Beam":
        "can_use_annihilator_beam(state, player)",
    "Shoot Darkburst":
        "can_use_darkburst(state, player)",
    "Shoot Sunburst":
        "can_use_sunburst(state, player)",
    "Shoot Sonic Boom":
        "can_use_sonic_boom(state, player)",
    "Shoot Supers":
        "can_use_super_missile(state, player)",
    "Shoot Any Beam":
        "condition_or([can_use_power_beam(state, player), can_use_dark_beam(state, player), "
        "can_use_light_beam(state, player), can_use_annihilator_beam(state, player)])",
    "Open Normal Door":
        "True",
    "Activate Safe Zone":
        "can_activate_safe_zone(state, player)",
    "Has Suit":
        "condition_or([has_dark_suit(state, player), has_light_suit(state, player)])",
    "Destroy Seeker Locks":
        "can_use_seeker_launcher(state, player)",
    "Destroy Underwater Seeker Locks":
        "condition_and([state.has('Gravity Boost', player), can_use_seeker_launcher(state, player)])",
    "Kill Quad MB":
        "condition_or([can_use_dark_beam(state, player), can_use_light_beam(state, player), "
        "can_use_annihilator_beam(state, player), has_missile_count(state, player, 5)])",
    "Activate Bomb Slot without Bombs (Space Jump)":
        "condition_and([can_use_boost_ball(state, player), state.has('Space Jump Boots', player)])",
    "Activate Bomb Slot without Bombs (No Space Jump)":
        "can_use_boost_ball(state, player)",
    "Activate Bomb Slot without Bombs (Instant Morph)":
        "condition_and([state.has('Morph Ball', player), can_lay_bomb(state, player)])",
}

# Randovania dock_weakness name → DoorCover enum value
DOOR_WEAKNESS_MAP: dict[str, str] = {
    "Normal Door":                  "DoorCover.Any",
    "Missile Blast Shield":         "DoorCover.Missile",
    "Seeker Launcher Blast Shield": "DoorCover.Seeker",
    "Dark Blast Shield":            "DoorCover.Dark",
    "Light Blast Shield":           "DoorCover.Light",
    "Annihilator Blast Shield":     "DoorCover.Annihilator",
    "Super Missile Blast Shield":   "DoorCover.SuperMissile",
    "Power Bomb Blast Shield":      "DoorCover.PowerBomb",
    "Darkburst Blast Shield":       "DoorCover.Darkburst",
    "Sunburst Blast Shield":        "DoorCover.Sunburst",
    "Sonic Boom Blast Shield":      "DoorCover.SonicBoom",
    "Morph Ball Door":              "DoorCover.MorphBallTunnel",
    "Bomb Door":                    "DoorCover.Bomb",
    "Charge Beam Blast Shield":     "DoorCover.ChargeBeam_Any",
    "Scan Visor":                   "DoorCover.ScanVisor",
    "Violet Translator Gate":       "DoorCover.VioletTranslator",
    "Amber Translator Gate":        "DoorCover.AmberTranslator",
    "Emerald Translator Gate":      "DoorCover.EmeraldTranslator",
    "Cobalt Translator Gate":       "DoorCover.CobaltTranslator",
    # Elevators and portals: door cover is always open; activation is in the rule
    "Elevator":                     "DoorCover.Opened",
    "No Return Portal":             "DoorCover.Opened",
    "Portal":                       "DoorCover.Opened",
}

# ── Requirement translation ───────────────────────────────────────────────────

def _split_comment(s: str) -> tuple[str, str | None]:
    """Strip a trailing inline # comment from the last non-empty line of s.

    Returns (clean_code, trailing_comment_or_None).
    Works for both single-line and multi-line expressions.
    """
    if '\n' in s:
        lines = s.split('\n')
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i]
            if line.strip():
                if '#' in line:
                    idx = line.index('#')
                    lines[i] = line[:idx].rstrip()
                    return '\n'.join(lines), line[idx:]
                break  # last non-empty line has no comment — safe
        return s, None
    if '#' in s:
        idx = s.index('#')
        return s[:idx].rstrip(), s[idx:]
    return s, None


def _fmt(exprs: list[str], op: str, indent: int) -> str:
    """Wrap expressions in condition_and/condition_or.

    Inline # comments (e.g. TRICK/EVENT markers) are moved to a line AFTER
    the expression so they cannot eat the separator comma that follows it.
    """
    fn = "condition_and" if op == "and" else "condition_or"
    pad = " " * indent
    inner_pad = pad + "    "
    rows: list[str] = []
    for expr in exprs:
        code, comment = _split_comment(expr)
        rows.append(f"{inner_pad}{code},")
        if comment:
            rows.append(f"{inner_pad}{comment}")
    return f"{fn}([\n" + "\n".join(rows) + f"\n{pad}])"


def translate_req(req: dict, indent: int = 0) -> str:
    """Recursively translate a Randovania requirement node to a Python expression."""
    t = req.get("type", "trivial")

    if t == "trivial":
        return "True"
    if t == "impossible":
        return "False"

    if t == "template":
        name = req["data"]
        return TEMPLATE_MAP.get(name, f"True  # TODO: expand template '{name}'")

    if t == "resource":
        d = req["data"]
        rtype, name, amount, negate = d["type"], d["name"], d["amount"], d["negate"]

        if rtype == "items":
            # Amount-dependent helpers first
            if name in ITEM_AMOUNT_MAP and amount > 1:
                expr = ITEM_AMOUNT_MAP[name](amount)
            elif name in ITEM_MAP:
                expr = ITEM_MAP[name]
            elif name in ITEM_AMOUNT_MAP:
                expr = ITEM_AMOUNT_MAP[name](amount)
            else:
                expr = f"True  # TODO: unknown item '{name}' amount={amount}"

        elif rtype == "tricks":
            # Randovania trick names are generic (BombJump, SlopeJump…).
            # MetroidEchoesAP uses room-specific trick strings.
            # Leave a placeholder — the reviewer replaces this with
            # has_trick_enabled(state, player, "<Area> - <Room> | <description>")
            return (
                f"False  # TRICK: {name} level={amount} "
                f"— replace with has_trick_enabled()"
            )

        elif rtype == "events":
            # Randovania event flags become locked-item locations in MetroidEchoesAP.
            # The exact item name almost certainly differs — reviewer must update.
            expr = f'state.has("{name}", player)'  # EVENT: {name} — verify item name

        elif rtype == "damage":
            # Dark-world damage resistance approximation
            if "Dark" in name:
                expr = (
                    "condition_or([\n"
                    f"{' ' * (indent + 4)}has_dark_suit(state, player),\n"
                    f"{' ' * (indent + 4)}has_light_suit(state, player),\n"
                    f"{' ' * (indent + 4)}state.count(\"Energy Tank\", player) >= 1,\n"
                    f"{' ' * indent}])"
                )
            else:
                expr = "True"  # non-dark damage — no equivalent check

        elif rtype == "versions":
            expr = "True"  # version flag, not tracked

        elif rtype == "misc":
            # Randovania misc flags (e.g. RoomRando) are never active in MetroidEchoesAP.
            # resource value = False; negate=True ("require NOT active") → True at runtime.
            expr = "False"

        else:
            expr = "True"  # TODO: resource type '{rtype}' name='{name}'

        if negate:
            # Strip any trailing inline comment so the closing ')' is not eaten.
            clean = expr.split('#')[0].rstrip() if '#' in expr and '\n' not in expr else expr
            return f"not ({clean})"
        return expr

    if t in ("and", "or"):
        items_list = req["data"].get("items", [])
        comment = req["data"].get("comment")

        if not items_list:
            return "True"

        translated = [translate_req(item, indent + 4) for item in items_list]

        if t == "and":
            non_trivial = [e for e in translated if e not in ("True", "")]
            if not non_trivial:
                return "True"
            if len(non_trivial) == 1:
                result = non_trivial[0]
            else:
                result = _fmt(non_trivial, "and", indent)
        else:
            if any(e == "True" for e in translated):
                return "True"
            non_false = [e for e in translated if e != "False"]
            if not non_false:
                return "False"
            if len(non_false) == 1:
                result = non_false[0]
            else:
                result = _fmt(non_false, "or", indent)

        if comment:
            result = f"# {comment}\n{' ' * indent}{result}"
        return result

    return f"True  # TODO: unknown req type '{t}'"


# ── Intra-room BFS ────────────────────────────────────────────────────────────

def _combine_and(a: str, b: str, indent: int = 12) -> str:
    if a == "True":
        return b
    if b == "True":
        return a
    return _fmt([a, b], "and", indent)


def _combine_or(a: str, b: str, indent: int = 12) -> str:
    if a == "True" or b == "True":
        return "True"
    if a == "False":
        return b
    if b == "False":
        return a
    return _fmt([a, b], "or", indent)


def bfs_reach(default_node: str, connections: dict[str, dict]) -> dict[str, str]:
    """
    BFS from default_node over intra-room connections.
    Returns {node_name: Python expression to reach it from default_node}.

    First-visit-wins: once a node is reached we don't re-expand it.
    This prevents exponential string growth in cyclic graphs at the cost of
    missing some alternative paths (acceptable — reviewers fix edge cases).
    """
    reached: dict[str, str] = {default_node: "True"}
    queue: list[str] = [default_node]

    while queue:
        current = queue.pop(0)
        cur_req = reached[current]

        for neighbor, edge_dict in connections.get(current, {}).items():
            if neighbor in reached:
                continue  # already visited — skip to avoid cycles
            edge_req = translate_req(edge_dict, indent=12)
            reached[neighbor] = _combine_and(cur_req, edge_req)
            queue.append(neighbor)

    return reached


# ── Per-area code generation ──────────────────────────────────────────────────

def _to_pascal(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", " ", s).title().replace(" ", "")


def _to_snake(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", s.lower()).strip("_")


def _door_cover(weakness: str) -> tuple[str, str | None]:
    """Return (enum_value, comment_or_None).  Comment goes on its own line."""
    if weakness in DOOR_WEAKNESS_MAP:
        return DOOR_WEAKNESS_MAP[weakness], None
    return "DoorCover.Any", f"# TODO: unknown weakness '{weakness}' — map to correct DoorCover"


def _is_trivial(expr: str) -> bool:
    return expr.strip() == "True"


def translate_area(
    area_name: str,
    area_data: dict,
    all_areas: dict,   # full region dict for cross-area weakness lookups
    prefix: str,
) -> str:
    """Return the Python source code for one MetroidEchoesAP room class."""
    nodes: dict[str, dict] = area_data["nodes"]
    default_node = area_data.get("default_node", next(iter(nodes)))

    # Build intra-room connection graph (only nodes within this area)
    connections: dict[str, dict] = {
        n: data.get("connections", {}) for n, data in nodes.items()
    }

    reach = bfs_reach(default_node, connections)

    # Detect rooms with asymmetric traversal (may need sub-region splitting)
    needs_review = False
    dock_nodes = [n for n, d in nodes.items() if d.get("node_type") == "dock"]
    for n in dock_nodes:
        req_there = reach.get(n, "False")
        # reverse: can we get back from n to default_node?
        rev_reach = bfs_reach(n, connections)
        req_back = rev_reach.get(default_node, "False")
        if not (_is_trivial(req_there) and _is_trivial(req_back)):
            if req_there != req_back:
                needs_review = True
                break

    class_name = _to_pascal(area_name)
    lines: list[str] = []

    if needs_review:
        lines.append(
            "# REVIEW: asymmetric intra-room traversal detected — "
            "consider splitting into sub-regions"
        )

    lines.append(f"class {class_name}(MetroidPrime2Region):")
    lines.append(f'    name = "{area_name}"')
    lines.append("    exits_ = [")

    # ── Exits (dock nodes) ────────────────────────────────────────────────────
    for node_name, node_data in nodes.items():
        if node_data.get("node_type") != "dock":
            continue

        conn = node_data.get("default_connection", {})
        if not conn:
            continue

        dest_region = conn.get("region", "")
        dest_area   = conn.get("area", "")
        dock_type   = node_data.get("dock_type", "door")
        weakness    = node_data.get("default_dock_weakness", "Normal Door")

        # Destination string with elevator/portal prefixes
        if dest_region == prefix:
            dest_str = f"{prefix} - {dest_area}"
        elif dock_type == "elevator":
            dest_str = f"E|{dest_region} - {dest_area}"
        elif dock_type == "portal":
            dest_str = f"P|{dest_region} - {dest_area}"
        else:
            dest_str = f"{dest_region} - {dest_area}"

        # DoorCover — prefer the DESTINATION dock's weakness (that's the blast
        # shield you're entering through) when it's in the same file; fall back
        # to the source weakness for cross-region connections.
        cover_val, cover_comment = _door_cover(weakness)
        if dest_region == prefix and dest_area in all_areas:
            dest_nodes = all_areas[dest_area].get("nodes", {})
            dest_node_name = conn.get("node", "")
            if dest_node_name in dest_nodes:
                dest_weakness = dest_nodes[dest_node_name].get("default_dock_weakness", weakness)
                cover_val, cover_comment = _door_cover(dest_weakness)

        rule = reach.get(node_name, "False")  # False = unreachable from default node

        # Portals that are not "No Return Portal" need activation logic
        if dock_type == "portal" and weakness != "No Return Portal":
            rule = _combine_and("can_activate_dark_portal(state, player)", rule)

        lines.append("        MetroidPrime2Exit(")
        lines.append(f'            destination="{dest_str}",')
        if cover_comment:
            lines.append(f"            {cover_comment}")
        lines.append(f"            door={cover_val},")
        lines.append(f"            rule=lambda state, player: {rule},")
        lines.append("        ),")

    lines.append("    ]")

    # ── Locations (pickup and event nodes) ────────────────────────────────────
    location_lines: list[str] = []

    for node_name, node_data in nodes.items():
        ntype = node_data.get("node_type", "generic")

        if ntype == "pickup":
            rule = reach.get(node_name, "True")
            location_lines.append(
                f"        self.add_location(\n"
                f'            name="{node_name}",\n'
                f"            can_access=lambda state, player: {rule},\n"
                f"        )"
            )

        elif ntype == "event":
            # Derive access: find what leads TO this event node
            access = "True"
            for src, src_conns in connections.items():
                if node_name in src_conns:
                    src_req  = reach.get(src, "True")
                    edge_req = translate_req(src_conns[node_name], indent=12)
                    access   = _combine_and(src_req, edge_req)
                    break  # use first referencing node

            event_item = f"{prefix} - {area_name} | {node_name}"
            location_lines.append(
                f"        self.add_location(\n"
                f'            name="{node_name}",\n'
                f"            locked_item=MetroidPrime2Item(\n"
                f'                name="{event_item}",\n'
                f"                classification=ItemClassification.progression,\n"
                f"                code=None,\n"
                f"                player=player,\n"
                f"            ),\n"
                f"            can_access=lambda state, player: {access},\n"
                f"        )"
            )

    if location_lines:
        lines.append("")
        lines.append("    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):")
        lines.append("        super().__init__(region_name, player, multiworld)")
        lines.append("")
        lines.append("\n\n".join(location_lines))

    return "\n".join(lines)


# ── File generation ───────────────────────────────────────────────────────────

_IMPORTS = """\
from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_dark_portal,
    can_activate_light_portal,
    can_activate_safe_zone,
    can_lay_bomb,
    can_lay_bomb_or_pb,
    can_lay_pb,
    can_use_annihilator_beam,
    can_use_boost_ball,
    can_use_charged_annihilator_beam,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_charged_power_beam,
    can_use_dark_beam,
    can_use_darkburst,
    can_use_grapple_beam,
    can_use_light_beam,
    can_use_power_beam,
    can_use_screw_attack,
    can_use_seeker_launcher,
    can_use_sonic_boom,
    can_use_spider_ball,
    can_use_sunburst,
    can_use_super_missile,
    has_dark_ammo,
    has_dark_suit,
    has_light_ammo,
    has_light_suit,
    has_missile_count,
    has_pb_count,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or
"""


def generate_file(
    area_name: str,
    area_data: dict,
    all_areas: dict,
    prefix: str,
) -> tuple[str, str]:
    """Return (filename, full_source) for one room."""
    body   = translate_area(area_name, area_data, all_areas, prefix)
    source = _IMPORTS + "\n\n" + body + "\n"
    return _to_snake(area_name) + ".py", source


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Translate a Randovania MP2 region JSON to MetroidEchoesAP Python files."
    )
    parser.add_argument("input_json", help="Randovania region JSON file (e.g. 'Agon Wastes.json')")
    parser.add_argument("output_dir", help="Directory to write generated .py files")
    parser.add_argument("--prefix", required=True,
                        help='MetroidEchoesAP area prefix, e.g. "Agon Wastes"')
    args = parser.parse_args()

    with open(args.input_json, encoding="utf-8") as f:
        data = json.load(f)

    # Randovania region files are either {"areas": {...}} or just {"RoomName": {...}}
    areas: dict = data.get("areas", data)

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    generated = []
    for area_name, area_data in areas.items():
        filename, source = generate_file(area_name, area_data, areas, args.prefix)
        (out / filename).write_text(source, encoding="utf-8")
        generated.append(filename)
        print(f"  {filename}")

    # Bare __init__.py so the package is importable
    init = out / "__init__.py"
    if not init.exists():
        init.write_text("\n", encoding="utf-8")

    print(f"\n{len(generated)} files written to {out}")
    print("Next steps:")
    print("  1. Search for '# TRICK' comments — replace with has_trick_enabled() calls")
    print("  2. Search for '# REVIEW: asymmetric' — split those rooms into sub-regions")
    print("  3. Search for '# EVENT' — verify event item names match what other rooms expect")
    print("  4. Search for '# TODO' — any remaining unknowns")


if __name__ == "__main__":
    main()
