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
class ReactorCore(MetroidPrime2Region):
    name = "Reactor Core"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Minigyro Chamber",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                    state.has("Sanctuary Fortress - Reactor Core | Event - Reactor Core Quad", player),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_spider_ball(state, player),
                                    condition_or([
                                        has_trick_enabled(state, player, "Movement"),
                                        can_use_boost_ball(state, player),
                                    ]),
                                ]),
                                # https://www.youtube.com/watch?v=3JCa2JxsH7U
                                condition_and([
                                    can_lay_bomb(state, player),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Save Station A",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Sanctuary Fortress - Reactor Core | Event - Reactor Core Quad", player),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Sanctuary Map Station",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Reactor Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Transit Station",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: condition_and([
                    state.has("Sanctuary Fortress - Reactor Core | Event - Reactor Core Quad", player),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_spider_ball(state, player),
                                    condition_or([
                                        has_trick_enabled(state, player, "Movement"),
                                        can_use_boost_ball(state, player),
                                    ]),
                                ]),
                                # https://www.youtube.com/watch?v=3JCa2JxsH7U
                                condition_and([
                                    can_lay_bomb(state, player),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Energy Tank)",
            can_access=lambda state, player: condition_and([
                condition_and([
                    state.has("Sanctuary Fortress - Reactor Core | Event - Reactor Core Quad", player),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            state.has("Morph Ball", player),
                            condition_or([
                                condition_and([
                                    can_use_spider_ball(state, player),
                                    condition_or([
                                        has_trick_enabled(state, player, "Movement"),
                                        can_use_boost_ball(state, player),
                                    ]),
                                ]),
                                # https://www.youtube.com/watch?v=3JCa2JxsH7U
                                condition_and([
                                    can_lay_bomb(state, player),
                                    has_trick_enabled(state, player, "Bomb Space Jump"),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_or([
                        condition_and([
                            can_use_spider_ball(state, player),
                            condition_or([
                                can_use_boost_ball(state, player),
                                condition_or([
                                    condition_and([
                                        state.has("Space Jump Boots", player),
                                        condition_and([
                                            can_use_screw_attack(state, player),
                                            has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                                        ]),
                                    ]),
                                    # https://www.youtube.com/watch?v=vguGiUrLkUA
                                    condition_and([
                                        can_lay_bomb(state, player),
                                        has_trick_enabled(state, player, "Bomb Jump"),
                                        has_trick_enabled(state, player, "Standable Terrain"),
                                    ]),
                                ]),
                            ]),
                        ]),
                        condition_and([
                            has_trick_enabled(state, player, "Standable Terrain"),
                            condition_or([
                                condition_and([
                                    can_use_screw_attack(state, player),
                                    has_trick_enabled(state, player, "Screw Attack into Tunnels/Openings"),
                                ]),
                                condition_and([
                                    state.has("Space Jump Boots", player),
                                    condition_or([
                                        condition_and([
                                            can_lay_bomb(state, player),
                                            has_trick_enabled(state, player, "Bomb Space Jump"),
                                        ]),
                                        # https://www.youtube.com/watch?v=LyIhjAc4pqM
                                        condition_and([
                                            state.has("Sanctuary Fortress - Reactor Core | Event - Reactor Core Quad", player),
                                            has_trick_enabled(state, player, "Jump Off Enemy"),
                                        ]),
                                        # https://clips.twitch.tv/GenerousComfortablePassionfruitDerp
                                        has_trick_enabled(state, player, "Movement"),
                                    ]),
                                ]),
                            ]),
                        ]),
                        # https://www.twitch.tv/dyceron/clip/TemperedScrumptiousCucumberFloof-JUhNr_ZvHlc_ppZL
                        condition_and([
                            state.has("Sanctuary Fortress - Reactor Core | Event - Reactor Core Quad", player),
                            can_lay_bomb(state, player),
                            has_trick_enabled(state, player, "Bomb Space Jump"),
                            has_trick_enabled(state, player, "Jump Off Enemy"),
                            has_trick_enabled(state, player, "Standable Terrain"),
                            has_trick_enabled(state, player, "Movement"),
                        ]),
                    ]),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Reactor Core Quad",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Reactor Core | Event - Reactor Core Quad",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([can_use_dark_beam(state, player), can_use_light_beam(state, player), can_use_annihilator_beam(state, player), has_missile_count(state, player, 5)]),
        )
