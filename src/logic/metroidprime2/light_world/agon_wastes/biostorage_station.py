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
class BiostorageStation(MetroidPrime2Region):
    name = "Biostorage Station"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Security Station A",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.has("Scan Visor", player),
                # https://www.youtube.com/watch?v=Pnm3-uD9BeM
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Standable Terrain"),
                ]),
                # https://www.youtube.com/watch?v=vScEQWXSHKw
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Biostorage Access",
            door=DoorCover.Missile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Storage B",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_or([
                state.has("Scan Visor", player),
                # https://www.youtube.com/watch?v=Pnm3-uD9BeM
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Standable Terrain"),
                ]),
                # https://www.youtube.com/watch?v=vScEQWXSHKw
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                ]),
            ]),
        ),
    ]
