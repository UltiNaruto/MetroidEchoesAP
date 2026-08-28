from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_lay_bomb,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    can_activate_safe_zone,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveTempleAccess_KeyDoor(MetroidPrime2Region):
    name = "Hive Temple Access"
    desc = "Key Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (South Upper)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    state.has("Ing Hive - Hive Temple Access | Ing Hive Key Lock Opened", player), 
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple Access | BSJ SA to Skip Key Door"),
                        can_lay_bomb(state, player),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple Access | BSJ to Skip Key Door"),
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple Access | Slope Jump SA to Skip Key Door"),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Ing Hive Key Lock Opened",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Temple Access | Ing Hive Key Lock Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has_all({
                "Ing Hive Key 1",
                "Ing Hive Key 2",
                "Ing Hive Key 3",
            }, player),
        )

class HiveTempleAccess_SafeZone(MetroidPrime2Region):
    name = "Hive Temple Access"
    desc = "Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access (Temple Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access (Key Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    condition_and([
                        state.has("Ing Hive - Hive Temple Access | Ing Hive Key Lock Opened", player),
                        condition_or([
                            condition_and([
                                has_trick_enabled(state, player, "Ing Hive - Hive Temple Access | Z-Axis SA to Front of Opened Gate"),
                                can_use_screw_attack(state, player, True),
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Ing Hive - Hive Temple Access | SJ Standable Enemy to Front of Opened Gate"),
                                state.has_all({
                                    "Space Jump Boots",
                                    "Ing Hive - Hive Temple | Quadraxis",
                                    "Scan Visor",
                                }, player),
                                condition_or([ #Needs to check whether the room can be reset since the enemy can be killed
                                    has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                                    has_trick_enabled(state, player, "Ing Hive - Hive Temple | Scan Dash to West Door"),
                                ])
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Ing Hive - Hive Temple Access | SA to Front of Opened Gate"),
                                can_use_screw_attack(state, player),
                            ]),
                        ])
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple Access | BSJ Reverse Key Door Closed Gate"),
                        can_lay_bomb(state, player),
                        state.has_all({ 
                            "Space Jump Boots",
                            "Ing Hive - Hive Temple | Quadraxis",
                        }),
                        condition_or([ #Needs to check whether the room can be reset since the enemy can be killed
                            can_use_screw_attack(state, player),
                            condition_and([
                                can_use_screw_attack(state, player, True),
                                has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                            ]),
                            condition_and([
                                state.has("Scan Visor", player),
                                condition_or([
                                    has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                                    has_trick_enabled(state, player, "Ing Hive - Hive Temple | Scan Dash to West Door"),
                                ])
                            ])
                        ]),
                    ]),
                ]),
            ]),
        ),
    ]

class HiveTempleAccess_TempleDoor(MetroidPrime2Region):
    name = "Hive Temple Access"
    desc = "Temple Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (North)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                    can_activate_safe_zone(state, player),
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
        ),
    ]
