from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HiveSaveStation(MetroidPrime2Region):
    name = "Hive Save Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber C",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
