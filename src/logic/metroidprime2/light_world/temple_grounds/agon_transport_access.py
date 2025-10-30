from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class AgonTransportAccess(MetroidPrime2Region):
    name = "Agon Transport Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Behind Translator Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Transport to Agon Wastes",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
