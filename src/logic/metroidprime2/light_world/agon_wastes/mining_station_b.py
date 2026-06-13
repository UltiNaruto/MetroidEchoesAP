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
class MiningStationB(MetroidPrime2Region):
    name = "Mining Station B"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Storage A",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                can_lay_pb(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transit Station",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Mine Shaft",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    state.has("Morph Ball", player),
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=OOliuV6E6s4
                    condition_or([
                        has_trick_enabled(state, player, "Standable Terrain"),
                        has_trick_enabled(state, player, "Slope Jump"),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Trial Grounds",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                # https://www.youtube.com/watch?v=RAVTrB3Mhrs
            condition_and([
                state.has("Space Jump Boots", player),
                state.has("Scan Visor", player),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                has_trick_enabled(state, player, "Standable Terrain"),
                has_trick_enabled(state, player, "Single Room Out of Bounds"),
            ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Darkburst)",
            can_access=lambda state, player: True,
        )

        self.add_location(
            name="Event - Mining Station B Portal Opened",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Mining Station B | Event - Mining Station B Portal Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_lay_bomb(state, player),
                        condition_or([
                            state.has("Scan Visor", player),
                            condition_and([
                                has_trick_enabled(state, player, "Standable Terrain"),
                                can_use_screw_attack(state, player),
                            ]),
                            condition_and([
                                state.has("Space Jump Boots", player),
                                has_trick_enabled(state, player, "Slope Jump"),
                            ]),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=CvU0QLIgzms
                    condition_and([
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                        has_trick_enabled(state, player, "Movement"),
                        condition_or([
                            condition_and([
                                can_use_boost_ball(state, player),
                                has_trick_enabled(state, player, "Wall Boost"),
                            ]),
                            has_trick_enabled(state, player, "Instant Morph"),
                        ]),
                        condition_and([
                            condition_or([
                                can_use_darkburst(state, player),
                                condition_and([
                                    can_use_sonic_boom(state, player),
                                    has_light_ammo(state, player, 60),
                                ]),
                            ]),
                            has_dark_ammo(state, player, 60),
                            has_missile_count(state, player, 10),
                        ]),
                        state.has("Scan Visor", player),
                    ]),
                ]),
            ]),
        )
