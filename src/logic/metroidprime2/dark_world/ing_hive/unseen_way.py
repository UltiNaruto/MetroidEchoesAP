from BaseClasses import MultiWorld

from ... import (
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    can_activate_safe_zone,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class UnseenWay_East(MetroidPrime2Region):
    name = "Unseen Way"
    desc = "East"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (West Safe Zone)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                can_activate_safe_zone(state, player),
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Unseen Way (West)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    condition_and([
                        state.has_all({"Space Jump Boots", "Dark Visor"}, player),
                    ]),
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Unseen Way | Cross with Dark Visor NSJ SA"),
                        state.has("Dark Visor", player),
                        condition_or([
                            can_activate_safe_zone(state, player),
                            state.count("Energy Tank", player) >= 2,
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                        ]),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Unseen Way | Cross without Dark Visor with SJ"),
                        state.has("Space Jump Boots", player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Unseen Way | Cross without Dark Visor with NSJ SA"),
                        can_use_screw_attack(state, player, False, True),
                        condition_or([
                            can_activate_safe_zone(state, player),
                            state.count("Energy Tank", player) >= 2,
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                        ]),
                    ]),
                ]),
            ]),
        ),
    ]


class UnseenWay_West(MetroidPrime2Region):
    name = "Unseen Way"
    desc = "West"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Reactor (Upper)",
            door=DoorCover.Any,
            rule=lambda state, player: can_activate_safe_zone(state, player),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Unseen Way (East)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    condition_and([
                        state.has_all({"Space Jump Boots", "Dark Visor"}, player),
                    ]),
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Unseen Way | Cross with Dark Visor NSJ SA"),
                        state.has("Dark Visor", player),
                        condition_or([
                            can_activate_safe_zone(state, player),
                            state.count("Energy Tank", player) >= 2,
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                        ]),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Unseen Way | Cross without Dark Visor with SJ"),
                        state.has("Space Jump Boots", player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Unseen Way | Cross without Dark Visor with NSJ SA"),
                        can_use_screw_attack(state, player, False, True),
                        condition_or([
                            can_activate_safe_zone(state, player),
                            state.count("Energy Tank", player) >= 2,
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                        ]),
                    ]),
                ]),
            ]),
        ),
    ]
