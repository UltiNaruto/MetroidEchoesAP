from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_use_spider_ball,
    has_dark_suit,
    has_light_suit,
    can_activate_light_portal,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HivePortalChamber_Lower(MetroidPrime2Region):
    name = "Hive Portal Chamber"
    desc = "Lower"
    exits = [
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Transit Station (Lower)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_light_portal(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 2, #Should possibly be increased if it is assumed the player will defeat the Ingsmasher instead of just ignoring it
                    condition_and([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class HivePortalChamber_Upper(MetroidPrime2Region):
    name = "Hive Portal Chamber"
    desc = "Upper"
    exits = [
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Transit Station (Upper)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_light_portal(state, player),
                can_use_spider_ball(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
