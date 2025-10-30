from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class WindchamberTunnel_GFMCCompoundSide(MetroidPrime2Region):
    name = "Windchamber Tunnel"
    desc = "GFMC Compound Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Windchamber Tunnel Ledge)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Tunnel (Grand Windchamber Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
    ]


class WindchamberTunnel_GrandWindchamberSide(MetroidPrime2Region):
    name = "Windchamber Tunnel"
    desc = "Grand Windchamber Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Tunnel Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Tunnel (GFMC Compound Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
    ]
