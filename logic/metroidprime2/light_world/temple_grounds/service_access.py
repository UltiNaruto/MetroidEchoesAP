from ... import can_lay_bomb, can_use_boost_ball
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and


class ServiceAccess_Bottom_MeetingGroundsSide(MetroidPrime2Region):
    name = "Service Access"
    desc = "Bottom - Meeting Grounds Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Meeting Grounds (Bottom)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Tunnel)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
    ]


class ServiceAccess_Bottom_PathOfHonorSide(MetroidPrime2Region):
    name = "Service Access"
    desc = "Bottom - Path of Honor Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Landing Site (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Honor (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Tunnel)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
    ]


class ServiceAccess_Bottom_Tunnel(MetroidPrime2Region):
    name = "Service Access"
    desc = "Bottom - Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Meeting Grounds Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Path of Honor Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
    ]


class ServiceAccess_Top_MeetingGroundsSide(MetroidPrime2Region):
    name = "Service Access"
    desc = "Top - Meeting Grounds Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Meeting Grounds (Top)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Tunnel)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Top - Path of Honor Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_use_boost_ball(state, player),
                can_lay_bomb(state, player),
            ]),
        ),
    ]


class ServiceAccess_Top_PathOfHonorSide(MetroidPrime2Region):
    name = "Service Access"
    desc = "Top - Path of Honor Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Honor (Top)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Tunnel)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Top - Meeting Grounds Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_boost_ball(state, player),
        ),
    ]
