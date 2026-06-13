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


class HiveEntrance(MetroidPrime2Region):
    name = "Hive Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Ing Hive - Entrance Defense Hall",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Sky Temple Key 5)",
            can_access=lambda state, player: condition_and([
                state.has("Dark Visor", player),
                condition_or([
                    has_light_suit(state, player),
                    # https://www.youtube.com/watch?v=NUbKATjYJDc
                    condition_and([
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Single Room Out of Bounds"),
                        has_trick_enabled(state, player, "Bomb Jump"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        has_trick_enabled(state, player, "Terminal Fall Abuse"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Roll Jump"),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            # https://youtu.be/UFJToddgAMQ
                            condition_and([
                                has_trick_enabled(state, player, "Movement"),
                                has_trick_enabled(state, player, "Slope Jump"),
                            ]),
                            # https://www.youtube.com/watch?v=5318bW_bopY
                            condition_and([
                                can_lay_bomb(state, player),
                                has_trick_enabled(state, player, "Bomb Space Jump"),
                                has_trick_enabled(state, player, "Slope Jump"),
                            ]),
                        ]),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
                can_use_screw_attack(state, player),
            ]),
        )
