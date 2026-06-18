"""Room connecting Torvus Temple and Torvus Energy Controller. It's the same as the rooms in Agon and Sanctuary.

Rotates by activating a bomb slot in the middle of the room. The bomb slot is not permanently activated."""

from ... import can_activate_bomb_slot
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class ControllerAccess(MetroidPrime2Region):
    name="Controller Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Upper)",
            door=DoorCover.Any,
            rule=lambda state, player: can_activate_bomb_slot(state, player, "Torvus Bog - Controller Access | Activate Bomb Slot without Bombs")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Energy Controller",
            door=DoorCover.Any,
            rule=lambda state, player: can_activate_bomb_slot(state, player, "Torvus Bog - Controller Access | Activate Bomb Slot without Bombs")
        )
    ]
