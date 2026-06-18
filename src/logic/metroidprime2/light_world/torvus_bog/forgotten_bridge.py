"""
A room characterized by a large spinning bridge in the center of the room. It contains:
- One phased Bomb Slot
- One Spinner
- One caged area
- One Dark Portal
- One Super Missile Cover door
- One Missile Cover door
- One white door
- Grenchler or Dark Pirate Commando enemies
"""

from BaseClasses import MultiWorld, ItemClassification
from ... import (
    can_activate_dark_portal,
    can_lay_bomb,
    can_use_boost_ball,
    can_use_screw_attack,
    forgotten_bridge_bridge_to_portal,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class ForgottenBridge_Bridge(MetroidPrime2Region):
    """The bridge. It rotates once after the bomb slot has been used in this room's dark twin."""
    name="Forgotten Bridge"
    desc="Bridge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Pickup Ledge)",
            rule=lambda state, player: condition_or([
                can_use_screw_attack(state, player),
                state.has("Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated", player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Dark Portal Ledge)",
            rule=lambda state, player: forgotten_bridge_bridge_to_portal(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated", player),
                state.has("Space Jump Boots", player)
            ])
        ),
    ]


class ForgottenBridge_Cage(MetroidPrime2Region):
    """A path between two side rooms that is not open to the rest of the room until a Spinner is used in this subregion.
    Also includes the platforms that lower after the Spinner has been operated."""
    name="Forgotten Bridge"
    desc="Cage"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: condition_or([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated", player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | BSJ into Cage"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated", player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: state.has("Torvus Bog - Forgotten Bridge | Spinner Activated", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Grove Access",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Entrance)",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Spinner Activated",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Forgotten Bridge | Spinner Activated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_use_boost_ball(state, player)
        )


class ForgottenBridge_Cliffs(MetroidPrime2Region):
    """Includes all the ledges leading up from the water to the phased bomb slot and bridge."""
    name="Forgotten Bridge"
    desc="Cliffs"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule = lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | BSJ into Cage"),
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player)
            ])
        )
    ]


class ForgottenBridge_DarkPortalLedge(MetroidPrime2Region):
    """Contains a portal to Dark Aether."""
    name="Forgotten Bridge"
    desc="Dark Portal Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Dark Forgotten Bridge (Light Portal Ledge)",
            rule=lambda state, player: can_activate_dark_portal(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated", player),
                state.has("Space Jump Boots", player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        )
    ]


class ForgottenBridge_PickupLedge(MetroidPrime2Region):
    """Contains a pickup and a Super Missile Cover door. Connects to the bridge once the bridge has been rotated."""
    name="Forgotten Bridge"
    desc="Pickup Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Forgotten Bridge Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True,
        )


class ForgottenBridge_Shallows(MetroidPrime2Region):
    """The water."""
    name="Forgotten Bridge"
    desc="Shallows"
    exits=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | Bomb Jump Between Platforms")
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | Reverse Air Underwater"),
                    state.has("Gravity Boost", player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Ruined Alcove",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
