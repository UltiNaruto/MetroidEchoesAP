from BaseClasses import MultiWorld

from ... import (
    can_use_screw_attack,
    has_pb_count,
    has_dark_suit,
    has_light_suit,
    can_activate_safe_zone,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveReactorAccess_Lower(MetroidPrime2Region):
    name = "Hive Reactor Access"
    desc = "Lower"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Entrance Defense Hall",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor Access (Upper)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        can_activate_safe_zone(state, player),
                        state.count("Energy Tank", player) >=1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                    ]),
                ]),
                condition_and([
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Reactor Access | NSJ SA Respawn to reach upper Door"),
                        can_use_screw_attack(state, player, True, True),
                    ]),
                    condition_or([
                        state.count("Energy Tank", player) >= 2,
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                    ]),
                ]),
            ]),
        ),
    ]

class HiveReactorAccess_Upper(MetroidPrime2Region):
    name = "Hive Reactor Access"
    desc = "Upper"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor Access (Lower)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor (Lower)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.has("Space Jump", player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Reactor Access | NSJ SA Respawn to reach upper Door"),
                        can_use_screw_attack(state, player, True, True),
                    ]),
                ]),
                has_pb_count(state, player, 1),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
    
