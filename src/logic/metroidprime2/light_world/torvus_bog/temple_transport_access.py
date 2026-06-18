from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TempleTransportAccess(MetroidPrime2Region):
    name = "Temple Transport Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transport to Temple Grounds",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
