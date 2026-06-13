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
class WatchStation(MetroidPrime2Region):
    name = "Watch Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Watch Station Access",
            door=DoorCover.Light,
            rule=lambda state, player: # No Space Jump https://www.youtube.com/watch?v=z2zCtuLRRvc
            condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Movement"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Central Area Transport West",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Ing Hive - Aerial Training Site",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                state.has("Sanctuary Fortress - Watch Station | Event - Watch Station Portal Gate", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Grand Abyss",
            door=DoorCover.Any,
            rule=lambda state, player: # No Space Jump https://www.youtube.com/watch?v=z2zCtuLRRvc&t=8s
            condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Movement"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Sentinel's Path",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                # No Space Jump https://www.youtube.com/watch?v=z2zCtuLRRvc
            condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Movement"),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_spider_ball(state, player),
                    # Instant Morph -> https://www.youtube.com/watch?v=2zk_smeEbm8&t=19s
                    condition_or([
                        can_lay_bomb(state, player),
                        # Wall Boost -> https://www.youtube.com/watch?v=2zk_smeEbm8
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        has_trick_enabled(state, player, "Instant Morph"),
                    ]),
                ]),
                can_use_screw_attack(state, player),
                # Standable Terrain -> https://www.youtube.com/watch?v=2zk_smeEbm8&t=36s
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Standable Terrain"),
                ]),
                # Z-Axis -> https://www.youtube.com/watch?v=2zk_smeEbm8&t=50s
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Beam Ammo Expansion)",
            can_access=lambda state, player: condition_and([
                not (False),
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Movement"),
                    ]),
                ]),
                condition_or([
                    # https://www.youtube.com/watch?v=nvDCHnonMM0
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Single Room Out of Bounds"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        has_trick_enabled(state, player, "Single Room Out of Bounds"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
                state.has("Morph Ball", player),
            ]),
        )

        self.add_location(
            name="Event - Watch Station Portal Gate",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Watch Station | Event - Watch Station Portal Gate",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                # No Space Jump https://www.youtube.com/watch?v=z2zCtuLRRvc
            condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Movement"),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_use_spider_ball(state, player),
                can_lay_bomb(state, player),
            ]),
            ]),
        )
