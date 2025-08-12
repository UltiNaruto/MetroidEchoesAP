from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransportToSanctuaryFortress(MetroidPrime2Region):
    name = "Transport to Sanctuary Fortress"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Transport to Sanctuary Fortress Side)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="E|Sanctuary Fortress - Transport to Agon Wastes",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]
