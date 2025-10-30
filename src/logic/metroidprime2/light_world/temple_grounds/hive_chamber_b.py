from BaseClasses import MultiWorld

from ... import can_lay_bomb
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HiveChamberB(MetroidPrime2Region):
    name = "Hive Chamber B"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber B (Behind Bomb Cover)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber C",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Storage",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class HiveChamberB_BehindBombCover(MetroidPrime2Region):
    name = "Hive Chamber B"
    desc = "Behind Bomb Cover"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber B",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]
