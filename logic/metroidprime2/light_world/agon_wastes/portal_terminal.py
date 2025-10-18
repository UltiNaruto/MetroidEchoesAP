from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_darkburst,
    can_use_sonic_boom,
    can_use_screw_attack,
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class PortalTerminal_PortalAccessASide(MetroidPrime2Region):
    name = "Portal Terminal"
    desc = "Portal Access A Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Terminal (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A (Portal Terminal Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class PortalTerminal_Center(MetroidPrime2Region):
    name = "Portal Terminal"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Portal Site (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Portal Terminal | Portal Activated", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Terminal (Portal Access A)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Terminal (Behind Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Dark Agon Wastes - Portal Site | Gate Opened", player),
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Portal Activated",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Portal Terminal | Portal Activated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Portal Terminal | Activate Portal Without Bombs"),
                        can_use_screw_attack(state, player),
                        condition_or([
                            can_use_darkburst(state, player),
                            can_use_sonic_boom(state, player),
                        ]),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Portal Terminal | Activate Portal Without Bombs NSJ"),
                        can_use_screw_attack(state, player, z_axis=True),
                        condition_or([
                            can_use_darkburst(state, player),
                            can_use_sonic_boom(state, player),
                        ]),
                    ])
                ]),
                parent=self,
            )
        ]

class PortalTerminal_BehindGate(MetroidPrime2Region):
    name = "Portal Terminal"
    desc = "Behind Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Terminal (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Dark Agon Wastes - Portal Site | Gate Opened"),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Portal Terminal Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]