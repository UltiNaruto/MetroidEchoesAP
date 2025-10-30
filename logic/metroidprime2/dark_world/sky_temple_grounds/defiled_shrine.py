from BaseClasses import MultiWorld

from ... import (
    can_activate_safe_zone,
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
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class DefiledShrine(MetroidPrime2Region):
    name = "Defiled Shrine"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Defiled Shrine (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Shrine Access (Safe Zone)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]


class DefiledShrine_IngCache(MetroidPrime2Region):
    name = "Defiled Shrine"
    desc = "Ing Cache"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Defiled Shrine (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Sky Temple Key 8)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class DefiledShrine_SafeZone(MetroidPrime2Region):
    name = "Defiled Shrine"
    desc = "Safe Zone"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Defiled Shrine",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Sky Temple Grounds - Defiled Shrine | DBJ to Top"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Defiled Shrine (Ing Cache)",
            door=DoorCover.SuperMissile,
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
                condition_or([
                    condition_and([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            state.count("Energy Tank") >= 1,
                            has_dark_suit(state, player),
                        ]),
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]