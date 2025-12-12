from BaseClasses import MultiWorld

from ... import can_lay_bomb, can_use_boost_ball, has_light_suit, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class FortressTransportAccess_Top(MetroidPrime2Region):
    name = "Fortress Transport Access"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Fortress Transport Access (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Energy Tank)",
            can_access=lambda state, player: True,
        )


class FortressTransportAccess_Bottom(MetroidPrime2Region):
    name = "Fortress Transport Access"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Fortress Transport Access (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Fortress Transport Access | IS to get item"),
                    # expects the player to be able to get Infinite Speed at Temple Grounds - Storage Cavern A
                    state.can_reach(spot="Temple Grounds - Storage Cavern A", player=player),
                    # needed for Infinite Speed to activate it
                    can_use_boost_ball(state, player),
                    # expect the player to be able to open the doors in between Storage Cavern A and Fortress Transport Access
                    can_lay_bomb(state, player),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Behind Translator Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Transport to Sanctuary Fortress",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
