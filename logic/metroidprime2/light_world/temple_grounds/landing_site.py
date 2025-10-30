from BaseClasses import MultiWorld, ItemClassification

from ... import can_activate_light_beam_block, has_trick_enabled
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class LandingSite_Bottom(MetroidPrime2Region):
    name = "Landing Site"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Landing Site (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Landing Site | Light Beam Block Skip"),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    state.has("Temple Grounds - Landing Site | Light Beam Block Moved", player),
                    state.has("Space Jump Boots", player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Access Tunnel (Landing Site Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Light Beam Block",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - Landing Site | Light Beam Block Moved",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: can_activate_light_beam_block(state, player),
                parent=self,
            ),
        ]


class LandingSite_Top(MetroidPrime2Region):
    name = "Landing Site"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Landing Site (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Service Access (Bottom - Path of Honor Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
