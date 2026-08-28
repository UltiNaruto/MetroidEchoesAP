from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_light_portal,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HiveCache2(MetroidPrime2Region):
    name = "Hive Cache 2" #Artist formerly known as Hive Cache 3
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (South Portal Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Dynamo Storage", #Name can be subject to change
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player)
        )
    ]
