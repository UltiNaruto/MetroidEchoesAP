from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransportToTorvusBog(MetroidPrime2Region):
    name = "Transport to Torvus Bog"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Torvus Transport Access",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="E|Torvus Bog - Transport to Temple Grounds",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]
