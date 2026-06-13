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
class SanctuaryTemple(MetroidPrime2Region):
    name = "Sanctuary Temple"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Controller Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_or([
                # https://www.youtube.com/watch?v=FsMEbSXfSx0
                condition_and([
                    state.has("Scan Visor", player),
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
                can_use_screw_attack(state, player),
                # https://www.youtube.com/watch?v=l5vF1J2hO-Q
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
                condition_or([
                condition_or([
                    can_use_grapple_beam(state, player),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    state.has("Scan Visor", player),
                    condition_or([
                        # https://www.youtube.com/watch?v=0MYrEDFJ9iY
                        condition_and([
                            has_trick_enabled(state, player, "Standable Terrain"),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                        # https://www.youtube.com/watch?v=kvfZxoNy004
                        has_trick_enabled(state, player, "Extended Dash"),
                    ]),
                ]),
                # https://www.youtube.com/watch?v=l5vF1J2hO-Q
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Workers Path",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_or([
                # https://www.youtube.com/watch?v=FsMEbSXfSx0
                condition_and([
                    state.has("Scan Visor", player),
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
                can_use_screw_attack(state, player),
                # https://www.youtube.com/watch?v=l5vF1J2hO-Q
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
                condition_or([
                # https://www.youtube.com/watch?v=0MYrEDFJ9iY
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    state.has("Scan Visor", player),
                ]),
                # Works the same as: https://www.youtube.com/watch?v=l5vF1J2hO-Q
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player),
                condition_and([
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Extended Dash"),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Temple Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Sentinel's Path",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                condition_or([
                # https://www.youtube.com/watch?v=FsMEbSXfSx0
                condition_and([
                    state.has("Scan Visor", player),
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
                can_use_screw_attack(state, player),
                # https://www.youtube.com/watch?v=l5vF1J2hO-Q
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
                condition_or([
                can_use_screw_attack(state, player),
                # https://www.youtube.com/watch?v=O3RgTYbAnZo
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    state.has("Scan Visor", player),
                ]),
                # Works the same as: https://www.youtube.com/watch?v=l5vF1J2hO-Q
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Event - Temple Access Reloaded (Top)",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Sanctuary Temple | Event - Temple Access Reloaded (Top)",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                # https://www.youtube.com/watch?v=FsMEbSXfSx0
                condition_and([
                    state.has("Scan Visor", player),
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
                can_use_screw_attack(state, player),
                # https://www.youtube.com/watch?v=l5vF1J2hO-Q
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
                state.has("Sanctuary Fortress - Temple Access | Event - Quad", player),
            ]),
        )

        self.add_location(
            name="Event - Temple Access Reloaded (Bottom)",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Sanctuary Temple | Event - Temple Access Reloaded (Bottom)",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Sanctuary Fortress - Temple Access | Event - Quad", player),
        )
