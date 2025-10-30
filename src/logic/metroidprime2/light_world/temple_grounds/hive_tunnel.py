from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HiveTunnel(MetroidPrime2Region):
    name = "Hive Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Command Chamber",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber A",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
