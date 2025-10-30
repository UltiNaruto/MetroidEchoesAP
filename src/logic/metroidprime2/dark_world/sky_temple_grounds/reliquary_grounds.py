from ... import has_light_suit
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and


class ReliquaryGrounds_Bottom(MetroidPrime2Region):
    name = "Reliquary Grounds"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Access (Reliquary Grounds Side)",
            door=DoorCover.Light,
            rule=lambda state, player: has_light_suit(state, player), # TODO: add trick for no light suit
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Grounds (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                has_light_suit(state, player),
                state.has("Space Jump Boots", player),
            ]),
        ),
    ]


class ReliquaryGrounds_Top(MetroidPrime2Region):
    name = "Reliquary Grounds"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Reliquary",
            door=DoorCover.Any,
            rule=lambda state, player: has_light_suit(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Grounds (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]
