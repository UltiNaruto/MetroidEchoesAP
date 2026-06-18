"""This room is most notable for being where the Alpha Blogg fight takes place. It has a large fan contraption that gets
destroyed during the boss cutscene."""

from BaseClasses import MultiWorld, ItemClassification
from ... import (
    can_activate_dark_portal,
    can_defeat_alpha_blogg,
    can_lay_bomb,
    can_use_spider_ball,
    has_trick_enabled
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


# tricks:
# Alpha Blogg Skip:
# - Get onto the first platform from the bottom with a Bomb Space Jump, then fly over to the upper door using Grav Boost.
# - https://youtu.be/OSnzyN6ZFR0

# BSJ to skip Spider Track:
# - The track is standable, but you must Bomb Space Jump to get onto it.
# - https://youtu.be/KPs8MIRVY-I

# Climb to Top Post-Alpha Blogg (NSJ):
# - The last jump requires an instant unmorph after rolling off the second platform from the bottom.
# - https://www.youtube.com/watch?v=tDa-PxtRTzo


class MainHydrochamber_Top(MetroidPrime2Region):
    """The ledge containing the exit door."""
    name = "Main Hydrochamber"
    desc="Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrochamber Shaft (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Main)",
            rule=lambda state, player: True
        ),
    ]


class MainHydrochamber_Main(MetroidPrime2Region):
    """Most of the room. Contains the fan platforms that are accessible after the boss battle."""
    name = "Main Hydrochamber"
    desc="Main"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Spider Track)",
            rule=lambda state, player: state.has("Torvus Bog - Main HydroChamber | Alpha Blogg Dead", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Top)",
            # options: main (has grav boost or has beaten boss)
            rule=lambda state, player: condition_or([
                # boss is dead
                condition_and([
                    state.has("Gravity Boost", player),
                    condition_or([
                        condition_and([
                            state.has('Space Jump Boots', player), # vanilla strats
                            state.has("Torvus Bog - Main HydroChamber | Alpha Blogg Dead", player)
                        ]),
                        condition_and([ # instant unmorph strats
                            has_trick_enabled(
                                state,
                                player,
                                "Torvus Bog - Main Hydrochamber | Climb to Top Post-Alpha Blogg (NSJ)"
                            ),
                            state.has('Morph Ball', player),
                        ])
                    ])
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Main Hydrochamber | Alpha Blogg Skip"),
                    state.has('Gravity Boost', player),
                    can_lay_bomb(state, player),
                    state.has('Space Jump Boots', player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Lower Door)",
            rule=lambda state, player: True
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Alpha Blogg Dead",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Main Hydrochamber | Alpha Blogg Dead",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_defeat_alpha_blogg(state, player)
        )


class MainHydrochamber_LowerDoor(MetroidPrime2Region):
    """Leads to Hydrochamber Storage. Gets blocked off by the rotating room during the boss fight."""
    name = "Main Hydrochamber"
    desc="Lower Door"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Main)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrochamber Storage",
            rule=lambda state, player: state.has("Torvus Bog - Main HydroChamber | Alpha Blogg Dead", player)
        ),
    ]


class MainHydrochamber_SpiderTrack(MetroidPrime2Region):
    """Leads to a Dark Portal. Gets blocked off by the rotating room during the boss fight."""
    name = "Main Hydrochamber"
    desc="Spider Track"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Portal Ledge)",
            rule=lambda state, player: condition_or([
                can_use_spider_ball(state, player),
                condition_and([
                    can_lay_bomb(state, player),
                    state.has('Space Jump Boots', player),
                    has_trick_enabled(state, player, "Torvus Bog - Main Hydrochamber | BSJ to skip Spider Track")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Main)",
            rule=lambda state, player: True
        ),
    ]


class MainHydrochamber_PortalLedge(MetroidPrime2Region):
    """Accessible via the Spider track. Connects to Dark Aether."""
    name = "Main Hydrochamber"
    desc="Portal Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Undertemple (Portal Ledge)",
            rule=lambda state, player: can_activate_dark_portal(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Main)",
            rule=lambda state, player: True
        ),
    ]
