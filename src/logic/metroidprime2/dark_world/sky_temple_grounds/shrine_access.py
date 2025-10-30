from ... import (
    can_activate_safe_zone,
    can_lay_bomb,
    can_use_boost_ball,
    has_dark_suit,
    has_light_suit,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class ShrineAccess_SafeZone(MetroidPrime2Region):
    name = "Shrine Access"
    desc = "Safe Zone"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Shrine Access (War Ritual Grounds Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Sky Temple Grounds - Shrine Access | Wall Boost"),
                        can_use_boost_ball(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Defiled Shrine (Top)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Gateway Access (Shrine Access Side)",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]


class ShrineAccess_WarRitualGroundsSide(MetroidPrime2Region):
    name = "Shrine Access"
    desc = "War Ritual Grounds Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Shrine Access (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    state.count("Energy Tank") >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Sky Temple Grounds - Shrine Access | Wall Boost"),
                        can_use_boost_ball(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - War Ritual Grounds (Shrine Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.count("Energy Tank") >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]