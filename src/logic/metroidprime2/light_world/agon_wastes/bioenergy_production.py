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
class BioenergyProduction(MetroidPrime2Region):
    name = "Bioenergy Production"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Storage C",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Standable Terrain"),
                ]),
                condition_and([
                    state.has("Scan Visor", player),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_boost_ball(state, player),
                                    can_use_spider_ball(state, player),
                                ]),
                                condition_and([
                                    can_lay_bomb(state, player),
                                    can_use_screw_attack(state, player),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                    has_trick_enabled(state, player, "Movement"),
                                ]),
                                condition_and([
                                    state.has("Space Jump Boots", player),
                                    has_trick_enabled(state, player, "Roll Jump"),
                                ]),
                            ]),
                        ]),
                        can_use_screw_attack(state, player),
                        condition_and([
                            state.has("Space Jump Boots", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station A",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area B",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Standable Terrain"),
                ]),
                condition_and([
                    state.has("Scan Visor", player),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_boost_ball(state, player),
                                    can_use_spider_ball(state, player),
                                    condition_or([
                                        # https://youtu.be/cEiwn9ZE2W4
                                        condition_and([
                                            can_use_screw_attack(state, player),
                                            has_trick_enabled(state, player, "Movement"),
                                        ]),
                                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                                    ]),
                                ]),
                                condition_and([
                                    can_lay_bomb(state, player),
                                    has_trick_enabled(state, player, "Movement"),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                ]),
                            ]),
                        ]),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Energy Tank)",
            can_access=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Standable Terrain"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    state.has("Scan Visor", player),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_boost_ball(state, player),
                                    can_use_spider_ball(state, player),
                                    condition_or([
                                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                                        # https://youtu.be/cEiwn9ZE2W4
                                        condition_and([
                                            can_use_screw_attack(state, player),
                                            has_trick_enabled(state, player, "Movement"),
                                        ]),
                                        has_trick_enabled(state, player, "Extended Dash"),
                                    ]),
                                ]),
                                condition_and([
                                    can_lay_bomb(state, player),
                                    can_use_screw_attack(state, player, z_axis=True),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                    has_trick_enabled(state, player, "Movement"),
                                ]),
                            ]),
                        ]),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
            ]),
        )
