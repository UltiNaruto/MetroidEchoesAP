"""A short Morph Ball puzzle room that requires Bombs for traversal and Boost to get the item."""

from BaseClasses import MultiWorld, ItemClassification
from ... import can_lay_bomb, can_use_boost_ball
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class PlazaAccess_ForgottenBridgeEntrance(MetroidPrime2Region):
    """The entrance on the Forgotten Bridge side. You are most likely starting here."""
    name = "Plaza Access"
    desc = "Forgotten Bridge Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Morph Ball Tunnel Forgotten Bridge Side)",
            rule=lambda state, player: can_lay_bomb(state, player)
        )
    ]


class PlazaAccess_HalfPipe(MetroidPrime2Region):
    """Entered via tunnel. Ride this half-pipe to the top to get a pickup."""
    name = "Plaza Access"
    desc="Half-Pipe"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: can_use_boost_ball(state, player)
        )


class PlazaAccess_Maze(MetroidPrime2Region):
    """Has a few contraptions that need flipping via bomb slot in order to traverse the room."""
    name = "Plaza Access"
    desc="Maze"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Half-Pipe)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Torvus Plaza Entrance)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Forgotten Bridge Entrance)",
            rule=lambda state, player: can_lay_bomb(state, player)
        ),
    ]


class PlazaAccess_TorvusPlazaEntrance(MetroidPrime2Region):
    """Contains a blue door leading to Torvus Plaza."""
    name = "Plaza Access"
    desc="Torvus Plaza Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Maze)",
            rule=lambda state, player: can_lay_bomb(state, player)
        )
    ]
