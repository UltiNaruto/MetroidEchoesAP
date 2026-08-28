from BaseClasses import MultiWorld

from ... import (
    has_dark_suit,
    has_light_suit,
    can_activate_safe_zone,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class EntranceDefenseHall(MetroidPrime2Region):
    name = "Entrance Defense Hall"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Entrance",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor Access (Lower)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]
