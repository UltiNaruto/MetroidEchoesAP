from typing import Callable, Optional, TYPE_CHECKING

from .Enums import DoorCover
from .Locations import MetroidPrime2Location

from BaseClasses import CollectionState, Region, MultiWorld

if TYPE_CHECKING:
    from .Items import MetroidPrime2Item


class MetroidPrime2Exit:
    door: DoorCover
    destination: Optional[str]
    rule: Callable[[CollectionState, int], bool]

    def __init__(self, rule: Callable[[CollectionState, int], bool], door: DoorCover=DoorCover.Opened, destination: Optional[str]=None):
        self.door = door
        self.rule = rule
        self.destination = destination


class MetroidPrime2Region(Region):
    desc: str = ""
    exits_: list[MetroidPrime2Exit] = {}

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        if self.desc != "":
            super().__init__(f"{region_name} - {self.name} ({self.desc})", player, multiworld)
        else:
            super().__init__(f"{region_name} - {self.name}", player, multiworld)

    def add_location(self, name: str, can_access: Callable[[CollectionState, int], bool], locked_item: Optional["MetroidPrime2Item"]=None):
        self.locations += [
            MetroidPrime2Location(
                name,
                can_access,
                self,
                locked_item,
            ),
        ]