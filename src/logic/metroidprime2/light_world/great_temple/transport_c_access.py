from BaseClasses import ItemClassification, MultiWorld

from ... import can_activate_light_beam_block
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TransportCAccess_ElevatorSide(MetroidPrime2Region):
    name = "Transport C Access"
    desc = "Elevator Side"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Any,
            destination="Great Temple - Temple Transport C",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport C Access (Temple Sanctuary Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Transport C Access | Light Beam Block Opened", player),
        ),
    ]


class TransportCAccess_TempleSanctuarySide(MetroidPrime2Region):
    name = "Transport C Access"
    desc = "Temple Sanctuary Side"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Any,
            destination="Great Temple - Temple Sanctuary (Transport C Side)",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport C Access (Elevator Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Transport C Access | Light Beam Block Opened", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Light Beam Block Opened",
                locked_item=MetroidPrime2Item(
                    name="Great Temple - Transport C Access | Light Beam Block Opened",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: can_activate_light_beam_block(state, player),
                parent=self,
            ),
        ]