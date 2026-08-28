from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_use_boost_ball,
    can_lay_bomb,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class TempleSecurityAccess_Centre(MetroidPrime2Region):
    name = "Temple Security Access"
    desc = "Centre"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access (Temple Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with NSJ SA"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with SA"),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with Wall Boosts"),
                        can_use_boost_ball(state, player)
                    ]),
                ]),
                condition_or([
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with Dark Suit"),
                        has_dark_suit(state, player),
                        state.count("Energy Tank", player) >= 1
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with No Suit"),
                        state.count("Energy Tank", player) >= 2
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access (Training Site Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with NSJ SA"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with SA"),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with Wall Boosts"),
                        can_use_boost_ball(state, player)
                    ]),
                ]),
                condition_or([
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with Dark Suit"),
                        has_dark_suit(state, player),
                        state.count("Energy Tank", player) >= 1
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with No Suit"),
                        state.count("Energy Tank", player) >= 2
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class TempleSecurityAccess_TempleDoor(MetroidPrime2Region):
    name = "Temple Security Access"
    desc = "Temple Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (West)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access (Centre)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with NSJ SA"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with SA"),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with Wall Boosts"),
                        can_use_boost_ball(state, player)
                    ]),
                ]),
                condition_or([
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with Dark Suit"),
                        has_dark_suit(state, player),
                        state.count("Energy Tank", player) >= 1
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with No Suit"),
                        state.count("Energy Tank", player) >= 2
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class TempleSecurityAccess_TrainingSiteDoor(MetroidPrime2Region):
    name = "Temple Security Access"
    desc = "Training Site Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Crystal Door)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access (Centre)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with NSJ SA"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with SA"),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with Wall Boosts"),
                        can_use_boost_ball(state, player)
                    ]),
                ]),
                condition_or([
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with Dark Suit"),
                        has_dark_suit(state, player),
                        state.count("Energy Tank", player) >= 1
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with No Suit"),
                        state.count("Energy Tank", player) >= 2
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
