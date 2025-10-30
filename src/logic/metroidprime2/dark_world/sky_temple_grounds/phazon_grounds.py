from BaseClasses import MultiWorld

from ... import can_use_screw_attack, has_dark_suit, has_light_suit, has_trick_enabled
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class PhazonGrounds(MetroidPrime2Region):
    name = "Phazon Grounds"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Pit (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                # cross the gap
                condition_or([
                    condition_and([
                        condition_or([
                            has_trick_enabled(state, player, "Sky Temple Grounds - Phazon Grounds | Visorless Invisible Platforms"),
                            state.has("Dark Visor", player),
                        ]),
                        state.has("Space Jump Boots", player),
                    ]),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Pit (Phazon Grounds Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Reliquary Access (Phazon Grounds Side)",
            door=DoorCover.Seeker,
            rule=lambda state, player: has_light_suit(state, player),
        ),
    ]


class PhazonGrounds_Item(MetroidPrime2Region):
    name = "Phazon Grounds"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Grounds",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                # cross the gap
                condition_or([
                    condition_and([
                        condition_or([
                            has_trick_enabled(state, player, "Sky Temple Grounds - Phazon Grounds | Visorless Invisible Platforms"),
                            state.has("Dark Visor", player),
                        ]),
                        state.has("Space Jump Boots", player),
                    ]),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]
