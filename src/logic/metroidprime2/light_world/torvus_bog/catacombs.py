"""A room characterized by its underwater bomb slot and dark portal wrapped by a gate."""

from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_screw_attack,
    can_activate_bomb_slot,
    can_reach_underwater_bomb_slot,
    catacombs_can_clip_through_gate
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Utils import condition_or, condition_and
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


# tricks:
#         "Torvus Bog - Catacombs | Activate Bomb Slot without Bombs",
#         "Torvus Bog - Catacombs | Clip Through Gate",
#         "Torvus Bog - Catacombs | Exit Water NSJ",
#         "Torvus Bog - Catacombs | Underwater Dash to Bomb Slot",


class Catacombs_TransitTunnelEastEntrance(MetroidPrime2Region):
    """An isolated ledge with a blue door that connects to Transit Tunnel East."""
    name="Catacombs"
    desc="Transit Tunnel East Entrance"
    exits_=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East (Catacombs Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Portal Ledge)",
            rule = lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            rule= lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Under Water)",
            rule= lambda state, player: True
        )
    ]


class Catacombs_TransitTunnelSouthEntrance(MetroidPrime2Region):
    """A connected ledge with a zebra-stripe door that connects to Transit Tunnel South."""
    name="Catacombs"
    desc="Transit Tunnel South Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South (Catacombs Side)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            rule=lambda state, player: True
        )
    ]


class Catacombs_KeybearerLedge(MetroidPrime2Region):
    """A ledge sandwiched between two door alcoves and the large pool in the center of the room.
    The Keybearer Luminoth body is its most notable feature. Entry: G-Sch's Testament
    Contains a black door leading to Catacombs Access.
    Contains Grenchler enemies (later visits)."""
    name="Catacombs"
    desc="Keybearer Ledge"
    exits_=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Portal Ledge)",
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has('Torvus Bog - Catacombs | Bomb Slot Activated', player),
                    state.has('Space Jump Boots', player),
                ]),
                catacombs_can_clip_through_gate(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Catacombs Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Under Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Entrance)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel South Entrance)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has('Space Jump Boots', player)
            ])
        )
    ]


class Catacombs_UnderWater(MetroidPrime2Region):
    """The pool in the center of the room.
    Contains Blogg enemies (first visit) and a Bomb Slot."""
    name="Catacombs"
    desc="Under Water"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Torvus Bog - Catacombs | Exit Water NSJ"),
                can_lay_bomb(state, player) # requires DBJ, but this seems reasonable to expect someone to do
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Entrance)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Torvus Bog - Catacombs | Exit Water NSJ"),
                can_lay_bomb(state, player)  # requires DBJ, but this seems reasonable to expect someone to do
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Bomb Slot Activated",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Catacombs | Bomb Slot Activated",
                classification=ItemClassification.progression,
                code=None,
                player=player
            ),
            can_access=lambda state, player: condition_and([
                can_reach_underwater_bomb_slot(state, player, "Torvus Bog - Catacombs | Underwater Dash to Bomb Slot"),
                can_activate_bomb_slot(state, player, "Torvus Bog - Catacombs | Activate Bomb Slot without Bombs")
            ])
        )

class Catacombs_PortalLedge(MetroidPrime2Region):
    """An isolated ledge suspended above the central pool.
    Until the Bomb Slot is used, it is barred from entry by a wrap-around gate.
    Contains a Lore Projector. Entry: The New Terror (GC)/Recovering Energy (Wii)"""
    name="Catacombs"
    desc="Portal Ledge"
    exits_=[
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Dungeon (Portal Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Under Water)",
            rule=lambda state, player: condition_or([
                state.has('Torvus Bog - Catacombs | Bomb Slot Activated', player),
                catacombs_can_clip_through_gate(state, player, True)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Entrance",
            rule=lambda state, player: condition_and([
                can_use_screw_attack(state, player),
                state.has('Torvus Bog - Catacombs | Bomb Slot Activated', player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel South Entrance",
            rule=lambda state, player: condition_and([
                can_use_screw_attack(state, player),
                state.has('Torvus Bog - Catacombs | Bomb Slot Activated', player)
            ])
        )
    ]
