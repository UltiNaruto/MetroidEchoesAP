from BaseClasses import MultiWorld, ItemClassification
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

class AgonEnergyController(MetroidPrime2Region):
    name = "Agon Energy Controller"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Controller Access (Agon Energy Contoller Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Main Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Sanctuary Fortress - Sanctuary Energy Controller | Light Returned"),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Light Returned",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Agon Energy Controller | Light Returned",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player
                ),
                can_access=lambda state, player: state.has("Dark Agon Wastes - Dark Agon Temple | Energy Recovered", player),
                parent=self,
            ),
            MetroidPrime2Location(
                name="Pickup (Amber Translator)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]