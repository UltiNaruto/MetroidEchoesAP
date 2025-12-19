from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_light_portal,
    can_lay_bomb,
    can_use_annihilator_beam,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class ProfanePath_Item(MetroidPrime2Region):
    name = "Profane Path"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Profane Path (Sky Temple Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Sky Temple Grounds - Profane Path | Sonic Gate Opened", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Beam Ammo Expansion)",
            can_access=lambda state, player: True,
        )


class ProfanePath_PhazonPitSide(MetroidPrime2Region):
    name = "Profane Path"
    desc = "Phazon Pit Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Pit (Profane Path Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Profane Path (Sky Temple Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Sky Temple Grounds - Profane Path | DBJ to Sky Temple Side"),
                    can_lay_bomb(state, player),
                ]),
            ]),
        ),
    ]


class ProfanePath_PortalLedge(MetroidPrime2Region):
    name = "Profane Path"
    desc = "Portal Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Temple Grounds - Sacred Path (Portal Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Profane Path (Phazon Pit Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]


class ProfanePath_SkyTempleSide(MetroidPrime2Region):
    name = "Profane Path"
    desc = "Sky Temple Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Portal Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Space Jump Boots", player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Profane Path (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Sky Temple Grounds - Profane Path | Sonic Gate Opened", player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Profane Path (Phazon Pit Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Sonic Gate Opened",
            locked_item=MetroidPrime2Item(
                name="Sky Temple Grounds - Profane Path | Sonic Gate Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Echo Visor", player),
                can_use_annihilator_beam(state, player),
            ]),
        )
