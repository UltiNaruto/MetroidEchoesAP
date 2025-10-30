from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_light_portal,
    can_lay_bomb,
    can_use_annihilator_beam,
    can_use_dark_beam,
    can_use_light_beam,
    can_use_power_beam,
    has_dark_suit,
    has_light_suit,
    has_missile_count,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class AbandonedBase(MetroidPrime2Region):
    name = "Abandoned Base"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Abandoned Base (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, ""),
                state.has("Space Jump Boots", player),
                condition_or([
                    # consider the amount of energy tank to return to safety
                    # assuming we get the item, starting from Base Access door
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Abandoned Base (Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Base Access (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class AbandonedBase_Platform(MetroidPrime2Region):
    name = "Abandoned Base"
    desc = "Platform"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="Sky Temple Grounds - Abandoned Base",
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="Sky Temple Grounds - Abandoned Base (Portal)",
            rule=lambda state, player: condition_and([
                state.has("Sky Temple Grounds - Abandoned Base | Bomb Puzzle Solved", player),
                condition_or([
                    can_use_power_beam(state, player),
                    can_use_dark_beam(state, player),
                    can_use_light_beam(state, player),
                    can_use_annihilator_beam(state, player),
                    has_missile_count(state, player, 5),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Bomb Puzzle Solved",
                locked_item=MetroidPrime2Item(
                    name="Sky Temple Grounds - Abandoned Base | Bomb Puzzle Solved",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: can_lay_bomb(state, player),
                parent=self,
            ),
        ]


class AbandonedBase_Portal(MetroidPrime2Region):
    name = "Abandoned Base"
    desc = "Portal"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="P|Temple Grounds - Path of Eyes (Hall of Eyes Side)",
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="Sky Temple Grounds - Abandoned Base",
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]