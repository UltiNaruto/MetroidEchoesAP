from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class StorageCavernA(MetroidPrime2Region):
    name = "Storage Cavern A"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Communication Area (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
