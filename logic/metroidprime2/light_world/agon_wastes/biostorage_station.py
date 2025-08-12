from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_screw_attack,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class BiostorageStation_Bottom(MetroidPrime2Region):
    name = "Biostorage Station"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Station (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Scan Visor", player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Biostorage Station | Jump to Top Level from Crates"),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Biostorage Station | TBJS to Top Level"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Biostorage Station | SA Recoil up to Top Level"),
                    can_use_screw_attack(state, player),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Access",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        )
    ]

class BiostorageStation_Top(MetroidPrime2Region):
    name = "Biostorage Station"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Storage B",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station A (Biostorage Station Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Station (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        )
    ]