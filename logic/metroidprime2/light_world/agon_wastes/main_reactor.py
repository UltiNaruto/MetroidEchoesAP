from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_lay_bomb_or_pb,
    can_use_power_beam,
    can_use_dark_beam,
    can_use_spider_ball,
    can_use_screw_attack,
    can_use_boost_ball,
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class MainReactor_Portal(MetroidPrime2Region):
    name = "Main Reactor"
    desc = "Portal"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Storage D Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_use_dark_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Main Reactor | Activate Dark Crystal Gate with SA"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal (Main Reactor Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Behind Glass)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class MainReactor_StorageDSide(MetroidPrime2Region):
    name = "Main Reactor"
    desc = "Storage D Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Securtiy Station B Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_use_dark_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Main Reactor | Activate Dark Crystal Gate with SA"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Main Reactor | DS1 Dead"),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Ventilation Area A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Agon Wastes - Main Reactor | 3BSJ to SA Recoil up to Ventilation Area A Side"),
                state.has("Space Jump Boots", player),
                can_lay_bomb(state, player),
                can_use_screw_attack(state, player),
            ]),
        )
    ]

class MainReactor_Center(MetroidPrime2Region):
    name = "Main Reactor"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Storage D Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Main Reactor | DS1 Dead"),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Ventilation Area A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                # TODO: add logic to make sure player can reload room
                state.has("Agon Wastes - Main Reactor | DS1 Dead", player),
                condition_or([
                    can_use_spider_ball(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Main Reactor | 3BSJ to SA Recoil up to Ventilation Area A Side"),
                        state.has("Space Jump Boots", player),
                        can_lay_bomb(state, player),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (On Phazon Container)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Agon Wastes - Main Reactor | BSJ onto Phazon Container"),
                # TODO: add logic to make sure player can reload room
                state.has("Space Jump Boots", player),
                can_lay_bomb(state, player),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Agon Wastes - Main Reactor | DS1 Dead"),
                can_use_spider_ball(state, player),
                condition_or([
                    can_use_boost_ball(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Main Reactor | 2BSJ onto Railing then Jump Around to Item"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
            ]),
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="DS1 Dead",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Main Reactor | DS1 Dead",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
        ] 

class MainReactor_Item(MetroidPrime2Region):
    name = "Main Reactor"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: condition_or([
                    can_lay_bomb_or_pb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Main Reactor | Destroy Glass without Bombs"),
                        condition_or([
                            can_use_boost_ball(state, player),
                            can_use_power_beam(state, player),
                            can_use_screw_attack(state, player),
                        ])
                    ])
                ]),
                parent=self,
            ),
        ]

class MainReactor_OnPhazonContainer(MetroidPrime2Region):
    name = "Main Reactor"
    desc = "On Phazon Container"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Space Jump Boots", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # TODO: Add logic for roll jump or scan dash over to corpse
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Main Reactor | SA in Morph Exit by Item"),
                    can_use_screw_attack(state, player),
                ]),
            ])
        )
    ]