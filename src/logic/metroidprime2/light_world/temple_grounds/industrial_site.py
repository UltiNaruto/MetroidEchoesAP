from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_lay_bomb,
    can_lay_bomb_or_pb,
    can_use_charged_annihilator_beam,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_charged_power_beam,
    can_use_power_beam,
    can_use_screw_attack,
    has_missile_count,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class IndustrialSite_BehindTranslatorGate(MetroidPrime2Region):
    name = "Industrial Site"
    desc = "Behind Translator Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Agon Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Front of Translator Gate)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
    ]


class IndustrialSite_Center(MetroidPrime2Region):
    name = "Industrial Site"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Collapsed Tunnel Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Industrial Site | DBJ from Center to Collapsed Tunnel Ledge"),
                    can_lay_bomb(state, player),
                ]),
                state.has("Space Jump Boots", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Front of Translator Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has_any({
                    "Space Jump Boots",
                    "Temple Grounds - Industrial Site | Container Moved"
                }, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Scan Visor", player),
                # conditions to destroy the locks of the gate
                condition_or([
                    condition_and([
                        has_trick_enabled(state, player, "Temple Grounds - Industrial Site | Open Gate from Center with Missiles"),
                        has_missile_count(state, player, 2),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Temple Grounds - Industrial Site | Open Gate from Center with Charged Annihilator Beam"),
                        can_use_charged_annihilator_beam(state, player, requires_ammo=True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Temple Grounds - Industrial Site | Open Gate from Center with Charge Beam"),
                        can_use_charged_power_beam(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Hive Transport Area Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Temple Grounds - Industrial Site | Gate Opened", player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Industrial Site | SA over Gate"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Industrial Site | 3BJ over Gate"),
                    can_lay_bomb(state, player),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Container Moved",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - Industrial Site | Container Moved",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
        ]


class IndustrialSite_CollapsedTunnelLedge(MetroidPrime2Region):
    name = "Industrial Site"
    desc = "Collapsed Tunnel Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Collapsed Tunnel (Industrial Site Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]


class IndustrialSite_FrontOfTranslatorGate(MetroidPrime2Region):
    name = "Industrial Site"
    desc = "Front of Translator Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Behind Translator Gate)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has_any({
                    "Space Jump Boots",
                    "Temple Grounds - Industrial Site | Container Moved"
                }, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Collapsed Tunnel Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Industrial Site | Lowered Bridge", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Lowered Bridge",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - Industrial Site | Lowered Bridge",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_and([
                    state.has("Scan Visor", player),
                    condition_or([
                        can_use_power_beam(state, player),
                        can_use_charged_dark_beam(state, player),
                        can_use_charged_light_beam(state, player),
                        can_use_charged_annihilator_beam(state, player),
                        has_missile_count(state, player, 2),
                    ]),
                ]),
                parent=self,
            ),
        ]


class IndustrialSite_Gate(MetroidPrime2Region):
    name = "Industrial Site"
    desc = "Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Hive Transport Area Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Gate Opened",
                locked_item=MetroidPrime2Item(
                    name="Temple Grounds - Industrial Site | Gate Opened",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class IndustrialSite_HiveTransportAreaSide(MetroidPrime2Region):
    name = "Industrial Site"
    desc = "Hive Transport Area Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hive Transport Area (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Industrial Site | Gate Opened", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Industrial Site (Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Scan Visor", player),
                # conditions to break the gate locks
                condition_or([
                    can_use_power_beam(state, player),
                    can_use_charged_dark_beam(state, player),
                    can_use_charged_light_beam(state, player),
                    can_use_charged_annihilator_beam(state, player),
                    can_use_screw_attack(state, player),
                    can_lay_bomb_or_pb(state, player, 2),
                    has_missile_count(state, player, 2),
                ]),
            ]),
        ),
    ]
