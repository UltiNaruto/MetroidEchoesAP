from BaseClasses import MultiWorld

from ... import (
    can_lay_bomb,
    has_missile_count,
    has_pb_count,
    has_dark_suit,
    has_light_suit,
    can_activate_safe_zone,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveReactor_Upper(MetroidPrime2Region):
    name = "Hive Reactor"
    desc = "Upper"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor (Lower)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                state.has("Space Jump Boots", player),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Unseen Way (West)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]

class HiveReactor_Lower(MetroidPrime2Region):
    name = "Hive Reactor"
    desc = "Lower"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Cache 1",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Save Station 1",
            door=DoorCover.Missile,
            rule=lambda state, player: condition_and([
                has_missile_count(state, player, 5),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor Access",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                state.has("Space Jump", player),
                has_pb_count(state, player, 1),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor (Upper)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Reactor | NSJ Climb with BSJ"),
                        can_lay_bomb(state, player),
                    ]),

                ]),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
