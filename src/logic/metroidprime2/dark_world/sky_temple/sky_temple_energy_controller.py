from ... import (
    has_enough_sky_temple_keys,
    has_light_suit,
    must_fight_dark_samus_3_4,
)

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and


class SkyTempleEnergyController(MetroidPrime2Region):
    name = "Sky Temple Energy Controller"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple - Sanctum Access (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: has_light_suit(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sky Temple Gateway (Credits)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Sky Temple - Sanctum | Escape Started", player),
                not must_fight_dark_samus_3_4(state, player),
                has_enough_sky_temple_keys(state, player),
                # TODO: add suitless logic
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sky Temple Gateway (Dark Samus Fight)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Sky Temple - Sanctum | Escape Started", player),
                not must_fight_dark_samus_3_4(state, player),
                has_enough_sky_temple_keys(state, player),
                # TODO: add suitless logic
                has_light_suit(state, player),
            ]),
        ),
    ]