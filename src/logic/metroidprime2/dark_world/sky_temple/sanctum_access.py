from ... import (
    can_use_screw_attack,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class SanctumAccess_Bottom(MetroidPrime2Region):
    name = "Sanctum Access"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple - Sanctum Access (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_light_suit(state, player),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Sky Temple - Sanctum Access | Z-Axis SA to Top"),
                        can_use_screw_attack(state, player, z_axis=True),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple - Sky Temple Energy Controller",
            door=DoorCover.Any,
            rule=lambda state, player: has_light_suit(state, player),
        ),
    ]


class SanctumAccess_Top(MetroidPrime2Region):
    name = "Sanctum Access"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple - Sanctum Access (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: has_light_suit(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple - Sanctum",
            door=DoorCover.Any,
            rule=lambda state, player: has_light_suit(state, player),
        ),
    ]