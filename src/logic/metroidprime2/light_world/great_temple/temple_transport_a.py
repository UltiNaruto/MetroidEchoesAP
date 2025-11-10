from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TempleTransportA(MetroidPrime2Region):
    name = "Temple Transport A"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="E|Temple Grounds - Temple Transport A",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport A Access (Elevator Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
