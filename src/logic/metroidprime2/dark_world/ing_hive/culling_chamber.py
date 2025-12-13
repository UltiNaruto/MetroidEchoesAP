from BaseClasses import MultiWorld

from ... import (
    can_activate_safe_zone,
    can_lay_bomb,
    can_use_spider_ball,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled
)

from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
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
                #has_trick_enabled(state, player, "Placeholder for NSJ and DBJ trick"),
                state.has("Space Jump Boots", player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hazing Cliff",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank") >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Safe Zone 1)",
            door=DoorCover.Any,
            rule=lambda state, player: can_activate_safe_zone(state, player),
        )
    ]

class CullingChamber_Portal(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "Portal"
    exits = [
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Hall of Combat Mastery", #The name for the destination might change
            door=DoorCover.ScanVisor,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Near Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                #has_trick_enabled(state, player, "Placeholder for NSJ and DBJ trick"),
                state.has("Space Jump Boots", player)
            ])
        )
    ]

class CullingChamber_SafeZone1(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "Safe Zone Near Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Near Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: 
                can_activate_safe_zone(state, player),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Safe Zone 2)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_safe_zone(state, player),
        )
    ]

class CullingChamber_SafeZone2(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "North Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Safe Zone 1)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_safe_zone(state, player),
        ),
        MetroidPrime2Exit(
            destionation="Ing Hive - Culling Chamber (Safe Zone 3)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive East Transport (Lower)",
            door=DoorCover.Dark,
            rule=lambda state, player: can_activate_safe_zone(state, player),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Spider Track)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: condition_and([
                can_lay_bomb,
                can_use_spider_ball,
                condition_or([
                    state.count("Energy Tank") >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ])
            ])
        )
    ]

class CullingChamber_SafeZone3(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "West Safe Zone"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Safe Zone 2)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Unseen Way (East)",
            door=DoorCover.Any,
            rule=lambda state, player: can_activate_safe_zone(state, player)
        ),
    ]


class CullingChamber_SpiderTrack(MetroidPrime2Region):
    name = "Culling Chamber"
    desc = "Spider Track"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Safe Zone 2)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: condition_and([
                can_lay_bomb,
                can_use_spider_ball,
                condition_or([
                    state.count("Energy Tank") >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ])
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Ing Hive Temple Key 1)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]