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
class AgonTemple(MetroidPrime2Region):
    name = "Agon Temple"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Mine Shaft",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_or([
                # Double Bomb Jump
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Movement"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Temple Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Controller Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                # Double Bomb Jump
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Movement"),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Sandcanyon",
            door=DoorCover.Light,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Morph Ball Bomb)",
            can_access=lambda state, player: condition_and([
                condition_or([
                state.has("Space Jump Boots", player),
                not (state.has("Agon Wastes - Agon Temple | Event - Bomb Guardian", player)),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        can_lay_bomb(state, player),
                        can_lay_pb(state, player),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Knowledge"),
                    condition_or([
                        can_use_screw_attack(state, player),
                        condition_and([
                            state.has("Morph Ball", player),
                            can_use_boost_ball(state, player),
                        ]),
                        condition_and([
                            can_use_screw_attack(state, player, z_axis=True),
                            has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                            not (False),
                        ]),
                    ]),
                ]),
            ]),
                # Bomb Guardian - 160HP for the head - 52HP to stun the tail
            condition_or([
                can_use_power_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Combat"),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            can_lay_pb(state, player),
                        ]),
                        has_missile_count(state, player, 15),
                    ]),
                ]),
                # 2 charged dark shots to the tail, then 4 charged dark shots to the head: https://youtu.be/yaISvZXNLTw
                condition_and([
                    has_trick_enabled(state, player, "Combat"),
                    state.has("Charge Beam", player),
                    can_use_dark_beam(state, player),
                    has_dark_ammo(state, player, 31),
                ]),
                # Screw Attack the head during an attack animation, cannot stun the tail
                condition_and([
                    has_trick_enabled(state, player, "Combat"),
                    condition_or([
                        can_use_screw_attack(state, player),
                        # https://youtu.be/9W1__s4ABFw
                        condition_and([
                            can_use_screw_attack(state, player, z_axis=True),
                            not (False),
                            has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        ]),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Bomb Guardian",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Agon Temple | Event - Bomb Guardian",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                state.has("Space Jump Boots", player),
                not (state.has("Agon Wastes - Agon Temple | Event - Bomb Guardian", player)),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        can_lay_bomb(state, player),
                        can_lay_pb(state, player),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Knowledge"),
                    condition_or([
                        can_use_screw_attack(state, player),
                        condition_and([
                            state.has("Morph Ball", player),
                            can_use_boost_ball(state, player),
                        ]),
                        condition_and([
                            can_use_screw_attack(state, player, z_axis=True),
                            has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                            not (False),
                        ]),
                    ]),
                ]),
            ]),
                # Bomb Guardian - 160HP for the head - 52HP to stun the tail
            condition_or([
                can_use_power_beam(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Combat"),
                    condition_or([
                        condition_and([
                            state.has("Morph Ball", player),
                            can_lay_pb(state, player),
                        ]),
                        has_missile_count(state, player, 15),
                    ]),
                ]),
                # 2 charged dark shots to the tail, then 4 charged dark shots to the head: https://youtu.be/yaISvZXNLTw
                condition_and([
                    has_trick_enabled(state, player, "Combat"),
                    state.has("Charge Beam", player),
                    can_use_dark_beam(state, player),
                    has_dark_ammo(state, player, 31),
                ]),
                # Screw Attack the head during an attack animation, cannot stun the tail
                condition_and([
                    has_trick_enabled(state, player, "Combat"),
                    condition_or([
                        can_use_screw_attack(state, player),
                        # https://youtu.be/9W1__s4ABFw
                        condition_and([
                            can_use_screw_attack(state, player, z_axis=True),
                            not (False),
                            has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        ]),
                    ]),
                ]),
            ]),
            ]),
        )
