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
class HydrodynamoStation(MetroidPrime2Region):
    name = "Hydrodynamo Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Save Station B",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
                ]),
                state.has("Space Jump Boots", player),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
                ]),
                state.has("Space Jump Boots", player),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    condition_or([
                        condition_and([
                            not (False),
                            has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        ]),
                        has_trick_enabled(state, player, "Movement"),
                    ]),
                ]),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Access",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    state.has("Gravity Boost", player),
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
                condition_and([
                state.has("Torvus Bog - Hydrodynamo Station | Event - Hydrodynamo Station Lock (below Seeker Door)", player),
                state.has("Torvus Bog - Hydrodynamo Station | Event - Hydrodynamo Station Lock (by Dark Door)", player),
                state.has("Torvus Bog - Hydrodynamo Station | Event - Hydrodynamo Station Lock (by Light Door)", player),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Hydrodynamo Station Lock (below Seeker Door)",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Hydrodynamo Station | Event - Hydrodynamo Station Lock (below Seeker Door)",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
                state.has("Scan Visor", player),
            ]),
        )

        self.add_location(
            name="Event - Hydrodynamo Station Lock (by Dark Door)",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Hydrodynamo Station | Event - Hydrodynamo Station Lock (by Dark Door)",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
                state.has("Scan Visor", player),
            ]),
        )

        self.add_location(
            name="Event - Hydrodynamo Station Lock (by Light Door)",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Hydrodynamo Station | Event - Hydrodynamo Station Lock (by Light Door)",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                    has_trick_enabled(state, player, "Underwater Dash"),
                ]),
            ]),
                state.has("Scan Visor", player),
            ]),
        )
