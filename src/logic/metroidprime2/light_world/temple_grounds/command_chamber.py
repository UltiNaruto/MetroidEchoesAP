from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class CommandChamber(MetroidPrime2Region):
    name = "Command Chamber"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Tunnel",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Storage",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
