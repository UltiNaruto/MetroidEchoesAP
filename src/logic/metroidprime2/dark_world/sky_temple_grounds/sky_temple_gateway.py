from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_safe_zone,
    can_use_charged_annihilator_beam,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_charged_power_beam,
    has_dark_suit,
    has_enough_sky_temple_keys,
    has_light_suit,
    has_trick_enabled,
    must_fight_dark_samus_3_4,
    must_fight_emperor_ing,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class SkyTempleGateway(MetroidPrime2Region):
    name = "Sky Temple Gateway"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sky Temple Gateway (Gateway Access Side)",
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
            destination="Sky Temple Grounds - Sky Temple Gateway (Dark Samus Fight)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                not must_fight_emperor_ing(state, player),
                must_fight_dark_samus_3_4(state, player),
                has_enough_sky_temple_keys(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple - Sky Temple Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                must_fight_emperor_ing(state, player),
                has_enough_sky_temple_keys(state, player),
                # TODO: add suitless logic
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sky Temple Gateway (Credits)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                not must_fight_emperor_ing(state, player),
                not must_fight_dark_samus_3_4(state, player),
                has_enough_sky_temple_keys(state, player),
            ]),
        ),
    ]


class SkyTempleGateway_Credits(MetroidPrime2Region):
    name = "Sky Temple Gateway"
    desc = "Credits"

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Victory",
            locked_item=MetroidPrime2Item(
                name="Sky Temple Grounds - Sky Temple Gateway | Victory",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True,
        )


class SkyTempleGateway_DarkSamusFight(MetroidPrime2Region):
    name = "Sky Temple Gateway"
    desc = "Dark Samus Fight"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sky Temple Gateway (Credits)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Sky Temple Grounds - Sky Temple Gateway | Dark Samus 3/4 Defeated", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Dark Samus 3/4 Defeated",
            locked_item=MetroidPrime2Item(
                name="Sky Temple Grounds - Sky Temple Gateway | Dark Samus 3/4 Defeated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                    can_use_charged_power_beam(state, player),
                    can_use_charged_dark_beam(state, player),
                    can_use_charged_light_beam(state, player),
                    can_use_charged_annihilator_beam(state, player),
                ]),
                condition_or([
                    state.has("Echo Visor", player),
                    has_trick_enabled(state, player, "Sky Temple Grounds - Sky Temple Gateway | Dark Samus Fight without Echo Visor"),
                ]),
                # TODO: add no light suit logic
                has_light_suit(state, player),
            ]),
        )


class SkyTempleGateway_GatewayAccessSide(MetroidPrime2Region):
    name = "Sky Temple Gateway"
    desc = "Gateway Access Side"
    exits_ = [
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
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Sky Temple Gateway",
            door=DoorCover.Opened,
            # TODO: add suitless logic
            rule=lambda state, player: has_light_suit(state, player),
        ),
    ]