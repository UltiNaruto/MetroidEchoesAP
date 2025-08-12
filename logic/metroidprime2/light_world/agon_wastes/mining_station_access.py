from BaseClasses import MultiWorld
from ... import (
    can_lay_bomb_or_pb
)
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class MiningStationAccess_MiningPlazaSide(MetroidPrime2Region):
    name = "Mining Station Access"
    desc = "Mining Plaza Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Mining Station Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player:  True,
        )
    ]

class MiningStationAccess_MiningStationASide(MetroidPrime2Region):
    name = "Mining Station Access"
    desc = "Mining Plaza Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Mining Station Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class MiningStationAccess_Center(MetroidPrime2Region):
    name = "Mining Station Access"
    desc = "Mining Plaza Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Mining Plaza Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Mining Station A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb_or_pb(state, player),
        )
    ]

class MiningStationAccess_Item(MetroidPrime2Region):
    name = "Mining Station Access"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        )
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