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
class HiveTemple(MetroidPrime2Region):
    name = "Hive Temple"
    exits_ = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Controller Access",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                condition_and([
                can_use_screw_attack(state, player),
                state.has("Ing Hive - Hive Temple | Event - Quadraxis", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                condition_or([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=9SOVgXKKAyY
                    condition_and([
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                    ]),
                ]),
            ]),
                condition_and([
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                state.has("Ing Hive - Hive Temple | Event - Quadraxis", player),
                condition_or([
                    can_use_screw_attack(state, player),
                    # https://www.youtube.com/watch?v=9SOVgXKKAyY
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                    ]),
                    # https://www.youtube.com/watch?v=K7btnz2qmsg
                    condition_and([
                        state.has("Space Jump Boots", player),
                        state.has("Scan Visor", player),
                        has_trick_enabled(state, player, "Extended Dash"),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                condition_and([
                can_use_screw_attack(state, player),
                state.has("Ing Hive - Hive Temple | Event - Quadraxis", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                condition_or([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=9SOVgXKKAyY
                    condition_and([
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                    ]),
                ]),
            ]),
                condition_and([
                state.has("Ing Hive - Hive Temple | Event - Quadraxis", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                condition_or([
                    condition_and([
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_or([
                            can_use_screw_attack(state, player),
                            # https://www.youtube.com/watch?v=9SOVgXKKAyY
                            condition_and([
                                can_use_screw_attack(state, player, z_axis=True),
                                has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                                not (False),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        state.has("Scan Visor", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        condition_or([
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                            has_trick_enabled(state, player, "Extended Dash"),
                            # Works the same as: (Lock on Blue/Anni Door) -> https://www.youtube.com/watch?v=K7btnz2qmsg&t=20s
                            has_trick_enabled(state, player, "Extended Dash"),
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
            name="Pickup (Annihilator Beam)",
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        can_lay_pb(state, player, 2),
                        has_trick_enabled(state, player, "Knowledge"),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_use_spider_ball(state, player),
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Charge Beam", player),
                        condition_or([
                            condition_and([
                                can_use_light_beam(state, player),
                                has_light_ammo(state, player, 50),
                                has_trick_enabled(state, player, "Combat"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Combat"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        condition_or([has_dark_suit(state, player), has_light_suit(state, player)]),
                        state.has("Charge Beam", player),
                        condition_or([
                            condition_and([
                                can_use_light_beam(state, player),
                                has_light_ammo(state, player, 50),
                            ]),
                            condition_and([
                                has_missile_count(state, player, 65),
                                can_use_super_missile(state, player),
                            ]),
                        ]),
                    ]),
                ]),
                condition_or([
                    state.has("Echo Visor", player),
                    has_trick_enabled(state, player, "Invisible Objects"),
                ]),
            ]),
            ]),
                condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
            ]),
        )

        self.add_location(
            name="Event - Quadraxis",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Temple | Event - Quadraxis",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        can_lay_pb(state, player, 2),
                        has_trick_enabled(state, player, "Knowledge"),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_use_spider_ball(state, player),
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Charge Beam", player),
                        condition_or([
                            condition_and([
                                can_use_light_beam(state, player),
                                has_light_ammo(state, player, 50),
                                has_trick_enabled(state, player, "Combat"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Combat"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        condition_or([has_dark_suit(state, player), has_light_suit(state, player)]),
                        state.has("Charge Beam", player),
                        condition_or([
                            condition_and([
                                can_use_light_beam(state, player),
                                has_light_ammo(state, player, 50),
                            ]),
                            condition_and([
                                has_missile_count(state, player, 65),
                                can_use_super_missile(state, player),
                            ]),
                        ]),
                    ]),
                ]),
                condition_or([
                    state.has("Echo Visor", player),
                    has_trick_enabled(state, player, "Invisible Objects"),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Prepare Elevator Before Fight",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Temple | Event - Prepare Elevator Before Fight",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
        )

        self.add_location(
            name="Event - Prepare Elevator After Fight",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Temple | Event - Prepare Elevator After Fight",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        can_lay_pb(state, player, 2),
                        has_trick_enabled(state, player, "Knowledge"),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_use_spider_ball(state, player),
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Charge Beam", player),
                        condition_or([
                            condition_and([
                                can_use_light_beam(state, player),
                                has_light_ammo(state, player, 50),
                                has_trick_enabled(state, player, "Combat"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                            condition_and([
                                has_trick_enabled(state, player, "Combat"),
                                condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        condition_or([has_dark_suit(state, player), has_light_suit(state, player)]),
                        state.has("Charge Beam", player),
                        condition_or([
                            condition_and([
                                can_use_light_beam(state, player),
                                has_light_ammo(state, player, 50),
                            ]),
                            condition_and([
                                has_missile_count(state, player, 65),
                                can_use_super_missile(state, player),
                            ]),
                        ]),
                    ]),
                ]),
                condition_or([
                    state.has("Echo Visor", player),
                    has_trick_enabled(state, player, "Invisible Objects"),
                ]),
            ]),
            ]),
                condition_and([
                can_use_screw_attack(state, player),
                has_trick_enabled(state, player, "Standable Terrain"),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
            ]),
        )
