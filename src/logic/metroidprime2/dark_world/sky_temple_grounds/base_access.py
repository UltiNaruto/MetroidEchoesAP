from ... import can_activate_light_portal, can_lay_bomb, has_dark_suit, has_light_suit, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class BaseAccess_Bottom(MetroidPrime2Region):
    name = "Base Access"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Base Access (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Sky Temple Grounds - Base Access | DBJ to Top"),
                    can_lay_bomb(state, player),
                ]),
                state.has("Space Jump Boots", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds (Base Access Side)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 2,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]


class BaseAccess_Top(MetroidPrime2Region):
    name = "Base Access"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="P|Temple Grounds - Hall of Eyes (Top)",
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Base Access (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Abandoned Base",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
