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
class Catacombs(MetroidPrime2Region):
    name = "Catacombs"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Dungeon",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    state.has("Gravity Boost", player),
                    has_trick_enabled(state, player, "Air Underwater"),
                ]),
                # https://www.youtube.com/watch?v=2M7rPNLelJo
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                condition_and([
                    state.has("Torvus Bog - Catacombs | Event - Catacombs Gate", player),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            has_trick_enabled(state, player, "Standable Terrain"),
                            condition_or([
                                can_use_screw_attack(state, player, z_axis=True),
                                has_trick_enabled(state, player, "Combat/Scan Dash"),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Standable Terrain"),
                    condition_or([
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        condition_and([
                            state.has("Scan Visor", player),
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                        ]),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Jump Off Enemy"),
                    state.has("Torvus Bog - Hydrochamber Storage | Event - Hydrochamber Storage Item", player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Event - Catacombs Gate",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Catacombs | Event - Catacombs Gate",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                    ]),
                    # https://youtu.be/CsXAvL3jah4?list=PLevfta9o_QKWuQNXAnmBXtzW4nmU5VLyN&t=8
                    condition_and([
                        condition_and([state.has('Morph Ball', player), can_lay_bomb(state, player)]),
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                        has_trick_enabled(state, player, "Instant Morph"),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Underwater Dash"),
                    ]),
                    state.has("Gravity Boost", player),
                    # https://www.youtube.com/watch?v=bxc5m5UbrFI
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Air Underwater"),
                    ]),
                ]),
            ]),
        )
