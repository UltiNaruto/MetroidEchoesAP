from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TempleTransportB(MetroidPrime2Region):
    name = "Temple Transport B"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="E|Temple Grounds - Temple Transport B",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport B Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
