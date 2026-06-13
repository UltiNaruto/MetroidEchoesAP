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
class SanctuaryEntrance(MetroidPrime2Region):
    name = "Sanctuary Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Power Junction",
            door=DoorCover.Light,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
                not (state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player)),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Temple Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Power Bomb Expansion)",
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
                not (state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player)),
            ]),
                condition_and([
                state.has("Sanctuary Fortress - Sanctuary Entrance | Event - Sanctuary Entrance Debris", player),
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_use_spider_ball(state, player),
                        condition_or([
                            # https://www.youtube.com/watch?v=wW_QjW48jwM
                            condition_and([
                                can_lay_bomb(state, player),
                                has_trick_enabled(state, player, "Bomb Jump"),
                            ]),
                            condition_and([
                                can_use_boost_ball(state, player),
                                condition_or([
                                    can_lay_bomb(state, player),
                                    # https://www.youtube.com/watch?v=wW_QjW48jwM&t=22s
                                    has_trick_enabled(state, player, "Movement"),
                                ]),
                            ]),
                            # https://www.youtube.com/watch?v=wW_QjW48jwM&t=37s
                            condition_and([
                                has_trick_enabled(state, player, "Instant Morph"),
                                has_trick_enabled(state, player, "Standable Terrain"),
                                condition_or([
                                    state.has("Space Jump Boots", player),
                                    has_trick_enabled(state, player, "Movement"),
                                ]),
                            ]),
                        ]),
                    ]),
                    # https://clips.twitch.tv/RoughTriangularSheepPermaSmug-lBZ81dzbFIH6a89O
                    condition_and([
                        state.has("Space Jump Boots", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                ]),
            ]),
            ]),
                state.has("Morph Ball", player),
            ]),
        )

        self.add_location(
            name="Event - Sanctuary Entrance Debris",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Sanctuary Entrance | Event - Sanctuary Entrance Debris",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
                not (state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player)),
            ]),
                condition_and([
                state.has("Scan Visor", player),
                condition_or([
                    condition_and([
                        can_use_spider_ball(state, player),
                        condition_or([
                            condition_and([
                                state.has("Morph Ball", player),
                                can_lay_pb(state, player),
                            ]),
                            # https://www.youtube.com/watch?v=2brsOGq0P7Y
                            condition_and([
                                can_use_screw_attack(state, player),
                                has_trick_enabled(state, player, "Movement"),
                            ]),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=2brsOGq0P7Y&t=72s
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                    # https://www.youtube.com/watch?v=2brsOGq0P7Y&t=55s
                    condition_and([
                        can_lay_pb(state, player),
                        state.has("Space Jump Boots", player),
                        state.has("Morph Ball", player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        has_trick_enabled(state, player, "Slope Jump"),
                        not (state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player)),
                    ]),
                ]),
                state.has("SancEntranceReload", player),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Sanctuary Entrance Fight",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Sanctuary Entrance | Event - Sanctuary Entrance Fight",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player),
                ]),
                not (state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player)),
            ]),
        )
