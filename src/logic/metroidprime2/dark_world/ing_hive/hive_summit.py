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
class HiveSummit(MetroidPrime2Region):
    name = "Hive Summit"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Aerie",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                can_activate_safe_zone(state, player),
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_use_spider_ball(state, player),
                        condition_or([
                            condition_and([
                                can_use_boost_ball(state, player),
                                condition_or([
                                    condition_and([
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                        condition_or([
                                            state.has("Space Jump Boots", player),
                                            # https://www.youtube.com/watch?v=Lkzy0HJEO6k&t=33s
                                            has_trick_enabled(state, player, "Movement"),
                                        ]),
                                    ]),
                                    # https://www.youtube.com/watch?v=Lkzy0HJEO6k&t=16s
                                    condition_and([
                                        can_lay_bomb(state, player),
                                        has_trick_enabled(state, player, "Bomb Jump"),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                    ]),
                                ]),
                            ]),
                            condition_and([
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                                condition_or([
                                    # https://www.youtube.com/watch?v=Lkzy0HJEO6k
                                    condition_and([
                                        state.has("Space Jump Boots", player),
                                        has_trick_enabled(state, player, "Standable Terrain"),
                                    ]),
                                    # https://www.youtube.com/watch?v=Lkzy0HJEO6k&t=60s
                                    condition_and([
                                        can_lay_bomb(state, player),
                                        has_trick_enabled(state, player, "Bomb Jump"),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=4bPTa8JvBBA
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Boost Jump"),
                        has_trick_enabled(state, player, "Single Room Out of Bounds"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Aerie",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]
