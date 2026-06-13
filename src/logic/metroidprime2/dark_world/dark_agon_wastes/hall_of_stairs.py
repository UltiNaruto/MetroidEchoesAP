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
class HallOfStairs(MetroidPrime2Region):
    name = "Hall of Stairs"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Agon Wastes - Save Station 3",
            door=DoorCover.Missile,
            rule=lambda state, player: condition_and([
                condition_or([
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    can_activate_safe_zone(state, player),
                ]),
            ]),
                condition_and([
                condition_or([
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    can_activate_safe_zone(state, player),
                ]),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            condition_and([
                                can_use_dark_beam(state, player),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Standable Terrain"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        state.has("Morph Ball", player),
                        condition_or([
                            condition_and([
                                can_use_boost_ball(state, player),
                                has_trick_enabled(state, player, "Movement"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            # https://youtu.be/9YUW5K-nkGg?si=Om_MB9scqa2d5S98
                            condition_or([
                                condition_and([
                                    can_lay_bomb(state, player),
                                    has_trick_enabled(state, player, "Bomb Jump"),
                                    has_trick_enabled(state, player, "Standable Terrain"),
                                    condition_or([
                                        has_dark_suit(state, player),
                                        has_light_suit(state, player),
                                        state.count("Energy Tank", player) >= 1,
                                    ]),
                                ]),
                                # https://www.youtube.com/watch?v=fnqMz66rGQY
                                condition_and([
                                    can_lay_bomb(state, player),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                    has_trick_enabled(state, player, "Standable Terrain"),
                                    condition_or([
                                        has_dark_suit(state, player),
                                        has_light_suit(state, player),
                                        state.count("Energy Tank", player) >= 1,
                                    ]),
                                ]),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        can_use_dark_beam(state, player),
                        can_use_light_beam(state, player),
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        state.has("Scan Visor", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Agon Wastes - Dark Oasis",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
