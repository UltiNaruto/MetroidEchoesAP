from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class BiostorageAccess(MetroidPrime2Region):
    name = "Biostorage Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Behind Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Station (Biostorage Access Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        )
    ]