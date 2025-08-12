from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_lay_pb,
    can_use_boost_ball,
    can_use_spider_ball,
    can_use_screw_attack,
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class MiningStationA_MiningStationAccessSide(MetroidPrime2Region):
    name = "Mining Station A"
    desc = "Mining Station Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A (Mining Station A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Mining Station A Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class MiningStationA_Center(MetroidPrime2Exit):
    name = "Mining Station A"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Mining Station Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Portal Access A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Behind Translator Gate)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Central Station Access Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | DBJ to Central Station Access Platform"),
                    can_lay_bomb(state, player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Temple Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has_any({
                    "Missile Launcher",
                    "Space Jump Boots"
                }, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | NSJ SA to Temple Access Ledge"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | SA Z-Axis to Temple Access Ledge"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | Combat/Scan Dash to Temple Access Ledge"),
                    state.has_any({
                        "Combat Visor",
                        "Scan Visor"
                    }, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | Extended Dash to Temple Access Ledge"),
                    state.has("Scan Visor", player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | Boost Jump to Temple Access Ledge"),
                    can_use_boost_ball(state, player),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_lay_pb(state, player),
                    can_lay_bomb(state, player),
                    can_use_spider_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | 3BSJ to Standable Terrain"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player),
                ]),
            ])
        ),
    ]

class MiningStationA_PortalAccessASide(MetroidPrime2Region):
    name = "Mining Station A"
    desc = "Portal Access A Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A (Mining Station A Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class MiningStationA_TempleAccessLedge(MetroidPrime2Region):
    name = "Mining Station A"
    desc = "Temple Access Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Temple Access",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
    ]

class MiningStationA_CentralStationAccessPlatform(MetroidPrime2Region):
    name = "Mining Station A"
    desc = "Central Station Access Platform"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Scan Post)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | DBJ to Scan Post"),
                    can_lay_bomb(state, player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Behind Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Agon Wastes - Mining Station A | Gate Opened", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Mining Station A | DBJ to Central Station Access Ledge"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        )
    ]

class MiningStationA_ScanPost(MetroidPrime2Region):
    name = "Mining Station A"
    desc = "Scan Post"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Central Station Access Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots"),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | Combat/Scan Dash to Central Station Access Ledge"),
                    state.has_any({
                        "Combat Visor",
                        "Scan Visor"
                    }, player)
                ])
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Central Station Access Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Gate Opened",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Mining Station A | Gate Opened",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
        ]

class MiningStationA_CentralStationAccessLedge(MetroidPrime2Region):
    name = "Mining Station A"
    desc = "Central Station Access Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Agon Wastes - Mining Station A | Gate Opened", player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | 2BSJ over Gate"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station A | SA Bonk over Gate"),
                    can_use_screw_attack(state, player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Station Access (Mining Station A Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class MiningStationA_Item(MetroidPrime2Region):
    name = "Mining Station A"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]