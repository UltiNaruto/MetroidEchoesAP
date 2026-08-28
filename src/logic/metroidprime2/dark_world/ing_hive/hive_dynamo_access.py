from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_safe_zone,
    can_use_annihilator_beam,
    can_use_dark_beam,
    can_use_darkburst,
    can_use_light_beam,
    can_use_power_beam,
    can_use_sonic_boom,
    has_dark_suit,
    has_light_suit,
    has_missile_count,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveDynamoAccess_EchoLock(MetroidPrime2Region):
    name = "Hive Dynamo Access"
    desc = "Echo Lock"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Works (North Portal Safe Zone)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Access (Gyro Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                    ]),
                ]),
                state.has("Ing Hive - Hive Dynamo Access | Echo Gate Opened", player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Echo Gate Opened",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Dynamo Access | Echo Gate Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Echo Visor", player),
                condition_or([
                    can_use_power_beam(state, player),
                    can_use_dark_beam(state, player),
                    can_use_light_beam(state, player),
                    can_use_annihilator_beam(state, player),
                    has_missile_count(state, player, 5),
                ]),
            ]),
        )

class HiveDynamoAccess_GyroSide(MetroidPrime2Region):
    name = "Hive Dynamo Access"
    desc = "Gyro Side"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Access (Echo Lock)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                    ]),
                ]),
                condition_or([
                    state.has("Ing Hive - Hive Dynamo Access | Echo Gate Opened", player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Dynamo Access | Sonicboom or Darkburst Behind Echo Lock"),
                        condition_or([
                            can_use_darkburst(state, player, amount_to_use=2),
                            can_use_sonic_boom(state, player, amount_to_use=2),
                        ])
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Gyro Chamber (South Lower)",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
    ]
