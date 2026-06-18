from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusMapStation(MetroidPrime2Region):
    name="Torvus Map Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Behind Translator Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
