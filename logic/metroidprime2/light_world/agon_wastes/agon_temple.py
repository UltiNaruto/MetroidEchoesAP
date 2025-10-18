from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    has_missile_count,
    can_use_power_beam,
    can_use_dark_beam,
    can_lay_bomb,
    can_lay_pb,
    can_lay_bomb_or_pb,
    can_use_boost_ball,
    can_use_screw_attack
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class AgonTemple_TempleAccessSide(MetroidPrime2Exit):
    name = "Agon Temple"
    desc = "Temple Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Controller Access Side)",
            door=DoorCover.Opened,
            # TODO: add logic for various bombless tricks
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Agon Temple Side)",
            door=DoorCover.Light,
            rule=lambda state, player: True, 
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Temple Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class AgonTemple_ControllerAccessSide(MetroidPrime2Exit):
    name = "Agon Temple"
    desc = "Controller Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Temple Access Side)",
            door=DoorCover.Opened,
            # TODO: add logic for various bombless tricks
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mine Shaft (Top)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Controller Access (Agon Temple Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]

class AgonTemple_Center(MetroidPrime2Region):
    name = "Agon Temple"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Temple Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb_or_pb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Break Glass to Temple Access with SA"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Break Glass to Temple Access with Boost Ball"),
                    can_use_boost_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Slope Jump over Glass to Temple Access"),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Break Glass to Temple Access with SA on Z-Axis"),
                    can_use_screw_attack(state, player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Controller Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb_or_pb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Break Glass to Controller Access with SA"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Break Glass to Controller Access with Boost Ball"),
                    can_use_boost_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Slope Jump over Glass to Controller Access"),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Break Glass to Controller Access with SA on Z-Axis"),
                    can_use_screw_attack(state, player),
                ]),
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Morph Ball Bomb)",
                can_access=lambda state, player: state.has("Agon Wastes - Agon Temple | Bomb Guardian Dead"),
                parent=self,
            ),
            MetroidPrime2Location(
                name="Bomb Guardian Dead",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Agon Temple | Bomb Guardian Dead",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_or([
                    can_use_power_beam(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Bomb Guardian with Missiles"),
                        has_missile_count(state, player, 15),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Bomb Guardian with PBs"),
                        can_lay_pb(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Bomb Guardian with Dark Beam"),
                        can_use_dark_beam(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Agon Temple | Bomb Guardian with SA"),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
                parent=self,
            ),
        ]