from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class ControllerTransport_Bottom(MetroidPrime2Region):
    name = "Controller Transport"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="Great Temple - Controller Transport (Top)",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Controller Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class ControllerTransport_Top(MetroidPrime2Region):
    name = "Controller Transport"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="Great Temple - Controller Transport (Bottom)",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Main Energy Controller",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]