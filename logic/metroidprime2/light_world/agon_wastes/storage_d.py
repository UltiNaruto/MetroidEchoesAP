from BaseClasses import MultiWorld
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class StorageD(MetroidPrime2Region):
    name = "Storage D"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Storage D Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Dark Beam)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]