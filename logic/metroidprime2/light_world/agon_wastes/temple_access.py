from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class TempleAccess(MetroidPrime2Region):
    name = "Temple Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Temple Access Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Temple Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]