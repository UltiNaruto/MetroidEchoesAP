from BaseClasses import MultiWorld

from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class StorageCavernB(MetroidPrime2Region):
    name = "Storage Cavern B"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Storage Cavern B Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Energy Tank)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]
