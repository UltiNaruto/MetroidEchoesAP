from BaseClasses import MultiWorld

from ... import (
    can_activate_safe_zone,
    can_lay_bomb,
    can_use_spider_ball,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class CullingChamber_NearPortal(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "Near Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Ing Hive - Culling Chamber | DBJ Broken Tube"),
                    can_lay_bomb(state, player)
                ]),
                has_trick_enabled(state, player, "Ing Hive - Culling Chamber | NSJ Broken Tube"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hazing Cliff (Door)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Safe Zone Near Portal)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                    ])
                ]),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Culling Chamber | DBJ Broken Tube"),
                        can_lay_bomb(state, player)
                ]),
                    has_trick_enabled(state, player, "Ing Hive - Culling Chamber | NSJ Broken Tube"),
                ]),
            ]),
        ),
    ]

class CullingChamber_NorthSafeZone(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "North Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive East Transport (Lower)",
            door=DoorCover.Dark,
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
            destination="Ing Hive - Culling Chamber (Safe Zone Near Portal)",
            door=DoorCover.Opened,
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
            destination="Ing Hive - Culling Chamber (West Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Spider Track)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_lay_bomb(state, player),
                can_use_spider_ball(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class CullingChamber_Portal(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "Portal"
    exits = [
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Hall of Combat Mastery", #The name for the destination might change
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Near Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
    ]

class CullingChamber_SafeZoneNearPortal(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "Safe Zone Near Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Near Portal)",
            door=DoorCover.Opened,
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
            destination="Ing Hive - Culling Chamber (North Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class CullingChamber_SpiderTrack(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "Spider Track"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (North Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_lay_bomb(state, player),
                can_use_spider_ball(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Ing Hive Temple Key 1)",
            can_access=lambda state, player: True,
        )

class CullingChamber_WestSafeZone(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "West Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (North Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Unseen Way (East)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]
