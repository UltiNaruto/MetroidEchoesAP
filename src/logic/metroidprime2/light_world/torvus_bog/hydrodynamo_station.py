"""A the hub room of the lower level of Torvus. A large portion of this room is underwater.Has many doors to enter and things to scan.
The bottom raises up once all three panels are scanned, revealing a door."""

from BaseClasses import MultiWorld, ItemClassification
from ... import (
    has_trick_enabled,
    can_lay_bomb,
    has_missile_count,
    hydrodynamo_station_has_scanned_panels,
    underwater_movement)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

# tricks in this room:
# "Torvus Bog - Hydrodynamo Station | Boost Jump"
# - Cross gaps using the speed and momentum of a boost ball while underwater. Requires good unmorph timing to get an instant unmorph.
# - https://youtu.be/7I2Jl824CMI

# "Torvus Bog - Hydrodynamo Station | Underwater Dash"
# - Dash while entering the water, preserving your momentum by taking advantage of the underwater physics.
# - https://youtu.be/IUcPDkHKd0I
# - https://youtu.be/nY4U_0Uyn0M

# "Torvus Bog - Hydrodynamo Station | Air Underwater"
# - Trick the game into thinking you are not in the water when you are. This allows for standard movement.
# - You can activate Air Underwater by causing a camera transition while entering the water. This is almost always done by morphing.
# - https://youtu.be/g7DeBeDMpeU

# "Torvus Bog - Hydrodynamo Station | Seeker Skip"
# - Break the Seeker locks using Missiles and Screw Attack.
# - Requires Air Underwater since you can't Screw Attack underwater normally.
# - https://youtu.be/ALjnm411Ldk

class HydrodynamoStation_AboveWater(MetroidPrime2Region):
    """Contains the entrance to Underground Transport, plus some rotating platforms that can be jumped
    on to reach the top. Puffer enemies in the air can menace Samus while she navigates the platforms."""
    name="Hydrodynamo Station"
    desc="Above Water"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Lower)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: True
        ),
    ]


class HydrodynamoStation_Top(MetroidPrime2Region):
    """The Kinetic Orb launcher in the center of the room launches you to the top of the tower. Samus can break a Missile
    door cover to reach Save Station B and Samus can jump down to reach the rest of the room."""
    name="Hydrodynamo Station"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top Door Ledge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: True
        ),
    ]


class HydrodynamoStation_TopDoorLedge(MetroidPrime2Region):
    """The ledge containing the door to Save Station B. The door has a Missile cover."""
    name="Hydrodynamo Station"
    desc = "Top Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Save Station B",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
    ]


class HydrodynamoStation_ThreeDoors(MetroidPrime2Region):
    """The first underwater section of the room, contains ledges with doors leading to Gathering Hall, Training Chamber, and
    Catacombs. The ledges in front of each door are their own subregions"""
    name="Hydrodynamo Station"
    desc = "Three Doors"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            rule=lambda state, player: condition_or([
                    state.has("Gravity Boost", player),
                    condition_and([
                        state.has("Torvus Bog - Hydrodynamo Station | Scanned North Panel", player),
                        condition_or([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player)
                    ]),
                ])
            ])
        ), # summary: if you have gravity boost, you're fine. If you have scanned the panel and can either DBJ or
             # have SJB, you're fine
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (West Door Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Torvus Bog - Hydrodynamo Station | Scanned West Panel", player),
                    condition_or([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player)
                    ]),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (East Door Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Torvus Bog - Hydrodynamo Station | Scanned East Panel", player),
                    condition_or([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player)
                    ]),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Scan Ledge)",
            rule=lambda state, player: True
        )
    ]


class HydrodynamoStation_NorthDoorLedge(MetroidPrime2Region):
    """Contains a door leading to Training Access, which is blocked by a Seeker Cover."""
    name="Hydrodynamo Station"
    desc = "North Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                state.has("Space Jump Boots", player),
                state.has("Torvus Bog - Hydrodynamo Station | Scanned North Panel", player)
            ])  # this jump is very tight; it's doable with nothing, but I think that's unlikely for most players
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Scan Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Access (South)",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Seeker Missile Launcher", player),
                    has_missile_count(state, player, 6)
                ]),
                condition_and([
                    has_missile_count(state, player, 5),
                    state.has("Screw Attack", player),
                    has_trick_enabled(state, player, "Torvus Bog - Hydrodynamo Station | Air Underwater"),
                    # air underwater is needed for seeker skip here because that's the only way to use Screw Attack underwater
                    has_trick_enabled(state, player, "Torvus Bog - Hydrodynamo Station | Seeker Skip")
                ])
            ])
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )


class HydrodynamoStation_WestDoorLedge(MetroidPrime2Region):
    """Has a scan panel and a white door leading to Gathering Access."""
    name="Hydrodynamo Station"
    desc = "West Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                state.has("Space Jump Boots", player),
                state.has("Torvus Bog - Hydrodynamo Station | Scanned West Panel", player)
            ]) #this jump is very tight; it's doable with nothing, but I think that's unlikely for most players
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (East Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Access (East)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Scanned West Panel",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Hydrodynamo Station | Scanned West Panel",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player)
        )


class HydrodynamoStation_EastDoorLedge(MetroidPrime2Region):
    """Ledge with a scan panel and a dark door leading to Catacombs Access."""
    name="Hydrodynamo Station"
    desc = "East Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                state.has("Space Jump Boots", player),
                state.has("Torvus Bog - Hydrodynamo Station | Scanned East Panel", player)
            ])  # this jump is very tight; it's doable with nothing, but I think that's unlikely for most players
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (West Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (West)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Scanned East Panel",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Hydrodynamo Station | Scanned East Panel",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player)
        )


class HydrodynamoStation_NorthScanLedge(MetroidPrime2Region):
    """Contains the northern scan panel. You would need to fall down from Three Doors to reach this."""
    name="Hydrodynamo Station"
    desc="North Scan Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True  # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Scanned North Panel",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Hydrodynamo Station | Scanned North Panel",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: state.has("Scan Visor", player)
        )


class HydrodynamoStation_AboveMovableBase(MetroidPrime2Region):
    """Made smaller when the base below moves up. Also contains the Kinetic Orb Cannon, but the
    cannon can't be logically relevant because it becomes inoperable after raising the movable base."""
    name="Hydrodynamo Station"
    desc = "Above Movable Base"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Under Movable Base)",
            rule=lambda state, player: hydrodynamo_station_has_scanned_panels(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        )
    ]


class HydrodynamoStation_UnderMovableBase(MetroidPrime2Region):
    """Opened by scanning all three panels in the underwater section of the room."""
    name="Hydrodynamo Station"
    desc = "Under Movable Base"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: hydrodynamo_station_has_scanned_panels(state, player)
        ),
    ]
