from BaseClasses import ItemClassification, MultiWorld

from ... import (
    has_dark_suit,
    has_light_suit,
    can_activate_light_portal,
    can_activate_safe_zone,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class StagingArea(MetroidPrime2Region):
    name = "Staging Area"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Staging Area (Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    state.has("Ing Hive - Staging Area | Echo Scan", player),
                    has_trick_enabled(state, player, "Ing Hive - Staging Area | Reach Door with SJ Standable")
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Staging Area (Lower)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Ing Hive - Staging Area | Echo Scan", player)
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Main Research (Portal)", #Name is subject to change
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
    ]


    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Echo Scan",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Staging Area | Echo Scan",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                state.has_all({
                    "Scan Visor",
                    "Echo Visor",
                    }, player),
                ]),
            )

class StagingArea_Door(MetroidPrime2Region):
    name = "Staging Area"
    desc = "Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive West Transport (Lower)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                    can_activate_safe_zone(state, player),
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
            ),
        MetroidPrime2Exit(
            destination="Ing Hive - Staging Area",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
    ]

class StagingArea_Lower(MetroidPrime2Region):
    name = "Staging Area"
    desc = "Lower"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Staging Area",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has_all({
                "Space Jump Boots",
                "Ing Hive - Staging Area | Echo Scan",
            }, player),
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Main Research (Drone)", #Name is subject to change
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
    ]
