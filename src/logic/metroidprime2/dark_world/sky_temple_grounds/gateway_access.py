from ... import (
    can_activate_safe_zone,
    has_dark_suit,
    has_light_suit,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class GatewayAccess_SafeZone(MetroidPrime2Region):
    name = "Gateway Access"
    desc = "Safe Zone"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Gateway Access (Shrine Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Gateway Access (Sky Temple Gateway Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
    ]


class GatewayAccess_ShrineAccessSide(MetroidPrime2Region):
    name = "Gateway Access"
    desc = "Shrine Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Gateway Access (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Shrine Access (Safe Zone)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
    ]


class GatewayAccess_SkyTempleGatewaySide(MetroidPrime2Region):
    name = "Gateway Access"
    desc = "Sky Temple Gateway Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Gateway Access (Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank") >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sky Temple Gateway (Gateway Access Side)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                # TODO: suitless logic
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]