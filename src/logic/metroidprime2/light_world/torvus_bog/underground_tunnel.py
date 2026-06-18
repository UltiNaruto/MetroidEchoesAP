"""
Connects Torvus Temple and Torvus Grove. There is an item in the floor on the Torvus Temple side.
The room is notable for having a short morph ball tunnel "hidden" by a small waterfall.
Has:
- Grenchler (1st pass) / Seedburster swarm (later passes) enemies
- 2 Sporb enemies
- An Emerald Lore Projector. Entry: Our War Begins (GC) / The Ing Attack (Wii)
- A pickup (Missile Expansion)
"""

from BaseClasses import MultiWorld, ItemClassification
from ... import can_lay_bomb, can_use_boost_ball, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class UndergroundTunnel_Tunnel(MetroidPrime2Region):
    """Be sure to check under the grating! The wooden tunnel makes for a striking environment."""
    name="Underground Tunnel"
    desc="Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Tunnel (After Falls)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: state.has("Morph Ball", player)
        )


class UndergroundTunnel_AfterFalls(MetroidPrime2Region):
    """Two Sporbs guard the tunnel here."""
    name="Underground Tunnel"
    desc="After Falls"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Tunnel (Tunnel)",
            rule=lambda state, player: condition_or([
                # TODO: change to can_ball_jump later
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Underground Tunnel | Instant Morph to enter Tunnel"),
                    state.has("Morph Ball", player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Underground Tunnel | Wall Boost to enter Tunnel"),
                    can_use_boost_ball(state, player)
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
