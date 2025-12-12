from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_lay_bomb,
    can_lay_pb,
    can_use_annihilator_beam,
    can_use_boost_ball,
    can_use_dark_beam,
    can_use_light_beam,
    can_use_power_beam,
    can_use_screw_attack,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TempleSanctuary_Center(MetroidPrime2Region):
    name = "Temple Sanctuary"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Controller Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Temple Sanctuary | Alpha Splinter Defeated", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Transport A Side)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: state.has("Great Temple - Temple Sanctuary | Alpha Splinter Defeated", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Transport B Side)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: state.has("Great Temple - Temple Sanctuary | Alpha Splinter Defeated", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Transport C Side)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: state.has("Great Temple - Temple Sanctuary | Alpha Splinter Defeated", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Alpha Splinter Defeated",
            locked_item=MetroidPrime2Item(
                name="Great Temple - Temple Sanctuary | Alpha Splinter Defeated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
                can_use_power_beam(state, player),
                can_use_dark_beam(state, player),
                can_use_light_beam(state, player),
                can_use_annihilator_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Bombs"),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Boost Ball"),
                    can_use_boost_ball(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Power Bomb"),
                    can_lay_pb(state, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Screw Attack and SJ"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        )
        self.add_location(
            name="Pickup (Energy Transfer Module)",
            can_access=lambda state, player: state.has("Great Temple - Temple Sanctuary | Alpha Splinter Defeated", player),
        )


class TempleSanctuary_ControllerSide(MetroidPrime2Region):
    name = "Temple Sanctuary"
    desc = "Controller Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Great Temple - Controller Transport (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
    ]


class TempleSanctuary_TransportASide(MetroidPrime2Region):
    name = "Temple Sanctuary"
    desc = "Transport A Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Great Temple - Transport A Access (Temple Sanctuary Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Center)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: True,
        ),
    ]


class TempleSanctuary_TransportBSide(MetroidPrime2Region):
    name = "Temple Sanctuary"
    desc = "Transport B Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Great Temple - Transport B Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Center)",
            door=DoorCover.VioletTranslator,
            rule=lambda state, player: True,
        ),
    ]


class TempleSanctuary_TransportCSide(MetroidPrime2Region):
    name = "Temple Sanctuary"
    desc = "Transport C Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Great Temple - Transport C Access (Temple Sanctuary Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Temple Sanctuary (Center)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
    ]