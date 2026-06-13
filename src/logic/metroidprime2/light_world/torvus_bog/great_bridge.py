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
class GreatBridge(MetroidPrime2Region):
    name = "Great Bridge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Map Station",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        # https://youtu.be/QXozKAHHqfI
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/MDuQCmnNc80
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
                condition_and([
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Slope Jump"),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Access",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_and([
                condition_and([
                condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        # https://youtu.be/QXozKAHHqfI
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/MDuQCmnNc80
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    # https://www.youtube.com/watch?v=TCaFF6E7RRM No Space Jump
                    condition_or([
                        # https://www.youtube.com/watch?v=1mSdHR_z4fw
                        condition_and([
                            state.has("Space Jump Boots", player),
                            has_trick_enabled(state, player, "Bomb Space Jump"),
                        ]),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                ]),
                # https://www.youtube.com/watch?v=dyWwRC0fq7Q
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                # https://www.youtube.com/watch?v=-Z7y1qUeubw
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
            ]),
                condition_or([
                can_use_screw_attack(state, player),
                # https://youtu.be/4nglOQXAFuk
                condition_and([
                    state.has("Space Jump Boots", player),
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        # https://youtu.be/QXozKAHHqfI
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/MDuQCmnNc80
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    # https://www.youtube.com/watch?v=TCaFF6E7RRM No Space Jump
                    condition_or([
                        # https://www.youtube.com/watch?v=1mSdHR_z4fw
                        condition_and([
                            state.has("Space Jump Boots", player),
                            has_trick_enabled(state, player, "Bomb Space Jump"),
                        ]),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                ]),
                # https://www.youtube.com/watch?v=dyWwRC0fq7Q
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                # https://www.youtube.com/watch?v=-Z7y1qUeubw
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Light)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        # https://youtu.be/QXozKAHHqfI
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/MDuQCmnNc80
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        # https://youtu.be/QXozKAHHqfI
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/MDuQCmnNc80
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Power Bomb Expansion)",
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        # https://youtu.be/QXozKAHHqfI
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/MDuQCmnNc80
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    # https://www.youtube.com/watch?v=TCaFF6E7RRM No Space Jump
                    condition_or([
                        # https://www.youtube.com/watch?v=1mSdHR_z4fw
                        condition_and([
                            state.has("Space Jump Boots", player),
                            has_trick_enabled(state, player, "Bomb Space Jump"),
                        ]),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                ]),
                # https://www.youtube.com/watch?v=dyWwRC0fq7Q
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                # https://www.youtube.com/watch?v=-Z7y1qUeubw
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_lay_pb(state, player),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Great Bridge Cannon",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Great Bridge | Event - Great Bridge Cannon",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        # https://youtu.be/QXozKAHHqfI
                        condition_and([
                            can_use_boost_ball(state, player),
                            has_trick_enabled(state, player, "Wall Boost"),
                        ]),
                        # Double Bomb Jump
                        condition_and([
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Jump"),
                        ]),
                    ]),
                ]),
                # https://youtu.be/MDuQCmnNc80
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
                condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                    # https://www.youtube.com/watch?v=TCaFF6E7RRM No Space Jump
                    condition_or([
                        # https://www.youtube.com/watch?v=1mSdHR_z4fw
                        condition_and([
                            state.has("Space Jump Boots", player),
                            has_trick_enabled(state, player, "Bomb Space Jump"),
                        ]),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                    ]),
                ]),
                # https://www.youtube.com/watch?v=dyWwRC0fq7Q
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                # https://www.youtube.com/watch?v=-Z7y1qUeubw
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Slope Jump"),
                ]),
            ]),
            ]),
                state.has("Scan Visor", player),
            ]),
        )
