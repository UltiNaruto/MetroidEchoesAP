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
class TempleSecurityAccess(MetroidPrime2Region):
    name = "Temple Security Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Ing Hive - Aerial Training Site",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Ing Hive - Temple Security Access | Event - Temple Security Access Gates", player),
                state.has("Morph Ball", player),
                False,
                condition_or([
                    condition_and([
                        can_lay_bomb(state, player),
                        condition_or([
                            has_light_suit(state, player),
                            condition_and([
                                has_trick_enabled(state, player, "Suitless Dark Aether"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=oWT_41KIE0E
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Wall Boost"),
                        condition_or([
                            has_light_suit(state, player),
                            condition_and([
                                has_trick_enabled(state, player, "Suitless Dark Aether"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player),
                        condition_or([
                            # https://www.youtube.com/watch?v=2c9fDMqBWy8
                            condition_and([
                                state.has("Space Jump Boots", player),
                                has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                                condition_or([
                                    has_light_suit(state, player),
                                    condition_and([
                                        has_trick_enabled(state, player, "Suitless Dark Aether"),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                    ]),
                                ]),
                            ]),
                            # https://www.youtube.com/watch?v=sGIG5aaPkNM
                            condition_and([
                                condition_or([
                                    has_light_suit(state, player),
                                    condition_and([
                                        has_trick_enabled(state, player, "Suitless Dark Aether"),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                    ]),
                                ]),
                                has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
                condition_and([
                state.has("Ing Hive - Temple Security Access | Event - Temple Security Access Gates", player),
                state.has("Morph Ball", player),
                False,
                condition_or([
                    condition_and([
                        can_lay_bomb(state, player),
                        condition_or([
                            has_light_suit(state, player),
                            condition_and([
                                has_trick_enabled(state, player, "Suitless Dark Aether"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=oWT_41KIE0E
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Wall Boost"),
                        condition_or([
                            has_light_suit(state, player),
                            condition_and([
                                has_trick_enabled(state, player, "Suitless Dark Aether"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player),
                        condition_or([
                            # https://www.youtube.com/watch?v=2c9fDMqBWy8
                            condition_and([
                                state.has("Space Jump Boots", player),
                                has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                                condition_or([
                                    has_light_suit(state, player),
                                    condition_and([
                                        has_trick_enabled(state, player, "Suitless Dark Aether"),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                    ]),
                                ]),
                            ]),
                            # https://www.youtube.com/watch?v=sGIG5aaPkNM
                            condition_and([
                                has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                                condition_or([
                                    has_light_suit(state, player),
                                    condition_and([
                                        has_trick_enabled(state, player, "Suitless Dark Aether"),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                        condition_or([
                                            has_dark_suit(state, player),
                                            has_light_suit(state, player),
                                            state.count("Energy Tank", player) >= 1,
                                        ]),
                                    ]),
                                ]),
                            ]),
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
            name="Event - Temple Security Access Gates",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Temple Security Access | Event - Temple Security Access Gates",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True,
        )
