from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    can_lay_pb,
    can_use_boost_ball,
    can_use_screw_attack,
    has_dark_ammo,
    has_light_ammo,
    can_use_darkburst,
    can_use_sonic_boom,
    can_activate_dark_portal,
    has_oob_kit
)
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class MiningStationB_MineShaftSide(MetroidPrime2Region):
    name = "Mining Station B"
    desc = "Mine Shaft Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Cannon)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mine Shaft (Bottom)",
            door=DoorCover.Seeker,
            rule=lambda state, player: True
        ),
    ]

class MiningStationB_Center(MetroidPrime2Region):
    name = "Mining Station B"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Agon Wastes - Mining Station B | Portal Opened", player),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                can_use_boost_ball(state, player),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | BSJ up to Portal"),
                                    state.has("Space Jump Boots", player)
                                ]),
                            ]),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Mining Station B | SA to Portal"),
                            can_use_screw_attack(state, player),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Slope Jump to Portal"),
                            state.has("Space Jump Boots", player),
                        ])
                    ])
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Out of Bounds"),
                    has_oob_kit(state, player),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Mine Shaft Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Agon Wastes - Mining Station B | Cannon Activated")
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | 2BJS to Item before Puzzle"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player),
                    not state.has("Agon Wastes - Mining Station B | Portal Opened", player),
                ]),
                condition_and([
                    state.has("Agon Wastes - Mining Station B | Portal Opened", player),
                    condition_or([
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Mining Station B | SA Cancel to Item"),
                            can_use_screw_attack(state, player)
                        ]),
                        condition_and([
                            state.has("Space Jump Boots", player),
                            condition_or([
                                has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Slope Jump to Standable Terrain"),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | 1BSJ to Item Ledge"),
                                    can_lay_bomb(state, player),
                                ])
                            ])
                        ]),
                        condition_and([
                            can_lay_bomb(state, player),
                            can_use_boost_ball(state, player),
                            condition_or([
                                has_trick_enabled(state, player, "Agon Wastes - Mining Station B | TBJ to Standable Terrain from Portal Platform"),
                                has_trick_enabled(state, player, "Agon Wastes - Mining Station B | 2BSJ to Standable Terrain from Portal Platform"),
                            ])
                        ])
                    ])
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | SA from Cannon Standable Terrain to Item"),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Slope Jump to Portal Cover then Combat/Scan Dash to Item"),
                    not state.has("Agon Wastes - Mining Station B | Portal Opened"),
                    state.has({
                        "Scan Visor",
                        "Space Jump Boots",
                    }, player),
                ])
            ])
        )
    ]
    

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Portal Opened",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Mining Station B | Portal Opened",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player
                ),
                can_access=lambda state, player: condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        condition_and([
                            can_lay_bomb(state, player),
                            condition_or([
                                state.has("Scan Visor", player),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | SA from Standable Terrain to Top Bomb Slot"),
                                    can_use_screw_attack(state, player)
                                ]),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Slope Jump to Top Bomb Slot"),
                                    state.has("Space Jump Boots", player),
                                ])
                            ])
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Bomb Slots without Bombs"),
                            state.has("Scan Visor", player),
                            condition_or([
                                has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Instant Morph into Bottom Bomb Slot"),
                                condition_and([
                                    has_trick_enabled(state, player, "Agon Wastes - Mining Station B | Wall Boost into Bottom Bomb Slot"),
                                    can_use_boost_ball(state, player),
                                ])
                            ]),
                            condition_and([
                                has_dark_ammo(state, player),
                                condition_or([
                                    can_use_darkburst(state, player),
                                    condition_and([
                                        has_light_ammo(state, player),
                                        can_use_sonic_boom(state, player),
                                    ])
                                ])
                            ])
                        ])
                    ])
                ])
            ),
            MetroidPrime2Location(
                name="Cannon Activated",
                locked_item=MetroidPrime2Item(
                    name="Agon Wastes - Mining Station B | Cannon Activated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            )
        ]

class MiningStationB_BehindPBWall(MetroidPrime2Region):
    name = "Mining Station B"
    desc = "Behind PB Wall"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_lay_pb(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Storage A",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        )
    ]


class MiningStationB_TransitStationSide(MetroidPrime2Region):
    name = "Mining Station B"
    desc = "Transit Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transit Station (Mining Station B Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]

class MiningStationB_Portal(MetroidPrime2Region):
    name = "Mining Station B"
    desc = "Portal"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Trial Grounds (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station B (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        )
    ]