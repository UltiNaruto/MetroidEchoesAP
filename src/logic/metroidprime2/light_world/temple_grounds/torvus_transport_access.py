from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusTransportAccess(MetroidPrime2Region):
    name = "Torvus Transport Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Torvus Transport Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Transport to Torvus Bog",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
    ]
