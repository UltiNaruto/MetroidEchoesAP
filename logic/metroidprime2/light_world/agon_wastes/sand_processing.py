from BaseClasses import Multiworld, ItemClassification
from ... import (
    has_trick_enabled,
    has_missile_count,
    can_lay_bomb,
    can_use_boost_ball,
    can_use_screw_attack,
    can_use_darkburst,
    can_use_sonic_boom,
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class SandProcessing_SaveStationCSide(MetroidPrime2Region):
    name = "Sand Processing"
    desc = "Save Station C Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Halfpipe)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station C",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

class SandProcessing_Halfpipe(MetroidPrime2Region):
    name = "Sand Processing"
    desc = "Halfpipe"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Save Station C Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    not state.has("Agon Wastes - Sand Processing | Sand Drained"),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Sand Processing | DBJ up to Save Station C"),
                            can_lay_bomb(state, player),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "NSJ SA Slope Jump to Save Station C"),
                            can_use_screw_attack(state, player),
                        ])
                    ])
                ]),
                condition_and([
                    state.has("Agon Wastes - Sand Processing | Sand Drained"),
                    condition_or([
                        can_use_boost_ball(state, player),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Sand Processing | TBSJ up to Save Station C"),
                            state.has("Space Jump Boots", player),
                            can_lay_bomb(state, player),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Sand Processing | SA Slope Jump up to Save Station C")
                        ])
                    ])
                ])
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Behind Glass)",
            door=DoorCover.Opened,
            rule=lambda state, player: has_missile_count(state, player, 1),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Morph Tunnel Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_use_boost_ball(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Sand Process | 2BSJ up to Morph Tunnel Ledge"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Sand Process | SA over to Morph Tunnel Ledge"),
                    can_use_screw_attack(state, player),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Sand Processing | Sand Drained"),
        ),
    ]

class SandProcessing_BehindGlass(MetroidPrime2Region):
    name = "Sand Processing"
    desc = "Behind Glass"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Halfpipe)",
            door=DoorCover.Opened,
            rule=lambda state, player: has_missile_count(state, player, 1),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Main Reactor (Sand Processing Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

class SandProcessing_MorphTunnelLedge(MetroidPrime2Region):
    name = "Sand Processing"
    desc = "Morph Tunnel Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Bomb Slot)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Sand Processing | Wall Boost into Morph Tunnel"),
                    can_use_boost_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Sand Processing | SA into Morph Tunnel"),
                    can_use_screw_attack(state, player),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Halfpipe)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        )
    ]

class SandProcessing_BombSlot(MetroidPrime2Region):
    name = "Sand Processing"
    desc = "Bomb Slot"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Processing (Morph Tunnel Ledge)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Sand Processing | Wall Boost into Morph Tunnel"),
                    can_use_boost_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Sand Processing | SA into Morph Tunnel"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: Multiworld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Sand Drained",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Sand Processing | Sand Drained",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Agon Wastes - Sand Processing | Bomb Slot without Bombs"),
                        state.has("Space Jump Boots", player),
                        condition_or([
                            can_use_darkburst(state, player),
                            can_use_sonic_boom(state, player),
                        ]),
                    ]),
                ]),
                parent=self,
            ),
        ]