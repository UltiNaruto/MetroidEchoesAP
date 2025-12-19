from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_light_portal,
    can_use_boost_ball,
    can_use_screw_attack,
    can_use_seeker_launcher,
    has_missile_count,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class IngWindchamber_East(MetroidPrime2Region):
    name = "Ing Windchamber"
    desc = "East"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (North)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Morph Ball", player),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
    ]


class IngWindchamber_Portal(MetroidPrime2Region):
    name = "Ing Windchamber"
    # alternatively called South
    desc = "Portal"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Temple Grounds - Grand Windchamber (Windchamber Gateway Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_light_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (East)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Morph Ball", player),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (West)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="South Grapple Up",
            locked_item=MetroidPrime2Item(
                name="Sky Temple Grounds - Ing Windchamber | South Grapple Up",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.can_reach(spot="Sky Temple Grounds - Ing Windchamber (East)", player=player),
                state.can_reach(spot="Sky Temple Grounds - Ing Windchamber (West)", player=player),
                state.can_reach(spot="Sky Temple Grounds - Ing Windchamber (North)", player=player),
                can_use_boost_ball(state, player),
                can_use_seeker_launcher(state, player),
            ]),
        )


class IngWindchamber_North(MetroidPrime2Region):
    name = "Ing Windchamber"
    desc = "North"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (East)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (West)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Morph Ball", player),
                can_use_screw_attack(state, player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="North Grapple Up",
            locked_item=MetroidPrime2Item(
                name="Sky Temple Grounds - Ing Windchamber | North Grapple Up",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.can_reach(spot="Sky Temple Grounds - Ing Windchamber (East)", player=player),
                state.can_reach(spot="Sky Temple Grounds - Ing Windchamber (West)", player=player),
                # aka South
                state.can_reach(spot="Sky Temple Grounds - Ing Windchamber (Portal)", player=player),
                can_use_boost_ball(state, player),
                can_use_seeker_launcher(state, player),
            ]),
        )


class IngWindchamber_West(MetroidPrime2Region):
    name = "Ing Windchamber"
    desc = "West"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (North)",
            door=DoorCover.Opened,
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Ing Windchamber (Portal)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Morph Ball", player),
                can_use_screw_attack(state, player),
            ]),
        ),
    ]
