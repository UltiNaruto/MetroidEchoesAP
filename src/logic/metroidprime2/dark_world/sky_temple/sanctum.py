from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_lay_bomb_or_pb,
    can_use_charged_annihilator_beam,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_super_missile,
    can_use_screw_attack,
    can_use_spider_ball,
    has_light_suit,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class Sanctum(MetroidPrime2Region):
    name = "Sanctum"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sanctum (Emperor Ing 1)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 4,
            ]),
        ),
    ]


class Sanctum_EmperorIng1(MetroidPrime2Region):
    name = "Sanctum"
    desc = "Emperor Ing 1"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sanctum (Emperor Ing 2)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Sky Temple - Sanctum | Emperor Ing 1 Defeated", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Emperor Ing 1 Defeated",
                locked_item=MetroidPrime2Item(
                    name="Sky Temple - Sanctum | Emperor Ing 1 Defeated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_and([
                    has_light_suit(state, player),
                    can_use_super_missile(state, player),
                    can_use_charged_dark_beam(state, player),
                    can_use_charged_light_beam(state, player),
                    can_use_charged_annihilator_beam(state, player),
                ]),
                parent=self,
            ),
        ]


class Sanctum_EmperorIng2(MetroidPrime2Region):
    name = "Sanctum"
    desc = "Emperor Ing 2"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sanctum (Emperor Ing 3)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Sky Temple - Sanctum | Emperor Ing 2 Defeated", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Emperor Ing 2 Defeated",
                locked_item=MetroidPrime2Item(
                    name="Sky Temple - Sanctum | Emperor Ing 2 Defeated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_and([
                    has_light_suit(state, player),
                    can_use_spider_ball(state, player),
                    can_lay_bomb_or_pb(state, player, 4),
                ]),
                parent=self,
            ),
        ]


class Sanctum_EmperorIng3(MetroidPrime2Region):
    name = "Sanctum"
    desc = "Emperor Ing 3"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sanctum (Escape)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Sky Temple - Sanctum | Emperor Ing 3 Defeated", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Emperor Ing 3 Defeated",
                locked_item=MetroidPrime2Item(
                    name="Sky Temple - Sanctum | Emperor Ing 3 Defeated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_and([
                    has_light_suit(state, player),
                    condition_or([
                        condition_and([
                            has_trick_enabled(state, player, "Sky Temple - Sanctum | Emperor Ing 3 with SA"),
                            can_use_screw_attack(state, player),
                        ]),
                        condition_and([
                            can_use_super_missile(state, player),
                            can_use_charged_dark_beam(state, player),
                            can_use_charged_light_beam(state, player),
                            can_use_charged_annihilator_beam(state, player),
                        ]),
                    ]),
                ]),
                parent=self,
            ),
        ]


class Sanctum_Escape(MetroidPrime2Region):
    name = "Sanctum"
    desc = "Escape"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sanctum Access (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Sky Temple - Sanctum | Escape Started", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Escape Started",
                locked_item=MetroidPrime2Item(
                    name="Sky Temple - Sanctum | Escape Started",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Sky Temple - Sanctum | Escape with Z-Axis SA"),
                        can_use_screw_attack(state, player, z_axis=True),
                    ]),
                ]),
                parent=self,
            ),
        ]