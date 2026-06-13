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


class DarkTorvusArena(MetroidPrime2Region):
    name = "Dark Torvus Arena"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Dark Arena Tunnel",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Boost Ball)",
            can_access=lambda state, player: condition_and([
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                state.has("Dark Torvus Bog - Dark Torvus Arena | Event - Boost Guardian", player),
            ]),
        )

        self.add_location(
            name="Pickup (Dark Torvus Key 1)",
            can_access=lambda state, player: condition_and([
                condition_or([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        has_dark_suit(state, player),
                        has_light_suit(state, player),
                        state.count("Energy Tank", player) >= 1,
                    ]),
                ]),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=RlvAvH4_w1g
                    condition_and([
                        state.has("Morph Ball", player),
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Roll Jump"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        has_trick_enabled(state, player, "Standable Terrain"),
                    ]),
                    # https://www.youtube.com/watch?v=0k8JzNxnZLw
                    condition_and([
                        state.has("Scan Visor", player),
                        state.has("Space Jump Boots", player),
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Boost Guardian",
            locked_item=MetroidPrime2Item(
                name="Dark Torvus Bog - Dark Torvus Arena | Event - Boost Guardian",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
                state.has("Morph Ball", player),
                condition_or([
                    condition_and([
                        can_lay_bomb(state, player),
                        condition_or([has_dark_suit(state, player), has_light_suit(state, player)]),
                        can_use_light_beam(state, player),
                        has_light_ammo(state, player, 50),
                        state.has("Charge Beam", player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Combat"),
                        can_lay_pb(state, player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    condition_and([
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Combat"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                        state.has("Charge Beam", player),
                    ]),
                ]),
            ]),
        )
