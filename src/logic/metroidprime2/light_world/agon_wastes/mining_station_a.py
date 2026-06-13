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
class MiningStationA(MetroidPrime2Region):
    name = "Mining Station A"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Temple Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                # https://www.youtube.com/watch?v=rWNazr6v578
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                has_missile_count(state, player, 1),
                condition_and([
                    state.has("Morph Ball", player),
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Boost Jump"),
                ]),
                # https://www.youtube.com/watch?v=ljIhZ5Ae6Lg
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                # https://www.youtube.com/watch?v=5j4pWnuojmc
                condition_and([
                    has_trick_enabled(state, player, "Extended Dash"),
                    state.has("Scan Visor", player),
                ]),
                # https://www.youtube.com/watch?v=Xlu62DIi4tY
                condition_and([
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    can_use_screw_attack(state, player, z_axis=True),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sand Cache",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Central Station Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has("Agon Wastes - Mining Station A | Event - Mining Station A Gate", player),
                condition_or([
                    # https://www.youtube.com/watch?v=vJ_MaFqBo0E
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
                    ]),
                    state.has("Space Jump Boots", player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mining Station Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Access A",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    # https://www.youtube.com/watch?v=oXg5O2Oa01Q
                    condition_and([
                        can_use_boost_ball(state, player),
                        can_lay_pb(state, player),
                        state.has("Dark Agon Wastes - Ing Cache 1 | Event - Agon Wastes Ing Cache 1 Pickup", player),
                        has_trick_enabled(state, player, "Jump Off Enemy"),
                    ]),
                    condition_and([
                        can_use_spider_ball(state, player),
                        can_lay_bomb(state, player),
                        can_lay_pb(state, player),
                    ]),
                    # https://www.youtube.com/watch?v=Z17kkmEA-HE
                    condition_and([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Mining Station A Gate",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Mining Station A | Event - Mining Station A Gate",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                # https://www.youtube.com/watch?v=j_kCNsjwzgI
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Jump"),
                ]),
                state.has("Space Jump Boots", player),
            ]),
                state.has("Scan Visor", player),
            ]),
        )
