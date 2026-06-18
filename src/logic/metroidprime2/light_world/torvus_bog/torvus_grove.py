"""A combat room leading to Meditation Vista. Contains a pickup that can be gotten after power-bombing the roots of the
large central tree."""

from BaseClasses import MultiWorld, ItemClassification
from ... import (
    can_lay_bomb,
    can_lay_pb,
    can_use_boost_ball,
    can_use_screw_attack,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


class TorvusGrove_Center(MetroidPrime2Region):
    """Contains the large tree in the center, a half-pipe, two doors, and some Pirate Commando enemies triggered via cutscene."""
    name = "Torvus Grove"
    desc="Center" # pretty much the entire bottom
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Connector Ledge)",
            rule=lambda state, player: condition_or([
                can_use_boost_ball(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Grove | Climb Roots to reach Connected Ledge"),
                    state.has("Space Jump Boots", player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Behind Breakable Wall)",
            rule=lambda state, player: can_lay_pb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Meditation Vista (Entrance)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Grove | Pirates Dead", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Tunnel (After Falls)",
            door=DoorCover.Light,
            rule=lambda state, player: state.has("Torvus Bog - Torvus Grove | Pirates Dead", player)
        )
    ]


class TorvusGrove_BehindBreakableWall(MetroidPrime2Region):
    """Contains a pickup."""
    name = "Torvus Grove"
    desc="Behind Breakable Wall" # behind the wall broken by the felled tree
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )


class TorvusGrove_ConnectorLedge(MetroidPrime2Region):
    """Contains the first walkway above the half-pipe."""
    name = "Torvus Grove"
    desc="Connector Ledge" # at the top of the half-pipe
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Upper Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Curved Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has("Screw Attack", player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Grove | Scan Dash to reach Curved Ledge"),
                    state.has("Scan Visor", player),
                ]),
                has_trick_enabled(state, player, "Torvus Bog - Torvus Grove | STE to reach Curved Ledge")
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            rule=lambda state, player: True # You can always fall down
        )
    ]


class TorvusGrove_CurvedLedge(MetroidPrime2Region):
    """The second high ledge."""
    name = "Torvus Grove"
    desc = "Curved Ledge" # past a small hole after the connector ledge
    exits_=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Isolated Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Grove | Instant Unmorph to reach Isolated Ledge")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            rule=lambda state, player: True  # You can always fall down
        )
    ]

class TorvusGrove_IsolatedLedge(MetroidPrime2Region):
    """The third high ledge."""
    name = "Torvus Grove"
    desc="Isolated Ledge" # the tall one
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            rule=lambda state, player: True  # You can always fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Curved Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Upper Door Ledge)",
            rule=lambda state, player: True
        )
    ]

class TorvusGrove_UpperDoorLedge(MetroidPrime2Region):
    """The fourth high ledge. Contains a dark door that leads to Grove Access."""
    name = "Torvus Grove"
    desc="Upper Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            rule=lambda state, player: True  # You can always fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Isolated Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Grove | Instant Unmorph to reach Isolated Ledge")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Grove Access", # curiously, this door is not locked while the pirates are around,
            # so you don't need to defeat them to get up here at all
            door=DoorCover.Dark,
            rule = lambda state, player: True
        )
    ]
