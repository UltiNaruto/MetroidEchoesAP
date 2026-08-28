from BaseClasses import MultiWorld

from ... import (
    can_use_boost_ball,
    can_use_spider_ball,
    can_lay_bomb_or_pb,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or



class HiveGyroChamber_Ball(MetroidPrime2Region): #The Soup Bowl
    name = "Hive Gyro Chamber"
    desc = "Ball"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (North Lower)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_use_spider_ball(state, player),
                condition_or([
                    can_lay_bomb_or_pb(state, player),
                    has_trick_enabled(state, player, "Ing Hive - Hive Gyro Chamber | Gyro Chamber Without Morph Weapons"),
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (North Upper)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([ #Could very well be tricks to get up without SJ or Boost.
                can_use_spider_ball(state, player),
                condition_or([
                    can_lay_bomb_or_pb(state, player),
                    has_trick_enabled(state, player, "Ing Hive - Hive Gyro Chamber | Gyro Chamber Without Morph Weapons")
                ]),
                condition_or([
                    state.has("Space Jump Boots", player),
                    can_use_boost_ball(state, player),
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (South Lower)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_use_spider_ball(state, player),
                condition_or([
                    can_lay_bomb_or_pb(state, player),
                    has_trick_enabled(state, player, "Ing Hive - Hive Gyro Chamber | Gyro Chamber Without Morph Weapons")
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (South Upper)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([ 
                can_use_spider_ball(state, player),
                condition_or([
                    can_lay_bomb_or_pb(state, player),
                    has_trick_enabled(state, player, "Ing Hive - Hive Gyro Chamber | Gyro Chamber Without Morph Weapons")
                ]),
                condition_or([
                    state.has("Space Jump Boots", player),
                    can_use_boost_ball(state, player),
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Ing Hive Key 2)",
            can_access=lambda state, player: condition_and([
                condition_or([
                    can_use_boost_ball(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Gyro Chamber | Get Item without Boost using SA"),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
                condition_or([
                    can_lay_bomb_or_pb(state, player),
                    has_trick_enabled(state, player, "Ing Hive - Hive Gyro Chamber | Gyro Chamber Without Morph Weapons"),
                ]),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ])
            ]),
        )

class HiveGyroChamber_NorthLower(MetroidPrime2Region):
    name = "Hive Gyro Chamber"
    desc = "North Lower"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (Ball)",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Save Station 2",
            door=DoorCover.Missile,
            rule=lambda state, player: True, 
        ),
    ]

class HiveGyroChamber_NorthUpper(MetroidPrime2Region):
    name = "Hive Gyro Chamber"
    desc = "North Upper"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (Ball)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        )
    ]

class HiveGyroChamber_SouthLower(MetroidPrime2Region):
    name = "Hive Gyro Chamber"
    desc = "South Lower"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Access (Gyro Side)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (Ball)",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        )
    ]

class HiveGyroChamber_SouthUpper(MetroidPrime2Region):
    name = "Hive Gyro Chamber"
    desc = "South Upper"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (Ball)",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access (Key Door)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]
