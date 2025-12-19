from BaseClasses import MultiWorld

from ... import (
    can_lay_bomb,
    can_use_boost_ball,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TransportBAccess(MetroidPrime2Region):
    name = "Transport B Access"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Any,
            destination="Great Temple - Temple Transport B",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Transport B Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Great Temple - Transport B Access | Item with Slope Jump and SJ"),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Great Temple - Transport B Access | Item with Wall Boost"),
                    can_use_boost_ball(state, player),
                ]),
            ]),
        )