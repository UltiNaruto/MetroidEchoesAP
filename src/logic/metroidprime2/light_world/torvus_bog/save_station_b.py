from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class SaveStationB(MetroidPrime2Region):
    name="Save Station B"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top Door Ledge)",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        )
    ]
