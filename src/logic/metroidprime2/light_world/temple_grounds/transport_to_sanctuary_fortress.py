from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransportToSanctuaryFortress(MetroidPrime2Region):
    name = "Transport to Sanctuary Fortress"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Fortress Transport Access (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="E|Sanctuary Fortress - Transport to Temple Grounds",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]
