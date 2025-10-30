from BaseClasses import MultiWorld

from ... import can_lay_bomb, can_lay_pb, has_trick_enabled
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class DynamoChamber_BetweenItemGates(MetroidPrime2Region):
    name = "Dynamo Chamber"
    desc = "Between Item Gates"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_pb(state, player, 2),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_pb(state, player, 2),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Temple Assembly Site Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_pb(state, player, 2),
        ),
    ]


class DynamoChamber_Center(MetroidPrime2Region):
    name = "Dynamo Chamber"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Between Item Gates)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_pb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Communication Area Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_pb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Dynamo Chamber | DBJ over Communication Area Side gate"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Dynamo Chamber | SJ over Communication Area Side gate"),
                    state.has_all({
                        "Space Jump Boots",
                        "Morph Ball",
                    }, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Temple Assembly Site Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Space Jump Boots", player),
        ),
    ]


class DynamoChamber_CommunicationAreaSide(MetroidPrime2Region):
    name = "Dynamo Chamber"
    desc = "Communication Area Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Communication Area (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_pb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Dynamo Chamber | DBJ over Communication Area Side gate"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Dynamo Chamber | SJ over Communication Area Side gate"),
                    state.has_all({
                        "Space Jump Boots",
                        "Morph Ball",
                    }, player),
                ]),
            ]),
        ),
    ]


class DynamoChamber_Item(MetroidPrime2Region):
    name = "Dynamo Chamber"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Between Item Gates)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_pb(state, player, 2),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Power Bomb Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class DynamoChamber_TempleAssemblySiteSide(MetroidPrime2Region):
    name = "Dynamo Chamber"
    desc = "Temple Assembly Site Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Dynamo Chamber Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Between Item Gates)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_pb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Space Jump Boots", player),
        ),
    ]
