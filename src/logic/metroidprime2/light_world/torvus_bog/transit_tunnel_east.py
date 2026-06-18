"""Morph Ball puzzle room connecting Training Chamber and Catacombs.
Air jets in this room can lift the Morph Ball if the player has neither Bombs nor Gravity Boost."""

from BaseClasses import MultiWorld, ItemClassification
from ... import can_lay_bomb
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and


class TransitTunnelEast_CatacombsSide(MetroidPrime2Region):
    name="Transit Tunnel East"
    desc="Catacombs Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East (Training Chamber Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
            #todo: replace with can_ball_jump once that's a thing
        )
    ]

class TransitTunnelEast_TrainingChamberSide(MetroidPrime2Region):
    """Has the Bomb Slot as well as the pickup."""
    name="Transit Tunnel East"
    desc="Training Chamber Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (East Caged Area)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East (Catacombs Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
            #todo: replace with can_ball_jump once that's a thing
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Energy Tank)",
            can_access=lambda state, player: condition_and([
                can_lay_bomb(state, player),
                state.has('Gravity Boost', player)
            ])
        )
