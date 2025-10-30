from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HiveTransportArea_BehindTranslatorGate(MetroidPrime2Region):
    name = "Hive Transport Area"
    desc = "Behind Translator Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Access Tunnel (Hive Transport Area Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Transport Area (Top)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
    ]


class HiveTransportArea_Bottom(MetroidPrime2Region):
    name = "Hive Transport Area"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Chamber C",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Transport Area (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]


class HiveTransportArea_Top(MetroidPrime2Region):
    name = "Hive Transport Area"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Transport Area (Behind Translator Gate)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Hive Transport Area Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Transport Area (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]
