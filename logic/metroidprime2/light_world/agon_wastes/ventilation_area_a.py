from BaseClasses import Multiworld
from ... import (
    can_lay_bomb
)
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and

class VentilationAreaA_SandcanyonSide(MetroidPrime2Region):
    name = "Ventiliation Area A"
    desc = "Sandcanyon Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Ventilation Area A Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class VentilationAreaA_ReactorCoreSide(MetroidPrime2Region):
    name = "Ventiliation Area A"
    desc = "Main Reactor Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Ventilation Area A Side)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
    ]

class VentilationAreaA_TransportToSanctuaryFortressSide(MetroidPrime2Region):
    name = "Ventiliation Area A"
    desc = "Transport to Sanctuary Fortress Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport to Sanctuary Fortress",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
    ]


class VentilationAreaA_Center(MetroidPrime2Region):
    name = "Ventiliation Area A"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Sandcanyon Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Main Reactor Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Transport to Sanctuary Fortress Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        )
    ]

class VentilationAreaA_Item(MetroidPrime2Region):
    name = "Ventilation Area A"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: Multiworld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]