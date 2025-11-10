from BaseClasses import MultiWorld

from ... import (
    can_lay_bomb_or_pb,
    can_use_boost_ball,
    can_use_screw_attack,
    can_use_super_missile,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TransportAAccess_ElevatorSide(MetroidPrime2Region):
    name = "Transport A Access"
    desc = "Elevator Side"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Any,
            destination="Great Temple - Temple Transport A",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport A Access (Temple Sanctuary Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]


class TransportAAccess_SaveStation(MetroidPrime2Region):
    name = "Transport A Access"
    desc = "Save Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Great Temple - Transport A Access (Temple Sanctuary Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: condition_or([
                    can_lay_bomb_or_pb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Great Temple - Transport A Access | Break Block with Boost Ball"),
                        can_use_boost_ball(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Great Temple - Transport A Access | Break Block with Screw Attack"),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Great Temple - Transport A Access | Break Block with Super Missile"),
                        can_use_super_missile(state, player),
                    ]),
                ]),
                parent=self,
            ),
        ]


class TransportAAccess_TempleSanctuarySide(MetroidPrime2Region):
    name = "Transport A Access"
    desc = "Temple Sanctuary Side"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Any,
            destination="Great Temple - Temple Sanctuary (Transport A Side)",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport A Access (Elevator Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Transport A Access (Save Station)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]