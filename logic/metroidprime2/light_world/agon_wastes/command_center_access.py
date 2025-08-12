from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_lay_bomb_or_pb,
    can_use_boost_ball,
    can_use_screw_attack,
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class CommandCenterAccess_Top(MetroidPrime2Region):
    name = "Command Center Access",
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Top)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Turret Platform)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        )
    ]

class CommandCenterAccess_Bottom(MetroidPrime2Region):
    name = "Command Center Access"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center (Bottom)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Command Center Access (Morph Tunnel)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Command Center Access | Grates/Crates Broken"),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Behind Laser Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Grates/Crates Broken",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Command Center Access | Grates/Crates Broken",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                rule=lambda state, player: condition_or([
                    can_lay_bomb_or_pb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Command Center Access | Break Grates with Boost Ball"),
                        can_use_boost_ball(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Command Center Access | Break Grates with SA"),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
            )
        ]

class CommandCenterAccess_MorphTunnel(MetroidPrime2Region):
        name = "Command Center Access"
        desc = "Morph Tunnel"
        exits_ = [
            MetroidPrime2Exit(
                destination="Agon Wastes - Command Center Access (Bottom)",
                door=DoorCover.Opened,
                rule=lambda state, player: condition_and([
                     state.has("Agon Wastes - Command Center Access | Grates/Crates Broken"),
                     condition_or([
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Command Center Access | DBJ from Under Grates to Command Center Access Bottom"),   
                            can_lay_bomb(state, player),
                        ]),
                        condition_and([
                             has_trick_enabled(state, player, "Agon Wastes - Command Center Access | Wall Boost from Under Grates to Command Center Access Bottom"),
                             can_use_boost_ball(state, player),
                        ]),
                        condition_and([
                             state.has("Agon Wastes - Command Center | Gate Closed"),
                             condition_or([
                                  state.has("Space Jump Boots", player),
                                  has_trick_enabled(state, player, "Agon Wastes - Command Center Access | Standable from Under Grates to Command Center Bottom"),
                             ]),
                        ]),
                     ]),
                ])
            ),
            MetroidPrime2Exit(
                 destination="Agon Wastes - Command Center (Morph Tunnel)",
                 door=DoorCover.MorohBallTunnel,
                 rule=lambda state, player: True,
            ),
        ]