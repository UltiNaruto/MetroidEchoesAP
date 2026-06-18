"""A room characterized by revolving platforms located above a small pool containing a Blogg enemy.
    The room's two doors normally lead to Transport to Sanctuary on the north side and Training Hall on the south side.
    Caution: A player may get stuck here if they fall into the water and lack any movement upgrades."""

from ... import can_lay_bomb, can_use_screw_attack, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class FortressTransportAccess_UpperLedge(MetroidPrime2Region):
    """The taller ledge containing the door that leads to the Torvus-Sanctuary elevator."""
    name="Fortress Transport Access"
    desc = "Upper Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transport to Sanctuary Fortress",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Under Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Lower Ledge)",
            rule=lambda state, player: True
        )
    ]


class FortressTransportAccess_LowerLedge(MetroidPrime2Region):
    """The shorter ledge in the room. Has a yellow door that leads back to Training Chamber."""
    name="Fortress Transport Access"
    desc="Lower Ledge"
    exits_=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (North Door Ledge)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Under Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Upper Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(
                    state,
                    player,
                    "Torvus Bog - Fortress Transport Access | NSJ Jump Between Platforms"),
                can_use_screw_attack(state, player),
                condition_and([
                    can_use_screw_attack(state, player, is_nsj=True, z_axis=True),
                    has_trick_enabled(
                        state,
                        player,
                        "Torvus Bog - Fortress Transport Access | NSJ SA to Platforms")
                ])
            ])
        ),
    ]


class FortressTransportAccess_UnderWater(MetroidPrime2Region):
    """The central pool of water, including the steps that lead to the Lower Ledge.
    Contains a Blogg or Dark Blogg enemy.
    Can be difficult to leave without upgrades."""
    name="Fortress Transport Access"
    desc = "Under Water"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Lower Ledge)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has('Space Jump Boots', player),
                state.has('Gravity Boost', player),
                can_use_screw_attack(state, player),
                condition_and([
                    has_trick_enabled(
                        state,
                        player,
                        "Torvus Bog - Fortress Transport Access | NSJ SA to Platforms"
                    ),
                    can_use_screw_attack(state, player, is_nsj=True)
                ])
            ])
        )
    ]
