from ... import has_dark_suit, has_light_suit
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class LakeAccess(MetroidPrime2Region):
    name = "Lake Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Accursed Lake",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                # assuming we get the item, starting from Plain of Dark Worship door
                state.count("Energy Tank", player) >= 5,
                condition_and([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Plain of Dark Worship",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                # assuming we come from Accursed Lake door
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]
