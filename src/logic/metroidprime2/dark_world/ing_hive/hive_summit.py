from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_use_boost_ball,
    can_use_spider_ball,
    can_lay_bomb,
    has_dark_suit,
    has_light_suit,
    can_activate_light_portal,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveSummit_Portal(MetroidPrime2Region):
    name = "Hive Summit"
    desc = "Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Summit (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Space Jump Booots", player)
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Aerie (Echo Visor)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player)
        ),
    ]

class HiveSummit_SafeZone(MetroidPrime2Region):
    name = "Hive Summit"
    desc = "Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Summit (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_use_spider_ball(state, player),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        can_use_boost_ball(state, player)
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Summit | Reach Portal with Bombs Only"),
                        can_lay_bomb(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Summit | Reach Portal with Boost and Bombs"),
                        can_use_boost_ball(state, player),
                        can_lay_bomb(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Summit | Reach Portal with Boost Only"),
                        can_use_boost_ball(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Summit | Reach Portal with SJ Only"),
                        state.has("Space Jump Boots", player)
                    ]),
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
