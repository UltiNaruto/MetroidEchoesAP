"""Connects Torvus Grove and the caged area of Forgotten Bridge."""

from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class GroveAccess(MetroidPrime2Region):
    name="Grove Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Upper Door Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        )
    ]
