from typing import Callable, Optional

from BaseClasses import CollectionState, Region, MultiWorld
from .Enums import DoorCover


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
