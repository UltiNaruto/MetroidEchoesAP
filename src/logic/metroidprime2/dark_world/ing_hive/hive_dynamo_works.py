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
class HiveDynamoWorks(MetroidPrime2Region):
    name = "Hive Dynamo Works"
    exits_ = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Dynamo Access",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_or([
                condition_and([
                    can_use_grapple_beam(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Boost Jump"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Scan Visor", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                        condition_and([
                            state.has("Morph Ball", player),
                            has_trick_enabled(state, player, "Roll Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/9N3PB7M4lzc?t=98
                condition_and([
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Extended Dash"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Dynamo Works",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                condition_and([
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_or([
                condition_and([
                    can_use_grapple_beam(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Boost Jump"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Scan Visor", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                        condition_and([
                            state.has("Morph Ball", player),
                            has_trick_enabled(state, player, "Roll Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/9N3PB7M4lzc?t=98
                condition_and([
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Extended Dash"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Ing Hive - Hive Dynamo Works | Event - Hive Dynamo Works Portal Barrier", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive East Transport",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Cache 3",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                condition_and([
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_or([
                condition_and([
                    can_use_grapple_beam(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Boost Jump"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Scan Visor", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                        condition_and([
                            state.has("Morph Ball", player),
                            has_trick_enabled(state, player, "Roll Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/9N3PB7M4lzc?t=98
                condition_and([
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Extended Dash"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
                # https://www.youtube.com/watch?v=KULUv9Ml7ws&t=16s
            condition_and([
                state.has("Dark Visor", player),
                has_trick_enabled(state, player, "Terminal Fall Abuse"),
                state.has("Morph Ball", player),
                condition_or([
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
                has_trick_enabled(state, player, "Single Room Out of Bounds"),
                not (False),
                not (False),
                can_use_light_beam(state, player),
            ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_use_spider_ball(state, player),
                        condition_or([
                            condition_or([
                                    has_dark_suit(state, player),
                                    has_light_suit(state, player),
                                    state.count("Energy Tank", player) >= 1,
                                ]),
                            condition_and([
                                has_trick_enabled(state, player, "Movement"),
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
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        state.has("Scan Visor", player),
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
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
            name="Pickup (Sky Temple Key 6)",
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_or([
                condition_and([
                    can_use_grapple_beam(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Boost Jump"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Scan Visor", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                        condition_and([
                            state.has("Morph Ball", player),
                            has_trick_enabled(state, player, "Roll Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/9N3PB7M4lzc?t=98
                condition_and([
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Extended Dash"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
                # https://www.youtube.com/watch?v=KULUv9Ml7ws&t=16s
            condition_and([
                state.has("Dark Visor", player),
                has_trick_enabled(state, player, "Terminal Fall Abuse"),
                state.has("Morph Ball", player),
                condition_or([
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
                has_trick_enabled(state, player, "Single Room Out of Bounds"),
                not (False),
                not (False),
                can_use_light_beam(state, player),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Hive Dynamo Works Portal Barrier",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Dynamo Works | Event - Hive Dynamo Works Portal Barrier",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_or([
                condition_and([
                    can_use_grapple_beam(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Boost Jump"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                    condition_or([
                        condition_and([
                            state.has("Scan Visor", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                        condition_and([
                            state.has("Morph Ball", player),
                            has_trick_enabled(state, player, "Roll Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/9N3PB7M4lzc?t=98
                condition_and([
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Extended Dash"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Dark Visor", player),
                can_use_seeker_launcher(state, player),
                has_missile_count(state, player, 5),
            ]),
            ]),
        )
