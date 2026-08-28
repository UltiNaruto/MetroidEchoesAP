from BaseClasses import MultiWorld

from ... import (
    has_missile_count,
    has_dark_suit,
    has_light_suit,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class HiveSaveStation(MetroidPrime2Region):
    name = "Ing Hive - Hive Save Station 1"
    exits = [
        MetroidPrime2Exit(
            destination="Hive Reactor",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
