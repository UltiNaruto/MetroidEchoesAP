from BaseClasses import MultiWorld, ItemClassification
from ... import can_activate_dark_portal, can_lay_bomb, can_use_boost_ball, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


class PortalChamber_Center(MetroidPrime2Region):
    name="Portal Chamber"
    desc="Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Portal Chamber | Center",
            door=DoorCover.Dark,
            rule=lambda state, player: can_activate_dark_portal(state, player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )


class PortalChamber_GreatBridgeSide(MetroidPrime2Region):
    """Contains a Missile Cover door that leads to Great Bridge (North Path)"""
    name = "Portal Chamber"
    desc = "Great Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (North Path)",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Morph Ball Tunnel)",
            rule=lambda state, player: condition_or([
                #todo: change to can_ball_jump
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        )
    ]


class PortalChamber_MorphBallTunnel(MetroidPrime2Region):
    """Connects the two Entrance subregions."""
    name = "Portal Chamber"
    desc = "Morph Ball Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Great Bridge Side)",
            rule=lambda state, player: condition_or([
                # todo: change to can_ball_jump
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Torvus Lagoon Side)",
            rule=lambda state, player: condition_or([
                # todo: change to can_ball_jump
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        )
    ]


class PortalChamber_TorvusLagoonSide(MetroidPrime2Region):
    """Has a blue door that leads to the bridge section of Torvus Lagoon."""
    name="Portal Chamber"
    desc="Torvus Lagoon Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Morph Ball Tunnel)",
            rule=lambda state, player: condition_or([
                # todo: change to can_ball_jump
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Portal Chamber Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
