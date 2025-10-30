from BaseClasses import MultiWorld

from ... import can_use_grapple_beam, can_use_screw_attack
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or


class WindchamberGateway_GrandWindchamberSide(MetroidPrime2Region):
    name = "Windchamber Gateway"
    desc = "Grand Windchamber Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Gateway Side)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Gateway (Path of Eyes Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
    ]


class WindchamberGateway_PathOfEyesSide(MetroidPrime2Region):
    name = "Windchamber Gateway"
    desc = "Path of Eyes Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Winchamber Gateway Side)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Gateway (Grand Windchamber Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Gateway (Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player),
            ]),
        ),
    ]


class WindchamberGateway_Platform(MetroidPrime2Region):
    name = "Windchamber Gateway"
    desc = "Platform"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Grand Windchamber (Windchamber Gateway Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Energy Tank)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]
