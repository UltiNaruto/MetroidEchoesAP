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
class CommandCenter(MetroidPrime2Region):
    name = "Command Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access (Top)",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Closed", player),
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Opened", player),
            ]),
                condition_and([
                state.has("Scan Visor", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Movement"),
                    ]),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station B",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Closed", player),
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Opened", player),
            ]),
                condition_and([
                state.has("Scan Visor", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Movement"),
                    ]),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Closed", player),
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Opened", player),
            ]),
                condition_or([
                not (state.has("Agon Wastes - Command Center | Event - Command Center Gate Closed", player)),
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Opened", player),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_and([
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Closed", player),
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Opened", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Doomed Entry",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Closed", player),
                state.has("Agon Wastes - Command Center | Event - Command Center Gate Opened", player),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station B",
            door=DoorCover.Missile,
            rule=lambda state, player: state.has("Agon Wastes - Command Center | Event - Command Center Gate Opened", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: state.has("Morph Ball", player),
        )

        self.add_location(
            name="Event - Command Center Gate Closed",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Command Center | Event - Command Center Gate Closed",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Morph Ball", player),
        )

        self.add_location(
            name="Event - Command Center Gate Opened",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Command Center | Event - Command Center Gate Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player),
        )
