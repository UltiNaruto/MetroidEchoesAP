from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_lay_bomb,
    can_lay_bomb_or_pb,
    can_use_annihilator_beam,
    can_use_boost_ball,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_charged_power_beam,
    can_use_screw_attack,
    has_missile_count,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class GFMCCompound_AboveShip(MetroidPrime2Region):
    name = "GFMC Compound"
    desc = "Above Ship"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: state.has("Dark Agon Wastes - Judgement Pit | Jump Guardian Dead", player),
                parent=self,
            ),
        ]


class GFMCCompound_BehindTranslatorGate(MetroidPrime2Region):
    name = "GFMC Compound"
    desc = "Behind Translator Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Fortress Transport Access (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Center)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: True,
        ),
    ]


class GFMCCompound_Center(MetroidPrime2Region):
    name = "GFMC Compound"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Behind Translator Gate)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Sacred Bridge Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - GFMC Compound | DBJ to Sacred Bridge Ledge"),
                    can_lay_bomb(state, player),
                ]),
                state.has_all({
                    "Temple Grounds - GFMC Compound | Cannon Activated",
                    "Morph Ball",
                }, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Trooper Security Station Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - GFMC Compound | Cutscene Watched", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Windchamber Tunnel Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: has_trick_enabled(state, player, "Temple Grounds - GFMC Compound | DBJ to Windchamber Tunnel Ledge"),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Cannon Activated",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - GFMC Compound | Cannon Activated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
            MetroidPrime2Location(
                name="Pickup (Missile Launcher)",
                can_access=lambda state, player: condition_or([
                    can_lay_bomb_or_pb(state, player),
                    can_use_annihilator_beam(state, player),
                    can_use_boost_ball(state, player),
                    can_use_charged_power_beam(state, player),
                    can_use_charged_dark_beam(state, player),
                    can_use_charged_light_beam(state, player),
                    can_use_screw_attack(state, player),
                    has_missile_count(state, player, 1),
                ]),
                parent=self,
            ),
        ]


class GFMCCompound_Cutscene(MetroidPrime2Region):
    name = "GFMC Compound"
    desc = "Cutscene"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - GFMC Compound | Cutscene Watched", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Cutscene Watched",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - GFMC Compound | Cutscene Watched",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class GFMCCompound_SacredBridgeLedge(MetroidPrime2Region):
    name = "GFMC Compound"
    desc = "Sacred Bridge Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Trooper Security Station Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Windchamber Tunnel Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Sacred Bridge (GFMC Compound Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
    ]


class GFMCCompound_TrooperSecurityStationSide(MetroidPrime2Region):
    name = "GFMC Compound"
    desc = "Trooper Security Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has_any({
                    "Temple Grounds - GFMC Compound | Cutscene Watched",
                    "Space Jump Boots",
                }, player),
                has_trick_enabled(state, player, "Temple Grounds - GFMC Compound | Slope Jump to Sacred Bridge Ledge"),
                has_trick_enabled(state, player, "Temple Grounds - GFMC Compound | DBJ to Sacred Bridge Ledge"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Cutscene)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Trooper Security Station (GFMC Compound Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Cutscene Watched (From Trooper Security Station Side)",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - GFMC Compound | Cutscene Watched",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class GFMCCompound_WindchamberTunnelLedge(MetroidPrime2Region):
    name = "GFMC Compound"
    desc = "Windchamber Tunnel Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Sacred Bridge Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Morph Ball", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Tunnel (GFMC Compound Side)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True,
        ),
    ]
