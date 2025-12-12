from BaseClasses import ItemClassification, MultiWorld

from ... import can_activate_dark_portal, can_lay_bomb, has_trick_enabled
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class SacredPath_GreatTempleSide(MetroidPrime2Region):
    name = "Sacred Path"
    desc = "Great Temple Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Portal Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Space Jump Boots", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Sacred Bridge Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Transport A",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class SacredPath_PortalLedge(MetroidPrime2Region):
    name = "Sacred Path"
    desc = "Portal Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Sky Temple Grounds - Profane Path (Portal Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Great Temple Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Sacred Bridge Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]


class SacredPath_SacredBridgeSide(MetroidPrime2Region):
    name = "Sacred Path"
    desc = "Sacred Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Bridge (Sacred Path Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Great Temple Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Sacred Path | DBJ to Great Temple Side"),
                    can_lay_bomb(state, player),
                ]),
                state.has_all({
                    "Temple Grounds - Sacred Path | Cannon Activated",
                    "Morph Ball",
                }, player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Cannon Activated",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Sacred Path | Cannon Activated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True,
        )
