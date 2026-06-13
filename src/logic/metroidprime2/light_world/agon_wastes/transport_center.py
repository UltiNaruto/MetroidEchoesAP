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
class TransportCenter(MetroidPrime2Region):
    name = "Transport Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Agon Wastes - Crossroads",
            door=DoorCover.Opened,
            rule=lambda state, player: can_activate_dark_portal(state, player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Save Station A",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Agon Wastes - Transport Center | Event - Transport Center Gate", player),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Transport to Torvus Bog",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                # https://www.youtube.com/watch?v=fjjsnAXoaIc
                condition_and([
                    can_use_screw_attack(state, player, z_axis=True),
                    has_trick_enabled(state, player, "Movement"),
                ]),
                # https://www.youtube.com/watch?v=F1MFnqIj9gg
                condition_and([
                    has_trick_enabled(state, player, "Combat/Scan Dash"),
                    state.has("Scan Visor", player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Agon Wastes - Portal Terminal",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: state.has("Agon Wastes - Transport Center | Event - Transport Center Gate", player),
        )

        self.add_location(
            name="Event - Transport Center Gate",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Transport Center | Event - Transport Center Gate",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
                condition_and([
                    state.has("Morph Ball", player),
                    can_lay_bomb(state, player),
                ]),
                # https://www.youtube.com/watch?v=kX1HXF_BCew
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Bomb Slot without Bombs"),
                ]),
            ]),
        )
