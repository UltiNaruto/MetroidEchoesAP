from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class CollapsedTunnel_TempleAssemblySiteSide(MetroidPrime2Region):
    name = "Collapsed Tunnel"
    desc = "Temple Assembly Site Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Collapsed Tunnel (Industrial Site Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Collapsed Tunnel Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class CollapsedTunnel_IndustrialSiteSide(MetroidPrime2Region):
    name = "Collapsed Tunnel"
    desc = "Industrial Site Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Collapsed Tunnel (Temple Assembly Site Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Collapsed Tunnel Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
