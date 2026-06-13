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
class JudgmentPit(MetroidPrime2Region):
    name = "Judgment Pit"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Agon Wastes - Dark Agon Temple Access",
            door=DoorCover.Missile,
            rule=lambda state, player: condition_or([
                condition_and([
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
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
                condition_or([
                # https://www.youtube.com/watch?v=9ldu-Rh8DOQ
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
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
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Standable Terrain"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
                # https://www.youtube.com/watch?v=9ldu-Rh8DOQ&t=39s
            condition_and([
                can_use_screw_attack(state, player, z_axis=True),
                has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                not (False),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Agon Wastes - Save Station 1",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_and([
                condition_and([
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
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
                condition_or([
                # https://www.youtube.com/watch?v=9ldu-Rh8DOQ
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
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
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Standable Terrain"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                            can_activate_safe_zone(state, player),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=9ldu-Rh8DOQ&t=8s
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
                        condition_or([
                            can_activate_safe_zone(state, player),
                            condition_or([
                                has_dark_suit(state, player),
                                has_light_suit(state, player),
                                state.count("Energy Tank", player) >= 1,
                            ]),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=9ldu-Rh8DOQ&t=39s
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                        condition_or([
                            can_activate_safe_zone(state, player),
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
        ),
        MetroidPrime2Exit(
            destination="Dark Agon Wastes - Warrior's Walk",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: condition_and([
                condition_and([
                condition_and([
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
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
                condition_or([
                # https://www.youtube.com/watch?v=9ldu-Rh8DOQ
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
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
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Standable Terrain"),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
            ]),
                # https://www.youtube.com/watch?v=9ldu-Rh8DOQ&t=39s
            condition_and([
                can_use_screw_attack(state, player, z_axis=True),
                has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                not (False),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
            ]),
                condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=C8FZgsHFKw8
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
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
            destination="Dark Agon Wastes - Portal Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
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
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
                condition_or([
                # https://www.youtube.com/watch?v=9ldu-Rh8DOQ
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
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
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Standable Terrain"),
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
            destination="Dark Agon Wastes - Junction Site",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Space Jump Boots)",
            can_access=lambda state, player: condition_or([
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
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Jump Guardian",
            locked_item=MetroidPrime2Item(
                name="Dark Agon Wastes - Judgment Pit | Event - Jump Guardian",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
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
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
            ]),
        )
