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
class MainReactor(MetroidPrime2Region):
    name = "Main Reactor"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Dark Oasis",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_or([
                can_use_dark_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Knowledge"),
                    can_use_screw_attack(state, player, z_axis=True),
                ]),
            ]),
                # https://www.youtube.com/watch?v=KIP9PWtVt7o
            condition_and([
                can_lay_bomb(state, player),
                can_use_screw_attack(state, player),
                has_trick_enabled(state, player, "Bomb Space Jump"),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Storage D",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_or([
                can_use_dark_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Knowledge"),
                    can_use_screw_attack(state, player, z_axis=True),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station B",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                state.has("Agon Wastes - Main Reactor | Event - Dark Samus 1", player),
                state.has("Agon Wastes - Sand Processing | Event - Main Reactor Reloaded via Sand Processing", player),
                condition_or([
                    # https://www.youtube.com/watch?v=Ibb9XlRcAQE
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            # https://www.youtube.com/watch?v=X8Fe5va-ehc
                            condition_and([
                                has_trick_enabled(state, player, "Slope Jump"),
                                has_trick_enabled(state, player, "Roll Jump"),
                            ]),
                            # https://www.youtube.com/watch?v=Yr-cCSIIWfM
                            condition_and([
                                has_trick_enabled(state, player, "Combat/Scan Dash"),
                                state.has("Scan Visor", player),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    condition_or([
                        can_lay_bomb(state, player),
                        can_lay_pb(state, player),
                    ]),
                    condition_and([
                            has_trick_enabled(state, player, "Knowledge"),
                            condition_or([
                                can_use_power_beam(state, player),
                                can_use_boost_ball(state, player),
                                can_use_screw_attack(state, player),
                            ]),
                        ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Dark Samus 1",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Main Reactor | Event - Dark Samus 1",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_or([
                can_use_dark_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Knowledge"),
                    can_use_screw_attack(state, player, z_axis=True),
                ]),
            ]),
                # https://www.youtube.com/watch?v=KIP9PWtVt7o
            condition_and([
                can_lay_bomb(state, player),
                can_use_screw_attack(state, player),
                has_trick_enabled(state, player, "Bomb Space Jump"),
            ]),
            ]),
                # https://www.youtube.com/watch?v=ZcW-Ws9nA6Q
            condition_and([
                state.has("Space Jump Boots", player),
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
                has_trick_enabled(state, player, "Bomb Space Jump"),
                has_trick_enabled(state, player, "Standable Terrain"),
                has_trick_enabled(state, player, "Single Room Out of Bounds"),
            ]),
            ]),
        )
