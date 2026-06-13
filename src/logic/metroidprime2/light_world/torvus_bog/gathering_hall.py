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
class GatheringHall(MetroidPrime2Region):
    name = "Gathering Hall"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Crypt",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                state.has("Torvus Bog - Gathering Hall | Event - Gathering Hall Portal Gate", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                state.has("Gravity Boost", player),
                has_trick_enabled(state, player, "Air Underwater"),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Access",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_or([
                condition_or([
                    can_use_grapple_beam(state, player),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    state.has("Gravity Boost", player),
                    has_trick_enabled(state, player, "Air Underwater"),
                ]),
            ]),
                state.has("Morph Ball", player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                condition_or([
                condition_or([
                    can_use_grapple_beam(state, player),
                    can_use_screw_attack(state, player),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    state.has("Gravity Boost", player),
                    has_trick_enabled(state, player, "Air Underwater"),
                ]),
            ]),
                condition_and([
                state.has("Torvus Bog - Gathering Hall | Event - Gathering Hall Spider Puzzle", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Gathering Hall Water Drained",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Gathering Hall | Event - Gathering Hall Water Drained",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                can_lay_pb(state, player, 2),
            ]),
        )

        self.add_location(
            name="Event - Gathering Hall Portal Gate",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Gathering Hall | Event - Gathering Hall Portal Gate",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                state.has("Gravity Boost", player),
                has_trick_enabled(state, player, "Air Underwater"),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                ]),
                # https://www.youtube.com/watch?v=L5-1qlEnDBY
                condition_and([
                    condition_and([can_use_boost_ball(state, player), state.has('Space Jump Boots', player)]),
                    has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Gathering Hall Spider Puzzle",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Gathering Hall | Event - Gathering Hall Spider Puzzle",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    # https://www.youtube.com/watch?v=DSs_SAAp65s
                    condition_and([
                        condition_and([state.has('Morph Ball', player), can_lay_bomb(state, player)]),
                        has_light_ammo(state, player, 60),
                        has_dark_ammo(state, player, 60),
                        has_missile_count(state, player, 10),
                        has_trick_enabled(state, player, "Instant Morph"),
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        condition_or([
                            condition_and([
                                can_use_boost_ball(state, player),
                                can_use_spider_ball(state, player),
                            ]),
                            has_trick_enabled(state, player, "Instant Morph"),
                        ]),
                        condition_or([
                            condition_and([
                                can_use_screw_attack(state, player),
                                has_trick_enabled(state, player, "Standable Terrain"),
                            ]),
                            # https://www.youtube.com/watch?v=DtRteGK5390
                            condition_and([
                                state.has("Space Jump Boots", player),
                                state.has("Scan Visor", player),
                                has_trick_enabled(state, player, "Combat/Scan Dash"),
                                has_trick_enabled(state, player, "Roll Jump"),
                            ]),
                        ]),
                    ]),
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_use_spider_ball(state, player),
                        condition_or([
                            condition_and([
                                can_lay_bomb(state, player),
                                state.has("Torvus Bog - Gathering Hall | Event - Gathering Hall Water Drained", player),
                            ]),
                            # https://youtu.be/DtRteGK5390&t=6
                            condition_and([
                                has_trick_enabled(state, player, "Instant Morph"),
                                condition_or([
                                    state.has("Space Jump Boots", player),
                                    condition_and([
                                        state.has("Gravity Boost", player),
                                        not (state.has("Torvus Bog - Gathering Hall | Event - Gathering Hall Water Drained", player)),
                                        has_trick_enabled(state, player, "Air Underwater"),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        )
