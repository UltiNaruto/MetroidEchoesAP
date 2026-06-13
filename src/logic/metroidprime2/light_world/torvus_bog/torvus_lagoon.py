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
class TorvusLagoon(MetroidPrime2Region):
    name = "Torvus Lagoon"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Save Station A",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                # https://www.youtube.com/watch?v=VO50mC6OMy4
                has_trick_enabled(state, player, "Standable Terrain"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Light)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Torvus Lagoon | Event - Torvus Lagoon Gates", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=5Rd-0l12zIo
                    condition_and([
                        has_trick_enabled(state, player, "Slope Jump"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Ruined Alcove",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Torvus Bog - Torvus Lagoon | Event - Torvus Lagoon Gates", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=5Rd-0l12zIo
                    condition_and([
                        has_trick_enabled(state, player, "Slope Jump"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                ]),
            ]),
                state.has("Torvus Bog - Torvus Lagoon | Event - Torvus Lagoon Gates", player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_or([
                # https://www.youtube.com/watch?v=UydDNpPdLRI
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Air Underwater"),
                ]),
                state.has("Gravity Boost", player),
            ]),
        )

        self.add_location(
            name="Event - Torvus Lagoon Gates",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Torvus Lagoon | Event - Torvus Lagoon Gates",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Torvus Bog - Torvus Lagoon | Event - Torvus Lagoon Gates", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=5Rd-0l12zIo
                    condition_and([
                        has_trick_enabled(state, player, "Slope Jump"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                ]),
            ]),
                state.has("Scan Visor", player),
            ]),
        )
