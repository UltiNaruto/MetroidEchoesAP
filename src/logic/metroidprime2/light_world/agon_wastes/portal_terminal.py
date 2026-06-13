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
class PortalTerminal(MetroidPrime2Region):
    name = "Portal Terminal"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport Center",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Dark Agon Wastes - Portal Site | Event - Portal Site Gate", player),
        ),
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Portal Site",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                ]),
                # https://www.youtube.com/watch?v=mTvERL0H_NI
                condition_and([
                    condition_and([can_use_boost_ball(state, player), state.has('Space Jump Boots', player)]),
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                    has_trick_enabled(state, player, "Knowledge"),
                ]),
                # https://www.youtube.com/watch?v=KKoOubP1P7g
                condition_and([
                    can_use_boost_ball(state, player),
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                    has_trick_enabled(state, player, "Slope Jump"),
                    has_trick_enabled(state, player, "Standable Terrain"),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    has_trick_enabled(state, player, "Knowledge"),
                    not (False),
                ]),
            ]),
            ]),
        ),
    ]
