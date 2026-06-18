"""A room characterized by its split nature. Morph Ball tunnels provide connections between all but the pickup ledge subregion."""

from BaseClasses import MultiWorld, ItemClassification
from ... import (
    can_boost_jump,
    can_lay_bomb,
    can_use_screw_attack,
    can_use_grapple_beam,
    has_trick_enabled
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


class AbandonedWorksite_ForgottenBridgeEntrance(MetroidPrime2Region):
    """The part of the room leading to/from Forgotten Bridge. Has a Super Missile door and a Morph Ball tunnel protected by a Sporb."""
    name = "Abandoned Worksite"
    desc="Forgotten Bridge Entrance"
    exits=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Pickup Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Forgotten Bridge Side)",
            rule=lambda state, player: condition_or([
                # TODO: replace with can_ball_jump
                can_lay_bomb(state, player),
                can_use_screw_attack(state, player)
            ])
        )
    ]


class AbandonedWorksite_GreatBridgeEntrance(MetroidPrime2Region):
    """The part of the room leading to/from Great Bridge. Has a piston to lead Samus to a Morph Ball tunnel.
    The grapple point above can be accessed from down here."""
    name = "Abandoned Worksite"
    desc="Great Bridge Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Scan Panel Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: condition_or([
                # TODO: replace with can_ball_jump
                can_lay_bomb(state, player), # either navigate the morph puzzle
                can_use_grapple_beam(state, player) # or grapple from the floor to the ledge next to the morph tunnel
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Pickup Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Grapple Beam", player), # you can just grapple up there from the floor
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | BSJ to Pickup Ledge"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player)
                ]),
            ])
        )
    ]


class AbandonedWorksite_LedgeForgottenBridgeSide(MetroidPrime2Region):
    """The ledge on the Forgotten Bridge side of the room, joined to the Great Bridge side of the room by a Morph Ball tunnel."""
    name = "Abandoned Worksite"
    desc="Ledge Forgotten Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Forgotten Bridge Entrance)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player),
                can_use_screw_attack(state, player, is_nsj=True)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]


class AbandonedWorksite_LedgeGreatBridgeSide(MetroidPrime2Region):
    """The ledge on the Great Bridge side of the room, joined to the Forgotten Bridge side of the room by a Morph Ball tunnel."""
    name = "Abandoned Worksite"
    desc="Ledge Great Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Pickup Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | NSJ BSJ to Pickup Ledge"),
                    can_lay_bomb(state, player) # todo: swap to can_ball_jump
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | NSJ SA to Pickup Ledge"),
                    can_use_screw_attack(state, player, is_nsj=True)
                ]),
                can_boost_jump(state, player, "Torvus Bog - Abandoned Worksite | Boost Jump to Pickup Ledge"),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | Roll Jump to Pickup Ledge"),
                    state.has_all(["Morph Ball", "Space Jump Boots"], player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Forgotten Bridge Side)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Great Bridge Entrance)",
            rule=lambda state, player: True
        )
    ]


class AbandonedWorksite_PickupLedge(MetroidPrime2Region):
    """A ledge containing a pickup. Sits above the Great Bridge entrance and across from the ledge on the Great Bridge side."""
    name = "Abandoned Worksite"
    desc="Pickup Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Great Bridge Entrance)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )
