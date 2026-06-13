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
class HallOfCombatMastery(MetroidPrime2Region):
    name = "Hall of Combat Mastery"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Central Area Transport East",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_use_spider_ball(state, player),
                    # https://www.youtube.com/watch?v=ycwAO4nX0dE
                    condition_and([
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Instant Morph"),
                        has_trick_enabled(state, player, "Slope Jump"),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player),
                        has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                        condition_or([
                            # https://www.youtube.com/watch?v=BnCRXrOvPGs
                            has_trick_enabled(state, player, "Slope Jump"),
                            # https://www.youtube.com/watch?v=FtylAcZbKFA
                            has_trick_enabled(state, player, "Standable Terrain"),
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=PO2iuLTh2iw
                    condition_and([
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Space Jump"),
                        has_trick_enabled(state, player, "Instant Morph"),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Agon Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Sanctuary Fortress - Hall of Combat Mastery | Event - Hall of Combat Mastery Glass Tunnel", player),
        ),
        MetroidPrime2Exit(
            destination="P|Ing Hive - Culling Chamber",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Minigyro Chamber",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_lay_bomb(state, player),
                        can_use_spider_ball(state, player),
                        condition_or([
                            condition_or([can_use_dark_beam(state, player), can_use_light_beam(state, player), can_use_annihilator_beam(state, player), has_missile_count(state, player, 5)]),
                            state.has("Sanctuary Fortress - Dynamo Works | Event - Spider Guardian", player),
                        ]),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            condition_and([
                                can_use_screw_attack(state, player),
                                has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                            ]),
                            # https://www.youtube.com/watch?v=nVzQ88rAXTQ
                            condition_and([
                                state.has("Space Jump Boots", player),
                                has_trick_enabled(state, player, "Instant Morph"),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
                condition_and([
                state.has("Morph Ball", player),
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Knowledge"),
                        can_use_boost_ball(state, player),
                        has_trick_enabled(state, player, "Wall Boost"),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Hall of Combat Mastery Glass Tunnel",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Hall of Combat Mastery | Event - Hall of Combat Mastery Glass Tunnel",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Sanctuary Fortress - Hall of Combat Mastery | Event - Hall of Combat Mastery Glass Tunnel", player),
                condition_and([
                state.has("Morph Ball", player),
                can_lay_pb(state, player),
            ]),
            ]),
        )
