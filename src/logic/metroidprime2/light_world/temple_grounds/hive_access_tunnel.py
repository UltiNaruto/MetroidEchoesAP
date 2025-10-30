from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HiveAccessTunnel_HiveTransportAreaSide(MetroidPrime2Region):
    name = "Hive Access Tunnel"
    desc = "Hive Transport Area Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Access Tunnel (Landing Site Side)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Transport Area (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class HiveAccessTunnel_LandingSiteSide(MetroidPrime2Region):
    name = "Hive Access Tunnel"
    desc = "Landing Site Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Access Tunnel (Hive Transport Area Side)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber A",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Landing Site (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
