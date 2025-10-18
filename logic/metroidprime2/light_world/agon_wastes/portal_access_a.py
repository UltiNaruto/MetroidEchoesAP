from BaseClasses import MultiWorld
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class PortalAccessA_MiningStationASide(MetroidPrime2Region):
    name = "Portal Access A",
    desc = "Mining Station A Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A (Portal Teminal Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Portal Access A Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class PortalAccessA_PortalTerminalSide(MetroidPrime2Region):
    name = "Portal Access A",
    desc = "Poral Terminal Side",
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A (Mining Station A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Terminal (Portal Access A Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        )
    ]

class PortalAccessA_Item(MetroidPrime2Region):
    name = "Portal Access A"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A (Portal Terminal Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]