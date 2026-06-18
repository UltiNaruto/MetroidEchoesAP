"""Has a cage with an item on top. You're expected to come back here once you can use Grapple Beam in vanilla."""

from BaseClasses import MultiWorld, ItemClassification
from ... import can_use_grapple_beam, can_use_screw_attack, can_use_dark_beam
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or


class PathOfRoots_AboveCage(MetroidPrime2Region):
    """The small area above the cage. You can grab a pickup here."""
    name="Path of Roots"
    desc="Above Cage"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Middle)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Lagoon Side)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Great Bridge Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )


class PathOfRoots_GreatBridgeLedge(MetroidPrime2Region):
    """A ledge containing a blue door that leads to Great Bridge. Also has a lore projector.
    Entry: The Ing Attack (GC) / Dark Aether (Trilogy)"""
    name="Path of Roots"
    desc="Great Bridge Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Beach)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Above Cage)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Middle)",
            rule=lambda state, player: True
        )
    ]


class PathOfRoots_LagoonSide(MetroidPrime2Region):
    """Contains a dark door that connects to Torvus Lagoon."""
    name="Path of Roots"
    desc="Lagoon Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            door=DoorCover.Dark,
            rule=lambda state, player: can_use_dark_beam(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Middle)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]


class PathOfRoots_Middle(MetroidPrime2Region):
    """Contains the watery area below the Great Bridge Ledge. Also contains the under-side of the cage."""
    name="Path of Roots"
    desc="Middle"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Lagoon Side)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Great Bridge Ledge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        )
    ]
