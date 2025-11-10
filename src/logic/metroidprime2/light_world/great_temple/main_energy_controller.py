from BaseClasses import ItemClassification, MultiWorld

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class MainEnergyController(MetroidPrime2Region):
    name = "Main Energy Controller"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item"),
        ),
        MetroidPrime2Exit(
            door=DoorCover.Any,
            destination="Great Temple - Controller Transport (Top)",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="Great Temple - Main Energy Controller (Item)",
            rule=lambda state, player: state.has("Sanctuary Fortress - Sanctuary Energy Controller | Energy Returned"),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item"),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Sanctuary Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item"),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Violet Translator)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class MainEnergyController_LightSuitItem(MetroidPrime2Region):
    name = "Main Energy Controller"
    desc = "Light Suit Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Great Temple - Main Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item"),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Can Pick Up Light Suit Item",
                locked_item=MetroidPrime2Item(
                    name="Great Temple - Main Energy Controller | Can Pick Up Light Suit Item",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
            MetroidPrime2Location(
                name="Pickup (Light Suit)",
                can_access=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item"),
                parent=self,
            ),
        ]