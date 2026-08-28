from BaseClasses import MultiWorld

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class HiveSaveStation2(MetroidPrime2Region):
    name = "Hive Save Station 2"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (North Lower)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
