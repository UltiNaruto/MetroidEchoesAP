from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_use_screw_attack,
    can_activate_dark_portal,
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class CommandCenter_Bottom(MetroidPrime2Region):
    name = "Command Center"
    desc = "Command Center Access Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access (Bottom)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access (Morph Tunnel)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has_all({
                "Agon Wastes - Command Center | Gate Closed",
                "Agon Wastes - Command Center | Gate Opened",
            }, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Behind Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                not state.has("Agon Wastes - Command Center | Gate Closed"),
                state.has("Agon Wastes - Command Center | Gate Opened"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Doomed Entry (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Gate Closed",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Command Center | Gate Closed",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: state.has("Morph Ball", player),
                parent=self,
            ),
        ]

class CommandCenter_BehindGate(MetroidPrime2Region):
    name = "Command Center"
    desc = "Behind Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                not state.has("Agon Wastes - Command Center | Gate Closed"),
                state.has("Agon Wastes - Command Center | Gate Opened"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class CommandCenter_Top(MetroidPrime2Region):
    name = "Command Center"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Securtiy Station B (Command Center Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Command Center | Scan/Combat Dash over Gap to Security Station B"),
                        state.has("Scan Visor", player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Command Center | NSJ SA over Gap to Security Station B"),
                        can_use_screw_attack(state, player),
                    ])
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access (Top)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        )
    ]

class CommandCenter_GateController(MetroidPrime2Region):
    name = "Command Center"
    desc = "Gate Controller"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Securtiy Station B (Command Center Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Gate Opened",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Command Center | Gate Opened",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
        ]