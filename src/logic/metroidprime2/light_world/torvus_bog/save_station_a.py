from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class SaveStationA(MetroidPrime2Region):
    name="Save Station A"
    exits_ = ([
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Save Room Ledge)",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        )
    ])
