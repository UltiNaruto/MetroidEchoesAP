from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_use_spider_ball,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveTemple(MetroidPrime2Region):
    name = "Hive Temple"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (North)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (South)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (West)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        condition_or([ #These two tricks have the same requirements but different difficulties
                            has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                            has_trick_enabled(state, player, "Ing Hive - Hive Temple | Scan Dash to West Door"),
                        ]),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (Quadraxis)",
            door=DoorCover.Opened,
            rule=lambda state, player: quadraxis_combat_logic(state, player)
        ),
    ]

class HiveTemple_North(MetroidPrime2Region):
    name = "Hive Temple"
    desc = "North"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access (Temple Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
    ]

class HiveTemple_South(MetroidPrime2Region):
    name = "Hive Temple"
    desc = "South"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Controller Access (Temple Door)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

class HiveTemple_West(MetroidPrime2Region):
    name = "Hive Temple"
    desc = "South"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access (Temple Door)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True
        ),
    ],

class HiveTemple_Quadraxis(MetroidPrime2Region):

    name = "Hive Temple"
    desc = "Quadraxis"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
                quadraxis_combat_logic(state, player),
            ]),
        ),
    ],



    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Quadraxis",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Temple | Quadraxis",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True,
        )
        self.add_location(
            name="Pickup (Annihilator Beam)",
            can_access=lambda state, player: state.has("Ing Hive - Hive Temple | Quadraxis", player),
        )
