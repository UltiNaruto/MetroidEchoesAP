from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransportToTorvusBog(MetroidPrime2Region):
    name = "Transport to Torvus Bog"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Transport to Torvus Bog Ledge)",
            door=DoorCover.Seeker,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="E|Torvus Bog - Transport to Agon Wastes",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]
