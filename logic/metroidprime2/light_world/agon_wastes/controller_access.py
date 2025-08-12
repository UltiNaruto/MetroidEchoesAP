from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_darkburst,
    can_use_sonic_boom
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Region, MetroidPrime2Exit
from .....Utils import condition_or, condition_and

class ControllerAccess_AgonTempleSide(MetroidPrime2Exit):
    name = "Controller Access"
    desc = "Agon Temple Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Controller Access (Agon Energy Controller Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    # TODO: check if this can be done with Sunburst
                    has_trick_enabled(state, player, "Agon Wastes - Controller Access | Bomb Slot without Bombs"),
                    state.has_all({
                        "Morph Ball",
                        "Space Jump Boots"
                    }, player),
                    condition_or([
                        can_use_darkburst(state, player),
                        can_use_sonic_boom(state, player),
                    ]),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Energy Controller",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Contoller Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class ControllerAccess_AgonEnergyControllerSide(MetroidPrime2Region):
    name = "Controller Access"
    desc = "Agon Energy Controller Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Controller Access (Agon Temple Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    # TODO: check if this can be done with Sunburst
                    has_trick_enabled(state, player, "Agon Wastes - Controller Access | Bomb Slot without Bombs"),
                    state.has_all({
                        "Morph Ball",
                        "Space Jump Boots"
                    }, player),
                    condition_or([
                        can_use_darkburst(state, player),
                        can_use_sonic_boom(state, player),
                    ]),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Controller Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Energy Controller",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]