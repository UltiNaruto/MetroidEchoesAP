from ... import has_dark_suit, has_light_suit
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or


class ReliquaryAccess_PhazonGroundsSide(MetroidPrime2Region):
    name = "Reliquary Access"
    desc = "Phazon Grounds Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Grounds",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 2,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Access (Reliquary Grounds Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: has_light_suit(state, player), # TODO: add trick for no light suit
        ),
    ]


class ReliquaryAccess_ReliquaryGroundsSide(MetroidPrime2Region):
    name = "Reliquary Access"
    desc = "Reliquary Grounds Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Access (Phazon Grounds Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: has_light_suit(state, player), # TODO: add trick for no light suit
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Grounds (Bottom)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
    ]
