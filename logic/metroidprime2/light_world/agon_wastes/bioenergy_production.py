from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_boost_ball,
    can_use_spider_ball,
    can_use_screw_attack
)
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class BioenergyProduction_Bottom(MetroidPrime2Region):
    name = "Bioenergy Production"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Ventilation Area B Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_boost_ball(state, player),
                                    can_use_spider_ball(state, player),
                                    condition_or([
                                        condition_and([
                                            has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | NSJ SA across Containers"),
                                            can_use_screw_attack(state, player),
                                        ]),
                                        has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | Scan/Combat Dash across Containers"),
                                    ]),
                                ]),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | BSJ up Container Steps"),
                                    can_lay_bomb(state, player),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | SA from Standable to Ventilation Area B Ledge"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_boost_ball(state, player),
                                    can_use_spider_ball(state, player),
                                    condition_or([
                                        has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | Scan/Combat Dash across Containers"),
                                        has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | Extended Dash across Containers"),
                                        condition_and([
                                            has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | NSJ SA across Containers"),
                                            can_use_screw_attack(state, player),
                                        ]),
                                    ]),
                                ]),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | BSJ up Container Steps then NSJ SA to Item"),
                                    can_use_screw_attack(state, player),
                                    can_lay_bomb(state, player),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | SA from Standable to Item"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Storage C Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_boost_ball(state, player),
                                    can_use_spider_ball(state, player),
                                ]),
                                condition_and([
                                    has_trick_enabled("Agon Wastes - Bioenergy Production | BSJ up Container Steps then NSJ SA to Storage C Ledge"),
                                    can_use_screw_attack(state, player),
                                    can_lay_bomb(state, player),
                                ]),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | Roll Jump to Storage C Ledge"),
                                    state.has("Space Jump Boots", player),
                                ]),
                            ]),
                        ]),
                        can_use_screw_attack(state, player),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | Scan/Combat Dash to Storage C Ledge"),
                            state.has("Space Jump Boots", player),
                        ])
                    ])
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | SA from Standable to Storage C Ledge"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station A (Bioenergy Production Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class BioenergyProduction_VentilationAreaBLedge(MetroidPrime2Region):
    name = "Bioenergy Production"
    desc = "Ventilation Area B Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Storage C Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | SA around Pipes"),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area B (Bioenergy Production Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class BioenergyProduction_StorageCLedge(MetroidPrime2Exit):
    name = "Bioenergy Production"
    desc = "Storage C Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Ventilation Area B Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Agon Wastes - Bioenergy Production | SA around Pipes"),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Storage C",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True,
        ),
    ]

class BioenergyProduction_Item(MetroidPrime2Region):
    name = "Bioenergy Production"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Ventilation Area B Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Storage C Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Energy Tank)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]