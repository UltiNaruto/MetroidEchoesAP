"""Room connecting Hydrodynamo Station and Gathering Hall. Has white doors on both sides."""

from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class GatheringAccess(MetroidPrime2Region):
    name="Gathering Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Upper Door Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (West Door Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
