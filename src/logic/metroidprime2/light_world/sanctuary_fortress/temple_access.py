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
class TempleAccess(MetroidPrime2Region):
    name = "Temple Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Main Gyro Chamber",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Sanctuary Temple",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Sanctuary Fortress - Temple Access | Event - Quad", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_lay_bomb(state, player),
                        # https://www.youtube.com/watch?v=apnuLwmVQZ8&t=12s
                        condition_or([
                            # https://www.youtube.com/watch?v=apnuLwmVQZ8
                            condition_and([
                                can_use_screw_attack(state, player),
                                has_trick_enabled(state, player, "Bomb Space Jump"),
                            ]),
                            has_trick_enabled(state, player, "Bomb Space Jump"),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=y5GgfLSG2lQ
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Quad",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Temple Access | Event - Quad",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Knowledge"),
                    condition_or([
                        condition_and([
                            state.has("Sanctuary Fortress - Temple Access | Event - Activate Cannon", player),
                            state.has("Morph Ball", player),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                            can_use_screw_attack(state, player, z_axis=True),
                            not (False),
                        ]),
                    ]),
                ]),
                condition_or([can_use_dark_beam(state, player), can_use_light_beam(state, player), can_use_annihilator_beam(state, player), has_missile_count(state, player, 5)]),
            ]),
        )

        self.add_location(
            name="Event - Activate Cannon",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Temple Access | Event - Activate Cannon",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Dark Visor", player),
                has_missile_count(state, player, 4),
                can_use_seeker_launcher(state, player),
            ]),
        )
