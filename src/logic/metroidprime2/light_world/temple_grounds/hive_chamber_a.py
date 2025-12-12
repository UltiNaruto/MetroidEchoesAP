from BaseClasses import MultiWorld

from ... import has_oob_kit, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and


class HiveChamberA(MetroidPrime2Region):
    name = "Hive Chamber A"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Access Tunnel (Landing Site Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Temple Grounds - Hive Chamber A | Out of Bounds"),
                has_oob_kit(state, player),
            ])
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Access Tunnel (Hive Transport Area Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Temple Grounds - Hive Chamber A | Out of Bounds"),
                has_oob_kit(state, player),
            ])
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber A (Dark Missile Trooper)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Agon Temple | Bomb Guardian Dead", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Tunnel",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class HiveChamberA_DarkMissileTrooper(MetroidPrime2Region):
    name = "Hive Chamber A"
    desc = "Dark Missile Trooper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber A",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True,
        )
