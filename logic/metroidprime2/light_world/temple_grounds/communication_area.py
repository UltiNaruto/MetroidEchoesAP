from BaseClasses import MultiWorld

from ... import can_lay_bomb, can_lay_bomb_or_pb, can_use_screw_attack, has_trick_enabled
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class CommunicationArea_Bottom(MetroidPrime2Region):
    name = "Communication Area"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Communication Area (Item Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Temple Grounds - Communication Area | Standable Terrain from Bottom to Item Ledge"),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Communication Area | DBJ from Bottom to Item Ledge"),
                    can_lay_bomb(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Communication Area Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Trooper Security Station (Communication Area Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class CommunicationArea_ItemLedge(MetroidPrime2Region):
    name = "Communication Area"
    desc = "Item Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Communication Area (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Communication Area (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Communication Area | DBJ from Item Ledge to Top"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Communication Area | NSJ SA from Item Ledge to Top"),
                    can_use_screw_attack(state, player, is_nsj=True),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: can_lay_bomb_or_pb(state, player),
                parent=self,
            ),
        ]


class CommunicationArea_Top(MetroidPrime2Region):
    name = "Communication Area"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Communication Area (Item Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Storage Cavern A",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
