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
class MainGyroChamber(MetroidPrime2Region):
    name = "Main Gyro Chamber"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Dynamo Access",
            door=DoorCover.Dark,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Save Station B",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    # https://www.youtube.com/watch?v=qYFQpPuZhI4
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                    ]),
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Wall Boost"),
                    ]),
                ]),
            ]),
                state.has("Morph Ball", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Watch Station Access",
            door=DoorCover.Light,
            rule=lambda state, player: state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Spinner Gate", player),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Temple Access",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Spinner Gate", player),
                condition_or([
                state.has("Scan Visor", player),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Checkpoint Station",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                condition_and([
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Spinner Gate", player),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Wall Boost"),
                    ]),
                    can_lay_bomb(state, player),
                    # Works the same from all sides https://www.youtube.com/watch?v=qYFQpPuZhI4
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                can_use_boost_ball(state, player),
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Puzzle 2", player),
                condition_or([
                    can_use_spider_ball(state, player),
                    # Instant Morph -> https://youtu.be/d-yq4nqriDo?si=pCKZzyH7Q8yg6MUH
                    condition_and([
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        has_trick_enabled(state, player, "Instant Morph"),
                    ]),
                ]),
            ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Power Bomb Expansion)",
            can_access=lambda state, player: condition_and([
                state.has("Scan Visor", player),
                condition_and([
                state.has("Morph Ball", player),
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Echo Gate", player),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Main Gyro Chamber Puzzle 1",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Puzzle 1",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    # https://www.youtube.com/watch?v=qYFQpPuZhI4
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                    ]),
                    condition_and([
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Wall Boost"),
                    ]),
                ]),
            ]),
                state.has("Morph Ball", player),
            ]),
                condition_and([
                condition_or([
                    has_missile_count(state, player, 4),
                    can_use_power_beam(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Knowledge"),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                    ]),
                    # https://www.youtube.com/watch?v=u1EZwK9MrpU
                    condition_and([
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                        has_dark_ammo(state, player, 60),
                        state.has("Charge Beam", player),
                        has_missile_count(state, player, 10),
                        condition_or([
                            condition_and([
                                can_use_dark_beam(state, player),
                                can_use_darkburst(state, player),
                            ]),
                            condition_and([
                                can_use_annihilator_beam(state, player),
                                has_light_ammo(state, player, 60),
                                can_use_sonic_boom(state, player),
                            ]),
                        ]),
                        state.has("Space Jump Boots", player),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Main Gyro Chamber Puzzle 2",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Puzzle 2",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                condition_and([
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Spinner Gate", player),
                condition_or([
                state.has("Scan Visor", player),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_pb(state, player),
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Knowledge"),
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Puzzle 1", player),
                condition_or([
                    can_use_power_beam(state, player),
                    has_missile_count(state, player, 7),
                    condition_and([
                        has_trick_enabled(state, player, "Knowledge"),
                        can_use_screw_attack(state, player),
                    ]),
                ]),
                condition_or([
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                    ]),
                    # https://www.youtube.com/watch?v=ZAXCWoJlxfM
                    condition_and([
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                        state.has("Space Jump Boots", player),
                        has_dark_ammo(state, player, 60),
                        state.has("Charge Beam", player),
                        condition_or([
                            condition_and([
                                can_use_dark_beam(state, player),
                                can_use_darkburst(state, player),
                            ]),
                            condition_and([
                                can_use_annihilator_beam(state, player),
                                has_light_ammo(state, player, 60),
                                can_use_sonic_boom(state, player),
                            ]),
                        ]),
                        has_missile_count(state, player, 10),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Main Gyro Chamber Echo Gate",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Echo Gate",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Scan Visor", player),
                condition_and([
                can_use_annihilator_beam(state, player),
                state.has("Echo Visor", player),
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Puzzle 2", player),
                condition_or([
                    state.has("Charge Beam", player),
                    condition_and([
                        has_dark_ammo(state, player, 4),
                        has_light_ammo(state, player, 4),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Main Gyro Chamber Spinner Gate",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Spinner Gate",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Sanctuary Fortress - Main Gyro Chamber | Event - Main Gyro Chamber Spinner Gate", player),
                condition_and([
                state.has("Morph Ball", player),
                can_use_boost_ball(state, player),
            ]),
            ]),
        )
