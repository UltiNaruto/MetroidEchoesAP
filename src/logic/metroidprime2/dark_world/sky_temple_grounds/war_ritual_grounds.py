from BaseClasses import MultiWorld

from ... import can_use_seeker_launcher, has_dark_suit, has_light_suit
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class WarRitualGrounds_BaseAccessSide(MetroidPrime2Region):
    name = "War Ritual Grounds"
    desc = "Base Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Base Access (Bottom)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: state.can_reach("Sky Temple Grounds - Base Access (Top)", player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 2,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]


class WarRitualGrounds_Item(MetroidPrime2Region):
    name = "War Ritual Grounds"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
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


class WarRitualGrounds_SafeZone(MetroidPrime2Region):
    name = "War Ritual Grounds"
    desc = "Safe Zone"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds (Base Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 2,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                state.has("Dark Visor", player),
                can_use_seeker_launcher(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds (Shrine Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]


class WarRitualGrounds_ShrineAccessSide(MetroidPrime2Region):
    name = "War Ritual Grounds"
    desc = "Shrine Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Shrine Access (War Ritual Grounds Side)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]
