from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_use_spider_ball,
    can_lay_bomb,
    can_use_screw_attack,
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class CentralMiningStation_CentralMiningStationSide(MetroidPrime2Region):
    name = "Central Mining Station"
    desc = "Central Station Access Side",
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Behind Laser Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Turret Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
                    can_use_spider_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | BSJ up to Turret Platform"),
                    state.has("Space Jump Boots", player),
                    can_lay_bomb(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Center Platforms)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has_all({
                    "Space Jump Boots",
                    "Agon Wastes - Central Mining Station | Pirates Fought"
                }, player),
                condition_or([
                    has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Slope Jump to Center Platforms"),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Scan/Combat Dash to Center Platforms"),
                        state.has("Scan Visor", player),    
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | SA from Standable to Center Platforms"),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Station Access (Central Mining Station Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pirtates Fought",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Command Center Access | Pirates Fought",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            )
        ]

class CentralMiningStation_TurretPlatform(MetroidPrime2Region):
    name = "Central Mining Station"
    desc = "Turret Platform"
    exits_ [
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Central Station Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Behind Laser Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Center Platforms)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
                    has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | NSJ BSJ SA to Center Platform"),
                    can_lay_bomb(state, player),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
                        can_use_screw_attack(state, player),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Scan/Combat Dash to/from Center Platforms to Turret Platform"),
                            state.has("Scan Visor", player),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Roll Jump to/from Turret Platform to Center Platforms"),
                            state.has("Morph Ball", player),
                        ]),
                    ]),
                ]),
                has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Extended Dash to/from Turret Platform to Center Platforms"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access (Top)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        )
    ]

class CentralMiningStation_CenterPlatforms(MetroidPrime2Region):
    name = "Central Mining Station"
    desc = "Center Platforms"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Central Station Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Turret Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        can_use_screw_attack(state, player),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Roll Jump to/from Turret Platform to Center Platforms"),
                            state.has("Morph Ball", player),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Scan/Combat Dash to/from Center Platforms to Turret Platform"),
                            state.has("Scan Visor", player),
                        ])
                    ]),
                ]),
                has_trick_enabled(state, player, "Agon Wastes - Central Mining Station | Extended Dash to/from Center Platforms to Turret Platform"),
            ]),
        )
    ]

class CentralMiningStation_BehindLaserGate(MetroidPrime2Region):
    name = "Central Mining Station"
    desc = "Behind Laser Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Central Station Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Central Mining Station | Pirates Fought", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Control Center Access (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class CentralMiningStation_Item(MetroidPrime2Region):
    name = "Central Mining Station"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Center Platforms)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Beam Ammo Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            )
        ]