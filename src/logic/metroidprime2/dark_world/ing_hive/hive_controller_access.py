from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_lay_bomb,
    can_use_darkburst,
    can_use_screw_attack,
    can_use_sunburst,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveControllerAccess_TempleDoor(MetroidPrime2Region):
    name = "Hive Controller Access"
    desc = "Temple Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Controller Access (Controller Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Ing Hive - Hive Controller Access | Bomb Slot Without Bombs"),
                    state.has("Space Jump Boots", player),
                    condition_or([
                        can_use_darkburst(state, player, amount_to_use=3),
                        can_use_sunburst(state, player, amount_to_use=3),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player,"Ing Hive - Hive Controller Access | Bomb Slot Without Bombs NSJ SA Standable"),
                    can_use_screw_attack(state, player, z_axis=True),
                    condition_or([
                        can_use_darkburst(state, player, amount_to_use=3),
                        can_use_sunburst(state, player, amount_to_use=3),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (South)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True,
        ),
    ]

class HiveControllerAccess_ControllerDoor(MetroidPrime2Region):
    name = "Hive Controller Access"
    desc = "Controller Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Controller Access (Temple Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Ing Hive - Hive Controller Access | Bomb Slot Without Bombs"),
                    state.has("Space Jump Boots", player),
                    condition_or([
                        can_use_darkburst(state, player, amount_to_use=3),
                        can_use_sunburst(state, player, amount_to_use=3),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player,"Ing Hive - Hive Controller Access | Bomb Slot Without Bombs NSJ SA Standable"),
                    can_use_screw_attack(state, player, z_axis=True),
                    condition_or([
                        can_use_darkburst(state, player, amount_to_use=3),
                        can_use_sunburst(state, player, amount_to_use=3),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]
