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
class AgonEnergyController(MetroidPrime2Region):
    name = "Agon Energy Controller"
    exits_ = [
        MetroidPrime2Exit(
            destination="Agon Wastes - Controller Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sanctuary Fortress - Sanctuary Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item", player),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item", player),
        ),
        MetroidPrime2Exit(
            destination="Great Temple - Main Energy Controller",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Great Temple - Main Energy Controller | Can Pick Up Light Suit Item", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Amber Translator)",
            can_access=lambda state, player: True,
        )

        self.add_location(
            name="Event - Agon Energy Returned",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Agon Energy Controller | Event - Agon Energy Returned",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Dark Agon Wastes - Dark Agon Energy Controller | Event - Dark Agon Energy Taken", player),
        )

        self.add_location(
            name="Event - Agon Energy Controller Pickup",
            locked_item=MetroidPrime2Item(
                name="Agon Wastes - Agon Energy Controller | Event - Agon Energy Controller Pickup",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True,
        )
