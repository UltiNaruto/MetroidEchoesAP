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


# REVIEW: asymmetric intra-room traversal detected — consider splitting into sub-regions
class TransitStation(MetroidPrime2Region):
    name = "Transit Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Reactor Core",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Ing Hive - Hive Portal Chamber",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_or([
                    # https://www.youtube.com/watch?v=4aYwB8NJnbM
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Slope Jump"),
                    ]),
                    # https://www.youtube.com/watch?v=5xM-JJK94PY
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Main Research",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Ing Hive - Hive Portal Chamber",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                state.has("Morph Ball", player),
                can_lay_pb(state, player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Power Bomb Expansion)",
            can_access=lambda state, player: condition_and([
                condition_or([
                # https://www.youtube.com/watch?v=4aYwB8NJnbM
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
                # https://www.youtube.com/watch?v=5xM-JJK94PY
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                ]),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_spider_ball(state, player),
                ]),
                # https://www.youtube.com/watch?v=XbJsYZe8rd0
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                ]),
            ]),
            ]),
        )
