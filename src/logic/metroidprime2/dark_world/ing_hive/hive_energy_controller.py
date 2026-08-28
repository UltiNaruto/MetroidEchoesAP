from BaseClasses import ItemClassification, MultiWorld

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class HiveEnergyController(MetroidPrime2Region):
    name = "Hive Energy Controller"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Controller Access (Controller Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Ing Hive Energy",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Energy Controller | Ing Hive Energy",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True,
        )
