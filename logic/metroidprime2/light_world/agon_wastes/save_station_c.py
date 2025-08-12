from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class SaveStationC(MetroidPrime2Region):
    name = "Save Station C"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area B (Save Station C Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]