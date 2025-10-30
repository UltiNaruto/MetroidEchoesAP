from BaseClasses import MultiWorld

from ... import (
    can_use_annihilator_beam,
    can_use_dark_beam,
    can_use_light_beam,
    can_use_power_beam,
    has_dark_suit,
    has_light_suit,
    has_missile_count, can_activate_safe_zone,
)
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class AccursedLake(MetroidPrime2Region):
    name = "Accursed Lake"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Accursed Lake (Ing Cache)",
            door=DoorCover.Opened,
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
                # consider the amount of energy tank to return to safety
                # assuming we get the item, starting from Plain of Dark Worship door
                condition_or([
                    condition_and([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            state.count("Energy Tank", player) >= 5,
                            condition_and([
                                state.count("Energy Tank", player) >= 1,
                                has_dark_suit(state, player),
                            ]),
                        ]),
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Lake Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                # assuming we go to Plain of Dark Worship portal
                state.count("Energy Tank", player) >= 3,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]


class AccursedLake_IngCache(MetroidPrime2Region):
    name = "Accursed Lake"
    desc = "Ing Cache"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Accursed Lake",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                # assuming we get the item, starting from Plain of Dark Worship door
                state.count("Energy Tank", player) >= 6,
                condition_and([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                ]),
                has_light_suit(state, player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Sky Temple Key 9)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]
