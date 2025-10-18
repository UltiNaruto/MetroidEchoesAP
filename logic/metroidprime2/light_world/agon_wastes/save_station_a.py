from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class SaveStationA_MiningPlazaSide(MetroidPrime2Region):
    name = "Save Station A"
    desc = "Mining Plaza Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station A (Transport Center Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Save Station A Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        )
    ]

class SaveStationA_TransportCenterSide(MetroidPrime2Region):
    name = "Save Station A"
    desc = "Transport Center Side",
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station A (Mining Plaza Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Behind Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]