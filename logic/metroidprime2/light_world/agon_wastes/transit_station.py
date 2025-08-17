from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_lay_pb,
    has_pb_count,
    can_use_boost_ball,
    has_oob_kit
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class TransitStation_MiningStationBSide(MetroidPrime2Region):
    name = "Transit Station"
    desc = "Mining Station B Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transit Station (Mining Plaza Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    can_lay_pb(state, player),
                    has_pb_count(state, player, 2),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Transit Station | Break Rocks with Boost Ball"),
                    can_use_boost_ball(state, player),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Transit Station Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class TransitStation_MiningPlazaSide(MetroidPrime2Region):
    name = "Transit Station"
    desc = "Mining Plaza Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transit Station (Mining Station B Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb_or_pb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Transit Station | Break Rocks with Boost Ball"),
                    can_use_boost_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Transit Station | Out of Bounds"),
                    has_oob_kit(state, player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Portal Exit)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]