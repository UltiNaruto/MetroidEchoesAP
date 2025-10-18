from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class PlazaAccess(MetroidPrime2Region):
    name = "Plaza Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport to Temple Grounds",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Plaza Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]