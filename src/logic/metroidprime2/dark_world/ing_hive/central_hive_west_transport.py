from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_safe_zone,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class CentralHiveWestTransport_Lower(MetroidPrime2Region):
    name = "Central Hive West Transport"
    desc = "Upper"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive West Transport (Upper)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_use_screw_attack(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Staging Area (Door)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
    ]

class CentralHiveWestTransport_Upper(MetroidPrime2Region):
    name = "Central Hive West Transport"
    desc = "Lower"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Box)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive West Transport (Lower)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
