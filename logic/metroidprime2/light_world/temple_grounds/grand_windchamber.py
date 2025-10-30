from BaseClasses import MultiWorld

from ... import can_activate_dark_portal, can_lay_bomb, can_use_grapple_beam, can_use_screw_attack, has_trick_enabled
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class GrandWindchamber_Cannon(MetroidPrime2Region):
    name = "Grand Windchamber"
    desc = "Cannon"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Grand Windchamber | SA from Cannon to Platform"),
                    can_use_screw_attack(state, player),
                ]),
                state.has_all({
                    "Morph Ball",
                    "Sky Temple Grounds - Ing Windchamber | North Grapple Up",
                    "Sky Temple Grounds - Ing Windchamber | South Grapple Up",
                }, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Gateway Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Sky Temple Grounds - Ing Windchamber | North Grapple Up", player),
                    can_use_grapple_beam(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Tunnel Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Sky Temple Grounds - Ing Windchamber | North Grapple Up", player),
                    can_use_grapple_beam(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
    ]


class GrandWindchamber_Platform(MetroidPrime2Region):
    name = "Grand Windchamber"
    desc = "Platform"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Gateway Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Tunnel Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Space Jump Boots", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Sunburst)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class GrandWindchamber_WindchamberGatewaySide(MetroidPrime2Region):
    name = "Grand Windchamber"
    desc = "Windchamber Gateway Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Sky Temple Grounds - Ing Windchamber (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Cannon)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Sky Temple Grounds - Ing Windchamber | North Grapple Up", player),
                    can_use_grapple_beam(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Tunnel Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Sky Temple Grounds - Ing Windchamber | South Grapple Up", player),
                    can_use_grapple_beam(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Gateway (Grand Windchamber Side)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
    ]


class GrandWindchamber_WindchamberTunnelSide(MetroidPrime2Region):
    name = "Grand Windchamber"
    desc = "Windchamber Tunnel Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Cannon)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Sky Temple Grounds - Ing Windchamber | North Grapple Up", player),
                    can_use_grapple_beam(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Temple Grounds - Grand Windchamber | 3BSJ then SA from Windchamber Tunnel Side to Platform"),
                can_lay_bomb(state, player),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Gateway Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Sky Temple Grounds - Ing Windchamber | South Grapple Up", player),
                    can_use_grapple_beam(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Tunnel (Grand Windchamber Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
