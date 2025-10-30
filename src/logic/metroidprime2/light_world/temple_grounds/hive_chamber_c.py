from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HiveChamberC(MetroidPrime2Region):
    name = "Hive Chamber C"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber B",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Save Station",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Transport Area (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
