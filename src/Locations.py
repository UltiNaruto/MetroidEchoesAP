from typing import Callable, Optional

from BaseClasses import CollectionState, Location, Region
from .Items import MetroidPrime2Item
from .Utils import strip_description_from_region_name


class MetroidPrime2Location(Location):
    game: str = "Metroid Prime 2 Echoes"

    def __init__(self, name: str, can_access: Callable[[CollectionState, int], bool], parent: Region, locked_item: Optional[MetroidPrime2Item]=None):
        loc_name = f"{strip_description_from_region_name(parent.name)} - {name}"
        if loc_name not in parent.multiworld.worlds[parent.player].location_name_to_id:
            idx = None
        else:
            idx = parent.multiworld.worlds[parent.player].location_name_to_id[loc_name]

        super().__init__(parent.player, f"{strip_description_from_region_name(parent.name)} - {name}", idx, parent)

        if locked_item is not None:
            locked_item.location = self
            self.place_locked_item(locked_item)
        # No can_access or access_rule override: accessibility is enforced entirely
        # through region exit rules (DoorCover types + rule lambdas in each room file).
        # This lets fill_restrictive place all progression items without deadlocking
        # on location-level circular dependencies.
