"""Contains the Gravity Boost in vanilla. Picking up the item would be the trigger for the Alpha Blogg boss,
but it has been moved in the Archipelago randomizer."""

from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HydrochamberStorage(MetroidPrime2Region):
    name="Hydrochamber Storage"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Lower Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Gravity Boost)",
            can_access=lambda state, player: True
        )
