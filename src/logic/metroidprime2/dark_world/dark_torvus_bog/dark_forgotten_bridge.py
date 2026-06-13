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
class DarkForgottenBridge(MetroidPrime2Region):
    name = "Dark Forgotten Bridge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Brooding Ground",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: condition_and([
                condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    has_trick_enabled(state, player, "Jump Off Enemy"),
                    has_trick_enabled(state, player, "Standable Terrain"),
                    condition_or([
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_and([
                            can_activate_safe_zone(state, player),
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
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_and([
                            not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Space Jump Boots", player),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            state.has("Morph Ball", player),
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                    condition_or([
                        can_activate_safe_zone(state, player),
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
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Dark Torvus Bog - Dark Forgotten Bridge | Event - Dark Forgotten Bridge Rotated", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    # Same as Light World -> https://www.youtube.com/watch?v=tvc4XMSPWl4
                    condition_and([
                        state.has("Scan Visor", player),
                        has_trick_enabled(state, player, "Extended Dash"),
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
                                can_use_screw_attack(state, player),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            # Same as Light World ->  https://www.youtube.com/watch?v=fRwM33F0C5s
                            condition_and([
                                state.has("Scan Visor", player),
                                has_trick_enabled(state, player, "Combat/Scan Dash"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            # Same as Light World -> https://www.youtube.com/watch?v=Uv9du120y68
                            condition_and([
                                state.has("Morph Ball", player),
                                has_trick_enabled(state, player, "Roll Jump"),
                                not (state.has("Dark Torvus Bog - Dark Forgotten Bridge | Event - Dark Forgotten Bridge Rotated", player)),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Dark Falls",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                condition_or([
                    condition_and([
                        can_activate_safe_zone(state, player),
                        not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                    ]),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    # Double Bomb Jump
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Movement"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
                condition_and([
                state.has("Torvus Bog - Forgotten Bridge | Event - Forgotten Bridge Gate", player),
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
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        condition_or([
                            condition_and([
                                can_use_screw_attack(state, player, z_axis=True),
                                has_trick_enabled(state, player, "Bomb Jump"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            condition_and([
                                not (state.has("Dark Torvus Bog - Dark Forgotten Bridge | Event - Dark Forgotten Bridge Rotated", player)),
                                has_trick_enabled(state, player, "Bomb Jump"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Putrid Alcove",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Dark Arena Tunnel",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    has_trick_enabled(state, player, "Jump Off Enemy"),
                    has_trick_enabled(state, player, "Standable Terrain"),
                    condition_or([
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_and([
                            can_activate_safe_zone(state, player),
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
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_and([
                            not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Space Jump Boots", player),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            state.has("Morph Ball", player),
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                    condition_or([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
                condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        state.has("Dark Torvus Bog - Dark Forgotten Bridge | Event - Dark Forgotten Bridge Rotated", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Movement"),
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
        ),
        MetroidPrime2Exit(
            destination="P|Torvus Bog - Forgotten Bridge",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                condition_or([
                    condition_and([
                        can_activate_safe_zone(state, player),
                        not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                    ]),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    # Double Bomb Jump
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Movement"),
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
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Event - Dark Forgotten Bridge Rotated",
            locked_item=MetroidPrime2Item(
                name="Dark Torvus Bog - Dark Forgotten Bridge | Event - Dark Forgotten Bridge Rotated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    has_trick_enabled(state, player, "Jump Off Enemy"),
                    has_trick_enabled(state, player, "Standable Terrain"),
                    condition_or([
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_and([
                            can_activate_safe_zone(state, player),
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
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_and([
                            not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Space Jump Boots", player),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            state.has("Morph Ball", player),
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                    condition_or([
                        can_activate_safe_zone(state, player),
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
                    condition_and([
                        not (state.has("Dark Torvus Bog - Sacrificial Chamber | Event - Grapple Guardian", player)),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                    ]),
                    # https://www.youtube.com/watch?v=TMTKSnUB-zE
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                ]),
            ]),
            ]),
        )
