from BaseClasses import MultiWorld

from ... import has_dark_suit, has_light_suit, has_missile_count
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


class WarRitualGrounds_Center(MetroidPrime2Region):
    name = "War Ritual Grounds"
    desc = "Center"
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
                state.has_all({
                    "Dark Visor",
                    "Seeker Launcher"
                }, player),
                # consider more missile to start the charging process of Seeker Launcher
                has_missile_count(state, player, 6),
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

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self,
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
            destination="Sky Temple Grounds - War Ritual Grounds (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]
