from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TempleTransportC(MetroidPrime2Region):
    name = "Temple Transport C"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="E|Temple Grounds - Temple Transport C",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport C Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
