from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_light_portal,
    can_activate_safe_zone,
    can_lay_bomb,
    can_use_annihilator_beam,
    can_use_boost_ball,
    can_use_dark_beam,
    can_use_grapple_beam,
    can_use_light_beam,
    can_use_power_beam,
    can_use_screw_attack,
    can_use_seeker_launcher,
    can_use_spider_ball,
    has_dark_suit,
    has_light_suit,
    has_missile_count,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveDynamoWorks_NorthTrackSafeZone(MetroidPrime2Region):
    name = "Hive Dynamo Works"
    desc = "North Track Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (North Track Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    can_use_spider_ball(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Skip North Spider Track with BSJ"),
                        can_lay_bomb(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Skip North Spider Track with Slope Jump"),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (North Portal Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                    ]),
                ]),
                condition_or([
                    can_use_grapple_beam(state, player),
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Z-Axis SA across gap North"),
                        can_use_screw_attack(state, player, True)
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Scan Dash across gap North"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Roll Jump across gap North"),
                        state.has_all({
                            "Morph Ball",
                            "Space Jump Boots"
                        }, player)
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | NSJ E-Dash across gap North"),
                        state.has("Scan Visor", player)
                    ]),
                ]),
            ]),
        ),
    ],


class HiveDynamoWorks_NorthTrackDoor(MetroidPrime2Region):
    name = "Hive Dynamo Works"
    desc = "North Track Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive East Transport (Upper)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (North Track Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ],

class HiveDynamoWorks_NorthPortalSafeZone(MetroidPrime2Region):
    name = "Hive Dynamo Works"
    desc = "North Portal Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (North Track Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_use_grapple_beam(state, player),
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Z-Axis SA across gap North"),
                        can_use_screw_attack(state, player, True)
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Terminal Fall across gap North"),
                        state.has("Space Jump Boots", player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Scan Dash across gap North"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Roll Jump across gap North"),
                        state.has_all({
                            "Morph Ball",
                            "Space Jump Boots"
                        }, player)
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | NSJ Boost Jump across gap North"),
                        can_use_boost_ball(state, player)
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | NSJ E-Dash Terminal Fall across gap North"),
                        state.has("Scan Visor", player)
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Access (Echo Lock)",
            door=DoorCover.Light,
            rule=lambda state, player: condition_or([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                    ]),
                ]),
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Dynamo Works", #Name is subject to change depending on what it will be named on the other side
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_light_portal(state, player),
                state.has("Ing Hive - Hive Dynamo Works | Dark Visor Locks Destroyed", player),
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Dark Visor Locks Destroyed",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Dynamo Works | Dark Visor Locks Destroyed",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_use_seeker_launcher(state, player, dark_visor=True),
        )


class HiveDynamoWorks_SouthPortalDoor(MetroidPrime2Region):
    name = "Hive Dynamo Works"
    desc = "South Portal Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Cache 2",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (Ing Cache)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Dark Visor", player), 
                condition_or([
                    state.count("Energy Tank", player) >= 4,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    can_use_annihilator_beam(state, player),
                    can_use_dark_beam(state, player),
                    can_use_light_beam(state, player),
                    can_use_power_beam(state, player),
                    has_missile_count(state, player, 5)
                ]),
                condition_or([
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_use_spider_ball(state, player),
                    ]),
                    condition_and([
                        state.has("Morph Ball", player),
                        condition_or([
                            condition_and([
                                has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | SA Standable to Ing Cache South"),
                                can_use_screw_attack(state, player),
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | SJ Standable to Ing Cache South"),
                                state.has("Space Jump Boots", player),
                            ]),
                        ]),
                    ]),
                ]),
            ])
        )
    ]

class HiveDynamoWorks_IngCache(MetroidPrime2Region):
    name = "Hive Dynamo Works"
    desc = "Ing Cache"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (South Portal Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has_all({
                    "Morph Ball",
                    "Dark Visor",
                    }, player), 
                condition_or([
                    state.count("Energy Tank") >= 4, 
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([ 
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_use_spider_ball(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Works | Scan Dash from Ing Cache South"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player)
                    ]),
                    can_use_screw_attack(state, player),

                ]),
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Sky Temple Key 6)",
            can_access=lambda state, player: True,
        )
