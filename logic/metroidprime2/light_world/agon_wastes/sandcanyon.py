from BaseClasses import MultiWorld

from ... import (
    has_trick_enabled,
    can_use_screw_attack,
    can_lay_pb,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and

class Sandcanyon_AgonTempleSide(MetroidPrime2Region):
    name = "Sandcanyon"
    desc = "Agon Temple Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Ventilation Area A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Sandcanyon Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Sandcanyon Side)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
    ]

class Sandcanyon_VentilationAreaASide(MetroidPrime2Region):
    name = "Sandcanyon"
    desc = "Ventilation Area A Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Agon Temple Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Temple (Sandcanyon Side)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Ventilation Area A (Sandcanyon Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class Sandcanyon_Platform(MetroidPrime2Region):
    name = "Sandcanyon"
    desc = "Platform"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Agon Temple Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon (Ventilatin Area A Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Agon Wastes - Sandcanyon | Terminal Fall Abuse"),
                can_use_screw_attack(state, player),
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Power Bomb Expansion)",
                can_access=lambda state, player: can_lay_pb(state, player),
                parent=self,
            ),
        ]