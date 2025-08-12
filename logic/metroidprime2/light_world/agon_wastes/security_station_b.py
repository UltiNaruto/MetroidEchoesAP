from BaseClasses import MultiWorld, ItemClassification
from ... import (
    can_use_dark_beam
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and

class SecurityStationB_CommandCenterSide(MetroidPrime2Region):
    name = "Security Station B"
    desc = "Command Center Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Securtiy Station B (Main Reactor Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Agon Wastes - Security Station B | Cutscene Watched"),
                can_use_dark_beam(state, player),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Gate Scan)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class SecurityStationB_MainReactorSide(MetroidPrime2Region):
    name = "Security Station B"
    desc = "Main Reactor"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station B (Command Center Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Agon Wastes - Security Station B | Cutscene Watched"),
                can_use_dark_beam(state, player),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Security Station B Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        )
    ]