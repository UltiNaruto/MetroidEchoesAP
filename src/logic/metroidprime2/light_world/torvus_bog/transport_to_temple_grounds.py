from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransportToTempleGrounds(MetroidPrime2Region):
    name = "Transport to Temple Grounds"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="E|Temple Grounds - Transport to Torvus Bog",
            rule=lambda state, player: state.has("Scan Visor", player)
        )
    ]
