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
class CullingChamber(MetroidPrime2Region):
    name = "Culling Chamber"
    exits_ = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hazing Cliff",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Unseen Way",
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
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    condition_and([
                        state.has("Morph Ball", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    condition_and([
                        state.has("Morph Ball", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
            ]),
                condition_or([
                condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                condition_and([
                    state.has("Morph Ball", player),
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
            rule=lambda state, player: condition_and([
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    condition_and([
                        state.has("Morph Ball", player),
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
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Hall of Combat Mastery",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Ing Hive Key 1)",
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
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    condition_and([
                        state.has("Morph Ball", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_use_spider_ball(state, player),
                can_lay_bomb(state, player),
                can_activate_safe_zone(state, player),
                condition_or([
                    # https://www.youtube.com/watch?v=gSKWrUk5uM4
                    condition_and([
                        condition_or([
                                condition_or([has_dark_suit(state, player), has_light_suit(state, player)]),
                                has_trick_enabled(state, player, "Suitless Dark Aether"),
                            ]),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        condition_or([
                            condition_and([
                                can_use_boost_ball(state, player),
                                has_trick_enabled(state, player, "Movement"),
                            ]),
                            condition_and([
                                state.has("Ing Hive - Culling Chamber | Event - Culling Chamber Blocks", player),
                                has_trick_enabled(state, player, "Movement"),
                            ]),
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
        )

        self.add_location(
            name="Event - Culling Chamber Blocks",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Culling Chamber | Event - Culling Chamber Blocks",
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
                condition_and([
                can_activate_safe_zone(state, player),
                condition_or([
                    condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    condition_and([
                        state.has("Morph Ball", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                can_activate_safe_zone(state, player),
                state.has("Morph Ball", player),
                can_lay_bomb(state, player),
                can_use_spider_ball(state, player),
                has_trick_enabled(state, player, "Movement"),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
            ]),
        )
