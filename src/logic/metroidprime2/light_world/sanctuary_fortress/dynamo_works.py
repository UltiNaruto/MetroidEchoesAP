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
class DynamoWorks(MetroidPrime2Region):
    name = "Dynamo Works"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Workers Path",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Ing Hive - Hive Dynamo Works",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                condition_and([
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
                condition_or([
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_use_spider_ball(state, player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
            ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Dynamo Storage",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
                condition_or([
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Central Area Transport East",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                condition_and([
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
                condition_or([
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_use_spider_ball(state, player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
            ]),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_spider_ball(state, player),
                    state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
                ]),
                # https://www.youtube.com/watch?v=yrXFvJcN308
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=12HEtxdV0b0
                    condition_or([
                        has_trick_enabled(state, player, "Slope Jump"),
                        # https://www.youtube.com/watch?v=12HEtxdV0b0&t=12s
                        condition_and([
                            state.has("Morph Ball", player),
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Space Jump"),
                        ]),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Dynamo Access",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
                condition_or([
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_use_spider_ball(state, player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
            ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Spider Ball)",
            can_access=lambda state, player: state.has(
                "Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player
            ),
        )

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
                condition_or([
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_use_spider_ball(state, player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Dynamo Works Quads Gone",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Dynamo Works | Event - Dynamo Works Quads Gone",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
            ]),
        )

        self.add_location(
            name="Event - Spider Guardian",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Dynamo Works | Event - Spider Guardian",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                can_use_boost_ball(state, player),
                can_lay_bomb(state, player),
                state.has("Sanctuary Fortress - Dynamo Works | Event - Dynamo Works Quads Gone", player),
                # Spider Guardian is a Difficult Boss.
                condition_or([
                    has_trick_enabled(state, player, "Combat"),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
        )
