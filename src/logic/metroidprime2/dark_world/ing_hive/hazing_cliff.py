from BaseClasses import MultiWorld

from ... import (
    can_use_charged_annihilator_beam,
    can_use_charged_light_beam,
    has_dark_suit,
    has_light_suit,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HazingCliff_Door(MetroidPrime2Region):
    name = "Hazing Cliff"
    desc = "Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Culling Chamber (Near Portal)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hazing Cliff (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_use_charged_annihilator_beam(state, player),
                    can_use_charged_light_beam(state, player),
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class HazingCliff_Item(MetroidPrime2Region):
    name = "Hazing Cliff"
    desc = "Item"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hazing Cliff (Door)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_use_charged_annihilator_beam(state, player),
                    can_use_charged_light_beam(state, player),
                ]),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ])
        )
    ]
    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True,
        )
