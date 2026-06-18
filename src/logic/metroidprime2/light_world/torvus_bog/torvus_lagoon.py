"""The room containing the entry cutscene for Torvus. This room is largely underwater, and contains many doors. The above-water
doors (that don't lead to Save Station A) are unreachable until a panel is scanned."""

from BaseClasses import MultiWorld, ItemClassification
from ... import has_trick_enabled, can_use_screw_attack
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TorvusLagoon_Beach(MetroidPrime2Region):
    """The strip of land leading into the water."""
    name = "Torvus Lagoon"
    desc = "Beach"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Save Room Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has("Screw Attack", player),
                has_trick_enabled(state, player, "Torvus Bog - Torvus Lagoon | NSJ to Save Room Ledge")
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Bridge)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Torvus Lagoon | Gates Lowered", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    state.has("Screw Attack", player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Lagoon | NSJ to Bridge")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Underwater)",
            door=DoorCover.Dark,
            rule=lambda state, player: state.has("Dark Beam", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Underwater Ledge)",
            rule=lambda state, player: condition_or([
                state.has('Gravity Boost', player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Lagoon | Air Underwater"),
                    can_use_screw_attack(state, player)
                ])
            ])
        )
    ]


class TorvusLagoon_SaveRoomLedge(MetroidPrime2Region):
    """The ledge leading to Save Station A. Contains a door with a Missile Cover."""
    name = "Torvus Lagoon"
    desc = "Save Room Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Save Station A",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Lagoon - Bridge",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Torvus Lagoon | Gates Lowered", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    can_use_screw_attack(state, player, is_nsj=True)
                ])
            ])
        )
    ]


class TorvusLagoon_UnderwaterLedge(MetroidPrime2Region):
    """The pickup ledge underwater. Requires Gravity Boost or tricks to reach."""
    name= "Torvus Lagoon"
    desc= "Underwater Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Beach",
            rule = lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )


class TorvusLagoon_Bridge(MetroidPrime2Region):
    """Doesn't exist until the gates are lowered. This section is the walkway connecting the Portal Chamber and Ruined Alcove entrances."""
    name = "Torvus Lagoon"
    desc = "Bridge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Portal Chamber Ledge)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Lagoon | Bridge Lowered", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Ruined Alcove Ledge)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Lagoon | Bridge Lowered", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            rule=lambda state, player: True
        )
    ]


class TorvusLagoon_PortalChamberLedge(MetroidPrime2Region):
    """Ledge leading to Portal Chamber. Has the scan panel that opens up the walkway to the Ruined Alcove entrance."""
    name = "Torvus Lagoon"
    desc = "Portal Chamber Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Torvus Lagoon Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Bridge)",
            rule=lambda state, player: state.has("Scan Visor", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Torvus Bog - Torvus Lagoon | Gates Lowered",
            can_access=lambda state, player: state.has("Scan Visor", player),
            locked_item= MetroidPrime2Item(
                name="Torvus Bog - Torvus Lagoon | Gates Lowered",
                classification=ItemClassification.progression,
                code=None,
                player=player
            )
        )


class TorvusLagoon_RuinedAlcoveLedge(MetroidPrime2Region):
    """Has a door leading to Ruined Alcove."""
    name = "Torvus Lagoon"
    desc = "Ruined Alcove Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Bridge)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Lagoon | Gates Lowered", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Ruined Alcove",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        )
    ]
