from BaseClasses import MultiWorld
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class StorageA(MetroidPrime2Region):
    name = "Storage A"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Behind PB Wall)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]