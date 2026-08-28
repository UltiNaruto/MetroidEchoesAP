from BaseClasses import MultiWorld

from ... import (
    has_dark_suit,
    has_light_suit,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or

class HiveAmmoStation(MetroidPrime2Region):
    name = "Hive Ammo Station"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]
