from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TrainingAccess(MetroidPrime2Region):
    name="Training Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (South Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
