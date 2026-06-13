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
class Vault(MetroidPrime2Region):
    name = "Vault"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Grand Abyss",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Ing Hive - Vault Attack Portal",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                state.has("Sanctuary Fortress - Vault | Event - Vault Bridge", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="P|Ing Hive - Vault Attack Portal",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                condition_and([
                state.has("Morph Ball", player),
                can_use_boost_ball(state, player),
                condition_or([
                    can_use_screw_attack(state, player),
                    # Scan Dash -> https://www.youtube.com/watch?v=1uWwpO7IHtk
                    condition_and([
                        state.has("Space Jump Boots", player),
                        state.has("Scan Visor", player),
                        # Extended Dash -> https://www.youtube.com/watch?v=WU-uQkzCycA
                        condition_or([
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                            has_trick_enabled(state, player, "Extended Dash"),
                        ]),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                    ]),
                    # Boost Jump -> https://youtu.be/slAxhRMksBk
                    condition_and([
                        has_trick_enabled(state, player, "Boost Jump"),
                        has_trick_enabled(state, player, "Terminal Fall Abuse"),
                    ]),
                ]),
            ]),
                condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    state.has("Scan Visor", player),
                    has_trick_enabled(state, player, "Terminal Fall Abuse"),
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                ]),
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                    not (False),
                ]),
            ]),
            ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Screw Attack)",
            can_access=lambda state, player: condition_and([
                not (state.has("Sanctuary Fortress - Vault | Event - Vault Bridge", player)),
                condition_and([
                state.has("Sanctuary Fortress - Vault | Event - Vault Bomb Slot", player),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                    ]),
                ]),
            ]),
            ]),
        )

        self.add_location(
            name="Event - Vault Bridge",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Vault | Event - Vault Bridge",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player),
        )

        self.add_location(
            name="Event - Vault Spinners",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Vault | Event - Vault Spinners",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Morph Ball", player),
                can_use_boost_ball(state, player),
                condition_or([
                    can_use_screw_attack(state, player),
                    # Scan Dash -> https://www.youtube.com/watch?v=1uWwpO7IHtk
                    condition_and([
                        state.has("Space Jump Boots", player),
                        state.has("Scan Visor", player),
                        # Extended Dash -> https://www.youtube.com/watch?v=WU-uQkzCycA
                        condition_or([
                            has_trick_enabled(state, player, "Combat/Scan Dash"),
                            has_trick_enabled(state, player, "Extended Dash"),
                        ]),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                    ]),
                    # Boost Jump -> https://youtu.be/slAxhRMksBk
                    condition_and([
                        has_trick_enabled(state, player, "Boost Jump"),
                        has_trick_enabled(state, player, "Terminal Fall Abuse"),
                    ]),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Vault Bomb Slot",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Vault | Event - Vault Bomb Slot",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                condition_and([
                state.has("Sanctuary Fortress - Vault | Event - Vault Bridge", player),
                condition_and([
                state.has("Sanctuary Fortress - Vault | Event - Vault Bridge", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                        has_trick_enabled(state, player, "Bomb Jump"),
                    ]),
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Movement"),
                    ]),
                ]),
            ]),
            ]),
                condition_and([
                state.has("Sanctuary Fortress - Vault | Event - Vault Spinners", player),
                condition_or([
                    condition_and([
                        state.has("Morph Ball", player),
                        can_lay_bomb(state, player),
                    ]),
                    # https://www.youtube.com/watch?v=rZOFeOuPkRA
                    condition_and([
                        condition_and([state.has('Morph Ball', player), can_lay_bomb(state, player)]),
                        has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                        has_trick_enabled(state, player, "Instant Morph"),
                    ]),
                ]),
            ]),
            ]),
        )
