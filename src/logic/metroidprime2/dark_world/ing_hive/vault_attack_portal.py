from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_use_grapple_beam,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    can_activate_light_portal,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or



class VaultAttackPortal_BeamPortal(MetroidPrime2Region):
    name = "Vault Attack Portal"
    desc = "Beam Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Vault Attack Portal (Scan Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Vault Attack Portal | Z-Axis SA to cross"),
                        can_use_screw_attack(state, player, True)
                    ]),
                ]),
                condition_and([
                    condition_or([ 
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player)
                        ]),
                    can_use_grapple_beam(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Vault (East)", #Name is subject to change
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
    ]


class VaultAttackPortal_ScanPortal(MetroidPrime2Region):
    name = "Vault Attack Portal"
    desc = "Scan Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Vault Attack Portal (Beam Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Vault Attack Portal | Z-Axis SA to cross"),
                        can_use_screw_attack(state, player, True)
                    ]),
                ]),
                condition_and([
                    condition_or([
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                        has_light_suit(state, player)
                        ]),
                    can_use_grapple_beam(state, player),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Vault (West)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
    ]
