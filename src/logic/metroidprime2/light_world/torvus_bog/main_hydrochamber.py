from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_activate_dark_portal,
    can_activate_light_portal,
    can_activate_safe_zone,
    can_lay_bomb,
    can_lay_bomb_or_pb,
    can_lay_pb,
    can_use_annihilator_beam,
    can_use_boost_ball,
    can_use_charged_annihilator_beam,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_charged_power_beam,
    can_use_dark_beam,
    can_use_darkburst,
    can_use_grapple_beam,
    can_use_light_beam,
    can_use_power_beam,
    can_use_screw_attack,
    can_use_seeker_launcher,
    can_use_sonic_boom,
    can_use_spider_ball,
    can_use_sunburst,
    can_use_super_missile,
    has_dark_ammo,
    has_dark_suit,
    has_light_ammo,
    has_light_suit,
    has_missile_count,
    has_pb_count,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


# REVIEW: asymmetric intra-room traversal detected — consider splitting into sub-regions
class MainHydrochamber(MetroidPrime2Region):
    name = "Main Hydrochamber"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrochamber Storage",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Undertemple",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    not (state.has("Torvus Bog - Hydrochamber Storage | Event - Hydrochamber Storage Item", player)),
                    state.has("Torvus Bog - Main Hydrochamber | Event - Alpha Blogg", player),
                ]),
                condition_or([
                    can_use_spider_ball(state, player),
                    # https://www.youtube.com/watch?v=KPs8MIRVY-I
                    condition_and([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player),
                        state.has("Gravity Boost", player),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                condition_and([
                    can_use_screw_attack(state, player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Air Underwater"),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    condition_or([
                        state.has("Torvus Bog - Main Hydrochamber | Event - Alpha Blogg", player),
                        not (state.has("Torvus Bog - Hydrochamber Storage | Event - Hydrochamber Storage Item", player)),
                    ]),
                ]),
                condition_and([
                    state.has("Gravity Boost", player),
                    condition_or([
                        condition_and([
                            state.has("Torvus Bog - Main Hydrochamber | Event - Alpha Blogg", player),
                            condition_or([
                                # https://www.youtube.com/watch?v=tDa-PxtRTzo
                                condition_and([
                                    state.has("Morph Ball", player),
                                    has_trick_enabled(state, player, "Roll Jump"),
                                ]),
                                state.has("Space Jump Boots", player),
                            ]),
                        ]),
                        # https://www.youtube.com/watch?v=uUtdWkXB2BY
                        condition_and([
                            not (state.has("Torvus Bog - Hydrochamber Storage | Event - Hydrochamber Storage Item", player)),
                            has_trick_enabled(state, player, "Standable Terrain"),
                        ]),
                        condition_and([
                            state.has("Torvus Bog - Hydrochamber Storage | Event - Hydrochamber Storage Item", player),
                            state.has("Morph Ball", player),
                            can_lay_bomb(state, player),
                            condition_or([
                                condition_and([
                                    state.has("Space Jump Boots", player),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                ]),
                                has_trick_enabled(state, player, "Bomb Space Jump"),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Event - Alpha Blogg",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Main Hydrochamber | Event - Alpha Blogg",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Torvus Bog - Hydrochamber Storage | Event - Hydrochamber Storage Item", player),
                condition_or([
                    condition_and([
                        condition_or([
                            has_trick_enabled(state, player, "Combat"),
                            state.has("Gravity Boost", player),
                        ]),
                        condition_or([
                            condition_and([
                                can_use_power_beam(state, player),
                                state.has("Charge Beam", player),
                                has_missile_count(state, player, 25),
                                can_use_super_missile(state, player),
                            ]),
                            condition_and([
                                has_missile_count(state, player, 27),
                                can_use_seeker_launcher(state, player),
                            ]),
                            condition_and([
                                can_use_dark_beam(state, player),
                                has_dark_ammo(state, player, 37),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        condition_or([
                            has_trick_enabled(state, player, "Combat"),
                            condition_and([
                                state.has("Gravity Boost", player),
                                has_trick_enabled(state, player, "Combat"),
                            ]),
                        ]),
                        condition_or([
                            condition_and([
                                can_use_dark_beam(state, player),
                                has_dark_ammo(state, player, 27),
                            ]),
                            condition_and([
                                can_use_power_beam(state, player),
                                state.has("Charge Beam", player),
                                has_missile_count(state, player, 10),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        condition_or([
                            has_trick_enabled(state, player, "Combat"),
                            condition_and([
                                state.has("Gravity Boost", player),
                                has_trick_enabled(state, player, "Combat"),
                            ]),
                        ]),
                        condition_or([
                            has_missile_count(state, player, 27),
                            condition_and([
                                can_use_power_beam(state, player),
                                state.has("Charge Beam", player),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        )
