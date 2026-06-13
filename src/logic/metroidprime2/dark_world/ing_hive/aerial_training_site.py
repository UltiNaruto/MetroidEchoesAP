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
class AerialTrainingSite(MetroidPrime2Region):
    name = "Aerial Training Site"
    exits_ = [
        MetroidPrime2Exit(
            destination="Ing Hive - Judgment Drop",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="P|Sanctuary Fortress - Watch Station",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                can_activate_dark_portal(state, player),
                condition_and([
                # https://youtu.be/wPLKS7hOhrE?si=ojCi7x8Vw6K49bUM&t=24
            condition_and([
                state.has("Scan Visor", player),
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Slope Jump"),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                state.has("Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_and([
                state.has("Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    # Works the same as -> https://www.youtube.com/watch?v=Bi3Ap-JiotU
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                # https://youtu.be/wPLKS7hOhrE?si=ojCi7x8Vw6K49bUM&t=24
            condition_and([
                state.has("Scan Visor", player),
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Slope Jump"),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                state.has("Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_and([
                state.has("Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier", player),
                condition_or([
                    condition_and([
                        can_use_screw_attack(state, player),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                    # https://www.youtube.com/watch?v=Bi3Ap-JiotU
                    condition_and([
                        can_use_screw_attack(state, player, z_axis=True),
                        has_trick_enabled(state, player, "Standable Terrain"),
                        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
                        not (False),
                        condition_or([
                            has_dark_suit(state, player),
                            has_light_suit(state, player),
                            state.count("Energy Tank", player) >= 1,
                        ]),
                    ]),
                ]),
            ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Central Hive West Transport",
            door=DoorCover.Any,
            rule=lambda state, player: # https://youtu.be/wPLKS7hOhrE?si=ojCi7x8Vw6K49bUM&t=24
            condition_and([
                state.has("Scan Visor", player),
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Slope Jump"),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                state.has("Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Ing Hive Key 3)",
            can_access=lambda state, player: condition_and([
                # https://youtu.be/wPLKS7hOhrE?si=ojCi7x8Vw6K49bUM&t=24
            condition_and([
                state.has("Scan Visor", player),
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Slope Jump"),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                state.has("Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier", player),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
                condition_or([
                has_dark_suit(state, player),
                has_light_suit(state, player),
                state.count("Energy Tank", player) >= 1,
            ]),
            ]),
        )

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: # https://www.youtube.com/watch?v=wPLKS7hOhrE
            condition_and([
                state.has("Space Jump Boots", player),
                state.has("Morph Ball", player),
                has_trick_enabled(state, player, "Roll Jump"),
                has_trick_enabled(state, player, "Standable Terrain"),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
        )

        self.add_location(
            name="Event - Aerial Training Site Barrier",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: # https://www.youtube.com/watch?v=wPLKS7hOhrE&t=23s
            condition_and([
                state.has("Scan Visor", player),
                state.has("Space Jump Boots", player),
                has_trick_enabled(state, player, "Combat/Scan Dash"),
                has_trick_enabled(state, player, "Slope Jump"),
                not (state.has("Ing Hive - Aerial Training Site | Event - Aerial Training Site Barrier", player)),
                condition_or([
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                    state.count("Energy Tank", player) >= 1,
                ]),
            ]),
        )
