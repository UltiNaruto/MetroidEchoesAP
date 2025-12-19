from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_dark_portal,
    can_lay_bomb,
    can_use_annihilator_beam,
    can_use_dark_beam,
    can_use_light_beam,
    can_use_power_beam,
    can_use_screw_attack,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TempleAssemblySite_BehindLightBeamBlock(MetroidPrime2Region):
    name = "Temple Assembly Site"
    desc = "Behind Light Beam Block"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Sky Temple Grounds - Plain of Dark Worship",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Temple Assembly Site | Light Beam Block Opened", player),
        ),
    ]


class TempleAssemblySite_BehindTranslatorGate(MetroidPrime2Region):
    name = "Temple Assembly Site"
    desc = "Behind Translator Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Transport B",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Center)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
    ]


class TempleAssemblySite_Center(MetroidPrime2Region):
    name = "Temple Assembly Site"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Behind Translator Gate)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Collapsed Tunnel Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Dynamo Chamber Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has_all({
                    "Temple Grounds - Temple Assembly Site | Container Moved",
                    "Temple Grounds - Temple Assembly Site | Container Shot Down",
                }, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Item Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Temple Grounds - Temple Assembly Site | Slope Jump to Item Ledge"),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Temple Assembly Site | DBJ to Item Ledge"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Temple Assembly Site | NSJ SA to Item Ledge"),
                    can_use_screw_attack(state, player, is_nsj=True),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Storage Cavern B Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Container Moved",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Temple Assembly Site | Container Moved",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player),
        )
        self.add_location(
            name="Container Shot Down",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Temple Assembly Site | Container Shot Down",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Temple Grounds - Temple Assembly Site | Container Moved", player),
                condition_or([
                    can_use_power_beam(state, player),
                    can_use_dark_beam(state, player),
                    can_use_light_beam(state, player),
                    can_use_annihilator_beam(state, player),
                ]),
            ]),
        )


class TempleAssemblySite_CollapsedTunnelSide(MetroidPrime2Region):
    name = "Temple Assembly Site"
    desc = "Collapsed Tunnel Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Collapsed Tunnel (Temple Assembly Site Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Behind Light Beam Block)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Temple Assembly Site | Light Beam Block Opened", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Light Beam Block Opened",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Temple Assembly Site | Light Beam Block Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_use_light_beam(state, player),
        )


class TempleAssemblySite_DynamoChamberLedge(MetroidPrime2Region):
    name = "Temple Assembly Site"
    desc = "Dynamo Chamber Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Dynamo Chamber (Temple Assembly Site Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]


class TempleAssemblySite_ItemLedge(MetroidPrime2Region):
    name = "Temple Assembly Site"
    desc = "Item Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: state.has("Morph Ball", player),
        )


class TempleAssemblySite_StorageCavernBSide(MetroidPrime2Region):
    name = "Temple Assembly Site"
    desc = "Storage Cavern B Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Storage Cavern B",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]
