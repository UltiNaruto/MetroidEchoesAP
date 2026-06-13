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
class UndertempleShaft(MetroidPrime2Region):
    name = "Undertemple Shaft"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Crypt Tunnel",
            door=DoorCover.Light,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_use_grapple_beam(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            has_trick_enabled(state, player, "Roll Jump"),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                        condition_and([
                            can_use_screw_attack(state, player),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                            state.has("Scan Visor", player),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Undertemple Access",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Save Station 2",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        condition_or([
                            condition_and([
                                has_trick_enabled(state, player, "Movement"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                                not (False),
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
                        has_trick_enabled(state, player, "Roll Jump"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Sacrificial Chamber Tunnel",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_use_grapple_beam(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Scan Visor", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                        condition_and([
                            state.has("Morph Ball", player),
                            has_trick_enabled(state, player, "Roll Jump"),
                        ]),
                    ]),
                ]),
            ]),
        ),
    ]
