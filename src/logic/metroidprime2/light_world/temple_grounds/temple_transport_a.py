from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TempleTransportA(MetroidPrime2Region):
    name = "Temple Transport A"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="E|Great Temple - Temple Transport A",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Great Temple Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
