"""Morph Ball puzzle room connecting Training Chamber and Gathering Hall.
Air jets in this room can lift the Morph Ball if the player does not have Gravity Boost."""

from ... import can_lay_bomb
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransitTunnelWest_SouthSide(MetroidPrime2Region):
    name="Transit Tunnel West"
    desc="South Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West (North Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]


class TransitTunnelWest_NorthSide(MetroidPrime2Region):
    name="Transit Tunnel West"
    desc="North Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West (South Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (West Caged Area)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
