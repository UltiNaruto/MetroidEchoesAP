from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_light_portal,
    can_activate_safe_zone,
    can_lay_bomb,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class AerialTrainingSite_Box(MetroidPrime2Region):
    name = "Aerial Training Site"
    desc = "Box"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Safe Zones)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | Z-Axis SA Throughout the Room"),
                        can_use_screw_attack(state, player, z_axis=True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | E-Dash from Box to Safe Zones"),
                        state.has_all({
                            "Space Jump Boots", 
                            "Scan Visor"}, 
                            player),
                        ]),
                    ]),
                state.has("Ing Hive - Aerial Training Site | Box Scanned", player),
                condition_or([
                    has_light_suit(state, player),
                    condition_and([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            state.count("Energy Tank", player) >= 1, #Maybe an extra could be added because of the dark commandos
                            has_dark_suit(state, player),
                        ]),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive West Transport (Upper)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Box Scanned",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Aerial Training Site | Box Scanned",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player),
        )
        self.add_location(
            name="Pickup (Ing Hive Key 3)",
            can_access=lambda state, player: True,
        )

class AerialTrainingSite_CrystalDoor(MetroidPrime2Region):
    name = "Aerial Training Site"
    desc = "Crystal Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Safe Zones)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | Z-Axis SA Throughout the Room"),
                        can_use_screw_attack(state, player, z_axis=True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | SJ Terminal Fall from Crystal Door to Safe Zones"),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
                condition_or([
                    has_light_suit(state, player),
                    has_dark_suit(state, player),
                    condition_and([
                        can_activate_safe_zone(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access (Training Site Door)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True
        ),
    ]


class AerialTrainingSite_LedgeDoor(MetroidPrime2Region):
    name = "Aerial Training Site"
    desc = "Ledge Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Safe Zones)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                has_light_suit(state, player),
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Judgement Drop (Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class AerialTrainingSite_Portal(MetroidPrime2Region):
    name = "Aerial Training Site"
    desc = "Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Safe Zones)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_safe_zone(state, player),
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Watch Station (Portal)", #Name can be subject to change
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player)
        ),
    ],

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)
        
        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: 
            condition_or([
                can_use_screw_attack(state, player),
                condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | SA Wall Item Z-Axis SA"),
                        can_use_screw_attack(state, player, z_axis=True),
                    ]),
                condition_and([
                    has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | SA Wall Item with DBJ and Roll Jump"),
                    state.has("Space Jump Boots",player),
                    can_lay_bomb(state, player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | SA Wall Item with Slope Jump and Roll Jump"),
                    state.has_all({
                        "Space Jump Boots",
                        "Morph Ball",
                    },player)
                ]),
            ]),
        )


class AerialTrainingSite_SafeZones(MetroidPrime2Region):
    name = "Aerial Training Site"
    desc = "Safe Zones"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Box)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | Z-Axis SA Throughout the Room"),
                        can_use_screw_attack(state, player, z_axis=True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | SJ and Scan Dash to Box"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor"
                        }, player),
                    ]),
                ]),
                condition_or([
                    state.has("Ing Hive - Aerial Training Site | Box Scanned", player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | SJ and Scan Dash to Box"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor"
                        }, player),
                    ]),
                ]),
                condition_or([
                    has_light_suit(state, player),
                    condition_and([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            state.count("Energy Tank", player) >= 2,
                            has_dark_suit(state, player),
                        ]),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Crystal Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | Z-Axis SA Throughout the Room"),
                        can_use_screw_attack(state, player, z_axis=True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | E-Dash to Crystal Door"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                            }, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | Roll Jump to Crystal Door"),
                        state.has_all({
                            "Space Jump Boots",
                            "Morph Ball",
                        }, player)
                    ]),
                ]),
                condition_or([
                    has_light_suit(state, player),
                    condition_and([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            state.count("Energy Tank", player) >= 1, 
                            has_dark_suit(state, player),
                        ]),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Ledge Door)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Ing Hive - Aerial Training Site | NSJ to Judgement Drop Door"),
            ]),
        ),
    ]
