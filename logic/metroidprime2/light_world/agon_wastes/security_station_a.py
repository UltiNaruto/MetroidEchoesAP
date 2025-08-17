from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_darkburst,
    can_use_sonic_boom
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class SecurityStationA_BiostorageStationSide(MetroidPrime2Region):
    name = "Security Station A"
    desc = "Biostorage Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station A (Bioenergy Production Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Security Station A | Bomb Slot without Bombs"),
                    state.has_all({
                        "Morph Ball",
                        "Space Jump Boots",
                    }, player),
                    condition_or([
                        can_use_darkburst(state, player),
                        can_use_sonic_boom(state, player),
                    ]),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Station (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class SecurityStationA_BioenergyProductionSide(MetroidPrime2Region):
    name = "Security Station A"
    desc = "Bioenergy Production Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station A (Biostorage Station Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Security Station A | Bomb Slot without Bombs"),
                    state.has_all({
                        "Morph Ball",
                        "Space Jump Boots",
                    }, player),
                    condition_or([
                        can_use_darkburst(state, player),
                        can_use_sonic_boom(state, player),
                    ]),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]