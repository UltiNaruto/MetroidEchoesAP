from ... import can_activate_dark_portal, can_lay_bomb, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class HallOfEyes_Bottom(MetroidPrime2Region):
    name = "Hall of Eyes"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Eyes (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Hall of Eyes | DBJ to Top"),
                    can_lay_bomb(state, player),
                ]),
                state.has("Space Jump Boots", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Meeting Grounds (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class HallOfEyes_Top(MetroidPrime2Region):
    name = "Hall of Eyes"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="P|Sky Temple Grounds - Base Access (Top)",
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Eyes (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Hall of Eyes Side)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True,
        ),
    ]
