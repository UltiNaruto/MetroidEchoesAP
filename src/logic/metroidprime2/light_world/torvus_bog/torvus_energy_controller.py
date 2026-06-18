from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusEnergyController(MetroidPrime2Region):
    name="Torvus Energy Controller"
    exits_ = [
        MetroidPrime2Exit(
            destination="Controller Access",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Torvus Energy Returned",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Torvus Energy Controller | Energy Returned",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Dark Torvus Bog - Dark Torvus Energy Controller | Energy Recovered", player)
        )
        self.add_location(
            name="Pickup (Emerald Translator)",
            can_access=lambda state, player: True
        )
