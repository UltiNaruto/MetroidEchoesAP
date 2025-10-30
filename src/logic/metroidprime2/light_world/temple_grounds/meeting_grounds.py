from ... import can_use_boost_ball, can_use_screw_attack, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class MeetingGrounds_Bottom(MetroidPrime2Region):
    name = "Meeting Grounds"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Eyes (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Meeting Grounds (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_use_boost_ball(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Meeting Grounds | To top with Screw Attack"),
                    can_use_screw_attack(state, player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Meeting Grounds (Great Temple Side)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Meeting Grounds Side)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True,
        ),
    ]


class MeetingGrounds_GreatTempleSide(MetroidPrime2Region):
    name = "Meeting Grounds"
    desc = "Great Temple Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Meeting Grounds (Bottom)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Transport C",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class MeetingGrounds_Top(MetroidPrime2Region):
    name = "Meeting Grounds"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Meeting Grounds (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Top - Meeting Grounds Side)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
    ]
