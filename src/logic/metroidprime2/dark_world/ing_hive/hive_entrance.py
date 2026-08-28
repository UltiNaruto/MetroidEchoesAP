from BaseClasses import MultiWorld

from ... import (
    can_use_power_beam,
    can_use_dark_beam,
    can_use_light_beam,
    can_use_annihilator_beam,
    can_lay_bomb,
    can_use_screw_attack,
    has_missile_count,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveEntrance(MetroidPrime2Region):
    name = "Hive Entrance"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Entrance (Ing Cache)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has_all({
                    "Dark Visor",
                    "Space Jump Boots",
                }, player),
                condition_or([
                    can_use_annihilator_beam(state, player),
                    can_use_dark_beam(state, player),
                    can_use_light_beam(state, player),
                    can_use_power_beam(state, player),
                    has_missile_count(state, player, 5)
                ]),
                can_use_screw_attack(state, player),
                condition_or([
                    has_light_suit(state, player),
                    has_trick_enabled(state, player, "Ing Hive - Hive Entrance | Light Suit Skip SA Only to Ing Cache"),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Entrance | Light Suit Skip with BJ to Ing Cache"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Entrance Defense Hall",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]

class HiveEntranceIngCache(MetroidPrime2Region):
    name = "Hive Entrance"
    desc = "Ing Cache"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Entrance",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
    ]
    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Sky Temple Key 5)",
            can_access=lambda state, player: True,
        )
