from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class AgonMapStation(MetroidPrime2Region):
    name = "Agon Map Station",
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Behind Translator Gate)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        )
    ]