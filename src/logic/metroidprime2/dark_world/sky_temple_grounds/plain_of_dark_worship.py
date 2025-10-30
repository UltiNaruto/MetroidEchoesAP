from BaseClasses import MultiWorld

from ... import can_activate_light_portal, can_use_screw_attack, has_dark_suit, has_light_suit, has_trick_enabled
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class PlainOfDarkWorship(MetroidPrime2Region):
    name = "Plain of Dark Worship"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Lake Access",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                # assuming we get the item, starting from portal
                state.count("Energy Tank", player) >= 5,
                condition_and([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Temple Grounds - Temple Assembly Site (Behind Light Beam Block)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Plains of Dark Worship (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Sky Temple Grounds - Plains of Dark Worship | Suitless SA to Item"),
                    # consider both going to and coming back from
                    state.count("Energy Tank", player) >= 6,
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
    ]


class PlainOfDarkWorship_Item(MetroidPrime2Region):
    name = "Plain of Dark Worship"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Plain of Dark Worship",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Sky Temple Grounds - Plains of Dark Worship | Suitless SA to Item"),
                    # consider both going to and coming back from
                    state.count("Energy Tank", player) >= 6,
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