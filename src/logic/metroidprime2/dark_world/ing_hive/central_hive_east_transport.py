from BaseClasses import MultiWorld

from ... import (
    can_activate_safe_zone,
    has_dark_suit,
    has_light_suit,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or

class CentralHiveEastTransport_Lower(MetroidPrime2Region):
    name = "Central Hive East Transport"
    desc = "Lower"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive East Transport (Upper)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (North Safe Zone)",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_or([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class CentralHiveEastTransport_Upper(MetroidPrime2Region):
    name = "Central Hive East Transport"
    desc = "Upper"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive East Transport (Lower)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (North Track Door)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
    ]
