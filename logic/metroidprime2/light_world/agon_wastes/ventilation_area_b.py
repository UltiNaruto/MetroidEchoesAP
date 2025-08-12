from ... import (
    has_trick_enabled,
    can_lay_bomb,
    has_missile_count,
    can_use_charged_power_beam,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_charged_annihilator_beam,
    can_use_screw_attack,
    has_oob_kit,
)
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class VentilationAreaB_BioenergyProductionSide(MetroidPrime2Region):
    name = "Ventilation Area B"
    desc = "Bioenergy Production Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Bioenergy Production (Ventilation Area B Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area B (Save Station C Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Ventilation Area B | Disable Lasers from Out of Bounds"),
                    state.has("Space Jump Boots", player),
                    condition_or([
                        can_use_charged_power_beam(state, player),
                        can_use_charged_dark_beam(state, player),
                        can_use_charged_light_beam(state, player),
                        can_use_charged_annihilator_beam(state, player),
                        has_missile_count(state, player, 2),
                    ]),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Ventilation Area B | Out of Bounds to Save Station C Side"),
                    has_oob_kit(state, player),
                ])
            ])
        )
    ]

class VentilationAreaB_SaveStationCSide(MetroidPrime2Region):
    name = "Ventilation Area B"
    desc = "Save Station C Side",
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area B (Bioenergy Production Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_bomb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station C",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        )
    ]