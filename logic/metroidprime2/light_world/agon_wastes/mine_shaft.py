from BaseClasses import MultiWorld
from ... import (
    has_trick_enabled,
    can_use_boost_ball,
    can_lay_bomb
)
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class MineShaft_Top(MetroidPrime2Region):
    name = "Mine Shaft"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mine Shaft (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Mine Shaft Side)",
            door=DoorCover.Seeker,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mine Shaft (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Mine Shaft Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Energy Tank)",
                can_access=lambda state, player: can_lay_bomb(state, player),
                parent=self
            ),
        ]

class MineShaft_Bottom(MetroidPrime2Region):
    name = "Mine Shaft"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mine Shaft (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mine Shaft | Wall Boost up to Mine Shaft Top"),
                    can_use_boost_ball(state, player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Mine Shaft Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Mine Shaft Side)",
            door=DoorCover.Seeker,
            rule=lambda state, player: True,
        )
    ]