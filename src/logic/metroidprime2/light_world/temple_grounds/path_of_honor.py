from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class PathOfHonor_Bottom(MetroidPrime2Region):
    name = "Path Of Honor"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Honored Dead",
            door=DoorCover.Seeker,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Path of Honor Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class PathOfHonor_Top(MetroidPrime2Region):
    name = "Path Of Honor"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Honored Dead (Path of Honor Side)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Top - Path of Honor Side)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
    ]
