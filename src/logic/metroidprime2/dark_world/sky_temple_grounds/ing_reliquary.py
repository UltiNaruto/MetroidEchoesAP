from BaseClasses import MultiWorld

from ... import (
    can_use_annihilator_beam,
    can_use_dark_beam,
    can_use_light_beam,
    can_use_power_beam,
    has_light_suit,
    has_missile_count,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class IngReliquary(MetroidPrime2Region):
    name = "Ing Reliquary"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Reliquary (Ing Cache)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                # requires dark visor to be able to shoot the ing cache
                # and space jump boots to reach the item
                state.has_all({
                    "Dark Visor",
                    "Space Jump Boots",
                }, player),
                # used to shoot at the ing cache
                condition_or([
                    can_use_power_beam(state, player),
                    can_use_dark_beam(state, player),
                    can_use_light_beam(state, player),
                    can_use_annihilator_beam(state, player),
                    has_missile_count(state, player, 5),
                ]),
                # TODO: add Dark Suit logic
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Grounds (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: has_light_suit(state, player),
        ),
    ]


class IngReliquary_IngCache(MetroidPrime2Region):
    name = "Ing Reliquary"
    desc = "Ing Cache"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Reliquary",
            door=DoorCover.Opened,
            rule=lambda state, player: has_light_suit(state, player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Sky Temple Key 7)",
            can_access=lambda state, player: True,
        )
