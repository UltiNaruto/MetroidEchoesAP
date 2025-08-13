from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_screw_attack,
)
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class MiningPlaza_Bottom(MetroidPrime2Region):
    name = "Mining Plaza"
    desc = "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Top)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Plaza | DBJ up Ledges"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Plaza | NSJ SA over Pillar Gap"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Plaza | Scan Dash over Pillar Gap"),
                    state.has("Scan Visor", player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station A (Mining Plaza Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Plaza Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Behind Translator Gate)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
    ]

class MiningPlaza_Top(MetroidPrime2Region):
    name = "Mining Plaza"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has_all({
                    "Agon Wastes - Agon Energy Controller | Light Returned",
                    "Echo Visor"
                }, player),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Mining Plaza | Extended Dash to Item"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor"
                        }, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access (Mining Plaza Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class MiningPlaza_BehindTranslatorGate(MetroidPrime2Region):
    name = "Mining Plaza"
    desc = "Behind Translator Gate",
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Bottom)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Agon Map Station",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        )
    ]

class MiningPlaza_Item(MetroidPrime2Region):
    name = "Mining Plaza"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Plaza (Bottom)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
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