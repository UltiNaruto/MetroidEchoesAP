from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_use_grapple_beam,
    can_use_boost_ball,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    can_activate_light_portal,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class JudgementDrop_Door(MetroidPrime2Region):
    name = "Judgement Drop"
    desc = "Door"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site (Ledge Door)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Judgement Drop (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    can_use_grapple_beam(state, player),
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Judgement Drop | Boost Jump across Gap"),
                        state.has("Space Jump Boots", player),
                        can_use_boost_ball(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Judgement Drop | NSJ SA across Gap"),
                        can_use_screw_attack(state, player, True),
                    ]),
                ]),
            ]),
        ),
    ]

class JudgementDrop_Portal(MetroidPrime2Region):
    name = "Judgement Drop"
    desc = "Portal"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Judgement Drop (Door)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    can_use_grapple_beam(state, player),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Grand Abyss",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player)
        )
    ]
