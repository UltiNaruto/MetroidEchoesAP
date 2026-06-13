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
class SandProcessing(MetroidPrime2Region):
    name = "Sand Processing"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor",
            door=DoorCover.Any,
            rule=lambda state, player: has_missile_count(state, player, 1),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station C",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: state.has("Agon Wastes - Sand Processing | Event - Sand Processing Sand Drained", player),
        )

        self.add_location(
            name="Event - Sand Processing Sand Drained",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Sand Processing | Event - Sand Processing Sand Drained",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_use_boost_ball(state, player),
                        # https://youtu.be/cEghPZPy_AM?t=35
                        condition_or([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=CzhDj8MmERg
                    condition_and([
                        state.has("Space Jump Boots", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                    # https://www.youtube.com/watch?v=1Meg1C7X-1Q
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                    ]),
                ]),
            ]),
                condition_and([
                state.has("Scan Visor", player),
                condition_or([
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                    ]),
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                        condition_or([
                            # With Space Jump: https://www.youtube.com/watch?v=9i3Tc8UlFts
                            state.has("Space Jump Boots", player),
                            # No Space Jump: https://youtu.be/cEghPZPy_AM?t=81
                            has_trick_enabled(state, player, "Slope Jump"),
                        ]),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Main Reactor Reloaded via Sand Processing",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Sand Processing | Event - Main Reactor Reloaded via Sand Processing",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Agon Wastes - Main Reactor | Event - Dark Samus 1", player),
        )
