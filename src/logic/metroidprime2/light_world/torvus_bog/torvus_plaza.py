from BaseClasses import MultiWorld, ItemClassification
from ... import has_trick_enabled, can_lay_bomb, can_use_boost_ball, can_use_spider_ball, can_use_screw_attack
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and

# tricks:
# "Torvus Bog - Torvus Plaza | STE SA to Item",
# "Torvus Bog - Torvus Plaza | Boost-only/Cannonball",
# "Torvus Bog - Torvus Plaza | BSJ to Entrance",


class TorvusPlaza_Entrance(MetroidPrime2Region):
    """The ledge that contains the door. Overlooks the half-pipe."""
    name = "Torvus Plaza"
    desc="Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Half-Pipe)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Spider Track)",
            rule=lambda state, player: condition_or([
                # normal conditions
                condition_and([
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player)
                ]),
                # using SA
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | STE SA to Item")
                ]),
                # using Boost
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Boost-only/Cannonball")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Torvus Plaza Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
    ]


class TorvusPlaza_HalfPipe(MetroidPrime2Region):
    """The half-pipe. Use the boost to get through! Also contains the raised area leading up to a sealed hole where an
    arena is in Dark Aether."""
    name = "Torvus Plaza"
    desc = "Half-Pipe"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Entrance)",
            rule=lambda state, player: condition_or([
                can_use_boost_ball(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Instant Unmorph BSJ to Entrance"),
                    can_lay_bomb(state, player)
                ]),
                can_use_screw_attack(state, player) # you can screw from the back of the room to the middle of the entrance ledge easily
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Spider Track)",
            rule = lambda state, player: condition_and([
                can_use_boost_ball(state, player),
                condition_or([
                    can_use_spider_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Boost-only/Cannonball")
                ])
            ])
        )
    ]


class TorvusPlaza_SpiderTrack(MetroidPrime2Region):
    """The section of spider track ending before the Sporb. Also includes the area in the back of the room with a standable tree."""
    name = "Torvus Plaza"
    desc="Spider Track"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True #you can simply just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Spider Challenge)",
            rule=lambda state, player: condition_or([
                condition_and([
                    can_lay_bomb(state, player),
                    can_use_spider_ball(state, player)
                    # boost makes it easier but isn't required for the expected path
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | STE SA to Item")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Item Ledge)",
            rule=lambda state, player: condition_and([
                #boost-only requires BSJ
                has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Boost-only/Cannonball"),
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player)
            ])
        )
    ]


class TorvusPlaza_SpiderChallenge(MetroidPrime2Region):
    """The more difficult sections of the track, including the area covered by the Sporb as well as the parts with rotating
    and moving elements. Leads all the way to the ledge containing the Kinetic Orb Cannon."""
    name = "Torvus Plaza"
    desc="Spider Challenge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Entrance)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Spider Track)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Cannon Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Item Ledge)",
            rule=lambda state, player: condition_or([
                can_use_screw_attack(state, player),
                can_use_spider_ball(state, player)
            ])
        ),
    ]


class TorvusPlaza_CannonLedge(MetroidPrime2Region):
    """Contains a Kinetic Orb Cannon leading to the item ledge."""
    name = "Torvus Plaza"
    desc="Cannon Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Entrance)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Item Ledge)",
            rule=lambda state, player: True  # the cannon is already activated
        ),
    ]


class TorvusPlaza_ItemLedge(MetroidPrime2Region):
    """Contains a pickup. Is the highest point in the room."""
    name = "Torvus Plaza"
    desc="Item Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Energy Tank)",
            can_access=lambda state, player: True
        )
