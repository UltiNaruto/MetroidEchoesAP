from BaseClasses import ItemClassification, MultiWorld
from ... import can_use_seeker_launcher

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or


class SacredBridge_Center(MetroidPrime2Region):
    name = "Sacred Bridge"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Bridge (Sacred Path Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has_all({
                    "Temple Grounds - Sacred Bridge | SJ from Center to Sacred Path Side",
                    "Space Jump Boots",
                }, player),
                state.has("Temple Grounds - Sacred Bridge | Cannon Activated", player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Cannon Activated",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Sacred Bridge | Cannon Activated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player),
        )


class SacredBridge_GFMCCompoundSide(MetroidPrime2Region):
    name = "Sacred Bridge"
    desc = "GFMC Compound Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Sacred Bridge Ledge)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Bridge (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Bridge (Sacred Path Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Sacred Bridge | Dark Visor Locks Destroyed", player),
        ),
    ]


class SacredBridge_SacredPathSide(MetroidPrime2Region):
    name = "Sacred Bridge"
    desc = "Sacred Path Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Bridge (GFMC Compound Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Sacred Bridge | Dark Visor Locks Destroyed", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Path (Sacred Bridge Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Dark Visor Locks Destroyed",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Sacred Bridge | Dark Visor Locks Destroyed",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_use_seeker_launcher(state, player, has_dark_visor=True),
        )
