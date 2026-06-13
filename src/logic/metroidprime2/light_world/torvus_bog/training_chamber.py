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
class TrainingChamber(MetroidPrime2Region):
    name = "Training Chamber"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                state.has("Scan Visor", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Training Chamber | Event - Training Chamber Statue", player),
                state.has("Morph Ball", player),
                condition_or([
                    can_use_spider_ball(state, player),
                    condition_and([
                        state.has("Gravity Boost", player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                state.has("Scan Visor", player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: state.has("Torvus Bog - Training Chamber | Event - Training Chamber Statue", player),
        )

        self.add_location(
            name="Event - Training Chamber Statue",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Training Chamber | Event - Training Chamber Statue",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                can_use_screw_attack(state, player),
                condition_and([
                    state.has("Space Jump Boots", player),
                    state.has("Scan Visor", player),
                    condition_or([
                        condition_and([
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                            has_trick_enabled(state, player, "Standable Terrain"),
                            has_trick_enabled(state, player, "Underwater Dash"),
                            state.has("Morph Ball", player),
                            can_use_spider_ball(state, player),
                            has_trick_enabled(state, player, "Instant Morph"),
                            can_lay_bomb(state, player),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                            state.has("Torvus Bog - Training Chamber | Event - Training Chamber Statue", player),
                        ]),
                        # https://www.youtube.com/watch?v=El7ReUe6WEE
                        has_trick_enabled(state, player, "Extended Dash"),
                    ]),
                ]),
                # https://youtu.be/LgeZpkGDQjw
                condition_and([
                    state.has("Morph Ball", player),
                    state.has("Gravity Boost", player),
                    condition_or([
                        has_trick_enabled(state, player, "Air Underwater"),
                        condition_and([
                            state.has("Space Jump Boots", player),
                            has_trick_enabled(state, player, "Air Underwater"),
                        ]),
                    ]),
                ]),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                ]),
                # https://www.youtube.com/watch?v=I7DVJ3KwI3w
                condition_and([
                    can_use_boost_ball(state, player),
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Wall Boost"),
                    has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                ]),
            ]),
            ]),
        )
