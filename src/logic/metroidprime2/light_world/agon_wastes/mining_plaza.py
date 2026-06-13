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
class MiningPlaza(MetroidPrime2Region):
    name = "Mining Plaza"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transit Station",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
                ]),
                state.has("Space Jump Boots", player),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                has_missile_count(state, player, 1),
                condition_and([
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Duelling Range",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_or([
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
                    ]),
                    state.has("Space Jump Boots", player),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Movement"),
                    ]),
                    has_missile_count(state, player, 1),
                    condition_and([
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        has_trick_enabled(state, player, "Slope Jump"),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Map Station",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    can_lay_pb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Knowledge"),
                        # Use Boost Ball or Screw Attack to destroy the rock
                        condition_or([
                            can_use_boost_ball(state, player),
                            can_use_screw_attack(state, player),
                        ]),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station A",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                # Double Bomb Jump
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
                ]),
                state.has("Space Jump Boots", player),
                # https://www.youtube.com/watch?v=drldqXBvPLs
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                has_missile_count(state, player, 1),
                # https://www.youtube.com/watch?v=0BuPg72jQgI
                condition_and([
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Plaza Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Energy Tank)",
            can_access=lambda state, player: condition_and([
                condition_or([
                # Double Bomb Jump
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
                ]),
                state.has("Space Jump Boots", player),
                # https://www.youtube.com/watch?v=drldqXBvPLs
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                has_missile_count(state, player, 1),
                # https://www.youtube.com/watch?v=0BuPg72jQgI
                condition_and([
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
                condition_and([
                state.has("Echo Visor", player),
                state.has("Agon Wastes - Agon Energy Controller | Event - Agon Energy Returned", player),
                condition_or([
                    can_use_screw_attack(state, player),
                    # https://www.youtube.com/watch?v=A9JXJVOykZU
                    condition_and([
                        state.has("Scan Visor", player),
                        has_trick_enabled(state, player, "Extended Dash"),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
            ]),
            ]),
        )
