from BaseClasses import ItemClassification, MultiWorld

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransportToAgonWastes(MetroidPrime2Region):
    name = "Transport to Agon Wastes"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Agon Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Transport to Agon Wastes (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Transport to Agon Wastes | Webbing Destroyed", player),
        ),
        MetroidPrime2Exit(
            destination="E|Agon Wastes - Transport to Temple Grounds",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Webbing Destroyed",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - Transport to Agon Wastes | Webbing Destroyed",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class TransportToAgonWastes_Item(MetroidPrime2Region):
    name = "Transport to Agon Wastes"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Transport to Agon Wastes",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Transport to Agon Wastes | Webbing Destroyed", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]
