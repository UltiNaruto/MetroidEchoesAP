from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_use_screw_attack,
    can_use_boost_ball,
    can_use_darkburst,
    can_use_sonic_boom
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class TransportCenter_PortalTerminalSide(MetroidPrime2Region):
    name = "Transport Center"
    desc = "Portal Terminal Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Halfpipe)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Terminal (Behind Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class TransportCenter_Halfpipe(MetroidPrime2Region):
    name = "Transport Center",
    desc = "Halfpipe",
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Behind Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Transport Center | Gate Opened"),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Transport to Trovus Bog Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_use_boost_ball(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Transport Center | Slope Jump SA to Transport to Torvus Bog"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        has_trick_enabled(state, player, "Agon Wastes - Transport Center | Halfpipe Standable up to Tranpsort to Torvus Bog"),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Transport Center | Instant Morph to Instant Unmorph Jump to Transport to Torvus Bog"),
                            state.has("Morph Ball", player),
                        ])
                    ])
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_boost_ball(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Portal Terminal Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Gate Opened",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Transport Center | Gate Opened",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Transport Center | Bomb Slot without Bombs"),
                        state.has("Morph Ball", player),
                        condition_or([
                            can_use_darkburst(state, player),
                            can_use_sonic_boom(state, player),
                        ]),
                    ]),
                ]),
                parent=self,
            ),
            MetroidPrime2Location(
                name="Pickup (Missile)",
                can_access=lambda state, player: state.has("Agon Wastes - Transport Center | Gate Opened"),
                parent=self,
            ),
        ]

class TransportCenter_TransportToTorvusBogLedge(MetroidPrime2Region):
    name = "Transport Center"
    desc = "Trasnport to Torvus Bog Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Halfpipe)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Agon Wastes - Transport Center | 2BSJ from Transport to Torvus Bog Ledge to Portal"),
                state.has("Space Jump Boots", player),\
                can_lay_bomb(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport to Torvus Bog",
            # TODO: add logic for seeker skip
            door=DoorCover.Seeker,
            rule=lambda state, player: True,
        )
    ]

class TransportCenter_BehindGate(MetroidPrime2Region):
    name = "Transport Center"
    desc = "Behind Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Trasport Center (Halfpipe)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Transport Center | Gate Opened"),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station A (Transport Center Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]