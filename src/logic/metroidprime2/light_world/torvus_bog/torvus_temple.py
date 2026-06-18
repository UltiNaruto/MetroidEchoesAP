"""Best known for having a protracted Pirate battle. This is where Samus obtains Super Missile in vanilla. Has an elevator
that connects its above-ground and underground sections that requires the Emerald Translator."""

from BaseClasses import MultiWorld, ItemClassification
from ... import can_use_screw_attack, can_use_seeker_launcher, has_missile_count, has_trick_enabled
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


class TorvusTemple_Arena(MetroidPrime2Region):
    """Where the Pirate battle takes place. The elevators become accessible after the pirates have been killed."""
    name = "Torvus Temple"
    desc="Arena"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bug - Plaza Access (Upper)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple | Item Collected", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Upper)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple | Pirates Dead", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pirates Dead",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Torvus Temple | Pirates Dead",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True
        )
        self.add_location(
            name="Item Collected",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Torvus Temple | Item Collected",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True
        )
        self.add_location(
            name="Pickup (Super Missile)",
            can_access=lambda state, player: True
        )


class TorvusTemple_Underground(MetroidPrime2Region):
    """The area that the central elevator brings Samus to. Contains paths back into upper Torvus, a Seeker path to Agon,
    and an elevator path to lower Torvus."""
    name = "Torvus Temple"
    desc="Underground"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Access (Lower Torvus Temple Entrance)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transport to Agon Wastes",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                can_use_seeker_launcher(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Temple | Seeker Skip"),
                    has_missile_count(state, player, 2),
                    can_use_screw_attack(state, player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Tunnel (Tunnel)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground Transport Entrance)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        # MetroidPrime2Exit(
        #     destination="Torvus Bog - Torvus Temple (Out of Bounds)",
        #     rule=lambda state, player: condition_and([
        #         has_oob_kit(state, player),
        #         has_trick_enabled(state, player, "Torvus Bog - Torvus Temple | Out of Bounds")
        #     ])
        # )
    ]


class TorvusTemple_UndergroundTransportEntrance(MetroidPrime2Region):
    """Leads to/from lower Torvus. The barrier that covers the elevator to the uppermost ledge extends down to cover the door here too."""
    name = "Torvus Temple"
    desc="Underground Transport Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Upper)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple | Pirates Dead", player)
            # the laser barrier preventing access to the Super Missiles also blocks the lower tunnel
        )
    ]


class TorvusTemple_Upper(MetroidPrime2Region):
    """The uppermost ledge, reached via the blocked elevator. Has a door that leads to Controller Access."""
    name = "Torvus Temple"
    desc="Upper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Arena)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Controller Access",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True
        )
    ]


# class TorvusTemple_OutOfBounds(MetroidPrime2Region):
#     name = "Torvus Temple"
#     desc = "Out of Bounds"
#     exits_ = [
#         MetroidPrime2Exit(
#             destination="Torvus Bog - Torvus Temple (Arena)",
#             rule=lambda state, player: True
#         ),
#         MetroidPrime2Exit(
#             destination="Torvus Bog - Transport to Agon Wastes",
#             rule=lambda state, player: True
#         ),
#         MetroidPrime2Exit(
#             destination="Torvus Bog - Torvus Temple (Underground)",
#             rule=lambda state, player: True
#         ),
#     ]
