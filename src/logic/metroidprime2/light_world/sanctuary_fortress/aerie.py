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
class Aerie(MetroidPrime2Region):
    name = "Aerie"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Ing Hive - Hive Summit",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                state.has("Sanctuary Fortress - Aerie | Event - Dark Samus 2", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Aerie Access",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Aerie Transport Station",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Sanctuary Fortress - Aerie | Event - Dark Samus 2", player),
                condition_and([
                state.has("Echo Visor", player),
                state.has("Sanctuary Fortress - Aerie | Event - Aerie Pickup", player),
            ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Echo Visor)",
            can_access=lambda state, player: condition_or([
                # Normal route: elevator unlocks after Dark Samus 2 fight
                state.has("Sanctuary Fortress - Aerie | Event - Dark Samus 2", player),
                # https://www.youtube.com/watch?v=29qB37vxSgY — skip route via tricks
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Bomb Space Jump"),
                    has_trick_enabled(state, player, "Movement"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        )

        self.add_location(
            name="Event - Dark Samus 2",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Aerie | Event - Dark Samus 2",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
                condition_or([
                        state.has("Dark Visor", player),
                        condition_and([
                            state.has("Echo Visor", player),
                            has_trick_enabled(state, player, "Combat"),
                        ]),
                    ]),
                has_trick_enabled(state, player, "Invisible Objects"),
            ]),
        )

        self.add_location(
            name="Event - Aerie Pickup",
            locked_item=MetroidPrime2Item(
                name="Sanctuary Fortress - Aerie | Event - Aerie Pickup",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_and([
                state.has("Sanctuary Fortress - Aerie | Event - Dark Samus 2", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    # https://www.youtube.com/watch?v=su_5kgsXU8Y
                    condition_and([
                        has_trick_enabled(state, player, "Combat/Scan Dash"),
                        state.has("Scan Visor", player),
                    ]),
                    # https://www.youtube.com/watch?v=gt_lKlVVr28
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Movement"),
                    ]),
                ]),
                state.has("Echo Visor", player),
            ]),
        )
