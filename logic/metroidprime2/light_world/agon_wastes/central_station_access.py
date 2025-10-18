from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_screw_attack,
    can_use_boost_ball,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class CentralStationAccess_MiningStationASide(MetroidPrime2Region):
    name = "Central Station Access"
    desc = "Mining Station A Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Central Station Access Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Central Station Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class CentralStationAccess_CentralMiningStationSide(MetroidPrime2Region):
    name = "Central Station Access"
    desc = "Central Mining Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station A (Central Station Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Central Station Access | DBJ to Mining Station A Ledge"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Central Station Access | SA on Z-Axis to Mining Station Ledge"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Central Station Access | Wall Boost to Mining Station A Ledge"),
                    can_use_boost_ball(state, player),
                ])            
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Mining Station (Central Station Access Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        )
    ]